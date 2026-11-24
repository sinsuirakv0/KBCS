# v16.0.1 → v16.0.2 · 要調査の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-ca5a405ef4f466eb0db1f3f1c9369370"></a>

### [`00520bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520bbc.md) → [`00520bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520bfc.md) FUN_00520bfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00520bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520bbc.md#insn-00520bd8) · [`00520bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520bbc.md#insn-00520bf8)
- 新版 `00520c18`（命令位置の公開資料なし） · `00520c38`（命令位置の公開資料なし）

~~~diff
- 00520bd8 ["INT_ADD", "register:40f0:8", ["const:520bd8:8", "const:4:8"]]
- 00520bd8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00520c18 ["INT_ADD", "register:40f0:8", ["const:520c18:8", "const:4:8"]]
+ 00520c18 ["CALL", null, ["callee:00c53da0:8"]]
- 00520bd8 bytes 4acc1c94
+ 00520c18 bytes 62cc1c94
- 00520bf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00520bf8 ["INT_ADD", "register:40f0:8", ["const:520bf8:8", "const:4:8"]]
- 00520bf8 ["CALLIND", null, ["register:0:8"]]
+ 00520c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00520c38 ["INT_ADD", "register:40f0:8", ["const:520c38:8", "const:4:8"]]
+ 00520c38 ["CALLIND", null, ["register:0:8"]]
- 00520bf8 bytes 00013fd6
+ 00520c38 bytes 00013fd6
~~~


<a id="compare-da1b51bff9ae4ee44dbf101f03869da9"></a>

### [`00522828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522828.md) → [`00522868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522868.md) FUN_00522868

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d4e4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522828.md#insn-00522844)
- 新版 `00522884`（命令位置の公開資料なし）

~~~diff
- 00522844 ["INT_ADD", "register:40f0:8", ["const:522844:8", "const:4:8"]]
- 00522844 ["CALL", null, ["callee:0054d4e4:8"]]
+ 00522884 ["INT_ADD", "register:40f0:8", ["const:522884:8", "const:4:8"]]
+ 00522884 ["CALL", null, ["callee:0054d4e4:8"]]
- 00522844 bytes 18ab0094
+ 00522884 bytes 18ab0094
~~~


<a id="compare-cb4a86c63c1ca68d3707e935b4f0f85a"></a>

### [`00522960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522960.md) → [`005229a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229a0.md) _ZNK5Botan16X509_Certificate12x509_versionEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522960.md#insn-00522968)
- 新版 `005229a8`（命令位置の公開資料なし）

~~~diff
- 00522968 ["INT_ADD", "register:40f0:8", ["const:522968:8", "const:4:8"]]
- 00522968 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005229a8 ["INT_ADD", "register:40f0:8", ["const:5229a8:8", "const:4:8"]]
+ 005229a8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522968 bytes 22dc1c94
+ 005229a8 bytes 46dc1c94
~~~


<a id="compare-e92bcc75dce3a824534074d68ed65d75"></a>

### [`00522978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522978.md) → [`005229b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229b8.md) _ZNK5Botan16X509_Certificate14is_self_signedEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522978.md#insn-00522980)
- 新版 `005229c0`（命令位置の公開資料なし）

~~~diff
- 00522980 ["INT_ADD", "register:40f0:8", ["const:522980:8", "const:4:8"]]
- 00522980 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005229c0 ["INT_ADD", "register:40f0:8", ["const:5229c0:8", "const:4:8"]]
+ 005229c0 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522980 bytes 1cdc1c94
+ 005229c0 bytes 40dc1c94
~~~


<a id="compare-5ea975b8f467cbc5a8cd09d5409bbe4a"></a>

### [`00522990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522990.md) → [`005229d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229d0.md) _ZNK5Botan16X509_Certificate10not_beforeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522990.md#insn-00522998)
- 新版 `005229d8`（命令位置の公開資料なし）

~~~diff
- 00522998 ["INT_ADD", "register:40f0:8", ["const:522998:8", "const:4:8"]]
- 00522998 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005229d8 ["INT_ADD", "register:40f0:8", ["const:5229d8:8", "const:4:8"]]
+ 005229d8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522998 bytes 16dc1c94
+ 005229d8 bytes 3adc1c94
~~~


<a id="compare-f70347ec91bcb7fc6d4725c0b3dc8bc9"></a>

### [`005229a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229a8.md) → [`005229e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005229e8.md) _ZNK5Botan16X509_Certificate9not_afterEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229a8.md#insn-005229b0)
- 新版 `005229f0`（命令位置の公開資料なし）

~~~diff
- 005229b0 ["INT_ADD", "register:40f0:8", ["const:5229b0:8", "const:4:8"]]
- 005229b0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005229f0 ["INT_ADD", "register:40f0:8", ["const:5229f0:8", "const:4:8"]]
+ 005229f0 ["CALL", null, ["callee:00c59ac0:8"]]
- 005229b0 bytes 10dc1c94
+ 005229f0 bytes 34dc1c94
~~~


<a id="compare-d362d5162aac17a5cf34613c8cbb6414"></a>

### [`005229c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229c0.md) → [`00522a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a00.md) _ZNK5Botan16X509_Certificate23subject_public_key_algoEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229c0.md#insn-005229c8)
- 新版 `00522a08`（命令位置の公開資料なし）

~~~diff
- 005229c8 ["INT_ADD", "register:40f0:8", ["const:5229c8:8", "const:4:8"]]
- 005229c8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a08 ["INT_ADD", "register:40f0:8", ["const:522a08:8", "const:4:8"]]
+ 00522a08 ["CALL", null, ["callee:00c59ac0:8"]]
- 005229c8 bytes 0adc1c94
+ 00522a08 bytes 2edc1c94
~~~


<a id="compare-e17f24c054cad03d26cf2557c7fc9419"></a>

### [`005229d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229d8.md) → [`00522a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a18.md) _ZNK5Botan16X509_Certificate16v2_issuer_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229d8.md#insn-005229e0)
- 新版 `00522a20`（命令位置の公開資料なし）

~~~diff
- 005229e0 ["INT_ADD", "register:40f0:8", ["const:5229e0:8", "const:4:8"]]
- 005229e0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a20 ["INT_ADD", "register:40f0:8", ["const:522a20:8", "const:4:8"]]
+ 00522a20 ["CALL", null, ["callee:00c59ac0:8"]]
- 005229e0 bytes 04dc1c94
+ 00522a20 bytes 28dc1c94
~~~


<a id="compare-7770d905a0b7154dc12df9c51cb89808"></a>

### [`005229f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229f0.md) → [`00522a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a30.md) _ZNK5Botan16X509_Certificate17v2_subject_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229f0.md#insn-005229f8)
- 新版 `00522a38`（命令位置の公開資料なし）

~~~diff
- 005229f8 ["INT_ADD", "register:40f0:8", ["const:5229f8:8", "const:4:8"]]
- 005229f8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a38 ["INT_ADD", "register:40f0:8", ["const:522a38:8", "const:4:8"]]
+ 00522a38 ["CALL", null, ["callee:00c59ac0:8"]]
- 005229f8 bytes fedb1c94
+ 00522a38 bytes 22dc1c94
~~~


<a id="compare-9be8493a461002c200251d072dc635ff"></a>

### [`00522a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a08.md) → [`00522a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a48.md) _ZNK5Botan16X509_Certificate23subject_public_key_bitsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a08.md#insn-00522a10)
- 新版 `00522a50`（命令位置の公開資料なし）

~~~diff
- 00522a10 ["INT_ADD", "register:40f0:8", ["const:522a10:8", "const:4:8"]]
- 00522a10 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a50 ["INT_ADD", "register:40f0:8", ["const:522a50:8", "const:4:8"]]
+ 00522a50 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a10 bytes f8db1c94
+ 00522a50 bytes 1cdc1c94
~~~


<a id="compare-0d3e1a2eb795f4c0c8a722b786400cb0"></a>

### [`00522a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a20.md) → [`00522a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a60.md) _ZNK5Botan16X509_Certificate18is_serial_negativeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a20.md#insn-00522a28)
- 新版 `00522a68`（命令位置の公開資料なし）

~~~diff
- 00522a28 ["INT_ADD", "register:40f0:8", ["const:522a28:8", "const:4:8"]]
- 00522a28 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a68 ["INT_ADD", "register:40f0:8", ["const:522a68:8", "const:4:8"]]
+ 00522a68 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a28 bytes f2db1c94
+ 00522a68 bytes 16dc1c94
~~~


<a id="compare-cb0dd9adbc22225c1fb7844cf458068c"></a>

### [`00522a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a38.md) → [`00522a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a78.md) _ZNK5Botan16X509_Certificate10path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a38.md#insn-00522a40)
- 新版 `00522a80`（命令位置の公開資料なし）

~~~diff
- 00522a40 ["INT_ADD", "register:40f0:8", ["const:522a40:8", "const:4:8"]]
- 00522a40 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a80 ["INT_ADD", "register:40f0:8", ["const:522a80:8", "const:4:8"]]
+ 00522a80 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a40 bytes ecdb1c94
+ 00522a80 bytes 10dc1c94
~~~


<a id="compare-fff5c39ab4efbb5b21a99fae3b783ff4"></a>

### [`00522a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a50.md) → [`00522a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522a90.md) _ZNK5Botan16X509_Certificate11constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a50.md#insn-00522a58)
- 新版 `00522a98`（命令位置の公開資料なし）

~~~diff
- 00522a58 ["INT_ADD", "register:40f0:8", ["const:522a58:8", "const:4:8"]]
- 00522a58 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522a98 ["INT_ADD", "register:40f0:8", ["const:522a98:8", "const:4:8"]]
+ 00522a98 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a58 bytes e6db1c94
+ 00522a98 bytes 0adc1c94
~~~


<a id="compare-08d976c85afffb6907ce424dc7c6ff5d"></a>

### [`00522a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a68.md) → [`00522aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522aa8.md) _ZNK5Botan16X509_Certificate18extended_key_usageEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a68.md#insn-00522a70)
- 新版 `00522ab0`（命令位置の公開資料なし）

~~~diff
- 00522a70 ["INT_ADD", "register:40f0:8", ["const:522a70:8", "const:4:8"]]
- 00522a70 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522ab0 ["INT_ADD", "register:40f0:8", ["const:522ab0:8", "const:4:8"]]
+ 00522ab0 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a70 bytes e0db1c94
+ 00522ab0 bytes 04dc1c94
~~~


<a id="compare-5bcd6de910d823a89ccfee21e74aa887"></a>

### [`00522a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a80.md) → [`00522ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ac0.md) _ZNK5Botan16X509_Certificate23certificate_policy_oidsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a80.md#insn-00522a88)
- 新版 `00522ac8`（命令位置の公開資料なし）

~~~diff
- 00522a88 ["INT_ADD", "register:40f0:8", ["const:522a88:8", "const:4:8"]]
- 00522a88 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522ac8 ["INT_ADD", "register:40f0:8", ["const:522ac8:8", "const:4:8"]]
+ 00522ac8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522a88 bytes dadb1c94
+ 00522ac8 bytes fedb1c94
~~~


<a id="compare-1a82c12e99154423d2557cdaee79fddf"></a>

### [`00522a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a98.md) → [`00522ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ad8.md) _ZNK5Botan16X509_Certificate16name_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a98.md#insn-00522aa0)
- 新版 `00522ae0`（命令位置の公開資料なし）

~~~diff
- 00522aa0 ["INT_ADD", "register:40f0:8", ["const:522aa0:8", "const:4:8"]]
- 00522aa0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522ae0 ["INT_ADD", "register:40f0:8", ["const:522ae0:8", "const:4:8"]]
+ 00522ae0 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522aa0 bytes d4db1c94
+ 00522ae0 bytes f8db1c94
~~~


<a id="compare-c1706c27e3a36c585f66f096202412b1"></a>

### [`00522ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ab0.md) → [`00522af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522af0.md) _ZNK5Botan16X509_Certificate13v3_extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ab0.md#insn-00522ab8)
- 新版 `00522af8`（命令位置の公開資料なし）

~~~diff
- 00522ab8 ["INT_ADD", "register:40f0:8", ["const:522ab8:8", "const:4:8"]]
- 00522ab8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522af8 ["INT_ADD", "register:40f0:8", ["const:522af8:8", "const:4:8"]]
+ 00522af8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522ab8 bytes cedb1c94
+ 00522af8 bytes f2db1c94
~~~


<a id="compare-2aed7fa8e42f3d06ca15ade664afc42b"></a>

### [`00522ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ac8.md) → [`00522b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522b08.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ac8.md#insn-00522ad8)
- 新版 `00522b18`（命令位置の公開資料なし）

~~~diff
- 00522ad8 ["INT_ADD", "register:40f0:8", ["const:522ad8:8", "const:4:8"]]
- 00522ad8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522b18 ["INT_ADD", "register:40f0:8", ["const:522b18:8", "const:4:8"]]
+ 00522b18 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522ad8 bytes c6db1c94
+ 00522b18 bytes eadb1c94
~~~


<a id="compare-ee5e50d8631edd6991458d675243ab62"></a>

### [`00522dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md) → [`00522dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522dec.md) _ZNK5Botan16X509_Certificate15has_constraintsENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md#insn-00522dc0) · [`00522dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md#insn-00522dd0)
- 新版 `00522e00`（命令位置の公開資料なし） · `00522e10`（命令位置の公開資料なし）

~~~diff
- 00522dc0 ["INT_ADD", "register:40f0:8", ["const:522dc0:8", "const:4:8"]]
- 00522dc0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522e00 ["INT_ADD", "register:40f0:8", ["const:522e00:8", "const:4:8"]]
+ 00522e00 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522dc0 bytes 0cdb1c94
+ 00522e00 bytes 30db1c94
- 00522dd0 ["INT_ADD", "register:40f0:8", ["const:522dd0:8", "const:4:8"]]
- 00522dd0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522e10 ["INT_ADD", "register:40f0:8", ["const:522e10:8", "const:4:8"]]
+ 00522e10 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522dd0 bytes 08db1c94
+ 00522e10 bytes 2cdb1c94
~~~


