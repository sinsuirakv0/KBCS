# v16.0.1 → v16.0.2 · 要調査の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-a6a1285caea4d351fe075b852e3c065b"></a>

### [`00c2b53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b53c.md) → [`00c2b5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b5d8.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b5ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b648.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b53c.md#insn-00c2b588)
- 新版 `00c2b624`（命令位置の公開資料なし）

~~~diff
- 00c2b588 ["INT_ADD", "register:40f0:8", ["const:c2b588:8", "const:4:8"]]
- 00c2b588 ["CALL", null, ["callee:00c2b648:8"]]
+ 00c2b624 ["INT_ADD", "register:40f0:8", ["const:c2b624:8", "const:4:8"]]
+ 00c2b624 ["CALL", null, ["callee:00c2b648:8"]]
- 00c2b588 bytes 09000094
+ 00c2b624 bytes 09000094
~~~


<a id="compare-52c8bd7c6917694803d608549cc13e3c"></a>

### [`00c2b7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b7d4.md) → [`00c2b870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b870.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b844.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b7d4.md#insn-00c2b820)
- 新版 `00c2b8bc`（命令位置の公開資料なし）

~~~diff
- 00c2b820 ["INT_ADD", "register:40f0:8", ["const:c2b820:8", "const:4:8"]]
- 00c2b820 ["CALL", null, ["callee:00c2b8e0:8"]]
+ 00c2b8bc ["INT_ADD", "register:40f0:8", ["const:c2b8bc:8", "const:4:8"]]
+ 00c2b8bc ["CALL", null, ["callee:00c2b8e0:8"]]
- 00c2b820 bytes 09000094
+ 00c2b8bc bytes 09000094
~~~


<a id="compare-3c05498d82a6ddf1d689eea7f66ed754"></a>

### [`00c2bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bb34.md) → [`00c2bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bbd0.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28cdc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c28d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c28d78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bb34.md#insn-00c2bb80)
- 新版 `00c2bc1c`（命令位置の公開資料なし）

~~~diff
- 00c2bb80 ["INT_ADD", "register:40f0:8", ["const:c2bb80:8", "const:4:8"]]
- 00c2bb80 ["CALL", null, ["callee:00c28d78:8"]]
+ 00c2bc1c ["INT_ADD", "register:40f0:8", ["const:c2bc1c:8", "const:4:8"]]
+ 00c2bc1c ["CALL", null, ["callee:00c28d78:8"]]
- 00c2bb80 bytes 57f4ff97
+ 00c2bc1c bytes 57f4ff97
~~~


<a id="compare-e4a54225596d9dca7a96bea0b88d2680"></a>

### [`00c2bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bba4.md) → [`00c2bc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bc40.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c28fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c28/00c28fa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c29/00c2903c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bba4.md#insn-00c2bbf0)
- 新版 `00c2bc8c`（命令位置の公開資料なし）

~~~diff
- 00c2bbf0 ["INT_ADD", "register:40f0:8", ["const:c2bbf0:8", "const:4:8"]]
- 00c2bbf0 ["CALL", null, ["callee:00c2903c:8"]]
+ 00c2bc8c ["INT_ADD", "register:40f0:8", ["const:c2bc8c:8", "const:4:8"]]
+ 00c2bc8c ["CALL", null, ["callee:00c2903c:8"]]
- 00c2bbf0 bytes ecf4ff97
+ 00c2bc8c bytes ecf4ff97
~~~


<a id="compare-b69be4fe4f579554bc1ebc6e3dcc2723"></a>

### [`00c2bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bc78.md) → [`00c2bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd14.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b5ac.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b648.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bc78.md#insn-00c2bcc4)
- 新版 `00c2bd60`（命令位置の公開資料なし）

~~~diff
- 00c2bcc4 ["INT_ADD", "register:40f0:8", ["const:c2bcc4:8", "const:4:8"]]
- 00c2bcc4 ["CALL", null, ["callee:00c2b648:8"]]
+ 00c2bd60 ["INT_ADD", "register:40f0:8", ["const:c2bd60:8", "const:4:8"]]
+ 00c2bd60 ["CALL", null, ["callee:00c2b648:8"]]
- 00c2bcc4 bytes 3afeff97
+ 00c2bd60 bytes 3afeff97
~~~


<a id="compare-89e11a08e1368bc1f6888a192cd6a290"></a>

### [`00c2bce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bce8.md) → [`00c2bd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bd84.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c2b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b844.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2b8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bd34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bce8.md#insn-00c2bd34)
- 新版 `00c2bdd0`（命令位置の公開資料なし）

~~~diff
- 00c2bd34 ["INT_ADD", "register:40f0:8", ["const:c2bd34:8", "const:4:8"]]
- 00c2bd34 ["CALL", null, ["callee:00c2b8e0:8"]]
+ 00c2bdd0 ["INT_ADD", "register:40f0:8", ["const:c2bdd0:8", "const:4:8"]]
+ 00c2bdd0 ["CALL", null, ["callee:00c2b8e0:8"]]
- 00c2bd34 bytes c4feff97
+ 00c2bdd0 bytes c4feff97
~~~


<a id="compare-e0a4936c76c9c6554d669dd4dab17a07"></a>

### [`00c2bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bdbc.md) → [`00c2be58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be58.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bdbc.md#insn-00c2bdd0)
- 新版 `00c2be6c`（命令位置の公開資料なし）

~~~diff
- 00c2bdd0 ["INT_ADD", "register:40f0:8", ["const:c2bdd0:8", "const:4:8"]]
- 00c2bdd0 ["CALL", null, ["callee:00c5eca0:8"]]
+ 00c2be6c ["INT_ADD", "register:40f0:8", ["const:c2be6c:8", "const:4:8"]]
+ 00c2be6c ["CALL", null, ["callee:00c5eca0:8"]]
- 00c2bdd0 bytes 80cb0094
+ 00c2be6c bytes 8dcb0094
~~~


<a id="compare-35736264641185b943143aa19c57a40f"></a>

### [`00c2bde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bde8.md) → [`00c2be84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2be84.md) _ZNSt6__ndk116__narrow_to_utf8ILm32EED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bde8.md#insn-00c2bdfc)
- 新版 `00c2be98`（命令位置の公開資料なし）

~~~diff
- 00c2bdfc ["INT_ADD", "register:40f0:8", ["const:c2bdfc:8", "const:4:8"]]
- 00c2bdfc ["CALL", null, ["callee:00c5ecb0:8"]]
+ 00c2be98 ["INT_ADD", "register:40f0:8", ["const:c2be98:8", "const:4:8"]]
+ 00c2be98 ["CALL", null, ["callee:00c5ecb0:8"]]
- 00c2bdfc bytes 79cb0094
+ 00c2be98 bytes 86cb0094
~~~


<a id="compare-c07ef15f0d811f68f75cc4733a4ecf17"></a>

### [`00c2be14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be14.md) → [`00c2beb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2beb0.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ebf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ebf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be14.md#insn-00c2be28)
- 新版 `00c2bec4`（命令位置の公開資料なし）

~~~diff
- 00c2be28 ["INT_ADD", "register:40f0:8", ["const:c2be28:8", "const:4:8"]]
- 00c2be28 ["CALL", null, ["callee:00c5ecc0:8"]]
+ 00c2bec4 ["INT_ADD", "register:40f0:8", ["const:c2bec4:8", "const:4:8"]]
+ 00c2bec4 ["CALL", null, ["callee:00c5ecc0:8"]]
- 00c2be28 bytes 72cb0094
+ 00c2bec4 bytes 7fcb0094
~~~


<a id="compare-b1f807d44c9d9f461ac672c1922e8dfb"></a>

### [`00c2be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be40.md) → [`00c2bedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bedc.md) _ZNSt6__ndk117__widen_from_utf8ILm32EED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2be54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2be40.md#insn-00c2be54)
- 新版 `00c2bef0`（命令位置の公開資料なし）

~~~diff
- 00c2be54 ["INT_ADD", "register:40f0:8", ["const:c2be54:8", "const:4:8"]]
- 00c2be54 ["CALL", null, ["callee:00c5ecd0:8"]]
+ 00c2bef0 ["INT_ADD", "register:40f0:8", ["const:c2bef0:8", "const:4:8"]]
+ 00c2bef0 ["CALL", null, ["callee:00c5ecd0:8"]]
- 00c2be54 bytes 6bcb0094
+ 00c2bef0 bytes 78cb0094
~~~


<a id="compare-2efed3cac735f85f546c37cf68abc9c1"></a>

### [`00c2bf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf18.md) → [`00c2bfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bfb4.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ecf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ecf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bf2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf18.md#insn-00c2bf2c)
- 新版 `00c2bfc8`（命令位置の公開資料なし）

~~~diff
- 00c2bf2c ["INT_ADD", "register:40f0:8", ["const:c2bf2c:8", "const:4:8"]]
- 00c2bf2c ["CALL", null, ["callee:00c5ecf0:8"]]
+ 00c2bfc8 ["INT_ADD", "register:40f0:8", ["const:c2bfc8:8", "const:4:8"]]
+ 00c2bfc8 ["CALL", null, ["callee:00c5ecf0:8"]]
- 00c2bf2c bytes 3dcb0094
+ 00c2bfc8 bytes 4acb0094
~~~


<a id="compare-bd1e8eaceb5b3eee7c52bb5bfec148a3"></a>

### [`00c2bf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf94.md) → [`00c2c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c030.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2bfa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bf94.md#insn-00c2bfa8)
- 新版 `00c2c044`（命令位置の公開資料なし）

~~~diff
- 00c2bfa8 ["INT_ADD", "register:40f0:8", ["const:c2bfa8:8", "const:4:8"]]
- 00c2bfa8 ["CALL", null, ["callee:00c5ed10:8"]]
+ 00c2c044 ["INT_ADD", "register:40f0:8", ["const:c2c044:8", "const:4:8"]]
+ 00c2c044 ["CALL", null, ["callee:00c5ed10:8"]]
- 00c2bfa8 bytes 26cb0094
+ 00c2c044 bytes 33cb0094
~~~


<a id="compare-fb99b6ff9b8dce4c12ed35fda6a87a6d"></a>

