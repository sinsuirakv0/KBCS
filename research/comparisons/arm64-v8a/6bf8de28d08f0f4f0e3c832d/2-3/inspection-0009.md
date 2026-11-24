# v16.0.2 → v16.0.3 · 要調査の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-663165681dcf98e6d5f835c2ee5cbe57"></a>

### [`00520bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520bfc.md) → [`00520f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f1c.md) FUN_00520f1c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00520c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520bfc.md#insn-00520c18) · [`00520c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520bfc.md#insn-00520c38)
- 新版 [`00520f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f1c.md#insn-00520f38) · [`00520f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f1c.md#insn-00520f58)

~~~diff
- 00520c18 ["INT_ADD", "register:40f0:8", ["const:520c18:8", "const:4:8"]]
- 00520c18 ["CALL", null, ["callee:00c54d90:8"]]
+ 00520f38 ["INT_ADD", "register:40f0:8", ["const:520f38:8", "const:4:8"]]
+ 00520f38 ["CALL", null, ["callee:00c54d90:8"]]
- 00520c18 bytes 62cc1c94
+ 00520f38 bytes 96cf1c94
- 00520c38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00520c38 ["INT_ADD", "register:40f0:8", ["const:520c38:8", "const:4:8"]]
- 00520c38 ["CALLIND", null, ["register:0:8"]]
+ 00520f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00520f58 ["INT_ADD", "register:40f0:8", ["const:520f58:8", "const:4:8"]]
+ 00520f58 ["CALLIND", null, ["register:0:8"]]
- 00520c38 bytes 00013fd6
+ 00520f58 bytes 00013fd6
~~~


<a id="compare-eaf6c56c3c4db6565e47c41c25996fb4"></a>

### [`00522868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522868.md) → [`00522b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522b88.md) FUN_00522b88

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054d4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d4e4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054d804.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522868.md#insn-00522884)
- 新版 [`00522ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522b88.md#insn-00522ba4)

~~~diff
- 00522884 ["INT_ADD", "register:40f0:8", ["const:522884:8", "const:4:8"]]
- 00522884 ["CALL", null, ["callee:0054d804:8"]]
+ 00522ba4 ["INT_ADD", "register:40f0:8", ["const:522ba4:8", "const:4:8"]]
+ 00522ba4 ["CALL", null, ["callee:0054d804:8"]]
- 00522884 bytes 18ab0094
+ 00522ba4 bytes 18ab0094
~~~


<a id="compare-d90f691ff0334b5d359bc5ad66308e8f"></a>

### [`005229a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229a0.md) → [`00522cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cc0.md) _ZNK5Botan16X509_Certificate12x509_versionEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229a0.md#insn-005229a8)
- 新版 [`00522cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cc0.md#insn-00522cc8)

~~~diff
- 005229a8 ["INT_ADD", "register:40f0:8", ["const:5229a8:8", "const:4:8"]]
- 005229a8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522cc8 ["INT_ADD", "register:40f0:8", ["const:522cc8:8", "const:4:8"]]
+ 00522cc8 ["CALL", null, ["callee:00c5aa90:8"]]
- 005229a8 bytes 46dc1c94
+ 00522cc8 bytes 72df1c94
~~~


<a id="compare-52da84c69982b8043be6e689a9a961cd"></a>

### [`005229b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229b8.md) → [`00522cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cd8.md) _ZNK5Botan16X509_Certificate14is_self_signedEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229b8.md#insn-005229c0)
- 新版 [`00522ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cd8.md#insn-00522ce0)

~~~diff
- 005229c0 ["INT_ADD", "register:40f0:8", ["const:5229c0:8", "const:4:8"]]
- 005229c0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522ce0 ["INT_ADD", "register:40f0:8", ["const:522ce0:8", "const:4:8"]]
+ 00522ce0 ["CALL", null, ["callee:00c5aa90:8"]]
- 005229c0 bytes 40dc1c94
+ 00522ce0 bytes 6cdf1c94
~~~


<a id="compare-6dae37162ef24caf5a5ce62a7245b5dc"></a>

### [`005229d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229d0.md) → [`00522cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cf0.md) _ZNK5Botan16X509_Certificate10not_beforeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229d0.md#insn-005229d8)
- 新版 [`00522cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522cf0.md#insn-00522cf8)

~~~diff
- 005229d8 ["INT_ADD", "register:40f0:8", ["const:5229d8:8", "const:4:8"]]
- 005229d8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522cf8 ["INT_ADD", "register:40f0:8", ["const:522cf8:8", "const:4:8"]]
+ 00522cf8 ["CALL", null, ["callee:00c5aa90:8"]]
- 005229d8 bytes 3adc1c94
+ 00522cf8 bytes 66df1c94
~~~


<a id="compare-437b91e11b74e73501881c97ceb0b6aa"></a>

### [`005229e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229e8.md) → [`00522d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d08.md) _ZNK5Botan16X509_Certificate9not_afterEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229e8.md#insn-005229f0)
- 新版 [`00522d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d08.md#insn-00522d10)

~~~diff
- 005229f0 ["INT_ADD", "register:40f0:8", ["const:5229f0:8", "const:4:8"]]
- 005229f0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d10 ["INT_ADD", "register:40f0:8", ["const:522d10:8", "const:4:8"]]
+ 00522d10 ["CALL", null, ["callee:00c5aa90:8"]]
- 005229f0 bytes 34dc1c94
+ 00522d10 bytes 60df1c94
~~~


<a id="compare-e52e9f69501b50d0e3046fd3f118ef23"></a>

### [`00522a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a00.md) → [`00522d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d20.md) _ZNK5Botan16X509_Certificate23subject_public_key_algoEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a00.md#insn-00522a08)
- 新版 [`00522d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d20.md#insn-00522d28)

~~~diff
- 00522a08 ["INT_ADD", "register:40f0:8", ["const:522a08:8", "const:4:8"]]
- 00522a08 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d28 ["INT_ADD", "register:40f0:8", ["const:522d28:8", "const:4:8"]]
+ 00522d28 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a08 bytes 2edc1c94
+ 00522d28 bytes 5adf1c94
~~~


<a id="compare-79ea2bb521260ac5cf855399b129c9cf"></a>

### [`00522a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a18.md) → [`00522d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d38.md) _ZNK5Botan16X509_Certificate16v2_issuer_key_idEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a18.md#insn-00522a20)
- 新版 [`00522d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d38.md#insn-00522d40)

~~~diff
- 00522a20 ["INT_ADD", "register:40f0:8", ["const:522a20:8", "const:4:8"]]
- 00522a20 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d40 ["INT_ADD", "register:40f0:8", ["const:522d40:8", "const:4:8"]]
+ 00522d40 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a20 bytes 28dc1c94
+ 00522d40 bytes 54df1c94
~~~


<a id="compare-fb23789b7537a5d2f5bc71899f40d7da"></a>

### [`00522a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a30.md) → [`00522d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d50.md) _ZNK5Botan16X509_Certificate17v2_subject_key_idEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a30.md#insn-00522a38)
- 新版 [`00522d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d50.md#insn-00522d58)

~~~diff
- 00522a38 ["INT_ADD", "register:40f0:8", ["const:522a38:8", "const:4:8"]]
- 00522a38 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d58 ["INT_ADD", "register:40f0:8", ["const:522d58:8", "const:4:8"]]
+ 00522d58 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a38 bytes 22dc1c94
+ 00522d58 bytes 4edf1c94
~~~


<a id="compare-1a5e031ddc5af18b6aa389a2bc924528"></a>

### [`00522a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a48.md) → [`00522d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d68.md) _ZNK5Botan16X509_Certificate23subject_public_key_bitsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a48.md#insn-00522a50)
- 新版 [`00522d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d68.md#insn-00522d70)

~~~diff
- 00522a50 ["INT_ADD", "register:40f0:8", ["const:522a50:8", "const:4:8"]]
- 00522a50 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d70 ["INT_ADD", "register:40f0:8", ["const:522d70:8", "const:4:8"]]
+ 00522d70 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a50 bytes 1cdc1c94
+ 00522d70 bytes 48df1c94
~~~


<a id="compare-f877181872bf32508f6f11932bf33eab"></a>

### [`00522a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a60.md) → [`00522d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d80.md) _ZNK5Botan16X509_Certificate18is_serial_negativeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a60.md#insn-00522a68)
- 新版 [`00522d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d80.md#insn-00522d88)

~~~diff
- 00522a68 ["INT_ADD", "register:40f0:8", ["const:522a68:8", "const:4:8"]]
- 00522a68 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522d88 ["INT_ADD", "register:40f0:8", ["const:522d88:8", "const:4:8"]]
+ 00522d88 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a68 bytes 16dc1c94
+ 00522d88 bytes 42df1c94
~~~


<a id="compare-2cd396fe40f0f5d1a55b3f1655d64065"></a>

### [`00522a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a78.md) → [`00522d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d98.md) _ZNK5Botan16X509_Certificate10path_limitEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a78.md#insn-00522a80)
- 新版 [`00522da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522d98.md#insn-00522da0)

~~~diff
- 00522a80 ["INT_ADD", "register:40f0:8", ["const:522a80:8", "const:4:8"]]
- 00522a80 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522da0 ["INT_ADD", "register:40f0:8", ["const:522da0:8", "const:4:8"]]
+ 00522da0 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a80 bytes 10dc1c94
+ 00522da0 bytes 3cdf1c94
~~~


<a id="compare-a7376e55a703ad4980513449517fe467"></a>

### [`00522a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a90.md) → [`00522db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522db0.md) _ZNK5Botan16X509_Certificate11constraintsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a90.md#insn-00522a98)
- 新版 [`00522db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522db0.md#insn-00522db8)

~~~diff
- 00522a98 ["INT_ADD", "register:40f0:8", ["const:522a98:8", "const:4:8"]]
- 00522a98 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522db8 ["INT_ADD", "register:40f0:8", ["const:522db8:8", "const:4:8"]]
+ 00522db8 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522a98 bytes 0adc1c94
+ 00522db8 bytes 36df1c94
~~~


<a id="compare-146e9b258b9f8d1bb75c0b4d31a9d5ea"></a>

### [`00522aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522aa8.md) → [`00522dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522dc8.md) _ZNK5Botan16X509_Certificate18extended_key_usageEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522aa8.md#insn-00522ab0)
- 新版 [`00522dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522dc8.md#insn-00522dd0)

~~~diff
- 00522ab0 ["INT_ADD", "register:40f0:8", ["const:522ab0:8", "const:4:8"]]
- 00522ab0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522dd0 ["INT_ADD", "register:40f0:8", ["const:522dd0:8", "const:4:8"]]
+ 00522dd0 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522ab0 bytes 04dc1c94
+ 00522dd0 bytes 30df1c94
~~~


<a id="compare-1d1053debf310c9cd960dd21bf168b95"></a>

### [`00522ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ac0.md) → [`00522de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522de0.md) _ZNK5Botan16X509_Certificate23certificate_policy_oidsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ac0.md#insn-00522ac8)
- 新版 [`00522de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522de0.md#insn-00522de8)

~~~diff
- 00522ac8 ["INT_ADD", "register:40f0:8", ["const:522ac8:8", "const:4:8"]]
- 00522ac8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522de8 ["INT_ADD", "register:40f0:8", ["const:522de8:8", "const:4:8"]]
+ 00522de8 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522ac8 bytes fedb1c94
+ 00522de8 bytes 2adf1c94
~~~


<a id="compare-b3615156ced14ccbd2fcdae575d0418d"></a>

### [`00522ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ad8.md) → [`00522df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522df8.md) _ZNK5Botan16X509_Certificate16name_constraintsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ad8.md#insn-00522ae0)
- 新版 [`00522e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522df8.md#insn-00522e00)

~~~diff
- 00522ae0 ["INT_ADD", "register:40f0:8", ["const:522ae0:8", "const:4:8"]]
- 00522ae0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522e00 ["INT_ADD", "register:40f0:8", ["const:522e00:8", "const:4:8"]]
+ 00522e00 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522ae0 bytes f8db1c94
+ 00522e00 bytes 24df1c94
~~~


<a id="compare-00165a6ecdf11c553e3c4c67fe1b5c37"></a>

### [`00522af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522af0.md) → [`00522e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522e10.md) _ZNK5Botan16X509_Certificate13v3_extensionsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522af0.md#insn-00522af8)
- 新版 [`00522e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522e10.md#insn-00522e18)

~~~diff
- 00522af8 ["INT_ADD", "register:40f0:8", ["const:522af8:8", "const:4:8"]]
- 00522af8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522e18 ["INT_ADD", "register:40f0:8", ["const:522e18:8", "const:4:8"]]
+ 00522e18 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522af8 bytes f2db1c94
+ 00522e18 bytes 1edf1c94
~~~


<a id="compare-a711ec0f48061cce19866646121066c2"></a>

### [`00522b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522b08.md) → [`00522e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522e28.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNS_3OIDE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522b08.md#insn-00522b18)
- 新版 [`00522e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522e28.md#insn-00522e38)

~~~diff
- 00522b18 ["INT_ADD", "register:40f0:8", ["const:522b18:8", "const:4:8"]]
- 00522b18 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522e38 ["INT_ADD", "register:40f0:8", ["const:522e38:8", "const:4:8"]]
+ 00522e38 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522b18 bytes eadb1c94
+ 00522e38 bytes 16df1c94
~~~


<a id="compare-a0331b28964d0b141f5f4abd0cb64a6a"></a>

### [`00522dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522dec.md) → [`0052310c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052310c.md) _ZNK5Botan16X509_Certificate15has_constraintsENS_15Key_ConstraintsE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522dec.md#insn-00522e00) · [`00522e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522dec.md#insn-00522e10)
- 新版 [`00523120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052310c.md#insn-00523120) · [`00523130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052310c.md#insn-00523130)

~~~diff
- 00522e00 ["INT_ADD", "register:40f0:8", ["const:522e00:8", "const:4:8"]]
- 00522e00 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523120 ["INT_ADD", "register:40f0:8", ["const:523120:8", "const:4:8"]]
+ 00523120 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522e00 bytes 30db1c94
+ 00523120 bytes 5cde1c94
- 00522e10 ["INT_ADD", "register:40f0:8", ["const:522e10:8", "const:4:8"]]
- 00522e10 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523130 ["INT_ADD", "register:40f0:8", ["const:523130:8", "const:4:8"]]
+ 00523130 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522e10 bytes 2cdb1c94
+ 00523130 bytes 58de1c94
~~~


<a id="compare-2428daf2b650609c5c2b44d154cf24f3"></a>

### [`00522e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522e34.md) → [`00523154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523154.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522e34.md#insn-00522e60) · [`00522e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522e34.md#insn-00522e68) · [`00522ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522e34.md#insn-00522ee4)
- 新版 [`00523180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523154.md#insn-00523180) · [`00523188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523154.md#insn-00523188) · [`00523204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523154.md#insn-00523204)

~~~diff
- 00522e60 ["INT_ADD", "register:40f0:8", ["const:522e60:8", "const:4:8"]]
- 00522e60 ["CALL", null, ["callee:00c59720:8"]]
+ 00523180 ["INT_ADD", "register:40f0:8", ["const:523180:8", "const:4:8"]]
+ 00523180 ["CALL", null, ["callee:00c59720:8"]]
- 00522e60 bytes 3cd61c94
+ 00523180 bytes 68d91c94
- 00522e68 ["INT_ADD", "register:40f0:8", ["const:522e68:8", "const:4:8"]]
- 00522e68 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523188 ["INT_ADD", "register:40f0:8", ["const:523188:8", "const:4:8"]]
+ 00523188 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522e68 bytes 16db1c94
+ 00523188 bytes 42de1c94
- 00522ee4 ["INT_ADD", "register:40f0:8", ["const:522ee4:8", "const:4:8"]]
- 00522ee4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00523204 ["INT_ADD", "register:40f0:8", ["const:523204:8", "const:4:8"]]
+ 00523204 ["CALL", null, ["callee:00c58f50:8"]]
- 00522ee4 bytes 27d41c94
+ 00523204 bytes 53d71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66af4ffd5fdd68cb6ba6e93aedebbf0f"></a>

### [`00522f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522f54.md) → [`00523274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523274.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522f54.md#insn-00522f64)
- 新版 [`00523284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523274.md#insn-00523284)

~~~diff
- 00522f64 ["INT_ADD", "register:40f0:8", ["const:522f64:8", "const:4:8"]]
- 00522f64 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523284 ["INT_ADD", "register:40f0:8", ["const:523284:8", "const:4:8"]]
+ 00523284 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522f64 bytes d7da1c94
+ 00523284 bytes 03de1c94
~~~


<a id="compare-48eefe0946b484117ff3511c2579c114"></a>

### [`00522fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522fe4.md) → [`00523304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523304.md) _ZNK5Botan16X509_Certificate14ocsp_responderEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522fe4.md#insn-00522ff4)
- 新版 [`00523314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523304.md#insn-00523314)

~~~diff
- 00522ff4 ["INT_ADD", "register:40f0:8", ["const:522ff4:8", "const:4:8"]]
- 00522ff4 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523314 ["INT_ADD", "register:40f0:8", ["const:523314:8", "const:4:8"]]
+ 00523314 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522ff4 bytes b3da1c94
+ 00523314 bytes dfdd1c94
~~~


<a id="compare-07e23d42a744ca2d7e242eb9865063eb"></a>

### [`00523038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523038.md) → [`00523358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523358.md) _ZNK5Botan16X509_Certificate10ca_issuersEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523038.md#insn-00523048)
- 新版 [`00523368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523358.md#insn-00523368)

~~~diff
- 00523048 ["INT_ADD", "register:40f0:8", ["const:523048:8", "const:4:8"]]
- 00523048 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00523368 ["INT_ADD", "register:40f0:8", ["const:523368:8", "const:4:8"]]
+ 00523368 ["CALL", null, ["callee:00c5aa90:8"]]
- 00523048 bytes 9eda1c94
+ 00523368 bytes cadd1c94
~~~


<a id="compare-68c96a5578ff9606017876e9f4afe130"></a>

### [`00523080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523080.md) → [`005233a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/005233a0.md) _ZNK5Botan16X509_Certificate22crl_distribution_pointEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523080.md#insn-00523094) · [`005230ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523080.md#insn-005230ac)
- 新版 [`005233b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/005233a0.md#insn-005233b4) · [`005233cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/005233a0.md#insn-005233cc)

~~~diff
- 00523094 ["INT_ADD", "register:40f0:8", ["const:523094:8", "const:4:8"]]
- 00523094 ["CALL", null, ["callee:00c5aa90:8"]]
+ 005233b4 ["INT_ADD", "register:40f0:8", ["const:5233b4:8", "const:4:8"]]
+ 005233b4 ["CALL", null, ["callee:00c5aa90:8"]]
- 00523094 bytes 8bda1c94
+ 005233b4 bytes b7dd1c94
- 005230ac ["INT_ADD", "register:40f0:8", ["const:5230ac:8", "const:4:8"]]
- 005230ac ["CALL", null, ["callee:00c5aa90:8"]]
+ 005233cc ["INT_ADD", "register:40f0:8", ["const:5233cc:8", "const:4:8"]]
+ 005233cc ["CALL", null, ["callee:00c5aa90:8"]]
- 005230ac bytes 85da1c94
+ 005233cc bytes b1dd1c94
~~~


<a id="compare-2488ffc684a8ca86719238d896d3cf31"></a>

### [`005230f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/005230f4.md) → [`00523414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523414.md) _ZNK5Botan16X509_Certificate15issuer_alt_nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005230fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/005230f4.md#insn-005230fc)
- 新版 [`0052341c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/00523414.md#insn-0052341c)

~~~diff
- 005230fc ["INT_ADD", "register:40f0:8", ["const:5230fc:8", "const:4:8"]]
- 005230fc ["CALL", null, ["callee:00c5aa90:8"]]
+ 0052341c ["INT_ADD", "register:40f0:8", ["const:52341c:8", "const:4:8"]]
+ 0052341c ["CALL", null, ["callee:00c5aa90:8"]]
- 005230fc bytes 71da1c94
+ 0052341c bytes 9ddd1c94
~~~


<a id="compare-8bda449001c57011e3dfc53470d61bcd"></a>

### [`00523e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523e28.md) → [`00524148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524148.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ce0.md) · 呼出先 5件 [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c597c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597c0.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5acb0.md) · 呼出先 5件 [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a790.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523e28.md#insn-00523e4c) · [`00523e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523e28.md#insn-00523e58) · [`00523e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523e28.md#insn-00523e60)
- 新版 [`0052416c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524148.md#insn-0052416c) · [`00524178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524148.md#insn-00524178) · [`00524180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524148.md#insn-00524180)

~~~diff
- 00523e4c ["INT_ADD", "register:40f0:8", ["const:523e4c:8", "const:4:8"]]
- 00523e4c ["CALL", null, ["callee:00c5aa90:8"]]
+ 0052416c ["INT_ADD", "register:40f0:8", ["const:52416c:8", "const:4:8"]]
+ 0052416c ["CALL", null, ["callee:00c5aa90:8"]]
- 00523e4c bytes 1dd71c94
+ 0052416c bytes 49da1c94
- 00523e58 ["INT_ADD", "register:40f0:8", ["const:523e58:8", "const:4:8"]]
- 00523e58 ["CALL", null, ["callee:004a6f7c:8"]]
+ 00524178 ["INT_ADD", "register:40f0:8", ["const:524178:8", "const:4:8"]]
+ 00524178 ["CALL", null, ["callee:004a6f7c:8"]]
- 00523e58 bytes 810bfe97
+ 00524178 bytes 810bfe97
- 00523e60 ["INT_ADD", "register:40f0:8", ["const:523e60:8", "const:4:8"]]
- 00523e60 ["CALL", null, ["callee:00c5a790:8"]]
+ 00524180 ["INT_ADD", "register:40f0:8", ["const:524180:8", "const:4:8"]]
+ 00524180 ["CALL", null, ["callee:00c5a790:8"]]
- 00523e60 bytes 58d61c94
+ 00524180 bytes 84d91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7965df638400b776c64e0b0fdf3a61c3"></a>

### [`00523f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523f9c.md) → [`005242bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005242bc.md) _ZNK5Botan16X509_Certificate20raw_issuer_dn_sha256Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523f9c.md#insn-00523ffc) · [`0052400c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523f9c.md#insn-0052400c) · [`0052401c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523f9c.md#insn-0052401c)
- 新版 [`0052431c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005242bc.md#insn-0052431c) · [`0052432c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005242bc.md#insn-0052432c) · [`0052433c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005242bc.md#insn-0052433c)

~~~diff
- 00523ffc ["INT_ADD", "register:40f0:8", ["const:523ffc:8", "const:4:8"]]
- 00523ffc ["CALL", null, ["callee:00c59f10:8"]]
+ 0052431c ["INT_ADD", "register:40f0:8", ["const:52431c:8", "const:4:8"]]
+ 0052431c ["CALL", null, ["callee:00c59f10:8"]]
- 00523ffc bytes d1d31c94
+ 0052431c bytes fdd61c94
- 0052400c ["INT_ADD", "register:40f0:8", ["const:52400c:8", "const:4:8"]]
- 0052400c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052432c ["INT_ADD", "register:40f0:8", ["const:52432c:8", "const:4:8"]]
+ 0052432c ["CALL", null, ["callee:00c58f50:8"]]
- 0052400c bytes ddcf1c94
+ 0052432c bytes 09d31c94
- 0052401c ["INT_ADD", "register:40f0:8", ["const:52401c:8", "const:4:8"]]
- 0052401c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052433c ["INT_ADD", "register:40f0:8", ["const:52433c:8", "const:4:8"]]
+ 0052433c ["CALL", null, ["callee:00c58f50:8"]]
- 0052401c bytes d9cf1c94
+ 0052433c bytes 05d31c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a841edb902572e1cc06a101fa6ed183e"></a>

### [`0052418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052418c.md) → [`005244ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005244ac.md) _ZNK5Botan16X509_Certificate21raw_subject_dn_sha256Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c59e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005241ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052418c.md#insn-005241ec) · [`005241f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052418c.md#insn-005241f8) · [`00524210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052418c.md#insn-00524210)
- 新版 [`0052450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005244ac.md#insn-0052450c) · [`00524518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005244ac.md#insn-00524518) · [`00524530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005244ac.md#insn-00524530)

~~~diff
- 005241ec ["INT_ADD", "register:40f0:8", ["const:5241ec:8", "const:4:8"]]
- 005241ec ["CALL", null, ["callee:00c59e90:8"]]
+ 0052450c ["INT_ADD", "register:40f0:8", ["const:52450c:8", "const:4:8"]]
+ 0052450c ["CALL", null, ["callee:00c59e90:8"]]
- 005241ec bytes 35d31c94
+ 0052450c bytes 61d61c94
- 005241f8 ["INT_ADD", "register:40f0:8", ["const:5241f8:8", "const:4:8"]]
- 005241f8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00524518 ["INT_ADD", "register:40f0:8", ["const:524518:8", "const:4:8"]]
+ 00524518 ["CALL", null, ["callee:00c5aa90:8"]]
- 005241f8 bytes 32d61c94
+ 00524518 bytes 5ed91c94
- 00524210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00524210 ["INT_ADD", "register:40f0:8", ["const:524210:8", "const:4:8"]]
- 00524210 ["CALLIND", null, ["register:0:8"]]
+ 00524530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00524530 ["INT_ADD", "register:40f0:8", ["const:524530:8", "const:4:8"]]
+ 00524530 ["CALLIND", null, ["register:0:8"]]
- 00524210 bytes 00013fd6
+ 00524530 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf8d1da2faecc6364cd5b3cef065b18c"></a>

### [`00524324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524324.md) → [`00524644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524644.md) _ZNK5Botan16X509_Certificate14ex_constraintsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052466c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524324.md#insn-00524334)
- 新版 [`00524654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524644.md#insn-00524654)

~~~diff
- 00524334 ["INT_ADD", "register:40f0:8", ["const:524334:8", "const:4:8"]]
- 00524334 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00524654 ["INT_ADD", "register:40f0:8", ["const:524654:8", "const:4:8"]]
+ 00524654 ["CALL", null, ["callee:00c5aa90:8"]]
- 00524334 bytes e3d51c94
+ 00524654 bytes 0fd91c94
~~~


<a id="compare-75d229dc2b3c0e38fe99ce9f805824fc"></a>

### [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) → [`0052466c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md) FUN_0052466c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00524324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524324.md) [`0052457c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052457c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00524644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524644.md) [`0052489c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052489c.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005243d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md#insn-005243d8) · [`00524440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md#insn-00524440) · [`00524484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md#insn-00524484)
- 新版 [`005246f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md#insn-005246f8) · [`00524760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md#insn-00524760) · [`005247a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md#insn-005247a4)

~~~diff
- 005243d8 ["INT_ADD", "register:40f0:8", ["const:5243d8:8", "const:4:8"]]
- 005243d8 ["CALL", null, ["callee:00c59950:8"]]
+ 005246f8 ["INT_ADD", "register:40f0:8", ["const:5246f8:8", "const:4:8"]]
+ 005246f8 ["CALL", null, ["callee:00c59950:8"]]
- 005243d8 bytes 6ad11c94
+ 005246f8 bytes 96d41c94
- 00524440 ["INT_ADD", "register:40f0:8", ["const:524440:8", "const:4:8"]]
- 00524440 ["CALL", null, ["callee:00c58f30:8"]]
+ 00524760 ["INT_ADD", "register:40f0:8", ["const:524760:8", "const:4:8"]]
+ 00524760 ["CALL", null, ["callee:00c58f30:8"]]
- 00524440 bytes c8ce1c94
+ 00524760 bytes f4d11c94
- 00524484 ["INT_ADD", "register:40f0:8", ["const:524484:8", "const:4:8"]]
- 00524484 ["CALL", null, ["callee:00c590a0:8"]]
+ 005247a4 ["INT_ADD", "register:40f0:8", ["const:5247a4:8", "const:4:8"]]
+ 005247a4 ["CALL", null, ["callee:00c590a0:8"]]
- 00524484 bytes 13cf1c94
+ 005247a4 bytes 3fd21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d04c9d8e7d210c6f3ed57fcd2cd745"></a>

### [`0052457c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052457c.md) → [`0052489c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052489c.md) _ZNK5Botan16X509_Certificate8policiesEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052466c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052466c.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052458c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052457c.md#insn-0052458c)
- 新版 [`005248ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/0052489c.md#insn-005248ac)

~~~diff
- 0052458c ["INT_ADD", "register:40f0:8", ["const:52458c:8", "const:4:8"]]
- 0052458c ["CALL", null, ["callee:00c5aa90:8"]]
+ 005248ac ["INT_ADD", "register:40f0:8", ["const:5248ac:8", "const:4:8"]]
+ 005248ac ["CALL", null, ["callee:00c5aa90:8"]]
- 0052458c bytes 4dd51c94
+ 005248ac bytes 79d81c94
~~~


<a id="compare-e517fe0bdb7ab1938b61fd25b148fe42"></a>

### [`005245a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005245a4.md) → [`005248c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005248c4.md) _ZNK5Botan16X509_Certificate11fingerprintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59690.md) [`00c59f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a660.md) [`00c5af20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005245d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005245a4.md#insn-005245d0) · [`005245e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005245a4.md#insn-005245e4) · [`005245f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005245a4.md#insn-005245f4)
- 新版 [`005248f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005248c4.md#insn-005248f0) · [`00524904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005248c4.md#insn-00524904) · [`00524914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/005248c4.md#insn-00524914)

~~~diff
- 005245d0 ["INT_ADD", "register:40f0:8", ["const:5245d0:8", "const:4:8"]]
- 005245d0 ["CALL", null, ["callee:00c5af20:8"]]
+ 005248f0 ["INT_ADD", "register:40f0:8", ["const:5248f0:8", "const:4:8"]]
+ 005248f0 ["CALL", null, ["callee:00c5af20:8"]]
- 005245d0 bytes 60d61c94
+ 005248f0 bytes 8cd91c94
- 005245e4 ["INT_ADD", "register:40f0:8", ["const:5245e4:8", "const:4:8"]]
- 005245e4 ["CALL", null, ["callee:00c5a660:8"]]
+ 00524904 ["INT_ADD", "register:40f0:8", ["const:524904:8", "const:4:8"]]
+ 00524904 ["CALL", null, ["callee:00c5a660:8"]]
- 005245e4 bytes 2bd41c94
+ 00524904 bytes 57d71c94
- 005245f4 ["INT_ADD", "register:40f0:8", ["const:5245f4:8", "const:4:8"]]
- 005245f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00524914 ["INT_ADD", "register:40f0:8", ["const:524914:8", "const:4:8"]]
+ 00524914 ["CALL", null, ["callee:00c58f50:8"]]
- 005245f4 bytes 63ce1c94
+ 00524914 bytes 8fd11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a3c88ee3a2130de3ea5217737cbe003"></a>

### [`00524650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524650.md) → [`00524970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524970.md) _ZNK5Botan16X509_Certificate16matches_dns_nameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f90.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c599f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599f0.md) [`00c59f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f80.md)
- 新版 呼出元 1件 [`00c5af60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af60.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a9c0.md) [`00c5af50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005246b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524650.md#insn-005246b0) · [`005246c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524650.md#insn-005246c0) · [`005246f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524650.md#insn-005246f4)
- 新版 [`005249d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524970.md#insn-005249d0) · [`005249e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524970.md#insn-005249e0) · [`00524a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524970.md#insn-00524a14)

~~~diff
- 005246b0 ["INT_ADD", "register:40f0:8", ["const:5246b0:8", "const:4:8"]]
- 005246b0 ["CALL", null, ["callee:00c5af50:8"]]
+ 005249d0 ["INT_ADD", "register:40f0:8", ["const:5249d0:8", "const:4:8"]]
+ 005249d0 ["CALL", null, ["callee:00c5af50:8"]]
- 005246b0 bytes 34d61c94
+ 005249d0 bytes 60d91c94
- 005246c0 ["INT_ADD", "register:40f0:8", ["const:5246c0:8", "const:4:8"]]
- 005246c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005249e0 ["INT_ADD", "register:40f0:8", ["const:5249e0:8", "const:4:8"]]
+ 005249e0 ["CALL", null, ["callee:00c58f50:8"]]
- 005246c0 bytes 30ce1c94
+ 005249e0 bytes 5cd11c94
- 005246f4 ["INT_ADD", "register:40f0:8", ["const:5246f4:8", "const:4:8"]]
- 005246f4 ["CALL", null, ["callee:00c5af50:8"]]
+ 00524a14 ["INT_ADD", "register:40f0:8", ["const:524a14:8", "const:4:8"]]
+ 00524a14 ["CALL", null, ["callee:00c5af50:8"]]
- 005246f4 bytes 23d61c94
+ 00524a14 bytes 4fd91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24bf534bf023f43ef5640f5bd5fc2010"></a>

### [`005248b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005248b0.md) → [`00524bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524bd0.md) _ZNK5Botan16X509_CertificateltERKS0_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005248ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005248b0.md#insn-005248ec)
- 新版 [`00524c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524bd0.md#insn-00524c0c)

~~~diff
- 005248ec ["INT_ADD", "register:40f0:8", ["const:5248ec:8", "const:4:8"]]
- 005248ec ["CALL", null, ["callee:00c590f0:8"]]
+ 00524c0c ["INT_ADD", "register:40f0:8", ["const:524c0c:8", "const:4:8"]]
+ 00524c0c ["CALL", null, ["callee:00c590f0:8"]]
- 005248ec bytes 0dce1c94
+ 00524c0c bytes 39d11c94
~~~


<a id="compare-b07cb14f3b3673c1a05af872dce6e6d0"></a>

### [`005249a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005249a4.md) → [`00524cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524cc4.md) _ZN5BotanneERKNS_16X509_CertificateES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c59740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005249d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005249a4.md#insn-005249d0) · [`005249e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005249a4.md#insn-005249e0) · [`00524a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005249a4.md#insn-00524a00)
- 新版 [`00524cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524cc4.md#insn-00524cf0) · [`00524d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524cc4.md#insn-00524d00) · [`00524d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524cc4.md#insn-00524d20)

~~~diff
- 005249d0 ["INT_ADD", "register:40f0:8", ["const:5249d0:8", "const:4:8"]]
- 005249d0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00524cf0 ["INT_ADD", "register:40f0:8", ["const:524cf0:8", "const:4:8"]]
+ 00524cf0 ["CALL", null, ["callee:00c590f0:8"]]
- 005249d0 bytes d4cd1c94
+ 00524cf0 bytes 00d11c94
- 005249e0 ["INT_ADD", "register:40f0:8", ["const:5249e0:8", "const:4:8"]]
- 005249e0 ["CALL", null, ["callee:00c59740:8"]]
+ 00524d00 ["INT_ADD", "register:40f0:8", ["const:524d00:8", "const:4:8"]]
+ 00524d00 ["CALL", null, ["callee:00c59740:8"]]
- 005249e0 bytes 64cf1c94
+ 00524d00 bytes 90d21c94
- 00524a00 ["INT_ADD", "register:40f0:8", ["const:524a00:8", "const:4:8"]]
- 00524a00 ["CALL", null, ["callee:00c590f0:8"]]
+ 00524d20 ["INT_ADD", "register:40f0:8", ["const:524d20:8", "const:4:8"]]
+ 00524d20 ["CALL", null, ["callee:00c590f0:8"]]
- 00524a00 bytes c8cd1c94
+ 00524d20 bytes f4d01c94
~~~


<a id="compare-2920c815c2448b17485aa0339ff473ae"></a>

### [`00526250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526250.md) → [`00526570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526570.md) _ZN5Botan17X509_Cert_Options10not_beforeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5af70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00526278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526250.md#insn-00526278) · [`005262b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526250.md#insn-005262b0)
- 新版 [`00526598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526570.md#insn-00526598) · [`005265d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526570.md#insn-005265d0)

~~~diff
- 00526278 ["INT_ADD", "register:40f0:8", ["const:526278:8", "const:4:8"]]
- 00526278 ["CALL", null, ["callee:00c5af70:8"]]
+ 00526598 ["INT_ADD", "register:40f0:8", ["const:526598:8", "const:4:8"]]
+ 00526598 ["CALL", null, ["callee:00c5af70:8"]]
- 00526278 bytes 4acf1c94
+ 00526598 bytes 76d21c94
- 005262b0 ["INT_ADD", "register:40f0:8", ["const:5262b0:8", "const:4:8"]]
- 005262b0 ["CALL", null, ["callee:00c58f80:8"]]
+ 005265d0 ["INT_ADD", "register:40f0:8", ["const:5265d0:8", "const:4:8"]]
+ 005265d0 ["CALL", null, ["callee:00c58f80:8"]]
- 005262b0 bytes 40c71c94
+ 005265d0 bytes 6cca1c94
~~~


<a id="compare-94f1e1cac2cf23b99809659189bd66b8"></a>

### [`005262b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005262b4.md) → [`005265d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/005265d4.md) _ZN5Botan17X509_Cert_Options9not_afterERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5af70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005262dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005262b4.md#insn-005262dc) · [`00526314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005262b4.md#insn-00526314)
- 新版 [`005265fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/005265d4.md#insn-005265fc) · [`00526634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/005265d4.md#insn-00526634)

~~~diff
- 005262dc ["INT_ADD", "register:40f0:8", ["const:5262dc:8", "const:4:8"]]
- 005262dc ["CALL", null, ["callee:00c5af70:8"]]
+ 005265fc ["INT_ADD", "register:40f0:8", ["const:5265fc:8", "const:4:8"]]
+ 005265fc ["CALL", null, ["callee:00c5af70:8"]]
- 005262dc bytes 31cf1c94
+ 005265fc bytes 5dd21c94
- 00526314 ["INT_ADD", "register:40f0:8", ["const:526314:8", "const:4:8"]]
- 00526314 ["CALL", null, ["callee:00c58f80:8"]]
+ 00526634 ["INT_ADD", "register:40f0:8", ["const:526634:8", "const:4:8"]]
+ 00526634 ["CALL", null, ["callee:00c58f80:8"]]
- 00526314 bytes 27c71c94
+ 00526634 bytes 53ca1c94
~~~


<a id="compare-fe23c90eb1fe8d7ff18622cb9bbbb14a"></a>

### [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) → [`0052811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md) FUN_0052811c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md) [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) · 呼出先 2件 [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`00526d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md) [`00528188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md) [`0052c6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md) [`0052d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md) · 呼出先 2件 [`0053fb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fb70.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00527e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md#insn-00527e34)
- 新版 [`00528154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md#insn-00528154)

~~~diff
- 00527e34 ["INT_ADD", "register:40f0:8", ["const:527e34:8", "const:4:8"]]
- 00527e34 ["CALL", null, ["callee:0053fb70:8"]]
+ 00528154 ["INT_ADD", "register:40f0:8", ["const:528154:8", "const:4:8"]]
+ 00528154 ["CALL", null, ["callee:0053fb70:8"]]
- 00527e34 bytes 875e0094
+ 00528154 bytes 875e0094
~~~


<a id="compare-4c6eef566f7700e315437a1ade3a9123"></a>

### [`00529cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529cf8.md) → [`0052a018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a018.md) FUN_0052a018

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00529d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529cf8.md#insn-00529d44) · [`00529d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529cf8.md#insn-00529d58) · [`00529d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529cf8.md#insn-00529d60)
- 新版 [`0052a064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a018.md#insn-0052a064) · [`0052a078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a018.md#insn-0052a078) · [`0052a080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a018.md#insn-0052a080)

~~~diff
- 00529d44 ["INT_ADD", "register:40f0:8", ["const:529d44:8", "const:4:8"]]
- 00529d44 ["CALL", null, ["callee:00c54d90:8"]]
+ 0052a064 ["INT_ADD", "register:40f0:8", ["const:52a064:8", "const:4:8"]]
+ 0052a064 ["CALL", null, ["callee:00c54d90:8"]]
- 00529d44 bytes 17a81c94
+ 0052a064 bytes 4bab1c94
- 00529d58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00529d58 ["INT_ADD", "register:40f0:8", ["const:529d58:8", "const:4:8"]]
- 00529d58 ["CALLIND", null, ["register:0:8"]]
+ 0052a078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052a078 ["INT_ADD", "register:40f0:8", ["const:52a078:8", "const:4:8"]]
+ 0052a078 ["CALLIND", null, ["register:0:8"]]
- 00529d58 bytes 00013fd6
+ 0052a078 bytes 00013fd6
- 00529d60 ["INT_ADD", "register:40f0:8", ["const:529d60:8", "const:4:8"]]
- 00529d60 ["CALL", null, ["callee:00c58f20:8"]]
+ 0052a080 ["INT_ADD", "register:40f0:8", ["const:52a080:8", "const:4:8"]]
+ 0052a080 ["CALL", null, ["callee:00c58f20:8"]]
- 00529d60 bytes 7cb81c94
+ 0052a080 bytes a8bb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7397b48b4bcfcfdf4039d05efac2a0"></a>

### [`0052b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b080.md) → [`0052b3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3a0.md) FUN_0052b3a0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b080.md#insn-0052b09c) · [`0052b0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b080.md#insn-0052b0bc)
- 新版 [`0052b3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3a0.md#insn-0052b3bc) · [`0052b3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3a0.md#insn-0052b3dc)

~~~diff
- 0052b09c ["INT_ADD", "register:40f0:8", ["const:52b09c:8", "const:4:8"]]
- 0052b09c ["CALL", null, ["callee:00c54d90:8"]]
+ 0052b3bc ["INT_ADD", "register:40f0:8", ["const:52b3bc:8", "const:4:8"]]
+ 0052b3bc ["CALL", null, ["callee:00c54d90:8"]]
- 0052b09c bytes 41a31c94
+ 0052b3bc bytes 75a61c94
- 0052b0bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b0bc ["INT_ADD", "register:40f0:8", ["const:52b0bc:8", "const:4:8"]]
- 0052b0bc ["CALLIND", null, ["register:0:8"]]
+ 0052b3dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b3dc ["INT_ADD", "register:40f0:8", ["const:52b3dc:8", "const:4:8"]]
+ 0052b3dc ["CALLIND", null, ["register:0:8"]]
- 0052b0bc bytes 00013fd6
+ 0052b3dc bytes 00013fd6
~~~


<a id="compare-1581028e814889e50f99222260bba248"></a>

### [`0052b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b0d0.md) → [`0052b3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3f0.md) FUN_0052b3f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b0d0.md#insn-0052b11c) · [`0052b130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b0d0.md#insn-0052b130) · [`0052b138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b0d0.md#insn-0052b138)
- 新版 [`0052b43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3f0.md#insn-0052b43c) · [`0052b450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3f0.md#insn-0052b450) · [`0052b458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b3f0.md#insn-0052b458)

~~~diff
- 0052b11c ["INT_ADD", "register:40f0:8", ["const:52b11c:8", "const:4:8"]]
- 0052b11c ["CALL", null, ["callee:00c54d90:8"]]
+ 0052b43c ["INT_ADD", "register:40f0:8", ["const:52b43c:8", "const:4:8"]]
+ 0052b43c ["CALL", null, ["callee:00c54d90:8"]]
- 0052b11c bytes 21a31c94
+ 0052b43c bytes 55a61c94
- 0052b130 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b130 ["INT_ADD", "register:40f0:8", ["const:52b130:8", "const:4:8"]]
- 0052b130 ["CALLIND", null, ["register:0:8"]]
+ 0052b450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b450 ["INT_ADD", "register:40f0:8", ["const:52b450:8", "const:4:8"]]
+ 0052b450 ["CALLIND", null, ["register:0:8"]]
- 0052b130 bytes 00013fd6
+ 0052b450 bytes 00013fd6
- 0052b138 ["INT_ADD", "register:40f0:8", ["const:52b138:8", "const:4:8"]]
- 0052b138 ["CALL", null, ["callee:00c58f20:8"]]
+ 0052b458 ["INT_ADD", "register:40f0:8", ["const:52b458:8", "const:4:8"]]
+ 0052b458 ["CALL", null, ["callee:00c58f20:8"]]
- 0052b138 bytes 86b31c94
+ 0052b458 bytes b2b61c94
~~~


<a id="compare-3502a8e003ffc392042bc07e31389cca"></a>

### [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) → [`0052c5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md) FUN_0052c5a4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) [`0052c508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c508.md) [`0054ed44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ed44.md) · 呼出先 4件 [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0052ba98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md) [`0052c828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c828.md) [`0054f064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f064.md) · 呼出先 4件 [`0053fb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fb70.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md#insn-0052c2d0) · [`0052c2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md#insn-0052c2e4) · [`0052c2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md#insn-0052c2ec)
- 新版 [`0052c5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md#insn-0052c5f0) · [`0052c604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md#insn-0052c604) · [`0052c60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md#insn-0052c60c)

~~~diff
- 0052c2d0 ["INT_ADD", "register:40f0:8", ["const:52c2d0:8", "const:4:8"]]
- 0052c2d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0052c5f0 ["INT_ADD", "register:40f0:8", ["const:52c5f0:8", "const:4:8"]]
+ 0052c5f0 ["CALL", null, ["callee:00c54d90:8"]]
- 0052c2d0 bytes b49e1c94
+ 0052c5f0 bytes e8a11c94
- 0052c2e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c2e4 ["INT_ADD", "register:40f0:8", ["const:52c2e4:8", "const:4:8"]]
- 0052c2e4 ["CALLIND", null, ["register:0:8"]]
+ 0052c604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c604 ["INT_ADD", "register:40f0:8", ["const:52c604:8", "const:4:8"]]
+ 0052c604 ["CALLIND", null, ["register:0:8"]]
- 0052c2e4 bytes 00013fd6
+ 0052c604 bytes 00013fd6
- 0052c2ec ["INT_ADD", "register:40f0:8", ["const:52c2ec:8", "const:4:8"]]
- 0052c2ec ["CALL", null, ["callee:00c58f20:8"]]
+ 0052c60c ["INT_ADD", "register:40f0:8", ["const:52c60c:8", "const:4:8"]]
+ 0052c60c ["CALL", null, ["callee:00c58f20:8"]]
- 0052c2ec bytes 19af1c94
+ 0052c60c bytes 45b21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5ef45bcd94257b2262c14f94e62662"></a>

### [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md) → [`0052c6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md) FUN_0052c6b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) · 呼出先 7件 [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005485c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005485c4.md) [`0054ebcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ebcc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`0052ba98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md) · 呼出先 7件 [`0052811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md) [`005488e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005488e4.md) [`0054eeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054e/0054eeec.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md#insn-0052c3e8) · [`0052c40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md#insn-0052c40c) · [`0052c438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md#insn-0052c438)
- 新版 [`0052c708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md#insn-0052c708) · [`0052c72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md#insn-0052c72c) · [`0052c758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md#insn-0052c758)

~~~diff
- 0052c3e8 ["INT_ADD", "register:40f0:8", ["const:52c3e8:8", "const:4:8"]]
- 0052c3e8 ["CALL", null, ["callee:0054eeec:8"]]
+ 0052c708 ["INT_ADD", "register:40f0:8", ["const:52c708:8", "const:4:8"]]
+ 0052c708 ["CALL", null, ["callee:0054eeec:8"]]
- 0052c3e8 bytes f9890094
+ 0052c708 bytes f9890094
- 0052c40c ["INT_ADD", "register:40f0:8", ["const:52c40c:8", "const:4:8"]]
- 0052c40c ["CALL", null, ["callee:0054eeec:8"]]
+ 0052c72c ["INT_ADD", "register:40f0:8", ["const:52c72c:8", "const:4:8"]]
+ 0052c72c ["CALL", null, ["callee:0054eeec:8"]]
- 0052c40c bytes f0890094
+ 0052c72c bytes f0890094
- 0052c438 ["INT_ADD", "register:40f0:8", ["const:52c438:8", "const:4:8"]]
- 0052c438 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052c758 ["INT_ADD", "register:40f0:8", ["const:52c758:8", "const:4:8"]]
+ 0052c758 ["CALL", null, ["callee:00c58f30:8"]]
- 0052c438 bytes caae1c94
+ 0052c758 bytes f6b11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09256e54c63d9ab01e322e2aae721707"></a>

### [`0052c508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c508.md) → [`0052c828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c828.md) FUN_0052c828

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052c5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c508.md#insn-0052c53c)
- 新版 [`0052c85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c828.md#insn-0052c85c)

~~~diff
- 0052c53c ["INT_ADD", "register:40f0:8", ["const:52c53c:8", "const:4:8"]]
- 0052c53c ["CALL", null, ["callee:0052c5a4:8"]]
+ 0052c85c ["INT_ADD", "register:40f0:8", ["const:52c85c:8", "const:4:8"]]
+ 0052c85c ["CALL", null, ["callee:0052c5a4:8"]]
- 0052c53c bytes 52ffff97
+ 0052c85c bytes 52ffff97
~~~


<a id="compare-1c7fec26455c8d99891407c971a987df"></a>

### [`0052c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c570.md) → [`0052c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c890.md) FUN_0052c890

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c570.md#insn-0052c5b4) · [`0052c5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c570.md#insn-0052c5fc) · [`0052c610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c570.md#insn-0052c610)
- 新版 [`0052c8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c890.md#insn-0052c8d4) · [`0052c91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c890.md#insn-0052c91c) · [`0052c930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c890.md#insn-0052c930)

~~~diff
- 0052c5b4 ["INT_ADD", "register:40f0:8", ["const:52c5b4:8", "const:4:8"]]
- 0052c5b4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0052c8d4 ["INT_ADD", "register:40f0:8", ["const:52c8d4:8", "const:4:8"]]
+ 0052c8d4 ["CALL", null, ["callee:00c58f50:8"]]
- 0052c5b4 bytes 73ae1c94
+ 0052c8d4 bytes 9fb11c94
- 0052c5fc ["INT_ADD", "register:40f0:8", ["const:52c5fc:8", "const:4:8"]]
- 0052c5fc ["CALL", null, ["callee:00c54d90:8"]]
+ 0052c91c ["INT_ADD", "register:40f0:8", ["const:52c91c:8", "const:4:8"]]
+ 0052c91c ["CALL", null, ["callee:00c54d90:8"]]
- 0052c5fc bytes e99d1c94
+ 0052c91c bytes 1da11c94
- 0052c610 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c610 ["INT_ADD", "register:40f0:8", ["const:52c610:8", "const:4:8"]]
- 0052c610 ["CALLIND", null, ["register:0:8"]]
+ 0052c930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c930 ["INT_ADD", "register:40f0:8", ["const:52c930:8", "const:4:8"]]
+ 0052c930 ["CALLIND", null, ["register:0:8"]]
- 0052c610 bytes 00013fd6
+ 0052c930 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f153d47bb4241eacecc0b42d9dd00c"></a>

### [`0052c658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c658.md) → [`0052c978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c978.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS6_9a

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054ef50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ef50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f270.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5afe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c658.md#insn-0052c6b4) · [`0052c6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c658.md#insn-0052c6e0) · [`0052c710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c658.md#insn-0052c710)
- 新版 [`0052c9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c978.md#insn-0052c9d4) · [`0052ca00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c978.md#insn-0052ca00) · [`0052ca30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c978.md#insn-0052ca30)

~~~diff
- 0052c6b4 ["INT_ADD", "register:40f0:8", ["const:52c6b4:8", "const:4:8"]]
- 0052c6b4 ["CALL", null, ["callee:0054f270:8"]]
+ 0052c9d4 ["INT_ADD", "register:40f0:8", ["const:52c9d4:8", "const:4:8"]]
+ 0052c9d4 ["CALL", null, ["callee:0054f270:8"]]
- 0052c6b4 bytes 278a0094
+ 0052c9d4 bytes 278a0094
- 0052c6e0 ["INT_ADD", "register:40f0:8", ["const:52c6e0:8", "const:4:8"]]
- 0052c6e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 0052ca00 ["INT_ADD", "register:40f0:8", ["const:52ca00:8", "const:4:8"]]
+ 0052ca00 ["CALL", null, ["callee:00c5afe0:8"]]
- 0052c6e0 bytes 4cb61c94
+ 0052ca00 bytes 78b91c94
- 0052c710 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c710 ["INT_ADD", "register:40f0:8", ["const:52c710:8", "const:4:8"]]
- 0052c710 ["CALLIND", null, ["register:0:8"]]
+ 0052ca30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ca30 ["INT_ADD", "register:40f0:8", ["const:52ca30:8", "const:4:8"]]
+ 0052ca30 ["CALLIND", null, ["register:0:8"]]
- 0052c710 bytes 00013fd6
+ 0052ca30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-614ab415f650103134319f5506431217"></a>

### [`0052c784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c784.md) → [`0052caa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052caa4.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS_17Cer

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5afe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c784.md#insn-0052c7d8) · [`0052c814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c784.md#insn-0052c814) · [`0052c870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c784.md#insn-0052c870)
- 新版 [`0052caf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052caa4.md#insn-0052caf8) · [`0052cb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052caa4.md#insn-0052cb34) · [`0052cb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052caa4.md#insn-0052cb90)

~~~diff
- 0052c7d8 ["INT_ADD", "register:40f0:8", ["const:52c7d8:8", "const:4:8"]]
- 0052c7d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052caf8 ["INT_ADD", "register:40f0:8", ["const:52caf8:8", "const:4:8"]]
+ 0052caf8 ["CALL", null, ["callee:00c58f30:8"]]
- 0052c7d8 bytes e2ad1c94
+ 0052caf8 bytes 0eb11c94
- 0052c814 ["INT_ADD", "register:40f0:8", ["const:52c814:8", "const:4:8"]]
- 0052c814 ["CALL", null, ["callee:00c5afe0:8"]]
+ 0052cb34 ["INT_ADD", "register:40f0:8", ["const:52cb34:8", "const:4:8"]]
+ 0052cb34 ["CALL", null, ["callee:00c5afe0:8"]]
- 0052c814 bytes ffb51c94
+ 0052cb34 bytes 2bb91c94
- 0052c870 ["INT_ADD", "register:40f0:8", ["const:52c870:8", "const:4:8"]]
- 0052c870 ["CALL", null, ["callee:00c58f80:8"]]
+ 0052cb90 ["INT_ADD", "register:40f0:8", ["const:52cb90:8", "const:4:8"]]
+ 0052cb90 ["CALL", null, ["callee:00c58f80:8"]]
- 0052c870 bytes d0ad1c94
+ 0052cb90 bytes fcb01c94
~~~


<a id="compare-4868a706017ba15e10f3e328ad6fb4f5"></a>

### [`0052c874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c874.md) → [`0052cb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052cb94.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNS_17Certificate_StoreERKNSt6__ndk112basic_strin

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054ef50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ef50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f270.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5afe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c874.md#insn-0052c8d0) · [`0052c8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c874.md#insn-0052c8dc) · [`0052c918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c874.md#insn-0052c918)
- 新版 [`0052cbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052cb94.md#insn-0052cbf0) · [`0052cbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052cb94.md#insn-0052cbfc) · [`0052cc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052cb94.md#insn-0052cc38)

~~~diff
- 0052c8d0 ["INT_ADD", "register:40f0:8", ["const:52c8d0:8", "const:4:8"]]
- 0052c8d0 ["CALL", null, ["callee:0054f270:8"]]
+ 0052cbf0 ["INT_ADD", "register:40f0:8", ["const:52cbf0:8", "const:4:8"]]
+ 0052cbf0 ["CALL", null, ["callee:0054f270:8"]]
- 0052c8d0 bytes a0890094
+ 0052cbf0 bytes a0890094
- 0052c8dc ["INT_ADD", "register:40f0:8", ["const:52c8dc:8", "const:4:8"]]
- 0052c8dc ["CALL", null, ["callee:00c58f30:8"]]
+ 0052cbfc ["INT_ADD", "register:40f0:8", ["const:52cbfc:8", "const:4:8"]]
+ 0052cbfc ["CALL", null, ["callee:00c58f30:8"]]
- 0052c8dc bytes a1ad1c94
+ 0052cbfc bytes cdb01c94
- 0052c918 ["INT_ADD", "register:40f0:8", ["const:52c918:8", "const:4:8"]]
- 0052c918 ["CALL", null, ["callee:00c5afe0:8"]]
+ 0052cc38 ["INT_ADD", "register:40f0:8", ["const:52cc38:8", "const:4:8"]]
+ 0052cc38 ["CALL", null, ["callee:00c5afe0:8"]]
- 0052c918 bytes beb51c94
+ 0052cc38 bytes eab81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40abfa770b557f28494af32ccb4766a4"></a>

### [`0052c9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c9d8.md) → [`0052ccf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052ccf8.md) _ZN5Botan28Path_Validation_RestrictionsC1Ebmb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ca54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c9d8.md#insn-0052ca54) · [`0052ca6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c9d8.md#insn-0052ca6c) · [`0052caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c9d8.md#insn-0052caa0)
- 新版 [`0052cd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052ccf8.md#insn-0052cd74) · [`0052cd8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052ccf8.md#insn-0052cd8c) · [`0052cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052ccf8.md#insn-0052cdc0)

~~~diff
- 0052ca54 ["INT_ADD", "register:40f0:8", ["const:52ca54:8", "const:4:8"]]
- 0052ca54 ["CALL", null, ["callee:0054a974:8"]]
+ 0052cd74 ["INT_ADD", "register:40f0:8", ["const:52cd74:8", "const:4:8"]]
+ 0052cd74 ["CALL", null, ["callee:0054a974:8"]]
- 0052ca54 bytes 00770094
+ 0052cd74 bytes 00770094
- 0052ca6c ["INT_ADD", "register:40f0:8", ["const:52ca6c:8", "const:4:8"]]
- 0052ca6c ["CALL", null, ["callee:00c58f50:8"]]
+ 0052cd8c ["INT_ADD", "register:40f0:8", ["const:52cd8c:8", "const:4:8"]]
+ 0052cd8c ["CALL", null, ["callee:00c58f50:8"]]
- 0052ca6c bytes 45ad1c94
+ 0052cd8c bytes 71b01c94
- 0052caa0 ["INT_ADD", "register:40f0:8", ["const:52caa0:8", "const:4:8"]]
- 0052caa0 ["CALL", null, ["callee:0054a974:8"]]
+ 0052cdc0 ["INT_ADD", "register:40f0:8", ["const:52cdc0:8", "const:4:8"]]
+ 0052cdc0 ["CALL", null, ["callee:0054a974:8"]]
- 0052caa0 bytes ed760094
+ 0052cdc0 bytes ed760094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb1d86a22c72f8069df5b239a9a2ec24"></a>

### [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) → [`0052d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md) _ZN5Botan22Path_Validation_ResultC1ENSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a020.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00501df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`0053f370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f370.md) [`0053f584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f584.md)
- 新版 呼出元 1件 [`00c5aff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aff0.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00502118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502118.md) [`0052811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md) [`0053f690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f690.md) [`0053f8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f8a4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md#insn-0052ce90) · [`0052cec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md#insn-0052cec0) · [`0052ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md#insn-0052ced0)
- 新版 [`0052d1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md#insn-0052d1b0) · [`0052d1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md#insn-0052d1e0) · [`0052d1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d150.md#insn-0052d1f0)

~~~diff
- 0052ce90 ["INT_ADD", "register:40f0:8", ["const:52ce90:8", "const:4:8"]]
- 0052ce90 ["CALL", null, ["callee:0054eeec:8"]]
+ 0052d1b0 ["INT_ADD", "register:40f0:8", ["const:52d1b0:8", "const:4:8"]]
+ 0052d1b0 ["CALL", null, ["callee:0054eeec:8"]]
- 0052ce90 bytes 4f870094
+ 0052d1b0 bytes 4f870094
- 0052cec0 ["INT_ADD", "register:40f0:8", ["const:52cec0:8", "const:4:8"]]
- 0052cec0 ["CALL", null, ["callee:0053f690:8"]]
+ 0052d1e0 ["INT_ADD", "register:40f0:8", ["const:52d1e0:8", "const:4:8"]]
+ 0052d1e0 ["CALL", null, ["callee:0053f690:8"]]
- 0052cec0 bytes 2c490094
+ 0052d1e0 bytes 2c490094
- 0052ced0 ["INT_ADD", "register:40f0:8", ["const:52ced0:8", "const:4:8"]]
- 0052ced0 ["CALL", null, ["callee:0053fb70:8"]]
+ 0052d1f0 ["INT_ADD", "register:40f0:8", ["const:52d1f0:8", "const:4:8"]]
+ 0052d1f0 ["CALL", null, ["callee:0053fb70:8"]]
- 0052ced0 bytes 604a0094
+ 0052d1f0 bytes 604a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed62f76c29dae2a5b32bca2800297722"></a>

### [`0052d2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d2c4.md) → [`0052d5e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d5e4.md) _ZNK5Botan22Path_Validation_Result14trusted_hashesEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052d338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d2c4.md#insn-0052d338) · [`0052d348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d2c4.md#insn-0052d348) · [`0052d368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d2c4.md#insn-0052d368)
- 新版 [`0052d658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d5e4.md#insn-0052d658) · [`0052d668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d5e4.md#insn-0052d668) · [`0052d688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d5e4.md#insn-0052d688)

~~~diff
- 0052d338 ["INT_ADD", "register:40f0:8", ["const:52d338:8", "const:4:8"]]
- 0052d338 ["CALL", null, ["callee:00c5af30:8"]]
+ 0052d658 ["INT_ADD", "register:40f0:8", ["const:52d658:8", "const:4:8"]]
+ 0052d658 ["CALL", null, ["callee:00c5af30:8"]]
- 0052d338 bytes 0ab31c94
+ 0052d658 bytes 36b61c94
- 0052d348 ["INT_ADD", "register:40f0:8", ["const:52d348:8", "const:4:8"]]
- 0052d348 ["CALL", null, ["callee:0054a974:8"]]
+ 0052d668 ["INT_ADD", "register:40f0:8", ["const:52d668:8", "const:4:8"]]
+ 0052d668 ["CALL", null, ["callee:0054a974:8"]]
- 0052d348 bytes c3740094
+ 0052d668 bytes c3740094
- 0052d368 ["INT_ADD", "register:40f0:8", ["const:52d368:8", "const:4:8"]]
- 0052d368 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052d688 ["INT_ADD", "register:40f0:8", ["const:52d688:8", "const:4:8"]]
+ 0052d688 ["CALL", null, ["callee:00c58f30:8"]]
- 0052d368 bytes feaa1c94
+ 0052d688 bytes 2aae1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9e8816bb5c02ac79489c8b9cccc95d"></a>

### [`0052dc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dc4c.md) → [`0052df6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052df6c.md) FUN_0052df6c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 2件 [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dc4c.md#insn-0052dc70) · [`0052dcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dc4c.md#insn-0052dcb8) · [`0052dcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dc4c.md#insn-0052dcd8)
- 新版 [`0052df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052df6c.md#insn-0052df90) · [`0052dfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052df6c.md#insn-0052dfd8) · [`0052dff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052df6c.md#insn-0052dff8)

~~~diff
- 0052dc70 ["INT_ADD", "register:40f0:8", ["const:52dc70:8", "const:4:8"]]
- 0052dc70 ["CALL", null, ["callee:00c59080:8"]]
+ 0052df90 ["INT_ADD", "register:40f0:8", ["const:52df90:8", "const:4:8"]]
+ 0052df90 ["CALL", null, ["callee:00c59080:8"]]
- 0052dc70 bytes 10a91c94
+ 0052df90 bytes 3cac1c94
- 0052dcb8 ["INT_ADD", "register:40f0:8", ["const:52dcb8:8", "const:4:8"]]
- 0052dcb8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052dfd8 ["INT_ADD", "register:40f0:8", ["const:52dfd8:8", "const:4:8"]]
+ 0052dfd8 ["CALL", null, ["callee:00c58f30:8"]]
- 0052dcb8 bytes aaa81c94
+ 0052dfd8 bytes d6ab1c94
- 0052dcd8 ["INT_ADD", "register:40f0:8", ["const:52dcd8:8", "const:4:8"]]
- 0052dcd8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0052dff8 ["INT_ADD", "register:40f0:8", ["const:52dff8:8", "const:4:8"]]
+ 0052dff8 ["CALL", null, ["callee:00c58fe0:8"]]
- 0052dcd8 bytes cea81c94
+ 0052dff8 bytes faab1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bb2955a1ca83cb8ffc4e05bc26b3ec"></a>

### [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) → [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) FUN_0052e060

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 62件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) [`005ccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md) [`005db4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005db4c8.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0053bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bcf0.md) [`0054f1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f1d4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 62件 [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) [`005cd0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd0f4.md) [`005db878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005db/005db878.md) [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0053c010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053c010.md) [`0054f4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f4f4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md#insn-0052dd90) · [`0052ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md#insn-0052ddc0) · [`0052dddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md#insn-0052dddc)
- 新版 [`0052e0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md#insn-0052e0b0) · [`0052e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md#insn-0052e0e0) · [`0052e0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md#insn-0052e0fc)

~~~diff
- 0052dd90 ["INT_ADD", "register:40f0:8", ["const:52dd90:8", "const:4:8"]]
- 0052dd90 ["CALL", null, ["callee:0043bf04:8"]]
+ 0052e0b0 ["INT_ADD", "register:40f0:8", ["const:52e0b0:8", "const:4:8"]]
+ 0052e0b0 ["CALL", null, ["callee:0043bf04:8"]]
- 0052dd90 bytes 9537fc97
+ 0052e0b0 bytes 9537fc97
- 0052ddc0 ["INT_ADD", "register:40f0:8", ["const:52ddc0:8", "const:4:8"]]
- 0052ddc0 ["CALL", null, ["callee:0054f4f4:8"]]
+ 0052e0e0 ["INT_ADD", "register:40f0:8", ["const:52e0e0:8", "const:4:8"]]
+ 0052e0e0 ["CALL", null, ["callee:0054f4f4:8"]]
- 0052ddc0 bytes 05850094
+ 0052e0e0 bytes 05850094
- 0052dddc ["INT_ADD", "register:40f0:8", ["const:52dddc:8", "const:4:8"]]
- 0052dddc ["CALL", null, ["callee:0053c010:8"]]
+ 0052e0fc ["INT_ADD", "register:40f0:8", ["const:52e0fc:8", "const:4:8"]]
+ 0052e0fc ["CALL", null, ["callee:0053c010:8"]]
- 0052dddc bytes c5370094
+ 0052e0fc bytes c5370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a48aef68679cca8769183e7e7d35dc1f"></a>

### [`0052efbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052efbc.md) → [`0052f2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f2dc.md) FUN_0052f2dc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052efd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052efbc.md#insn-0052efd8)
- 新版 [`0052f2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f2dc.md#insn-0052f2f8)

~~~diff
- 0052efd8 ["INT_ADD", "register:40f0:8", ["const:52efd8:8", "const:4:8"]]
- 0052efd8 ["CALL", null, ["callee:00c58f50:8"]]
+ 0052f2f8 ["INT_ADD", "register:40f0:8", ["const:52f2f8:8", "const:4:8"]]
+ 0052f2f8 ["CALL", null, ["callee:00c58f50:8"]]
- 0052efd8 bytes eaa31c94
+ 0052f2f8 bytes 16a71c94
~~~


<a id="compare-f6b47b581032c92745f7a93a20f74e20"></a>

### [`0052f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f0f4.md) → [`0052f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f414.md) FUN_0052f414

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f320.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f0f4.md#insn-0052f104)
- 新版 [`0052f424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f414.md#insn-0052f424)

~~~diff
- 0052f104 ["INT_ADD", "register:40f0:8", ["const:52f104:8", "const:4:8"]]
- 0052f104 ["CALL", null, ["callee:0052f320:8"]]
+ 0052f424 ["INT_ADD", "register:40f0:8", ["const:52f424:8", "const:4:8"]]
+ 0052f424 ["CALL", null, ["callee:0052f320:8"]]
- 0052f104 bytes bfffff97
+ 0052f424 bytes bfffff97
~~~


<a id="compare-62a6650441531cbacade4800da96de82"></a>

### [`0052f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f3e0.md) → [`0052f700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f700.md) FUN_0052f700

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f60c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f3e0.md#insn-0052f3f0)
- 新版 [`0052f710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f700.md#insn-0052f710)

~~~diff
- 0052f3f0 ["INT_ADD", "register:40f0:8", ["const:52f3f0:8", "const:4:8"]]
- 0052f3f0 ["CALL", null, ["callee:0052f60c:8"]]
+ 0052f710 ["INT_ADD", "register:40f0:8", ["const:52f710:8", "const:4:8"]]
+ 0052f710 ["CALL", null, ["callee:0052f60c:8"]]
- 0052f3f0 bytes bfffff97
+ 0052f710 bytes bfffff97
~~~


<a id="compare-64fb0b91348acad66de9adfe5faa13fb"></a>

### [`0052f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f6cc.md) → [`0052f9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f9ec.md) FUN_0052f9ec

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8f8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f6cc.md#insn-0052f6dc)
- 新版 [`0052f9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f9ec.md#insn-0052f9fc)

~~~diff
- 0052f6dc ["INT_ADD", "register:40f0:8", ["const:52f6dc:8", "const:4:8"]]
- 0052f6dc ["CALL", null, ["callee:0052f8f8:8"]]
+ 0052f9fc ["INT_ADD", "register:40f0:8", ["const:52f9fc:8", "const:4:8"]]
+ 0052f9fc ["CALL", null, ["callee:0052f8f8:8"]]
- 0052f6dc bytes bfffff97
+ 0052f9fc bytes bfffff97
~~~


<a id="compare-ead894795fb80c87a6df96e11a576310"></a>

### [`0052fdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdbc.md) → [`005300dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005300dc.md) FUN_005300dc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdbc.md#insn-0052fdd8) · [`0052fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdbc.md#insn-0052fde8)
- 新版 [`005300f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005300dc.md#insn-005300f8) · [`00530108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005300dc.md#insn-00530108)

~~~diff
- 0052fdd8 ["INT_ADD", "register:40f0:8", ["const:52fdd8:8", "const:4:8"]]
- 0052fdd8 ["CALL", null, ["callee:00c58f50:8"]]
+ 005300f8 ["INT_ADD", "register:40f0:8", ["const:5300f8:8", "const:4:8"]]
+ 005300f8 ["CALL", null, ["callee:00c58f50:8"]]
- 0052fdd8 bytes 6aa01c94
+ 005300f8 bytes 96a31c94
- 0052fde8 ["INT_ADD", "register:40f0:8", ["const:52fde8:8", "const:4:8"]]
- 0052fde8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00530108 ["INT_ADD", "register:40f0:8", ["const:530108:8", "const:4:8"]]
+ 00530108 ["CALL", null, ["callee:00c58f50:8"]]
- 0052fde8 bytes 66a01c94
+ 00530108 bytes 92a31c94
~~~


<a id="compare-4eca38b0809971696039a374704c3ed3"></a>

### [`0052fdfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdfc.md) → [`0053011c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053011c.md) FUN_0053011c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdfc.md#insn-0052fe1c)
- 新版 [`0053013c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053011c.md#insn-0053013c)

~~~diff
- 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
- 0052fe1c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053013c ["INT_ADD", "register:40f0:8", ["const:53013c:8", "const:4:8"]]
+ 0053013c ["CALL", null, ["callee:00c58f50:8"]]
- 0052fe1c bytes 59a01c94
+ 0053013c bytes 85a31c94
~~~


<a id="compare-5f99273b084cc88aa9186f430c53e0c8"></a>

### [`0052fe30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe30.md) → [`00530150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530150.md) FUN_00530150

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe30.md#insn-0052fe4c) · [`0052fe5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe30.md#insn-0052fe5c)
- 新版 [`0053016c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530150.md#insn-0053016c) · [`0053017c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530150.md#insn-0053017c)

~~~diff
- 0052fe4c ["INT_ADD", "register:40f0:8", ["const:52fe4c:8", "const:4:8"]]
- 0052fe4c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053016c ["INT_ADD", "register:40f0:8", ["const:53016c:8", "const:4:8"]]
+ 0053016c ["CALL", null, ["callee:00c58f50:8"]]
- 0052fe4c bytes 4da01c94
+ 0053016c bytes 79a31c94
- 0052fe5c ["INT_ADD", "register:40f0:8", ["const:52fe5c:8", "const:4:8"]]
- 0052fe5c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053017c ["INT_ADD", "register:40f0:8", ["const:53017c:8", "const:4:8"]]
+ 0053017c ["CALL", null, ["callee:00c58f50:8"]]
- 0052fe5c bytes 49a01c94
+ 0053017c bytes 75a31c94
~~~


<a id="compare-f4be85f6a268bfd63510802f81c72d35"></a>

### [`0052fe70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe70.md) → [`00530190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530190.md) FUN_00530190

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe70.md#insn-0052fe8c) · [`0052fe9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe70.md#insn-0052fe9c)
- 新版 [`005301ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530190.md#insn-005301ac) · [`005301bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530190.md#insn-005301bc)

~~~diff
- 0052fe8c ["INT_ADD", "register:40f0:8", ["const:52fe8c:8", "const:4:8"]]
- 0052fe8c ["CALL", null, ["callee:00c58f50:8"]]
+ 005301ac ["INT_ADD", "register:40f0:8", ["const:5301ac:8", "const:4:8"]]
+ 005301ac ["CALL", null, ["callee:00c58f50:8"]]
- 0052fe8c bytes 3da01c94
+ 005301ac bytes 69a31c94
- 0052fe9c ["INT_ADD", "register:40f0:8", ["const:52fe9c:8", "const:4:8"]]
- 0052fe9c ["CALL", null, ["callee:00c58f50:8"]]
+ 005301bc ["INT_ADD", "register:40f0:8", ["const:5301bc:8", "const:4:8"]]
+ 005301bc ["CALL", null, ["callee:00c58f50:8"]]
- 0052fe9c bytes 39a01c94
+ 005301bc bytes 65a31c94
~~~


<a id="compare-e0066a514307ece37e5d30884a998edf"></a>

### [`005303fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005303fc.md) → [`0053071c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053071c.md) FUN_0053071c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00530328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530648.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053040c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005303fc.md#insn-0053040c)
- 新版 [`0053072c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053071c.md#insn-0053072c)

~~~diff
- 0053040c ["INT_ADD", "register:40f0:8", ["const:53040c:8", "const:4:8"]]
- 0053040c ["CALL", null, ["callee:00530648:8"]]
+ 0053072c ["INT_ADD", "register:40f0:8", ["const:53072c:8", "const:4:8"]]
+ 0053072c ["CALL", null, ["callee:00530648:8"]]
- 0053040c bytes c7ffff97
+ 0053072c bytes c7ffff97
~~~


<a id="compare-081181781815eacd2b03eb7ff204a645"></a>

### [`00530420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530420.md) → [`00530740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530740.md) FUN_00530740

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cbc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbc90.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbfb0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530420.md#insn-00530430) · [`00530438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530420.md#insn-00530438)
- 新版 [`00530750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530740.md#insn-00530750) · [`00530758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530740.md#insn-00530758)

~~~diff
- 00530430 ["INT_ADD", "register:40f0:8", ["const:530430:8", "const:4:8"]]
- 00530430 ["CALL", null, ["callee:00c58f30:8"]]
+ 00530750 ["INT_ADD", "register:40f0:8", ["const:530750:8", "const:4:8"]]
+ 00530750 ["CALL", null, ["callee:00c58f30:8"]]
- 00530430 bytes cc9e1c94
+ 00530750 bytes f8a11c94
- 00530438 ["INT_ADD", "register:40f0:8", ["const:530438:8", "const:4:8"]]
- 00530438 ["CALL", null, ["callee:004cbfb0:8"]]
+ 00530758 ["INT_ADD", "register:40f0:8", ["const:530758:8", "const:4:8"]]
+ 00530758 ["CALL", null, ["callee:004cbfb0:8"]]
- 00530438 bytes 166efe97
+ 00530758 bytes 166efe97
~~~


<a id="compare-a2f6ddce202659dc093ab06d6609f5b7"></a>

### [`0053047c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053047c.md) → [`0053079c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053079c.md) FUN_0053079c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053047c.md#insn-00530498) · [`005304a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053047c.md#insn-005304a4)
- 新版 [`005307b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053079c.md#insn-005307b8) · [`005307c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053079c.md#insn-005307c4)

~~~diff
- 00530498 ["INT_ADD", "register:40f0:8", ["const:530498:8", "const:4:8"]]
- 00530498 ["CALL", null, ["callee:00c58f50:8"]]
+ 005307b8 ["INT_ADD", "register:40f0:8", ["const:5307b8:8", "const:4:8"]]
+ 005307b8 ["CALL", null, ["callee:00c58f50:8"]]
- 00530498 bytes ba9e1c94
+ 005307b8 bytes e6a11c94
- 005304a4 ["INT_ADD", "register:40f0:8", ["const:5304a4:8", "const:4:8"]]
- 005304a4 ["CALL", null, ["callee:0053b2f0:8"]]
+ 005307c4 ["INT_ADD", "register:40f0:8", ["const:5307c4:8", "const:4:8"]]
+ 005307c4 ["CALL", null, ["callee:0053b2f0:8"]]
- 005304a4 bytes cb2a0094
+ 005307c4 bytes cb2a0094
~~~


<a id="compare-d9236d49ae6c5453f205fd6d894311cd"></a>

### [`00530650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530650.md) → [`00530970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530970.md) FUN_00530970

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530650.md#insn-00530678)
- 新版 [`00530998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530970.md#insn-00530998)

~~~diff
- 00530678 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530678 ["INT_ADD", "register:40f0:8", ["const:530678:8", "const:4:8"]]
- 00530678 ["CALLIND", null, ["register:0:8"]]
+ 00530998 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530998 ["INT_ADD", "register:40f0:8", ["const:530998:8", "const:4:8"]]
+ 00530998 ["CALLIND", null, ["register:0:8"]]
- 00530678 bytes 20013fd6
+ 00530998 bytes 20013fd6
~~~


<a id="compare-6bbe5b24d395bf96332ec9124ffbe795"></a>

### [`005308f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005308f8.md) → [`00530c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530c18.md) FUN_00530c18

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005308f8.md#insn-00530908)
- 新版 [`00530c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530c18.md#insn-00530c28)

~~~diff
- 00530908 ["INT_ADD", "register:40f0:8", ["const:530908:8", "const:4:8"]]
- 00530908 ["CALL", null, ["callee:00530b2c:8"]]
+ 00530c28 ["INT_ADD", "register:40f0:8", ["const:530c28:8", "const:4:8"]]
+ 00530c28 ["CALL", null, ["callee:00530b2c:8"]]
- 00530908 bytes c1ffff97
+ 00530c28 bytes c1ffff97
~~~


<a id="compare-9bac66e764e75d80e4f7b1049437ed4c"></a>

### [`0053098c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053098c.md) → [`00530cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cac.md) FUN_00530cac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005309a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053098c.md#insn-005309a0)
- 新版 [`00530cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cac.md#insn-00530cc0)

~~~diff
- 005309a0 ["INT_ADD", "register:40f0:8", ["const:5309a0:8", "const:4:8"]]
- 005309a0 ["CALL", null, ["callee:00530b2c:8"]]
+ 00530cc0 ["INT_ADD", "register:40f0:8", ["const:530cc0:8", "const:4:8"]]
+ 00530cc0 ["CALL", null, ["callee:00530b2c:8"]]
- 005309a0 bytes 9bffff97
+ 00530cc0 bytes 9bffff97
~~~


<a id="compare-41a498a3a6caf7605801111ffa804cea"></a>

### [`00530a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530a88.md) → [`00530da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530da8.md) FUN_00530da8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005309b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cd4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530a88.md#insn-00530a98)
- 新版 [`00530db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530da8.md#insn-00530db8)

~~~diff
- 00530a98 ["INT_ADD", "register:40f0:8", ["const:530a98:8", "const:4:8"]]
- 00530a98 ["CALL", null, ["callee:00530cd4:8"]]
+ 00530db8 ["INT_ADD", "register:40f0:8", ["const:530db8:8", "const:4:8"]]
+ 00530db8 ["CALL", null, ["callee:00530cd4:8"]]
- 00530a98 bytes c7ffff97
+ 00530db8 bytes c7ffff97
~~~


<a id="compare-22ab2c8713d5c4a1a2f9c9dfe9d1ff38"></a>

### [`00530aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530aac.md) → [`00530dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530dcc.md) FUN_00530dcc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb76c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cba8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cba8c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530aac.md#insn-00530abc) · [`00530ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530aac.md#insn-00530ac4)
- 新版 [`00530ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530dcc.md#insn-00530ddc) · [`00530de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530dcc.md#insn-00530de4)

~~~diff
- 00530abc ["INT_ADD", "register:40f0:8", ["const:530abc:8", "const:4:8"]]
- 00530abc ["CALL", null, ["callee:00c58f30:8"]]
+ 00530ddc ["INT_ADD", "register:40f0:8", ["const:530ddc:8", "const:4:8"]]
+ 00530ddc ["CALL", null, ["callee:00c58f30:8"]]
- 00530abc bytes 299d1c94
+ 00530ddc bytes 55a01c94
- 00530ac4 ["INT_ADD", "register:40f0:8", ["const:530ac4:8", "const:4:8"]]
- 00530ac4 ["CALL", null, ["callee:004cba8c:8"]]
+ 00530de4 ["INT_ADD", "register:40f0:8", ["const:530de4:8", "const:4:8"]]
+ 00530de4 ["CALL", null, ["callee:004cba8c:8"]]
- 00530ac4 bytes 2a6bfe97
+ 00530de4 bytes 2a6bfe97
~~~


<a id="compare-44166ed134146c336e8701f2feff9b17"></a>

### [`00530c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530c54.md) → [`00530f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530f74.md) FUN_00530f74

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb928.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbc48.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530c54.md#insn-00530c64) · [`00530c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530c54.md#insn-00530c6c)
- 新版 [`00530f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530f74.md#insn-00530f84) · [`00530f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530f74.md#insn-00530f8c)

~~~diff
- 00530c64 ["INT_ADD", "register:40f0:8", ["const:530c64:8", "const:4:8"]]
- 00530c64 ["CALL", null, ["callee:00c58f30:8"]]
+ 00530f84 ["INT_ADD", "register:40f0:8", ["const:530f84:8", "const:4:8"]]
+ 00530f84 ["CALL", null, ["callee:00c58f30:8"]]
- 00530c64 bytes bf9c1c94
+ 00530f84 bytes eb9f1c94
- 00530c6c ["INT_ADD", "register:40f0:8", ["const:530c6c:8", "const:4:8"]]
- 00530c6c ["CALL", null, ["callee:004cbc48:8"]]
+ 00530f8c ["INT_ADD", "register:40f0:8", ["const:530f8c:8", "const:4:8"]]
+ 00530f8c ["CALL", null, ["callee:004cbc48:8"]]
- 00530c6c bytes 2f6bfe97
+ 00530f8c bytes 2f6bfe97
~~~


<a id="compare-528049ffb334478355906f14fea96935"></a>

### [`00530dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530dfc.md) → [`0053111c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053111c.md) FUN_0053111c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cbadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbadc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbdfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbdfc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530dfc.md#insn-00530e0c) · [`00530e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530dfc.md#insn-00530e14)
- 新版 [`0053112c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053111c.md#insn-0053112c) · [`00531134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053111c.md#insn-00531134)

~~~diff
- 00530e0c ["INT_ADD", "register:40f0:8", ["const:530e0c:8", "const:4:8"]]
- 00530e0c ["CALL", null, ["callee:00c58f30:8"]]
+ 0053112c ["INT_ADD", "register:40f0:8", ["const:53112c:8", "const:4:8"]]
+ 0053112c ["CALL", null, ["callee:00c58f30:8"]]
- 00530e0c bytes 559c1c94
+ 0053112c bytes 819f1c94
- 00530e14 ["INT_ADD", "register:40f0:8", ["const:530e14:8", "const:4:8"]]
- 00530e14 ["CALL", null, ["callee:004cbdfc:8"]]
+ 00531134 ["INT_ADD", "register:40f0:8", ["const:531134:8", "const:4:8"]]
+ 00531134 ["CALL", null, ["callee:004cbdfc:8"]]
- 00530e14 bytes 326bfe97
+ 00531134 bytes 326bfe97
~~~


<a id="compare-3ad1e3c9d394837e9a032bf37dd22160"></a>

### [`00530e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530e64.md) → [`00531184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531184.md) FUN_00531184

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530e64.md#insn-00530e80) · [`00530eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530e64.md#insn-00530eb8) · [`00530ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530e64.md#insn-00530ec8)
- 新版 [`005311a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531184.md#insn-005311a0) · [`005311d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531184.md#insn-005311d8) · [`005311e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531184.md#insn-005311e8)

~~~diff
- 00530e80 ["INT_ADD", "register:40f0:8", ["const:530e80:8", "const:4:8"]]
- 00530e80 ["CALL", null, ["callee:0053b784:8"]]
+ 005311a0 ["INT_ADD", "register:40f0:8", ["const:5311a0:8", "const:4:8"]]
+ 005311a0 ["CALL", null, ["callee:0053b784:8"]]
- 00530e80 bytes 79290094
+ 005311a0 bytes 79290094
- 00530eb8 ["INT_ADD", "register:40f0:8", ["const:530eb8:8", "const:4:8"]]
- 00530eb8 ["CALL", null, ["callee:00c58f50:8"]]
+ 005311d8 ["INT_ADD", "register:40f0:8", ["const:5311d8:8", "const:4:8"]]
+ 005311d8 ["CALL", null, ["callee:00c58f50:8"]]
- 00530eb8 bytes 329c1c94
+ 005311d8 bytes 5e9f1c94
- 00530ec8 ["INT_ADD", "register:40f0:8", ["const:530ec8:8", "const:4:8"]]
- 00530ec8 ["CALL", null, ["callee:00c58f50:8"]]
+ 005311e8 ["INT_ADD", "register:40f0:8", ["const:5311e8:8", "const:4:8"]]
+ 005311e8 ["CALL", null, ["callee:00c58f50:8"]]
- 00530ec8 bytes 2e9c1c94
+ 005311e8 bytes 5a9f1c94
~~~


<a id="compare-ad42211579b8844417b4ce19fead9a28"></a>

### [`00531310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531310.md) → [`00531630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531630.md) FUN_00531630

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531310.md#insn-00531330)
- 新版 [`00531650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531630.md#insn-00531650)

~~~diff
- 00531330 ["INT_ADD", "register:40f0:8", ["const:531330:8", "const:4:8"]]
- 00531330 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531650 ["INT_ADD", "register:40f0:8", ["const:531650:8", "const:4:8"]]
+ 00531650 ["CALL", null, ["callee:00c58f50:8"]]
- 00531330 bytes 149b1c94
+ 00531650 bytes 409e1c94
~~~


<a id="compare-8c1b09230dd3abc3eceba86f01e78776"></a>

### [`00531518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531518.md) → [`00531838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531838.md) FUN_00531838

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531518.md#insn-00531538)
- 新版 [`00531858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531838.md#insn-00531858)

~~~diff
- 00531538 ["INT_ADD", "register:40f0:8", ["const:531538:8", "const:4:8"]]
- 00531538 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531858 ["INT_ADD", "register:40f0:8", ["const:531858:8", "const:4:8"]]
+ 00531858 ["CALL", null, ["callee:00c58f50:8"]]
- 00531538 bytes 929a1c94
+ 00531858 bytes be9d1c94
~~~


<a id="compare-d78b7f8b46014ca8173340484d6d5faa"></a>

### [`0053155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053155c.md) → [`0053187c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053187c.md) FUN_0053187c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053155c.md#insn-00531574) · [`00531580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053155c.md#insn-00531580)
- 新版 [`00531894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053187c.md#insn-00531894) · [`005318a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053187c.md#insn-005318a0)

~~~diff
- 00531574 ["INT_ADD", "register:40f0:8", ["const:531574:8", "const:4:8"]]
- 00531574 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00531894 ["INT_ADD", "register:40f0:8", ["const:531894:8", "const:4:8"]]
+ 00531894 ["CALL", null, ["callee:0053b2f0:8"]]
- 00531574 bytes 97260094
+ 00531894 bytes 97260094
- 00531580 ["INT_ADD", "register:40f0:8", ["const:531580:8", "const:4:8"]]
- 00531580 ["CALL", null, ["callee:0046d7f0:8"]]
+ 005318a0 ["INT_ADD", "register:40f0:8", ["const:5318a0:8", "const:4:8"]]
+ 005318a0 ["CALL", null, ["callee:0046d7f0:8"]]
- 00531580 bytes d4effc97
+ 005318a0 bytes d4effc97
~~~


<a id="compare-b37e89c182f326d1eb29ba9a701a0e63"></a>

### [`005316e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005316e4.md) → [`00531a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a04.md) FUN_00531a04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005316fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005316e4.md#insn-005316fc)
- 新版 [`00531a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a04.md#insn-00531a1c)

~~~diff
- 005316fc ["INT_ADD", "register:40f0:8", ["const:5316fc:8", "const:4:8"]]
- 005316fc ["CALL", null, ["callee:0053b2f0:8"]]
+ 00531a1c ["INT_ADD", "register:40f0:8", ["const:531a1c:8", "const:4:8"]]
+ 00531a1c ["CALL", null, ["callee:0053b2f0:8"]]
- 005316fc bytes 35260094
+ 00531a1c bytes 35260094
~~~


<a id="compare-b9e78ab05247cf638a9c97021c28a5d3"></a>

### [`00531714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531714.md) → [`00531a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a34.md) FUN_00531a34

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531714.md#insn-0053172c) · [`00531738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531714.md#insn-00531738)
- 新版 [`00531a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a34.md#insn-00531a4c) · [`00531a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a34.md#insn-00531a58)

~~~diff
- 0053172c ["INT_ADD", "register:40f0:8", ["const:53172c:8", "const:4:8"]]
- 0053172c ["CALL", null, ["callee:0053b2f0:8"]]
+ 00531a4c ["INT_ADD", "register:40f0:8", ["const:531a4c:8", "const:4:8"]]
+ 00531a4c ["CALL", null, ["callee:0053b2f0:8"]]
- 0053172c bytes 29260094
+ 00531a4c bytes 29260094
- 00531738 ["INT_ADD", "register:40f0:8", ["const:531738:8", "const:4:8"]]
- 00531738 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00531a58 ["INT_ADD", "register:40f0:8", ["const:531a58:8", "const:4:8"]]
+ 00531a58 ["CALL", null, ["callee:0046d7f0:8"]]
- 00531738 bytes 66effc97
+ 00531a58 bytes 66effc97
~~~


<a id="compare-783ce80b58461d4690f29c56d7edc297"></a>

### [`005318b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318b4.md) → [`00531bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531bd4.md) FUN_00531bd4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005318cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318b4.md#insn-005318cc)
- 新版 [`00531bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531bd4.md#insn-00531bec)

~~~diff
- 005318cc ["INT_ADD", "register:40f0:8", ["const:5318cc:8", "const:4:8"]]
- 005318cc ["CALL", null, ["callee:0053b2f0:8"]]
+ 00531bec ["INT_ADD", "register:40f0:8", ["const:531bec:8", "const:4:8"]]
+ 00531bec ["CALL", null, ["callee:0053b2f0:8"]]
- 005318cc bytes c1250094
+ 00531bec bytes c1250094
~~~


<a id="compare-312e11fd468d17da11fa742f4359b7db"></a>

### [`005318e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318e4.md) → [`00531c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c04.md) FUN_00531c04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005318fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318e4.md#insn-005318fc) · [`00531908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318e4.md#insn-00531908)
- 新版 [`00531c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c04.md#insn-00531c1c) · [`00531c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c04.md#insn-00531c28)

~~~diff
- 005318fc ["INT_ADD", "register:40f0:8", ["const:5318fc:8", "const:4:8"]]
- 005318fc ["CALL", null, ["callee:0053b2f0:8"]]
+ 00531c1c ["INT_ADD", "register:40f0:8", ["const:531c1c:8", "const:4:8"]]
+ 00531c1c ["CALL", null, ["callee:0053b2f0:8"]]
- 005318fc bytes b5250094
+ 00531c1c bytes b5250094
- 00531908 ["INT_ADD", "register:40f0:8", ["const:531908:8", "const:4:8"]]
- 00531908 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00531c28 ["INT_ADD", "register:40f0:8", ["const:531c28:8", "const:4:8"]]
+ 00531c28 ["CALL", null, ["callee:0046d7f0:8"]]
- 00531908 bytes f2eefc97
+ 00531c28 bytes f2eefc97
~~~


<a id="compare-d3889fe1ed1e00d28be615b655a1972e"></a>

### [`00531b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531b4c.md) → [`00531e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531e6c.md) FUN_00531e6c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531b4c.md#insn-00531b94)
- 新版 [`00531eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531e6c.md#insn-00531eb4)

~~~diff
- 00531b94 ["INT_ADD", "register:40f0:8", ["const:531b94:8", "const:4:8"]]
- 00531b94 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531eb4 ["INT_ADD", "register:40f0:8", ["const:531eb4:8", "const:4:8"]]
+ 00531eb4 ["CALL", null, ["callee:00c58f50:8"]]
- 00531b94 bytes fb981c94
+ 00531eb4 bytes 279c1c94
~~~


<a id="compare-431772a3f8d4d785bd66031ca57115a7"></a>

### [`00531bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md) → [`00531ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531ee4.md) FUN_00531ee4

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0050f74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md#insn-00531c0c) · [`00531c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md#insn-00531c1c)
- 新版 [`00531f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531ee4.md#insn-00531f2c) · [`00531f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531ee4.md#insn-00531f3c)

~~~diff
- 00531c0c ["INT_ADD", "register:40f0:8", ["const:531c0c:8", "const:4:8"]]
- 00531c0c ["CALL", null, ["callee:00c58f50:8"]]
+ 00531f2c ["INT_ADD", "register:40f0:8", ["const:531f2c:8", "const:4:8"]]
+ 00531f2c ["CALL", null, ["callee:00c58f50:8"]]
- 00531c0c bytes dd981c94
+ 00531f2c bytes 099c1c94
- 00531c1c ["INT_ADD", "register:40f0:8", ["const:531c1c:8", "const:4:8"]]
- 00531c1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00531f3c ["INT_ADD", "register:40f0:8", ["const:531f3c:8", "const:4:8"]]
+ 00531f3c ["CALL", null, ["callee:00c58f50:8"]]
- 00531c1c bytes d9981c94
+ 00531f3c bytes 059c1c94
~~~


<a id="compare-2efa5aacd27ceac09bd5b206e323733c"></a>

### [`00531d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d74.md) → [`00532094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532094.md) FUN_00532094

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051b024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d74.md#insn-00531d88)
- 新版 [`005320a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532094.md#insn-005320a8)

~~~diff
- 00531d88 ["INT_ADD", "register:40f0:8", ["const:531d88:8", "const:4:8"]]
- 00531d88 ["CALL", null, ["callee:0051b024:8"]]
+ 005320a8 ["INT_ADD", "register:40f0:8", ["const:5320a8:8", "const:4:8"]]
+ 005320a8 ["CALL", null, ["callee:0051b024:8"]]
- 00531d88 bytes dfa3ff97
+ 005320a8 bytes dfa3ff97
~~~


<a id="compare-ad512524bc795fe69200fc14c4b41e2f"></a>

### [`00531fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531fbc.md) → [`005322dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005322dc.md) FUN_005322dc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531fbc.md#insn-00532004)
- 新版 [`00532324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005322dc.md#insn-00532324)

~~~diff
- 00532004 ["INT_ADD", "register:40f0:8", ["const:532004:8", "const:4:8"]]
- 00532004 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532324 ["INT_ADD", "register:40f0:8", ["const:532324:8", "const:4:8"]]
+ 00532324 ["CALL", null, ["callee:00c58f50:8"]]
- 00532004 bytes df971c94
+ 00532324 bytes 0b9b1c94
~~~


<a id="compare-ce5187f36d3645adfd623e9a49068385"></a>

### [`00532034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532034.md) → [`00532354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532354.md) FUN_00532354

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532034.md#insn-0053207c) · [`0053208c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532034.md#insn-0053208c)
- 新版 [`0053239c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532354.md#insn-0053239c) · [`005323ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532354.md#insn-005323ac)

~~~diff
- 0053207c ["INT_ADD", "register:40f0:8", ["const:53207c:8", "const:4:8"]]
- 0053207c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053239c ["INT_ADD", "register:40f0:8", ["const:53239c:8", "const:4:8"]]
+ 0053239c ["CALL", null, ["callee:00c58f50:8"]]
- 0053207c bytes c1971c94
+ 0053239c bytes ed9a1c94
- 0053208c ["INT_ADD", "register:40f0:8", ["const:53208c:8", "const:4:8"]]
- 0053208c ["CALL", null, ["callee:00c58f50:8"]]
+ 005323ac ["INT_ADD", "register:40f0:8", ["const:5323ac:8", "const:4:8"]]
+ 005323ac ["CALL", null, ["callee:00c58f50:8"]]
- 0053208c bytes bd971c94
+ 005323ac bytes e99a1c94
~~~


<a id="compare-18680309959af18646759b14df727774"></a>

### [`00532274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532274.md) → [`00532594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532594.md) FUN_00532594

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005322c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532274.md#insn-005322c0) · [`005322d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532274.md#insn-005322d0)
- 新版 [`005325e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532594.md#insn-005325e0) · [`005325f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532594.md#insn-005325f0)

~~~diff
- 005322c0 ["INT_ADD", "register:40f0:8", ["const:5322c0:8", "const:4:8"]]
- 005322c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005325e0 ["INT_ADD", "register:40f0:8", ["const:5325e0:8", "const:4:8"]]
+ 005325e0 ["CALL", null, ["callee:00c58f50:8"]]
- 005322c0 bytes 30971c94
+ 005325e0 bytes 5c9a1c94
- 005322d0 ["INT_ADD", "register:40f0:8", ["const:5322d0:8", "const:4:8"]]
- 005322d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005325f0 ["INT_ADD", "register:40f0:8", ["const:5325f0:8", "const:4:8"]]
+ 005325f0 ["CALL", null, ["callee:00c58f50:8"]]
- 005322d0 bytes 2c971c94
+ 005325f0 bytes 589a1c94
~~~


<a id="compare-96ed2adbe598ca4f597104c80c6403b7"></a>

### [`00532300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532300.md) → [`00532620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532620.md) FUN_00532620

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053234c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532300.md#insn-0053234c) · [`0053235c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532300.md#insn-0053235c) · [`0053236c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532300.md#insn-0053236c)
- 新版 [`0053266c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532620.md#insn-0053266c) · [`0053267c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532620.md#insn-0053267c) · [`0053268c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532620.md#insn-0053268c)

~~~diff
- 0053234c ["INT_ADD", "register:40f0:8", ["const:53234c:8", "const:4:8"]]
- 0053234c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053266c ["INT_ADD", "register:40f0:8", ["const:53266c:8", "const:4:8"]]
+ 0053266c ["CALL", null, ["callee:00c58f50:8"]]
- 0053234c bytes 0d971c94
+ 0053266c bytes 399a1c94
- 0053235c ["INT_ADD", "register:40f0:8", ["const:53235c:8", "const:4:8"]]
- 0053235c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053267c ["INT_ADD", "register:40f0:8", ["const:53267c:8", "const:4:8"]]
+ 0053267c ["CALL", null, ["callee:00c58f50:8"]]
- 0053235c bytes 09971c94
+ 0053267c bytes 359a1c94
- 0053236c ["INT_ADD", "register:40f0:8", ["const:53236c:8", "const:4:8"]]
- 0053236c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053268c ["INT_ADD", "register:40f0:8", ["const:53268c:8", "const:4:8"]]
+ 0053268c ["CALL", null, ["callee:00c58f50:8"]]
- 0053236c bytes 05971c94
+ 0053268c bytes 319a1c94
~~~


<a id="compare-d03ddcfd71b4ae1adead1ace2ebc5bdd"></a>

### [`00532700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532700.md) → [`00532a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532a20.md) FUN_00532a20

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053274c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532700.md#insn-0053274c) · [`0053275c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532700.md#insn-0053275c) · [`00532784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532700.md#insn-00532784)
- 新版 [`00532a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532a20.md#insn-00532a6c) · [`00532a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532a20.md#insn-00532a7c) · [`00532aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532a20.md#insn-00532aa4)

~~~diff
- 0053274c ["INT_ADD", "register:40f0:8", ["const:53274c:8", "const:4:8"]]
- 0053274c ["CALL", null, ["callee:00c58f50:8"]]
+ 00532a6c ["INT_ADD", "register:40f0:8", ["const:532a6c:8", "const:4:8"]]
+ 00532a6c ["CALL", null, ["callee:00c58f50:8"]]
- 0053274c bytes 0d961c94
+ 00532a6c bytes 39991c94
- 0053275c ["INT_ADD", "register:40f0:8", ["const:53275c:8", "const:4:8"]]
- 0053275c ["CALL", null, ["callee:00c58f50:8"]]
+ 00532a7c ["INT_ADD", "register:40f0:8", ["const:532a7c:8", "const:4:8"]]
+ 00532a7c ["CALL", null, ["callee:00c58f50:8"]]
- 0053275c bytes 09961c94
+ 00532a7c bytes 35991c94
- 00532784 ["INT_ADD", "register:40f0:8", ["const:532784:8", "const:4:8"]]
- 00532784 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532aa4 ["INT_ADD", "register:40f0:8", ["const:532aa4:8", "const:4:8"]]
+ 00532aa4 ["CALL", null, ["callee:0053b2f0:8"]]
- 00532784 bytes 13220094
+ 00532aa4 bytes 13220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71f4cc5b666e751a82956412f89529af"></a>

### [`005327cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005327cc.md) → [`00532aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532aec.md) FUN_00532aec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005327cc.md#insn-00532818) · [`00532828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005327cc.md#insn-00532828) · [`00532850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005327cc.md#insn-00532850)
- 新版 [`00532b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532aec.md#insn-00532b38) · [`00532b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532aec.md#insn-00532b48) · [`00532b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532aec.md#insn-00532b70)

~~~diff
- 00532818 ["INT_ADD", "register:40f0:8", ["const:532818:8", "const:4:8"]]
- 00532818 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532b38 ["INT_ADD", "register:40f0:8", ["const:532b38:8", "const:4:8"]]
+ 00532b38 ["CALL", null, ["callee:00c58f50:8"]]
- 00532818 bytes da951c94
+ 00532b38 bytes 06991c94
- 00532828 ["INT_ADD", "register:40f0:8", ["const:532828:8", "const:4:8"]]
- 00532828 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532b48 ["INT_ADD", "register:40f0:8", ["const:532b48:8", "const:4:8"]]
+ 00532b48 ["CALL", null, ["callee:00c58f50:8"]]
- 00532828 bytes d6951c94
+ 00532b48 bytes 02991c94
- 00532850 ["INT_ADD", "register:40f0:8", ["const:532850:8", "const:4:8"]]
- 00532850 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532b70 ["INT_ADD", "register:40f0:8", ["const:532b70:8", "const:4:8"]]
+ 00532b70 ["CALL", null, ["callee:0053b2f0:8"]]
- 00532850 bytes e0210094
+ 00532b70 bytes e0210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e5b597fbe33ae3e1e7d102135972890"></a>

### [`005328a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328a0.md) → [`00532bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532bc0.md) FUN_00532bc0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005328b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328a0.md#insn-005328b8)
- 新版 [`00532bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532bc0.md#insn-00532bd8)

~~~diff
- 005328b8 ["INT_ADD", "register:40f0:8", ["const:5328b8:8", "const:4:8"]]
- 005328b8 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532bd8 ["INT_ADD", "register:40f0:8", ["const:532bd8:8", "const:4:8"]]
+ 00532bd8 ["CALL", null, ["callee:0053b2f0:8"]]
- 005328b8 bytes c6210094
+ 00532bd8 bytes c6210094
~~~


<a id="compare-6954bd73639b26a8835d198a91503b21"></a>

### [`005328d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328d0.md) → [`00532bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532bf0.md) FUN_00532bf0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005328e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328d0.md#insn-005328e8) · [`005328f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328d0.md#insn-005328f4)
- 新版 [`00532c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532bf0.md#insn-00532c08) · [`00532c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532bf0.md#insn-00532c14)

~~~diff
- 005328e8 ["INT_ADD", "register:40f0:8", ["const:5328e8:8", "const:4:8"]]
- 005328e8 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532c08 ["INT_ADD", "register:40f0:8", ["const:532c08:8", "const:4:8"]]
+ 00532c08 ["CALL", null, ["callee:0053b2f0:8"]]
- 005328e8 bytes ba210094
+ 00532c08 bytes ba210094
- 005328f4 ["INT_ADD", "register:40f0:8", ["const:5328f4:8", "const:4:8"]]
- 005328f4 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00532c14 ["INT_ADD", "register:40f0:8", ["const:532c14:8", "const:4:8"]]
+ 00532c14 ["CALL", null, ["callee:0046d7f0:8"]]
- 005328f4 bytes f7eafc97
+ 00532c14 bytes f7eafc97
~~~


<a id="compare-bcae73fd9f141ac95931fcd60cd07439"></a>

### [`00532a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a60.md) → [`00532d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d80.md) FUN_00532d80

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a60.md#insn-00532a78)
- 新版 [`00532d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d80.md#insn-00532d98)

~~~diff
- 00532a78 ["INT_ADD", "register:40f0:8", ["const:532a78:8", "const:4:8"]]
- 00532a78 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532d98 ["INT_ADD", "register:40f0:8", ["const:532d98:8", "const:4:8"]]
+ 00532d98 ["CALL", null, ["callee:0053b2f0:8"]]
- 00532a78 bytes 56210094
+ 00532d98 bytes 56210094
~~~


<a id="compare-f59585630bdf81d48889a6cd16aa80e5"></a>

### [`00532a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a90.md) → [`00532db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532db0.md) FUN_00532db0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a90.md#insn-00532aa8) · [`00532ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a90.md#insn-00532ab4)
- 新版 [`00532dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532db0.md#insn-00532dc8) · [`00532dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532db0.md#insn-00532dd4)

~~~diff
- 00532aa8 ["INT_ADD", "register:40f0:8", ["const:532aa8:8", "const:4:8"]]
- 00532aa8 ["CALL", null, ["callee:0053b2f0:8"]]
+ 00532dc8 ["INT_ADD", "register:40f0:8", ["const:532dc8:8", "const:4:8"]]
+ 00532dc8 ["CALL", null, ["callee:0053b2f0:8"]]
- 00532aa8 bytes 4a210094
+ 00532dc8 bytes 4a210094
- 00532ab4 ["INT_ADD", "register:40f0:8", ["const:532ab4:8", "const:4:8"]]
- 00532ab4 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00532dd4 ["INT_ADD", "register:40f0:8", ["const:532dd4:8", "const:4:8"]]
+ 00532dd4 ["CALL", null, ["callee:0046d7f0:8"]]
- 00532ab4 bytes 87eafc97
+ 00532dd4 bytes 87eafc97
~~~


<a id="compare-cd6934254c57224f7ed3a727213b94b1"></a>

### [`00532c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532c4c.md) → [`00532f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532f6c.md) FUN_00532f6c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00540c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532c4c.md#insn-00532cd4) · [`00532d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532c4c.md#insn-00532d0c) · [`00532d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532c4c.md#insn-00532d30)
- 新版 [`00532ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532f6c.md#insn-00532ff4) · [`0053302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532f6c.md#insn-0053302c) · [`00533050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532f6c.md#insn-00533050)

~~~diff
- 00532cd4 ["INT_ADD", "register:40f0:8", ["const:532cd4:8", "const:4:8"]]
- 00532cd4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00532ff4 ["INT_ADD", "register:40f0:8", ["const:532ff4:8", "const:4:8"]]
+ 00532ff4 ["CALL", null, ["callee:00c58f30:8"]]
- 00532cd4 bytes a3941c94
+ 00532ff4 bytes cf971c94
- 00532d0c ["INT_ADD", "register:40f0:8", ["const:532d0c:8", "const:4:8"]]
- 00532d0c ["CALL", null, ["callee:0043bf04:8"]]
+ 0053302c ["INT_ADD", "register:40f0:8", ["const:53302c:8", "const:4:8"]]
+ 0053302c ["CALL", null, ["callee:0043bf04:8"]]
- 00532d0c bytes b623fc97
+ 0053302c bytes b623fc97
- 00532d30 ["INT_ADD", "register:40f0:8", ["const:532d30:8", "const:4:8"]]
- 00532d30 ["CALL", null, ["callee:00540c1c:8"]]
+ 00533050 ["INT_ADD", "register:40f0:8", ["const:533050:8", "const:4:8"]]
+ 00533050 ["CALL", null, ["callee:00540c1c:8"]]
- 00532d30 bytes f3360094
+ 00533050 bytes f3360094
~~~


<a id="compare-07f62e0968eb482b2f72745eb861f94a"></a>

### [`00532d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d34.md) → [`00533054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533054.md) FUN_00533054

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d34.md#insn-00532d50)
- 新版 [`00533070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533054.md#insn-00533070)

~~~diff
- 00532d50 ["INT_ADD", "register:40f0:8", ["const:532d50:8", "const:4:8"]]
- 00532d50 ["CALL", null, ["callee:00c58f50:8"]]
+ 00533070 ["INT_ADD", "register:40f0:8", ["const:533070:8", "const:4:8"]]
+ 00533070 ["CALL", null, ["callee:00c58f50:8"]]
- 00532d50 bytes 8c941c94
+ 00533070 bytes b8971c94
~~~


<a id="compare-8868c6539b119c81aecfdf4e8f6c3d8b"></a>

### [`00532d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d78.md) → [`00533098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533098.md) FUN_00533098

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d78.md#insn-00532d94) · [`00532da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d78.md#insn-00532da4)
- 新版 [`005330b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533098.md#insn-005330b4) · [`005330c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533098.md#insn-005330c4)

~~~diff
- 00532d94 ["INT_ADD", "register:40f0:8", ["const:532d94:8", "const:4:8"]]
- 00532d94 ["CALL", null, ["callee:00c58f50:8"]]
+ 005330b4 ["INT_ADD", "register:40f0:8", ["const:5330b4:8", "const:4:8"]]
+ 005330b4 ["CALL", null, ["callee:00c58f50:8"]]
- 00532d94 bytes 7b941c94
+ 005330b4 bytes a7971c94
- 00532da4 ["INT_ADD", "register:40f0:8", ["const:532da4:8", "const:4:8"]]
- 00532da4 ["CALL", null, ["callee:00c58f50:8"]]
+ 005330c4 ["INT_ADD", "register:40f0:8", ["const:5330c4:8", "const:4:8"]]
+ 005330c4 ["CALL", null, ["callee:00c58f50:8"]]
- 00532da4 bytes 77941c94
+ 005330c4 bytes a3971c94
~~~


<a id="compare-d6845d2abf775c5415542aa3ddc26bfc"></a>

### [`00532f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532f8c.md) → [`005332ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332ac.md) FUN_005332ac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005331dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005331dc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532f8c.md#insn-00532f9c)
- 新版 [`005332bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332ac.md#insn-005332bc)

~~~diff
- 00532f9c ["INT_ADD", "register:40f0:8", ["const:532f9c:8", "const:4:8"]]
- 00532f9c ["CALL", null, ["callee:005331dc:8"]]
+ 005332bc ["INT_ADD", "register:40f0:8", ["const:5332bc:8", "const:4:8"]]
+ 005332bc ["CALL", null, ["callee:005331dc:8"]]
- 00532f9c bytes c8ffff97
+ 005332bc bytes c8ffff97
~~~


<a id="compare-11461d781a84c5baa8631d0b8b95737b"></a>

### [`00532fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532fb0.md) → [`005332d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332d0.md) FUN_005332d0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053ffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540300.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532fb0.md#insn-00532fc4) · [`00532fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532fb0.md#insn-00532fd0)
- 新版 [`005332e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332d0.md#insn-005332e4) · [`005332f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332d0.md#insn-005332f0)

~~~diff
- 00532fc4 ["INT_ADD", "register:40f0:8", ["const:532fc4:8", "const:4:8"]]
- 00532fc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005332e4 ["INT_ADD", "register:40f0:8", ["const:5332e4:8", "const:4:8"]]
+ 005332e4 ["CALL", null, ["callee:00c58f30:8"]]
- 00532fc4 bytes e7931c94
+ 005332e4 bytes 13971c94
- 00532fd0 ["INT_ADD", "register:40f0:8", ["const:532fd0:8", "const:4:8"]]
- 00532fd0 ["CALL", null, ["callee:00540300:8"]]
+ 005332f0 ["INT_ADD", "register:40f0:8", ["const:5332f0:8", "const:4:8"]]
+ 005332f0 ["CALL", null, ["callee:00540300:8"]]
- 00532fd0 bytes 04340094
+ 005332f0 bytes 04340094
~~~


<a id="compare-5154f61fe89ac8af4ce5141fac6391fb"></a>

### [`0053316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/0053316c.md) → [`0053348c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/0053348c.md) FUN_0053348c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00533318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533318.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053317c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/0053316c.md#insn-0053317c)
- 新版 [`0053349c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/0053348c.md#insn-0053349c)

~~~diff
- 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
- 0053317c ["CALL", null, ["callee:00533318:8"]]
+ 0053349c ["INT_ADD", "register:40f0:8", ["const:53349c:8", "const:4:8"]]
+ 0053349c ["CALL", null, ["callee:00533318:8"]]
- 0053317c bytes 9fffff97
+ 0053349c bytes 9fffff97
~~~


<a id="compare-0f88be9ff9a49653b8563f4b4e7b285f"></a>

### [`00533190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533190.md) → [`005334b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334b0.md) FUN_005334b0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005331ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533190.md#insn-005331ac) · [`005331bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533190.md#insn-005331bc)
- 新版 [`005334cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334b0.md#insn-005334cc) · [`005334dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334b0.md#insn-005334dc)

~~~diff
- 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
- 005331ac ["CALL", null, ["callee:00c58f50:8"]]
+ 005334cc ["INT_ADD", "register:40f0:8", ["const:5334cc:8", "const:4:8"]]
+ 005334cc ["CALL", null, ["callee:00c58f50:8"]]
- 005331ac bytes 75931c94
+ 005334cc bytes a1961c94
- 005331bc ["INT_ADD", "register:40f0:8", ["const:5331bc:8", "const:4:8"]]
- 005331bc ["CALL", null, ["callee:00c58f50:8"]]
+ 005334dc ["INT_ADD", "register:40f0:8", ["const:5334dc:8", "const:4:8"]]
+ 005334dc ["CALL", null, ["callee:00c58f50:8"]]
- 005331bc bytes 71931c94
+ 005334dc bytes 9d961c94
~~~


<a id="compare-644659e44157ac2e90730209d37273b3"></a>

### [`005331d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005331d0.md) → [`005334f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334f0.md) FUN_005334f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005331ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005331d0.md#insn-005331ec) · [`005331fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005331d0.md#insn-005331fc)
- 新版 [`0053350c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334f0.md#insn-0053350c) · [`0053351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005334f0.md#insn-0053351c)

~~~diff
- 005331ec ["INT_ADD", "register:40f0:8", ["const:5331ec:8", "const:4:8"]]
- 005331ec ["CALL", null, ["callee:00c58f50:8"]]
+ 0053350c ["INT_ADD", "register:40f0:8", ["const:53350c:8", "const:4:8"]]
+ 0053350c ["CALL", null, ["callee:00c58f50:8"]]
- 005331ec bytes 65931c94
+ 0053350c bytes 91961c94
- 005331fc ["INT_ADD", "register:40f0:8", ["const:5331fc:8", "const:4:8"]]
- 005331fc ["CALL", null, ["callee:00c58f50:8"]]
+ 0053351c ["INT_ADD", "register:40f0:8", ["const:53351c:8", "const:4:8"]]
+ 0053351c ["CALL", null, ["callee:00c58f50:8"]]
- 005331fc bytes 61931c94
+ 0053351c bytes 8d961c94
~~~