<a id="compare-58816b8c73ff5642032b74fdb5ff1f27"></a>

### [`00522df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md) → [`00522e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522e34.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522e20) · [`00522e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522e28) · [`00522ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522ea4)
- 新版 `00522e60`（命令位置の公開資料なし） · `00522e68`（命令位置の公開資料なし） · `00522ee4`（命令位置の公開資料なし）

~~~diff
- 00522e20 ["INT_ADD", "register:40f0:8", ["const:522e20:8", "const:4:8"]]
- 00522e20 ["CALL", null, ["callee:00c58750:8"]]
+ 00522e60 ["INT_ADD", "register:40f0:8", ["const:522e60:8", "const:4:8"]]
+ 00522e60 ["CALL", null, ["callee:00c58750:8"]]
- 00522e20 bytes 18d61c94
+ 00522e60 bytes 3cd61c94
- 00522e28 ["INT_ADD", "register:40f0:8", ["const:522e28:8", "const:4:8"]]
- 00522e28 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522e68 ["INT_ADD", "register:40f0:8", ["const:522e68:8", "const:4:8"]]
+ 00522e68 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522e28 bytes f2da1c94
+ 00522e68 bytes 16db1c94
- 00522ea4 ["INT_ADD", "register:40f0:8", ["const:522ea4:8", "const:4:8"]]
- 00522ea4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00522ee4 ["INT_ADD", "register:40f0:8", ["const:522ee4:8", "const:4:8"]]
+ 00522ee4 ["CALL", null, ["callee:00c57f80:8"]]
- 00522ea4 bytes 03d41c94
+ 00522ee4 bytes 27d41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5006bcf628cee8606023a200014e79"></a>

### [`00522f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522f14.md) → [`00522f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522f54.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522f14.md#insn-00522f24)
- 新版 `00522f64`（命令位置の公開資料なし）

~~~diff
- 00522f24 ["INT_ADD", "register:40f0:8", ["const:522f24:8", "const:4:8"]]
- 00522f24 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522f64 ["INT_ADD", "register:40f0:8", ["const:522f64:8", "const:4:8"]]
+ 00522f64 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522f24 bytes b3da1c94
+ 00522f64 bytes d7da1c94
~~~


<a id="compare-66f87eafa872c8fcb0f7331447cb705e"></a>

### [`00522fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522fa4.md) → [`00522fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522fe4.md) _ZNK5Botan16X509_Certificate14ocsp_responderEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522fa4.md#insn-00522fb4)
- 新版 `00522ff4`（命令位置の公開資料なし）

~~~diff
- 00522fb4 ["INT_ADD", "register:40f0:8", ["const:522fb4:8", "const:4:8"]]
- 00522fb4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522ff4 ["INT_ADD", "register:40f0:8", ["const:522ff4:8", "const:4:8"]]
+ 00522ff4 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522fb4 bytes 8fda1c94
+ 00522ff4 bytes b3da1c94
~~~


<a id="compare-896c7fa80652d8ece980192cc870666f"></a>

### [`00522ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ff8.md) → [`00523038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523038.md) _ZNK5Botan16X509_Certificate10ca_issuersEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ff8.md#insn-00523008)
- 新版 `00523048`（命令位置の公開資料なし）

~~~diff
- 00523008 ["INT_ADD", "register:40f0:8", ["const:523008:8", "const:4:8"]]
- 00523008 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00523048 ["INT_ADD", "register:40f0:8", ["const:523048:8", "const:4:8"]]
+ 00523048 ["CALL", null, ["callee:00c59ac0:8"]]
- 00523008 bytes 7ada1c94
+ 00523048 bytes 9eda1c94
~~~


<a id="compare-14096a5d2b9f0308fa149089761cdb0e"></a>

### [`00523040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md) → [`00523080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523080.md) _ZNK5Botan16X509_Certificate22crl_distribution_pointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md#insn-00523054) · [`0052306c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md#insn-0052306c)
- 新版 `00523094`（命令位置の公開資料なし） · `005230ac`（命令位置の公開資料なし）

~~~diff
- 00523054 ["INT_ADD", "register:40f0:8", ["const:523054:8", "const:4:8"]]
- 00523054 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00523094 ["INT_ADD", "register:40f0:8", ["const:523094:8", "const:4:8"]]
+ 00523094 ["CALL", null, ["callee:00c59ac0:8"]]
- 00523054 bytes 67da1c94
+ 00523094 bytes 8bda1c94
- 0052306c ["INT_ADD", "register:40f0:8", ["const:52306c:8", "const:4:8"]]
- 0052306c ["CALL", null, ["callee:00c59ac0:8"]]
+ 005230ac ["INT_ADD", "register:40f0:8", ["const:5230ac:8", "const:4:8"]]
+ 005230ac ["CALL", null, ["callee:00c59ac0:8"]]
- 0052306c bytes 61da1c94
+ 005230ac bytes 85da1c94
~~~


<a id="compare-8e095135ddde80f50a9a696779c572f4"></a>

### [`005230b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230b4.md) → [`005230f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/005230f4.md) _ZNK5Botan16X509_Certificate15issuer_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005230bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230b4.md#insn-005230bc)
- 新版 `005230fc`（命令位置の公開資料なし）

~~~diff
- 005230bc ["INT_ADD", "register:40f0:8", ["const:5230bc:8", "const:4:8"]]
- 005230bc ["CALL", null, ["callee:00c59ac0:8"]]
+ 005230fc ["INT_ADD", "register:40f0:8", ["const:5230fc:8", "const:4:8"]]
+ 005230fc ["CALL", null, ["callee:00c59ac0:8"]]
- 005230bc bytes 4dda1c94
+ 005230fc bytes 71da1c94
~~~


<a id="compare-42fffdb125346c0174149a5eca7df2b3"></a>

### [`00523de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md) → [`00523e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523e28.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c10.md) · 呼出先 5件 [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c596f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596f0.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ce0.md) · 呼出先 5件 [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c597c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597c0.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e0c) · [`00523e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e18) · [`00523e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e20)
- 新版 `00523e4c`（命令位置の公開資料なし） · `00523e58`（命令位置の公開資料なし） · `00523e60`（命令位置の公開資料なし）

~~~diff
- 00523e0c ["INT_ADD", "register:40f0:8", ["const:523e0c:8", "const:4:8"]]
- 00523e0c ["CALL", null, ["callee:00c59ac0:8"]]
+ 00523e4c ["INT_ADD", "register:40f0:8", ["const:523e4c:8", "const:4:8"]]
+ 00523e4c ["CALL", null, ["callee:00c59ac0:8"]]
- 00523e0c bytes f9d61c94
+ 00523e4c bytes 1dd71c94
- 00523e18 ["INT_ADD", "register:40f0:8", ["const:523e18:8", "const:4:8"]]
- 00523e18 ["CALL", null, ["callee:004a6c5c:8"]]
+ 00523e58 ["INT_ADD", "register:40f0:8", ["const:523e58:8", "const:4:8"]]
+ 00523e58 ["CALL", null, ["callee:004a6c5c:8"]]
- 00523e18 bytes 810bfe97
+ 00523e58 bytes 810bfe97
- 00523e20 ["INT_ADD", "register:40f0:8", ["const:523e20:8", "const:4:8"]]
- 00523e20 ["CALL", null, ["callee:00c597c0:8"]]
+ 00523e60 ["INT_ADD", "register:40f0:8", ["const:523e60:8", "const:4:8"]]
+ 00523e60 ["CALL", null, ["callee:00c597c0:8"]]
- 00523e20 bytes 34d61c94
+ 00523e60 bytes 58d61c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b16b98d271910fbf5858efc5a822fa1"></a>

### [`00523f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md) → [`00523f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/00523f9c.md) _ZNK5Botan16X509_Certificate20raw_issuer_dn_sha256Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fbc) · [`00523fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fcc) · [`00523fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fdc)
- 新版 `00523ffc`（命令位置の公開資料なし） · `0052400c`（命令位置の公開資料なし） · `0052401c`（命令位置の公開資料なし）

~~~diff
- 00523fbc ["INT_ADD", "register:40f0:8", ["const:523fbc:8", "const:4:8"]]
- 00523fbc ["CALL", null, ["callee:00c58f40:8"]]
+ 00523ffc ["INT_ADD", "register:40f0:8", ["const:523ffc:8", "const:4:8"]]
+ 00523ffc ["CALL", null, ["callee:00c58f40:8"]]
- 00523fbc bytes add31c94
+ 00523ffc bytes d1d31c94
- 00523fcc ["INT_ADD", "register:40f0:8", ["const:523fcc:8", "const:4:8"]]
- 00523fcc ["CALL", null, ["callee:00c57f80:8"]]
+ 0052400c ["INT_ADD", "register:40f0:8", ["const:52400c:8", "const:4:8"]]
+ 0052400c ["CALL", null, ["callee:00c57f80:8"]]
- 00523fcc bytes b9cf1c94
+ 0052400c bytes ddcf1c94
- 00523fdc ["INT_ADD", "register:40f0:8", ["const:523fdc:8", "const:4:8"]]
- 00523fdc ["CALL", null, ["callee:00c57f80:8"]]
+ 0052401c ["INT_ADD", "register:40f0:8", ["const:52401c:8", "const:4:8"]]
+ 0052401c ["CALL", null, ["callee:00c57f80:8"]]
- 00523fdc bytes b5cf1c94
+ 0052401c bytes d9cf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce12244e8bc37b8c0da91512047f65c"></a>

### [`0052414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md) → [`0052418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052418c.md) _ZNK5Botan16X509_Certificate21raw_subject_dn_sha256Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005241ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241ac) · [`005241b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241b8) · [`005241d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241d0)
- 新版 `005241ec`（命令位置の公開資料なし） · `005241f8`（命令位置の公開資料なし） · `00524210`（命令位置の公開資料なし）

~~~diff
- 005241ac ["INT_ADD", "register:40f0:8", ["const:5241ac:8", "const:4:8"]]
- 005241ac ["CALL", null, ["callee:00c58ec0:8"]]
+ 005241ec ["INT_ADD", "register:40f0:8", ["const:5241ec:8", "const:4:8"]]
+ 005241ec ["CALL", null, ["callee:00c58ec0:8"]]
- 005241ac bytes 11d31c94
+ 005241ec bytes 35d31c94
- 005241b8 ["INT_ADD", "register:40f0:8", ["const:5241b8:8", "const:4:8"]]
- 005241b8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005241f8 ["INT_ADD", "register:40f0:8", ["const:5241f8:8", "const:4:8"]]
+ 005241f8 ["CALL", null, ["callee:00c59ac0:8"]]
- 005241b8 bytes 0ed61c94
+ 005241f8 bytes 32d61c94
- 005241d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005241d0 ["INT_ADD", "register:40f0:8", ["const:5241d0:8", "const:4:8"]]
- 005241d0 ["CALLIND", null, ["register:0:8"]]
+ 00524210 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00524210 ["INT_ADD", "register:40f0:8", ["const:524210:8", "const:4:8"]]
+ 00524210 ["CALLIND", null, ["register:0:8"]]
- 005241d0 bytes 00013fd6
+ 00524210 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa36640785e7072e15d19f579217317c"></a>

### [`005242e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md) → [`00524324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524324.md) _ZNK5Botan16X509_Certificate14ex_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005242f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md#insn-005242f4)
- 新版 `00524334`（命令位置の公開資料なし）

~~~diff
- 005242f4 ["INT_ADD", "register:40f0:8", ["const:5242f4:8", "const:4:8"]]
- 005242f4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00524334 ["INT_ADD", "register:40f0:8", ["const:524334:8", "const:4:8"]]
+ 00524334 ["CALL", null, ["callee:00c59ac0:8"]]
- 005242f4 bytes bfd51c94
+ 00524334 bytes e3d51c94
~~~


<a id="compare-a736a111f76da862968f7d4695f1a886"></a>

### [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) → [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) FUN_0052434c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005242e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md) [`0052453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00524324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524324.md) [`0052457c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052457c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524398) · [`00524400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524400) · [`00524444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524444)
- 新版 `005243d8`（命令位置の公開資料なし） · `00524440`（命令位置の公開資料なし） · `00524484`（命令位置の公開資料なし）

~~~diff
- 00524398 ["INT_ADD", "register:40f0:8", ["const:524398:8", "const:4:8"]]
- 00524398 ["CALL", null, ["callee:00c58980:8"]]
+ 005243d8 ["INT_ADD", "register:40f0:8", ["const:5243d8:8", "const:4:8"]]
+ 005243d8 ["CALL", null, ["callee:00c58980:8"]]
- 00524398 bytes 46d11c94
+ 005243d8 bytes 6ad11c94
- 00524400 ["INT_ADD", "register:40f0:8", ["const:524400:8", "const:4:8"]]
- 00524400 ["CALL", null, ["callee:00c57f60:8"]]
+ 00524440 ["INT_ADD", "register:40f0:8", ["const:524440:8", "const:4:8"]]
+ 00524440 ["CALL", null, ["callee:00c57f60:8"]]
- 00524400 bytes a4ce1c94
+ 00524440 bytes c8ce1c94
- 00524444 ["INT_ADD", "register:40f0:8", ["const:524444:8", "const:4:8"]]
- 00524444 ["CALL", null, ["callee:00c580d0:8"]]
+ 00524484 ["INT_ADD", "register:40f0:8", ["const:524484:8", "const:4:8"]]
+ 00524484 ["CALL", null, ["callee:00c580d0:8"]]
- 00524444 bytes efce1c94
+ 00524484 bytes 13cf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76fd009e059a9ce1be52f5ebd2213900"></a>

### [`0052453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md) → [`0052457c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052457c.md) _ZNK5Botan16X509_Certificate8policiesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052434c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/0052434c.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052454c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md#insn-0052454c)
- 新版 `0052458c`（命令位置の公開資料なし）

~~~diff
- 0052454c ["INT_ADD", "register:40f0:8", ["const:52454c:8", "const:4:8"]]
- 0052454c ["CALL", null, ["callee:00c59ac0:8"]]
+ 0052458c ["INT_ADD", "register:40f0:8", ["const:52458c:8", "const:4:8"]]
+ 0052458c ["CALL", null, ["callee:00c59ac0:8"]]
- 0052454c bytes 29d51c94
+ 0052458c bytes 4dd51c94
~~~