### [`00c2c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md) → [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) FUN_00c2c130

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c2e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e258.md) [`00c2e364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e364.md) [`00c2e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e470.md) [`00c2e57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e57c.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)
- 新版 呼出元 4件 [`00c2e2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md) [`00c2e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md) [`00c2e50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md) [`00c2e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c0b4) · [`00c2c108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c108) · [`00c2c128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c094.md#insn-00c2c128)
- 新版 `00c2c150`（命令位置の公開資料なし） · `00c2c1a4`（命令位置の公開資料なし） · `00c2c1c4`（命令位置の公開資料なし）

~~~diff
- 00c2c0b4 ["INT_ADD", "register:40f0:8", ["const:c2c0b4:8", "const:4:8"]]
- 00c2c0b4 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00c2c150 ["INT_ADD", "register:40f0:8", ["const:c2c150:8", "const:4:8"]]
+ 00c2c150 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00c2c0b4 bytes d3c70094
+ 00c2c150 bytes e0c70094
- 00c2c108 ["INT_ADD", "register:40f0:8", ["const:c2c108:8", "const:4:8"]]
- 00c2c108 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c2c1a4 ["INT_ADD", "register:40f0:8", ["const:c2c1a4:8", "const:4:8"]]
+ 00c2c1a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00c2c108 bytes 62af0094
+ 00c2c1a4 bytes 6faf0094
- 00c2c128 ["INT_ADD", "register:40f0:8", ["const:c2c128:8", "const:4:8"]]
- 00c2c128 ["CALL", null, ["callee:00c58010:8"]]
+ 00c2c1c4 ["INT_ADD", "register:40f0:8", ["const:c2c1c4:8", "const:4:8"]]
+ 00c2c1c4 ["CALL", null, ["callee:00c58010:8"]]
- 00c2c128 bytes 86af0094
+ 00c2c1c4 bytes 93af0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-494f1b892a1d65f56314ccacfa3e9ef5"></a>

### [`00c2c56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c56c.md) → [`00c2c608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c608.md) _ZNSt6__ndk115numpunct_bynameIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c56c.md#insn-00c2c580)
- 新版 `00c2c61c`（命令位置の公開資料なし）

~~~diff
- 00c2c580 ["INT_ADD", "register:40f0:8", ["const:c2c580:8", "const:4:8"]]
- 00c2c580 ["CALL", null, ["callee:00c5ed40:8"]]
+ 00c2c61c ["INT_ADD", "register:40f0:8", ["const:c2c61c:8", "const:4:8"]]
+ 00c2c61c ["CALL", null, ["callee:00c5ed40:8"]]
- 00c2c580 bytes bcc90094
+ 00c2c61c bytes c9c90094
~~~


<a id="compare-e825d27ecea493692d6aeaf9459e6991"></a>

### [`00c2c598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md) → [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md) FUN_00c2c634

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) [`00c33780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33780.md) [`00c3447c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c3447c.md) · 呼出先 1件 [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 3件 [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) [`00c3381c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md) [`00c34518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md) · 呼出先 1件 [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c598.md#insn-00c2c5ac)
- 新版 `00c2c648`（命令位置の公開資料なし）

~~~diff
- 00c2c5ac ["INT_ADD", "register:40f0:8", ["const:c2c5ac:8", "const:4:8"]]
- 00c2c5ac ["CALL", null, ["callee:00c5d2a0:8"]]
+ 00c2c648 ["INT_ADD", "register:40f0:8", ["const:c2c648:8", "const:4:8"]]
+ 00c2c648 ["CALL", null, ["callee:00c5d2a0:8"]]
- 00c2c5ac bytes 09c30094
+ 00c2c648 bytes 16c30094
~~~


<a id="compare-e0372ada854cb48a9a8349becf6f8110"></a>

### [`00c2c8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c8a4.md) → [`00c2c940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c940.md) _ZNSt6__ndk115numpunct_bynameIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ec90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ec90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2c8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c8a4.md#insn-00c2c8b8)
- 新版 `00c2c954`（命令位置の公開資料なし）

~~~diff
- 00c2c8b8 ["INT_ADD", "register:40f0:8", ["const:c2c8b8:8", "const:4:8"]]
- 00c2c8b8 ["CALL", null, ["callee:00c5ed60:8"]]
+ 00c2c954 ["INT_ADD", "register:40f0:8", ["const:c2c954:8", "const:4:8"]]
+ 00c2c954 ["CALL", null, ["callee:00c5ed60:8"]]
- 00c2c8b8 bytes f6c80094
+ 00c2c954 bytes 03c90094
~~~


<a id="compare-4fdc8221072e63d48b57740957a1559a"></a>

### [`00c2e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e780.md) → [`00c2e81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e81c.md) _ZNSt6__ndk110__time_getD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecc0.md) · 呼出先 1件 [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 1件 [`00c5ed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed90.md) · 呼出先 1件 [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e780.md#insn-00c2e790)
- 新版 `00c2e82c`（命令位置の公開資料なし）

~~~diff
- 00c2e790 ["INT_ADD", "register:40f0:8", ["const:c2e790:8", "const:4:8"]]
- 00c2e790 ["CALL", null, ["callee:00c5d2a0:8"]]
+ 00c2e82c ["INT_ADD", "register:40f0:8", ["const:c2e82c:8", "const:4:8"]]
+ 00c2e82c ["CALL", null, ["callee:00c5d2a0:8"]]
- 00c2e790 bytes 90ba0094
+ 00c2e82c bytes 9dba0094
~~~


<a id="compare-8600cfea2f6150e85c99ad3ac70c2c72"></a>

### [`00c2ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md) → [`00c2ee28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md) FUN_00c2ee28

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2e7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2e7a4.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)
- 新版 呼出元 1件 [`00c2e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c2edec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2edec) · [`00c2edfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2edfc) · [`00c2ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2e/00c2ed8c.md#insn-00c2ee90)
- 新版 `00c2ee88`（命令位置の公開資料なし） · `00c2ee98`（命令位置の公開資料なし） · `00c2ef2c`（命令位置の公開資料なし）

~~~diff
- 00c2edec ["INT_ADD", "register:40f0:8", ["const:c2edec:8", "const:4:8"]]
- 00c2edec ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c2ee88 ["INT_ADD", "register:40f0:8", ["const:c2ee88:8", "const:4:8"]]
+ 00c2ee88 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c2edec bytes 8dac0094
+ 00c2ee88 bytes 9aac0094
- 00c2edfc ["INT_ADD", "register:40f0:8", ["const:c2edfc:8", "const:4:8"]]
- 00c2edfc ["CALL", null, ["callee:00c5e050:8"]]
+ 00c2ee98 ["INT_ADD", "register:40f0:8", ["const:c2ee98:8", "const:4:8"]]
+ 00c2ee98 ["CALL", null, ["callee:00c5e050:8"]]
- 00c2edfc bytes 61bc0094
+ 00c2ee98 bytes 6ebc0094
- 00c2ee90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c2ee90 ["INT_ADD", "register:40f0:8", ["const:c2ee90:8", "const:4:8"]]
- 00c2ee90 ["CALLIND", null, ["register:0:8"]]
+ 00c2ef2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c2ef2c ["INT_ADD", "register:40f0:8", ["const:c2ef2c:8", "const:4:8"]]
+ 00c2ef2c ["CALLIND", null, ["register:0:8"]]
- 00c2ee90 bytes 00013fd6
+ 00c2ef2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7908d9ab267938402b415b9ece42bea6"></a>

### [`00c30744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md) → [`00c307e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md) FUN_00c307e0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c2f09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2f/00c2f09c.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)
- 新版 呼出元 1件 [`00c2f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c307a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c307a4) · [`00c307b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c307b4) · [`00c3085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30744.md#insn-00c3085c)
- 新版 `00c30840`（命令位置の公開資料なし） · `00c30850`（命令位置の公開資料なし） · `00c308f8`（命令位置の公開資料なし）

~~~diff
- 00c307a4 ["INT_ADD", "register:40f0:8", ["const:c307a4:8", "const:4:8"]]
- 00c307a4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c30840 ["INT_ADD", "register:40f0:8", ["const:c30840:8", "const:4:8"]]
+ 00c30840 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c307a4 bytes 1fa60094
+ 00c30840 bytes 2ca60094
- 00c307b4 ["INT_ADD", "register:40f0:8", ["const:c307b4:8", "const:4:8"]]
- 00c307b4 ["CALL", null, ["callee:00c5e050:8"]]
+ 00c30850 ["INT_ADD", "register:40f0:8", ["const:c30850:8", "const:4:8"]]
+ 00c30850 ["CALL", null, ["callee:00c5e050:8"]]
- 00c307b4 bytes f3b50094
+ 00c30850 bytes 00b60094
- 00c3085c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3085c ["INT_ADD", "register:40f0:8", ["const:c3085c:8", "const:4:8"]]
- 00c3085c ["CALLIND", null, ["register:0:8"]]
+ 00c308f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c308f8 ["INT_ADD", "register:40f0:8", ["const:c308f8:8", "const:4:8"]]
+ 00c308f8 ["CALLIND", null, ["register:0:8"]]
- 00c3085c bytes 00013fd6
+ 00c308f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13328e7a462c37380f3b9973a2722239"></a>

### [`00c34c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c30.md) → [`00c34ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ccc.md) FUN_00c34ccc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c30.md#insn-00c34c44)
- 新版 `00c34ce0`（命令位置の公開資料なし）

~~~diff
- 00c34c44 ["INT_ADD", "register:40f0:8", ["const:c34c44:8", "const:4:8"]]
- 00c34c44 ["CALL", null, ["callee:00c5a950:8"]]
+ 00c34ce0 ["INT_ADD", "register:40f0:8", ["const:c34ce0:8", "const:4:8"]]
+ 00c34ce0 ["CALL", null, ["callee:00c5a950:8"]]
- 00c34c44 bytes 0f970094
+ 00c34ce0 bytes 1c970094
~~~


<a id="compare-203770d78ddb16400e57803298fd6d60"></a>

### [`00c34c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c5c.md) → [`00c34cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34cf8.md) FUN_00c34cf8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c5c.md#insn-00c34c70)
- 新版 `00c34d0c`（命令位置の公開資料なし）

~~~diff
- 00c34c70 ["INT_ADD", "register:40f0:8", ["const:c34c70:8", "const:4:8"]]
- 00c34c70 ["CALL", null, ["callee:00c5e830:8"]]
+ 00c34d0c ["INT_ADD", "register:40f0:8", ["const:c34d0c:8", "const:4:8"]]
+ 00c34d0c ["CALL", null, ["callee:00c5e830:8"]]
- 00c34c70 bytes bca60094
+ 00c34d0c bytes c9a60094
~~~


<a id="compare-8a14258b8b9c31a6ba6e2b2d5a2b088a"></a>

### [`00c34c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c88.md) → [`00c34d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d24.md) FUN_00c34d24

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34c88.md#insn-00c34c9c)
- 新版 `00c34d38`（命令位置の公開資料なし）

~~~diff
- 00c34c9c ["INT_ADD", "register:40f0:8", ["const:c34c9c:8", "const:4:8"]]
- 00c34c9c ["CALL", null, ["callee:00c5e850:8"]]
+ 00c34d38 ["INT_ADD", "register:40f0:8", ["const:c34d38:8", "const:4:8"]]
+ 00c34d38 ["CALL", null, ["callee:00c5e850:8"]]
- 00c34c9c bytes b9a60094
+ 00c34d38 bytes c6a60094
~~~


<a id="compare-899a85aeafb0ba30153783d5e75053df"></a>

### [`00c34cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34cb4.md) → [`00c34d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d50.md) FUN_00c34d50

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34cb4.md#insn-00c34cc8)
- 新版 `00c34d64`（命令位置の公開資料なし）

~~~diff
- 00c34cc8 ["INT_ADD", "register:40f0:8", ["const:c34cc8:8", "const:4:8"]]
- 00c34cc8 ["CALL", null, ["callee:00c5a950:8"]]
+ 00c34d64 ["INT_ADD", "register:40f0:8", ["const:c34d64:8", "const:4:8"]]
+ 00c34d64 ["CALL", null, ["callee:00c5a950:8"]]
- 00c34cc8 bytes ee960094
+ 00c34d64 bytes fb960094
~~~


<a id="compare-fa4c454130cbddcac408f813192f4815"></a>

### [`00c34ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ce0.md) → [`00c34d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34d7c.md) FUN_00c34d7c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ce0.md#insn-00c34cf4)
- 新版 `00c34d90`（命令位置の公開資料なし）

~~~diff
- 00c34cf4 ["INT_ADD", "register:40f0:8", ["const:c34cf4:8", "const:4:8"]]
- 00c34cf4 ["CALL", null, ["callee:00c5a950:8"]]
+ 00c34d90 ["INT_ADD", "register:40f0:8", ["const:c34d90:8", "const:4:8"]]
+ 00c34d90 ["CALL", null, ["callee:00c5a950:8"]]
- 00c34cf4 bytes e3960094
+ 00c34d90 bytes f0960094
~~~


<a id="compare-bd0c32379bb889d791ab9d9b64db3dc2"></a>

### [`00c34d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d0c.md) → [`00c34da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34da8.md) FUN_00c34da8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d0c.md#insn-00c34d20)
- 新版 `00c34dbc`（命令位置の公開資料なし）

~~~diff
- 00c34d20 ["INT_ADD", "register:40f0:8", ["const:c34d20:8", "const:4:8"]]
- 00c34d20 ["CALL", null, ["callee:00c5e830:8"]]
+ 00c34dbc ["INT_ADD", "register:40f0:8", ["const:c34dbc:8", "const:4:8"]]
+ 00c34dbc ["CALL", null, ["callee:00c5e830:8"]]
- 00c34d20 bytes 90a60094
+ 00c34dbc bytes 9da60094
~~~


<a id="compare-e1ab42c5ef4c9d0761e4c2041eec372a"></a>

### [`00c34d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d38.md) → [`00c34dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34dd4.md) FUN_00c34dd4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d38.md#insn-00c34d4c)
- 新版 `00c34de8`（命令位置の公開資料なし）

~~~diff
- 00c34d4c ["INT_ADD", "register:40f0:8", ["const:c34d4c:8", "const:4:8"]]
- 00c34d4c ["CALL", null, ["callee:00c5e830:8"]]
+ 00c34de8 ["INT_ADD", "register:40f0:8", ["const:c34de8:8", "const:4:8"]]
+ 00c34de8 ["CALL", null, ["callee:00c5e830:8"]]
- 00c34d4c bytes 85a60094
+ 00c34de8 bytes 92a60094
~~~


<a id="compare-8eac348a848a3624c5c01b1f2cdcfd86"></a>

### [`00c34d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d64.md) → [`00c34e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e00.md) FUN_00c34e00

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d64.md#insn-00c34d78)
- 新版 `00c34e14`（命令位置の公開資料なし）

~~~diff
- 00c34d78 ["INT_ADD", "register:40f0:8", ["const:c34d78:8", "const:4:8"]]
- 00c34d78 ["CALL", null, ["callee:00c5e850:8"]]
+ 00c34e14 ["INT_ADD", "register:40f0:8", ["const:c34e14:8", "const:4:8"]]
+ 00c34e14 ["CALL", null, ["callee:00c5e850:8"]]
- 00c34d78 bytes 82a60094
+ 00c34e14 bytes 8fa60094
~~~


<a id="compare-e4f28fe4b7eb0e478451c7b2c5b7708e"></a>

### [`00c34d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d90.md) → [`00c34e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e2c.md) FUN_00c34e2c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34d90.md#insn-00c34da4)
- 新版 `00c34e40`（命令位置の公開資料なし）

~~~diff
- 00c34da4 ["INT_ADD", "register:40f0:8", ["const:c34da4:8", "const:4:8"]]
- 00c34da4 ["CALL", null, ["callee:00c5e850:8"]]
+ 00c34e40 ["INT_ADD", "register:40f0:8", ["const:c34e40:8", "const:4:8"]]
+ 00c34e40 ["CALL", null, ["callee:00c5e850:8"]]
- 00c34da4 bytes 77a60094
+ 00c34e40 bytes 84a60094
~~~


<a id="compare-94e739dae0f3dc6cc91f8059de81d593"></a>

### [`00c34e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34e7c.md) → [`00c34f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f18.md) FUN_00c34f18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34e7c.md#insn-00c34e90)
- 新版 `00c34f2c`（命令位置の公開資料なし）

~~~diff
- 00c34e90 ["INT_ADD", "register:40f0:8", ["const:c34e90:8", "const:4:8"]]
- 00c34e90 ["CALL", null, ["callee:00c5a950:8"]]
+ 00c34f2c ["INT_ADD", "register:40f0:8", ["const:c34f2c:8", "const:4:8"]]
+ 00c34f2c ["CALL", null, ["callee:00c5a950:8"]]
- 00c34e90 bytes 7c960094
+ 00c34f2c bytes 89960094
~~~


<a id="compare-df18e0fc17edef6d327092c130f9bcbf"></a>

### [`00c34ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ea8.md) → [`00c34f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f44.md) FUN_00c34f44

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e850.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ea8.md#insn-00c34ebc)
- 新版 `00c34f58`（命令位置の公開資料なし）

~~~diff
- 00c34ebc ["INT_ADD", "register:40f0:8", ["const:c34ebc:8", "const:4:8"]]
- 00c34ebc ["CALL", null, ["callee:00c5e850:8"]]
+ 00c34f58 ["INT_ADD", "register:40f0:8", ["const:c34f58:8", "const:4:8"]]
+ 00c34f58 ["CALL", null, ["callee:00c5e850:8"]]
- 00c34ebc bytes 31a60094
+ 00c34f58 bytes 3ea60094
~~~


<a id="compare-5a7bbc3f704e62ada94a82ee43444052"></a>

### [`00c34ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ed4.md) → [`00c34f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f70.md) FUN_00c34f70

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e760.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34ed4.md#insn-00c34ee8)
- 新版 `00c34f84`（命令位置の公開資料なし）

~~~diff
- 00c34ee8 ["INT_ADD", "register:40f0:8", ["const:c34ee8:8", "const:4:8"]]
- 00c34ee8 ["CALL", null, ["callee:00c5e830:8"]]
+ 00c34f84 ["INT_ADD", "register:40f0:8", ["const:c34f84:8", "const:4:8"]]
+ 00c34f84 ["CALL", null, ["callee:00c5e830:8"]]
- 00c34ee8 bytes 1ea60094
+ 00c34f84 bytes 2ba60094
~~~


<a id="compare-cc89574b250461d7997c131eb29fb258"></a>

### [`00c34f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f00.md) → [`00c34f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34f9c.md) FUN_00c34f9c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f00.md#insn-00c34f14)
- 新版 `00c34fb0`（命令位置の公開資料なし）

~~~diff
- 00c34f14 ["INT_ADD", "register:40f0:8", ["const:c34f14:8", "const:4:8"]]
- 00c34f14 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c34fb0 ["INT_ADD", "register:40f0:8", ["const:c34fb0:8", "const:4:8"]]
+ 00c34fb0 ["CALL", null, ["callee:00c583d0:8"]]
- 00c34f14 bytes fb8c0094
+ 00c34fb0 bytes 088d0094
~~~


<a id="compare-016450ebb6a6c4258f4a74fe81deb8c8"></a>

### [`00c34f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f2c.md) → [`00c34fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34fc8.md) FUN_00c34fc8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f2c.md#insn-00c34f40)
- 新版 `00c34fdc`（命令位置の公開資料なし）

~~~diff
- 00c34f40 ["INT_ADD", "register:40f0:8", ["const:c34f40:8", "const:4:8"]]
- 00c34f40 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c34fdc ["INT_ADD", "register:40f0:8", ["const:c34fdc:8", "const:4:8"]]
+ 00c34fdc ["CALL", null, ["callee:00c583d0:8"]]
- 00c34f40 bytes f08c0094
+ 00c34fdc bytes fd8c0094
~~~


<a id="compare-3b3c8a21a63f1b9d972f39934675ebc7"></a>

### [`00c34f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f58.md) → [`00c34ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34ff4.md) FUN_00c34ff4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f58.md#insn-00c34f6c)
- 新版 `00c35008`（命令位置の公開資料なし）

~~~diff
- 00c34f6c ["INT_ADD", "register:40f0:8", ["const:c34f6c:8", "const:4:8"]]
- 00c34f6c ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35008 ["INT_ADD", "register:40f0:8", ["const:c35008:8", "const:4:8"]]
+ 00c35008 ["CALL", null, ["callee:00c583d0:8"]]
- 00c34f6c bytes e58c0094
+ 00c35008 bytes f28c0094
~~~


<a id="compare-fc7fe15be106697537a169455167e78a"></a>

### [`00c34f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f84.md) → [`00c35020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35020.md) FUN_00c35020

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34f84.md#insn-00c34f98)
- 新版 `00c35034`（命令位置の公開資料なし）

~~~diff
- 00c34f98 ["INT_ADD", "register:40f0:8", ["const:c34f98:8", "const:4:8"]]
- 00c34f98 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35034 ["INT_ADD", "register:40f0:8", ["const:c35034:8", "const:4:8"]]
+ 00c35034 ["CALL", null, ["callee:00c583d0:8"]]
- 00c34f98 bytes da8c0094
+ 00c35034 bytes e78c0094
~~~


<a id="compare-f45692412e06a4a97a2fe2582b865023"></a>

### [`00c34fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fb8.md) → [`00c35054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35054.md) FUN_00c35054

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c34fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fb8.md#insn-00c34fcc)
- 新版 `00c35068`（命令位置の公開資料なし）

~~~diff
- 00c34fcc ["INT_ADD", "register:40f0:8", ["const:c34fcc:8", "const:4:8"]]
- 00c34fcc ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35068 ["INT_ADD", "register:40f0:8", ["const:c35068:8", "const:4:8"]]
+ 00c35068 ["CALL", null, ["callee:00c583d0:8"]]
- 00c34fcc bytes cd8c0094
+ 00c35068 bytes da8c0094
~~~


<a id="compare-8ace1c309465acb6c3b2005b724b69f8"></a>

### [`00c34fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fec.md) → [`00c35088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35088.md) FUN_00c35088

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c34/00c34fec.md#insn-00c35000)
- 新版 `00c3509c`（命令位置の公開資料なし）

~~~diff
- 00c35000 ["INT_ADD", "register:40f0:8", ["const:c35000:8", "const:4:8"]]
- 00c35000 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c3509c ["INT_ADD", "register:40f0:8", ["const:c3509c:8", "const:4:8"]]
+ 00c3509c ["CALL", null, ["callee:00c583d0:8"]]
- 00c35000 bytes c08c0094
+ 00c3509c bytes cd8c0094
~~~


<a id="compare-3ac1bbccbe2481ac86ee7a9ebd32eb80"></a>

### [`00c35018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md) → [`00c350b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350b4.md) FUN_00c350b4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md#insn-00c35030)
- 新版 `00c350cc`（命令位置の公開資料なし）

~~~diff
- 00c35030 ["INT_ADD", "register:40f0:8", ["const:c35030:8", "const:4:8"]]
- 00c35030 ["CALL", null, ["callee:00c36ce8:8"]]
+ 00c350cc ["INT_ADD", "register:40f0:8", ["const:c350cc:8", "const:4:8"]]
+ 00c350cc ["CALL", null, ["callee:00c36ce8:8"]]
- 00c35030 bytes 07070094
+ 00c350cc bytes 07070094
~~~


<a id="compare-4eece579a409ed5ce0ed0f88a229b425"></a>

### [`00c35048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md) → [`00c350e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md) FUN_00c350e4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md#insn-00c35060) · [`00c35068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md#insn-00c35068)
- 新版 `00c350fc`（命令位置の公開資料なし） · `00c35104`（命令位置の公開資料なし）

~~~diff
- 00c35060 ["INT_ADD", "register:40f0:8", ["const:c35060:8", "const:4:8"]]
- 00c35060 ["CALL", null, ["callee:00c36ce8:8"]]
+ 00c350fc ["INT_ADD", "register:40f0:8", ["const:c350fc:8", "const:4:8"]]
+ 00c350fc ["CALL", null, ["callee:00c36ce8:8"]]
- 00c35060 bytes fb060094
+ 00c350fc bytes fb060094
- 00c35068 ["INT_ADD", "register:40f0:8", ["const:c35068:8", "const:4:8"]]
- 00c35068 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35104 ["INT_ADD", "register:40f0:8", ["const:c35104:8", "const:4:8"]]
+ 00c35104 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35068 bytes a68c0094
+ 00c35104 bytes b38c0094
~~~


<a id="compare-59c666f85534e4ab0b697ca4a8ed3ba4"></a>

### [`00c35134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md) → [`00c351d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351d0.md) FUN_00c351d0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3514c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md#insn-00c3514c)
- 新版 `00c351e8`（命令位置の公開資料なし）

~~~diff
- 00c3514c ["INT_ADD", "register:40f0:8", ["const:c3514c:8", "const:4:8"]]
- 00c3514c ["CALL", null, ["callee:00c36f18:8"]]
+ 00c351e8 ["INT_ADD", "register:40f0:8", ["const:c351e8:8", "const:4:8"]]
+ 00c351e8 ["CALL", null, ["callee:00c36f18:8"]]
- 00c3514c bytes 4c070094
+ 00c351e8 bytes 4c070094
~~~


<a id="compare-1f8154d80a4d18647345bd7722220810"></a>

### [`00c35164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md) → [`00c35200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md) FUN_00c35200

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3517c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md#insn-00c3517c) · [`00c35184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md#insn-00c35184)
- 新版 `00c35218`（命令位置の公開資料なし） · `00c35220`（命令位置の公開資料なし）

~~~diff
- 00c3517c ["INT_ADD", "register:40f0:8", ["const:c3517c:8", "const:4:8"]]
- 00c3517c ["CALL", null, ["callee:00c36f18:8"]]
+ 00c35218 ["INT_ADD", "register:40f0:8", ["const:c35218:8", "const:4:8"]]
+ 00c35218 ["CALL", null, ["callee:00c36f18:8"]]
- 00c3517c bytes 40070094
+ 00c35218 bytes 40070094
- 00c35184 ["INT_ADD", "register:40f0:8", ["const:c35184:8", "const:4:8"]]
- 00c35184 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35220 ["INT_ADD", "register:40f0:8", ["const:c35220:8", "const:4:8"]]
+ 00c35220 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35184 bytes 5f8c0094
+ 00c35220 bytes 6c8c0094
~~~


<a id="compare-84696c982e573d328111e5d1d2465d88"></a>

### [`00c35250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md) → [`00c352ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c352ec.md) FUN_00c352ec

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md#insn-00c35268) · [`00c35270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35250.md#insn-00c35270)
- 新版 `00c35304`（命令位置の公開資料なし） · `00c3530c`（命令位置の公開資料なし）

~~~diff
- 00c35268 ["INT_ADD", "register:40f0:8", ["const:c35268:8", "const:4:8"]]
- 00c35268 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c35304 ["INT_ADD", "register:40f0:8", ["const:c35304:8", "const:4:8"]]
+ 00c35304 ["CALL", null, ["callee:00c5ee20:8"]]
- 00c35268 bytes baa60094
+ 00c35304 bytes c7a60094
- 00c35270 ["INT_ADD", "register:40f0:8", ["const:c35270:8", "const:4:8"]]
- 00c35270 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c3530c ["INT_ADD", "register:40f0:8", ["const:c3530c:8", "const:4:8"]]
+ 00c3530c ["CALL", null, ["callee:00c583d0:8"]]
- 00c35270 bytes 248c0094
+ 00c3530c bytes 318c0094
~~~


<a id="compare-d4ca46ebf8dfdfb2272323c5c206a3b1"></a>

### [`00c35288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md) → [`00c35324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35324.md) FUN_00c35324

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c352a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md#insn-00c352a0) · [`00c352a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35288.md#insn-00c352a8)
- 新版 `00c3533c`（命令位置の公開資料なし） · `00c35344`（命令位置の公開資料なし）

~~~diff
- 00c352a0 ["INT_ADD", "register:40f0:8", ["const:c352a0:8", "const:4:8"]]
- 00c352a0 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c3533c ["INT_ADD", "register:40f0:8", ["const:c3533c:8", "const:4:8"]]
+ 00c3533c ["CALL", null, ["callee:00c5ee20:8"]]
- 00c352a0 bytes aca60094
+ 00c3533c bytes b9a60094
- 00c352a8 ["INT_ADD", "register:40f0:8", ["const:c352a8:8", "const:4:8"]]
- 00c352a8 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35344 ["INT_ADD", "register:40f0:8", ["const:c35344:8", "const:4:8"]]
+ 00c35344 ["CALL", null, ["callee:00c583d0:8"]]
- 00c352a8 bytes 168c0094
+ 00c35344 bytes 238c0094
~~~


<a id="compare-51eea7f1f364213dd2d75027500cc624"></a>

### [`00c352c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352c0.md) → [`00c3535c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3535c.md) FUN_00c3535c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c352d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352c0.md#insn-00c352d8)
- 新版 `00c35374`（命令位置の公開資料なし）

~~~diff
- 00c352d8 ["INT_ADD", "register:40f0:8", ["const:c352d8:8", "const:4:8"]]
- 00c352d8 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c35374 ["INT_ADD", "register:40f0:8", ["const:c35374:8", "const:4:8"]]
+ 00c35374 ["CALL", null, ["callee:00c5ee20:8"]]
- 00c352d8 bytes 9ea60094
+ 00c35374 bytes aba60094
~~~


<a id="compare-3e139e64d83a8f41b58d32ea57791ae6"></a>

### [`00c352f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md) → [`00c3538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3538c.md) FUN_00c3538c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md#insn-00c35308) · [`00c35310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c352f0.md#insn-00c35310)
- 新版 `00c353a4`（命令位置の公開資料なし） · `00c353ac`（命令位置の公開資料なし）

~~~diff
- 00c35308 ["INT_ADD", "register:40f0:8", ["const:c35308:8", "const:4:8"]]
- 00c35308 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c353a4 ["INT_ADD", "register:40f0:8", ["const:c353a4:8", "const:4:8"]]
+ 00c353a4 ["CALL", null, ["callee:00c5ee20:8"]]
- 00c35308 bytes 92a60094
+ 00c353a4 bytes 9fa60094
- 00c35310 ["INT_ADD", "register:40f0:8", ["const:c35310:8", "const:4:8"]]
- 00c35310 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c353ac ["INT_ADD", "register:40f0:8", ["const:c353ac:8", "const:4:8"]]
+ 00c353ac ["CALL", null, ["callee:00c583d0:8"]]
- 00c35310 bytes fc8b0094
+ 00c353ac bytes 098c0094
~~~


<a id="compare-93bebeaee40517720c51bea054b23111"></a>

### [`00c35328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35328.md) → [`00c353c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353c4.md) FUN_00c353c4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35328.md#insn-00c35340)
- 新版 `00c353dc`（命令位置の公開資料なし）

~~~diff
- 00c35340 ["INT_ADD", "register:40f0:8", ["const:c35340:8", "const:4:8"]]
- 00c35340 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c353dc ["INT_ADD", "register:40f0:8", ["const:c353dc:8", "const:4:8"]]
+ 00c353dc ["CALL", null, ["callee:00c5ee20:8"]]
- 00c35340 bytes 84a60094
+ 00c353dc bytes 91a60094
~~~


<a id="compare-73220f3457ed8195d8901c41fee1ff19"></a>

### [`00c35358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md) → [`00c353f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c353f4.md) FUN_00c353f4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5ed50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md#insn-00c35370) · [`00c35378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35358.md#insn-00c35378)
- 新版 `00c3540c`（命令位置の公開資料なし） · `00c35414`（命令位置の公開資料なし）

~~~diff
- 00c35370 ["INT_ADD", "register:40f0:8", ["const:c35370:8", "const:4:8"]]
- 00c35370 ["CALL", null, ["callee:00c5ee20:8"]]
+ 00c3540c ["INT_ADD", "register:40f0:8", ["const:c3540c:8", "const:4:8"]]
+ 00c3540c ["CALL", null, ["callee:00c5ee20:8"]]
- 00c35370 bytes 78a60094
+ 00c3540c bytes 85a60094
- 00c35378 ["INT_ADD", "register:40f0:8", ["const:c35378:8", "const:4:8"]]
- 00c35378 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35414 ["INT_ADD", "register:40f0:8", ["const:c35414:8", "const:4:8"]]
+ 00c35414 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35378 bytes e28b0094
+ 00c35414 bytes ef8b0094
~~~


<a id="compare-c81d653b5ac83823101015cfccde843f"></a>

### [`00c35390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35390.md) → [`00c3542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3542c.md) FUN_00c3542c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35390.md#insn-00c353a4)
- 新版 `00c35440`（命令位置の公開資料なし）

~~~diff
- 00c353a4 ["INT_ADD", "register:40f0:8", ["const:c353a4:8", "const:4:8"]]
- 00c353a4 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35440 ["INT_ADD", "register:40f0:8", ["const:c35440:8", "const:4:8"]]
+ 00c35440 ["CALL", null, ["callee:00c583d0:8"]]
- 00c353a4 bytes d78b0094
+ 00c35440 bytes e48b0094
~~~


<a id="compare-bcb12a8fb1218efb41e0b3acdf69ab0d"></a>

### [`00c353bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353bc.md) → [`00c35458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35458.md) FUN_00c35458

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353bc.md#insn-00c353d0)
- 新版 `00c3546c`（命令位置の公開資料なし）

~~~diff
- 00c353d0 ["INT_ADD", "register:40f0:8", ["const:c353d0:8", "const:4:8"]]
- 00c353d0 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c3546c ["INT_ADD", "register:40f0:8", ["const:c3546c:8", "const:4:8"]]
+ 00c3546c ["CALL", null, ["callee:00c583d0:8"]]
- 00c353d0 bytes cc8b0094
+ 00c3546c bytes d98b0094
~~~


<a id="compare-927be6a748aa3557b6a0d29d3ed08d5c"></a>

### [`00c353e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353e8.md) → [`00c35484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35484.md) FUN_00c35484

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c353fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c353e8.md#insn-00c353fc)
- 新版 `00c35498`（命令位置の公開資料なし）

~~~diff
- 00c353fc ["INT_ADD", "register:40f0:8", ["const:c353fc:8", "const:4:8"]]
- 00c353fc ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35498 ["INT_ADD", "register:40f0:8", ["const:c35498:8", "const:4:8"]]
+ 00c35498 ["CALL", null, ["callee:00c583d0:8"]]
- 00c353fc bytes c18b0094
+ 00c35498 bytes ce8b0094
~~~


<a id="compare-f902a2090e62a9417c826bf607492bab"></a>

### [`00c35414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35414.md) → [`00c354b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354b0.md) FUN_00c354b0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35414.md#insn-00c35428)
- 新版 `00c354c4`（命令位置の公開資料なし）

~~~diff
- 00c35428 ["INT_ADD", "register:40f0:8", ["const:c35428:8", "const:4:8"]]
- 00c35428 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c354c4 ["INT_ADD", "register:40f0:8", ["const:c354c4:8", "const:4:8"]]
+ 00c354c4 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35428 bytes b68b0094
+ 00c354c4 bytes c38b0094
~~~


<a id="compare-460bf41fec5a082897b1572371740bab"></a>

### [`00c354d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md) → [`00c35570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35570.md) FUN_00c35570

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35440.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c354dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c354e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c354d4.md#insn-00c354e8)
- 新版 `00c35584`（命令位置の公開資料なし）

~~~diff
- 00c354e8 ["INT_ADD", "register:40f0:8", ["const:c354e8:8", "const:4:8"]]
- 00c354e8 ["CALL", null, ["callee:00c354dc:8"]]
+ 00c35584 ["INT_ADD", "register:40f0:8", ["const:c35584:8", "const:4:8"]]
+ 00c35584 ["CALL", null, ["callee:00c354dc:8"]]
- 00c354e8 bytes d6ffff97
+ 00c35584 bytes d6ffff97
~~~


<a id="compare-147f202d23b100d34ffa3c17476f8269"></a>

### [`00c35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md) → [`00c35630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35630.md) FUN_00c35630

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35500.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c355a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35594.md#insn-00c355a8)
- 新版 `00c35644`（命令位置の公開資料なし）

~~~diff
- 00c355a8 ["INT_ADD", "register:40f0:8", ["const:c355a8:8", "const:4:8"]]
- 00c355a8 ["CALL", null, ["callee:00c3559c:8"]]
+ 00c35644 ["INT_ADD", "register:40f0:8", ["const:c35644:8", "const:4:8"]]
+ 00c35644 ["CALL", null, ["callee:00c3559c:8"]]
- 00c355a8 bytes d6ffff97
+ 00c35644 bytes d6ffff97
~~~


<a id="compare-779604951d42a9195642ec47e5eda6c7"></a>

### [`00c35654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md) → [`00c356f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c356f0.md) FUN_00c356f0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c355c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c355c0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35654.md#insn-00c35668)
- 新版 `00c35704`（命令位置の公開資料なし）

~~~diff
- 00c35668 ["INT_ADD", "register:40f0:8", ["const:c35668:8", "const:4:8"]]
- 00c35668 ["CALL", null, ["callee:00c3565c:8"]]
+ 00c35704 ["INT_ADD", "register:40f0:8", ["const:c35704:8", "const:4:8"]]
+ 00c35704 ["CALL", null, ["callee:00c3565c:8"]]
- 00c35668 bytes d6ffff97
+ 00c35704 bytes d6ffff97
~~~


<a id="compare-530664c94c45cb70b965c9d56531c71f"></a>

### [`00c35714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35714.md) → [`00c357b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357b0.md) FUN_00c357b0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c35680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35680.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3571c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35714.md#insn-00c35728)
- 新版 `00c357c4`（命令位置の公開資料なし）

~~~diff
- 00c35728 ["INT_ADD", "register:40f0:8", ["const:c35728:8", "const:4:8"]]
- 00c35728 ["CALL", null, ["callee:00c3571c:8"]]
+ 00c357c4 ["INT_ADD", "register:40f0:8", ["const:c357c4:8", "const:4:8"]]
+ 00c357c4 ["CALL", null, ["callee:00c3571c:8"]]
- 00c35728 bytes d6ffff97
+ 00c357c4 bytes d6ffff97
~~~


<a id="compare-db30fe8278dc7cd8d6daab16e1fde770"></a>

### [`00c35740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35740.md) → [`00c357dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c357dc.md) FUN_00c357dc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35740.md#insn-00c35754)
- 新版 `00c357f0`（命令位置の公開資料なし）

~~~diff
- 00c35754 ["INT_ADD", "register:40f0:8", ["const:c35754:8", "const:4:8"]]
- 00c35754 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c357f0 ["INT_ADD", "register:40f0:8", ["const:c357f0:8", "const:4:8"]]
+ 00c357f0 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35754 bytes eb8a0094
+ 00c357f0 bytes f88a0094
~~~


<a id="compare-6307846a537861b0bb98c47711d35cd5"></a>

### [`00c3576c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3576c.md) → [`00c35808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35808.md) FUN_00c35808

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3576c.md#insn-00c35780)
- 新版 `00c3581c`（命令位置の公開資料なし）

~~~diff
- 00c35780 ["INT_ADD", "register:40f0:8", ["const:c35780:8", "const:4:8"]]
- 00c35780 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c3581c ["INT_ADD", "register:40f0:8", ["const:c3581c:8", "const:4:8"]]
+ 00c3581c ["CALL", null, ["callee:00c583d0:8"]]
- 00c35780 bytes e08a0094
+ 00c3581c bytes ed8a0094
~~~


<a id="compare-1addfc6d0ae31f7b23884973cb84d893"></a>

### [`00c35798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35798.md) → [`00c35834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35834.md) FUN_00c35834

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c357ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35798.md#insn-00c357ac)
- 新版 `00c35848`（命令位置の公開資料なし）

~~~diff
- 00c357ac ["INT_ADD", "register:40f0:8", ["const:c357ac:8", "const:4:8"]]
- 00c357ac ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35848 ["INT_ADD", "register:40f0:8", ["const:c35848:8", "const:4:8"]]
+ 00c35848 ["CALL", null, ["callee:00c583d0:8"]]
- 00c357ac bytes d58a0094
+ 00c35848 bytes e28a0094
~~~


<a id="compare-5dc91ebbbb91d8203707a7ba88cfee07"></a>

### [`00c357c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357c4.md) → [`00c35860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35860.md) FUN_00c35860

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c357d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357c4.md#insn-00c357d8)
- 新版 `00c35874`（命令位置の公開資料なし）

~~~diff
- 00c357d8 ["INT_ADD", "register:40f0:8", ["const:c357d8:8", "const:4:8"]]
- 00c357d8 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c35874 ["INT_ADD", "register:40f0:8", ["const:c35874:8", "const:4:8"]]
+ 00c35874 ["CALL", null, ["callee:00c583d0:8"]]
- 00c357d8 bytes ca8a0094
+ 00c35874 bytes d78a0094
~~~


<a id="compare-616027c60864276c51bf41d765fd1abd"></a>

### [`00c357f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357f0.md) → [`00c3588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3588c.md) FUN_00c3588c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c357f0.md#insn-00c35804)
- 新版 `00c358a0`（命令位置の公開資料なし）

~~~diff
- 00c35804 ["INT_ADD", "register:40f0:8", ["const:c35804:8", "const:4:8"]]
- 00c35804 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c358a0 ["INT_ADD", "register:40f0:8", ["const:c358a0:8", "const:4:8"]]
+ 00c358a0 ["CALL", null, ["callee:00c583d0:8"]]
- 00c35804 bytes bf8a0094
+ 00c358a0 bytes cc8a0094
~~~


<a id="compare-fde9821ec6f64f6776a496369acb8b31"></a>

### [`00c3581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3581c.md) → [`00c358b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358b8.md) FUN_00c358b8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3581c.md#insn-00c35830)
- 新版 `00c358cc`（命令位置の公開資料なし）

~~~diff
- 00c35830 ["INT_ADD", "register:40f0:8", ["const:c35830:8", "const:4:8"]]
- 00c35830 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c358cc ["INT_ADD", "register:40f0:8", ["const:c358cc:8", "const:4:8"]]
+ 00c358cc ["CALL", null, ["callee:00c583d0:8"]]
- 00c35830 bytes b48a0094
+ 00c358cc bytes c18a0094
~~~


<a id="compare-38bde27af15948c9cdc38e05ebdeea41"></a>

### [`00c35848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35848.md) → [`00c358e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c358e4.md) FUN_00c358e4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35848.md#insn-00c3585c)
- 新版 `00c358f8`（命令位置の公開資料なし）

~~~diff
- 00c3585c ["INT_ADD", "register:40f0:8", ["const:c3585c:8", "const:4:8"]]
- 00c3585c ["CALL", null, ["callee:00c583d0:8"]]
+ 00c358f8 ["INT_ADD", "register:40f0:8", ["const:c358f8:8", "const:4:8"]]
+ 00c358f8 ["CALL", null, ["callee:00c583d0:8"]]
- 00c3585c bytes a98a0094
+ 00c358f8 bytes b68a0094
~~~


<a id="compare-5ba8b2ece92e39a07cc3815c44156e24"></a>

### [`00c3587c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3587c.md) → [`00c35918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35918.md) FUN_00c35918

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c3587c.md#insn-00c35890)
- 新版 `00c3592c`（命令位置の公開資料なし）

~~~diff
- 00c35890 ["INT_ADD", "register:40f0:8", ["const:c35890:8", "const:4:8"]]
- 00c35890 ["CALL", null, ["callee:00c583d0:8"]]
+ 00c3592c ["INT_ADD", "register:40f0:8", ["const:c3592c:8", "const:4:8"]]
+ 00c3592c ["CALL", null, ["callee:00c583d0:8"]]
- 00c35890 bytes 9c8a0094
+ 00c3592c bytes a98a0094
~~~


<a id="compare-1b05f15536224a64267a63bd9eb86919"></a>

### [`00c358a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358a8.md) → [`00c35944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35944.md) FUN_00c35944

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c358bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358a8.md#insn-00c358bc)
- 新版 `00c35958`（命令位置の公開資料なし）

~~~diff
- 00c358bc ["INT_ADD", "register:40f0:8", ["const:c358bc:8", "const:4:8"]]
- 00c358bc ["CALL", null, ["callee:00c5e640:8"]]
+ 00c35958 ["INT_ADD", "register:40f0:8", ["const:c35958:8", "const:4:8"]]
+ 00c35958 ["CALL", null, ["callee:00c5e640:8"]]
- 00c358bc bytes 2da30094
+ 00c35958 bytes 3aa30094
~~~


<a id="compare-b869c82785dd750c9117495197221db3"></a>

### [`00c358e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md) → [`00c35984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md) FUN_00c35984

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) · 呼出先 4件 [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 4件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) · 呼出先 4件 [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c35938) · [`00c35968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c35968) · [`00c359f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md#insn-00c359f4)
- 新版 `00c359d4`（命令位置の公開資料なし） · `00c35a04`（命令位置の公開資料なし） · `00c35a90`（命令位置の公開資料なし）

~~~diff
- 00c35938 ["INT_ADD", "register:40f0:8", ["const:c35938:8", "const:4:8"]]
- 00c35938 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c359d4 ["INT_ADD", "register:40f0:8", ["const:c359d4:8", "const:4:8"]]
+ 00c359d4 ["CALL", null, ["callee:00c57f80:8"]]
- 00c35938 bytes 5e890094
+ 00c359d4 bytes 6b890094
- 00c35968 ["INT_ADD", "register:40f0:8", ["const:c35968:8", "const:4:8"]]
- 00c35968 ["CALL", null, ["callee:00c58010:8"]]
+ 00c35a04 ["INT_ADD", "register:40f0:8", ["const:c35a04:8", "const:4:8"]]
+ 00c35a04 ["CALL", null, ["callee:00c58010:8"]]
- 00c35968 bytes 76890094
+ 00c35a04 bytes 83890094
- 00c359f4 ["INT_ADD", "register:40f0:8", ["const:c359f4:8", "const:4:8"]]
- 00c359f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c35a90 ["INT_ADD", "register:40f0:8", ["const:c35a90:8", "const:4:8"]]
+ 00c35a90 ["CALL", null, ["callee:00c57f60:8"]]
- 00c359f4 bytes 27890094
+ 00c35a90 bytes 34890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf631c71fb82b390013356399c8f446"></a>

### [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) → [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) FUN_00c35ae0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 54件 [`00c1d69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c1fbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) [`00c1ff54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 54件 [`00c1d738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md) [`00c1fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md) [`00c1fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) [`00c1fec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md) [`00c1fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c35ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35ae4) · [`00c35b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35b0c) · [`00c35b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md#insn-00c35b2c)
- 新版 `00c35b80`（命令位置の公開資料なし） · `00c35ba8`（命令位置の公開資料なし） · `00c35bc8`（命令位置の公開資料なし）

~~~diff
- 00c35ae4 ["INT_ADD", "register:40f0:8", ["const:c35ae4:8", "const:4:8"]]
- 00c35ae4 ["CALL", null, ["callee:00c58160:8"]]
+ 00c35b80 ["INT_ADD", "register:40f0:8", ["const:c35b80:8", "const:4:8"]]
+ 00c35b80 ["CALL", null, ["callee:00c58160:8"]]
- 00c35ae4 bytes 6b890094
+ 00c35b80 bytes 78890094
- 00c35b0c ["INT_ADD", "register:40f0:8", ["const:c35b0c:8", "const:4:8"]]
- 00c35b0c ["CALL", null, ["callee:00c57f60:8"]]
+ 00c35ba8 ["INT_ADD", "register:40f0:8", ["const:c35ba8:8", "const:4:8"]]
+ 00c35ba8 ["CALL", null, ["callee:00c57f60:8"]]
- 00c35b0c bytes e1880094
+ 00c35ba8 bytes ee880094
- 00c35b2c ["INT_ADD", "register:40f0:8", ["const:c35b2c:8", "const:4:8"]]
- 00c35b2c ["CALL", null, ["callee:00c58160:8"]]
+ 00c35bc8 ["INT_ADD", "register:40f0:8", ["const:c35bc8:8", "const:4:8"]]
+ 00c35bc8 ["CALL", null, ["callee:00c58160:8"]]
- 00c35b2c bytes 59890094
+ 00c35bc8 bytes 66890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f914895cfa62dff21f795dc0df4b83"></a>

### [`00c360b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md) → [`00c36154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md) FUN_00c36154

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c32e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32e6c.md) · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md)
- 新版 呼出元 1件 [`00c32f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32f08.md) · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c360f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md#insn-00c360f4) · [`00c3610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md#insn-00c3610c)
- 新版 `00c36190`（命令位置の公開資料なし） · `00c361a8`（命令位置の公開資料なし）

~~~diff
- 00c360f4 ["INT_ADD", "register:40f0:8", ["const:c360f4:8", "const:4:8"]]
- 00c360f4 ["CALL", null, ["callee:00bf1ca8:8"]]
+ 00c36190 ["INT_ADD", "register:40f0:8", ["const:c36190:8", "const:4:8"]]
+ 00c36190 ["CALL", null, ["callee:00bf1ca8:8"]]
- 00c360f4 bytes c6eefe97
+ 00c36190 bytes c6eefe97
- 00c3610c ["INT_ADD", "register:40f0:8", ["const:c3610c:8", "const:4:8"]]
- 00c3610c ["CALL", null, ["callee:0044295c:8"]]
+ 00c361a8 ["INT_ADD", "register:40f0:8", ["const:c361a8:8", "const:4:8"]]
+ 00c361a8 ["CALL", null, ["callee:0044295c:8"]]
- 00c3610c bytes 0432e097
+ 00c361a8 bytes ed31e097
~~~


<a id="compare-56a834c6a63b3d3936969aacd5814648"></a>

### [`00c36110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md) → [`00c361ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md) FUN_00c361ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c33f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c33/00c33f34.md) · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md)
- 新版 呼出元 1件 [`00c33fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c33fd0.md) · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md#insn-00c36150) · [`00c36168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md#insn-00c36168)
- 新版 `00c361ec`（命令位置の公開資料なし） · `00c36204`（命令位置の公開資料なし）

~~~diff
- 00c36150 ["INT_ADD", "register:40f0:8", ["const:c36150:8", "const:4:8"]]
- 00c36150 ["CALL", null, ["callee:00bf40bc:8"]]
+ 00c361ec ["INT_ADD", "register:40f0:8", ["const:c361ec:8", "const:4:8"]]
+ 00c361ec ["CALL", null, ["callee:00bf40bc:8"]]
- 00c36150 bytes b4f7fe97
+ 00c361ec bytes b4f7fe97
- 00c36168 ["INT_ADD", "register:40f0:8", ["const:c36168:8", "const:4:8"]]
- 00c36168 ["CALL", null, ["callee:00bf2974:8"]]
+ 00c36204 ["INT_ADD", "register:40f0:8", ["const:c36204:8", "const:4:8"]]
+ 00c36204 ["CALL", null, ["callee:00bf2974:8"]]
- 00c36168 bytes dcf1fe97
+ 00c36204 bytes dcf1fe97
~~~


<a id="compare-7c83837e03602a84d17c41e3b3c669c2"></a>

### [`00c36c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md) → [`00c36ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36ce8.md) FUN_00c36ce8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c35018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35018.md) [`00c35048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35048.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 2件 [`00c350b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350b4.md) [`00c350e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c350e4.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36c94) · [`00c36cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36cb8) · [`00c36d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36c4c.md#insn-00c36d34)
- 新版 `00c36d30`（命令位置の公開資料なし） · `00c36d54`（命令位置の公開資料なし） · `00c36dd0`（命令位置の公開資料なし）

~~~diff
- 00c36c94 ["INT_ADD", "register:40f0:8", ["const:c36c94:8", "const:4:8"]]
- 00c36c94 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c36d30 ["INT_ADD", "register:40f0:8", ["const:c36d30:8", "const:4:8"]]
+ 00c36d30 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36c94 bytes 87840094
+ 00c36d30 bytes 94840094
- 00c36cb8 ["INT_ADD", "register:40f0:8", ["const:c36cb8:8", "const:4:8"]]
- 00c36cb8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c36d54 ["INT_ADD", "register:40f0:8", ["const:c36d54:8", "const:4:8"]]
+ 00c36d54 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36cb8 bytes 7e840094
+ 00c36d54 bytes 8b840094
- 00c36d34 ["INT_ADD", "register:40f0:8", ["const:c36d34:8", "const:4:8"]]
- 00c36d34 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c36dd0 ["INT_ADD", "register:40f0:8", ["const:c36dd0:8", "const:4:8"]]
+ 00c36dd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36d34 bytes 5f840094
+ 00c36dd0 bytes 6c840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95fccccae2ae4aae0d23abd658bc5184"></a>

### [`00c36e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md) → [`00c36f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36f18.md) FUN_00c36f18

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c35134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35134.md) [`00c35164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35164.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)
- 新版 呼出元 2件 [`00c351d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c351d0.md) [`00c35200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35200.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c36ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36ec4) · [`00c36ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36ee8) · [`00c36f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36e7c.md#insn-00c36f64)
- 新版 `00c36f60`（命令位置の公開資料なし） · `00c36f84`（命令位置の公開資料なし） · `00c37000`（命令位置の公開資料なし）

~~~diff
- 00c36ec4 ["INT_ADD", "register:40f0:8", ["const:c36ec4:8", "const:4:8"]]
- 00c36ec4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c36f60 ["INT_ADD", "register:40f0:8", ["const:c36f60:8", "const:4:8"]]
+ 00c36f60 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36ec4 bytes fb830094
+ 00c36f60 bytes 08840094
- 00c36ee8 ["INT_ADD", "register:40f0:8", ["const:c36ee8:8", "const:4:8"]]
- 00c36ee8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c36f84 ["INT_ADD", "register:40f0:8", ["const:c36f84:8", "const:4:8"]]
+ 00c36f84 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36ee8 bytes f2830094
+ 00c36f84 bytes ff830094
- 00c36f64 ["INT_ADD", "register:40f0:8", ["const:c36f64:8", "const:4:8"]]
- 00c36f64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c37000 ["INT_ADD", "register:40f0:8", ["const:c37000:8", "const:4:8"]]
+ 00c37000 ["CALL", null, ["callee:00c57f80:8"]]
- 00c36f64 bytes d3830094
+ 00c37000 bytes e0830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd099060ff78adc5784c8a126a188b37"></a>

### [`00c37290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37290.md) → [`00c3732c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3732c.md) _ZNSt6__ndk111regex_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a890.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c372a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37290.md#insn-00c372a4)
- 新版 `00c37340`（命令位置の公開資料なし）

~~~diff
- 00c372a4 ["INT_ADD", "register:40f0:8", ["const:c372a4:8", "const:4:8"]]
- 00c372a4 ["CALL", null, ["callee:00c5a890:8"]]
+ 00c37340 ["INT_ADD", "register:40f0:8", ["const:c37340:8", "const:4:8"]]
+ 00c37340 ["CALL", null, ["callee:00c5a890:8"]]
- 00c372a4 bytes 478d0094
+ 00c37340 bytes 548d0094
~~~


<a id="compare-47f47ebd69dcd68c1158084936d99212"></a>

### [`00c37bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bac.md) → [`00c37c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c48.md) _ZNSt9exceptionD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eed0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37bac.md#insn-00c37bc0)
- 新版 `00c37c5c`（命令位置の公開資料なし）

~~~diff
- 00c37bc0 ["INT_ADD", "register:40f0:8", ["const:c37bc0:8", "const:4:8"]]
- 00c37bc0 ["CALL", null, ["callee:00c5eed0:8"]]
+ 00c37c5c ["INT_ADD", "register:40f0:8", ["const:c37c5c:8", "const:4:8"]]
+ 00c37c5c ["CALL", null, ["callee:00c5eed0:8"]]
- 00c37bc0 bytes 909c0094
+ 00c37c5c bytes 9d9c0094
~~~


<a id="compare-cbcf9cd48baaa1ffae1b82e5c3527e91"></a>

### [`00c37be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37be8.md) → [`00c37c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c84.md) _ZNSt13bad_exceptionD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37be8.md#insn-00c37bfc)
- 新版 `00c37c98`（命令位置の公開資料なし）

~~~diff
- 00c37bfc ["INT_ADD", "register:40f0:8", ["const:c37bfc:8", "const:4:8"]]
- 00c37bfc ["CALL", null, ["callee:00c5eee0:8"]]
+ 00c37c98 ["INT_ADD", "register:40f0:8", ["const:c37c98:8", "const:4:8"]]
+ 00c37c98 ["CALL", null, ["callee:00c5eee0:8"]]
- 00c37bfc bytes 859c0094
+ 00c37c98 bytes 929c0094
~~~


<a id="compare-bbab7c7727b7f37f7ec8926a2c22aa57"></a>

### [`00c37c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c3c.md) → [`00c37cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cd8.md) _ZNSt9bad_allocD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c3c.md#insn-00c37c50)
- 新版 `00c37cec`（命令位置の公開資料なし）

~~~diff
- 00c37c50 ["INT_ADD", "register:40f0:8", ["const:c37c50:8", "const:4:8"]]
- 00c37c50 ["CALL", null, ["callee:00c58b20:8"]]
+ 00c37cec ["INT_ADD", "register:40f0:8", ["const:c37cec:8", "const:4:8"]]
+ 00c37cec ["CALL", null, ["callee:00c58b20:8"]]
- 00c37c50 bytes 80830094
+ 00c37cec bytes 8d830094
~~~


<a id="compare-89d3376e2a560d5352262c9a2bc6ad9b"></a>

### [`00c37c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c90.md) → [`00c37d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d2c.md) _ZNSt20bad_array_new_lengthD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37c90.md#insn-00c37ca4)
- 新版 `00c37d40`（命令位置の公開資料なし）

~~~diff
- 00c37ca4 ["INT_ADD", "register:40f0:8", ["const:c37ca4:8", "const:4:8"]]
- 00c37ca4 ["CALL", null, ["callee:00c58110:8"]]
+ 00c37d40 ["INT_ADD", "register:40f0:8", ["const:c37d40:8", "const:4:8"]]
+ 00c37d40 ["CALL", null, ["callee:00c58110:8"]]
- 00c37ca4 bytes e7800094
+ 00c37d40 bytes f4800094
~~~


<a id="compare-1aa32aee2310c62c4fc4ee8e93f49f72"></a>

### [`00c37d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d24.md) → [`00c37dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37dc0.md) _ZNSt11logic_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5eef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eef0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d24.md#insn-00c37d38)
- 新版 `00c37dd4`（命令位置の公開資料なし）

~~~diff
- 00c37d38 ["INT_ADD", "register:40f0:8", ["const:c37d38:8", "const:4:8"]]
- 00c37d38 ["CALL", null, ["callee:00c5eef0:8"]]
+ 00c37dd4 ["INT_ADD", "register:40f0:8", ["const:c37dd4:8", "const:4:8"]]
+ 00c37dd4 ["CALL", null, ["callee:00c5eef0:8"]]
- 00c37d38 bytes 3a9c0094
+ 00c37dd4 bytes 479c0094
~~~


<a id="compare-ee4ea3c269de2be6ea5b8f6106f66082"></a>

### [`00c37db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37db4.md) → [`00c37e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e50.md) _ZNSt13runtime_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37db4.md#insn-00c37dc8)
- 新版 `00c37e64`（命令位置の公開資料なし）

~~~diff
- 00c37dc8 ["INT_ADD", "register:40f0:8", ["const:c37dc8:8", "const:4:8"]]
- 00c37dc8 ["CALL", null, ["callee:00c5e0a0:8"]]
+ 00c37e64 ["INT_ADD", "register:40f0:8", ["const:c37e64:8", "const:4:8"]]
+ 00c37e64 ["CALL", null, ["callee:00c5e0a0:8"]]
- 00c37dc8 bytes 82980094
+ 00c37e64 bytes 8f980094
~~~


<a id="compare-2beec2d7fec26662d27927aa94d3ab59"></a>

### [`00c37dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37dec.md) → [`00c37e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37e88.md) _ZNSt12domain_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37dec.md#insn-00c37e00)
- 新版 `00c37e9c`（命令位置の公開資料なし）

~~~diff
- 00c37e00 ["INT_ADD", "register:40f0:8", ["const:c37e00:8", "const:4:8"]]
- 00c37e00 ["CALL", null, ["callee:00c5ef00:8"]]
+ 00c37e9c ["INT_ADD", "register:40f0:8", ["const:c37e9c:8", "const:4:8"]]
+ 00c37e9c ["CALL", null, ["callee:00c5ef00:8"]]
- 00c37e00 bytes 0c9c0094
+ 00c37e9c bytes 199c0094
~~~


<a id="compare-a2835eda11572483542ff5eabde5bc4f"></a>

### [`00c37e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e18.md) → [`00c37eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37eb4.md) _ZNSt16invalid_argumentD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e18.md#insn-00c37e2c)
- 新版 `00c37ec8`（命令位置の公開資料なし）

~~~diff
- 00c37e2c ["INT_ADD", "register:40f0:8", ["const:c37e2c:8", "const:4:8"]]
- 00c37e2c ["CALL", null, ["callee:00c5e200:8"]]
+ 00c37ec8 ["INT_ADD", "register:40f0:8", ["const:c37ec8:8", "const:4:8"]]
+ 00c37ec8 ["CALL", null, ["callee:00c5e200:8"]]
- 00c37e2c bytes c1980094
+ 00c37ec8 bytes ce980094
~~~


<a id="compare-90ecffac426f228239c6b5f6d1686025"></a>

### [`00c37e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e44.md) → [`00c37ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37ee0.md) _ZNSt12length_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e44.md#insn-00c37e58)
- 新版 `00c37ef4`（命令位置の公開資料なし）

~~~diff
- 00c37e58 ["INT_ADD", "register:40f0:8", ["const:c37e58:8", "const:4:8"]]
- 00c37e58 ["CALL", null, ["callee:00c57fd0:8"]]
+ 00c37ef4 ["INT_ADD", "register:40f0:8", ["const:c37ef4:8", "const:4:8"]]
+ 00c37ef4 ["CALL", null, ["callee:00c57fd0:8"]]
- 00c37e58 bytes 2a800094
+ 00c37ef4 bytes 37800094
~~~


<a id="compare-d485d350c5a8f46c02ca844c46a494ff"></a>

### [`00c37e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e70.md) → [`00c37f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f0c.md) _ZNSt12out_of_rangeD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e70.md#insn-00c37e84)
- 新版 `00c37f20`（命令位置の公開資料なし）

~~~diff
- 00c37e84 ["INT_ADD", "register:40f0:8", ["const:c37e84:8", "const:4:8"]]
- 00c37e84 ["CALL", null, ["callee:00c58170:8"]]
+ 00c37f20 ["INT_ADD", "register:40f0:8", ["const:c37f20:8", "const:4:8"]]
+ 00c37f20 ["CALL", null, ["callee:00c58170:8"]]
- 00c37e84 bytes 87800094
+ 00c37f20 bytes 94800094
~~~


<a id="compare-35fa1b71746ced7d0d4e968485d7342e"></a>

### [`00c37e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e9c.md) → [`00c37f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f38.md) _ZNSt11range_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a990.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37e9c.md#insn-00c37eb0)
- 新版 `00c37f4c`（命令位置の公開資料なし）

~~~diff
- 00c37eb0 ["INT_ADD", "register:40f0:8", ["const:c37eb0:8", "const:4:8"]]
- 00c37eb0 ["CALL", null, ["callee:00c5a990:8"]]
+ 00c37f4c ["INT_ADD", "register:40f0:8", ["const:c37f4c:8", "const:4:8"]]
+ 00c37f4c ["CALL", null, ["callee:00c5a990:8"]]
- 00c37eb0 bytes 848a0094
+ 00c37f4c bytes 918a0094
~~~


<a id="compare-1a13bc81642457a526decaf76e5f5c0f"></a>

### [`00c37ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ec8.md) → [`00c37f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f64.md) _ZNSt14overflow_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ec8.md#insn-00c37edc)
- 新版 `00c37f78`（命令位置の公開資料なし）

~~~diff
- 00c37edc ["INT_ADD", "register:40f0:8", ["const:c37edc:8", "const:4:8"]]
- 00c37edc ["CALL", null, ["callee:00c5e040:8"]]
+ 00c37f78 ["INT_ADD", "register:40f0:8", ["const:c37f78:8", "const:4:8"]]
+ 00c37f78 ["CALL", null, ["callee:00c5e040:8"]]
- 00c37edc bytes 25980094
+ 00c37f78 bytes 32980094
~~~


<a id="compare-74b0a8e58bcbc5485bfa3a8a6a9ccf14"></a>

### [`00c37ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ef4.md) → [`00c37f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37f90.md) _ZNSt15underflow_errorD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ef4.md#insn-00c37f08)
- 新版 `00c37fa4`（命令位置の公開資料なし）

~~~diff
- 00c37f08 ["INT_ADD", "register:40f0:8", ["const:c37f08:8", "const:4:8"]]
- 00c37f08 ["CALL", null, ["callee:00c5ef10:8"]]
+ 00c37fa4 ["INT_ADD", "register:40f0:8", ["const:c37fa4:8", "const:4:8"]]
+ 00c37fa4 ["CALL", null, ["callee:00c5ef10:8"]]
- 00c37f08 bytes ce9b0094
+ 00c37fa4 bytes db9b0094
~~~


<a id="compare-4b40e3740af02e30eb9e4da7b818a066"></a>

### [`00c37f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f28.md) → [`00c37fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37fc4.md) _ZNSt9type_infoD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f28.md#insn-00c37f3c)
- 新版 `00c37fd8`（命令位置の公開資料なし）

~~~diff
- 00c37f3c ["INT_ADD", "register:40f0:8", ["const:c37f3c:8", "const:4:8"]]
- 00c37f3c ["CALL", null, ["callee:00c5ef30:8"]]
+ 00c37fd8 ["INT_ADD", "register:40f0:8", ["const:c37fd8:8", "const:4:8"]]
+ 00c37fd8 ["CALL", null, ["callee:00c5ef30:8"]]
- 00c37f3c bytes c99b0094
+ 00c37fd8 bytes d69b0094
~~~


<a id="compare-f25f739e4fd62ef8913552770dc9bdbb"></a>

### [`00c37f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f74.md) → [`00c38010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38010.md) _ZNSt8bad_castD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e560.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f74.md#insn-00c37f88)
- 新版 `00c38024`（命令位置の公開資料なし）

~~~diff
- 00c37f88 ["INT_ADD", "register:40f0:8", ["const:c37f88:8", "const:4:8"]]
- 00c37f88 ["CALL", null, ["callee:00c5e560:8"]]
+ 00c38024 ["INT_ADD", "register:40f0:8", ["const:c38024:8", "const:4:8"]]
+ 00c38024 ["CALL", null, ["callee:00c5e560:8"]]
- 00c37f88 bytes 42990094
+ 00c38024 bytes 4f990094
~~~


<a id="compare-8d11e26449657046ee0d6ea82206adb5"></a>

### [`00c37fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fd0.md) → [`00c3806c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3806c.md) _ZNSt10bad_typeidD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ed80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ee50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c37fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37fd0.md#insn-00c37fe4)
- 新版 `00c38080`（命令位置の公開資料なし）

~~~diff
- 00c37fe4 ["INT_ADD", "register:40f0:8", ["const:c37fe4:8", "const:4:8"]]
- 00c37fe4 ["CALL", null, ["callee:00c5ee50:8"]]
+ 00c38080 ["INT_ADD", "register:40f0:8", ["const:c38080:8", "const:4:8"]]
+ 00c38080 ["CALL", null, ["callee:00c5ee50:8"]]
- 00c37fe4 bytes 679b0094
+ 00c38080 bytes 749b0094
~~~


<a id="compare-9302d6599b80fce840146c4bfb452eef"></a>

### [`00c38130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38130.md) → [`00c381cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381cc.md) FUN_00c381cc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38130.md#insn-00c38144)
- 新版 `00c381e0`（命令位置の公開資料なし）

~~~diff
- 00c38144 ["INT_ADD", "register:40f0:8", ["const:c38144:8", "const:4:8"]]
- 00c38144 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c381e0 ["INT_ADD", "register:40f0:8", ["const:c381e0:8", "const:4:8"]]
+ 00c381e0 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c38144 bytes 439b0094
+ 00c381e0 bytes 509b0094
~~~


<a id="compare-7fd3b494c425f8ebea3ae032d5796c63"></a>

### [`00c3815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3815c.md) → [`00c381f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c381f8.md) FUN_00c381f8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3815c.md#insn-00c38170)
- 新版 `00c3820c`（命令位置の公開資料なし）

~~~diff
- 00c38170 ["INT_ADD", "register:40f0:8", ["const:c38170:8", "const:4:8"]]
- 00c38170 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c3820c ["INT_ADD", "register:40f0:8", ["const:c3820c:8", "const:4:8"]]
+ 00c3820c ["CALL", null, ["callee:00c5ef20:8"]]
- 00c38170 bytes 389b0094
+ 00c3820c bytes 459b0094
~~~


<a id="compare-5eabd4bb46b30fec6fb6f4899ae7cb58"></a>

### [`00c38188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38188.md) → [`00c38224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38224.md) FUN_00c38224

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3819c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38188.md#insn-00c3819c)
- 新版 `00c38238`（命令位置の公開資料なし）

~~~diff
- 00c3819c ["INT_ADD", "register:40f0:8", ["const:c3819c:8", "const:4:8"]]
- 00c3819c ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c38238 ["INT_ADD", "register:40f0:8", ["const:c38238:8", "const:4:8"]]
+ 00c38238 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c3819c bytes 2d9b0094
+ 00c38238 bytes 3a9b0094
~~~


<a id="compare-9312f71fdf5b864a90066b6da26963fb"></a>

### [`00c381b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381b4.md) → [`00c38250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38250.md) FUN_00c38250

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c381c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381b4.md#insn-00c381c8)
- 新版 `00c38264`（命令位置の公開資料なし）

~~~diff
- 00c381c8 ["INT_ADD", "register:40f0:8", ["const:c381c8:8", "const:4:8"]]
- 00c381c8 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c38264 ["INT_ADD", "register:40f0:8", ["const:c38264:8", "const:4:8"]]
+ 00c38264 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c381c8 bytes 229b0094
+ 00c38264 bytes 2f9b0094
~~~


<a id="compare-10b076ecd20dcb4e77948ceb2b86718e"></a>

### [`00c381e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381e0.md) → [`00c3827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3827c.md) FUN_00c3827c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c381f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c381e0.md#insn-00c381f4)
- 新版 `00c38290`（命令位置の公開資料なし）

~~~diff
- 00c381f4 ["INT_ADD", "register:40f0:8", ["const:c381f4:8", "const:4:8"]]
- 00c381f4 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c38290 ["INT_ADD", "register:40f0:8", ["const:c38290:8", "const:4:8"]]
+ 00c38290 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c381f4 bytes 179b0094
+ 00c38290 bytes 249b0094
~~~


<a id="compare-7f14886b1bd5542bc906d06d5c565f18"></a>

### [`00c3820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3820c.md) → [`00c382a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382a8.md) FUN_00c382a8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3820c.md#insn-00c38220)
- 新版 `00c382bc`（命令位置の公開資料なし）

~~~diff
- 00c38220 ["INT_ADD", "register:40f0:8", ["const:c38220:8", "const:4:8"]]
- 00c38220 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c382bc ["INT_ADD", "register:40f0:8", ["const:c382bc:8", "const:4:8"]]
+ 00c382bc ["CALL", null, ["callee:00c5ef20:8"]]
- 00c38220 bytes 0c9b0094
+ 00c382bc bytes 199b0094
~~~


<a id="compare-2d0e215209c473c2670622d703468cda"></a>

### [`00c38238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38238.md) → [`00c382d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c382d4.md) FUN_00c382d4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38238.md#insn-00c3824c)
- 新版 `00c382e8`（命令位置の公開資料なし）

~~~diff
- 00c3824c ["INT_ADD", "register:40f0:8", ["const:c3824c:8", "const:4:8"]]
- 00c3824c ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c382e8 ["INT_ADD", "register:40f0:8", ["const:c382e8:8", "const:4:8"]]
+ 00c382e8 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c3824c bytes 019b0094
+ 00c382e8 bytes 0e9b0094
~~~


<a id="compare-b8969d504b499ac101ca718430878b87"></a>

### [`00c38264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38264.md) → [`00c38300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38300.md) FUN_00c38300

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38264.md#insn-00c38278)
- 新版 `00c38314`（命令位置の公開資料なし）

~~~diff
- 00c38278 ["INT_ADD", "register:40f0:8", ["const:c38278:8", "const:4:8"]]
- 00c38278 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c38314 ["INT_ADD", "register:40f0:8", ["const:c38314:8", "const:4:8"]]
+ 00c38314 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c38278 bytes f69a0094
+ 00c38314 bytes 039b0094
~~~


<a id="compare-0106c5f3ba1f0ffe05c21c0f15a98147"></a>

### [`00c38290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38290.md) → [`00c3832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c3832c.md) FUN_00c3832c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c382a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38290.md#insn-00c382a4)
- 新版 `00c38340`（命令位置の公開資料なし）

~~~diff
- 00c382a4 ["INT_ADD", "register:40f0:8", ["const:c382a4:8", "const:4:8"]]
- 00c382a4 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c38340 ["INT_ADD", "register:40f0:8", ["const:c38340:8", "const:4:8"]]
+ 00c38340 ["CALL", null, ["callee:00c5ef20:8"]]
- 00c382a4 bytes eb9a0094
+ 00c38340 bytes f89a0094
~~~


<a id="compare-e4a625d7cba3c03dd3bf006dcf5c7548"></a>

### [`00c382bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c382bc.md) → [`00c38358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38358.md) FUN_00c38358

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ee50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ee50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ef20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c382d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c382bc.md#insn-00c382d0)
- 新版 `00c3836c`（命令位置の公開資料なし）

~~~diff
- 00c382d0 ["INT_ADD", "register:40f0:8", ["const:c382d0:8", "const:4:8"]]
- 00c382d0 ["CALL", null, ["callee:00c5ef20:8"]]
+ 00c3836c ["INT_ADD", "register:40f0:8", ["const:c3836c:8", "const:4:8"]]
+ 00c3836c ["CALL", null, ["callee:00c5ef20:8"]]
- 00c382d0 bytes e09a0094
+ 00c3836c bytes ed9a0094
~~~


<a id="compare-e6b7d36c8a7667edc523131cf6edc87c"></a>

### [`00c3841c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md) → [`00c384b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c384b8.md) __dynamic_cast

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c384c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c384c0) · [`00c38520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c38520) · [`00c385f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3841c.md#insn-00c385f8)
- 新版 `00c3855c`（命令位置の公開資料なし） · `00c385bc`（命令位置の公開資料なし） · `00c38694`（命令位置の公開資料なし）

~~~diff
- 00c384c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c384c0 ["INT_ADD", "register:40f0:8", ["const:c384c0:8", "const:4:8"]]
- 00c384c0 ["CALLIND", null, ["register:0:8"]]
+ 00c3855c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3855c ["INT_ADD", "register:40f0:8", ["const:c3855c:8", "const:4:8"]]
+ 00c3855c ["CALLIND", null, ["register:0:8"]]
- 00c384c0 bytes 20013fd6
+ 00c3855c bytes 20013fd6
- 00c38520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c38520 ["INT_ADD", "register:40f0:8", ["const:c38520:8", "const:4:8"]]
- 00c38520 ["CALLIND", null, ["register:0:8"]]
+ 00c385bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c385bc ["INT_ADD", "register:40f0:8", ["const:c385bc:8", "const:4:8"]]
+ 00c385bc ["CALLIND", null, ["register:0:8"]]
- 00c38520 bytes 00013fd6
+ 00c385bc bytes 00013fd6
- 00c385f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c385f8 ["INT_ADD", "register:40f0:8", ["const:c385f8:8", "const:4:8"]]
- 00c385f8 ["CALLIND", null, ["register:0:8"]]
+ 00c38694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c38694 ["INT_ADD", "register:40f0:8", ["const:c38694:8", "const:4:8"]]
+ 00c38694 ["CALLIND", null, ["register:0:8"]]
- 00c385f8 bytes 00013fd6
+ 00c38694 bytes 00013fd6
~~~


<a id="compare-a71b5cdc78444d7aa617485ca4fe42ec"></a>

### [`00c38744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md) → [`00c387e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c387e0.md) FUN_00c387e0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c3884c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md#insn-00c3884c) · [`00c388d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38744.md#insn-00c388d0)
- 新版 `00c388e8`（命令位置の公開資料なし） · `00c3896c`（命令位置の公開資料なし）

~~~diff
- 00c3884c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3884c ["INT_ADD", "register:40f0:8", ["const:c3884c:8", "const:4:8"]]
- 00c3884c ["CALLIND", null, ["register:0:8"]]
+ 00c388e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c388e8 ["INT_ADD", "register:40f0:8", ["const:c388e8:8", "const:4:8"]]
+ 00c388e8 ["CALLIND", null, ["register:0:8"]]
- 00c3884c bytes 00013fd6
+ 00c388e8 bytes 00013fd6
- 00c388d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c388d0 ["INT_ADD", "register:40f0:8", ["const:c388d0:8", "const:4:8"]]
- 00c388d0 ["CALLIND", null, ["register:0:8"]]
+ 00c3896c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3896c ["INT_ADD", "register:40f0:8", ["const:c3896c:8", "const:4:8"]]
+ 00c3896c ["CALLIND", null, ["register:0:8"]]
- 00c388d0 bytes 00013fd6
+ 00c3896c bytes 00013fd6
~~~


<a id="compare-6b5680def171094200e4d7c5bf5d1362"></a>

### [`00c38f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md) → [`00c39018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39018.md) FUN_00c39018

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c38fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c38fcc) · [`00c38fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c38fe8) · [`00c39098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38f7c.md#insn-00c39098)
- 新版 `00c39068`（命令位置の公開資料なし） · `00c39084`（命令位置の公開資料なし） · `00c39134`（命令位置の公開資料なし）

~~~diff
- 00c38fcc ["INT_ADD", "register:40f0:8", ["const:c38fcc:8", "const:4:8"]]
- 00c38fcc ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39068 ["INT_ADD", "register:40f0:8", ["const:c39068:8", "const:4:8"]]
+ 00c39068 ["CALL", null, ["callee:00c5b920:8"]]
- 00c38fcc bytes 218a0094
+ 00c39068 bytes 2e8a0094
- 00c38fe8 ["INT_ADD", "register:40f0:8", ["const:c38fe8:8", "const:4:8"]]
- 00c38fe8 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c39084 ["INT_ADD", "register:40f0:8", ["const:c39084:8", "const:4:8"]]
+ 00c39084 ["CALL", null, ["callee:00c5b920:8"]]
- 00c38fe8 bytes 1a8a0094
+ 00c39084 bytes 278a0094
- 00c39098 ["COPY", "register:0:8", ["register:4050:8"]]
- 00c39098 ["INT_ADD", "register:40f0:8", ["const:c39098:8", "const:4:8"]]
- 00c39098 ["CALLIND", null, ["register:0:8"]]
+ 00c39134 ["COPY", "register:0:8", ["register:4050:8"]]
+ 00c39134 ["INT_ADD", "register:40f0:8", ["const:c39134:8", "const:4:8"]]
+ 00c39134 ["CALLIND", null, ["register:0:8"]]
- 00c39098 bytes 40013fd6
+ 00c39134 bytes 40013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

