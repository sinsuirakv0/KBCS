# v16.0.0 → v16.0.1 · 要調査の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-075ad02629f364c2ff8072ad3764e3fc"></a>

### [`005227e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md) → [`00522828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522828.md) FUN_00522828

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054d4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d4a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md#insn-00522804)
- 新版 [`00522844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522828.md#insn-00522844)

~~~diff
- 00522804 ["INT_ADD", "register:40f0:8", ["const:522804:8", "const:4:8"]]
- 00522804 ["CALL", null, ["callee:0054d4a4:8"]]
+ 00522844 ["INT_ADD", "register:40f0:8", ["const:522844:8", "const:4:8"]]
+ 00522844 ["CALL", null, ["callee:0054d4a4:8"]]
- 00522804 bytes 18ab0094
+ 00522844 bytes 18ab0094
~~~


<a id="compare-d158e2c259859e6aaecd304ea451d4e1"></a>

### [`00522920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522920.md) → [`00522960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522960.md) _ZNK5Botan16X509_Certificate12x509_versionEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522920.md#insn-00522928)
- 新版 [`00522968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522960.md#insn-00522968)

~~~diff
- 00522928 ["INT_ADD", "register:40f0:8", ["const:522928:8", "const:4:8"]]
- 00522928 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522968 ["INT_ADD", "register:40f0:8", ["const:522968:8", "const:4:8"]]
+ 00522968 ["CALL", null, ["callee:00c599f0:8"]]
- 00522928 bytes 32db1c94
+ 00522968 bytes 22dc1c94
~~~


<a id="compare-5e0e1bbfafa439bd29ff0028e5d9e09b"></a>

### [`00522938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522938.md) → [`00522978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522978.md) _ZNK5Botan16X509_Certificate14is_self_signedEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522938.md#insn-00522940)
- 新版 [`00522980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522978.md#insn-00522980)

~~~diff
- 00522940 ["INT_ADD", "register:40f0:8", ["const:522940:8", "const:4:8"]]
- 00522940 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522980 ["INT_ADD", "register:40f0:8", ["const:522980:8", "const:4:8"]]
+ 00522980 ["CALL", null, ["callee:00c599f0:8"]]
- 00522940 bytes 2cdb1c94
+ 00522980 bytes 1cdc1c94
~~~


<a id="compare-76c5a58ffe2295851dcf74fcdf285c3f"></a>

### [`00522950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522950.md) → [`00522990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522990.md) _ZNK5Botan16X509_Certificate10not_beforeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522950.md#insn-00522958)
- 新版 [`00522998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522990.md#insn-00522998)

~~~diff
- 00522958 ["INT_ADD", "register:40f0:8", ["const:522958:8", "const:4:8"]]
- 00522958 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522998 ["INT_ADD", "register:40f0:8", ["const:522998:8", "const:4:8"]]
+ 00522998 ["CALL", null, ["callee:00c599f0:8"]]
- 00522958 bytes 26db1c94
+ 00522998 bytes 16dc1c94
~~~


<a id="compare-f5b75afbbcb80b343dc4757ce8ee206c"></a>

### [`00522968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522968.md) → [`005229a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229a8.md) _ZNK5Botan16X509_Certificate9not_afterEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522968.md#insn-00522970)
- 新版 [`005229b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229a8.md#insn-005229b0)

~~~diff
- 00522970 ["INT_ADD", "register:40f0:8", ["const:522970:8", "const:4:8"]]
- 00522970 ["CALL", null, ["callee:00c599f0:8"]]
+ 005229b0 ["INT_ADD", "register:40f0:8", ["const:5229b0:8", "const:4:8"]]
+ 005229b0 ["CALL", null, ["callee:00c599f0:8"]]
- 00522970 bytes 20db1c94
+ 005229b0 bytes 10dc1c94
~~~


<a id="compare-3471fff1467f3418e4bc0f2e49f63b64"></a>

### [`00522980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522980.md) → [`005229c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229c0.md) _ZNK5Botan16X509_Certificate23subject_public_key_algoEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522980.md#insn-00522988)
- 新版 [`005229c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229c0.md#insn-005229c8)

~~~diff
- 00522988 ["INT_ADD", "register:40f0:8", ["const:522988:8", "const:4:8"]]
- 00522988 ["CALL", null, ["callee:00c599f0:8"]]
+ 005229c8 ["INT_ADD", "register:40f0:8", ["const:5229c8:8", "const:4:8"]]
+ 005229c8 ["CALL", null, ["callee:00c599f0:8"]]
- 00522988 bytes 1adb1c94
+ 005229c8 bytes 0adc1c94
~~~


<a id="compare-d2064f086e3ba7ab4959628bdfb42454"></a>

### [`00522998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522998.md) → [`005229d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229d8.md) _ZNK5Botan16X509_Certificate16v2_issuer_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522998.md#insn-005229a0)
- 新版 [`005229e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229d8.md#insn-005229e0)

~~~diff
- 005229a0 ["INT_ADD", "register:40f0:8", ["const:5229a0:8", "const:4:8"]]
- 005229a0 ["CALL", null, ["callee:00c599f0:8"]]
+ 005229e0 ["INT_ADD", "register:40f0:8", ["const:5229e0:8", "const:4:8"]]
+ 005229e0 ["CALL", null, ["callee:00c599f0:8"]]
- 005229a0 bytes 14db1c94
+ 005229e0 bytes 04dc1c94
~~~


<a id="compare-2454b97e910f0594cb1a1db919c8f9d0"></a>

### [`005229b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229b0.md) → [`005229f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229f0.md) _ZNK5Botan16X509_Certificate17v2_subject_key_idEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229b0.md#insn-005229b8)
- 新版 [`005229f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/005229f0.md#insn-005229f8)

~~~diff
- 005229b8 ["INT_ADD", "register:40f0:8", ["const:5229b8:8", "const:4:8"]]
- 005229b8 ["CALL", null, ["callee:00c599f0:8"]]
+ 005229f8 ["INT_ADD", "register:40f0:8", ["const:5229f8:8", "const:4:8"]]
+ 005229f8 ["CALL", null, ["callee:00c599f0:8"]]
- 005229b8 bytes 0edb1c94
+ 005229f8 bytes fedb1c94
~~~


<a id="compare-d0ab73d1323a312f6ff49f226ff41fd6"></a>

### [`005229c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229c8.md) → [`00522a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a08.md) _ZNK5Botan16X509_Certificate23subject_public_key_bitsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229c8.md#insn-005229d0)
- 新版 [`00522a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a08.md#insn-00522a10)

~~~diff
- 005229d0 ["INT_ADD", "register:40f0:8", ["const:5229d0:8", "const:4:8"]]
- 005229d0 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a10 ["INT_ADD", "register:40f0:8", ["const:522a10:8", "const:4:8"]]
+ 00522a10 ["CALL", null, ["callee:00c599f0:8"]]
- 005229d0 bytes 08db1c94
+ 00522a10 bytes f8db1c94
~~~


<a id="compare-b5f1f468f63b7a68783cb15fd0e2599e"></a>

### [`005229e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229e0.md) → [`00522a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a20.md) _ZNK5Botan16X509_Certificate18is_serial_negativeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005229e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229e0.md#insn-005229e8)
- 新版 [`00522a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a20.md#insn-00522a28)

~~~diff
- 005229e8 ["INT_ADD", "register:40f0:8", ["const:5229e8:8", "const:4:8"]]
- 005229e8 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a28 ["INT_ADD", "register:40f0:8", ["const:522a28:8", "const:4:8"]]
+ 00522a28 ["CALL", null, ["callee:00c599f0:8"]]
- 005229e8 bytes 02db1c94
+ 00522a28 bytes f2db1c94
~~~


<a id="compare-25b9186f1e09019074a6b9495081167c"></a>

### [`005229f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229f8.md) → [`00522a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a38.md) _ZNK5Botan16X509_Certificate10path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005229f8.md#insn-00522a00)
- 新版 [`00522a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a38.md#insn-00522a40)

~~~diff
- 00522a00 ["INT_ADD", "register:40f0:8", ["const:522a00:8", "const:4:8"]]
- 00522a00 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a40 ["INT_ADD", "register:40f0:8", ["const:522a40:8", "const:4:8"]]
+ 00522a40 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a00 bytes fcda1c94
+ 00522a40 bytes ecdb1c94
~~~


<a id="compare-378b1de119fa5bd54154572ff5767452"></a>

### [`00522a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a10.md) → [`00522a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a50.md) _ZNK5Botan16X509_Certificate11constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a10.md#insn-00522a18)
- 新版 [`00522a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a50.md#insn-00522a58)

~~~diff
- 00522a18 ["INT_ADD", "register:40f0:8", ["const:522a18:8", "const:4:8"]]
- 00522a18 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a58 ["INT_ADD", "register:40f0:8", ["const:522a58:8", "const:4:8"]]
+ 00522a58 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a18 bytes f6da1c94
+ 00522a58 bytes e6db1c94
~~~


<a id="compare-7626c7c0e40e94bc23d70fbaf2f6242b"></a>

### [`00522a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a28.md) → [`00522a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a68.md) _ZNK5Botan16X509_Certificate18extended_key_usageEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a28.md#insn-00522a30)
- 新版 [`00522a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a68.md#insn-00522a70)

~~~diff
- 00522a30 ["INT_ADD", "register:40f0:8", ["const:522a30:8", "const:4:8"]]
- 00522a30 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a70 ["INT_ADD", "register:40f0:8", ["const:522a70:8", "const:4:8"]]
+ 00522a70 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a30 bytes f0da1c94
+ 00522a70 bytes e0db1c94
~~~


<a id="compare-c84ce9bc1e71cc39ed1aab84ce1a8e1a"></a>

### [`00522a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a40.md) → [`00522a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a80.md) _ZNK5Botan16X509_Certificate23certificate_policy_oidsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a40.md#insn-00522a48)
- 新版 [`00522a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a80.md#insn-00522a88)

~~~diff
- 00522a48 ["INT_ADD", "register:40f0:8", ["const:522a48:8", "const:4:8"]]
- 00522a48 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522a88 ["INT_ADD", "register:40f0:8", ["const:522a88:8", "const:4:8"]]
+ 00522a88 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a48 bytes eada1c94
+ 00522a88 bytes dadb1c94
~~~


<a id="compare-0fdbb1913ad9f6cc5ce69714590456c2"></a>

### [`00522a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a58.md) → [`00522a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a98.md) _ZNK5Botan16X509_Certificate16name_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a58.md#insn-00522a60)
- 新版 [`00522aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522a98.md#insn-00522aa0)

~~~diff
- 00522a60 ["INT_ADD", "register:40f0:8", ["const:522a60:8", "const:4:8"]]
- 00522a60 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522aa0 ["INT_ADD", "register:40f0:8", ["const:522aa0:8", "const:4:8"]]
+ 00522aa0 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a60 bytes e4da1c94
+ 00522aa0 bytes d4db1c94
~~~


<a id="compare-0dd6ee8c9442013eacd8b1518ed8f906"></a>

### [`00522a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a70.md) → [`00522ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ab0.md) _ZNK5Botan16X509_Certificate13v3_extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a70.md#insn-00522a78)
- 新版 [`00522ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ab0.md#insn-00522ab8)

~~~diff
- 00522a78 ["INT_ADD", "register:40f0:8", ["const:522a78:8", "const:4:8"]]
- 00522a78 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522ab8 ["INT_ADD", "register:40f0:8", ["const:522ab8:8", "const:4:8"]]
+ 00522ab8 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a78 bytes deda1c94
+ 00522ab8 bytes cedb1c94
~~~


<a id="compare-aceed59e7c0cf2da3c202f9fe70c658d"></a>

### [`00522a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a88.md) → [`00522ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ac8.md) _ZNK5Botan16X509_Certificate22allowed_extended_usageERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522a88.md#insn-00522a98)
- 新版 [`00522ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ac8.md#insn-00522ad8)

~~~diff
- 00522a98 ["INT_ADD", "register:40f0:8", ["const:522a98:8", "const:4:8"]]
- 00522a98 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522ad8 ["INT_ADD", "register:40f0:8", ["const:522ad8:8", "const:4:8"]]
+ 00522ad8 ["CALL", null, ["callee:00c599f0:8"]]
- 00522a98 bytes d6da1c94
+ 00522ad8 bytes c6db1c94
~~~


<a id="compare-47d3e080db19702436154ad67e043bd5"></a>

### [`00522d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522d6c.md) → [`00522dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md) _ZNK5Botan16X509_Certificate15has_constraintsENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522d6c.md#insn-00522d80) · [`00522d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522d6c.md#insn-00522d90)
- 新版 [`00522dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md#insn-00522dc0) · [`00522dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522dac.md#insn-00522dd0)

~~~diff
- 00522d80 ["INT_ADD", "register:40f0:8", ["const:522d80:8", "const:4:8"]]
- 00522d80 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522dc0 ["INT_ADD", "register:40f0:8", ["const:522dc0:8", "const:4:8"]]
+ 00522dc0 ["CALL", null, ["callee:00c599f0:8"]]
- 00522d80 bytes 1cda1c94
+ 00522dc0 bytes 0cdb1c94
- 00522d90 ["INT_ADD", "register:40f0:8", ["const:522d90:8", "const:4:8"]]
- 00522d90 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522dd0 ["INT_ADD", "register:40f0:8", ["const:522dd0:8", "const:4:8"]]
+ 00522dd0 ["CALL", null, ["callee:00c599f0:8"]]
- 00522d90 bytes 18da1c94
+ 00522dd0 bytes 08db1c94
~~~


<a id="compare-35120d8eedff4d061fe2a8819fae5697"></a>

### [`00522db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522db4.md) → [`00522df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522db4.md#insn-00522de0) · [`00522de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522db4.md#insn-00522de8) · [`00522e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522db4.md#insn-00522e64)
- 新版 [`00522e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522e20) · [`00522e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522e28) · [`00522ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522df4.md#insn-00522ea4)

~~~diff
- 00522de0 ["INT_ADD", "register:40f0:8", ["const:522de0:8", "const:4:8"]]
- 00522de0 ["CALL", null, ["callee:00c58680:8"]]
+ 00522e20 ["INT_ADD", "register:40f0:8", ["const:522e20:8", "const:4:8"]]
+ 00522e20 ["CALL", null, ["callee:00c58680:8"]]
- 00522de0 bytes 28d51c94
+ 00522e20 bytes 18d61c94
- 00522de8 ["INT_ADD", "register:40f0:8", ["const:522de8:8", "const:4:8"]]
- 00522de8 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522e28 ["INT_ADD", "register:40f0:8", ["const:522e28:8", "const:4:8"]]
+ 00522e28 ["CALL", null, ["callee:00c599f0:8"]]
- 00522de8 bytes 02da1c94
+ 00522e28 bytes f2da1c94
- 00522e64 ["INT_ADD", "register:40f0:8", ["const:522e64:8", "const:4:8"]]
- 00522e64 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00522ea4 ["INT_ADD", "register:40f0:8", ["const:522ea4:8", "const:4:8"]]
+ 00522ea4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00522e64 bytes 13d31c94
+ 00522ea4 bytes 03d41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11fa74c32f778a9abd49ad435aa81529"></a>

### [`00522ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522ed4.md) → [`00522f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522f14.md) _ZNK5Botan16X509_Certificate17has_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522ed4.md#insn-00522ee4)
- 新版 [`00522f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522f14.md#insn-00522f24)

~~~diff
- 00522ee4 ["INT_ADD", "register:40f0:8", ["const:522ee4:8", "const:4:8"]]
- 00522ee4 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522f24 ["INT_ADD", "register:40f0:8", ["const:522f24:8", "const:4:8"]]
+ 00522f24 ["CALL", null, ["callee:00c599f0:8"]]
- 00522ee4 bytes c3d91c94
+ 00522f24 bytes b3da1c94
~~~


<a id="compare-42aec4ddce763d9ee214a9a534e28764"></a>

### [`00522f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522f64.md) → [`00522fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522fa4.md) _ZNK5Botan16X509_Certificate14ocsp_responderEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522f64.md#insn-00522f74)
- 新版 [`00522fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522fa4.md#insn-00522fb4)

~~~diff
- 00522f74 ["INT_ADD", "register:40f0:8", ["const:522f74:8", "const:4:8"]]
- 00522f74 ["CALL", null, ["callee:00c599f0:8"]]
+ 00522fb4 ["INT_ADD", "register:40f0:8", ["const:522fb4:8", "const:4:8"]]
+ 00522fb4 ["CALL", null, ["callee:00c599f0:8"]]
- 00522f74 bytes 9fd91c94
+ 00522fb4 bytes 8fda1c94
~~~


<a id="compare-4f4c51648d525935f1466f8a2319521d"></a>

### [`00522fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522fb8.md) → [`00522ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ff8.md) _ZNK5Botan16X509_Certificate10ca_issuersEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00522fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/00522fb8.md#insn-00522fc8)
- 新版 [`00523008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522ff8.md#insn-00523008)

~~~diff
- 00522fc8 ["INT_ADD", "register:40f0:8", ["const:522fc8:8", "const:4:8"]]
- 00522fc8 ["CALL", null, ["callee:00c599f0:8"]]
+ 00523008 ["INT_ADD", "register:40f0:8", ["const:523008:8", "const:4:8"]]
+ 00523008 ["CALL", null, ["callee:00c599f0:8"]]
- 00522fc8 bytes 8ad91c94
+ 00523008 bytes 7ada1c94
~~~


<a id="compare-4465dbd169966f1d7d340672d9ddeb73"></a>

### [`00523000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523000.md) → [`00523040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md) _ZNK5Botan16X509_Certificate22crl_distribution_pointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523000.md#insn-00523014) · [`0052302c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523000.md#insn-0052302c)
- 新版 [`00523054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md#insn-00523054) · [`0052306c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523040.md#insn-0052306c)

~~~diff
- 00523014 ["INT_ADD", "register:40f0:8", ["const:523014:8", "const:4:8"]]
- 00523014 ["CALL", null, ["callee:00c599f0:8"]]
+ 00523054 ["INT_ADD", "register:40f0:8", ["const:523054:8", "const:4:8"]]
+ 00523054 ["CALL", null, ["callee:00c599f0:8"]]
- 00523014 bytes 77d91c94
+ 00523054 bytes 67da1c94
- 0052302c ["INT_ADD", "register:40f0:8", ["const:52302c:8", "const:4:8"]]
- 0052302c ["CALL", null, ["callee:00c599f0:8"]]
+ 0052306c ["INT_ADD", "register:40f0:8", ["const:52306c:8", "const:4:8"]]
+ 0052306c ["CALL", null, ["callee:00c599f0:8"]]
- 0052302c bytes 71d91c94
+ 0052306c bytes 61da1c94
~~~


<a id="compare-00a4f696b9c99c35849e8362b2e64201"></a>

### [`00523074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523074.md) → [`005230b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230b4.md) _ZNK5Botan16X509_Certificate15issuer_alt_nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052307c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523074.md#insn-0052307c)
- 新版 [`005230bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230b4.md#insn-005230bc)

~~~diff
- 0052307c ["INT_ADD", "register:40f0:8", ["const:52307c:8", "const:4:8"]]
- 0052307c ["CALL", null, ["callee:00c599f0:8"]]
+ 005230bc ["INT_ADD", "register:40f0:8", ["const:5230bc:8", "const:4:8"]]
+ 005230bc ["CALL", null, ["callee:00c599f0:8"]]
- 0052307c bytes 5dd91c94
+ 005230bc bytes 4dda1c94
~~~


<a id="compare-9a911333f4187e5adcb5fdea1bdeecab"></a>

### [`00523da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md) → [`00523de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md) _ZNK5Botan16X509_Certificate23load_subject_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59810.md) · 呼出先 5件 [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c592f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592f0.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 1件 [`00c59c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c10.md) · 呼出先 5件 [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c596f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596f0.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md#insn-00523dcc) · [`00523dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md#insn-00523dd8) · [`00523de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523da8.md#insn-00523de0)
- 新版 [`00523e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e0c) · [`00523e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e18) · [`00523e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523de8.md#insn-00523e20)

~~~diff
- 00523dcc ["INT_ADD", "register:40f0:8", ["const:523dcc:8", "const:4:8"]]
- 00523dcc ["CALL", null, ["callee:00c599f0:8"]]
+ 00523e0c ["INT_ADD", "register:40f0:8", ["const:523e0c:8", "const:4:8"]]
+ 00523e0c ["CALL", null, ["callee:00c599f0:8"]]
- 00523dcc bytes 09d61c94
+ 00523e0c bytes f9d61c94
- 00523dd8 ["INT_ADD", "register:40f0:8", ["const:523dd8:8", "const:4:8"]]
- 00523dd8 ["CALL", null, ["callee:004a6c1c:8"]]
+ 00523e18 ["INT_ADD", "register:40f0:8", ["const:523e18:8", "const:4:8"]]
+ 00523e18 ["CALL", null, ["callee:004a6c1c:8"]]
- 00523dd8 bytes 810bfe97
+ 00523e18 bytes 810bfe97
- 00523de0 ["INT_ADD", "register:40f0:8", ["const:523de0:8", "const:4:8"]]
- 00523de0 ["CALL", null, ["callee:00c596f0:8"]]
+ 00523e20 ["INT_ADD", "register:40f0:8", ["const:523e20:8", "const:4:8"]]
+ 00523e20 ["CALL", null, ["callee:00c596f0:8"]]
- 00523de0 bytes 44d51c94
+ 00523e20 bytes 34d61c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f538c65f89289498fbc4342b505165de"></a>

### [`00523f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523f1c.md) → [`00523f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md) _ZNK5Botan16X509_Certificate20raw_issuer_dn_sha256Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00523f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523f1c.md#insn-00523f7c) · [`00523f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523f1c.md#insn-00523f8c) · [`00523f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00523/00523f1c.md#insn-00523f9c)
- 新版 [`00523fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fbc) · [`00523fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fcc) · [`00523fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/00523f5c.md#insn-00523fdc)

~~~diff
- 00523f7c ["INT_ADD", "register:40f0:8", ["const:523f7c:8", "const:4:8"]]
- 00523f7c ["CALL", null, ["callee:00c58e70:8"]]
+ 00523fbc ["INT_ADD", "register:40f0:8", ["const:523fbc:8", "const:4:8"]]
+ 00523fbc ["CALL", null, ["callee:00c58e70:8"]]
- 00523f7c bytes bdd21c94
+ 00523fbc bytes add31c94
- 00523f8c ["INT_ADD", "register:40f0:8", ["const:523f8c:8", "const:4:8"]]
- 00523f8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00523fcc ["INT_ADD", "register:40f0:8", ["const:523fcc:8", "const:4:8"]]
+ 00523fcc ["CALL", null, ["callee:00c57eb0:8"]]
- 00523f8c bytes c9ce1c94
+ 00523fcc bytes b9cf1c94
- 00523f9c ["INT_ADD", "register:40f0:8", ["const:523f9c:8", "const:4:8"]]
- 00523f9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00523fdc ["INT_ADD", "register:40f0:8", ["const:523fdc:8", "const:4:8"]]
+ 00523fdc ["CALL", null, ["callee:00c57eb0:8"]]
- 00523f9c bytes c5ce1c94
+ 00523fdc bytes b5cf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366011df233eeeb1fa1cd81922cf979a"></a>

### [`0052410c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/0052410c.md) → [`0052414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md) _ZNK5Botan16X509_Certificate21raw_subject_dn_sha256Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/0052410c.md#insn-0052416c) · [`00524178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/0052410c.md#insn-00524178) · [`00524190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/0052410c.md#insn-00524190)
- 新版 [`005241ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241ac) · [`005241b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241b8) · [`005241d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052414c.md#insn-005241d0)

~~~diff
- 0052416c ["INT_ADD", "register:40f0:8", ["const:52416c:8", "const:4:8"]]
- 0052416c ["CALL", null, ["callee:00c58df0:8"]]
+ 005241ac ["INT_ADD", "register:40f0:8", ["const:5241ac:8", "const:4:8"]]
+ 005241ac ["CALL", null, ["callee:00c58df0:8"]]
- 0052416c bytes 21d21c94
+ 005241ac bytes 11d31c94
- 00524178 ["INT_ADD", "register:40f0:8", ["const:524178:8", "const:4:8"]]
- 00524178 ["CALL", null, ["callee:00c599f0:8"]]
+ 005241b8 ["INT_ADD", "register:40f0:8", ["const:5241b8:8", "const:4:8"]]
+ 005241b8 ["CALL", null, ["callee:00c599f0:8"]]
- 00524178 bytes 1ed51c94
+ 005241b8 bytes 0ed61c94
- 00524190 ["COPY", "register:0:8", ["register:4040:8"]]
- 00524190 ["INT_ADD", "register:40f0:8", ["const:524190:8", "const:4:8"]]
- 00524190 ["CALLIND", null, ["register:0:8"]]
+ 005241d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005241d0 ["INT_ADD", "register:40f0:8", ["const:5241d0:8", "const:4:8"]]
+ 005241d0 ["CALLIND", null, ["register:0:8"]]
- 00524190 bytes 00013fd6
+ 005241d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e683cd764f95817d7989c6f0e94a8b28"></a>

### [`005242a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242a4.md) → [`005242e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md) _ZNK5Botan16X509_Certificate14ex_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005242b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242a4.md#insn-005242b4)
- 新版 [`005242f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md#insn-005242f4)

~~~diff
- 005242b4 ["INT_ADD", "register:40f0:8", ["const:5242b4:8", "const:4:8"]]
- 005242b4 ["CALL", null, ["callee:00c599f0:8"]]
+ 005242f4 ["INT_ADD", "register:40f0:8", ["const:5242f4:8", "const:4:8"]]
+ 005242f4 ["CALL", null, ["callee:00c599f0:8"]]
- 005242b4 bytes cfd41c94
+ 005242f4 bytes bfd51c94
~~~


<a id="compare-2a2bb725dca00c3ffe4d58320f5ba492"></a>

### [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) → [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) FUN_0052430c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005242a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242a4.md) [`005244fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005244fc.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`005242e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005242e4.md) [`0052453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md#insn-00524358) · [`005243c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md#insn-005243c0) · [`00524404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md#insn-00524404)
- 新版 [`00524398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524398) · [`00524400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524400) · [`00524444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md#insn-00524444)

~~~diff
- 00524358 ["INT_ADD", "register:40f0:8", ["const:524358:8", "const:4:8"]]
- 00524358 ["CALL", null, ["callee:00c588b0:8"]]
+ 00524398 ["INT_ADD", "register:40f0:8", ["const:524398:8", "const:4:8"]]
+ 00524398 ["CALL", null, ["callee:00c588b0:8"]]
- 00524358 bytes 56d01c94
+ 00524398 bytes 46d11c94
- 005243c0 ["INT_ADD", "register:40f0:8", ["const:5243c0:8", "const:4:8"]]
- 005243c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00524400 ["INT_ADD", "register:40f0:8", ["const:524400:8", "const:4:8"]]
+ 00524400 ["CALL", null, ["callee:00c57e90:8"]]
- 005243c0 bytes b4cd1c94
+ 00524400 bytes a4ce1c94
- 00524404 ["INT_ADD", "register:40f0:8", ["const:524404:8", "const:4:8"]]
- 00524404 ["CALL", null, ["callee:00c58000:8"]]
+ 00524444 ["INT_ADD", "register:40f0:8", ["const:524444:8", "const:4:8"]]
+ 00524444 ["CALL", null, ["callee:00c58000:8"]]
- 00524404 bytes ffcd1c94
+ 00524444 bytes efce1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4aa20e7bb246197d83805ee2901350"></a>

### [`005244fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005244fc.md) → [`0052453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md) _ZNK5Botan16X509_Certificate8policiesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005242cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005242cc.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052430c.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052450c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005244fc.md#insn-0052450c)
- 新版 [`0052454c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/0052453c.md#insn-0052454c)

~~~diff
- 0052450c ["INT_ADD", "register:40f0:8", ["const:52450c:8", "const:4:8"]]
- 0052450c ["CALL", null, ["callee:00c599f0:8"]]
+ 0052454c ["INT_ADD", "register:40f0:8", ["const:52454c:8", "const:4:8"]]
+ 0052454c ["CALL", null, ["callee:00c599f0:8"]]
- 0052450c bytes 39d41c94
+ 0052454c bytes 29d51c94
~~~


<a id="compare-66e9c970f8f1c3ce7a0e1b45ab4a9cc0"></a>

### [`00524524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md) → [`00524564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md) _ZNK5Botan16X509_Certificate11fingerprintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c591c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591c0.md) [`00c59a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c595c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595c0.md) [`00c59e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md#insn-00524550) · [`00524564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md#insn-00524564) · [`00524574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524524.md#insn-00524574)
- 新版 [`00524590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-00524590) · [`005245a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-005245a4) · [`005245b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524564.md#insn-005245b4)

~~~diff
- 00524550 ["INT_ADD", "register:40f0:8", ["const:524550:8", "const:4:8"]]
- 00524550 ["CALL", null, ["callee:00c59e80:8"]]
+ 00524590 ["INT_ADD", "register:40f0:8", ["const:524590:8", "const:4:8"]]
+ 00524590 ["CALL", null, ["callee:00c59e80:8"]]
- 00524550 bytes 4cd51c94
+ 00524590 bytes 3cd61c94
- 00524564 ["INT_ADD", "register:40f0:8", ["const:524564:8", "const:4:8"]]
- 00524564 ["CALL", null, ["callee:00c595c0:8"]]
+ 005245a4 ["INT_ADD", "register:40f0:8", ["const:5245a4:8", "const:4:8"]]
+ 005245a4 ["CALL", null, ["callee:00c595c0:8"]]
- 00524564 bytes 17d31c94
+ 005245a4 bytes 07d41c94
- 00524574 ["INT_ADD", "register:40f0:8", ["const:524574:8", "const:4:8"]]
- 00524574 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005245b4 ["INT_ADD", "register:40f0:8", ["const:5245b4:8", "const:4:8"]]
+ 005245b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00524574 bytes 4fcd1c94
+ 005245b4 bytes 3fce1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869246243ca070bacc42ca841854cd8f"></a>

### [`005245d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005245d0.md) → [`00524610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md) _ZNK5Botan16X509_Certificate16matches_dns_nameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ac0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59520.md) [`00c59ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ab0.md)
- 新版 呼出元 1件 [`00c59ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ec0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59920.md) [`00c59eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005245d0.md#insn-00524630) · [`00524640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005245d0.md#insn-00524640) · [`00524674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/005245d0.md#insn-00524674)
- 新版 [`00524670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-00524670) · [`00524680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-00524680) · [`005246b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524610.md#insn-005246b4)

~~~diff
- 00524630 ["INT_ADD", "register:40f0:8", ["const:524630:8", "const:4:8"]]
- 00524630 ["CALL", null, ["callee:00c59eb0:8"]]
+ 00524670 ["INT_ADD", "register:40f0:8", ["const:524670:8", "const:4:8"]]
+ 00524670 ["CALL", null, ["callee:00c59eb0:8"]]
- 00524630 bytes 20d51c94
+ 00524670 bytes 10d61c94
- 00524640 ["INT_ADD", "register:40f0:8", ["const:524640:8", "const:4:8"]]
- 00524640 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00524680 ["INT_ADD", "register:40f0:8", ["const:524680:8", "const:4:8"]]
+ 00524680 ["CALL", null, ["callee:00c57eb0:8"]]
- 00524640 bytes 1ccd1c94
+ 00524680 bytes 0cce1c94
- 00524674 ["INT_ADD", "register:40f0:8", ["const:524674:8", "const:4:8"]]
- 00524674 ["CALL", null, ["callee:00c59eb0:8"]]
+ 005246b4 ["INT_ADD", "register:40f0:8", ["const:5246b4:8", "const:4:8"]]
+ 005246b4 ["CALL", null, ["callee:00c59eb0:8"]]
- 00524674 bytes 0fd51c94
+ 005246b4 bytes ffd51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1127cbead3f2e785e56df487ef7e924"></a>

### [`00524830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524830.md) → [`00524870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524870.md) _ZNK5Botan16X509_CertificateltERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524830.md#insn-0052486c)
- 新版 [`005248ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524870.md#insn-005248ac)

~~~diff
- 0052486c ["INT_ADD", "register:40f0:8", ["const:52486c:8", "const:4:8"]]
- 0052486c ["CALL", null, ["callee:00c58050:8"]]
+ 005248ac ["INT_ADD", "register:40f0:8", ["const:5248ac:8", "const:4:8"]]
+ 005248ac ["CALL", null, ["callee:00c58050:8"]]
- 0052486c bytes f9cc1c94
+ 005248ac bytes e9cd1c94
~~~


<a id="compare-e1111618e2667627c320d196952478bc"></a>

### [`00524924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524924.md) → [`00524964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md) _ZN5BotanneERKNS_16X509_CertificateES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c582a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00524950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524924.md#insn-00524950) · [`00524960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524924.md#insn-00524960) · [`00524980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00524/00524924.md#insn-00524980)
- 新版 [`00524990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-00524990) · [`005249a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-005249a0) · [`005249c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/00524964.md#insn-005249c0)

~~~diff
- 00524950 ["INT_ADD", "register:40f0:8", ["const:524950:8", "const:4:8"]]
- 00524950 ["CALL", null, ["callee:00c58050:8"]]
+ 00524990 ["INT_ADD", "register:40f0:8", ["const:524990:8", "const:4:8"]]
+ 00524990 ["CALL", null, ["callee:00c58050:8"]]
- 00524950 bytes c0cc1c94
+ 00524990 bytes b0cd1c94
- 00524960 ["INT_ADD", "register:40f0:8", ["const:524960:8", "const:4:8"]]
- 00524960 ["CALL", null, ["callee:00c586a0:8"]]
+ 005249a0 ["INT_ADD", "register:40f0:8", ["const:5249a0:8", "const:4:8"]]
+ 005249a0 ["CALL", null, ["callee:00c586a0:8"]]
- 00524960 bytes 50ce1c94
+ 005249a0 bytes 40cf1c94
- 00524980 ["INT_ADD", "register:40f0:8", ["const:524980:8", "const:4:8"]]
- 00524980 ["CALL", null, ["callee:00c58050:8"]]
+ 005249c0 ["INT_ADD", "register:40f0:8", ["const:5249c0:8", "const:4:8"]]
+ 005249c0 ["CALL", null, ["callee:00c58050:8"]]
- 00524980 bytes b4cc1c94
+ 005249c0 bytes a4cd1c94
~~~


<a id="compare-400348c56e71bcdec32e0e1ead728255"></a>

### [`005261d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005261d0.md) → [`00526210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md) _ZN5Botan17X509_Cert_Options10not_beforeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ad0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005261f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005261d0.md#insn-005261f8) · [`00526230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/005261d0.md#insn-00526230)
- 新版 [`00526238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md#insn-00526238) · [`00526270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526210.md#insn-00526270)

~~~diff
- 005261f8 ["INT_ADD", "register:40f0:8", ["const:5261f8:8", "const:4:8"]]
- 005261f8 ["CALL", null, ["callee:00c59ed0:8"]]
+ 00526238 ["INT_ADD", "register:40f0:8", ["const:526238:8", "const:4:8"]]
+ 00526238 ["CALL", null, ["callee:00c59ed0:8"]]
- 005261f8 bytes 36ce1c94
+ 00526238 bytes 26cf1c94
- 00526230 ["INT_ADD", "register:40f0:8", ["const:526230:8", "const:4:8"]]
- 00526230 ["CALL", null, ["callee:00c57ee0:8"]]
+ 00526270 ["INT_ADD", "register:40f0:8", ["const:526270:8", "const:4:8"]]
+ 00526270 ["CALL", null, ["callee:00c57ee0:8"]]
- 00526230 bytes 2cc61c94
+ 00526270 bytes 1cc71c94
~~~


<a id="compare-ed3abb176cdf8b9d31e22d6f4b86f647"></a>

### [`00526234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526234.md) → [`00526274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md) _ZN5Botan17X509_Cert_Options9not_afterERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ad0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526234.md#insn-0052625c) · [`00526294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526234.md#insn-00526294)
- 新版 [`0052629c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md#insn-0052629c) · [`005262d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/00526274.md#insn-005262d4)

~~~diff
- 0052625c ["INT_ADD", "register:40f0:8", ["const:52625c:8", "const:4:8"]]
- 0052625c ["CALL", null, ["callee:00c59ed0:8"]]
+ 0052629c ["INT_ADD", "register:40f0:8", ["const:52629c:8", "const:4:8"]]
+ 0052629c ["CALL", null, ["callee:00c59ed0:8"]]
- 0052625c bytes 1dce1c94
+ 0052629c bytes 0dcf1c94
- 00526294 ["INT_ADD", "register:40f0:8", ["const:526294:8", "const:4:8"]]
- 00526294 ["CALL", null, ["callee:00c57ee0:8"]]
+ 005262d4 ["INT_ADD", "register:40f0:8", ["const:5262d4:8", "const:4:8"]]
+ 005262d4 ["CALL", null, ["callee:00c57ee0:8"]]
- 00526294 bytes 13c61c94
+ 005262d4 bytes 03c71c94
~~~


<a id="compare-08539e3cddbd226030742b0c0cd18bc2"></a>

### [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) → [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) FUN_00527dbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) · 呼出先 2件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) · 呼出先 2件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00527db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md#insn-00527db4)
- 新版 [`00527df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md#insn-00527df4)

~~~diff
- 00527db4 ["INT_ADD", "register:40f0:8", ["const:527db4:8", "const:4:8"]]
- 00527db4 ["CALL", null, ["callee:0053f810:8"]]
+ 00527df4 ["INT_ADD", "register:40f0:8", ["const:527df4:8", "const:4:8"]]
+ 00527df4 ["CALL", null, ["callee:0053f810:8"]]
- 00527db4 bytes 875e0094
+ 00527df4 bytes 875e0094
~~~


<a id="compare-43fd91c1f7454d3a68384c45a7e99e0b"></a>

### [`00529c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529c78.md) → [`00529cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md) FUN_00529cb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00529cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529c78.md#insn-00529cc4) · [`00529cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529c78.md#insn-00529cd8) · [`00529ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529c78.md#insn-00529ce0)
- 新版 [`00529d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d04) · [`00529d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d18) · [`00529d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529cb8.md#insn-00529d20)

~~~diff
- 00529cc4 ["INT_ADD", "register:40f0:8", ["const:529cc4:8", "const:4:8"]]
- 00529cc4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00529d04 ["INT_ADD", "register:40f0:8", ["const:529d04:8", "const:4:8"]]
+ 00529d04 ["CALL", null, ["callee:00c53d00:8"]]
- 00529cc4 bytes 07a71c94
+ 00529d04 bytes ffa71c94
- 00529cd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00529cd8 ["INT_ADD", "register:40f0:8", ["const:529cd8:8", "const:4:8"]]
- 00529cd8 ["CALLIND", null, ["register:0:8"]]
+ 00529d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00529d18 ["INT_ADD", "register:40f0:8", ["const:529d18:8", "const:4:8"]]
+ 00529d18 ["CALLIND", null, ["register:0:8"]]
- 00529cd8 bytes 00013fd6
+ 00529d18 bytes 00013fd6
- 00529ce0 ["INT_ADD", "register:40f0:8", ["const:529ce0:8", "const:4:8"]]
- 00529ce0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00529d20 ["INT_ADD", "register:40f0:8", ["const:529d20:8", "const:4:8"]]
+ 00529d20 ["CALL", null, ["callee:00c57e80:8"]]
- 00529ce0 bytes 68b71c94
+ 00529d20 bytes 58b81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3665ba49ebae2cb4b154efef3d5990e"></a>

### [`0052b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b000.md) → [`0052b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md) FUN_0052b040

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b000.md#insn-0052b01c) · [`0052b03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b000.md#insn-0052b03c)
- 新版 [`0052b05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md#insn-0052b05c) · [`0052b07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b040.md#insn-0052b07c)

~~~diff
- 0052b01c ["INT_ADD", "register:40f0:8", ["const:52b01c:8", "const:4:8"]]
- 0052b01c ["CALL", null, ["callee:00c53d00:8"]]
+ 0052b05c ["INT_ADD", "register:40f0:8", ["const:52b05c:8", "const:4:8"]]
+ 0052b05c ["CALL", null, ["callee:00c53d00:8"]]
- 0052b01c bytes 31a21c94
+ 0052b05c bytes 29a31c94
- 0052b03c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b03c ["INT_ADD", "register:40f0:8", ["const:52b03c:8", "const:4:8"]]
- 0052b03c ["CALLIND", null, ["register:0:8"]]
+ 0052b07c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b07c ["INT_ADD", "register:40f0:8", ["const:52b07c:8", "const:4:8"]]
+ 0052b07c ["CALLIND", null, ["register:0:8"]]
- 0052b03c bytes 00013fd6
+ 0052b07c bytes 00013fd6
~~~


<a id="compare-20c0450043c060adcafe0e8332ddbdce"></a>

### [`0052b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b050.md) → [`0052b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md) FUN_0052b090

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052b09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b050.md#insn-0052b09c) · [`0052b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b050.md#insn-0052b0b0) · [`0052b0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b050.md#insn-0052b0b8)
- 新版 [`0052b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0dc) · [`0052b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0f0) · [`0052b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b090.md#insn-0052b0f8)

~~~diff
- 0052b09c ["INT_ADD", "register:40f0:8", ["const:52b09c:8", "const:4:8"]]
- 0052b09c ["CALL", null, ["callee:00c53d00:8"]]
+ 0052b0dc ["INT_ADD", "register:40f0:8", ["const:52b0dc:8", "const:4:8"]]
+ 0052b0dc ["CALL", null, ["callee:00c53d00:8"]]
- 0052b09c bytes 11a21c94
+ 0052b0dc bytes 09a31c94
- 0052b0b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052b0b0 ["INT_ADD", "register:40f0:8", ["const:52b0b0:8", "const:4:8"]]
- 0052b0b0 ["CALLIND", null, ["register:0:8"]]
+ 0052b0f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052b0f0 ["INT_ADD", "register:40f0:8", ["const:52b0f0:8", "const:4:8"]]
+ 0052b0f0 ["CALLIND", null, ["register:0:8"]]
- 0052b0b0 bytes 00013fd6
+ 0052b0f0 bytes 00013fd6
- 0052b0b8 ["INT_ADD", "register:40f0:8", ["const:52b0b8:8", "const:4:8"]]
- 0052b0b8 ["CALL", null, ["callee:00c57e80:8"]]
+ 0052b0f8 ["INT_ADD", "register:40f0:8", ["const:52b0f8:8", "const:4:8"]]
+ 0052b0f8 ["CALL", null, ["callee:00c57e80:8"]]
- 0052b0b8 bytes 72b21c94
+ 0052b0f8 bytes 62b31c94
~~~


<a id="compare-5d28e3b468d46b288bbfe57b0b9cc647"></a>

### [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) → [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) FUN_0052c244

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c488.md) [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) · 呼出先 4件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) [`0052c4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md) [`0054ed04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md) · 呼出先 4件 [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md#insn-0052c250) · [`0052c264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md#insn-0052c264) · [`0052c26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md#insn-0052c26c)
- 新版 [`0052c290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c290) · [`0052c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c2a4) · [`0052c2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md#insn-0052c2ac)

~~~diff
- 0052c250 ["INT_ADD", "register:40f0:8", ["const:52c250:8", "const:4:8"]]
- 0052c250 ["CALL", null, ["callee:00c53d00:8"]]
+ 0052c290 ["INT_ADD", "register:40f0:8", ["const:52c290:8", "const:4:8"]]
+ 0052c290 ["CALL", null, ["callee:00c53d00:8"]]
- 0052c250 bytes a49d1c94
+ 0052c290 bytes 9c9e1c94
- 0052c264 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c264 ["INT_ADD", "register:40f0:8", ["const:52c264:8", "const:4:8"]]
- 0052c264 ["CALLIND", null, ["register:0:8"]]
+ 0052c2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c2a4 ["INT_ADD", "register:40f0:8", ["const:52c2a4:8", "const:4:8"]]
+ 0052c2a4 ["CALLIND", null, ["register:0:8"]]
- 0052c264 bytes 00013fd6
+ 0052c2a4 bytes 00013fd6
- 0052c26c ["INT_ADD", "register:40f0:8", ["const:52c26c:8", "const:4:8"]]
- 0052c26c ["CALL", null, ["callee:00c57e80:8"]]
+ 0052c2ac ["INT_ADD", "register:40f0:8", ["const:52c2ac:8", "const:4:8"]]
+ 0052c2ac ["CALL", null, ["callee:00c57e80:8"]]
- 0052c26c bytes 05ae1c94
+ 0052c2ac bytes f5ae1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b72407a042b0048328ba6d43c97a52c"></a>

### [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) → [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) FUN_0052c354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 7件 [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`0054eb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eb4c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) · 呼出先 7件 [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) [`0054eb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eb8c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md#insn-0052c368) · [`0052c38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md#insn-0052c38c) · [`0052c3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md#insn-0052c3b8)
- 新版 [`0052c3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3a8) · [`0052c3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3cc) · [`0052c3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md#insn-0052c3f8)

~~~diff
- 0052c368 ["INT_ADD", "register:40f0:8", ["const:52c368:8", "const:4:8"]]
- 0052c368 ["CALL", null, ["callee:0054eb8c:8"]]
+ 0052c3a8 ["INT_ADD", "register:40f0:8", ["const:52c3a8:8", "const:4:8"]]
+ 0052c3a8 ["CALL", null, ["callee:0054eb8c:8"]]
- 0052c368 bytes f9890094
+ 0052c3a8 bytes f9890094
- 0052c38c ["INT_ADD", "register:40f0:8", ["const:52c38c:8", "const:4:8"]]
- 0052c38c ["CALL", null, ["callee:0054eb8c:8"]]
+ 0052c3cc ["INT_ADD", "register:40f0:8", ["const:52c3cc:8", "const:4:8"]]
+ 0052c3cc ["CALL", null, ["callee:0054eb8c:8"]]
- 0052c38c bytes f0890094
+ 0052c3cc bytes f0890094
- 0052c3b8 ["INT_ADD", "register:40f0:8", ["const:52c3b8:8", "const:4:8"]]
- 0052c3b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052c3f8 ["INT_ADD", "register:40f0:8", ["const:52c3f8:8", "const:4:8"]]
+ 0052c3f8 ["CALL", null, ["callee:00c57e90:8"]]
- 0052c3b8 bytes b6ad1c94
+ 0052c3f8 bytes a6ae1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ae320c14e0f4642eada45f37df1551"></a>

### [`0052c488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c488.md) → [`0052c4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md) FUN_0052c4c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052c204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c204.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c488.md#insn-0052c4bc)
- 新版 [`0052c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c4c8.md#insn-0052c4fc)

~~~diff
- 0052c4bc ["INT_ADD", "register:40f0:8", ["const:52c4bc:8", "const:4:8"]]
- 0052c4bc ["CALL", null, ["callee:0052c244:8"]]
+ 0052c4fc ["INT_ADD", "register:40f0:8", ["const:52c4fc:8", "const:4:8"]]
+ 0052c4fc ["CALL", null, ["callee:0052c244:8"]]
- 0052c4bc bytes 52ffff97
+ 0052c4fc bytes 52ffff97
~~~


<a id="compare-2023ae88534f9b2a6aec49487c3bcdbc"></a>

### [`0052c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c4f0.md) → [`0052c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md) FUN_0052c530

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c4f0.md#insn-0052c534) · [`0052c57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c4f0.md#insn-0052c57c) · [`0052c590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c4f0.md#insn-0052c590)
- 新版 [`0052c574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c574) · [`0052c5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c5bc) · [`0052c5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c530.md#insn-0052c5d0)

~~~diff
- 0052c534 ["INT_ADD", "register:40f0:8", ["const:52c534:8", "const:4:8"]]
- 0052c534 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052c574 ["INT_ADD", "register:40f0:8", ["const:52c574:8", "const:4:8"]]
+ 0052c574 ["CALL", null, ["callee:00c57eb0:8"]]
- 0052c534 bytes 5fad1c94
+ 0052c574 bytes 4fae1c94
- 0052c57c ["INT_ADD", "register:40f0:8", ["const:52c57c:8", "const:4:8"]]
- 0052c57c ["CALL", null, ["callee:00c53d00:8"]]
+ 0052c5bc ["INT_ADD", "register:40f0:8", ["const:52c5bc:8", "const:4:8"]]
+ 0052c5bc ["CALL", null, ["callee:00c53d00:8"]]
- 0052c57c bytes d99c1c94
+ 0052c5bc bytes d19d1c94
- 0052c590 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c590 ["INT_ADD", "register:40f0:8", ["const:52c590:8", "const:4:8"]]
- 0052c590 ["CALLIND", null, ["register:0:8"]]
+ 0052c5d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c5d0 ["INT_ADD", "register:40f0:8", ["const:52c5d0:8", "const:4:8"]]
+ 0052c5d0 ["CALLIND", null, ["register:0:8"]]
- 0052c590 bytes 00013fd6
+ 0052c5d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e005cf6bf2b0c7853eeb2579cf808f75"></a>

### [`0052c5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c5d8.md) → [`0052c618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS6_9a

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054eed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eed0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ef10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c5d8.md#insn-0052c634) · [`0052c660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c5d8.md#insn-0052c660) · [`0052c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c5d8.md#insn-0052c690)
- 新版 [`0052c674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c674) · [`0052c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c6a0) · [`0052c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c618.md#insn-0052c6d0)

~~~diff
- 0052c634 ["INT_ADD", "register:40f0:8", ["const:52c634:8", "const:4:8"]]
- 0052c634 ["CALL", null, ["callee:0054ef10:8"]]
+ 0052c674 ["INT_ADD", "register:40f0:8", ["const:52c674:8", "const:4:8"]]
+ 0052c674 ["CALL", null, ["callee:0054ef10:8"]]
- 0052c634 bytes 278a0094
+ 0052c674 bytes 278a0094
- 0052c660 ["INT_ADD", "register:40f0:8", ["const:52c660:8", "const:4:8"]]
- 0052c660 ["CALL", null, ["callee:00c59f40:8"]]
+ 0052c6a0 ["INT_ADD", "register:40f0:8", ["const:52c6a0:8", "const:4:8"]]
+ 0052c6a0 ["CALL", null, ["callee:00c59f40:8"]]
- 0052c660 bytes 38b51c94
+ 0052c6a0 bytes 28b61c94
- 0052c690 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052c690 ["INT_ADD", "register:40f0:8", ["const:52c690:8", "const:4:8"]]
- 0052c690 ["CALLIND", null, ["register:0:8"]]
+ 0052c6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052c6d0 ["INT_ADD", "register:40f0:8", ["const:52c6d0:8", "const:4:8"]]
+ 0052c6d0 ["CALLIND", null, ["register:0:8"]]
- 0052c690 bytes 00013fd6
+ 0052c6d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe2986920071032111d5ca6887871af"></a>

### [`0052c704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c704.md) → [`0052c744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS_17Cer

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c704.md#insn-0052c758) · [`0052c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c704.md#insn-0052c794) · [`0052c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c704.md#insn-0052c7f0)
- 新版 [`0052c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c798) · [`0052c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c7d4) · [`0052c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c744.md#insn-0052c830)

~~~diff
- 0052c758 ["INT_ADD", "register:40f0:8", ["const:52c758:8", "const:4:8"]]
- 0052c758 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052c798 ["INT_ADD", "register:40f0:8", ["const:52c798:8", "const:4:8"]]
+ 0052c798 ["CALL", null, ["callee:00c57e90:8"]]
- 0052c758 bytes ceac1c94
+ 0052c798 bytes bead1c94
- 0052c794 ["INT_ADD", "register:40f0:8", ["const:52c794:8", "const:4:8"]]
- 0052c794 ["CALL", null, ["callee:00c59f40:8"]]
+ 0052c7d4 ["INT_ADD", "register:40f0:8", ["const:52c7d4:8", "const:4:8"]]
+ 0052c7d4 ["CALL", null, ["callee:00c59f40:8"]]
- 0052c794 bytes ebb41c94
+ 0052c7d4 bytes dbb51c94
- 0052c7f0 ["INT_ADD", "register:40f0:8", ["const:52c7f0:8", "const:4:8"]]
- 0052c7f0 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0052c830 ["INT_ADD", "register:40f0:8", ["const:52c830:8", "const:4:8"]]
+ 0052c830 ["CALL", null, ["callee:00c57ee0:8"]]
- 0052c7f0 bytes bcac1c94
+ 0052c830 bytes acad1c94
~~~


<a id="compare-688c1a2dcb1a268402b18c4ce3e58fd5"></a>

### [`0052c7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c7f4.md) → [`0052c834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md) _ZN5Botan18x509_path_validateERKNS_16X509_CertificateERKNS_28Path_Validation_RestrictionsERKNS_17Certificate_StoreERKNSt6__ndk112basic_strin

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054eed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eed0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ef10.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c7f4.md#insn-0052c850) · [`0052c85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c7f4.md#insn-0052c85c) · [`0052c898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c7f4.md#insn-0052c898)
- 新版 [`0052c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c890) · [`0052c89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c89c) · [`0052c8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c834.md#insn-0052c8d8)

~~~diff
- 0052c850 ["INT_ADD", "register:40f0:8", ["const:52c850:8", "const:4:8"]]
- 0052c850 ["CALL", null, ["callee:0054ef10:8"]]
+ 0052c890 ["INT_ADD", "register:40f0:8", ["const:52c890:8", "const:4:8"]]
+ 0052c890 ["CALL", null, ["callee:0054ef10:8"]]
- 0052c850 bytes a0890094
+ 0052c890 bytes a0890094
- 0052c85c ["INT_ADD", "register:40f0:8", ["const:52c85c:8", "const:4:8"]]
- 0052c85c ["CALL", null, ["callee:00c57e90:8"]]
+ 0052c89c ["INT_ADD", "register:40f0:8", ["const:52c89c:8", "const:4:8"]]
+ 0052c89c ["CALL", null, ["callee:00c57e90:8"]]
- 0052c85c bytes 8dac1c94
+ 0052c89c bytes 7dad1c94
- 0052c898 ["INT_ADD", "register:40f0:8", ["const:52c898:8", "const:4:8"]]
- 0052c898 ["CALL", null, ["callee:00c59f40:8"]]
+ 0052c8d8 ["INT_ADD", "register:40f0:8", ["const:52c8d8:8", "const:4:8"]]
+ 0052c8d8 ["CALL", null, ["callee:00c59f40:8"]]
- 0052c898 bytes aab41c94
+ 0052c8d8 bytes 9ab51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb24203d6c54c059466ab9dd009c27e"></a>

### [`0052c958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md) → [`0052c998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md) _ZN5Botan28Path_Validation_RestrictionsC1Ebmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052c9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md#insn-0052c9d4) · [`0052c9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md#insn-0052c9ec) · [`0052ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md#insn-0052ca20)
- 新版 [`0052ca14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca14) · [`0052ca2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca2c) · [`0052ca60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c998.md#insn-0052ca60)

~~~diff
- 0052c9d4 ["INT_ADD", "register:40f0:8", ["const:52c9d4:8", "const:4:8"]]
- 0052c9d4 ["CALL", null, ["callee:0054a614:8"]]
+ 0052ca14 ["INT_ADD", "register:40f0:8", ["const:52ca14:8", "const:4:8"]]
+ 0052ca14 ["CALL", null, ["callee:0054a614:8"]]
- 0052c9d4 bytes 00770094
+ 0052ca14 bytes 00770094
- 0052c9ec ["INT_ADD", "register:40f0:8", ["const:52c9ec:8", "const:4:8"]]
- 0052c9ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052ca2c ["INT_ADD", "register:40f0:8", ["const:52ca2c:8", "const:4:8"]]
+ 0052ca2c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052c9ec bytes 31ac1c94
+ 0052ca2c bytes 21ad1c94
- 0052ca20 ["INT_ADD", "register:40f0:8", ["const:52ca20:8", "const:4:8"]]
- 0052ca20 ["CALL", null, ["callee:0054a614:8"]]
+ 0052ca60 ["INT_ADD", "register:40f0:8", ["const:52ca60:8", "const:4:8"]]
+ 0052ca60 ["CALL", null, ["callee:0054a614:8"]]
- 0052ca20 bytes ed760094
+ 0052ca60 bytes ed760094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e786d3594cb7d8fca907727d0ab5cad"></a>

### [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) → [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) _ZN5Botan22Path_Validation_ResultC1ENSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b50.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00501d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501d78.md) [`00527d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527d7c.md) [`0053f2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f2f0.md) [`0053f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f504.md)
- 新版 呼出元 1件 [`00c59f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f50.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00501db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501db8.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`0053f330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f330.md) [`0053f544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f544.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md#insn-0052ce10) · [`0052ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md#insn-0052ce40) · [`0052ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md#insn-0052ce50)
- 新版 [`0052ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce50) · [`0052ce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce80) · [`0052ce90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md#insn-0052ce90)

~~~diff
- 0052ce10 ["INT_ADD", "register:40f0:8", ["const:52ce10:8", "const:4:8"]]
- 0052ce10 ["CALL", null, ["callee:0054eb8c:8"]]
+ 0052ce50 ["INT_ADD", "register:40f0:8", ["const:52ce50:8", "const:4:8"]]
+ 0052ce50 ["CALL", null, ["callee:0054eb8c:8"]]
- 0052ce10 bytes 4f870094
+ 0052ce50 bytes 4f870094
- 0052ce40 ["INT_ADD", "register:40f0:8", ["const:52ce40:8", "const:4:8"]]
- 0052ce40 ["CALL", null, ["callee:0053f330:8"]]
+ 0052ce80 ["INT_ADD", "register:40f0:8", ["const:52ce80:8", "const:4:8"]]
+ 0052ce80 ["CALL", null, ["callee:0053f330:8"]]
- 0052ce40 bytes 2c490094
+ 0052ce80 bytes 2c490094
- 0052ce50 ["INT_ADD", "register:40f0:8", ["const:52ce50:8", "const:4:8"]]
- 0052ce50 ["CALL", null, ["callee:0053f810:8"]]
+ 0052ce90 ["INT_ADD", "register:40f0:8", ["const:52ce90:8", "const:4:8"]]
+ 0052ce90 ["CALL", null, ["callee:0053f810:8"]]
- 0052ce50 bytes 604a0094
+ 0052ce90 bytes 604a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ccfd409950dee54c4300a8f8d97a83"></a>

### [`0052d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) → [`0052d284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md) _ZNK5Botan22Path_Validation_Result14trusted_hashesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0054a614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a614.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052d2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md#insn-0052d2b8) · [`0052d2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md#insn-0052d2c8) · [`0052d2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md#insn-0052d2e8)
- 新版 [`0052d2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d2f8) · [`0052d308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d308) · [`0052d328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d284.md#insn-0052d328)

~~~diff
- 0052d2b8 ["INT_ADD", "register:40f0:8", ["const:52d2b8:8", "const:4:8"]]
- 0052d2b8 ["CALL", null, ["callee:00c59e90:8"]]
+ 0052d2f8 ["INT_ADD", "register:40f0:8", ["const:52d2f8:8", "const:4:8"]]
+ 0052d2f8 ["CALL", null, ["callee:00c59e90:8"]]
- 0052d2b8 bytes f6b11c94
+ 0052d2f8 bytes e6b21c94
- 0052d2c8 ["INT_ADD", "register:40f0:8", ["const:52d2c8:8", "const:4:8"]]
- 0052d2c8 ["CALL", null, ["callee:0054a614:8"]]
+ 0052d308 ["INT_ADD", "register:40f0:8", ["const:52d308:8", "const:4:8"]]
+ 0052d308 ["CALL", null, ["callee:0054a614:8"]]
- 0052d2c8 bytes c3740094
+ 0052d308 bytes c3740094
- 0052d2e8 ["INT_ADD", "register:40f0:8", ["const:52d2e8:8", "const:4:8"]]
- 0052d2e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052d328 ["INT_ADD", "register:40f0:8", ["const:52d328:8", "const:4:8"]]
+ 0052d328 ["CALL", null, ["callee:00c57e90:8"]]
- 0052d2e8 bytes eaa91c94
+ 0052d328 bytes daaa1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f3d3fd7b4720b97731880cb0141f24"></a>

### [`0052dbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dbcc.md) → [`0052dc0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md) FUN_0052dc0c

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dbcc.md#insn-0052dbf0) · [`0052dc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dbcc.md#insn-0052dc38) · [`0052dc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dbcc.md#insn-0052dc58)
- 新版 [`0052dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc30) · [`0052dc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc78) · [`0052dc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dc0c.md#insn-0052dc98)

~~~diff
- 0052dbf0 ["INT_ADD", "register:40f0:8", ["const:52dbf0:8", "const:4:8"]]
- 0052dbf0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052dc30 ["INT_ADD", "register:40f0:8", ["const:52dc30:8", "const:4:8"]]
+ 0052dc30 ["CALL", null, ["callee:00c57fe0:8"]]
- 0052dbf0 bytes fca71c94
+ 0052dc30 bytes eca81c94
- 0052dc38 ["INT_ADD", "register:40f0:8", ["const:52dc38:8", "const:4:8"]]
- 0052dc38 ["CALL", null, ["callee:00c57e90:8"]]
+ 0052dc78 ["INT_ADD", "register:40f0:8", ["const:52dc78:8", "const:4:8"]]
+ 0052dc78 ["CALL", null, ["callee:00c57e90:8"]]
- 0052dc38 bytes 96a71c94
+ 0052dc78 bytes 86a81c94
- 0052dc58 ["INT_ADD", "register:40f0:8", ["const:52dc58:8", "const:4:8"]]
- 0052dc58 ["CALL", null, ["callee:00c57f40:8"]]
+ 0052dc98 ["INT_ADD", "register:40f0:8", ["const:52dc98:8", "const:4:8"]]
+ 0052dc98 ["CALL", null, ["callee:00c57f40:8"]]
- 0052dc58 bytes baa71c94
+ 0052dc98 bytes aaa81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f74e3c2de809e49d5290e70b695f674"></a>

### [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md) → [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) FUN_0052dd00

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 63件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) [`005cccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cccc4.md) [`005db448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db448.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`0054f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f154.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 62件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) [`005ccd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005ccd04.md) [`005db488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db488.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0053bcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bcb0.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md#insn-0052dd10) · [`0052dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md#insn-0052dd40) · [`0052dd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md#insn-0052dd5c)
- 新版 [`0052dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd50) · [`0052dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd80) · [`0052dd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md#insn-0052dd9c)

~~~diff
- 0052dd10 ["INT_ADD", "register:40f0:8", ["const:52dd10:8", "const:4:8"]]
- 0052dd10 ["CALL", null, ["callee:0043bba4:8"]]
+ 0052dd50 ["INT_ADD", "register:40f0:8", ["const:52dd50:8", "const:4:8"]]
+ 0052dd50 ["CALL", null, ["callee:0043bba4:8"]]
- 0052dd10 bytes 9537fc97
+ 0052dd50 bytes 9537fc97
- 0052dd40 ["INT_ADD", "register:40f0:8", ["const:52dd40:8", "const:4:8"]]
- 0052dd40 ["CALL", null, ["callee:0054f194:8"]]
+ 0052dd80 ["INT_ADD", "register:40f0:8", ["const:52dd80:8", "const:4:8"]]
+ 0052dd80 ["CALL", null, ["callee:0054f194:8"]]
- 0052dd40 bytes 05850094
+ 0052dd80 bytes 05850094
- 0052dd5c ["INT_ADD", "register:40f0:8", ["const:52dd5c:8", "const:4:8"]]
- 0052dd5c ["CALL", null, ["callee:0053bcb0:8"]]
+ 0052dd9c ["INT_ADD", "register:40f0:8", ["const:52dd9c:8", "const:4:8"]]
+ 0052dd9c ["CALL", null, ["callee:0053bcb0:8"]]
- 0052dd5c bytes c5370094
+ 0052dd9c bytes c5370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9fa336e3c32baa5bfd4337a8026e98"></a>

### [`0052ef3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef3c.md) → [`0052ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052ef7c.md) FUN_0052ef7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052ef58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef3c.md#insn-0052ef58)
- 新版 [`0052ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052ef7c.md#insn-0052ef98)

~~~diff
- 0052ef58 ["INT_ADD", "register:40f0:8", ["const:52ef58:8", "const:4:8"]]
- 0052ef58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052ef98 ["INT_ADD", "register:40f0:8", ["const:52ef98:8", "const:4:8"]]
+ 0052ef98 ["CALL", null, ["callee:00c57eb0:8"]]
- 0052ef58 bytes d6a21c94
+ 0052ef98 bytes c6a31c94
~~~


<a id="compare-dce064d7e8cf740606169934481c2616"></a>

### [`0052f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f074.md) → [`0052f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md) FUN_0052f0b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052ef80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052ef80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f074.md#insn-0052f084)
- 新版 [`0052f0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md#insn-0052f0c4)

~~~diff
- 0052f084 ["INT_ADD", "register:40f0:8", ["const:52f084:8", "const:4:8"]]
- 0052f084 ["CALL", null, ["callee:0052efc0:8"]]
+ 0052f0c4 ["INT_ADD", "register:40f0:8", ["const:52f0c4:8", "const:4:8"]]
+ 0052f0c4 ["CALL", null, ["callee:0052efc0:8"]]
- 0052f084 bytes bfffff97
+ 0052f0c4 bytes bfffff97
~~~


<a id="compare-2c5f974e2a10532a6f071cfb83182948"></a>

### [`0052f360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f360.md) → [`0052f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md) FUN_0052f3a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f26c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f360.md#insn-0052f370)
- 新版 [`0052f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md#insn-0052f3b0)

~~~diff
- 0052f370 ["INT_ADD", "register:40f0:8", ["const:52f370:8", "const:4:8"]]
- 0052f370 ["CALL", null, ["callee:0052f2ac:8"]]
+ 0052f3b0 ["INT_ADD", "register:40f0:8", ["const:52f3b0:8", "const:4:8"]]
+ 0052f3b0 ["CALL", null, ["callee:0052f2ac:8"]]
- 0052f370 bytes bfffff97
+ 0052f3b0 bytes bfffff97
~~~


<a id="compare-2e7f55488333675a3e918b56ca79351b"></a>

### [`0052f64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f64c.md) → [`0052f68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md) FUN_0052f68c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0052f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f558.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0052f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052f65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052f64c.md#insn-0052f65c)
- 新版 [`0052f69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md#insn-0052f69c)

~~~diff
- 0052f65c ["INT_ADD", "register:40f0:8", ["const:52f65c:8", "const:4:8"]]
- 0052f65c ["CALL", null, ["callee:0052f598:8"]]
+ 0052f69c ["INT_ADD", "register:40f0:8", ["const:52f69c:8", "const:4:8"]]
+ 0052f69c ["CALL", null, ["callee:0052f598:8"]]
- 0052f65c bytes bfffff97
+ 0052f69c bytes bfffff97
~~~


<a id="compare-a4826fbd831a20ba64e9913dcfd7e03d"></a>

### [`0052fd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd3c.md) → [`0052fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md) FUN_0052fd7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd3c.md#insn-0052fd58) · [`0052fd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd3c.md#insn-0052fd68)
- 新版 [`0052fd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md#insn-0052fd98) · [`0052fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fd7c.md#insn-0052fda8)

~~~diff
- 0052fd58 ["INT_ADD", "register:40f0:8", ["const:52fd58:8", "const:4:8"]]
- 0052fd58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fd98 ["INT_ADD", "register:40f0:8", ["const:52fd98:8", "const:4:8"]]
+ 0052fd98 ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fd58 bytes 569f1c94
+ 0052fd98 bytes 46a01c94
- 0052fd68 ["INT_ADD", "register:40f0:8", ["const:52fd68:8", "const:4:8"]]
- 0052fd68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fda8 ["INT_ADD", "register:40f0:8", ["const:52fda8:8", "const:4:8"]]
+ 0052fda8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fd68 bytes 529f1c94
+ 0052fda8 bytes 42a01c94
~~~


<a id="compare-54df6f04e800f6027cea25691ea4d1a0"></a>

### [`0052fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd7c.md) → [`0052fdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdbc.md) FUN_0052fdbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fd7c.md#insn-0052fd9c)
- 新版 [`0052fddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdbc.md#insn-0052fddc)

~~~diff
- 0052fd9c ["INT_ADD", "register:40f0:8", ["const:52fd9c:8", "const:4:8"]]
- 0052fd9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fddc ["INT_ADD", "register:40f0:8", ["const:52fddc:8", "const:4:8"]]
+ 0052fddc ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fd9c bytes 459f1c94
+ 0052fddc bytes 35a01c94
~~~


<a id="compare-facbfe6c601d34b143bbcce4d46beefa"></a>

### [`0052fdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdb0.md) → [`0052fdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md) FUN_0052fdf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdb0.md#insn-0052fdcc) · [`0052fddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdb0.md#insn-0052fddc)
- 新版 [`0052fe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md#insn-0052fe0c) · [`0052fe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fdf0.md#insn-0052fe1c)

~~~diff
- 0052fdcc ["INT_ADD", "register:40f0:8", ["const:52fdcc:8", "const:4:8"]]
- 0052fdcc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fe0c ["INT_ADD", "register:40f0:8", ["const:52fe0c:8", "const:4:8"]]
+ 0052fe0c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fdcc bytes 399f1c94
+ 0052fe0c bytes 29a01c94
- 0052fddc ["INT_ADD", "register:40f0:8", ["const:52fddc:8", "const:4:8"]]
- 0052fddc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
+ 0052fe1c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fddc bytes 359f1c94
+ 0052fe1c bytes 25a01c94
~~~


<a id="compare-8e4b232d1a4bfa8e548211b01439bdbc"></a>

### [`0052fdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdf0.md) → [`0052fe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md) FUN_0052fe30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0052fe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdf0.md#insn-0052fe0c) · [`0052fe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052f/0052fdf0.md#insn-0052fe1c)
- 新版 [`0052fe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md#insn-0052fe4c) · [`0052fe5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe30.md#insn-0052fe5c)

~~~diff
- 0052fe0c ["INT_ADD", "register:40f0:8", ["const:52fe0c:8", "const:4:8"]]
- 0052fe0c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fe4c ["INT_ADD", "register:40f0:8", ["const:52fe4c:8", "const:4:8"]]
+ 0052fe4c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fe0c bytes 299f1c94
+ 0052fe4c bytes 19a01c94
- 0052fe1c ["INT_ADD", "register:40f0:8", ["const:52fe1c:8", "const:4:8"]]
- 0052fe1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0052fe5c ["INT_ADD", "register:40f0:8", ["const:52fe5c:8", "const:4:8"]]
+ 0052fe5c ["CALL", null, ["callee:00c57eb0:8"]]
- 0052fe1c bytes 259f1c94
+ 0052fe5c bytes 15a01c94
~~~


<a id="compare-5df2bfae4f3aa39339907e8ab7ce4f73"></a>

### [`0053037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053037c.md) → [`005303bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md) FUN_005303bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005302a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005302a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005302e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053037c.md#insn-0053038c)
- 新版 [`005303cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md#insn-005303cc)

~~~diff
- 0053038c ["INT_ADD", "register:40f0:8", ["const:53038c:8", "const:4:8"]]
- 0053038c ["CALL", null, ["callee:005302e8:8"]]
+ 005303cc ["INT_ADD", "register:40f0:8", ["const:5303cc:8", "const:4:8"]]
+ 005303cc ["CALL", null, ["callee:005302e8:8"]]
- 0053038c bytes c7ffff97
+ 005303cc bytes c7ffff97
~~~


<a id="compare-337212c9a1d221a4e427487f821220bc"></a>

### [`005303a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md) → [`005303e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md) FUN_005303e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cbc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cbc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbc50.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005303b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md#insn-005303b0) · [`005303b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md#insn-005303b8)
- 新版 [`005303f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md#insn-005303f0) · [`005303f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md#insn-005303f8)

~~~diff
- 005303b0 ["INT_ADD", "register:40f0:8", ["const:5303b0:8", "const:4:8"]]
- 005303b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 005303f0 ["INT_ADD", "register:40f0:8", ["const:5303f0:8", "const:4:8"]]
+ 005303f0 ["CALL", null, ["callee:00c57e90:8"]]
- 005303b0 bytes b89d1c94
+ 005303f0 bytes a89e1c94
- 005303b8 ["INT_ADD", "register:40f0:8", ["const:5303b8:8", "const:4:8"]]
- 005303b8 ["CALL", null, ["callee:004cbc50:8"]]
+ 005303f8 ["INT_ADD", "register:40f0:8", ["const:5303f8:8", "const:4:8"]]
+ 005303f8 ["CALL", null, ["callee:004cbc50:8"]]
- 005303b8 bytes 166efe97
+ 005303f8 bytes 166efe97
~~~


<a id="compare-fd24f72bdfda61f5abb52f7a1085996b"></a>

### [`005303fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303fc.md) → [`0053043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md) FUN_0053043c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303fc.md#insn-00530418) · [`00530424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303fc.md#insn-00530424)
- 新版 [`00530458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md#insn-00530458) · [`00530464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053043c.md#insn-00530464)

~~~diff
- 00530418 ["INT_ADD", "register:40f0:8", ["const:530418:8", "const:4:8"]]
- 00530418 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00530458 ["INT_ADD", "register:40f0:8", ["const:530458:8", "const:4:8"]]
+ 00530458 ["CALL", null, ["callee:00c57eb0:8"]]
- 00530418 bytes a69d1c94
+ 00530458 bytes 969e1c94
- 00530424 ["INT_ADD", "register:40f0:8", ["const:530424:8", "const:4:8"]]
- 00530424 ["CALL", null, ["callee:0053af90:8"]]
+ 00530464 ["INT_ADD", "register:40f0:8", ["const:530464:8", "const:4:8"]]
+ 00530464 ["CALL", null, ["callee:0053af90:8"]]
- 00530424 bytes cb2a0094
+ 00530464 bytes cb2a0094
~~~


<a id="compare-ee00744862ee02308475fd0a4b918830"></a>

### [`005305d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005305d0.md) → [`00530610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530610.md) FUN_00530610

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005305f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005305d0.md#insn-005305f8)
- 新版 [`00530638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530610.md#insn-00530638)

~~~diff
- 005305f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005305f8 ["INT_ADD", "register:40f0:8", ["const:5305f8:8", "const:4:8"]]
- 005305f8 ["CALLIND", null, ["register:0:8"]]
+ 00530638 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530638 ["INT_ADD", "register:40f0:8", ["const:530638:8", "const:4:8"]]
+ 00530638 ["CALLIND", null, ["register:0:8"]]
- 005305f8 bytes 20013fd6
+ 00530638 bytes 20013fd6
~~~


<a id="compare-6c64daf88543a73b7983ef85547ba500"></a>

### [`00530878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md) → [`005308b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md) FUN_005308b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530878.md#insn-00530888)
- 新版 [`005308c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md#insn-005308c8)

~~~diff
- 00530888 ["INT_ADD", "register:40f0:8", ["const:530888:8", "const:4:8"]]
- 00530888 ["CALL", null, ["callee:005307cc:8"]]
+ 005308c8 ["INT_ADD", "register:40f0:8", ["const:5308c8:8", "const:4:8"]]
+ 005308c8 ["CALL", null, ["callee:005307cc:8"]]
- 00530888 bytes c1ffff97
+ 005308c8 bytes c1ffff97
~~~


<a id="compare-ae7a1a1a16538545ff4985f80bc3ab88"></a>

### [`0053090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md) → [`0053094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md) FUN_0053094c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053090c.md#insn-00530920)
- 新版 [`00530960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md#insn-00530960)

~~~diff
- 00530920 ["INT_ADD", "register:40f0:8", ["const:530920:8", "const:4:8"]]
- 00530920 ["CALL", null, ["callee:005307cc:8"]]
+ 00530960 ["INT_ADD", "register:40f0:8", ["const:530960:8", "const:4:8"]]
+ 00530960 ["CALL", null, ["callee:005307cc:8"]]
- 00530920 bytes 9bffff97
+ 00530960 bytes 9bffff97
~~~


<a id="compare-847923c8c00d179fc7ed81309c897c8a"></a>

### [`00530a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md) → [`00530a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md) FUN_00530a48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00530934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530934.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a08.md#insn-00530a18)
- 新版 [`00530a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md#insn-00530a58)

~~~diff
- 00530a18 ["INT_ADD", "register:40f0:8", ["const:530a18:8", "const:4:8"]]
- 00530a18 ["CALL", null, ["callee:00530974:8"]]
+ 00530a58 ["INT_ADD", "register:40f0:8", ["const:530a58:8", "const:4:8"]]
+ 00530a58 ["CALL", null, ["callee:00530974:8"]]
- 00530a18 bytes c7ffff97
+ 00530a58 bytes c7ffff97
~~~


<a id="compare-58d2a673564b04052f540225a724e0e4"></a>

### [`00530a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md) → [`00530a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md) FUN_00530a6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb72c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md#insn-00530a3c) · [`00530a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md#insn-00530a44)
- 新版 [`00530a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md#insn-00530a7c) · [`00530a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md#insn-00530a84)

~~~diff
- 00530a3c ["INT_ADD", "register:40f0:8", ["const:530a3c:8", "const:4:8"]]
- 00530a3c ["CALL", null, ["callee:00c57e90:8"]]
+ 00530a7c ["INT_ADD", "register:40f0:8", ["const:530a7c:8", "const:4:8"]]
+ 00530a7c ["CALL", null, ["callee:00c57e90:8"]]
- 00530a3c bytes 159c1c94
+ 00530a7c bytes 059d1c94
- 00530a44 ["INT_ADD", "register:40f0:8", ["const:530a44:8", "const:4:8"]]
- 00530a44 ["CALL", null, ["callee:004cb72c:8"]]
+ 00530a84 ["INT_ADD", "register:40f0:8", ["const:530a84:8", "const:4:8"]]
+ 00530a84 ["CALL", null, ["callee:004cb72c:8"]]
- 00530a44 bytes 2a6bfe97
+ 00530a84 bytes 2a6bfe97
~~~


<a id="compare-512dff182681a2df2bb6f8ab42952934"></a>

### [`00530bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md) → [`00530c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md) FUN_00530c14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cb8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb8e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md#insn-00530be4) · [`00530bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md#insn-00530bec)
- 新版 [`00530c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md#insn-00530c24) · [`00530c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md#insn-00530c2c)

~~~diff
- 00530be4 ["INT_ADD", "register:40f0:8", ["const:530be4:8", "const:4:8"]]
- 00530be4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00530c24 ["INT_ADD", "register:40f0:8", ["const:530c24:8", "const:4:8"]]
+ 00530c24 ["CALL", null, ["callee:00c57e90:8"]]
- 00530be4 bytes ab9b1c94
+ 00530c24 bytes 9b9c1c94
- 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
- 00530bec ["CALL", null, ["callee:004cb8e8:8"]]
+ 00530c2c ["INT_ADD", "register:40f0:8", ["const:530c2c:8", "const:4:8"]]
+ 00530c2c ["CALL", null, ["callee:004cb8e8:8"]]
- 00530bec bytes 2f6bfe97
+ 00530c2c bytes 2f6bfe97
~~~


<a id="compare-11b9898d7d143d24e85a55b0c2c993f9"></a>

### [`00530d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md) → [`00530dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md) FUN_00530dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004cba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004cba9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md#insn-00530d8c) · [`00530d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md#insn-00530d94)
- 新版 [`00530dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md#insn-00530dcc) · [`00530dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md#insn-00530dd4)

~~~diff
- 00530d8c ["INT_ADD", "register:40f0:8", ["const:530d8c:8", "const:4:8"]]
- 00530d8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00530dcc ["INT_ADD", "register:40f0:8", ["const:530dcc:8", "const:4:8"]]
+ 00530dcc ["CALL", null, ["callee:00c57e90:8"]]
- 00530d8c bytes 419b1c94
+ 00530dcc bytes 319c1c94
- 00530d94 ["INT_ADD", "register:40f0:8", ["const:530d94:8", "const:4:8"]]
- 00530d94 ["CALL", null, ["callee:004cba9c:8"]]
+ 00530dd4 ["INT_ADD", "register:40f0:8", ["const:530dd4:8", "const:4:8"]]
+ 00530dd4 ["CALL", null, ["callee:004cba9c:8"]]
- 00530d94 bytes 326bfe97
+ 00530dd4 bytes 326bfe97
~~~


<a id="compare-765f84247792382ab71f8995ef249d44"></a>

### [`00530de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530de4.md) → [`00530e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md) FUN_00530e24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00530e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530de4.md#insn-00530e00) · [`00530e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530de4.md#insn-00530e38) · [`00530e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530de4.md#insn-00530e48)
- 新版 [`00530e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e40) · [`00530e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e78) · [`00530e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530e24.md#insn-00530e88)

~~~diff
- 00530e00 ["INT_ADD", "register:40f0:8", ["const:530e00:8", "const:4:8"]]
- 00530e00 ["CALL", null, ["callee:0053b424:8"]]
+ 00530e40 ["INT_ADD", "register:40f0:8", ["const:530e40:8", "const:4:8"]]
+ 00530e40 ["CALL", null, ["callee:0053b424:8"]]
- 00530e00 bytes 79290094
+ 00530e40 bytes 79290094
- 00530e38 ["INT_ADD", "register:40f0:8", ["const:530e38:8", "const:4:8"]]
- 00530e38 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00530e78 ["INT_ADD", "register:40f0:8", ["const:530e78:8", "const:4:8"]]
+ 00530e78 ["CALL", null, ["callee:00c57eb0:8"]]
- 00530e38 bytes 1e9b1c94
+ 00530e78 bytes 0e9c1c94
- 00530e48 ["INT_ADD", "register:40f0:8", ["const:530e48:8", "const:4:8"]]
- 00530e48 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00530e88 ["INT_ADD", "register:40f0:8", ["const:530e88:8", "const:4:8"]]
+ 00530e88 ["CALL", null, ["callee:00c57eb0:8"]]
- 00530e48 bytes 1a9b1c94
+ 00530e88 bytes 0a9c1c94
~~~


<a id="compare-88a349b04227cf542fca2d2356fee25a"></a>

### [`00531290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531290.md) → [`005312d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005312d0.md) FUN_005312d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005312b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531290.md#insn-005312b0)
- 新版 [`005312f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005312d0.md#insn-005312f0)

~~~diff
- 005312b0 ["INT_ADD", "register:40f0:8", ["const:5312b0:8", "const:4:8"]]
- 005312b0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005312f0 ["INT_ADD", "register:40f0:8", ["const:5312f0:8", "const:4:8"]]
+ 005312f0 ["CALL", null, ["callee:00c57eb0:8"]]
- 005312b0 bytes 009a1c94
+ 005312f0 bytes f09a1c94
~~~


<a id="compare-0866297b4ea6f450c372751a44b0c271"></a>

### [`00531498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531498.md) → [`005314d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005314d8.md) FUN_005314d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005314b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531498.md#insn-005314b8)
- 新版 [`005314f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005314d8.md#insn-005314f8)

~~~diff
- 005314b8 ["INT_ADD", "register:40f0:8", ["const:5314b8:8", "const:4:8"]]
- 005314b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005314f8 ["INT_ADD", "register:40f0:8", ["const:5314f8:8", "const:4:8"]]
+ 005314f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005314b8 bytes 7e991c94
+ 005314f8 bytes 6e9a1c94
~~~


<a id="compare-ded0814a66f64478796e9c0b259548f8"></a>

### [`005314dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314dc.md) → [`0053151c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md) FUN_0053151c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005314f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314dc.md#insn-005314f4) · [`00531500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005314dc.md#insn-00531500)
- 新版 [`00531534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md#insn-00531534) · [`00531540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/0053151c.md#insn-00531540)

~~~diff
- 005314f4 ["INT_ADD", "register:40f0:8", ["const:5314f4:8", "const:4:8"]]
- 005314f4 ["CALL", null, ["callee:0053af90:8"]]
+ 00531534 ["INT_ADD", "register:40f0:8", ["const:531534:8", "const:4:8"]]
+ 00531534 ["CALL", null, ["callee:0053af90:8"]]
- 005314f4 bytes 97260094
+ 00531534 bytes 97260094
- 00531500 ["INT_ADD", "register:40f0:8", ["const:531500:8", "const:4:8"]]
- 00531500 ["CALL", null, ["callee:0046d490:8"]]
+ 00531540 ["INT_ADD", "register:40f0:8", ["const:531540:8", "const:4:8"]]
+ 00531540 ["CALL", null, ["callee:0046d490:8"]]
- 00531500 bytes d4effc97
+ 00531540 bytes d4effc97
~~~


<a id="compare-05446000eaec996437d4c934c765f362"></a>

### [`00531664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531664.md) → [`005316a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316a4.md) FUN_005316a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053167c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531664.md#insn-0053167c)
- 新版 [`005316bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316a4.md#insn-005316bc)

~~~diff
- 0053167c ["INT_ADD", "register:40f0:8", ["const:53167c:8", "const:4:8"]]
- 0053167c ["CALL", null, ["callee:0053af90:8"]]
+ 005316bc ["INT_ADD", "register:40f0:8", ["const:5316bc:8", "const:4:8"]]
+ 005316bc ["CALL", null, ["callee:0053af90:8"]]
- 0053167c bytes 35260094
+ 005316bc bytes 35260094
~~~


<a id="compare-dceba7e1ca8296d7df46d6c174f28876"></a>

### [`00531694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531694.md) → [`005316d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md) FUN_005316d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005316ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531694.md#insn-005316ac) · [`005316b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531694.md#insn-005316b8)
- 新版 [`005316ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md#insn-005316ec) · [`005316f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005316d4.md#insn-005316f8)

~~~diff
- 005316ac ["INT_ADD", "register:40f0:8", ["const:5316ac:8", "const:4:8"]]
- 005316ac ["CALL", null, ["callee:0053af90:8"]]
+ 005316ec ["INT_ADD", "register:40f0:8", ["const:5316ec:8", "const:4:8"]]
+ 005316ec ["CALL", null, ["callee:0053af90:8"]]
- 005316ac bytes 29260094
+ 005316ec bytes 29260094
- 005316b8 ["INT_ADD", "register:40f0:8", ["const:5316b8:8", "const:4:8"]]
- 005316b8 ["CALL", null, ["callee:0046d490:8"]]
+ 005316f8 ["INT_ADD", "register:40f0:8", ["const:5316f8:8", "const:4:8"]]
+ 005316f8 ["CALL", null, ["callee:0046d490:8"]]
- 005316b8 bytes 66effc97
+ 005316f8 bytes 66effc97
~~~


<a id="compare-c62e2f4263a90065d961fe676086b3bd"></a>

### [`00531834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531834.md) → [`00531874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531874.md) FUN_00531874

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053184c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531834.md#insn-0053184c)
- 新版 [`0053188c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531874.md#insn-0053188c)

~~~diff
- 0053184c ["INT_ADD", "register:40f0:8", ["const:53184c:8", "const:4:8"]]
- 0053184c ["CALL", null, ["callee:0053af90:8"]]
+ 0053188c ["INT_ADD", "register:40f0:8", ["const:53188c:8", "const:4:8"]]
+ 0053188c ["CALL", null, ["callee:0053af90:8"]]
- 0053184c bytes c1250094
+ 0053188c bytes c1250094
~~~


<a id="compare-cfbbfafb331e7c4c8ab3a9a045b2003d"></a>

### [`00531864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531864.md) → [`005318a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md) FUN_005318a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531864.md#insn-0053187c) · [`00531888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531864.md#insn-00531888)
- 新版 [`005318bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md#insn-005318bc) · [`005318c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/005318a4.md#insn-005318c8)

~~~diff
- 0053187c ["INT_ADD", "register:40f0:8", ["const:53187c:8", "const:4:8"]]
- 0053187c ["CALL", null, ["callee:0053af90:8"]]
+ 005318bc ["INT_ADD", "register:40f0:8", ["const:5318bc:8", "const:4:8"]]
+ 005318bc ["CALL", null, ["callee:0053af90:8"]]
- 0053187c bytes b5250094
+ 005318bc bytes b5250094
- 00531888 ["INT_ADD", "register:40f0:8", ["const:531888:8", "const:4:8"]]
- 00531888 ["CALL", null, ["callee:0046d490:8"]]
+ 005318c8 ["INT_ADD", "register:40f0:8", ["const:5318c8:8", "const:4:8"]]
+ 005318c8 ["CALL", null, ["callee:0046d490:8"]]
- 00531888 bytes f2eefc97
+ 005318c8 bytes f2eefc97
~~~


<a id="compare-e4f1d5874049c9d9bf2496df40762d3e"></a>

### [`00531acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531acc.md) → [`00531b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b0c.md) FUN_00531b0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531acc.md#insn-00531b14)
- 新版 [`00531b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b0c.md#insn-00531b54)

~~~diff
- 00531b14 ["INT_ADD", "register:40f0:8", ["const:531b14:8", "const:4:8"]]
- 00531b14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531b54 ["INT_ADD", "register:40f0:8", ["const:531b54:8", "const:4:8"]]
+ 00531b54 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531b14 bytes e7971c94
+ 00531b54 bytes d7981c94
~~~


<a id="compare-c7f13605a8f7338039d6acdb397489c7"></a>

### [`00531b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md) → [`00531b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md) FUN_00531b84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0050f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md#insn-00531b8c) · [`00531b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md#insn-00531b9c)
- 新版 [`00531bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md#insn-00531bcc) · [`00531bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md#insn-00531bdc)

~~~diff
- 00531b8c ["INT_ADD", "register:40f0:8", ["const:531b8c:8", "const:4:8"]]
- 00531b8c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531bcc ["INT_ADD", "register:40f0:8", ["const:531bcc:8", "const:4:8"]]
+ 00531bcc ["CALL", null, ["callee:00c57eb0:8"]]
- 00531b8c bytes c9971c94
+ 00531bcc bytes b9981c94
- 00531b9c ["INT_ADD", "register:40f0:8", ["const:531b9c:8", "const:4:8"]]
- 00531b9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531bdc ["INT_ADD", "register:40f0:8", ["const:531bdc:8", "const:4:8"]]
+ 00531bdc ["CALL", null, ["callee:00c57eb0:8"]]
- 00531b9c bytes c5971c94
+ 00531bdc bytes b5981c94
~~~


<a id="compare-76fb7196923371198143de2328a13ed4"></a>

### [`00531cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cf4.md) → [`00531d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md) FUN_00531d34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531cf4.md#insn-00531d08)
- 新版 [`00531d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531d34.md#insn-00531d48)

~~~diff
- 00531d08 ["INT_ADD", "register:40f0:8", ["const:531d08:8", "const:4:8"]]
- 00531d08 ["CALL", null, ["callee:0051acc4:8"]]
+ 00531d48 ["INT_ADD", "register:40f0:8", ["const:531d48:8", "const:4:8"]]
+ 00531d48 ["CALL", null, ["callee:0051acc4:8"]]
- 00531d08 bytes dfa3ff97
+ 00531d48 bytes dfa3ff97
~~~


<a id="compare-e05fb2dfb88016f2345255dae595183c"></a>

### [`00531f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531f3c.md) → [`00531f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531f7c.md) FUN_00531f7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531f3c.md#insn-00531f84)
- 新版 [`00531fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531f7c.md#insn-00531fc4)

~~~diff
- 00531f84 ["INT_ADD", "register:40f0:8", ["const:531f84:8", "const:4:8"]]
- 00531f84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00531fc4 ["INT_ADD", "register:40f0:8", ["const:531fc4:8", "const:4:8"]]
+ 00531fc4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00531f84 bytes cb961c94
+ 00531fc4 bytes bb971c94
~~~


<a id="compare-b66b9c442f71fa6d02b5edd60890271a"></a>

### [`00531fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531fb4.md) → [`00531ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md) FUN_00531ff4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00531ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531fb4.md#insn-00531ffc) · [`0053200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531fb4.md#insn-0053200c)
- 新版 [`0053203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md#insn-0053203c) · [`0053204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531ff4.md#insn-0053204c)

~~~diff
- 00531ffc ["INT_ADD", "register:40f0:8", ["const:531ffc:8", "const:4:8"]]
- 00531ffc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053203c ["INT_ADD", "register:40f0:8", ["const:53203c:8", "const:4:8"]]
+ 0053203c ["CALL", null, ["callee:00c57eb0:8"]]
- 00531ffc bytes ad961c94
+ 0053203c bytes 9d971c94
- 0053200c ["INT_ADD", "register:40f0:8", ["const:53200c:8", "const:4:8"]]
- 0053200c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053204c ["INT_ADD", "register:40f0:8", ["const:53204c:8", "const:4:8"]]
+ 0053204c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053200c bytes a9961c94
+ 0053204c bytes 99971c94
~~~


<a id="compare-d85b548f482d0668b4a05e0804836fe9"></a>

### [`005321f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005321f4.md) → [`00532234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md) FUN_00532234

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005321f4.md#insn-00532240) · [`00532250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005321f4.md#insn-00532250)
- 新版 [`00532280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md#insn-00532280) · [`00532290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532234.md#insn-00532290)

~~~diff
- 00532240 ["INT_ADD", "register:40f0:8", ["const:532240:8", "const:4:8"]]
- 00532240 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00532280 ["INT_ADD", "register:40f0:8", ["const:532280:8", "const:4:8"]]
+ 00532280 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532240 bytes 1c961c94
+ 00532280 bytes 0c971c94
- 00532250 ["INT_ADD", "register:40f0:8", ["const:532250:8", "const:4:8"]]
- 00532250 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00532290 ["INT_ADD", "register:40f0:8", ["const:532290:8", "const:4:8"]]
+ 00532290 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532250 bytes 18961c94
+ 00532290 bytes 08971c94
~~~


<a id="compare-eb2bcc9a3ea3d66d513c53f896e4819b"></a>

### [`00532280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532280.md) → [`005322c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md) FUN_005322c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005322cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532280.md#insn-005322cc) · [`005322dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532280.md#insn-005322dc) · [`005322ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532280.md#insn-005322ec)
- 新版 [`0053230c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053230c) · [`0053231c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053231c) · [`0053232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005322c0.md#insn-0053232c)

~~~diff
- 005322cc ["INT_ADD", "register:40f0:8", ["const:5322cc:8", "const:4:8"]]
- 005322cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053230c ["INT_ADD", "register:40f0:8", ["const:53230c:8", "const:4:8"]]
+ 0053230c ["CALL", null, ["callee:00c57eb0:8"]]
- 005322cc bytes f9951c94
+ 0053230c bytes e9961c94
- 005322dc ["INT_ADD", "register:40f0:8", ["const:5322dc:8", "const:4:8"]]
- 005322dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053231c ["INT_ADD", "register:40f0:8", ["const:53231c:8", "const:4:8"]]
+ 0053231c ["CALL", null, ["callee:00c57eb0:8"]]
- 005322dc bytes f5951c94
+ 0053231c bytes e5961c94
- 005322ec ["INT_ADD", "register:40f0:8", ["const:5322ec:8", "const:4:8"]]
- 005322ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053232c ["INT_ADD", "register:40f0:8", ["const:53232c:8", "const:4:8"]]
+ 0053232c ["CALL", null, ["callee:00c57eb0:8"]]
- 005322ec bytes f1951c94
+ 0053232c bytes e1961c94
~~~


<a id="compare-be2778542b75f14cd4eed019e9fea2d6"></a>

### [`00532680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532680.md) → [`005326c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md) FUN_005326c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005326cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532680.md#insn-005326cc) · [`005326dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532680.md#insn-005326dc) · [`00532704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532680.md#insn-00532704)
- 新版 [`0053270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-0053270c) · [`0053271c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-0053271c) · [`00532744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/005326c0.md#insn-00532744)

~~~diff
- 005326cc ["INT_ADD", "register:40f0:8", ["const:5326cc:8", "const:4:8"]]
- 005326cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053270c ["INT_ADD", "register:40f0:8", ["const:53270c:8", "const:4:8"]]
+ 0053270c ["CALL", null, ["callee:00c57eb0:8"]]
- 005326cc bytes f9941c94
+ 0053270c bytes e9951c94
- 005326dc ["INT_ADD", "register:40f0:8", ["const:5326dc:8", "const:4:8"]]
- 005326dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053271c ["INT_ADD", "register:40f0:8", ["const:53271c:8", "const:4:8"]]
+ 0053271c ["CALL", null, ["callee:00c57eb0:8"]]
- 005326dc bytes f5941c94
+ 0053271c bytes e5951c94
- 00532704 ["INT_ADD", "register:40f0:8", ["const:532704:8", "const:4:8"]]
- 00532704 ["CALL", null, ["callee:0053af90:8"]]
+ 00532744 ["INT_ADD", "register:40f0:8", ["const:532744:8", "const:4:8"]]
+ 00532744 ["CALL", null, ["callee:0053af90:8"]]
- 00532704 bytes 13220094
+ 00532744 bytes 13220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be71235a4c78442539dc7228ec39211f"></a>

### [`0053274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053274c.md) → [`0053278c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md) FUN_0053278c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053274c.md#insn-00532798) · [`005327a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053274c.md#insn-005327a8) · [`005327d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/0053274c.md#insn-005327d0)
- 新版 [`005327d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-005327d8) · [`005327e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-005327e8) · [`00532810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/0053278c.md#insn-00532810)

~~~diff
- 00532798 ["INT_ADD", "register:40f0:8", ["const:532798:8", "const:4:8"]]
- 00532798 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005327d8 ["INT_ADD", "register:40f0:8", ["const:5327d8:8", "const:4:8"]]
+ 005327d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532798 bytes c6941c94
+ 005327d8 bytes b6951c94
- 005327a8 ["INT_ADD", "register:40f0:8", ["const:5327a8:8", "const:4:8"]]
- 005327a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005327e8 ["INT_ADD", "register:40f0:8", ["const:5327e8:8", "const:4:8"]]
+ 005327e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005327a8 bytes c2941c94
+ 005327e8 bytes b2951c94
- 005327d0 ["INT_ADD", "register:40f0:8", ["const:5327d0:8", "const:4:8"]]
- 005327d0 ["CALL", null, ["callee:0053af90:8"]]
+ 00532810 ["INT_ADD", "register:40f0:8", ["const:532810:8", "const:4:8"]]
+ 00532810 ["CALL", null, ["callee:0053af90:8"]]
- 005327d0 bytes e0210094
+ 00532810 bytes e0210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20c4d85128c887fdba63d82714bf9a85"></a>

### [`00532820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532820.md) → [`00532860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532860.md) FUN_00532860

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532820.md#insn-00532838)
- 新版 [`00532878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532860.md#insn-00532878)

~~~diff
- 00532838 ["INT_ADD", "register:40f0:8", ["const:532838:8", "const:4:8"]]
- 00532838 ["CALL", null, ["callee:0053af90:8"]]
+ 00532878 ["INT_ADD", "register:40f0:8", ["const:532878:8", "const:4:8"]]
+ 00532878 ["CALL", null, ["callee:0053af90:8"]]
- 00532838 bytes c6210094
+ 00532878 bytes c6210094
~~~


<a id="compare-0006681e7aa5f85c8c03d0694259ba95"></a>

### [`00532850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532850.md) → [`00532890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md) FUN_00532890

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532850.md#insn-00532868) · [`00532874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532850.md#insn-00532874)
- 新版 [`005328a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md#insn-005328a8) · [`005328b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532890.md#insn-005328b4)

~~~diff
- 00532868 ["INT_ADD", "register:40f0:8", ["const:532868:8", "const:4:8"]]
- 00532868 ["CALL", null, ["callee:0053af90:8"]]
+ 005328a8 ["INT_ADD", "register:40f0:8", ["const:5328a8:8", "const:4:8"]]
+ 005328a8 ["CALL", null, ["callee:0053af90:8"]]
- 00532868 bytes ba210094
+ 005328a8 bytes ba210094
- 00532874 ["INT_ADD", "register:40f0:8", ["const:532874:8", "const:4:8"]]
- 00532874 ["CALL", null, ["callee:0046d490:8"]]
+ 005328b4 ["INT_ADD", "register:40f0:8", ["const:5328b4:8", "const:4:8"]]
+ 005328b4 ["CALL", null, ["callee:0046d490:8"]]
- 00532874 bytes f7eafc97
+ 005328b4 bytes f7eafc97
~~~


<a id="compare-33c711fd60e63f554bec9982c9fce379"></a>

### [`005329e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005329e0.md) → [`00532a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a20.md) FUN_00532a20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005329f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/005329e0.md#insn-005329f8)
- 新版 [`00532a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a20.md#insn-00532a38)

~~~diff
- 005329f8 ["INT_ADD", "register:40f0:8", ["const:5329f8:8", "const:4:8"]]
- 005329f8 ["CALL", null, ["callee:0053af90:8"]]
+ 00532a38 ["INT_ADD", "register:40f0:8", ["const:532a38:8", "const:4:8"]]
+ 00532a38 ["CALL", null, ["callee:0053af90:8"]]
- 005329f8 bytes 56210094
+ 00532a38 bytes 56210094
~~~


<a id="compare-c734f6e169ec37ed834df6f7ccd2279d"></a>

### [`00532a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532a10.md) → [`00532a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md) FUN_00532a50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532a10.md#insn-00532a28) · [`00532a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532a10.md#insn-00532a34)
- 新版 [`00532a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md#insn-00532a68) · [`00532a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532a50.md#insn-00532a74)

~~~diff
- 00532a28 ["INT_ADD", "register:40f0:8", ["const:532a28:8", "const:4:8"]]
- 00532a28 ["CALL", null, ["callee:0053af90:8"]]
+ 00532a68 ["INT_ADD", "register:40f0:8", ["const:532a68:8", "const:4:8"]]
+ 00532a68 ["CALL", null, ["callee:0053af90:8"]]
- 00532a28 bytes 4a210094
+ 00532a68 bytes 4a210094
- 00532a34 ["INT_ADD", "register:40f0:8", ["const:532a34:8", "const:4:8"]]
- 00532a34 ["CALL", null, ["callee:0046d490:8"]]
+ 00532a74 ["INT_ADD", "register:40f0:8", ["const:532a74:8", "const:4:8"]]
+ 00532a74 ["CALL", null, ["callee:0046d490:8"]]
- 00532a34 bytes 87eafc97
+ 00532a74 bytes 87eafc97
~~~


<a id="compare-e845d00543be6f1734db0ec09cbc3670"></a>

### [`00532bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532bcc.md) → [`00532c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md) FUN_00532c0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532bcc.md#insn-00532c54) · [`00532c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532bcc.md#insn-00532c8c) · [`00532cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532bcc.md#insn-00532cb0)
- 新版 [`00532c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532c94) · [`00532ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532ccc) · [`00532cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532c0c.md#insn-00532cf0)

~~~diff
- 00532c54 ["INT_ADD", "register:40f0:8", ["const:532c54:8", "const:4:8"]]
- 00532c54 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532c94 ["INT_ADD", "register:40f0:8", ["const:532c94:8", "const:4:8"]]
+ 00532c94 ["CALL", null, ["callee:00c57e90:8"]]
- 00532c54 bytes 8f931c94
+ 00532c94 bytes 7f941c94
- 00532c8c ["INT_ADD", "register:40f0:8", ["const:532c8c:8", "const:4:8"]]
- 00532c8c ["CALL", null, ["callee:0043bba4:8"]]
+ 00532ccc ["INT_ADD", "register:40f0:8", ["const:532ccc:8", "const:4:8"]]
+ 00532ccc ["CALL", null, ["callee:0043bba4:8"]]
- 00532c8c bytes b623fc97
+ 00532ccc bytes b623fc97
- 00532cb0 ["INT_ADD", "register:40f0:8", ["const:532cb0:8", "const:4:8"]]
- 00532cb0 ["CALL", null, ["callee:005408bc:8"]]
+ 00532cf0 ["INT_ADD", "register:40f0:8", ["const:532cf0:8", "const:4:8"]]
+ 00532cf0 ["CALL", null, ["callee:005408bc:8"]]
- 00532cb0 bytes f3360094
+ 00532cf0 bytes f3360094
~~~


<a id="compare-93a0345b64dbeec44d03992d2dee815c"></a>

### [`00532cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cb4.md) → [`00532cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532cf4.md) FUN_00532cf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cb4.md#insn-00532cd0)
- 新版 [`00532d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532cf4.md#insn-00532d10)

~~~diff
- 00532cd0 ["INT_ADD", "register:40f0:8", ["const:532cd0:8", "const:4:8"]]
- 00532cd0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00532d10 ["INT_ADD", "register:40f0:8", ["const:532d10:8", "const:4:8"]]
+ 00532d10 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532cd0 bytes 78931c94
+ 00532d10 bytes 68941c94
~~~


<a id="compare-3505e177d939556bc4d0b587726b3f50"></a>

### [`00532cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cf8.md) → [`00532d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md) FUN_00532d38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cf8.md#insn-00532d14) · [`00532d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532cf8.md#insn-00532d24)
- 新版 [`00532d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md#insn-00532d54) · [`00532d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532d38.md#insn-00532d64)

~~~diff
- 00532d14 ["INT_ADD", "register:40f0:8", ["const:532d14:8", "const:4:8"]]
- 00532d14 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00532d54 ["INT_ADD", "register:40f0:8", ["const:532d54:8", "const:4:8"]]
+ 00532d54 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532d14 bytes 67931c94
+ 00532d54 bytes 57941c94
- 00532d24 ["INT_ADD", "register:40f0:8", ["const:532d24:8", "const:4:8"]]
- 00532d24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00532d64 ["INT_ADD", "register:40f0:8", ["const:532d64:8", "const:4:8"]]
+ 00532d64 ["CALL", null, ["callee:00c57eb0:8"]]
- 00532d24 bytes 63931c94
+ 00532d64 bytes 53941c94
~~~


<a id="compare-eb43ec5115eb557597c8299c435de9b6"></a>

### [`00532f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md) → [`00532f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md) FUN_00532f4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f0c.md#insn-00532f1c)
- 新版 [`00532f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f4c.md#insn-00532f5c)

~~~diff
- 00532f1c ["INT_ADD", "register:40f0:8", ["const:532f1c:8", "const:4:8"]]
- 00532f1c ["CALL", null, ["callee:00532e7c:8"]]
+ 00532f5c ["INT_ADD", "register:40f0:8", ["const:532f5c:8", "const:4:8"]]
+ 00532f5c ["CALL", null, ["callee:00532e7c:8"]]
- 00532f1c bytes c8ffff97
+ 00532f5c bytes c8ffff97
~~~


<a id="compare-e82061902a5d30949b15362df9ae31af"></a>

### [`00532f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md) → [`00532f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md) FUN_00532f70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053ff60.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053ffa0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00532f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md#insn-00532f44) · [`00532f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f30.md#insn-00532f50)
- 新版 [`00532f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md#insn-00532f84) · [`00532f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532f70.md#insn-00532f90)

~~~diff
- 00532f44 ["INT_ADD", "register:40f0:8", ["const:532f44:8", "const:4:8"]]
- 00532f44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00532f84 ["INT_ADD", "register:40f0:8", ["const:532f84:8", "const:4:8"]]
+ 00532f84 ["CALL", null, ["callee:00c57e90:8"]]
- 00532f44 bytes d3921c94
+ 00532f84 bytes c3931c94
- 00532f50 ["INT_ADD", "register:40f0:8", ["const:532f50:8", "const:4:8"]]
- 00532f50 ["CALL", null, ["callee:0053ffa0:8"]]
+ 00532f90 ["INT_ADD", "register:40f0:8", ["const:532f90:8", "const:4:8"]]
+ 00532f90 ["CALL", null, ["callee:0053ffa0:8"]]
- 00532f50 bytes 04340094
+ 00532f90 bytes 04340094
~~~


<a id="compare-acc773ee0a58b0dfb2d3ee57bce86266"></a>

### [`005330ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md) → [`0053312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md) FUN_0053312c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00532fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005330fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/005330ec.md#insn-005330fc)
- 新版 [`0053313c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/0053312c.md#insn-0053313c)

~~~diff
- 005330fc ["INT_ADD", "register:40f0:8", ["const:5330fc:8", "const:4:8"]]
- 005330fc ["CALL", null, ["callee:00532fb8:8"]]
+ 0053313c ["INT_ADD", "register:40f0:8", ["const:53313c:8", "const:4:8"]]
+ 0053313c ["CALL", null, ["callee:00532fb8:8"]]
- 005330fc bytes 9fffff97
+ 0053313c bytes 9fffff97
~~~


<a id="compare-426e92e90a1699d29cdc459f2435a2f3"></a>

### [`00533110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533110.md) → [`00533150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md) FUN_00533150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053312c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533110.md#insn-0053312c) · [`0053313c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533110.md#insn-0053313c)
- 新版 [`0053316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md#insn-0053316c) · [`0053317c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533150.md#insn-0053317c)

~~~diff
- 0053312c ["INT_ADD", "register:40f0:8", ["const:53312c:8", "const:4:8"]]
- 0053312c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053316c ["INT_ADD", "register:40f0:8", ["const:53316c:8", "const:4:8"]]
+ 0053316c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053312c bytes 61921c94
+ 0053316c bytes 51931c94
- 0053313c ["INT_ADD", "register:40f0:8", ["const:53313c:8", "const:4:8"]]
- 0053313c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
+ 0053317c ["CALL", null, ["callee:00c57eb0:8"]]
- 0053313c bytes 5d921c94
+ 0053317c bytes 4d931c94
~~~


<a id="compare-732e85cff2311ae7a5ed3f67d31216d7"></a>

### [`00533150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533150.md) → [`00533190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md) FUN_00533190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0053316c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533150.md#insn-0053316c) · [`0053317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533150.md#insn-0053317c)
- 新版 [`005331ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md#insn-005331ac) · [`005331bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/00533190.md#insn-005331bc)

~~~diff
- 0053316c ["INT_ADD", "register:40f0:8", ["const:53316c:8", "const:4:8"]]
- 0053316c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
+ 005331ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0053316c bytes 51921c94
+ 005331ac bytes 41931c94
- 0053317c ["INT_ADD", "register:40f0:8", ["const:53317c:8", "const:4:8"]]
- 0053317c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005331bc ["INT_ADD", "register:40f0:8", ["const:5331bc:8", "const:4:8"]]
+ 005331bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0053317c bytes 4d921c94
+ 005331bc bytes 3d931c94
~~~


<a id="compare-f64a58e136b68bb91c8f4b3383daeead"></a>

### [`00533190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533190.md) → [`005331d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005331d0.md) FUN_005331d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005331ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00533/00533190.md#insn-005331ac)
- 新版 [`005331ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00533/005331d0.md#insn-005331ec)

~~~diff
- 005331ac ["INT_ADD", "register:40f0:8", ["const:5331ac:8", "const:4:8"]]
- 005331ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 005331ec ["INT_ADD", "register:40f0:8", ["const:5331ec:8", "const:4:8"]]
+ 005331ec ["CALL", null, ["callee:00c57eb0:8"]]
- 005331ac bytes 41921c94
+ 005331ec bytes 31931c94
~~~