<a id="compare-ea0b6075c14e28af63ed56ec0393339d"></a>

### [`00524564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md) → [`005245a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005245a4.md) _ZNK5Botan16X509_Certificate11fingerprintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c595c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595c0.md) [`00c59e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59690.md) [`00c59f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-00524590) · [`005245a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-005245a4) · [`005245b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-005245b4)
- 新版 `005245d0`（命令位置の公開資料なし） · `005245e4`（命令位置の公開資料なし） · `005245f4`（命令位置の公開資料なし）

~~~diff
- 00524590 ["INT_ADD", "register:40f0:8", ["const:524590:8", "const:4:8"]]
- 00524590 ["CALL", null, ["callee:00c59f50:8"]]
+ 005245d0 ["INT_ADD", "register:40f0:8", ["const:5245d0:8", "const:4:8"]]
+ 005245d0 ["CALL", null, ["callee:00c59f50:8"]]
- 00524590 bytes 3cd61c94
+ 005245d0 bytes 60d61c94
- 005245a4 ["INT_ADD", "register:40f0:8", ["const:5245a4:8", "const:4:8"]]
- 005245a4 ["CALL", null, ["callee:00c59690:8"]]
+ 005245e4 ["INT_ADD", "register:40f0:8", ["const:5245e4:8", "const:4:8"]]
+ 005245e4 ["CALL", null, ["callee:00c59690:8"]]
- 005245a4 bytes 07d41c94
+ 005245e4 bytes 2bd41c94
- 005245b4 ["INT_ADD", "register:40f0:8", ["const:5245b4:8", "const:4:8"]]
- 005245b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005245f4 ["INT_ADD", "register:40f0:8", ["const:5245f4:8", "const:4:8"]]
+ 005245f4 ["CALL", null, ["callee:00c57f80:8"]]
- 005245b4 bytes 3fce1c94
+ 005245f4 bytes 63ce1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4156c4ebe767c8eedae256ac245530e"></a>

### [`00524610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md) → [`00524650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524650.md) _ZNK5Botan16X509_Certificate16matches_dns_nameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ec0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59920.md) [`00c59eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59eb0.md)
- 新版 呼出元 1件 [`00c59f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f90.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c599f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599f0.md) [`00c59f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-00524670) · [`00524680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-00524680) · [`005246b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-005246b4)
- 新版 `005246b0`（命令位置の公開資料なし） · `005246c0`（命令位置の公開資料なし） · `005246f4`（命令位置の公開資料なし）

~~~diff
- 00524670 ["INT_ADD", "register:40f0:8", ["const:524670:8", "const:4:8"]]
- 00524670 ["CALL", null, ["callee:00c59f80:8"]]
+ 005246b0 ["INT_ADD", "register:40f0:8", ["const:5246b0:8", "const:4:8"]]
+ 005246b0 ["CALL", null, ["callee:00c59f80:8"]]
- 00524670 bytes 10d61c94
+ 005246b0 bytes 34d61c94
- 00524680 ["INT_ADD", "register:40f0:8", ["const:524680:8", "const:4:8"]]
- 00524680 ["CALL", null, ["callee:00c57f80:8"]]
+ 005246c0 ["INT_ADD", "register:40f0:8", ["const:5246c0:8", "const:4:8"]]
+ 005246c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00524680 bytes 0cce1c94
+ 005246c0 bytes 30ce1c94
- 005246b4 ["INT_ADD", "register:40f0:8", ["const:5246b4:8", "const:4:8"]]
- 005246b4 ["CALL", null, ["callee:00c59f80:8"]]
+ 005246f4 ["INT_ADD", "register:40f0:8", ["const:5246f4:8", "const:4:8"]]
+ 005246f4 ["CALL", null, ["callee:00c59f80:8"]]
- 005246b4 bytes ffd51c94
+ 005246f4 bytes 23d61c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc41fbc66d2bf126c4e783fc9c375e4a"></a>

### [`00524870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524870.md) → [`005248b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005248b0.md) _ZNK5Botan16X509_CertificateltERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005248ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524870.md#insn-005248ac)
- 新版 `005248ec`（命令位置の公開資料なし）

~~~diff
- 005248ac ["INT_ADD", "register:40f0:8", ["const:5248ac:8", "const:4:8"]]
- 005248ac ["CALL", null, ["callee:00c58120:8"]]
+ 005248ec ["INT_ADD", "register:40f0:8", ["const:5248ec:8", "const:4:8"]]
+ 005248ec ["CALL", null, ["callee:00c58120:8"]]
- 005248ac bytes e9cd1c94
+ 005248ec bytes 0dce1c94
~~~


<a id="compare-e4d7e73e5ff62b4b27eccc711c963f9b"></a>

### [`00524964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md) → [`005249a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/005249a4.md) _ZN5BotanneERKNS_16X509_CertificateES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-00524990) · [`005249a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-005249a0) · [`005249c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-005249c0)
- 新版 `005249d0`（命令位置の公開資料なし） · `005249e0`（命令位置の公開資料なし） · `00524a00`（命令位置の公開資料なし）

~~~diff
- 00524990 ["INT_ADD", "register:40f0:8", ["const:524990:8", "const:4:8"]]
- 00524990 ["CALL", null, ["callee:00c58120:8"]]
+ 005249d0 ["INT_ADD", "register:40f0:8", ["const:5249d0:8", "const:4:8"]]
+ 005249d0 ["CALL", null, ["callee:00c58120:8"]]
- 00524990 bytes b0cd1c94
+ 005249d0 bytes d4cd1c94
- 005249a0 ["INT_ADD", "register:40f0:8", ["const:5249a0:8", "const:4:8"]]
- 005249a0 ["CALL", null, ["callee:00c58770:8"]]
+ 005249e0 ["INT_ADD", "register:40f0:8", ["const:5249e0:8", "const:4:8"]]
+ 005249e0 ["CALL", null, ["callee:00c58770:8"]]
- 005249a0 bytes 40cf1c94
+ 005249e0 bytes 64cf1c94
- 005249c0 ["INT_ADD", "register:40f0:8", ["const:5249c0:8", "const:4:8"]]
- 005249c0 ["CALL", null, ["callee:00c58120:8"]]
+ 00524a00 ["INT_ADD", "register:40f0:8", ["const:524a00:8", "const:4:8"]]
+ 00524a00 ["CALL", null, ["callee:00c58120:8"]]
- 005249c0 bytes a4cd1c94
+ 00524a00 bytes c8cd1c94
~~~


<a id="compare-39889eb0cc04015ff24942ec13c6d53c"></a>

### [`00526210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md) → [`00526250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526250.md) _ZN5Botan17X509_Cert_Options10not_beforeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ed0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00526238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md#insn-00526238) · [`00526270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md#insn-00526270)
- 新版 `00526278`（命令位置の公開資料なし） · `005262b0`（命令位置の公開資料なし）

~~~diff
- 00526238 ["INT_ADD", "register:40f0:8", ["const:526238:8", "const:4:8"]]
- 00526238 ["CALL", null, ["callee:00c59fa0:8"]]
+ 00526278 ["INT_ADD", "register:40f0:8", ["const:526278:8", "const:4:8"]]
+ 00526278 ["CALL", null, ["callee:00c59fa0:8"]]
- 00526238 bytes 26cf1c94
+ 00526278 bytes 4acf1c94
- 00526270 ["INT_ADD", "register:40f0:8", ["const:526270:8", "const:4:8"]]
- 00526270 ["CALL", null, ["callee:00c57fb0:8"]]
+ 005262b0 ["INT_ADD", "register:40f0:8", ["const:5262b0:8", "const:4:8"]]
+ 005262b0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00526270 bytes 1cc71c94
+ 005262b0 bytes 40c71c94
~~~


<a id="compare-673feb6375a7beeb94cbf4003949d809"></a>

### [`00526274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md) → [`005262b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005262b4.md) _ZN5Botan17X509_Cert_Options9not_afterERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ed0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052629c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md#insn-0052629c) · [`005262d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md#insn-005262d4)
- 新版 `005262dc`（命令位置の公開資料なし） · `00526314`（命令位置の公開資料なし）

~~~diff
- 0052629c ["INT_ADD", "register:40f0:8", ["const:52629c:8", "const:4:8"]]
- 0052629c ["CALL", null, ["callee:00c59fa0:8"]]
+ 005262dc ["INT_ADD", "register:40f0:8", ["const:5262dc:8", "const:4:8"]]
+ 005262dc ["CALL", null, ["callee:00c59fa0:8"]]
- 0052629c bytes 0dcf1c94
+ 005262dc bytes 31cf1c94
- 005262d4 ["INT_ADD", "register:40f0:8", ["const:5262d4:8", "const:4:8"]]
- 005262d4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00526314 ["INT_ADD", "register:40f0:8", ["const:526314:8", "const:4:8"]]
+ 00526314 ["CALL", null, ["callee:00c57fb0:8"]]
- 005262d4 bytes 03c71c94
+ 00526314 bytes 27c71c94
~~~


<a id="compare-65eb9b2fe494bf1753ec67b3e922f31e"></a>

### [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) → [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) FUN_00527dfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) · 呼出先 2件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md) [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) · 呼出先 2件 [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00527df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md#insn-00527df4)
- 新版 `00527e34`（命令位置の公開資料なし）

~~~diff
- 00527df4 ["INT_ADD", "register:40f0:8", ["const:527df4:8", "const:4:8"]]
- 00527df4 ["CALL", null, ["callee:0053f850:8"]]
+ 00527e34 ["INT_ADD", "register:40f0:8", ["const:527e34:8", "const:4:8"]]
+ 00527e34 ["CALL", null, ["callee:0053f850:8"]]
- 00527df4 bytes 875e0094
+ 00527e34 bytes 875e0094
~~~


<a id="compare-374ea1eda414a33ad4ad257a22f11cc0"></a>

### [`00529cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md) → [`00529cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529cf8.md) FUN_00529cf8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00529d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d04) · [`00529d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d18) · [`00529d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d20)
- 新版 `00529d44`（命令位置の公開資料なし） · `00529d58`（命令位置の公開資料なし） · `00529d60`（命令位置の公開資料なし）

~~~diff
- 00529d04 ["INT_ADD", "register:40f0:8", ["const:529d04:8", "const:4:8"]]
- 00529d04 ["CALL", null, ["callee:00c53da0:8"]]
+ 00529d44 ["INT_ADD", "register:40f0:8", ["const:529d44:8", "const:4:8"]]
+ 00529d44 ["CALL", null, ["callee:00c53da0:8"]]
- 00529d04 bytes ffa71c94
+ 00529d44 bytes 17a81c94
- 00529d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00529d18 ["INT_ADD", "register:40f0:8", ["const:529d18:8", "const:4:8"]]
- 00529d18 ["CALLIND", null, ["register:0:8"]]
+ 00529d58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00529d58 ["INT_ADD", "register:40f0:8", ["const:529d58:8", "const:4:8"]]
+ 00529d58 ["CALLIND", null, ["register:0:8"]]
- 00529d18 bytes 00013fd6
+ 00529d58 bytes 00013fd6
- 00529d20 ["INT_ADD", "register:40f0:8", ["const:529d20:8", "const:4:8"]]
- 00529d20 ["CALL", null, ["callee:00c57f50:8"]]
+ 00529d60 ["INT_ADD", "register:40f0:8", ["const:529d60:8", "const:4:8"]]
+ 00529d60 ["CALL", null, ["callee:00c57f50:8"]]
- 00529d20 bytes 58b81c94
+ 00529d60 bytes 7cb81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef084a3f12335c0962c9dc3c57404ce0"></a>

### [`0052b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md) → [`0052b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b080.md) FUN_0052b080

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md#insn-0052b05c) · [`0052b07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md#insn-0052b07c)
- 新版 `0052b09c`（命令位置の公開資料なし） · `0052b0bc`（命令位置の公開資料なし）

~~~diff
- 0052b05c ["INT_ADD", "register:40f0:8", ["const:52b05c:8", "const:4:8"]]
- 0052b05c ["CALL", null, ["callee:00c53da0:8"]]
+ 0052b09c ["INT_ADD", "register:40f0:8", ["const:52b09c:8", "const:4:8"]]
+ 0052b09c ["CALL", null, ["callee:00c53da0:8"]]
- 0052b05c bytes 29a31c94
+ 0052b09c bytes 41a31c94
- 0052b07c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b07c ["INT_ADD", "register:40f0:8", ["const:52b07c:8", "const:4:8"]]
- 0052b07c ["CALLIND", null, ["register:0:8"]]
+ 0052b0bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b0bc ["INT_ADD", "register:40f0:8", ["const:52b0bc:8", "const:4:8"]]
+ 0052b0bc ["CALLIND", null, ["register:0:8"]]
- 0052b07c bytes 00013fd6
+ 0052b0bc bytes 00013fd6
~~~


<a id="compare-67696ad9997fdbc7ef8eac386dfe5986"></a>

### [`0052b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md) → [`0052b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b0d0.md) FUN_0052b0d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0dc) · [`0052b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0f0) · [`0052b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0f8)
- 新版 `0052b11c`（命令位置の公開資料なし） · `0052b130`（命令位置の公開資料なし） · `0052b138`（命令位置の公開資料なし）

~~~diff
- 0052b0dc ["INT_ADD", "register:40f0:8", ["const:52b0dc:8", "const:4:8"]]
- 0052b0dc ["CALL", null, ["callee:00c53da0:8"]]
+ 0052b11c ["INT_ADD", "register:40f0:8", ["const:52b11c:8", "const:4:8"]]
+ 0052b11c ["CALL", null, ["callee:00c53da0:8"]]
- 0052b0dc bytes 09a31c94
+ 0052b11c bytes 21a31c94
- 0052b0f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b0f0 ["INT_ADD", "register:40f0:8", ["const:52b0f0:8", "const:4:8"]]
- 0052b0f0 ["CALLIND", null, ["register:0:8"]]
+ 0052b130 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b130 ["INT_ADD", "register:40f0:8", ["const:52b130:8", "const:4:8"]]
+ 0052b130 ["CALLIND", null, ["register:0:8"]]
- 0052b0f0 bytes 00013fd6
+ 0052b130 bytes 00013fd6
- 0052b0f8 ["INT_ADD", "register:40f0:8", ["const:52b0f8:8", "const:4:8"]]
- 0052b0f8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0052b138 ["INT_ADD", "register:40f0:8", ["const:52b138:8", "const:4:8"]]
+ 0052b138 ["CALL", null, ["callee:00c57f50:8"]]
- 0052b0f8 bytes 62b31c94
+ 0052b138 bytes 86b31c94
~~~


<a id="compare-6e5a48e9b312e4dc0158a613a8b93b6c"></a>

### [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) → [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) FUN_0052c284

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) [`0052c4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md) [`0054ed04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md) · 呼出先 4件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) [`0052c508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c508.md) [`0054ed44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ed44.md) · 呼出先 4件 [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c290) · [`0052c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c2a4) · [`0052c2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c2ac)
- 新版 `0052c2d0`（命令位置の公開資料なし） · `0052c2e4`（命令位置の公開資料なし） · `0052c2ec`（命令位置の公開資料なし）

~~~diff
- 0052c290 ["INT_ADD", "register:40f0:8", ["const:52c290:8", "const:4:8"]]
- 0052c290 ["CALL", null, ["callee:00c53da0:8"]]
+ 0052c2d0 ["INT_ADD", "register:40f0:8", ["const:52c2d0:8", "const:4:8"]]
+ 0052c2d0 ["CALL", null, ["callee:00c53da0:8"]]
- 0052c290 bytes 9c9e1c94
+ 0052c2d0 bytes b49e1c94
- 0052c2a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c2a4 ["INT_ADD", "register:40f0:8", ["const:52c2a4:8", "const:4:8"]]
- 0052c2a4 ["CALLIND", null, ["register:0:8"]]
+ 0052c2e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c2e4 ["INT_ADD", "register:40f0:8", ["const:52c2e4:8", "const:4:8"]]
+ 0052c2e4 ["CALLIND", null, ["register:0:8"]]
- 0052c2a4 bytes 00013fd6
+ 0052c2e4 bytes 00013fd6
- 0052c2ac ["INT_ADD", "register:40f0:8", ["const:52c2ac:8", "const:4:8"]]
- 0052c2ac ["CALL", null, ["callee:00c57f50:8"]]
+ 0052c2ec ["INT_ADD", "register:40f0:8", ["const:52c2ec:8", "const:4:8"]]
+ 0052c2ec ["CALL", null, ["callee:00c57f50:8"]]
- 0052c2ac bytes f5ae1c94
+ 0052c2ec bytes 19af1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5305317f90e65728cb329f5d83865d73"></a>

### [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) → [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md) FUN_0052c394

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) · 呼出先 7件 [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`0054eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) · 呼出先 7件 [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005485c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005485c4.md) [`0054ebcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ebcc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3a8) · [`0052c3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3cc) · [`0052c3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3f8)
- 新版 `0052c3e8`（命令位置の公開資料なし） · `0052c40c`（命令位置の公開資料なし） · `0052c438`（命令位置の公開資料なし）

~~~diff
- 0052c3a8 ["INT_ADD", "register:40f0:8", ["const:52c3a8:8", "const:4:8"]]
- 0052c3a8 ["CALL", null, ["callee:0054ebcc:8"]]
+ 0052c3e8 ["INT_ADD", "register:40f0:8", ["const:52c3e8:8", "const:4:8"]]
+ 0052c3e8 ["CALL", null, ["callee:0054ebcc:8"]]
- 0052c3a8 bytes f9890094
+ 0052c3e8 bytes f9890094
- 0052c3cc ["INT_ADD", "register:40f0:8", ["const:52c3cc:8", "const:4:8"]]
- 0052c3cc ["CALL", null, ["callee:0054ebcc:8"]]
+ 0052c40c ["INT_ADD", "register:40f0:8", ["const:52c40c:8", "const:4:8"]]
+ 0052c40c ["CALL", null, ["callee:0054ebcc:8"]]
- 0052c3cc bytes f0890094
+ 0052c40c bytes f0890094
- 0052c3f8 ["INT_ADD", "register:40f0:8", ["const:52c3f8:8", "const:4:8"]]
- 0052c3f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052c438 ["INT_ADD", "register:40f0:8", ["const:52c438:8", "const:4:8"]]
+ 0052c438 ["CALL", null, ["callee:00c57f60:8"]]
- 0052c3f8 bytes a6ae1c94
+ 0052c438 bytes caae1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef82d0c81c8146d02973b855fb87f9f1"></a>

### [`0052c4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md) → [`0052c508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c508.md) FUN_0052c508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md#insn-0052c4fc)
- 新版 `0052c53c`（命令位置の公開資料なし）

~~~diff
- 0052c4fc ["INT_ADD", "register:40f0:8", ["const:52c4fc:8", "const:4:8"]]
- 0052c4fc ["CALL", null, ["callee:0052c284:8"]]
+ 0052c53c ["INT_ADD", "register:40f0:8", ["const:52c53c:8", "const:4:8"]]
+ 0052c53c ["CALL", null, ["callee:0052c284:8"]]
- 0052c4fc bytes 52ffff97
+ 0052c53c bytes 52ffff97
~~~


<a id="compare-3bfbce0452d37af268098a517c4068ab"></a>

### [`0052c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md) → [`0052c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c570.md) FUN_0052c570

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c574) · [`0052c5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c5bc) · [`0052c5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c5d0)
- 新版 `0052c5b4`（命令位置の公開資料なし） · `0052c5fc`（命令位置の公開資料なし） · `0052c610`（命令位置の公開資料なし）

~~~diff
- 0052c574 ["INT_ADD", "register:40f0:8", ["const:52c574:8", "const:4:8"]]
- 0052c574 ["CALL", null, ["callee:00c57f80:8"]]
+ 0052c5b4 ["INT_ADD", "register:40f0:8", ["const:52c5b4:8", "const:4:8"]]
+ 0052c5b4 ["CALL", null, ["callee:00c57f80:8"]]
- 0052c574 bytes 4fae1c94
+ 0052c5b4 bytes 73ae1c94
- 0052c5bc ["INT_ADD", "register:40f0:8", ["const:52c5bc:8", "const:4:8"]]
- 0052c5bc ["CALL", null, ["callee:00c53da0:8"]]
+ 0052c5fc ["INT_ADD", "register:40f0:8", ["const:52c5fc:8", "const:4:8"]]
+ 0052c5fc ["CALL", null, ["callee:00c53da0:8"]]
- 0052c5bc bytes d19d1c94
+ 0052c5fc bytes e99d1c94
- 0052c5d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c5d0 ["INT_ADD", "register:40f0:8", ["const:52c5d0:8", "const:4:8"]]
- 0052c5d0 ["CALLIND", null, ["register:0:8"]]
+ 0052c610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c610 ["INT_ADD", "register:40f0:8", ["const:52c610:8", "const:4:8"]]
+ 0052c610 ["CALLIND", null, ["register:0:8"]]
- 0052c5d0 bytes 00013fd6
+ 0052c610 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-804d8a33b8802307c19cc43e19de4a82"></a>

### [`0052c618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md) → [`0052c658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c658.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS6_9a

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ef10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054ef50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ef50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c674) · [`0052c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c6a0) · [`0052c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c6d0)
- 新版 `0052c6b4`（命令位置の公開資料なし） · `0052c6e0`（命令位置の公開資料なし） · `0052c710`（命令位置の公開資料なし）

~~~diff
- 0052c674 ["INT_ADD", "register:40f0:8", ["const:52c674:8", "const:4:8"]]
- 0052c674 ["CALL", null, ["callee:0054ef50:8"]]
+ 0052c6b4 ["INT_ADD", "register:40f0:8", ["const:52c6b4:8", "const:4:8"]]
+ 0052c6b4 ["CALL", null, ["callee:0054ef50:8"]]
- 0052c674 bytes 278a0094
+ 0052c6b4 bytes 278a0094
- 0052c6a0 ["INT_ADD", "register:40f0:8", ["const:52c6a0:8", "const:4:8"]]
- 0052c6a0 ["CALL", null, ["callee:00c5a010:8"]]
+ 0052c6e0 ["INT_ADD", "register:40f0:8", ["const:52c6e0:8", "const:4:8"]]
+ 0052c6e0 ["CALL", null, ["callee:00c5a010:8"]]
- 0052c6a0 bytes 28b61c94
+ 0052c6e0 bytes 4cb61c94
- 0052c6d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c6d0 ["INT_ADD", "register:40f0:8", ["const:52c6d0:8", "const:4:8"]]
- 0052c6d0 ["CALLIND", null, ["register:0:8"]]
+ 0052c710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c710 ["INT_ADD", "register:40f0:8", ["const:52c710:8", "const:4:8"]]
+ 0052c710 ["CALLIND", null, ["register:0:8"]]
- 0052c6d0 bytes 00013fd6
+ 0052c710 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b265047efcd0962a212b30fe689b8c2d"></a>

### [`0052c744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md) → [`0052c784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c784.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS_17Cer

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c798) · [`0052c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c7d4) · [`0052c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c830)
- 新版 `0052c7d8`（命令位置の公開資料なし） · `0052c814`（命令位置の公開資料なし） · `0052c870`（命令位置の公開資料なし）

~~~diff
- 0052c798 ["INT_ADD", "register:40f0:8", ["const:52c798:8", "const:4:8"]]
- 0052c798 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052c7d8 ["INT_ADD", "register:40f0:8", ["const:52c7d8:8", "const:4:8"]]
+ 0052c7d8 ["CALL", null, ["callee:00c57f60:8"]]
- 0052c798 bytes bead1c94
+ 0052c7d8 bytes e2ad1c94
- 0052c7d4 ["INT_ADD", "register:40f0:8", ["const:52c7d4:8", "const:4:8"]]
- 0052c7d4 ["CALL", null, ["callee:00c5a010:8"]]
+ 0052c814 ["INT_ADD", "register:40f0:8", ["const:52c814:8", "const:4:8"]]
+ 0052c814 ["CALL", null, ["callee:00c5a010:8"]]
- 0052c7d4 bytes dbb51c94
+ 0052c814 bytes ffb51c94
- 0052c830 ["INT_ADD", "register:40f0:8", ["const:52c830:8", "const:4:8"]]
- 0052c830 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0052c870 ["INT_ADD", "register:40f0:8", ["const:52c870:8", "const:4:8"]]
+ 0052c870 ["CALL", null, ["callee:00c57fb0:8"]]
- 0052c830 bytes acad1c94
+ 0052c870 bytes d0ad1c94
~~~


<a id="compare-cd43bbdb9b0b3abbf08021b3f9cc350d"></a>

### [`0052c834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md) → [`0052c874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c874.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNS_17Certificate_StoreERKNSt6__ndk112basic_strin

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ef10.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054ef50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ef50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c890) · [`0052c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c89c) · [`0052c8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c8d8)
- 新版 `0052c8d0`（命令位置の公開資料なし） · `0052c8dc`（命令位置の公開資料なし） · `0052c918`（命令位置の公開資料なし）

~~~diff
- 0052c890 ["INT_ADD", "register:40f0:8", ["const:52c890:8", "const:4:8"]]
- 0052c890 ["CALL", null, ["callee:0054ef50:8"]]
+ 0052c8d0 ["INT_ADD", "register:40f0:8", ["const:52c8d0:8", "const:4:8"]]
+ 0052c8d0 ["CALL", null, ["callee:0054ef50:8"]]
- 0052c890 bytes a0890094
+ 0052c8d0 bytes a0890094
- 0052c89c ["INT_ADD", "register:40f0:8", ["const:52c89c:8", "const:4:8"]]
- 0052c89c ["CALL", null, ["callee:00c57f60:8"]]
+ 0052c8dc ["INT_ADD", "register:40f0:8", ["const:52c8dc:8", "const:4:8"]]
+ 0052c8dc ["CALL", null, ["callee:00c57f60:8"]]
- 0052c89c bytes 7dad1c94
+ 0052c8dc bytes a1ad1c94
- 0052c8d8 ["INT_ADD", "register:40f0:8", ["const:52c8d8:8", "const:4:8"]]
- 0052c8d8 ["CALL", null, ["callee:00c5a010:8"]]
+ 0052c918 ["INT_ADD", "register:40f0:8", ["const:52c918:8", "const:4:8"]]
+ 0052c918 ["CALL", null, ["callee:00c5a010:8"]]
- 0052c8d8 bytes 9ab51c94
+ 0052c918 bytes beb51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0377f31414aa491335e2a2fc2ad4a37f"></a>

### [`0052c998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md) → [`0052c9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c9d8.md) _ZN5Botan28Path_Validation_RestrictionsC1Ebmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ca14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca14) · [`0052ca2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca2c) · [`0052ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca60)
- 新版 `0052ca54`（命令位置の公開資料なし） · `0052ca6c`（命令位置の公開資料なし） · `0052caa0`（命令位置の公開資料なし）

~~~diff
- 0052ca14 ["INT_ADD", "register:40f0:8", ["const:52ca14:8", "const:4:8"]]
- 0052ca14 ["CALL", null, ["callee:0054a654:8"]]
+ 0052ca54 ["INT_ADD", "register:40f0:8", ["const:52ca54:8", "const:4:8"]]
+ 0052ca54 ["CALL", null, ["callee:0054a654:8"]]
- 0052ca14 bytes 00770094
+ 0052ca54 bytes 00770094
- 0052ca2c ["INT_ADD", "register:40f0:8", ["const:52ca2c:8", "const:4:8"]]
- 0052ca2c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052ca6c ["INT_ADD", "register:40f0:8", ["const:52ca6c:8", "const:4:8"]]
+ 0052ca6c ["CALL", null, ["callee:00c57f80:8"]]
- 0052ca2c bytes 21ad1c94
+ 0052ca6c bytes 45ad1c94
- 0052ca60 ["INT_ADD", "register:40f0:8", ["const:52ca60:8", "const:4:8"]]
- 0052ca60 ["CALL", null, ["callee:0054a654:8"]]
+ 0052caa0 ["INT_ADD", "register:40f0:8", ["const:52caa0:8", "const:4:8"]]
+ 0052caa0 ["CALL", null, ["callee:0054a654:8"]]
- 0052ca60 bytes ed760094
+ 0052caa0 bytes ed760094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1f6e0abe9d88c2566b54ac40283aa4"></a>

### [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) → [`0052ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052ce30.md) _ZN5Botan22Path_Validation_ResultC1ENSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f50.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00501db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`0053f330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f330.md) [`0053f544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f544.md)
- 新版 呼出元 1件 [`00c5a020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a020.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00501df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501df8.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`0053f370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f370.md) [`0053f584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f584.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce50) · [`0052ce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce80) · [`0052ce90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce90)
- 新版 `0052ce90`（命令位置の公開資料なし） · `0052cec0`（命令位置の公開資料なし） · `0052ced0`（命令位置の公開資料なし）

~~~diff
- 0052ce50 ["INT_ADD", "register:40f0:8", ["const:52ce50:8", "const:4:8"]]
- 0052ce50 ["CALL", null, ["callee:0054ebcc:8"]]
+ 0052ce90 ["INT_ADD", "register:40f0:8", ["const:52ce90:8", "const:4:8"]]
+ 0052ce90 ["CALL", null, ["callee:0054ebcc:8"]]
- 0052ce50 bytes 4f870094
+ 0052ce90 bytes 4f870094
- 0052ce80 ["INT_ADD", "register:40f0:8", ["const:52ce80:8", "const:4:8"]]
- 0052ce80 ["CALL", null, ["callee:0053f370:8"]]
+ 0052cec0 ["INT_ADD", "register:40f0:8", ["const:52cec0:8", "const:4:8"]]
+ 0052cec0 ["CALL", null, ["callee:0053f370:8"]]
- 0052ce80 bytes 2c490094
+ 0052cec0 bytes 2c490094
- 0052ce90 ["INT_ADD", "register:40f0:8", ["const:52ce90:8", "const:4:8"]]
- 0052ce90 ["CALL", null, ["callee:0053f850:8"]]
+ 0052ced0 ["INT_ADD", "register:40f0:8", ["const:52ced0:8", "const:4:8"]]
+ 0052ced0 ["CALL", null, ["callee:0053f850:8"]]
- 0052ce90 bytes 604a0094
+ 0052ced0 bytes 604a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234c875afc89c8851dc215890d5db899"></a>

### [`0052d284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md) → [`0052d2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d2c4.md) _ZNK5Botan22Path_Validation_Result14trusted_hashesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052d2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d2f8) · [`0052d308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d308) · [`0052d328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d328)
- 新版 `0052d338`（命令位置の公開資料なし） · `0052d348`（命令位置の公開資料なし） · `0052d368`（命令位置の公開資料なし）

~~~diff
- 0052d2f8 ["INT_ADD", "register:40f0:8", ["const:52d2f8:8", "const:4:8"]]
- 0052d2f8 ["CALL", null, ["callee:00c59f60:8"]]
+ 0052d338 ["INT_ADD", "register:40f0:8", ["const:52d338:8", "const:4:8"]]
+ 0052d338 ["CALL", null, ["callee:00c59f60:8"]]
- 0052d2f8 bytes e6b21c94
+ 0052d338 bytes 0ab31c94
- 0052d308 ["INT_ADD", "register:40f0:8", ["const:52d308:8", "const:4:8"]]
- 0052d308 ["CALL", null, ["callee:0054a654:8"]]
+ 0052d348 ["INT_ADD", "register:40f0:8", ["const:52d348:8", "const:4:8"]]
+ 0052d348 ["CALL", null, ["callee:0054a654:8"]]
- 0052d308 bytes c3740094
+ 0052d348 bytes c3740094
- 0052d328 ["INT_ADD", "register:40f0:8", ["const:52d328:8", "const:4:8"]]
- 0052d328 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052d368 ["INT_ADD", "register:40f0:8", ["const:52d368:8", "const:4:8"]]
+ 0052d368 ["CALL", null, ["callee:00c57f60:8"]]
- 0052d328 bytes daaa1c94
+ 0052d368 bytes feaa1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4291ca218cb5d6360ffa3f67332f06c"></a>

### [`0052dc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md) → [`0052dc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dc4c.md) FUN_0052dc4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc30) · [`0052dc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc78) · [`0052dc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc98)
- 新版 `0052dc70`（命令位置の公開資料なし） · `0052dcb8`（命令位置の公開資料なし） · `0052dcd8`（命令位置の公開資料なし）

~~~diff
- 0052dc30 ["INT_ADD", "register:40f0:8", ["const:52dc30:8", "const:4:8"]]
- 0052dc30 ["CALL", null, ["callee:00c580b0:8"]]
+ 0052dc70 ["INT_ADD", "register:40f0:8", ["const:52dc70:8", "const:4:8"]]
+ 0052dc70 ["CALL", null, ["callee:00c580b0:8"]]
- 0052dc30 bytes eca81c94
+ 0052dc70 bytes 10a91c94
- 0052dc78 ["INT_ADD", "register:40f0:8", ["const:52dc78:8", "const:4:8"]]
- 0052dc78 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052dcb8 ["INT_ADD", "register:40f0:8", ["const:52dcb8:8", "const:4:8"]]
+ 0052dcb8 ["CALL", null, ["callee:00c57f60:8"]]
- 0052dc78 bytes 86a81c94
+ 0052dcb8 bytes aaa81c94
- 0052dc98 ["INT_ADD", "register:40f0:8", ["const:52dc98:8", "const:4:8"]]
- 0052dc98 ["CALL", null, ["callee:00c58010:8"]]
+ 0052dcd8 ["INT_ADD", "register:40f0:8", ["const:52dcd8:8", "const:4:8"]]
+ 0052dcd8 ["CALL", null, ["callee:00c58010:8"]]
- 0052dc98 bytes aaa81c94
+ 0052dcd8 bytes cea81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aca23267623bc3092a99587fe75b75f"></a>

### [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) → [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) FUN_0052dd40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 62件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) [`005db488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db488.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 62件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) [`005ccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md) [`005db4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005db4c8.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0053bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bcf0.md) [`0054f1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f1d4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd50) · [`0052dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd80) · [`0052dd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd9c)
- 新版 `0052dd90`（命令位置の公開資料なし） · `0052ddc0`（命令位置の公開資料なし） · `0052dddc`（命令位置の公開資料なし）

~~~diff
- 0052dd50 ["INT_ADD", "register:40f0:8", ["const:52dd50:8", "const:4:8"]]
- 0052dd50 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0052dd90 ["INT_ADD", "register:40f0:8", ["const:52dd90:8", "const:4:8"]]
+ 0052dd90 ["CALL", null, ["callee:0043bbe4:8"]]
- 0052dd50 bytes 9537fc97
+ 0052dd90 bytes 9537fc97
- 0052dd80 ["INT_ADD", "register:40f0:8", ["const:52dd80:8", "const:4:8"]]
- 0052dd80 ["CALL", null, ["callee:0054f1d4:8"]]
+ 0052ddc0 ["INT_ADD", "register:40f0:8", ["const:52ddc0:8", "const:4:8"]]
+ 0052ddc0 ["CALL", null, ["callee:0054f1d4:8"]]
- 0052dd80 bytes 05850094
+ 0052ddc0 bytes 05850094
- 0052dd9c ["INT_ADD", "register:40f0:8", ["const:52dd9c:8", "const:4:8"]]
- 0052dd9c ["CALL", null, ["callee:0053bcf0:8"]]
+ 0052dddc ["INT_ADD", "register:40f0:8", ["const:52dddc:8", "const:4:8"]]
+ 0052dddc ["CALL", null, ["callee:0053bcf0:8"]]
- 0052dd9c bytes c5370094
+ 0052dddc bytes c5370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a6a7897724da21552890bd617e4f2f"></a>

### [`0052ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052ef7c.md) → [`0052efbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052efbc.md) FUN_0052efbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052ef7c.md#insn-0052ef98)
- 新版 `0052efd8`（命令位置の公開資料なし）

~~~diff
- 0052ef98 ["INT_ADD", "register:40f0:8", ["const:52ef98:8", "const:4:8"]]
- 0052ef98 ["CALL", null, ["callee:00c57f80:8"]]
+ 0052efd8 ["INT_ADD", "register:40f0:8", ["const:52efd8:8", "const:4:8"]]
+ 0052efd8 ["CALL", null, ["callee:00c57f80:8"]]
- 0052ef98 bytes c6a31c94
+ 0052efd8 bytes eaa31c94
~~~


<a id="compare-ecb1cc8f436267fa6777cf1fe84234ea"></a>

### [`0052f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md) → [`0052f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f0f4.md) FUN_0052f0f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md#insn-0052f0c4)
- 新版 `0052f104`（命令位置の公開資料なし）

~~~diff
- 0052f0c4 ["INT_ADD", "register:40f0:8", ["const:52f0c4:8", "const:4:8"]]
- 0052f0c4 ["CALL", null, ["callee:0052f000:8"]]
+ 0052f104 ["INT_ADD", "register:40f0:8", ["const:52f104:8", "const:4:8"]]
+ 0052f104 ["CALL", null, ["callee:0052f000:8"]]
- 0052f0c4 bytes bfffff97
+ 0052f104 bytes bfffff97
~~~


<a id="compare-d9ce999e798eecbdcdf806b887222ad6"></a>

### [`0052f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md) → [`0052f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f3e0.md) FUN_0052f3e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md#insn-0052f3b0)
- 新版 `0052f3f0`（命令位置の公開資料なし）

~~~diff
- 0052f3b0 ["INT_ADD", "register:40f0:8", ["const:52f3b0:8", "const:4:8"]]
- 0052f3b0 ["CALL", null, ["callee:0052f2ec:8"]]
+ 0052f3f0 ["INT_ADD", "register:40f0:8", ["const:52f3f0:8", "const:4:8"]]
+ 0052f3f0 ["CALL", null, ["callee:0052f2ec:8"]]
- 0052f3b0 bytes bfffff97
+ 0052f3f0 bytes bfffff97
~~~


<a id="compare-eab87b55c451a2008cf9ca452d57768d"></a>

### [`0052f68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md) → [`0052f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f6cc.md) FUN_0052f6cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md#insn-0052f69c)
- 新版 `0052f6dc`（命令位置の公開資料なし）

~~~diff
- 0052f69c ["INT_ADD", "register:40f0:8", ["const:52f69c:8", "const:4:8"]]
- 0052f69c ["CALL", null, ["callee:0052f5d8:8"]]
+ 0052f6dc ["INT_ADD", "register:40f0:8", ["const:52f6dc:8", "const:4:8"]]
+ 0052f6dc ["CALL", null, ["callee:0052f5d8:8"]]
- 0052f69c bytes bfffff97
+ 0052f6dc bytes bfffff97
~~~


<a id="compare-9a8fe1a5411657e191559bd7e30ffa11"></a>

### [`0052fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md) → [`0052fdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdbc.md) FUN_0052fdbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md#insn-0052fd98) · [`0052fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md#insn-0052fda8)
- 新版 `0052fdd8`（命令位置の公開資料なし） · `0052fde8`（命令位置の公開資料なし）

~~~diff
- 0052fd98 ["INT_ADD", "register:40f0:8", ["const:52fd98:8", "const:4:8"]]
- 0052fd98 ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fdd8 ["INT_ADD", "register:40f0:8", ["const:52fdd8:8", "const:4:8"]]
+ 0052fdd8 ["CALL", null, ["callee:00c57f80:8"]]
- 0052fd98 bytes 46a01c94
+ 0052fdd8 bytes 6aa01c94
- 0052fda8 ["INT_ADD", "register:40f0:8", ["const:52fda8:8", "const:4:8"]]
- 0052fda8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fde8 ["INT_ADD", "register:40f0:8", ["const:52fde8:8", "const:4:8"]]
+ 0052fde8 ["CALL", null, ["callee:00c57f80:8"]]
- 0052fda8 bytes 42a01c94
+ 0052fde8 bytes 66a01c94
~~~


<a id="compare-80ec93b9bb305013d1242ecfe24129bd"></a>

### [`0052fdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdbc.md) → [`0052fdfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fdfc.md) FUN_0052fdfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdbc.md#insn-0052fddc)
- 新版 `0052fe1c`（命令位置の公開資料なし）

~~~diff
- 0052fddc ["INT_ADD", "register:40f0:8", ["const:52fddc:8", "const:4:8"]]
- 0052fddc ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
+ 0052fe1c ["CALL", null, ["callee:00c57f80:8"]]
- 0052fddc bytes 35a01c94
+ 0052fe1c bytes 59a01c94
~~~


<a id="compare-b3444aa39349a2e1405bad6c4cdbaef7"></a>

### [`0052fdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md) → [`0052fe30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe30.md) FUN_0052fe30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md#insn-0052fe0c) · [`0052fe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md#insn-0052fe1c)
- 新版 `0052fe4c`（命令位置の公開資料なし） · `0052fe5c`（命令位置の公開資料なし）

~~~diff
- 0052fe0c ["INT_ADD", "register:40f0:8", ["const:52fe0c:8", "const:4:8"]]
- 0052fe0c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fe4c ["INT_ADD", "register:40f0:8", ["const:52fe4c:8", "const:4:8"]]
+ 0052fe4c ["CALL", null, ["callee:00c57f80:8"]]
- 0052fe0c bytes 29a01c94
+ 0052fe4c bytes 4da01c94
- 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
- 0052fe1c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fe5c ["INT_ADD", "register:40f0:8", ["const:52fe5c:8", "const:4:8"]]
+ 0052fe5c ["CALL", null, ["callee:00c57f80:8"]]
- 0052fe1c bytes 25a01c94
+ 0052fe5c bytes 49a01c94
~~~


<a id="compare-ffb6241d8a49552b7c991f52a7b897e5"></a>

### [`0052fe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md) → [`0052fe70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fe70.md) FUN_0052fe70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md#insn-0052fe4c) · [`0052fe5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md#insn-0052fe5c)
- 新版 `0052fe8c`（命令位置の公開資料なし） · `0052fe9c`（命令位置の公開資料なし）

~~~diff
- 0052fe4c ["INT_ADD", "register:40f0:8", ["const:52fe4c:8", "const:4:8"]]
- 0052fe4c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fe8c ["INT_ADD", "register:40f0:8", ["const:52fe8c:8", "const:4:8"]]
+ 0052fe8c ["CALL", null, ["callee:00c57f80:8"]]
- 0052fe4c bytes 19a01c94
+ 0052fe8c bytes 3da01c94
- 0052fe5c ["INT_ADD", "register:40f0:8", ["const:52fe5c:8", "const:4:8"]]
- 0052fe5c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052fe9c ["INT_ADD", "register:40f0:8", ["const:52fe9c:8", "const:4:8"]]
+ 0052fe9c ["CALL", null, ["callee:00c57f80:8"]]
- 0052fe5c bytes 15a01c94
+ 0052fe9c bytes 39a01c94
~~~


<a id="compare-873844f9a7b0999adda3e606e99ef3b5"></a>

### [`005303bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md) → [`005303fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005303fc.md) FUN_005303fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005302e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005303cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md#insn-005303cc)
- 新版 `0053040c`（命令位置の公開資料なし）

~~~diff
- 005303cc ["INT_ADD", "register:40f0:8", ["const:5303cc:8", "const:4:8"]]
- 005303cc ["CALL", null, ["callee:00530328:8"]]
+ 0053040c ["INT_ADD", "register:40f0:8", ["const:53040c:8", "const:4:8"]]
+ 0053040c ["CALL", null, ["callee:00530328:8"]]
- 005303cc bytes c7ffff97
+ 0053040c bytes c7ffff97
~~~


<a id="compare-3e0006f3a078190a632326c1ce3096ea"></a>

### [`005303e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md) → [`00530420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530420.md) FUN_00530420

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cbc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbc50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbc90.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005303f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md#insn-005303f0) · [`005303f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md#insn-005303f8)
- 新版 `00530430`（命令位置の公開資料なし） · `00530438`（命令位置の公開資料なし）

~~~diff
- 005303f0 ["INT_ADD", "register:40f0:8", ["const:5303f0:8", "const:4:8"]]
- 005303f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00530430 ["INT_ADD", "register:40f0:8", ["const:530430:8", "const:4:8"]]
+ 00530430 ["CALL", null, ["callee:00c57f60:8"]]
- 005303f0 bytes a89e1c94
+ 00530430 bytes cc9e1c94
- 005303f8 ["INT_ADD", "register:40f0:8", ["const:5303f8:8", "const:4:8"]]
- 005303f8 ["CALL", null, ["callee:004cbc90:8"]]
+ 00530438 ["INT_ADD", "register:40f0:8", ["const:530438:8", "const:4:8"]]
+ 00530438 ["CALL", null, ["callee:004cbc90:8"]]
- 005303f8 bytes 166efe97
+ 00530438 bytes 166efe97
~~~


<a id="compare-f3a00967f5b00e932947099aab8ba92b"></a>

### [`0053043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md) → [`0053047c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053047c.md) FUN_0053047c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md#insn-00530458) · [`00530464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md#insn-00530464)
- 新版 `00530498`（命令位置の公開資料なし） · `005304a4`（命令位置の公開資料なし）

~~~diff
- 00530458 ["INT_ADD", "register:40f0:8", ["const:530458:8", "const:4:8"]]
- 00530458 ["CALL", null, ["callee:00c57f80:8"]]
+ 00530498 ["INT_ADD", "register:40f0:8", ["const:530498:8", "const:4:8"]]
+ 00530498 ["CALL", null, ["callee:00c57f80:8"]]
- 00530458 bytes 969e1c94
+ 00530498 bytes ba9e1c94
- 00530464 ["INT_ADD", "register:40f0:8", ["const:530464:8", "const:4:8"]]
- 00530464 ["CALL", null, ["callee:0053afd0:8"]]
+ 005304a4 ["INT_ADD", "register:40f0:8", ["const:5304a4:8", "const:4:8"]]
+ 005304a4 ["CALL", null, ["callee:0053afd0:8"]]
- 00530464 bytes cb2a0094
+ 005304a4 bytes cb2a0094
~~~


<a id="compare-4ae54a8672a68d1901e8480560c597ce"></a>

### [`00530610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530610.md) → [`00530650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530650.md) FUN_00530650

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530610.md#insn-00530638)
- 新版 `00530678`（命令位置の公開資料なし）

~~~diff
- 00530638 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530638 ["INT_ADD", "register:40f0:8", ["const:530638:8", "const:4:8"]]
- 00530638 ["CALLIND", null, ["register:0:8"]]
+ 00530678 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530678 ["INT_ADD", "register:40f0:8", ["const:530678:8", "const:4:8"]]
+ 00530678 ["CALLIND", null, ["register:0:8"]]
- 00530638 bytes 20013fd6
+ 00530678 bytes 20013fd6
~~~


<a id="compare-137a2485d7a10aaf5cba4b565c9a1ccc"></a>

### [`005308b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md) → [`005308f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005308f8.md) FUN_005308f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005308c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md#insn-005308c8)
- 新版 `00530908`（命令位置の公開資料なし）

~~~diff
- 005308c8 ["INT_ADD", "register:40f0:8", ["const:5308c8:8", "const:4:8"]]
- 005308c8 ["CALL", null, ["callee:0053080c:8"]]
+ 00530908 ["INT_ADD", "register:40f0:8", ["const:530908:8", "const:4:8"]]
+ 00530908 ["CALL", null, ["callee:0053080c:8"]]
- 005308c8 bytes c1ffff97
+ 00530908 bytes c1ffff97
~~~


<a id="compare-ce8315aae6dc43fac9dc076644a95756"></a>

### [`0053094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md) → [`0053098c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053098c.md) FUN_0053098c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md#insn-00530960)
- 新版 `005309a0`（命令位置の公開資料なし）

~~~diff
- 00530960 ["INT_ADD", "register:40f0:8", ["const:530960:8", "const:4:8"]]
- 00530960 ["CALL", null, ["callee:0053080c:8"]]
+ 005309a0 ["INT_ADD", "register:40f0:8", ["const:5309a0:8", "const:4:8"]]
+ 005309a0 ["CALL", null, ["callee:0053080c:8"]]
- 00530960 bytes 9bffff97
+ 005309a0 bytes 9bffff97
~~~


<a id="compare-a519ef069dccf58d35edf8f5ba164e43"></a>

### [`00530a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md) → [`00530a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530a88.md) FUN_00530a88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00530974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005309b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md#insn-00530a58)
- 新版 `00530a98`（命令位置の公開資料なし）

~~~diff
- 00530a58 ["INT_ADD", "register:40f0:8", ["const:530a58:8", "const:4:8"]]
- 00530a58 ["CALL", null, ["callee:005309b4:8"]]
+ 00530a98 ["INT_ADD", "register:40f0:8", ["const:530a98:8", "const:4:8"]]
+ 00530a98 ["CALL", null, ["callee:005309b4:8"]]
- 00530a58 bytes c7ffff97
+ 00530a98 bytes c7ffff97
~~~


<a id="compare-02c3a592583812d81fd980555b2ca5db"></a>

### [`00530a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md) → [`00530aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530aac.md) FUN_00530aac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb72c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb76c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md#insn-00530a7c) · [`00530a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md#insn-00530a84)
- 新版 `00530abc`（命令位置の公開資料なし） · `00530ac4`（命令位置の公開資料なし）

~~~diff
- 00530a7c ["INT_ADD", "register:40f0:8", ["const:530a7c:8", "const:4:8"]]
- 00530a7c ["CALL", null, ["callee:00c57f60:8"]]
+ 00530abc ["INT_ADD", "register:40f0:8", ["const:530abc:8", "const:4:8"]]
+ 00530abc ["CALL", null, ["callee:00c57f60:8"]]
- 00530a7c bytes 059d1c94
+ 00530abc bytes 299d1c94
- 00530a84 ["INT_ADD", "register:40f0:8", ["const:530a84:8", "const:4:8"]]
- 00530a84 ["CALL", null, ["callee:004cb76c:8"]]
+ 00530ac4 ["INT_ADD", "register:40f0:8", ["const:530ac4:8", "const:4:8"]]
+ 00530ac4 ["CALL", null, ["callee:004cb76c:8"]]
- 00530a84 bytes 2a6bfe97
+ 00530ac4 bytes 2a6bfe97
~~~


<a id="compare-754ccddafbc88d7fb97c64cc55f972c9"></a>

### [`00530c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md) → [`00530c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530c54.md) FUN_00530c54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb8e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb928.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md#insn-00530c24) · [`00530c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md#insn-00530c2c)
- 新版 `00530c64`（命令位置の公開資料なし） · `00530c6c`（命令位置の公開資料なし）

~~~diff
- 00530c24 ["INT_ADD", "register:40f0:8", ["const:530c24:8", "const:4:8"]]
- 00530c24 ["CALL", null, ["callee:00c57f60:8"]]
+ 00530c64 ["INT_ADD", "register:40f0:8", ["const:530c64:8", "const:4:8"]]
+ 00530c64 ["CALL", null, ["callee:00c57f60:8"]]
- 00530c24 bytes 9b9c1c94
+ 00530c64 bytes bf9c1c94
- 00530c2c ["INT_ADD", "register:40f0:8", ["const:530c2c:8", "const:4:8"]]
- 00530c2c ["CALL", null, ["callee:004cb928:8"]]
+ 00530c6c ["INT_ADD", "register:40f0:8", ["const:530c6c:8", "const:4:8"]]
+ 00530c6c ["CALL", null, ["callee:004cb928:8"]]
- 00530c2c bytes 2f6bfe97
+ 00530c6c bytes 2f6bfe97
~~~


<a id="compare-685b18df05cbada45cbf43971cf25fe7"></a>

### [`00530dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md) → [`00530dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530dfc.md) FUN_00530dfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cba9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbadc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md#insn-00530dcc) · [`00530dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md#insn-00530dd4)
- 新版 `00530e0c`（命令位置の公開資料なし） · `00530e14`（命令位置の公開資料なし）

~~~diff
- 00530dcc ["INT_ADD", "register:40f0:8", ["const:530dcc:8", "const:4:8"]]
- 00530dcc ["CALL", null, ["callee:00c57f60:8"]]
+ 00530e0c ["INT_ADD", "register:40f0:8", ["const:530e0c:8", "const:4:8"]]
+ 00530e0c ["CALL", null, ["callee:00c57f60:8"]]
- 00530dcc bytes 319c1c94
+ 00530e0c bytes 559c1c94
- 00530dd4 ["INT_ADD", "register:40f0:8", ["const:530dd4:8", "const:4:8"]]
- 00530dd4 ["CALL", null, ["callee:004cbadc:8"]]
+ 00530e14 ["INT_ADD", "register:40f0:8", ["const:530e14:8", "const:4:8"]]
+ 00530e14 ["CALL", null, ["callee:004cbadc:8"]]
- 00530dd4 bytes 326bfe97
+ 00530e14 bytes 326bfe97
~~~


<a id="compare-9eb601bb2582ef7716146acf7ab49ba2"></a>

### [`00530e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md) → [`00530e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530e64.md) FUN_00530e64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e40) · [`00530e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e78) · [`00530e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e88)
- 新版 `00530e80`（命令位置の公開資料なし） · `00530eb8`（命令位置の公開資料なし） · `00530ec8`（命令位置の公開資料なし）

~~~diff
- 00530e40 ["INT_ADD", "register:40f0:8", ["const:530e40:8", "const:4:8"]]
- 00530e40 ["CALL", null, ["callee:0053b464:8"]]
+ 00530e80 ["INT_ADD", "register:40f0:8", ["const:530e80:8", "const:4:8"]]
+ 00530e80 ["CALL", null, ["callee:0053b464:8"]]
- 00530e40 bytes 79290094
+ 00530e80 bytes 79290094
- 00530e78 ["INT_ADD", "register:40f0:8", ["const:530e78:8", "const:4:8"]]
- 00530e78 ["CALL", null, ["callee:00c57f80:8"]]
+ 00530eb8 ["INT_ADD", "register:40f0:8", ["const:530eb8:8", "const:4:8"]]
+ 00530eb8 ["CALL", null, ["callee:00c57f80:8"]]
- 00530e78 bytes 0e9c1c94
+ 00530eb8 bytes 329c1c94
- 00530e88 ["INT_ADD", "register:40f0:8", ["const:530e88:8", "const:4:8"]]
- 00530e88 ["CALL", null, ["callee:00c57f80:8"]]
+ 00530ec8 ["INT_ADD", "register:40f0:8", ["const:530ec8:8", "const:4:8"]]
+ 00530ec8 ["CALL", null, ["callee:00c57f80:8"]]
- 00530e88 bytes 0a9c1c94
+ 00530ec8 bytes 2e9c1c94
~~~


<a id="compare-ebe6ee4daff28dec75decfd550abaeae"></a>

### [`005312d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005312d0.md) → [`00531310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531310.md) FUN_00531310

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005312f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005312d0.md#insn-005312f0)
- 新版 `00531330`（命令位置の公開資料なし）

~~~diff
- 005312f0 ["INT_ADD", "register:40f0:8", ["const:5312f0:8", "const:4:8"]]
- 005312f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531330 ["INT_ADD", "register:40f0:8", ["const:531330:8", "const:4:8"]]
+ 00531330 ["CALL", null, ["callee:00c57f80:8"]]
- 005312f0 bytes f09a1c94
+ 00531330 bytes 149b1c94
~~~


<a id="compare-28e77667ad9eea6f64573f12e4244d25"></a>

### [`005314d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005314d8.md) → [`00531518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531518.md) FUN_00531518

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005314f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005314d8.md#insn-005314f8)
- 新版 `00531538`（命令位置の公開資料なし）

~~~diff
- 005314f8 ["INT_ADD", "register:40f0:8", ["const:5314f8:8", "const:4:8"]]
- 005314f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531538 ["INT_ADD", "register:40f0:8", ["const:531538:8", "const:4:8"]]
+ 00531538 ["CALL", null, ["callee:00c57f80:8"]]
- 005314f8 bytes 6e9a1c94
+ 00531538 bytes 929a1c94
~~~


<a id="compare-b29bdb41884d13ca78a8c1e26cdb4f71"></a>

### [`0053151c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md) → [`0053155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053155c.md) FUN_0053155c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md#insn-00531534) · [`00531540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md#insn-00531540)
- 新版 `00531574`（命令位置の公開資料なし） · `00531580`（命令位置の公開資料なし）

~~~diff
- 00531534 ["INT_ADD", "register:40f0:8", ["const:531534:8", "const:4:8"]]
- 00531534 ["CALL", null, ["callee:0053afd0:8"]]
+ 00531574 ["INT_ADD", "register:40f0:8", ["const:531574:8", "const:4:8"]]
+ 00531574 ["CALL", null, ["callee:0053afd0:8"]]
- 00531534 bytes 97260094
+ 00531574 bytes 97260094
- 00531540 ["INT_ADD", "register:40f0:8", ["const:531540:8", "const:4:8"]]
- 00531540 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00531580 ["INT_ADD", "register:40f0:8", ["const:531580:8", "const:4:8"]]
+ 00531580 ["CALL", null, ["callee:0046d4d0:8"]]
- 00531540 bytes d4effc97
+ 00531580 bytes d4effc97
~~~


<a id="compare-8a420786000dedf6021b424e3d50d2b8"></a>

### [`005316a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316a4.md) → [`005316e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005316e4.md) FUN_005316e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005316bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316a4.md#insn-005316bc)
- 新版 `005316fc`（命令位置の公開資料なし）

~~~diff
- 005316bc ["INT_ADD", "register:40f0:8", ["const:5316bc:8", "const:4:8"]]
- 005316bc ["CALL", null, ["callee:0053afd0:8"]]
+ 005316fc ["INT_ADD", "register:40f0:8", ["const:5316fc:8", "const:4:8"]]
+ 005316fc ["CALL", null, ["callee:0053afd0:8"]]
- 005316bc bytes 35260094
+ 005316fc bytes 35260094
~~~


<a id="compare-6e0017e159a28b98541db503d7eb7372"></a>

### [`005316d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md) → [`00531714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531714.md) FUN_00531714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005316ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md#insn-005316ec) · [`005316f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md#insn-005316f8)
- 新版 `0053172c`（命令位置の公開資料なし） · `00531738`（命令位置の公開資料なし）

~~~diff
- 005316ec ["INT_ADD", "register:40f0:8", ["const:5316ec:8", "const:4:8"]]
- 005316ec ["CALL", null, ["callee:0053afd0:8"]]
+ 0053172c ["INT_ADD", "register:40f0:8", ["const:53172c:8", "const:4:8"]]
+ 0053172c ["CALL", null, ["callee:0053afd0:8"]]
- 005316ec bytes 29260094
+ 0053172c bytes 29260094
- 005316f8 ["INT_ADD", "register:40f0:8", ["const:5316f8:8", "const:4:8"]]
- 005316f8 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00531738 ["INT_ADD", "register:40f0:8", ["const:531738:8", "const:4:8"]]
+ 00531738 ["CALL", null, ["callee:0046d4d0:8"]]
- 005316f8 bytes 66effc97
+ 00531738 bytes 66effc97
~~~


<a id="compare-f6400b32052ea5c2c15670f5d1c69370"></a>

### [`00531874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531874.md) → [`005318b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318b4.md) FUN_005318b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053188c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531874.md#insn-0053188c)
- 新版 `005318cc`（命令位置の公開資料なし）

~~~diff
- 0053188c ["INT_ADD", "register:40f0:8", ["const:53188c:8", "const:4:8"]]
- 0053188c ["CALL", null, ["callee:0053afd0:8"]]
+ 005318cc ["INT_ADD", "register:40f0:8", ["const:5318cc:8", "const:4:8"]]
+ 005318cc ["CALL", null, ["callee:0053afd0:8"]]
- 0053188c bytes c1250094
+ 005318cc bytes c1250094
~~~


<a id="compare-44125a9d6c81a7030aed3968d8a58bb4"></a>

### [`005318a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md) → [`005318e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005318e4.md) FUN_005318e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005318bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md#insn-005318bc) · [`005318c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md#insn-005318c8)
- 新版 `005318fc`（命令位置の公開資料なし） · `00531908`（命令位置の公開資料なし）

~~~diff
- 005318bc ["INT_ADD", "register:40f0:8", ["const:5318bc:8", "const:4:8"]]
- 005318bc ["CALL", null, ["callee:0053afd0:8"]]
+ 005318fc ["INT_ADD", "register:40f0:8", ["const:5318fc:8", "const:4:8"]]
+ 005318fc ["CALL", null, ["callee:0053afd0:8"]]
- 005318bc bytes b5250094
+ 005318fc bytes b5250094
- 005318c8 ["INT_ADD", "register:40f0:8", ["const:5318c8:8", "const:4:8"]]
- 005318c8 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00531908 ["INT_ADD", "register:40f0:8", ["const:531908:8", "const:4:8"]]
+ 00531908 ["CALL", null, ["callee:0046d4d0:8"]]
- 005318c8 bytes f2eefc97
+ 00531908 bytes f2eefc97
~~~


<a id="compare-6cd7ed6bacf6daa7e577520401e051ca"></a>

### [`00531b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b0c.md) → [`00531b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531b4c.md) FUN_00531b4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b0c.md#insn-00531b54)
- 新版 `00531b94`（命令位置の公開資料なし）

~~~diff
- 00531b54 ["INT_ADD", "register:40f0:8", ["const:531b54:8", "const:4:8"]]
- 00531b54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00531b94 ["INT_ADD", "register:40f0:8", ["const:531b94:8", "const:4:8"]]
+ 00531b94 ["CALL", null, ["callee:00c57f80:8"]]
- 00531b54 bytes d7981c94
+ 00531b94 bytes fb981c94
~~~


<a id="compare-fa99ac5be97b74c280cb22da2e2f43c3"></a>

### [`00531b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md) → [`00531bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md) FUN_00531bc4

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0050f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md#insn-00531bcc) · [`00531bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md#insn-00531bdc)
- 新版 `00531c0c`（命令位置の公開資料なし） · `00531c1c`（命令位置の公開資料なし）

~~~diff
- 00531bcc ["INT_ADD", "register:40f0:8", ["const:531bcc:8", "const:4:8"]]
- 00531bcc ["CALL", null, ["callee:00c57f80:8"]]
+ 00531c0c ["INT_ADD", "register:40f0:8", ["const:531c0c:8", "const:4:8"]]
+ 00531c0c ["CALL", null, ["callee:00c57f80:8"]]
- 00531bcc bytes b9981c94
+ 00531c0c bytes dd981c94
- 00531bdc ["INT_ADD", "register:40f0:8", ["const:531bdc:8", "const:4:8"]]
- 00531bdc ["CALL", null, ["callee:00c57f80:8"]]
+ 00531c1c ["INT_ADD", "register:40f0:8", ["const:531c1c:8", "const:4:8"]]
+ 00531c1c ["CALL", null, ["callee:00c57f80:8"]]
- 00531bdc bytes b5981c94
+ 00531c1c bytes d9981c94
~~~


<a id="compare-c623f765a003ab8e2bee1b8a10db9ffa"></a>

### [`00531d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md) → [`00531d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d74.md) FUN_00531d74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md#insn-00531d48)
- 新版 `00531d88`（命令位置の公開資料なし）

~~~diff
- 00531d48 ["INT_ADD", "register:40f0:8", ["const:531d48:8", "const:4:8"]]
- 00531d48 ["CALL", null, ["callee:0051ad04:8"]]
+ 00531d88 ["INT_ADD", "register:40f0:8", ["const:531d88:8", "const:4:8"]]
+ 00531d88 ["CALL", null, ["callee:0051ad04:8"]]
- 00531d48 bytes dfa3ff97
+ 00531d88 bytes dfa3ff97
~~~


<a id="compare-90cdeb669f47fb499476259dc55e626c"></a>

### [`00531f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531f7c.md) → [`00531fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531fbc.md) FUN_00531fbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531f7c.md#insn-00531fc4)
- 新版 `00532004`（命令位置の公開資料なし）

~~~diff
- 00531fc4 ["INT_ADD", "register:40f0:8", ["const:531fc4:8", "const:4:8"]]
- 00531fc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532004 ["INT_ADD", "register:40f0:8", ["const:532004:8", "const:4:8"]]
+ 00532004 ["CALL", null, ["callee:00c57f80:8"]]
- 00531fc4 bytes bb971c94
+ 00532004 bytes df971c94
~~~


<a id="compare-39195ef124cf5a959abd53e36dcad001"></a>

### [`00531ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md) → [`00532034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532034.md) FUN_00532034

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md#insn-0053203c) · [`0053204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md#insn-0053204c)
- 新版 `0053207c`（命令位置の公開資料なし） · `0053208c`（命令位置の公開資料なし）

~~~diff
- 0053203c ["INT_ADD", "register:40f0:8", ["const:53203c:8", "const:4:8"]]
- 0053203c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053207c ["INT_ADD", "register:40f0:8", ["const:53207c:8", "const:4:8"]]
+ 0053207c ["CALL", null, ["callee:00c57f80:8"]]
- 0053203c bytes 9d971c94
+ 0053207c bytes c1971c94
- 0053204c ["INT_ADD", "register:40f0:8", ["const:53204c:8", "const:4:8"]]
- 0053204c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053208c ["INT_ADD", "register:40f0:8", ["const:53208c:8", "const:4:8"]]
+ 0053208c ["CALL", null, ["callee:00c57f80:8"]]
- 0053204c bytes 99971c94
+ 0053208c bytes bd971c94
~~~


<a id="compare-83719d856919c5c004bf952f6a8e3b28"></a>

### [`00532234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md) → [`00532274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532274.md) FUN_00532274

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md#insn-00532280) · [`00532290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md#insn-00532290)
- 新版 `005322c0`（命令位置の公開資料なし） · `005322d0`（命令位置の公開資料なし）

~~~diff
- 00532280 ["INT_ADD", "register:40f0:8", ["const:532280:8", "const:4:8"]]
- 00532280 ["CALL", null, ["callee:00c57f80:8"]]
+ 005322c0 ["INT_ADD", "register:40f0:8", ["const:5322c0:8", "const:4:8"]]
+ 005322c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00532280 bytes 0c971c94
+ 005322c0 bytes 30971c94
- 00532290 ["INT_ADD", "register:40f0:8", ["const:532290:8", "const:4:8"]]
- 00532290 ["CALL", null, ["callee:00c57f80:8"]]
+ 005322d0 ["INT_ADD", "register:40f0:8", ["const:5322d0:8", "const:4:8"]]
+ 005322d0 ["CALL", null, ["callee:00c57f80:8"]]
- 00532290 bytes 08971c94
+ 005322d0 bytes 2c971c94
~~~


<a id="compare-b806af1b434ae15a56628cb70e0bd58d"></a>

### [`005322c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md) → [`00532300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532300.md) FUN_00532300

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053230c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053230c) · [`0053231c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053231c) · [`0053232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053232c)
- 新版 `0053234c`（命令位置の公開資料なし） · `0053235c`（命令位置の公開資料なし） · `0053236c`（命令位置の公開資料なし）

~~~diff
- 0053230c ["INT_ADD", "register:40f0:8", ["const:53230c:8", "const:4:8"]]
- 0053230c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053234c ["INT_ADD", "register:40f0:8", ["const:53234c:8", "const:4:8"]]
+ 0053234c ["CALL", null, ["callee:00c57f80:8"]]
- 0053230c bytes e9961c94
+ 0053234c bytes 0d971c94
- 0053231c ["INT_ADD", "register:40f0:8", ["const:53231c:8", "const:4:8"]]
- 0053231c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053235c ["INT_ADD", "register:40f0:8", ["const:53235c:8", "const:4:8"]]
+ 0053235c ["CALL", null, ["callee:00c57f80:8"]]
- 0053231c bytes e5961c94
+ 0053235c bytes 09971c94
- 0053232c ["INT_ADD", "register:40f0:8", ["const:53232c:8", "const:4:8"]]
- 0053232c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053236c ["INT_ADD", "register:40f0:8", ["const:53236c:8", "const:4:8"]]
+ 0053236c ["CALL", null, ["callee:00c57f80:8"]]
- 0053232c bytes e1961c94
+ 0053236c bytes 05971c94
~~~


<a id="compare-32b219e96e35fdb4cae5156f342ad50d"></a>

### [`005326c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md) → [`00532700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532700.md) FUN_00532700

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-0053270c) · [`0053271c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-0053271c) · [`00532744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-00532744)
- 新版 `0053274c`（命令位置の公開資料なし） · `0053275c`（命令位置の公開資料なし） · `00532784`（命令位置の公開資料なし）

~~~diff
- 0053270c ["INT_ADD", "register:40f0:8", ["const:53270c:8", "const:4:8"]]
- 0053270c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053274c ["INT_ADD", "register:40f0:8", ["const:53274c:8", "const:4:8"]]
+ 0053274c ["CALL", null, ["callee:00c57f80:8"]]
- 0053270c bytes e9951c94
+ 0053274c bytes 0d961c94
- 0053271c ["INT_ADD", "register:40f0:8", ["const:53271c:8", "const:4:8"]]
- 0053271c ["CALL", null, ["callee:00c57f80:8"]]
+ 0053275c ["INT_ADD", "register:40f0:8", ["const:53275c:8", "const:4:8"]]
+ 0053275c ["CALL", null, ["callee:00c57f80:8"]]
- 0053271c bytes e5951c94
+ 0053275c bytes 09961c94
- 00532744 ["INT_ADD", "register:40f0:8", ["const:532744:8", "const:4:8"]]
- 00532744 ["CALL", null, ["callee:0053afd0:8"]]
+ 00532784 ["INT_ADD", "register:40f0:8", ["const:532784:8", "const:4:8"]]
+ 00532784 ["CALL", null, ["callee:0053afd0:8"]]
- 00532744 bytes 13220094
+ 00532784 bytes 13220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88a90c49b6222ba46fab3dcf9b29a724"></a>

### [`0053278c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md) → [`005327cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005327cc.md) FUN_005327cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005327d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-005327d8) · [`005327e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-005327e8) · [`00532810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-00532810)
- 新版 `00532818`（命令位置の公開資料なし） · `00532828`（命令位置の公開資料なし） · `00532850`（命令位置の公開資料なし）

~~~diff
- 005327d8 ["INT_ADD", "register:40f0:8", ["const:5327d8:8", "const:4:8"]]
- 005327d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532818 ["INT_ADD", "register:40f0:8", ["const:532818:8", "const:4:8"]]
+ 00532818 ["CALL", null, ["callee:00c57f80:8"]]
- 005327d8 bytes b6951c94
+ 00532818 bytes da951c94
- 005327e8 ["INT_ADD", "register:40f0:8", ["const:5327e8:8", "const:4:8"]]
- 005327e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532828 ["INT_ADD", "register:40f0:8", ["const:532828:8", "const:4:8"]]
+ 00532828 ["CALL", null, ["callee:00c57f80:8"]]
- 005327e8 bytes b2951c94
+ 00532828 bytes d6951c94
- 00532810 ["INT_ADD", "register:40f0:8", ["const:532810:8", "const:4:8"]]
- 00532810 ["CALL", null, ["callee:0053afd0:8"]]
+ 00532850 ["INT_ADD", "register:40f0:8", ["const:532850:8", "const:4:8"]]
+ 00532850 ["CALL", null, ["callee:0053afd0:8"]]
- 00532810 bytes e0210094
+ 00532850 bytes e0210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdad0e2aaca579421ed8b9ee4a2e0f7f"></a>

### [`00532860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532860.md) → [`005328a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328a0.md) FUN_005328a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532860.md#insn-00532878)
- 新版 `005328b8`（命令位置の公開資料なし）

~~~diff
- 00532878 ["INT_ADD", "register:40f0:8", ["const:532878:8", "const:4:8"]]
- 00532878 ["CALL", null, ["callee:0053afd0:8"]]
+ 005328b8 ["INT_ADD", "register:40f0:8", ["const:5328b8:8", "const:4:8"]]
+ 005328b8 ["CALL", null, ["callee:0053afd0:8"]]
- 00532878 bytes c6210094
+ 005328b8 bytes c6210094
~~~


<a id="compare-ff3d521ad31c8b31f63003fb704fd3d2"></a>

### [`00532890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md) → [`005328d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005328d0.md) FUN_005328d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005328a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md#insn-005328a8) · [`005328b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md#insn-005328b4)
- 新版 `005328e8`（命令位置の公開資料なし） · `005328f4`（命令位置の公開資料なし）

~~~diff
- 005328a8 ["INT_ADD", "register:40f0:8", ["const:5328a8:8", "const:4:8"]]
- 005328a8 ["CALL", null, ["callee:0053afd0:8"]]
+ 005328e8 ["INT_ADD", "register:40f0:8", ["const:5328e8:8", "const:4:8"]]
+ 005328e8 ["CALL", null, ["callee:0053afd0:8"]]
- 005328a8 bytes ba210094
+ 005328e8 bytes ba210094
- 005328b4 ["INT_ADD", "register:40f0:8", ["const:5328b4:8", "const:4:8"]]
- 005328b4 ["CALL", null, ["callee:0046d4d0:8"]]
+ 005328f4 ["INT_ADD", "register:40f0:8", ["const:5328f4:8", "const:4:8"]]
+ 005328f4 ["CALL", null, ["callee:0046d4d0:8"]]
- 005328b4 bytes f7eafc97
+ 005328f4 bytes f7eafc97
~~~


<a id="compare-cdad1c6f9333c32537496e70339e9de4"></a>

### [`00532a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a20.md) → [`00532a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a60.md) FUN_00532a60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a20.md#insn-00532a38)
- 新版 `00532a78`（命令位置の公開資料なし）

~~~diff
- 00532a38 ["INT_ADD", "register:40f0:8", ["const:532a38:8", "const:4:8"]]
- 00532a38 ["CALL", null, ["callee:0053afd0:8"]]
+ 00532a78 ["INT_ADD", "register:40f0:8", ["const:532a78:8", "const:4:8"]]
+ 00532a78 ["CALL", null, ["callee:0053afd0:8"]]
- 00532a38 bytes 56210094
+ 00532a78 bytes 56210094
~~~


<a id="compare-874b4e528aae58b83f6b3507e0fd19ad"></a>

### [`00532a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md) → [`00532a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a90.md) FUN_00532a90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md#insn-00532a68) · [`00532a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md#insn-00532a74)
- 新版 `00532aa8`（命令位置の公開資料なし） · `00532ab4`（命令位置の公開資料なし）

~~~diff
- 00532a68 ["INT_ADD", "register:40f0:8", ["const:532a68:8", "const:4:8"]]
- 00532a68 ["CALL", null, ["callee:0053afd0:8"]]
+ 00532aa8 ["INT_ADD", "register:40f0:8", ["const:532aa8:8", "const:4:8"]]
+ 00532aa8 ["CALL", null, ["callee:0053afd0:8"]]
- 00532a68 bytes 4a210094
+ 00532aa8 bytes 4a210094
- 00532a74 ["INT_ADD", "register:40f0:8", ["const:532a74:8", "const:4:8"]]
- 00532a74 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00532ab4 ["INT_ADD", "register:40f0:8", ["const:532ab4:8", "const:4:8"]]
+ 00532ab4 ["CALL", null, ["callee:0046d4d0:8"]]
- 00532a74 bytes 87eafc97
+ 00532ab4 bytes 87eafc97
~~~


<a id="compare-bbdce497c068e11fe473b11394489357"></a>

### [`00532c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md) → [`00532c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532c4c.md) FUN_00532c4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532c94) · [`00532ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532ccc) · [`00532cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532cf0)
- 新版 `00532cd4`（命令位置の公開資料なし） · `00532d0c`（命令位置の公開資料なし） · `00532d30`（命令位置の公開資料なし）

~~~diff
- 00532c94 ["INT_ADD", "register:40f0:8", ["const:532c94:8", "const:4:8"]]
- 00532c94 ["CALL", null, ["callee:00c57f60:8"]]
+ 00532cd4 ["INT_ADD", "register:40f0:8", ["const:532cd4:8", "const:4:8"]]
+ 00532cd4 ["CALL", null, ["callee:00c57f60:8"]]
- 00532c94 bytes 7f941c94
+ 00532cd4 bytes a3941c94
- 00532ccc ["INT_ADD", "register:40f0:8", ["const:532ccc:8", "const:4:8"]]
- 00532ccc ["CALL", null, ["callee:0043bbe4:8"]]
+ 00532d0c ["INT_ADD", "register:40f0:8", ["const:532d0c:8", "const:4:8"]]
+ 00532d0c ["CALL", null, ["callee:0043bbe4:8"]]
- 00532ccc bytes b623fc97
+ 00532d0c bytes b623fc97
- 00532cf0 ["INT_ADD", "register:40f0:8", ["const:532cf0:8", "const:4:8"]]
- 00532cf0 ["CALL", null, ["callee:005408fc:8"]]
+ 00532d30 ["INT_ADD", "register:40f0:8", ["const:532d30:8", "const:4:8"]]
+ 00532d30 ["CALL", null, ["callee:005408fc:8"]]
- 00532cf0 bytes f3360094
+ 00532d30 bytes f3360094
~~~


<a id="compare-ed5667b3cfaf5198a17f45a99e127261"></a>

### [`00532cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532cf4.md) → [`00532d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d34.md) FUN_00532d34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532cf4.md#insn-00532d10)
- 新版 `00532d50`（命令位置の公開資料なし）

~~~diff
- 00532d10 ["INT_ADD", "register:40f0:8", ["const:532d10:8", "const:4:8"]]
- 00532d10 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532d50 ["INT_ADD", "register:40f0:8", ["const:532d50:8", "const:4:8"]]
+ 00532d50 ["CALL", null, ["callee:00c57f80:8"]]
- 00532d10 bytes 68941c94
+ 00532d50 bytes 8c941c94
~~~


<a id="compare-c388bfe5487200d2f5031348cf585270"></a>

### [`00532d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md) → [`00532d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532d78.md) FUN_00532d78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md#insn-00532d54) · [`00532d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md#insn-00532d64)
- 新版 `00532d94`（命令位置の公開資料なし） · `00532da4`（命令位置の公開資料なし）

~~~diff
- 00532d54 ["INT_ADD", "register:40f0:8", ["const:532d54:8", "const:4:8"]]
- 00532d54 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532d94 ["INT_ADD", "register:40f0:8", ["const:532d94:8", "const:4:8"]]
+ 00532d94 ["CALL", null, ["callee:00c57f80:8"]]
- 00532d54 bytes 57941c94
+ 00532d94 bytes 7b941c94
- 00532d64 ["INT_ADD", "register:40f0:8", ["const:532d64:8", "const:4:8"]]
- 00532d64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00532da4 ["INT_ADD", "register:40f0:8", ["const:532da4:8", "const:4:8"]]
+ 00532da4 ["CALL", null, ["callee:00c57f80:8"]]
- 00532d64 bytes 53941c94
+ 00532da4 bytes 77941c94
~~~


<a id="compare-40e5742ba626102d42c9a61def07091c"></a>

### [`00532f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md) → [`00532f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532f8c.md) FUN_00532f8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md#insn-00532f5c)
- 新版 `00532f9c`（命令位置の公開資料なし）

~~~diff
- 00532f5c ["INT_ADD", "register:40f0:8", ["const:532f5c:8", "const:4:8"]]
- 00532f5c ["CALL", null, ["callee:00532ebc:8"]]
+ 00532f9c ["INT_ADD", "register:40f0:8", ["const:532f9c:8", "const:4:8"]]
+ 00532f9c ["CALL", null, ["callee:00532ebc:8"]]
- 00532f5c bytes c8ffff97
+ 00532f9c bytes c8ffff97
~~~


<a id="compare-2c179226e7861145876560db0dc7f200"></a>

### [`00532f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md) → [`00532fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532fb0.md) FUN_00532fb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053ffa0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053ffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md#insn-00532f84) · [`00532f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md#insn-00532f90)
- 新版 `00532fc4`（命令位置の公開資料なし） · `00532fd0`（命令位置の公開資料なし）

~~~diff
- 00532f84 ["INT_ADD", "register:40f0:8", ["const:532f84:8", "const:4:8"]]
- 00532f84 ["CALL", null, ["callee:00c57f60:8"]]
+ 00532fc4 ["INT_ADD", "register:40f0:8", ["const:532fc4:8", "const:4:8"]]
+ 00532fc4 ["CALL", null, ["callee:00c57f60:8"]]
- 00532f84 bytes c3931c94
+ 00532fc4 bytes e7931c94
- 00532f90 ["INT_ADD", "register:40f0:8", ["const:532f90:8", "const:4:8"]]
- 00532f90 ["CALL", null, ["callee:0053ffe0:8"]]
+ 00532fd0 ["INT_ADD", "register:40f0:8", ["const:532fd0:8", "const:4:8"]]
+ 00532fd0 ["CALL", null, ["callee:0053ffe0:8"]]
- 00532f90 bytes 04340094
+ 00532fd0 bytes 04340094
~~~


<a id="compare-4161827f231cb187a90b05fb962cb90d"></a>

### [`0053312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md) → [`0053316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/0053316c.md) FUN_0053316c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053313c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md#insn-0053313c)
- 新版 `0053317c`（命令位置の公開資料なし）

~~~diff
- 0053313c ["INT_ADD", "register:40f0:8", ["const:53313c:8", "const:4:8"]]
- 0053313c ["CALL", null, ["callee:00532ff8:8"]]
+ 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
+ 0053317c ["CALL", null, ["callee:00532ff8:8"]]
- 0053313c bytes 9fffff97
+ 0053317c bytes 9fffff97
~~~


<a id="compare-bd3db3dbfb1a7cbe620ec50c2dd42af0"></a>

### [`00533150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md) → [`00533190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533190.md) FUN_00533190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md#insn-0053316c) · [`0053317c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md#insn-0053317c)
- 新版 `005331ac`（命令位置の公開資料なし） · `005331bc`（命令位置の公開資料なし）

~~~diff
- 0053316c ["INT_ADD", "register:40f0:8", ["const:53316c:8", "const:4:8"]]
- 0053316c ["CALL", null, ["callee:00c57f80:8"]]
+ 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
+ 005331ac ["CALL", null, ["callee:00c57f80:8"]]
- 0053316c bytes 51931c94
+ 005331ac bytes 75931c94
- 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
- 0053317c ["CALL", null, ["callee:00c57f80:8"]]
+ 005331bc ["INT_ADD", "register:40f0:8", ["const:5331bc:8", "const:4:8"]]
+ 005331bc ["CALL", null, ["callee:00c57f80:8"]]
- 0053317c bytes 4d931c94
+ 005331bc bytes 71931c94
~~~


<a id="compare-ee26e92d2d1c052b417d15e8f1976373"></a>

### [`00533190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md) → [`005331d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005331d0.md) FUN_005331d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005331ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md#insn-005331ac) · [`005331bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md#insn-005331bc)
- 新版 `005331ec`（命令位置の公開資料なし） · `005331fc`（命令位置の公開資料なし）

~~~diff
- 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
- 005331ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005331ec ["INT_ADD", "register:40f0:8", ["const:5331ec:8", "const:4:8"]]
+ 005331ec ["CALL", null, ["callee:00c57f80:8"]]
- 005331ac bytes 41931c94
+ 005331ec bytes 65931c94
- 005331bc ["INT_ADD", "register:40f0:8", ["const:5331bc:8", "const:4:8"]]
- 005331bc ["CALL", null, ["callee:00c57f80:8"]]
+ 005331fc ["INT_ADD", "register:40f0:8", ["const:5331fc:8", "const:4:8"]]
+ 005331fc ["CALL", null, ["callee:00c57f80:8"]]
- 005331bc bytes 3d931c94
+ 005331fc bytes 61931c94
~~~


