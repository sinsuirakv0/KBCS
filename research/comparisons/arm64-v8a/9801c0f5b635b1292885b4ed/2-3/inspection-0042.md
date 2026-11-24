# v16.0.1 → v16.0.2 · 要調査の変更候補 (42)

[一覧の目次](README.md)

<a id="compare-f5970bc3afa86b84d839a99274a846a5"></a>

### [`00bff9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9b0.md) → [`00bffa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa4c.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bff9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9b0.md#insn-00bff9c4)
- 新版 `00bffa60`（命令位置の公開資料なし）

~~~diff
- 00bff9c4 ["INT_ADD", "register:40f0:8", ["const:bff9c4:8", "const:4:8"]]
- 00bff9c4 ["CALL", null, ["callee:00c5e480:8"]]
+ 00bffa60 ["INT_ADD", "register:40f0:8", ["const:bffa60:8", "const:4:8"]]
+ 00bffa60 ["CALL", null, ["callee:00c5e480:8"]]
- 00bff9c4 bytes 7b7a0194
+ 00bffa60 bytes 887a0194
~~~


<a id="compare-76f1ca43dbd212d5429f063c7976451c"></a>

### [`00bff9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md) → [`00bffa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2d0.md) [`00c5e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e310.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffa04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa04) · [`00bffa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa10) · [`00bffa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff9dc.md#insn-00bffa2c)
- 新版 `00bffaa0`（命令位置の公開資料なし） · `00bffaac`（命令位置の公開資料なし） · `00bffac8`（命令位置の公開資料なし）

~~~diff
- 00bffa04 ["INT_ADD", "register:40f0:8", ["const:bffa04:8", "const:4:8"]]
- 00bffa04 ["CALL", null, ["callee:00c5e3a0:8"]]
+ 00bffaa0 ["INT_ADD", "register:40f0:8", ["const:bffaa0:8", "const:4:8"]]
+ 00bffaa0 ["CALL", null, ["callee:00c5e3a0:8"]]
- 00bffa04 bytes 337a0194
+ 00bffaa0 bytes 407a0194
- 00bffa10 ["INT_ADD", "register:40f0:8", ["const:bffa10:8", "const:4:8"]]
- 00bffa10 ["CALL", null, ["callee:00c5e3e0:8"]]
+ 00bffaac ["INT_ADD", "register:40f0:8", ["const:bffaac:8", "const:4:8"]]
+ 00bffaac ["CALL", null, ["callee:00c5e3e0:8"]]
- 00bffa10 bytes 407a0194
+ 00bffaac bytes 4d7a0194
- 00bffa2c ["INT_ADD", "register:40f0:8", ["const:bffa2c:8", "const:4:8"]]
- 00bffa2c ["CALL", null, ["callee:00c5e3a0:8"]]
+ 00bffac8 ["INT_ADD", "register:40f0:8", ["const:bffac8:8", "const:4:8"]]
+ 00bffac8 ["CALL", null, ["callee:00c5e3a0:8"]]
- 00bffa2c bytes 297a0194
+ 00bffac8 bytes 367a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ae7d52c521e2d3f95164e6d1c51820"></a>

### [`00bffa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md) → [`00bffb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb0c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffa84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md#insn-00bffa84)
- 新版 `00bffb20`（命令位置の公開資料なし）

~~~diff
- 00bffa84 ["INT_ADD", "register:40f0:8", ["const:bffa84:8", "const:4:8"]]
- 00bffa84 ["CALL", null, ["callee:00c5e4a0:8"]]
+ 00bffb20 ["INT_ADD", "register:40f0:8", ["const:bffb20:8", "const:4:8"]]
+ 00bffb20 ["CALL", null, ["callee:00c5e4a0:8"]]
- 00bffa84 bytes 537a0194
+ 00bffb20 bytes 607a0194
~~~


<a id="compare-930d82f9f14d214c4d75bfd379a24ed7"></a>

### [`00bffa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md) → [`00bffb38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb38.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md#insn-00bffac4) · [`00bffad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa9c.md#insn-00bffad0)
- 新版 `00bffb60`（命令位置の公開資料なし） · `00bffb6c`（命令位置の公開資料なし）

~~~diff
- 00bffac4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bffac4 ["INT_ADD", "register:40f0:8", ["const:bffac4:8", "const:4:8"]]
- 00bffac4 ["CALLIND", null, ["register:0:8"]]
+ 00bffb60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bffb60 ["INT_ADD", "register:40f0:8", ["const:bffb60:8", "const:4:8"]]
+ 00bffb60 ["CALLIND", null, ["register:0:8"]]
- 00bffac4 bytes 20013fd6
+ 00bffb60 bytes 20013fd6
- 00bffad0 ["INT_ADD", "register:40f0:8", ["const:bffad0:8", "const:4:8"]]
- 00bffad0 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bffb6c ["INT_ADD", "register:40f0:8", ["const:bffb6c:8", "const:4:8"]]
+ 00bffb6c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bffad0 bytes 406b0194
+ 00bffb6c bytes 4d6b0194
~~~


<a id="compare-17f2eb3821bf9eae173e882fcadee34f"></a>

### [`00bffb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb68.md) → [`00bffc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffc04.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb68.md#insn-00bffbb4)
- 新版 `00bffc50`（命令位置の公開資料なし）

~~~diff
- 00bffbb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bffbb4 ["INT_ADD", "register:40f0:8", ["const:bffbb4:8", "const:4:8"]]
- 00bffbb4 ["CALLIND", null, ["register:0:8"]]
+ 00bffc50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bffc50 ["INT_ADD", "register:40f0:8", ["const:bffc50:8", "const:4:8"]]
+ 00bffc50 ["CALLIND", null, ["register:0:8"]]
- 00bffbb4 bytes 00013fd6
+ 00bffc50 bytes 00013fd6
~~~


<a id="compare-b5d1f72c69485fe3caf4079bc5c9fe1f"></a>

### [`00bffda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffda4.md) → [`00bffe40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe40.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffda4.md#insn-00bffdc4)
- 新版 `00bffe60`（命令位置の公開資料なし）

~~~diff
- 00bffdc4 ["INT_ADD", "register:40f0:8", ["const:bffdc4:8", "const:4:8"]]
- 00bffdc4 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bffe60 ["INT_ADD", "register:40f0:8", ["const:bffe60:8", "const:4:8"]]
+ 00bffe60 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bffdc4 bytes 47790194
+ 00bffe60 bytes 54790194
~~~


<a id="compare-b71dc83af5cf6a1159a2afa9a296b233"></a>

### [`00bffdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md) → [`00bffe90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffe18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe18) · [`00bffe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe24) · [`00bffe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffdf4.md#insn-00bffe30)
- 新版 `00bffeb4`（命令位置の公開資料なし） · `00bffec0`（命令位置の公開資料なし） · `00bffecc`（命令位置の公開資料なし）

~~~diff
- 00bffe18 ["INT_ADD", "register:40f0:8", ["const:bffe18:8", "const:4:8"]]
- 00bffe18 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bffeb4 ["INT_ADD", "register:40f0:8", ["const:bffeb4:8", "const:4:8"]]
+ 00bffeb4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00bffe18 bytes 6e6a0194
+ 00bffeb4 bytes 7b6a0194
- 00bffe24 ["INT_ADD", "register:40f0:8", ["const:bffe24:8", "const:4:8"]]
- 00bffe24 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bffec0 ["INT_ADD", "register:40f0:8", ["const:bffec0:8", "const:4:8"]]
+ 00bffec0 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bffe24 bytes 2f790194
+ 00bffec0 bytes 3c790194
- 00bffe30 ["INT_ADD", "register:40f0:8", ["const:bffe30:8", "const:4:8"]]
- 00bffe30 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00bffecc ["INT_ADD", "register:40f0:8", ["const:bffecc:8", "const:4:8"]]
+ 00bffecc ["CALL", null, ["callee:00c5e3b0:8"]]
- 00bffe30 bytes 2c790194
+ 00bffecc bytes 39790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97453beba79cd46d73fa30fd9425cf52"></a>

### [`00bfff40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md) → [`00bfffdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bfffdc.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bfffc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md#insn-00bfffc4) · [`00bfffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md#insn-00bfffdc)
- 新版 `00c00060`（命令位置の公開資料なし） · `00c00078`（命令位置の公開資料なし）

~~~diff
- 00bfffc4 ["INT_ADD", "register:40f0:8", ["const:bfffc4:8", "const:4:8"]]
- 00bfffc4 ["CALL", null, ["callee:00c58010:8"]]
+ 00c00060 ["INT_ADD", "register:40f0:8", ["const:c00060:8", "const:4:8"]]
+ 00c00060 ["CALL", null, ["callee:00c58010:8"]]
- 00bfffc4 bytes df5f0194
+ 00c00060 bytes ec5f0194
- 00bfffdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfffdc ["INT_ADD", "register:40f0:8", ["const:bfffdc:8", "const:4:8"]]
- 00bfffdc ["CALLIND", null, ["register:0:8"]]
+ 00c00078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00078 ["INT_ADD", "register:40f0:8", ["const:c00078:8", "const:4:8"]]
+ 00c00078 ["CALLIND", null, ["register:0:8"]]
- 00bfffdc bytes 00013fd6
+ 00c00078 bytes 00013fd6
~~~


<a id="compare-bb7afa3f7e94829f169532ffb3127aa9"></a>

### [`00c00020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00020.md) → [`00c000bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c000bc.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0003c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00020.md#insn-00c0003c)
- 新版 `00c000d8`（命令位置の公開資料なし）

~~~diff
- 00c0003c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0003c ["INT_ADD", "register:40f0:8", ["const:c0003c:8", "const:4:8"]]
- 00c0003c ["CALLIND", null, ["register:0:8"]]
+ 00c000d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c000d8 ["INT_ADD", "register:40f0:8", ["const:c000d8:8", "const:4:8"]]
+ 00c000d8 ["CALLIND", null, ["register:0:8"]]
- 00c0003c bytes 00013fd6
+ 00c000d8 bytes 00013fd6
~~~


<a id="compare-dd2d91a983bbae10adbc9e84de0cf921"></a>

### [`00c00070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md) → [`00c0010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0010c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c000ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md#insn-00c000ec) · [`00c00108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00070.md#insn-00c00108)
- 新版 `00c00188`（命令位置の公開資料なし） · `00c001a4`（命令位置の公開資料なし）

~~~diff
- 00c000ec ["INT_ADD", "register:40f0:8", ["const:c000ec:8", "const:4:8"]]
- 00c000ec ["CALL", null, ["callee:00c58010:8"]]
+ 00c00188 ["INT_ADD", "register:40f0:8", ["const:c00188:8", "const:4:8"]]
+ 00c00188 ["CALL", null, ["callee:00c58010:8"]]
- 00c000ec bytes 955f0194
+ 00c00188 bytes a25f0194
- 00c00108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00108 ["INT_ADD", "register:40f0:8", ["const:c00108:8", "const:4:8"]]
- 00c00108 ["CALLIND", null, ["register:0:8"]]
+ 00c001a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c001a4 ["INT_ADD", "register:40f0:8", ["const:c001a4:8", "const:4:8"]]
+ 00c001a4 ["CALLIND", null, ["register:0:8"]]
- 00c00108 bytes 00013fd6
+ 00c001a4 bytes 00013fd6
~~~


<a id="compare-b42a5e740b79b59371728c33d15fbbd8"></a>

### [`00c00154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00154.md) → [`00c001f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c001f0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00154.md#insn-00c00190)
- 新版 `00c0022c`（命令位置の公開資料なし）

~~~diff
- 00c00190 ["INT_ADD", "register:40f0:8", ["const:c00190:8", "const:4:8"]]
- 00c00190 ["CALL", null, ["callee:00c582b0:8"]]
+ 00c0022c ["INT_ADD", "register:40f0:8", ["const:c0022c:8", "const:4:8"]]
+ 00c0022c ["CALL", null, ["callee:00c582b0:8"]]
- 00c00190 bytes 14600194
+ 00c0022c bytes 21600194
~~~


<a id="compare-cc3ea9bf254f2dbc3ee5e1f61d9399a9"></a>

### [`00c00248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00248.md) → [`00c002e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c002e4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00248.md#insn-00c00260)
- 新版 `00c002fc`（命令位置の公開資料なし）

~~~diff
- 00c00260 ["INT_ADD", "register:40f0:8", ["const:c00260:8", "const:4:8"]]
- 00c00260 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00c002fc ["INT_ADD", "register:40f0:8", ["const:c002fc:8", "const:4:8"]]
+ 00c002fc ["CALL", null, ["callee:00c5d1b0:8"]]
- 00c00260 bytes a0730194
+ 00c002fc bytes ad730194
~~~


<a id="compare-f0009f493d5fd0134b7d180aa50b8bd5"></a>

### [`00c00278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00278.md) → [`00c00314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00314.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00278.md#insn-00c00298)
- 新版 `00c00334`（命令位置の公開資料なし）

~~~diff
- 00c00298 ["INT_ADD", "register:40f0:8", ["const:c00298:8", "const:4:8"]]
- 00c00298 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00c00334 ["INT_ADD", "register:40f0:8", ["const:c00334:8", "const:4:8"]]
+ 00c00334 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00c00298 bytes 92730194
+ 00c00334 bytes 9f730194
~~~


<a id="compare-16640453b28c70218b8239d75de7bbf7"></a>

### [`00c002b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c002b0.md) → [`00c0034c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0034c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c002e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c002b0.md#insn-00c002e8)
- 新版 `00c00384`（命令位置の公開資料なし）

~~~diff
- 00c002e8 ["INT_ADD", "register:40f0:8", ["const:c002e8:8", "const:4:8"]]
- 00c002e8 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c00384 ["INT_ADD", "register:40f0:8", ["const:c00384:8", "const:4:8"]]
+ 00c00384 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c002e8 bytes 0e780194
+ 00c00384 bytes 1b780194
~~~


<a id="compare-5538481e5a5deb397848af36b7099da4"></a>

### [`00c0050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md) → [`00c005a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c005a8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 1件 [`00c5e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4c0.md) · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00540) · [`00c00564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00564) · [`00c00584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0050c.md#insn-00c00584)
- 新版 `00c005dc`（命令位置の公開資料なし） · `00c00600`（命令位置の公開資料なし） · `00c00620`（命令位置の公開資料なし）

~~~diff
- 00c00540 ["INT_ADD", "register:40f0:8", ["const:c00540:8", "const:4:8"]]
- 00c00540 ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c005dc ["INT_ADD", "register:40f0:8", ["const:c005dc:8", "const:4:8"]]
+ 00c005dc ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c00540 bytes b0770194
+ 00c005dc bytes bd770194
- 00c00564 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00564 ["INT_ADD", "register:40f0:8", ["const:c00564:8", "const:4:8"]]
- 00c00564 ["CALLIND", null, ["register:0:8"]]
+ 00c00600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00600 ["INT_ADD", "register:40f0:8", ["const:c00600:8", "const:4:8"]]
+ 00c00600 ["CALLIND", null, ["register:0:8"]]
- 00c00564 bytes 00013fd6
+ 00c00600 bytes 00013fd6
- 00c00584 ["INT_ADD", "register:40f0:8", ["const:c00584:8", "const:4:8"]]
- 00c00584 ["CALL", null, ["callee:00c58370:8"]]
+ 00c00620 ["INT_ADD", "register:40f0:8", ["const:c00620:8", "const:4:8"]]
+ 00c00620 ["CALL", null, ["callee:00c58370:8"]]
- 00c00584 bytes 475f0194
+ 00c00620 bytes 545f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4d66e0d302a488a5f9c2d7e69fcf11"></a>

### [`00c005fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c005fc.md) → [`00c00698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00698.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0061c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c005fc.md#insn-00c0061c)
- 新版 `00c006b8`（命令位置の公開資料なし）

~~~diff
- 00c0061c ["COPY", "register:0:8", ["register:4008:8"]]
- 00c0061c ["INT_ADD", "register:40f0:8", ["const:c0061c:8", "const:4:8"]]
- 00c0061c ["CALLIND", null, ["register:0:8"]]
+ 00c006b8 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c006b8 ["INT_ADD", "register:40f0:8", ["const:c006b8:8", "const:4:8"]]
+ 00c006b8 ["CALLIND", null, ["register:0:8"]]
- 00c0061c bytes 20003fd6
+ 00c006b8 bytes 20003fd6
~~~


<a id="compare-2a22bbec49ce3ffd419db71e63222ea0"></a>

### [`00c00634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00634.md) → [`00c006d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c006d0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c00634.md#insn-00c00654)
- 新版 `00c006f0`（命令位置の公開資料なし）

~~~diff
- 00c00654 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c00654 ["INT_ADD", "register:40f0:8", ["const:c00654:8", "const:4:8"]]
- 00c00654 ["CALLIND", null, ["register:0:8"]]
+ 00c006f0 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c006f0 ["INT_ADD", "register:40f0:8", ["const:c006f0:8", "const:4:8"]]
+ 00c006f0 ["CALLIND", null, ["register:0:8"]]
- 00c00654 bytes 20003fd6
+ 00c006f0 bytes 20003fd6
~~~


<a id="compare-aa9f6e26020060bdc1148518cb3eec6f"></a>

### [`00c0066c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md) → [`00c00708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00708.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c0069c) · [`00c00700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c00700) · [`00c00734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0066c.md#insn-00c00734)
- 新版 `00c00738`（命令位置の公開資料なし） · `00c0079c`（命令位置の公開資料なし） · `00c007d0`（命令位置の公開資料なし）

~~~diff
- 00c0069c ["INT_ADD", "register:40f0:8", ["const:c0069c:8", "const:4:8"]]
- 00c0069c ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c00738 ["INT_ADD", "register:40f0:8", ["const:c00738:8", "const:4:8"]]
+ 00c00738 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c0069c bytes 61770194
+ 00c00738 bytes 6e770194
- 00c00700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00700 ["INT_ADD", "register:40f0:8", ["const:c00700:8", "const:4:8"]]
- 00c00700 ["CALLIND", null, ["register:0:8"]]
+ 00c0079c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0079c ["INT_ADD", "register:40f0:8", ["const:c0079c:8", "const:4:8"]]
+ 00c0079c ["CALLIND", null, ["register:0:8"]]
- 00c00700 bytes 00013fd6
+ 00c0079c bytes 00013fd6
- 00c00734 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00734 ["INT_ADD", "register:40f0:8", ["const:c00734:8", "const:4:8"]]
- 00c00734 ["CALLIND", null, ["register:0:8"]]
+ 00c007d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c007d0 ["INT_ADD", "register:40f0:8", ["const:c007d0:8", "const:4:8"]]
+ 00c007d0 ["CALLIND", null, ["register:0:8"]]
- 00c00734 bytes 00013fd6
+ 00c007d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-958db8aa1d5cd5a500b8267889ece631"></a>

### [`00c01878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md) → [`00c01914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01914.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e430.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 1件 [`00c5e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e500.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c018a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c018a0) · [`00c018f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c018f8) · [`00c01920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01878.md#insn-00c01920)
- 新版 `00c0193c`（命令位置の公開資料なし） · `00c01994`（命令位置の公開資料なし） · `00c019bc`（命令位置の公開資料なし）

~~~diff
- 00c018a0 ["INT_ADD", "register:40f0:8", ["const:c018a0:8", "const:4:8"]]
- 00c018a0 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c0193c ["INT_ADD", "register:40f0:8", ["const:c0193c:8", "const:4:8"]]
+ 00c0193c ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c018a0 bytes e0720194
+ 00c0193c bytes ed720194
- 00c018f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c018f8 ["INT_ADD", "register:40f0:8", ["const:c018f8:8", "const:4:8"]]
- 00c018f8 ["CALLIND", null, ["register:0:8"]]
+ 00c01994 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01994 ["INT_ADD", "register:40f0:8", ["const:c01994:8", "const:4:8"]]
+ 00c01994 ["CALLIND", null, ["register:0:8"]]
- 00c018f8 bytes 00013fd6
+ 00c01994 bytes 00013fd6
- 00c01920 ["INT_ADD", "register:40f0:8", ["const:c01920:8", "const:4:8"]]
- 00c01920 ["CALL", null, ["callee:00c58370:8"]]
+ 00c019bc ["INT_ADD", "register:40f0:8", ["const:c019bc:8", "const:4:8"]]
+ 00c019bc ["CALL", null, ["callee:00c58370:8"]]
- 00c01920 bytes 605a0194
+ 00c019bc bytes 6d5a0194
~~~


<a id="compare-158d3714dfe254fb152b1af909c217de"></a>

### [`00c01990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01990.md) → [`00c01a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01a2c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c019a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01990.md#insn-00c019a8)
- 新版 `00c01a44`（命令位置の公開資料なし）

~~~diff
- 00c019a8 ["INT_ADD", "register:40f0:8", ["const:c019a8:8", "const:4:8"]]
- 00c019a8 ["CALL", null, ["callee:00c5e500:8"]]
+ 00c01a44 ["INT_ADD", "register:40f0:8", ["const:c01a44:8", "const:4:8"]]
+ 00c01a44 ["CALL", null, ["callee:00c5e500:8"]]
- 00c019a8 bytes a2720194
+ 00c01a44 bytes af720194
~~~


<a id="compare-9820db7872d98645fcece0e254bc303b"></a>

### [`00c01a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md) → [`00c01b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01b0c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e440.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 1件 [`00c5e510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e510.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01aac) · [`00c01b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01b24) · [`00c01b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01a70.md#insn-00c01b60)
- 新版 `00c01b48`（命令位置の公開資料なし） · `00c01bc0`（命令位置の公開資料なし） · `00c01bfc`（命令位置の公開資料なし）

~~~diff
- 00c01aac ["INT_ADD", "register:40f0:8", ["const:c01aac:8", "const:4:8"]]
- 00c01aac ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c01b48 ["INT_ADD", "register:40f0:8", ["const:c01b48:8", "const:4:8"]]
+ 00c01b48 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c01aac bytes 5d720194
+ 00c01b48 bytes 6a720194
- 00c01b24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01b24 ["INT_ADD", "register:40f0:8", ["const:c01b24:8", "const:4:8"]]
- 00c01b24 ["CALLIND", null, ["register:0:8"]]
+ 00c01bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01bc0 ["INT_ADD", "register:40f0:8", ["const:c01bc0:8", "const:4:8"]]
+ 00c01bc0 ["CALLIND", null, ["register:0:8"]]
- 00c01b24 bytes 00013fd6
+ 00c01bc0 bytes 00013fd6
- 00c01b60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01b60 ["INT_ADD", "register:40f0:8", ["const:c01b60:8", "const:4:8"]]
- 00c01b60 ["CALLIND", null, ["register:0:8"]]
+ 00c01bfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01bfc ["INT_ADD", "register:40f0:8", ["const:c01bfc:8", "const:4:8"]]
+ 00c01bfc ["CALLIND", null, ["register:0:8"]]
- 00c01b60 bytes 00013fd6
+ 00c01bfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb085973158ffb9ae88f60bbb07cb166"></a>

### [`00c01cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md) → [`00c01d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01d70.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e450.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 1件 [`00c5e520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e520.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01d08) · [`00c01d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01d68) · [`00c01da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01cd4.md#insn-00c01da4)
- 新版 `00c01da4`（命令位置の公開資料なし） · `00c01e04`（命令位置の公開資料なし） · `00c01e40`（命令位置の公開資料なし）

~~~diff
- 00c01d08 ["INT_ADD", "register:40f0:8", ["const:c01d08:8", "const:4:8"]]
- 00c01d08 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c01da4 ["INT_ADD", "register:40f0:8", ["const:c01da4:8", "const:4:8"]]
+ 00c01da4 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c01d08 bytes c6710194
+ 00c01da4 bytes d3710194
- 00c01d68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01d68 ["INT_ADD", "register:40f0:8", ["const:c01d68:8", "const:4:8"]]
- 00c01d68 ["CALLIND", null, ["register:0:8"]]
+ 00c01e04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01e04 ["INT_ADD", "register:40f0:8", ["const:c01e04:8", "const:4:8"]]
+ 00c01e04 ["CALLIND", null, ["register:0:8"]]
- 00c01d68 bytes 00013fd6
+ 00c01e04 bytes 00013fd6
- 00c01da4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01da4 ["INT_ADD", "register:40f0:8", ["const:c01da4:8", "const:4:8"]]
- 00c01da4 ["CALLIND", null, ["register:0:8"]]
+ 00c01e40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01e40 ["INT_ADD", "register:40f0:8", ["const:c01e40:8", "const:4:8"]]
+ 00c01e40 ["CALLIND", null, ["register:0:8"]]
- 00c01da4 bytes 00013fd6
+ 00c01e40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe14cf8c9cac0115b3e17e4f885315c0"></a>

### [`00c01edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md) → [`00c01f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01f78.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e460.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 1件 [`00c5e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e530.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01f1c) · [`00c01f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01f74) · [`00c01fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c01/00c01edc.md#insn-00c01fbc)
- 新版 `00c01fb8`（命令位置の公開資料なし） · `00c02010`（命令位置の公開資料なし） · `00c02058`（命令位置の公開資料なし）

~~~diff
- 00c01f1c ["INT_ADD", "register:40f0:8", ["const:c01f1c:8", "const:4:8"]]
- 00c01f1c ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c01fb8 ["INT_ADD", "register:40f0:8", ["const:c01fb8:8", "const:4:8"]]
+ 00c01fb8 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c01f1c bytes 41710194
+ 00c01fb8 bytes 4e710194
- 00c01f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01f74 ["INT_ADD", "register:40f0:8", ["const:c01f74:8", "const:4:8"]]
- 00c01f74 ["CALLIND", null, ["register:0:8"]]
+ 00c02010 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02010 ["INT_ADD", "register:40f0:8", ["const:c02010:8", "const:4:8"]]
+ 00c02010 ["CALLIND", null, ["register:0:8"]]
- 00c01f74 bytes 00013fd6
+ 00c02010 bytes 00013fd6
- 00c01fbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01fbc ["INT_ADD", "register:40f0:8", ["const:c01fbc:8", "const:4:8"]]
- 00c01fbc ["CALLIND", null, ["register:0:8"]]
+ 00c02058 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02058 ["INT_ADD", "register:40f0:8", ["const:c02058:8", "const:4:8"]]
+ 00c02058 ["CALLIND", null, ["register:0:8"]]
- 00c01fbc bytes 00013fd6
+ 00c02058 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba80d7d04713d71a4c03973d2f20fb0"></a>

### [`00c02118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md) → [`00c021b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c021b4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c0214c) · [`00c021a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c021a4) · [`00c0220c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02118.md#insn-00c0220c)
- 新版 `00c021e8`（命令位置の公開資料なし） · `00c02240`（命令位置の公開資料なし） · `00c022a8`（命令位置の公開資料なし）

~~~diff
- 00c0214c ["INT_ADD", "register:40f0:8", ["const:c0214c:8", "const:4:8"]]
- 00c0214c ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c021e8 ["INT_ADD", "register:40f0:8", ["const:c021e8:8", "const:4:8"]]
+ 00c021e8 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c0214c bytes b5700194
+ 00c021e8 bytes c2700194
- 00c021a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c021a4 ["INT_ADD", "register:40f0:8", ["const:c021a4:8", "const:4:8"]]
- 00c021a4 ["CALLIND", null, ["register:0:8"]]
+ 00c02240 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c02240 ["INT_ADD", "register:40f0:8", ["const:c02240:8", "const:4:8"]]
+ 00c02240 ["CALLIND", null, ["register:0:8"]]
- 00c021a4 bytes 20013fd6
+ 00c02240 bytes 20013fd6
- 00c0220c ["COPY", "register:0:8", ["register:4048:8"]]
- 00c0220c ["INT_ADD", "register:40f0:8", ["const:c0220c:8", "const:4:8"]]
- 00c0220c ["CALLIND", null, ["register:0:8"]]
+ 00c022a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c022a8 ["INT_ADD", "register:40f0:8", ["const:c022a8:8", "const:4:8"]]
+ 00c022a8 ["CALLIND", null, ["register:0:8"]]
- 00c0220c bytes 20013fd6
+ 00c022a8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e208c63c0706029ab678477c2a0e132"></a>

### [`00c022cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md) → [`00c02368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02368.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c022f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c022f4) · [`00c02334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c02334) · [`00c0235c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c022cc.md#insn-00c0235c)
- 新版 `00c02390`（命令位置の公開資料なし） · `00c023d0`（命令位置の公開資料なし） · `00c023f8`（命令位置の公開資料なし）

~~~diff
- 00c022f4 ["INT_ADD", "register:40f0:8", ["const:c022f4:8", "const:4:8"]]
- 00c022f4 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02390 ["INT_ADD", "register:40f0:8", ["const:c02390:8", "const:4:8"]]
+ 00c02390 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c022f4 bytes 4b700194
+ 00c02390 bytes 58700194
- 00c02334 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02334 ["INT_ADD", "register:40f0:8", ["const:c02334:8", "const:4:8"]]
- 00c02334 ["CALLIND", null, ["register:0:8"]]
+ 00c023d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c023d0 ["INT_ADD", "register:40f0:8", ["const:c023d0:8", "const:4:8"]]
+ 00c023d0 ["CALLIND", null, ["register:0:8"]]
- 00c02334 bytes 00013fd6
+ 00c023d0 bytes 00013fd6
- 00c0235c ["INT_ADD", "register:40f0:8", ["const:c0235c:8", "const:4:8"]]
- 00c0235c ["CALL", null, ["callee:00c58370:8"]]
+ 00c023f8 ["INT_ADD", "register:40f0:8", ["const:c023f8:8", "const:4:8"]]
+ 00c023f8 ["CALL", null, ["callee:00c58370:8"]]
- 00c0235c bytes d1570194
+ 00c023f8 bytes de570194
~~~


<a id="compare-92af5d8daaa22032f2566254d8c7de06"></a>

### [`00c023cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md) → [`00c02468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02468.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c023fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c023fc) · [`00c02428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c02428) · [`00c02458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c023cc.md#insn-00c02458)
- 新版 `00c02498`（命令位置の公開資料なし） · `00c024c4`（命令位置の公開資料なし） · `00c024f4`（命令位置の公開資料なし）

~~~diff
- 00c023fc ["INT_ADD", "register:40f0:8", ["const:c023fc:8", "const:4:8"]]
- 00c023fc ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02498 ["INT_ADD", "register:40f0:8", ["const:c02498:8", "const:4:8"]]
+ 00c02498 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c023fc bytes 09700194
+ 00c02498 bytes 16700194
- 00c02428 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02428 ["INT_ADD", "register:40f0:8", ["const:c02428:8", "const:4:8"]]
- 00c02428 ["CALLIND", null, ["register:0:8"]]
+ 00c024c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c024c4 ["INT_ADD", "register:40f0:8", ["const:c024c4:8", "const:4:8"]]
+ 00c024c4 ["CALLIND", null, ["register:0:8"]]
- 00c02428 bytes 00013fd6
+ 00c024c4 bytes 00013fd6
- 00c02458 ["INT_ADD", "register:40f0:8", ["const:c02458:8", "const:4:8"]]
- 00c02458 ["CALL", null, ["callee:00c58370:8"]]
+ 00c024f4 ["INT_ADD", "register:40f0:8", ["const:c024f4:8", "const:4:8"]]
+ 00c024f4 ["CALL", null, ["callee:00c58370:8"]]
- 00c02458 bytes 92570194
+ 00c024f4 bytes 9f570194
~~~


<a id="compare-4aac92b8d949274ccdef5ee7c14bbb82"></a>

### [`00c024c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md) → [`00c02560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02560.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c024f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c024f4) · [`00c02538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c02538) · [`00c02584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c024c4.md#insn-00c02584)
- 新版 `00c02590`（命令位置の公開資料なし） · `00c025d4`（命令位置の公開資料なし） · `00c02620`（命令位置の公開資料なし）

~~~diff
- 00c024f4 ["INT_ADD", "register:40f0:8", ["const:c024f4:8", "const:4:8"]]
- 00c024f4 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02590 ["INT_ADD", "register:40f0:8", ["const:c02590:8", "const:4:8"]]
+ 00c02590 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c024f4 bytes cb6f0194
+ 00c02590 bytes d86f0194
- 00c02538 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02538 ["INT_ADD", "register:40f0:8", ["const:c02538:8", "const:4:8"]]
- 00c02538 ["CALLIND", null, ["register:0:8"]]
+ 00c025d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c025d4 ["INT_ADD", "register:40f0:8", ["const:c025d4:8", "const:4:8"]]
+ 00c025d4 ["CALLIND", null, ["register:0:8"]]
- 00c02538 bytes 00013fd6
+ 00c025d4 bytes 00013fd6
- 00c02584 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c02584 ["INT_ADD", "register:40f0:8", ["const:c02584:8", "const:4:8"]]
- 00c02584 ["CALLIND", null, ["register:0:8"]]
+ 00c02620 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c02620 ["INT_ADD", "register:40f0:8", ["const:c02620:8", "const:4:8"]]
+ 00c02620 ["CALLIND", null, ["register:0:8"]]
- 00c02584 bytes 20013fd6
+ 00c02620 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a986b0e4777582ded5eab4e9a44f3d0"></a>

### [`00c02618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md) → [`00c026b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c026b4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c02658) · [`00c02668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c02668) · [`00c026c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02618.md#insn-00c026c4)
- 新版 `00c026f4`（命令位置の公開資料なし） · `00c02704`（命令位置の公開資料なし） · `00c02760`（命令位置の公開資料なし）

~~~diff
- 00c02658 ["INT_ADD", "register:40f0:8", ["const:c02658:8", "const:4:8"]]
- 00c02658 ["CALL", null, ["callee:00c58370:8"]]
+ 00c026f4 ["INT_ADD", "register:40f0:8", ["const:c026f4:8", "const:4:8"]]
+ 00c026f4 ["CALL", null, ["callee:00c58370:8"]]
- 00c02658 bytes 12570194
+ 00c026f4 bytes 1f570194
- 00c02668 ["INT_ADD", "register:40f0:8", ["const:c02668:8", "const:4:8"]]
- 00c02668 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02704 ["INT_ADD", "register:40f0:8", ["const:c02704:8", "const:4:8"]]
+ 00c02704 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c02668 bytes 6e6f0194
+ 00c02704 bytes 7b6f0194
- 00c026c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c026c4 ["INT_ADD", "register:40f0:8", ["const:c026c4:8", "const:4:8"]]
- 00c026c4 ["CALLIND", null, ["register:0:8"]]
+ 00c02760 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02760 ["INT_ADD", "register:40f0:8", ["const:c02760:8", "const:4:8"]]
+ 00c02760 ["CALLIND", null, ["register:0:8"]]
- 00c026c4 bytes 00013fd6
+ 00c02760 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78106d836d9e8fd8433962e50985cb3e"></a>

### [`00c02758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md) → [`00c027f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c027f4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c02794) · [`00c027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c027a4) · [`00c027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02758.md#insn-00c027f8)
- 新版 `00c02830`（命令位置の公開資料なし） · `00c02840`（命令位置の公開資料なし） · `00c02894`（命令位置の公開資料なし）

~~~diff
- 00c02794 ["INT_ADD", "register:40f0:8", ["const:c02794:8", "const:4:8"]]
- 00c02794 ["CALL", null, ["callee:00c58370:8"]]
+ 00c02830 ["INT_ADD", "register:40f0:8", ["const:c02830:8", "const:4:8"]]
+ 00c02830 ["CALL", null, ["callee:00c58370:8"]]
- 00c02794 bytes c3560194
+ 00c02830 bytes d0560194
- 00c027a4 ["INT_ADD", "register:40f0:8", ["const:c027a4:8", "const:4:8"]]
- 00c027a4 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02840 ["INT_ADD", "register:40f0:8", ["const:c02840:8", "const:4:8"]]
+ 00c02840 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c027a4 bytes 1f6f0194
+ 00c02840 bytes 2c6f0194
- 00c027f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c027f8 ["INT_ADD", "register:40f0:8", ["const:c027f8:8", "const:4:8"]]
- 00c027f8 ["CALLIND", null, ["register:0:8"]]
+ 00c02894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02894 ["INT_ADD", "register:40f0:8", ["const:c02894:8", "const:4:8"]]
+ 00c02894 ["CALLIND", null, ["register:0:8"]]
- 00c027f8 bytes 00013fd6
+ 00c02894 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-454b16e2cd452230cab14d997514000a"></a>

### [`00c0288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md) → [`00c02928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02928.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c028b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028b0) · [`00c028d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028d8) · [`00c028fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0288c.md#insn-00c028fc)
- 新版 `00c0294c`（命令位置の公開資料なし） · `00c02974`（命令位置の公開資料なし） · `00c02998`（命令位置の公開資料なし）

~~~diff
- 00c028b0 ["INT_ADD", "register:40f0:8", ["const:c028b0:8", "const:4:8"]]
- 00c028b0 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c0294c ["INT_ADD", "register:40f0:8", ["const:c0294c:8", "const:4:8"]]
+ 00c0294c ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c028b0 bytes dc6e0194
+ 00c0294c bytes e96e0194
- 00c028d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c028d8 ["INT_ADD", "register:40f0:8", ["const:c028d8:8", "const:4:8"]]
- 00c028d8 ["CALLIND", null, ["register:0:8"]]
+ 00c02974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02974 ["INT_ADD", "register:40f0:8", ["const:c02974:8", "const:4:8"]]
+ 00c02974 ["CALLIND", null, ["register:0:8"]]
- 00c028d8 bytes 00013fd6
+ 00c02974 bytes 00013fd6
- 00c028fc ["INT_ADD", "register:40f0:8", ["const:c028fc:8", "const:4:8"]]
- 00c028fc ["CALL", null, ["callee:00c58370:8"]]
+ 00c02998 ["INT_ADD", "register:40f0:8", ["const:c02998:8", "const:4:8"]]
+ 00c02998 ["CALL", null, ["callee:00c58370:8"]]
- 00c028fc bytes 69560194
+ 00c02998 bytes 76560194
~~~


<a id="compare-4c962b5f531dd6554fa6f06ba5f6c441"></a>

### [`00c0297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md) → [`00c02a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02a18.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c029a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029a0) · [`00c029d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029d0) · [`00c029f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c0297c.md#insn-00c029f4)
- 新版 `00c02a3c`（命令位置の公開資料なし） · `00c02a6c`（命令位置の公開資料なし） · `00c02a90`（命令位置の公開資料なし）

~~~diff
- 00c029a0 ["INT_ADD", "register:40f0:8", ["const:c029a0:8", "const:4:8"]]
- 00c029a0 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02a3c ["INT_ADD", "register:40f0:8", ["const:c02a3c:8", "const:4:8"]]
+ 00c02a3c ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c029a0 bytes a06e0194
+ 00c02a3c bytes ad6e0194
- 00c029d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c029d0 ["INT_ADD", "register:40f0:8", ["const:c029d0:8", "const:4:8"]]
- 00c029d0 ["CALLIND", null, ["register:0:8"]]
+ 00c02a6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02a6c ["INT_ADD", "register:40f0:8", ["const:c02a6c:8", "const:4:8"]]
+ 00c02a6c ["CALLIND", null, ["register:0:8"]]
- 00c029d0 bytes 00013fd6
+ 00c02a6c bytes 00013fd6
- 00c029f4 ["INT_ADD", "register:40f0:8", ["const:c029f4:8", "const:4:8"]]
- 00c029f4 ["CALL", null, ["callee:00c58370:8"]]
+ 00c02a90 ["INT_ADD", "register:40f0:8", ["const:c02a90:8", "const:4:8"]]
+ 00c02a90 ["CALL", null, ["callee:00c58370:8"]]
- 00c029f4 bytes 2b560194
+ 00c02a90 bytes 38560194
~~~


<a id="compare-fc34de953fac303401d9a6bfb607ba3b"></a>

### [`00c02a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md) → [`00c02b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02b14.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02ab4) · [`00c02ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02ac4) · [`00c02af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02a78.md#insn-00c02af4)
- 新版 `00c02b50`（命令位置の公開資料なし） · `00c02b60`（命令位置の公開資料なし） · `00c02b90`（命令位置の公開資料なし）

~~~diff
- 00c02ab4 ["INT_ADD", "register:40f0:8", ["const:c02ab4:8", "const:4:8"]]
- 00c02ab4 ["CALL", null, ["callee:00c58370:8"]]
+ 00c02b50 ["INT_ADD", "register:40f0:8", ["const:c02b50:8", "const:4:8"]]
+ 00c02b50 ["CALL", null, ["callee:00c58370:8"]]
- 00c02ab4 bytes fb550194
+ 00c02b50 bytes 08560194
- 00c02ac4 ["INT_ADD", "register:40f0:8", ["const:c02ac4:8", "const:4:8"]]
- 00c02ac4 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02b60 ["INT_ADD", "register:40f0:8", ["const:c02b60:8", "const:4:8"]]
+ 00c02b60 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c02ac4 bytes 576e0194
+ 00c02b60 bytes 646e0194
- 00c02af4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02af4 ["INT_ADD", "register:40f0:8", ["const:c02af4:8", "const:4:8"]]
- 00c02af4 ["CALLIND", null, ["register:0:8"]]
+ 00c02b90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02b90 ["INT_ADD", "register:40f0:8", ["const:c02b90:8", "const:4:8"]]
+ 00c02b90 ["CALLIND", null, ["register:0:8"]]
- 00c02af4 bytes 00013fd6
+ 00c02b90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c29928aff1deaa4ac2b626ea0835a8d"></a>

### [`00c02b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md) → [`00c02c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02c24.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02bc4) · [`00c02bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02bd4) · [`00c02c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02b88.md#insn-00c02c04)
- 新版 `00c02c60`（命令位置の公開資料なし） · `00c02c70`（命令位置の公開資料なし） · `00c02ca0`（命令位置の公開資料なし）

~~~diff
- 00c02bc4 ["INT_ADD", "register:40f0:8", ["const:c02bc4:8", "const:4:8"]]
- 00c02bc4 ["CALL", null, ["callee:00c58370:8"]]
+ 00c02c60 ["INT_ADD", "register:40f0:8", ["const:c02c60:8", "const:4:8"]]
+ 00c02c60 ["CALL", null, ["callee:00c58370:8"]]
- 00c02bc4 bytes b7550194
+ 00c02c60 bytes c4550194
- 00c02bd4 ["INT_ADD", "register:40f0:8", ["const:c02bd4:8", "const:4:8"]]
- 00c02bd4 ["CALL", null, ["callee:00c5e4f0:8"]]
+ 00c02c70 ["INT_ADD", "register:40f0:8", ["const:c02c70:8", "const:4:8"]]
+ 00c02c70 ["CALL", null, ["callee:00c5e4f0:8"]]
- 00c02bd4 bytes 136e0194
+ 00c02c70 bytes 206e0194
- 00c02c04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02c04 ["INT_ADD", "register:40f0:8", ["const:c02c04:8", "const:4:8"]]
- 00c02c04 ["CALLIND", null, ["register:0:8"]]
+ 00c02ca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02ca0 ["INT_ADD", "register:40f0:8", ["const:c02ca0:8", "const:4:8"]]
+ 00c02ca0 ["CALLIND", null, ["register:0:8"]]
- 00c02c04 bytes 00013fd6
+ 00c02ca0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3270b86031489adf9a58a769eba6db"></a>

### [`00c02c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02c98.md) → [`00c02d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02d34.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02c98.md#insn-00c02cd0)
- 新版 `00c02d6c`（命令位置の公開資料なし）

~~~diff
- 00c02cd0 ["INT_ADD", "register:40f0:8", ["const:c02cd0:8", "const:4:8"]]
- 00c02cd0 ["CALL", null, ["callee:00c582b0:8"]]
+ 00c02d6c ["INT_ADD", "register:40f0:8", ["const:c02d6c:8", "const:4:8"]]
+ 00c02d6c ["CALL", null, ["callee:00c582b0:8"]]
- 00c02cd0 bytes 44550194
+ 00c02d6c bytes 51550194
~~~


<a id="compare-fe86dbb30c408428b2f490c92ddcbd52"></a>

### [`00c02d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02d88.md) → [`00c02e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e24.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02d88.md#insn-00c02da0)
- 新版 `00c02e3c`（命令位置の公開資料なし）

~~~diff
- 00c02da0 ["INT_ADD", "register:40f0:8", ["const:c02da0:8", "const:4:8"]]
- 00c02da0 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00c02e3c ["INT_ADD", "register:40f0:8", ["const:c02e3c:8", "const:4:8"]]
+ 00c02e3c ["CALL", null, ["callee:00c5d1b0:8"]]
- 00c02da0 bytes d0680194
+ 00c02e3c bytes dd680194
~~~


<a id="compare-1aeff81642870e2934c3300f8715b723"></a>

### [`00c02db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02db8.md) → [`00c02e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e54.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02db8.md#insn-00c02dd8)
- 新版 `00c02e74`（命令位置の公開資料なし）

~~~diff
- 00c02dd8 ["INT_ADD", "register:40f0:8", ["const:c02dd8:8", "const:4:8"]]
- 00c02dd8 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00c02e74 ["INT_ADD", "register:40f0:8", ["const:c02e74:8", "const:4:8"]]
+ 00c02e74 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00c02dd8 bytes c2680194
+ 00c02e74 bytes cf680194
~~~


<a id="compare-ec773bcfee2cb9875fbc7d5d7f15b366"></a>

### [`00c02df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02df0.md) → [`00c02e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e8c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02df0.md#insn-00c02e20)
- 新版 `00c02ebc`（命令位置の公開資料なし）

~~~diff
- 00c02e20 ["INT_ADD", "register:40f0:8", ["const:c02e20:8", "const:4:8"]]
- 00c02e20 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c02ebc ["INT_ADD", "register:40f0:8", ["const:c02ebc:8", "const:4:8"]]
+ 00c02ebc ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c02e20 bytes 406d0194
+ 00c02ebc bytes 4d6d0194
~~~


<a id="compare-2bdcd5b17d241444220d81f18ecd4e3b"></a>

### [`00c02e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02e54.md) → [`00c02ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02ef0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 1件 [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) · 呼出先 1件 [`00c5e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02e54.md#insn-00c02e98)
- 新版 `00c02f34`（命令位置の公開資料なし）

~~~diff
- 00c02e98 ["INT_ADD", "register:40f0:8", ["const:c02e98:8", "const:4:8"]]
- 00c02e98 ["CALL", null, ["callee:00c5e4c0:8"]]
+ 00c02f34 ["INT_ADD", "register:40f0:8", ["const:c02f34:8", "const:4:8"]]
+ 00c02f34 ["CALL", null, ["callee:00c5e4c0:8"]]
- 00c02e98 bytes 566d0194
+ 00c02f34 bytes 636d0194
~~~


<a id="compare-22dff6b4ae97826029cd3d1ddab3bde8"></a>

### [`00c02eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md) → [`00c02f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02f54.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md)
- 新版 呼出元 1件 [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02ef4) · [`00c02f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02f18) · [`00c02f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02eb8.md#insn-00c02f3c)
- 新版 `00c02f90`（命令位置の公開資料なし） · `00c02fb4`（命令位置の公開資料なし） · `00c02fd8`（命令位置の公開資料なし）

~~~diff
- 00c02ef4 ["INT_ADD", "register:40f0:8", ["const:c02ef4:8", "const:4:8"]]
- 00c02ef4 ["CALL", null, ["callee:00c5d1c0:8"]]
+ 00c02f90 ["INT_ADD", "register:40f0:8", ["const:c02f90:8", "const:4:8"]]
+ 00c02f90 ["CALL", null, ["callee:00c5d1c0:8"]]
- 00c02ef4 bytes 7f680194
+ 00c02f90 bytes 8c680194
- 00c02f18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02f18 ["INT_ADD", "register:40f0:8", ["const:c02f18:8", "const:4:8"]]
- 00c02f18 ["CALLIND", null, ["register:0:8"]]
+ 00c02fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02fb4 ["INT_ADD", "register:40f0:8", ["const:c02fb4:8", "const:4:8"]]
+ 00c02fb4 ["CALLIND", null, ["register:0:8"]]
- 00c02f18 bytes 00013fd6
+ 00c02fb4 bytes 00013fd6
- 00c02f3c ["INT_ADD", "register:40f0:8", ["const:c02f3c:8", "const:4:8"]]
- 00c02f3c ["CALL", null, ["callee:00c58370:8"]]
+ 00c02fd8 ["INT_ADD", "register:40f0:8", ["const:c02fd8:8", "const:4:8"]]
+ 00c02fd8 ["CALL", null, ["callee:00c58370:8"]]
- 00c02f3c bytes d9540194
+ 00c02fd8 bytes e6540194
~~~


<a id="compare-35fcb2b3d77ae0607338d46d1008b2e2"></a>

### [`00c02f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02f6c.md) → [`00c03008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03008.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02f6c.md#insn-00c02f8c)
- 新版 `00c03028`（命令位置の公開資料なし）

~~~diff
- 00c02f8c ["COPY", "register:0:8", ["register:4008:8"]]
- 00c02f8c ["INT_ADD", "register:40f0:8", ["const:c02f8c:8", "const:4:8"]]
- 00c02f8c ["CALLIND", null, ["register:0:8"]]
+ 00c03028 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c03028 ["INT_ADD", "register:40f0:8", ["const:c03028:8", "const:4:8"]]
+ 00c03028 ["CALLIND", null, ["register:0:8"]]
- 00c02f8c bytes 20003fd6
+ 00c03028 bytes 20003fd6
~~~


<a id="compare-2698ce25003a4db44f1c41d32ff60d31"></a>

### [`00c02fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02fa4.md) → [`00c03040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03040.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c02/00c02fa4.md#insn-00c02fc4)
- 新版 `00c03060`（命令位置の公開資料なし）

~~~diff
- 00c02fc4 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c02fc4 ["INT_ADD", "register:40f0:8", ["const:c02fc4:8", "const:4:8"]]
- 00c02fc4 ["CALLIND", null, ["register:0:8"]]
+ 00c03060 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c03060 ["INT_ADD", "register:40f0:8", ["const:c03060:8", "const:4:8"]]
+ 00c03060 ["CALLIND", null, ["register:0:8"]]
- 00c02fc4 bytes 20003fd6
+ 00c03060 bytes 20003fd6
~~~


<a id="compare-276f68e4d918bca43cf8089f3d9fedcb"></a>

### [`00c0448c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c0448c.md) → [`00c04528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04528.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c044b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c0448c.md#insn-00c044b4) · [`00c04508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c0448c.md#insn-00c04508) · [`00c04534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c0448c.md#insn-00c04534)
- 新版 `00c04550`（命令位置の公開資料なし） · `00c045a4`（命令位置の公開資料なし） · `00c045d0`（命令位置の公開資料なし）

~~~diff
- 00c044b4 ["INT_ADD", "register:40f0:8", ["const:c044b4:8", "const:4:8"]]
- 00c044b4 ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c04550 ["INT_ADD", "register:40f0:8", ["const:c04550:8", "const:4:8"]]
+ 00c04550 ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c044b4 bytes d3670194
+ 00c04550 bytes e0670194
- 00c04508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04508 ["INT_ADD", "register:40f0:8", ["const:c04508:8", "const:4:8"]]
- 00c04508 ["CALLIND", null, ["register:0:8"]]
+ 00c045a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c045a4 ["INT_ADD", "register:40f0:8", ["const:c045a4:8", "const:4:8"]]
+ 00c045a4 ["CALLIND", null, ["register:0:8"]]
- 00c04508 bytes 00013fd6
+ 00c045a4 bytes 00013fd6
- 00c04534 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04534 ["INT_ADD", "register:40f0:8", ["const:c04534:8", "const:4:8"]]
- 00c04534 ["CALLIND", null, ["register:0:8"]]
+ 00c045d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c045d0 ["INT_ADD", "register:40f0:8", ["const:c045d0:8", "const:4:8"]]
+ 00c045d0 ["CALLIND", null, ["register:0:8"]]
- 00c04534 bytes 00013fd6
+ 00c045d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0b089143b3703d724d5ae49a50aafc"></a>

### [`00c04658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04658.md) → [`00c046f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c046f4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE3putEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04658.md#insn-00c0467c) · [`00c046c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04658.md#insn-00c046c8) · [`00c046ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04658.md#insn-00c046ec)
- 新版 `00c04718`（命令位置の公開資料なし） · `00c04764`（命令位置の公開資料なし） · `00c04788`（命令位置の公開資料なし）

~~~diff
- 00c0467c ["INT_ADD", "register:40f0:8", ["const:c0467c:8", "const:4:8"]]
- 00c0467c ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c04718 ["INT_ADD", "register:40f0:8", ["const:c04718:8", "const:4:8"]]
+ 00c04718 ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c0467c bytes 61670194
+ 00c04718 bytes 6e670194
- 00c046c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c046c8 ["INT_ADD", "register:40f0:8", ["const:c046c8:8", "const:4:8"]]
- 00c046c8 ["CALLIND", null, ["register:0:8"]]
+ 00c04764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04764 ["INT_ADD", "register:40f0:8", ["const:c04764:8", "const:4:8"]]
+ 00c04764 ["CALLIND", null, ["register:0:8"]]
- 00c046c8 bytes 00013fd6
+ 00c04764 bytes 00013fd6
- 00c046ec ["INT_ADD", "register:40f0:8", ["const:c046ec:8", "const:4:8"]]
- 00c046ec ["CALL", null, ["callee:00c58370:8"]]
+ 00c04788 ["INT_ADD", "register:40f0:8", ["const:c04788:8", "const:4:8"]]
+ 00c04788 ["CALL", null, ["callee:00c58370:8"]]
- 00c046ec bytes ed4e0194
+ 00c04788 bytes fa4e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53890f1d53281aa8de64c198c53d6e79"></a>

### [`00c04758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04758.md) → [`00c047f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c047f4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5writeEPKwl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04758.md#insn-00c04784) · [`00c047b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04758.md#insn-00c047b4) · [`00c047d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04758.md#insn-00c047d4)
- 新版 `00c04820`（命令位置の公開資料なし） · `00c04850`（命令位置の公開資料なし） · `00c04870`（命令位置の公開資料なし）

~~~diff
- 00c04784 ["INT_ADD", "register:40f0:8", ["const:c04784:8", "const:4:8"]]
- 00c04784 ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c04820 ["INT_ADD", "register:40f0:8", ["const:c04820:8", "const:4:8"]]
+ 00c04820 ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c04784 bytes 1f670194
+ 00c04820 bytes 2c670194
- 00c047b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c047b4 ["INT_ADD", "register:40f0:8", ["const:c047b4:8", "const:4:8"]]
- 00c047b4 ["CALLIND", null, ["register:0:8"]]
+ 00c04850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04850 ["INT_ADD", "register:40f0:8", ["const:c04850:8", "const:4:8"]]
+ 00c04850 ["CALLIND", null, ["register:0:8"]]
- 00c047b4 bytes 00013fd6
+ 00c04850 bytes 00013fd6
- 00c047d4 ["INT_ADD", "register:40f0:8", ["const:c047d4:8", "const:4:8"]]
- 00c047d4 ["CALL", null, ["callee:00c58370:8"]]
+ 00c04870 ["INT_ADD", "register:40f0:8", ["const:c04870:8", "const:4:8"]]
+ 00c04870 ["CALL", null, ["callee:00c58370:8"]]
- 00c047d4 bytes b34e0194
+ 00c04870 bytes c04e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c85106def470f14411573b063f2b7a"></a>

### [`00c04844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04844.md) → [`00c048e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c048e0.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5tellpEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04844.md#insn-00c04894)
- 新版 `00c04930`（命令位置の公開資料なし）

~~~diff
- 00c04894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04894 ["INT_ADD", "register:40f0:8", ["const:c04894:8", "const:4:8"]]
- 00c04894 ["CALLIND", null, ["register:0:8"]]
+ 00c04930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04930 ["INT_ADD", "register:40f0:8", ["const:c04930:8", "const:4:8"]]
+ 00c04930 ["CALLIND", null, ["register:0:8"]]
- 00c04894 bytes 00013fd6
+ 00c04930 bytes 00013fd6
~~~


<a id="compare-a4e9088bdf4e48dbfa36ffdac154b3f7"></a>

### [`00c048a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c048a4.md) → [`00c04940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04940.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c048d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c048a4.md#insn-00c048d0) · [`00c04908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c048a4.md#insn-00c04908) · [`00c04928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c048a4.md#insn-00c04928)
- 新版 `00c0496c`（命令位置の公開資料なし） · `00c049a4`（命令位置の公開資料なし） · `00c049c4`（命令位置の公開資料なし）

~~~diff
- 00c048d0 ["INT_ADD", "register:40f0:8", ["const:c048d0:8", "const:4:8"]]
- 00c048d0 ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c0496c ["INT_ADD", "register:40f0:8", ["const:c0496c:8", "const:4:8"]]
+ 00c0496c ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c048d0 bytes cc660194
+ 00c0496c bytes d9660194
- 00c04908 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04908 ["INT_ADD", "register:40f0:8", ["const:c04908:8", "const:4:8"]]
- 00c04908 ["CALLIND", null, ["register:0:8"]]
+ 00c049a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c049a4 ["INT_ADD", "register:40f0:8", ["const:c049a4:8", "const:4:8"]]
+ 00c049a4 ["CALLIND", null, ["register:0:8"]]
- 00c04908 bytes 00013fd6
+ 00c049a4 bytes 00013fd6
- 00c04928 ["INT_ADD", "register:40f0:8", ["const:c04928:8", "const:4:8"]]
- 00c04928 ["CALL", null, ["callee:00c58370:8"]]
+ 00c049c4 ["INT_ADD", "register:40f0:8", ["const:c049c4:8", "const:4:8"]]
+ 00c049c4 ["CALL", null, ["callee:00c58370:8"]]
- 00c04928 bytes 5e4e0194
+ 00c049c4 bytes 6b4e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb5b3a16961c16952eeba140aefc3ea"></a>

### [`00c04968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04968.md) → [`00c04a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04a04.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5e400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e400.md) [`00c5e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04968.md#insn-00c04994) · [`00c049cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04968.md#insn-00c049cc) · [`00c049ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04968.md#insn-00c049ec)
- 新版 `00c04a30`（命令位置の公開資料なし） · `00c04a68`（命令位置の公開資料なし） · `00c04a88`（命令位置の公開資料なし）

~~~diff
- 00c04994 ["INT_ADD", "register:40f0:8", ["const:c04994:8", "const:4:8"]]
- 00c04994 ["CALL", null, ["callee:00c5e4d0:8"]]
+ 00c04a30 ["INT_ADD", "register:40f0:8", ["const:c04a30:8", "const:4:8"]]
+ 00c04a30 ["CALL", null, ["callee:00c5e4d0:8"]]
- 00c04994 bytes 9b660194
+ 00c04a30 bytes a8660194
- 00c049cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c049cc ["INT_ADD", "register:40f0:8", ["const:c049cc:8", "const:4:8"]]
- 00c049cc ["CALLIND", null, ["register:0:8"]]
+ 00c04a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04a68 ["INT_ADD", "register:40f0:8", ["const:c04a68:8", "const:4:8"]]
+ 00c04a68 ["CALLIND", null, ["register:0:8"]]
- 00c049cc bytes 00013fd6
+ 00c04a68 bytes 00013fd6
- 00c049ec ["INT_ADD", "register:40f0:8", ["const:c049ec:8", "const:4:8"]]
- 00c049ec ["CALL", null, ["callee:00c58370:8"]]
+ 00c04a88 ["INT_ADD", "register:40f0:8", ["const:c04a88:8", "const:4:8"]]
+ 00c04a88 ["CALL", null, ["callee:00c58370:8"]]
- 00c049ec bytes 2d4e0194
+ 00c04a88 bytes 3a4e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109d78758eb82fd7d7cb08b471e83cae"></a>

### [`00c04ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ad8.md) → [`00c04b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04b74.md) FUN_00c04b74

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c04a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04a2c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 1件 [`00c04ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04ac8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ad8.md#insn-00c04b90) · [`00c04c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ad8.md#insn-00c04c34) · [`00c04c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ad8.md#insn-00c04c48)
- 新版 `00c04c2c`（命令位置の公開資料なし） · `00c04cd0`（命令位置の公開資料なし） · `00c04ce4`（命令位置の公開資料なし）

~~~diff
- 00c04b90 ["INT_ADD", "register:40f0:8", ["const:c04b90:8", "const:4:8"]]
- 00c04b90 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c04c2c ["INT_ADD", "register:40f0:8", ["const:c04c2c:8", "const:4:8"]]
+ 00c04c2c ["CALL", null, ["callee:00c57f80:8"]]
- 00c04b90 bytes c84c0194
+ 00c04c2c bytes d54c0194
- 00c04c34 ["INT_ADD", "register:40f0:8", ["const:c04c34:8", "const:4:8"]]
- 00c04c34 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c04cd0 ["INT_ADD", "register:40f0:8", ["const:c04cd0:8", "const:4:8"]]
+ 00c04cd0 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c04c34 bytes e7560194
+ 00c04cd0 bytes f4560194
- 00c04c48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04c48 ["INT_ADD", "register:40f0:8", ["const:c04c48:8", "const:4:8"]]
- 00c04c48 ["CALLIND", null, ["register:0:8"]]
+ 00c04ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04ce4 ["INT_ADD", "register:40f0:8", ["const:c04ce4:8", "const:4:8"]]
+ 00c04ce4 ["CALLIND", null, ["register:0:8"]]
- 00c04c48 bytes 00013fd6
+ 00c04ce4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfa34a5a46af43a44690b67e17644e5f"></a>

### [`00c04cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04cac.md) → [`00c04d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04d48.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e470.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 1件 [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04cac.md#insn-00c04d64) · [`00c04e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04cac.md#insn-00c04e2c) · [`00c04e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04cac.md#insn-00c04e40)
- 新版 `00c04e00`（命令位置の公開資料なし） · `00c04ec8`（命令位置の公開資料なし） · `00c04edc`（命令位置の公開資料なし）

~~~diff
- 00c04d64 ["INT_ADD", "register:40f0:8", ["const:c04d64:8", "const:4:8"]]
- 00c04d64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00c04e00 ["INT_ADD", "register:40f0:8", ["const:c04e00:8", "const:4:8"]]
+ 00c04e00 ["CALL", null, ["callee:00c57f80:8"]]
- 00c04d64 bytes 534c0194
+ 00c04e00 bytes 604c0194
- 00c04e2c ["INT_ADD", "register:40f0:8", ["const:c04e2c:8", "const:4:8"]]
- 00c04e2c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c04ec8 ["INT_ADD", "register:40f0:8", ["const:c04ec8:8", "const:4:8"]]
+ 00c04ec8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c04e2c bytes 69560194
+ 00c04ec8 bytes 76560194
- 00c04e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04e40 ["INT_ADD", "register:40f0:8", ["const:c04e40:8", "const:4:8"]]
- 00c04e40 ["CALLIND", null, ["register:0:8"]]
+ 00c04edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c04edc ["INT_ADD", "register:40f0:8", ["const:c04edc:8", "const:4:8"]]
+ 00c04edc ["CALLIND", null, ["register:0:8"]]
- 00c04e40 bytes 00013fd6
+ 00c04edc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63411c7bf0999379930bc4dd25c52132"></a>

### [`00c04ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ea8.md) → [`00c04f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04f44.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4swapERS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c050dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ea8.md#insn-00c050dc) · [`00c050e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ea8.md#insn-00c050e8) · [`00c050fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c04/00c04ea8.md#insn-00c050fc)
- 新版 `00c05178`（命令位置の公開資料なし） · `00c05184`（命令位置の公開資料なし） · `00c05198`（命令位置の公開資料なし）

~~~diff
- 00c050dc ["INT_ADD", "register:40f0:8", ["const:c050dc:8", "const:4:8"]]
- 00c050dc ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c05178 ["INT_ADD", "register:40f0:8", ["const:c05178:8", "const:4:8"]]
+ 00c05178 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c050dc bytes bd550194
+ 00c05178 bytes ca550194
- 00c050e8 ["INT_ADD", "register:40f0:8", ["const:c050e8:8", "const:4:8"]]
- 00c050e8 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c05184 ["INT_ADD", "register:40f0:8", ["const:c05184:8", "const:4:8"]]
+ 00c05184 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c050e8 bytes ba550194
+ 00c05184 bytes c7550194
- 00c050fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c050fc ["INT_ADD", "register:40f0:8", ["const:c050fc:8", "const:4:8"]]
- 00c050fc ["CALLIND", null, ["register:0:8"]]
+ 00c05198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05198 ["INT_ADD", "register:40f0:8", ["const:c05198:8", "const:4:8"]]
+ 00c05198 ["CALLIND", null, ["register:0:8"]]
- 00c050fc bytes 00013fd6
+ 00c05198 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d374dc364061eb6061b72784b1111b2"></a>

### [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) → [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00bf21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md) [`00bf225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00bf2244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md) [`00bf22f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c051dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md#insn-00c051dc) · [`00c051f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md#insn-00c051f4)
- 新版 `00c05278`（命令位置の公開資料なし） · `00c05290`（命令位置の公開資料なし）

~~~diff
- 00c051dc ["INT_ADD", "register:40f0:8", ["const:c051dc:8", "const:4:8"]]
- 00c051dc ["CALL", null, ["callee:00bf22f8:8"]]
+ 00c05278 ["INT_ADD", "register:40f0:8", ["const:c05278:8", "const:4:8"]]
+ 00c05278 ["CALL", null, ["callee:00bf22f8:8"]]
- 00c051dc bytes 20b4ff97
+ 00c05278 bytes 20b4ff97
- 00c051f4 ["INT_ADD", "register:40f0:8", ["const:c051f4:8", "const:4:8"]]
- 00c051f4 ["CALL", null, ["callee:00bf2244:8"]]
+ 00c05290 ["INT_ADD", "register:40f0:8", ["const:c05290:8", "const:4:8"]]
+ 00c05290 ["CALL", null, ["callee:00bf2244:8"]]
- 00c051f4 bytes edb3ff97
+ 00c05290 bytes edb3ff97
~~~


<a id="compare-e3a458cf2d0f1100521e386e8d84294e"></a>

### [`00c0520c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0520c.md) → [`00c052a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c052a8.md) _ZNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md) [`00c5e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0520c.md#insn-00c05250) · [`00c0527c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0520c.md#insn-00c0527c)
- 新版 `00c052ec`（命令位置の公開資料なし） · `00c05318`（命令位置の公開資料なし）

~~~diff
- 00c05250 ["INT_ADD", "register:40f0:8", ["const:c05250:8", "const:4:8"]]
- 00c05250 ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c052ec ["INT_ADD", "register:40f0:8", ["const:c052ec:8", "const:4:8"]]
+ 00c052ec ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c05250 bytes 34640194
+ 00c052ec bytes 41640194
- 00c0527c ["INT_ADD", "register:40f0:8", ["const:c0527c:8", "const:4:8"]]
- 00c0527c ["CALL", null, ["callee:00c5e540:8"]]
+ 00c05318 ["INT_ADD", "register:40f0:8", ["const:c05318:8", "const:4:8"]]
+ 00c05318 ["CALL", null, ["callee:00c5e540:8"]]
- 00c0527c bytes 7d640194
+ 00c05318 bytes 8a640194
~~~


<a id="compare-1cbe611bc2806461362c5783f7873ae7"></a>

### [`00c05298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05298.md) → [`00c05334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05334.md) _ZNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md) [`00c5e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c052dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05298.md#insn-00c052dc) · [`00c05308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05298.md#insn-00c05308)
- 新版 `00c05378`（命令位置の公開資料なし） · `00c053a4`（命令位置の公開資料なし）

~~~diff
- 00c052dc ["INT_ADD", "register:40f0:8", ["const:c052dc:8", "const:4:8"]]
- 00c052dc ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c05378 ["INT_ADD", "register:40f0:8", ["const:c05378:8", "const:4:8"]]
+ 00c05378 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c052dc bytes 11640194
+ 00c05378 bytes 1e640194
- 00c05308 ["INT_ADD", "register:40f0:8", ["const:c05308:8", "const:4:8"]]
- 00c05308 ["CALL", null, ["callee:00c5e540:8"]]
+ 00c053a4 ["INT_ADD", "register:40f0:8", ["const:c053a4:8", "const:4:8"]]
+ 00c053a4 ["CALL", null, ["callee:00c5e540:8"]]
- 00c05308 bytes 5a640194
+ 00c053a4 bytes 67640194
~~~


<a id="compare-576b7e3e8a725d930b4c64a2a3e3ae5a"></a>

### [`00c05328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05328.md) → [`00c053c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c053c4.md) _ZNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e320.md) [`00c5e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0536c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05328.md#insn-00c0536c) · [`00c05398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05328.md#insn-00c05398)
- 新版 `00c05408`（命令位置の公開資料なし） · `00c05434`（命令位置の公開資料なし）

~~~diff
- 00c0536c ["INT_ADD", "register:40f0:8", ["const:c0536c:8", "const:4:8"]]
- 00c0536c ["CALL", null, ["callee:00c5e3f0:8"]]
+ 00c05408 ["INT_ADD", "register:40f0:8", ["const:c05408:8", "const:4:8"]]
+ 00c05408 ["CALL", null, ["callee:00c5e3f0:8"]]
- 00c0536c bytes ed630194
+ 00c05408 bytes fa630194
- 00c05398 ["INT_ADD", "register:40f0:8", ["const:c05398:8", "const:4:8"]]
- 00c05398 ["CALL", null, ["callee:00c5e540:8"]]
+ 00c05434 ["INT_ADD", "register:40f0:8", ["const:c05434:8", "const:4:8"]]
+ 00c05434 ["CALL", null, ["callee:00c5e540:8"]]
- 00c05398 bytes 36640194
+ 00c05434 bytes 43640194
~~~


<a id="compare-4f4db743eaecf48c58a63889aab92728"></a>

### [`00c053b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md) → [`00c05450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05450.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md#insn-00c0540c) · [`00c0541c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md#insn-00c0541c) · [`00c05438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md#insn-00c05438)
- 新版 `00c054a8`（命令位置の公開資料なし） · `00c054b8`（命令位置の公開資料なし） · `00c054d4`（命令位置の公開資料なし）

~~~diff
- 00c0540c ["INT_ADD", "register:40f0:8", ["const:c0540c:8", "const:4:8"]]
- 00c0540c ["CALL", null, ["callee:00c05e68:8"]]
+ 00c054a8 ["INT_ADD", "register:40f0:8", ["const:c054a8:8", "const:4:8"]]
+ 00c054a8 ["CALL", null, ["callee:00c05e68:8"]]
- 00c0540c bytes 70020094
+ 00c054a8 bytes 70020094
- 00c0541c ["INT_ADD", "register:40f0:8", ["const:c0541c:8", "const:4:8"]]
- 00c0541c ["CALL", null, ["callee:00c5a160:8"]]
+ 00c054b8 ["INT_ADD", "register:40f0:8", ["const:c054b8:8", "const:4:8"]]
+ 00c054b8 ["CALL", null, ["callee:00c5a160:8"]]
- 00c0541c bytes 1d530194
+ 00c054b8 bytes 2a530194
- 00c05438 ["INT_ADD", "register:40f0:8", ["const:c05438:8", "const:4:8"]]
- 00c05438 ["CALL", null, ["callee:00c5a130:8"]]
+ 00c054d4 ["INT_ADD", "register:40f0:8", ["const:c054d4:8", "const:4:8"]]
+ 00c054d4 ["CALL", null, ["callee:00c5a130:8"]]
- 00c05438 bytes 0a530194
+ 00c054d4 bytes 17530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df34af9b6caa04f78301ebf3dab4b4b"></a>

### [`00c05464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md) → [`00c05500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05500.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c054c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md#insn-00c054c8) · [`00c054d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md#insn-00c054d8) · [`00c054f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md#insn-00c054f4)
- 新版 `00c05564`（命令位置の公開資料なし） · `00c05574`（命令位置の公開資料なし） · `00c05590`（命令位置の公開資料なし）

~~~diff
- 00c054c8 ["INT_ADD", "register:40f0:8", ["const:c054c8:8", "const:4:8"]]
- 00c054c8 ["CALL", null, ["callee:00c05e68:8"]]
+ 00c05564 ["INT_ADD", "register:40f0:8", ["const:c05564:8", "const:4:8"]]
+ 00c05564 ["CALL", null, ["callee:00c05e68:8"]]
- 00c054c8 bytes 41020094
+ 00c05564 bytes 41020094
- 00c054d8 ["INT_ADD", "register:40f0:8", ["const:c054d8:8", "const:4:8"]]
- 00c054d8 ["CALL", null, ["callee:00c5a160:8"]]
+ 00c05574 ["INT_ADD", "register:40f0:8", ["const:c05574:8", "const:4:8"]]
+ 00c05574 ["CALL", null, ["callee:00c5a160:8"]]
- 00c054d8 bytes ee520194
+ 00c05574 bytes fb520194
- 00c054f4 ["INT_ADD", "register:40f0:8", ["const:c054f4:8", "const:4:8"]]
- 00c054f4 ["CALL", null, ["callee:00c5a130:8"]]
+ 00c05590 ["INT_ADD", "register:40f0:8", ["const:c05590:8", "const:4:8"]]
+ 00c05590 ["CALL", null, ["callee:00c5a130:8"]]
- 00c054f4 bytes db520194
+ 00c05590 bytes e8520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-262ccd85381e71cf56b0382f7f12b217"></a>

### [`00c05520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md) → [`00c055bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c055bc.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md#insn-00c05578) · [`00c05588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md#insn-00c05588) · [`00c055a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md#insn-00c055a4)
- 新版 `00c05614`（命令位置の公開資料なし） · `00c05624`（命令位置の公開資料なし） · `00c05640`（命令位置の公開資料なし）

~~~diff
- 00c05578 ["INT_ADD", "register:40f0:8", ["const:c05578:8", "const:4:8"]]
- 00c05578 ["CALL", null, ["callee:00c05e68:8"]]
+ 00c05614 ["INT_ADD", "register:40f0:8", ["const:c05614:8", "const:4:8"]]
+ 00c05614 ["CALL", null, ["callee:00c05e68:8"]]
- 00c05578 bytes 15020094
+ 00c05614 bytes 15020094
- 00c05588 ["INT_ADD", "register:40f0:8", ["const:c05588:8", "const:4:8"]]
- 00c05588 ["CALL", null, ["callee:00c5a160:8"]]
+ 00c05624 ["INT_ADD", "register:40f0:8", ["const:c05624:8", "const:4:8"]]
+ 00c05624 ["CALL", null, ["callee:00c5a160:8"]]
- 00c05588 bytes c2520194
+ 00c05624 bytes cf520194
- 00c055a4 ["INT_ADD", "register:40f0:8", ["const:c055a4:8", "const:4:8"]]
- 00c055a4 ["CALL", null, ["callee:00c5a130:8"]]
+ 00c05640 ["INT_ADD", "register:40f0:8", ["const:c05640:8", "const:4:8"]]
+ 00c05640 ["CALL", null, ["callee:00c5a130:8"]]
- 00c055a4 bytes af520194
+ 00c05640 bytes bc520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18395f8001e9fba5686af9bf17332498"></a>

### [`00c055d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md) → [`00c0566c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0566c.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md#insn-00c05634) · [`00c05644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md#insn-00c05644) · [`00c05660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md#insn-00c05660)
- 新版 `00c056d0`（命令位置の公開資料なし） · `00c056e0`（命令位置の公開資料なし） · `00c056fc`（命令位置の公開資料なし）

~~~diff
- 00c05634 ["INT_ADD", "register:40f0:8", ["const:c05634:8", "const:4:8"]]
- 00c05634 ["CALL", null, ["callee:00c05e68:8"]]
+ 00c056d0 ["INT_ADD", "register:40f0:8", ["const:c056d0:8", "const:4:8"]]
+ 00c056d0 ["CALL", null, ["callee:00c05e68:8"]]
- 00c05634 bytes e6010094
+ 00c056d0 bytes e6010094
- 00c05644 ["INT_ADD", "register:40f0:8", ["const:c05644:8", "const:4:8"]]
- 00c05644 ["CALL", null, ["callee:00c5a160:8"]]
+ 00c056e0 ["INT_ADD", "register:40f0:8", ["const:c056e0:8", "const:4:8"]]
+ 00c056e0 ["CALL", null, ["callee:00c5a160:8"]]
- 00c05644 bytes 93520194
+ 00c056e0 bytes a0520194
- 00c05660 ["INT_ADD", "register:40f0:8", ["const:c05660:8", "const:4:8"]]
- 00c05660 ["CALL", null, ["callee:00c5a130:8"]]
+ 00c056fc ["INT_ADD", "register:40f0:8", ["const:c056fc:8", "const:4:8"]]
+ 00c056fc ["CALL", null, ["callee:00c5a130:8"]]
- 00c05660 bytes 80520194
+ 00c056fc bytes 8d520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b49163c4354c6923f26be388080465"></a>

### [`00c05a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05a18.md) → [`00c05ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ab4.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE5closeEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05a18.md#insn-00c05a40) · [`00c05a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05a18.md#insn-00c05a4c) · [`00c05a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05a18.md#insn-00c05a74)
- 新版 `00c05adc`（命令位置の公開資料なし） · `00c05ae8`（命令位置の公開資料なし） · `00c05b10`（命令位置の公開資料なし）

~~~diff
- 00c05a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c05a40 ["INT_ADD", "register:40f0:8", ["const:c05a40:8", "const:4:8"]]
- 00c05a40 ["CALLIND", null, ["register:0:8"]]
+ 00c05adc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05adc ["INT_ADD", "register:40f0:8", ["const:c05adc:8", "const:4:8"]]
+ 00c05adc ["CALLIND", null, ["register:0:8"]]
- 00c05a40 bytes 00013fd6
+ 00c05adc bytes 00013fd6
- 00c05a4c ["INT_ADD", "register:40f0:8", ["const:c05a4c:8", "const:4:8"]]
- 00c05a4c ["CALL", null, ["callee:00c5a0d0:8"]]
+ 00c05ae8 ["INT_ADD", "register:40f0:8", ["const:c05ae8:8", "const:4:8"]]
+ 00c05ae8 ["CALL", null, ["callee:00c5a0d0:8"]]
- 00c05a4c bytes 6d510194
+ 00c05ae8 bytes 7a510194
- 00c05a74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c05a74 ["INT_ADD", "register:40f0:8", ["const:c05a74:8", "const:4:8"]]
- 00c05a74 ["CALLIND", null, ["register:0:8"]]
+ 00c05b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05b10 ["INT_ADD", "register:40f0:8", ["const:c05b10:8", "const:4:8"]]
+ 00c05b10 ["CALLIND", null, ["register:0:8"]]
- 00c05a74 bytes 00013fd6
+ 00c05b10 bytes 00013fd6
~~~


<a id="compare-7a063d9ad54abd48695789f3f2820e4a"></a>

### [`00c05aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05aa4.md) → [`00c05b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b40.md) FUN_00c05b40

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05aa4.md#insn-00c05ab8)
- 新版 `00c05b54`（命令位置の公開資料なし）

~~~diff
- 00c05ab8 ["INT_ADD", "register:40f0:8", ["const:c05ab8:8", "const:4:8"]]
- 00c05ab8 ["CALL", null, ["callee:00c58ff0:8"]]
+ 00c05b54 ["INT_ADD", "register:40f0:8", ["const:c05b54:8", "const:4:8"]]
+ 00c05b54 ["CALL", null, ["callee:00c58ff0:8"]]
- 00c05ab8 bytes 1a4d0194
+ 00c05b54 bytes 274d0194
~~~


<a id="compare-12735656ff9ed71cf825ed9d86c086d0"></a>

### [`00c05ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ad0.md) → [`00c05b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b6c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ad0.md#insn-00c05af4) · [`00c05b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ad0.md#insn-00c05b00) · [`00c05b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ad0.md#insn-00c05b0c)
- 新版 `00c05b90`（命令位置の公開資料なし） · `00c05b9c`（命令位置の公開資料なし） · `00c05ba8`（命令位置の公開資料なし）

~~~diff
- 00c05af4 ["INT_ADD", "register:40f0:8", ["const:c05af4:8", "const:4:8"]]
- 00c05af4 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00c05b90 ["INT_ADD", "register:40f0:8", ["const:c05b90:8", "const:4:8"]]
+ 00c05b90 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00c05af4 bytes 37530194
+ 00c05b90 bytes 44530194
- 00c05b00 ["INT_ADD", "register:40f0:8", ["const:c05b00:8", "const:4:8"]]
- 00c05b00 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00c05b9c ["INT_ADD", "register:40f0:8", ["const:c05b9c:8", "const:4:8"]]
+ 00c05b9c ["CALL", null, ["callee:00c5e3b0:8"]]
- 00c05b00 bytes f8610194
+ 00c05b9c bytes 05620194
- 00c05b0c ["INT_ADD", "register:40f0:8", ["const:c05b0c:8", "const:4:8"]]
- 00c05b0c ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00c05ba8 ["INT_ADD", "register:40f0:8", ["const:c05ba8:8", "const:4:8"]]
+ 00c05ba8 ["CALL", null, ["callee:00c5e3b0:8"]]
- 00c05b0c bytes f5610194
+ 00c05ba8 bytes 02620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b93866e49ef3504f1138f7d3d9d4757"></a>

### [`00c06810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06810.md) → [`00c068ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c068ac.md) FUN_00c068ac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06810.md#insn-00c06824)
- 新版 `00c068c0`（命令位置の公開資料なし）

~~~diff
- 00c06824 ["INT_ADD", "register:40f0:8", ["const:c06824:8", "const:4:8"]]
- 00c06824 ["CALL", null, ["callee:00c58070:8"]]
+ 00c068c0 ["INT_ADD", "register:40f0:8", ["const:c068c0:8", "const:4:8"]]
+ 00c068c0 ["CALL", null, ["callee:00c58070:8"]]
- 00c06824 bytes df450194
+ 00c068c0 bytes ec450194
~~~


<a id="compare-18ca1255797b28debb2de8e2370a31d2"></a>

### [`00c068d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068d4.md) → [`00c06970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06970.md) FUN_00c06970

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068d4.md#insn-00c06914) · [`00c06974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068d4.md#insn-00c06974) · [`00c069c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068d4.md#insn-00c069c0)
- 新版 `00c069b0`（命令位置の公開資料なし） · `00c06a10`（命令位置の公開資料なし） · `00c06a5c`（命令位置の公開資料なし）

~~~diff
- 00c06914 ["INT_ADD", "register:40f0:8", ["const:c06914:8", "const:4:8"]]
- 00c06914 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c069b0 ["INT_ADD", "register:40f0:8", ["const:c069b0:8", "const:4:8"]]
+ 00c069b0 ["CALL", null, ["callee:00c5e570:8"]]
- 00c06914 bytes e35e0194
+ 00c069b0 bytes f05e0194
- 00c06974 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06974 ["INT_ADD", "register:40f0:8", ["const:c06974:8", "const:4:8"]]
- 00c06974 ["CALLIND", null, ["register:0:8"]]
+ 00c06a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06a10 ["INT_ADD", "register:40f0:8", ["const:c06a10:8", "const:4:8"]]
+ 00c06a10 ["CALLIND", null, ["register:0:8"]]
- 00c06974 bytes 00013fd6
+ 00c06a10 bytes 00013fd6
- 00c069c0 ["INT_ADD", "register:40f0:8", ["const:c069c0:8", "const:4:8"]]
- 00c069c0 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c06a5c ["INT_ADD", "register:40f0:8", ["const:c06a5c:8", "const:4:8"]]
+ 00c06a5c ["CALL", null, ["callee:00c5e570:8"]]
- 00c069c0 bytes b85e0194
+ 00c06a5c bytes c55e0194
~~~


<a id="compare-d6043df1cff588daf0480416d89dfa22"></a>

### [`00c069fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c069fc.md) → [`00c06a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06a98.md) FUN_00c06a98

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c068bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068bc.md) [`00c068c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c068c8.md) · 呼出先 2件 [`00c5e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4a0.md) [`00c5e4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4b0.md)
- 新版 呼出元 2件 [`00c06958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06958.md) [`00c06964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06964.md) · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c069fc.md#insn-00c06a4c) · [`00c06a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c069fc.md#insn-00c06a80) · [`00c06acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c069fc.md#insn-00c06acc)
- 新版 `00c06ae8`（命令位置の公開資料なし） · `00c06b1c`（命令位置の公開資料なし） · `00c06b68`（命令位置の公開資料なし）

~~~diff
- 00c06a4c ["INT_ADD", "register:40f0:8", ["const:c06a4c:8", "const:4:8"]]
- 00c06a4c ["CALL", null, ["callee:00c5e580:8"]]
+ 00c06ae8 ["INT_ADD", "register:40f0:8", ["const:c06ae8:8", "const:4:8"]]
+ 00c06ae8 ["CALL", null, ["callee:00c5e580:8"]]
- 00c06a4c bytes 995e0194
+ 00c06ae8 bytes a65e0194
- 00c06a80 ["INT_ADD", "register:40f0:8", ["const:c06a80:8", "const:4:8"]]
- 00c06a80 ["CALL", null, ["callee:00c5e580:8"]]
+ 00c06b1c ["INT_ADD", "register:40f0:8", ["const:c06b1c:8", "const:4:8"]]
+ 00c06b1c ["CALL", null, ["callee:00c5e580:8"]]
- 00c06a80 bytes 8c5e0194
+ 00c06b1c bytes 995e0194
- 00c06acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06acc ["INT_ADD", "register:40f0:8", ["const:c06acc:8", "const:4:8"]]
- 00c06acc ["CALLIND", null, ["register:0:8"]]
+ 00c06b68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06b68 ["INT_ADD", "register:40f0:8", ["const:c06b68:8", "const:4:8"]]
+ 00c06b68 ["CALLIND", null, ["register:0:8"]]
- 00c06acc bytes 00013fd6
+ 00c06b68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067736df691811765342340602ac0183"></a>

### [`00c06ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ba4.md) → [`00c06c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06c40.md) FUN_00c06c40

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ba4.md#insn-00c06bb8)
- 新版 `00c06c54`（命令位置の公開資料なし）

~~~diff
- 00c06bb8 ["INT_ADD", "register:40f0:8", ["const:c06bb8:8", "const:4:8"]]
- 00c06bb8 ["CALL", null, ["callee:00c58070:8"]]
+ 00c06c54 ["INT_ADD", "register:40f0:8", ["const:c06c54:8", "const:4:8"]]
+ 00c06c54 ["CALL", null, ["callee:00c58070:8"]]
- 00c06bb8 bytes fa440194
+ 00c06c54 bytes 07450194
~~~


<a id="compare-c7923a86405b45d5b7c5d624eba5dde8"></a>

### [`00c06c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06c2c.md) → [`00c06cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06cc8.md) FUN_00c06cc8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06c2c.md#insn-00c06c64) · [`00c06c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06c2c.md#insn-00c06c84) · [`00c06cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06c2c.md#insn-00c06cac)
- 新版 `00c06d00`（命令位置の公開資料なし） · `00c06d20`（命令位置の公開資料なし） · `00c06d48`（命令位置の公開資料なし）

~~~diff
- 00c06c64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06c64 ["INT_ADD", "register:40f0:8", ["const:c06c64:8", "const:4:8"]]
- 00c06c64 ["CALLIND", null, ["register:0:8"]]
+ 00c06d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06d00 ["INT_ADD", "register:40f0:8", ["const:c06d00:8", "const:4:8"]]
+ 00c06d00 ["CALLIND", null, ["register:0:8"]]
- 00c06c64 bytes 00013fd6
+ 00c06d00 bytes 00013fd6
- 00c06c84 ["INT_ADD", "register:40f0:8", ["const:c06c84:8", "const:4:8"]]
- 00c06c84 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c06d20 ["INT_ADD", "register:40f0:8", ["const:c06d20:8", "const:4:8"]]
+ 00c06d20 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c06c84 bytes 674d0194
+ 00c06d20 bytes 744d0194
- 00c06cac ["INT_ADD", "register:40f0:8", ["const:c06cac:8", "const:4:8"]]
- 00c06cac ["CALL", null, ["callee:00c5a280:8"]]
+ 00c06d48 ["INT_ADD", "register:40f0:8", ["const:c06d48:8", "const:4:8"]]
+ 00c06d48 ["CALL", null, ["callee:00c5a280:8"]]
- 00c06cac bytes 414d0194
+ 00c06d48 bytes 4e4d0194
~~~


<a id="compare-01926d55141e64a8cbcdea864f1c4f3d"></a>

### [`00c06cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06cd0.md) → [`00c06d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06d6c.md) FUN_00c06d6c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06cd0.md#insn-00c06d38)
- 新版 `00c06dd4`（命令位置の公開資料なし）

~~~diff
- 00c06d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06d38 ["INT_ADD", "register:40f0:8", ["const:c06d38:8", "const:4:8"]]
- 00c06d38 ["CALLIND", null, ["register:0:8"]]
+ 00c06dd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06dd4 ["INT_ADD", "register:40f0:8", ["const:c06dd4:8", "const:4:8"]]
+ 00c06dd4 ["CALLIND", null, ["register:0:8"]]
- 00c06d38 bytes 00013fd6
+ 00c06dd4 bytes 00013fd6
~~~


<a id="compare-dde5e473e1b75cb2d737000223ae45e8"></a>

### [`00c06d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06d74.md) → [`00c06e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06e10.md) FUN_00c06e10

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06d74.md#insn-00c06dc0) · [`00c06e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06d74.md#insn-00c06e0c) · [`00c06e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06d74.md#insn-00c06e48)
- 新版 `00c06e5c`（命令位置の公開資料なし） · `00c06ea8`（命令位置の公開資料なし） · `00c06ee4`（命令位置の公開資料なし）

~~~diff
- 00c06dc0 ["INT_ADD", "register:40f0:8", ["const:c06dc0:8", "const:4:8"]]
- 00c06dc0 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c06e5c ["INT_ADD", "register:40f0:8", ["const:c06e5c:8", "const:4:8"]]
+ 00c06e5c ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c06dc0 bytes 184d0194
+ 00c06e5c bytes 254d0194
- 00c06e0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06e0c ["INT_ADD", "register:40f0:8", ["const:c06e0c:8", "const:4:8"]]
- 00c06e0c ["CALLIND", null, ["register:0:8"]]
+ 00c06ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06ea8 ["INT_ADD", "register:40f0:8", ["const:c06ea8:8", "const:4:8"]]
+ 00c06ea8 ["CALLIND", null, ["register:0:8"]]
- 00c06e0c bytes 00013fd6
+ 00c06ea8 bytes 00013fd6
- 00c06e48 ["INT_ADD", "register:40f0:8", ["const:c06e48:8", "const:4:8"]]
- 00c06e48 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c06ee4 ["INT_ADD", "register:40f0:8", ["const:c06ee4:8", "const:4:8"]]
+ 00c06ee4 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c06e48 bytes f64c0194
+ 00c06ee4 bytes 034d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b63e8991e7140cdee07103caf7813f9f"></a>

### [`00c06ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ea4.md) → [`00c06f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06f40.md) FUN_00c06f40

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ea4.md#insn-00c06eb8)
- 新版 `00c06f54`（命令位置の公開資料なし）

~~~diff
- 00c06eb8 ["INT_ADD", "register:40f0:8", ["const:c06eb8:8", "const:4:8"]]
- 00c06eb8 ["CALL", null, ["callee:00c5e490:8"]]
+ 00c06f54 ["INT_ADD", "register:40f0:8", ["const:c06f54:8", "const:4:8"]]
+ 00c06f54 ["CALL", null, ["callee:00c5e490:8"]]
- 00c06eb8 bytes 425d0194
+ 00c06f54 bytes 4f5d0194
~~~


<a id="compare-23eb471b65397b9d4da740aca53956c9"></a>

### [`00c06f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f68.md) → [`00c07004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07004.md) FUN_00c07004

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4a0.md) [`00c5e4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f68.md#insn-00c06fa8) · [`00c07008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f68.md#insn-00c07008) · [`00c07054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f68.md#insn-00c07054)
- 新版 `00c07044`（命令位置の公開資料なし） · `00c070a4`（命令位置の公開資料なし） · `00c070f0`（命令位置の公開資料なし）

~~~diff
- 00c06fa8 ["INT_ADD", "register:40f0:8", ["const:c06fa8:8", "const:4:8"]]
- 00c06fa8 ["CALL", null, ["callee:00c5e590:8"]]
+ 00c07044 ["INT_ADD", "register:40f0:8", ["const:c07044:8", "const:4:8"]]
+ 00c07044 ["CALL", null, ["callee:00c5e590:8"]]
- 00c06fa8 bytes 465d0194
+ 00c07044 bytes 535d0194
- 00c07008 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c07008 ["INT_ADD", "register:40f0:8", ["const:c07008:8", "const:4:8"]]
- 00c07008 ["CALLIND", null, ["register:0:8"]]
+ 00c070a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c070a4 ["INT_ADD", "register:40f0:8", ["const:c070a4:8", "const:4:8"]]
+ 00c070a4 ["CALLIND", null, ["register:0:8"]]
- 00c07008 bytes 00013fd6
+ 00c070a4 bytes 00013fd6
- 00c07054 ["INT_ADD", "register:40f0:8", ["const:c07054:8", "const:4:8"]]
- 00c07054 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c070f0 ["INT_ADD", "register:40f0:8", ["const:c070f0:8", "const:4:8"]]
+ 00c070f0 ["CALL", null, ["callee:00c5e570:8"]]
- 00c07054 bytes 135d0194
+ 00c070f0 bytes 205d0194
~~~


<a id="compare-b8f355e65ab8c75c1e5dccf242c4f9cf"></a>

### [`00c07090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07090.md) → [`00c0712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0712c.md) FUN_00c0712c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c06f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f50.md) [`00c06f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06f5c.md) · 呼出先 4件 [`00c5e4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4a0.md) [`00c5e4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4b0.md) [`00c5e4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4c0.md) [`00c5e4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4d0.md)
- 新版 呼出元 2件 [`00c06fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06fec.md) [`00c06ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06ff8.md) · 呼出先 4件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e580.md) [`00c5e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e590.md) [`00c5e5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c070e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07090.md#insn-00c070e0) · [`00c07110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07090.md#insn-00c07110) · [`00c0715c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07090.md#insn-00c0715c)
- 新版 `00c0717c`（命令位置の公開資料なし） · `00c071ac`（命令位置の公開資料なし） · `00c071f8`（命令位置の公開資料なし）

~~~diff
- 00c070e0 ["INT_ADD", "register:40f0:8", ["const:c070e0:8", "const:4:8"]]
- 00c070e0 ["CALL", null, ["callee:00c5e5a0:8"]]
+ 00c0717c ["INT_ADD", "register:40f0:8", ["const:c0717c:8", "const:4:8"]]
+ 00c0717c ["CALL", null, ["callee:00c5e5a0:8"]]
- 00c070e0 bytes fc5c0194
+ 00c0717c bytes 095d0194
- 00c07110 ["INT_ADD", "register:40f0:8", ["const:c07110:8", "const:4:8"]]
- 00c07110 ["CALL", null, ["callee:00c5e580:8"]]
+ 00c071ac ["INT_ADD", "register:40f0:8", ["const:c071ac:8", "const:4:8"]]
+ 00c071ac ["CALL", null, ["callee:00c5e580:8"]]
- 00c07110 bytes e85c0194
+ 00c071ac bytes f55c0194
- 00c0715c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0715c ["INT_ADD", "register:40f0:8", ["const:c0715c:8", "const:4:8"]]
- 00c0715c ["CALLIND", null, ["register:0:8"]]
+ 00c071f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c071f8 ["INT_ADD", "register:40f0:8", ["const:c071f8:8", "const:4:8"]]
+ 00c071f8 ["CALLIND", null, ["register:0:8"]]
- 00c0715c bytes 00013fd6
+ 00c071f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4005fde30adf174930a0b97ef14aad2"></a>

### [`00c07230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07230.md) → [`00c072cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c072cc.md) FUN_00c072cc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07230.md#insn-00c07244)
- 新版 `00c072e0`（命令位置の公開資料なし）

~~~diff
- 00c07244 ["INT_ADD", "register:40f0:8", ["const:c07244:8", "const:4:8"]]
- 00c07244 ["CALL", null, ["callee:00c5e490:8"]]
+ 00c072e0 ["INT_ADD", "register:40f0:8", ["const:c072e0:8", "const:4:8"]]
+ 00c072e0 ["CALL", null, ["callee:00c5e490:8"]]
- 00c07244 bytes 5f5c0194
+ 00c072e0 bytes 6c5c0194
~~~


<a id="compare-77689481c66dfbda853511a4ad17186e"></a>

### [`00c072b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c072b8.md) → [`00c07354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07354.md) FUN_00c07354

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c072f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c072b8.md#insn-00c072f0) · [`00c07310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c072b8.md#insn-00c07310) · [`00c07338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c072b8.md#insn-00c07338)
- 新版 `00c0738c`（命令位置の公開資料なし） · `00c073ac`（命令位置の公開資料なし） · `00c073d4`（命令位置の公開資料なし）

~~~diff
- 00c072f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c072f0 ["INT_ADD", "register:40f0:8", ["const:c072f0:8", "const:4:8"]]
- 00c072f0 ["CALLIND", null, ["register:0:8"]]
+ 00c0738c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0738c ["INT_ADD", "register:40f0:8", ["const:c0738c:8", "const:4:8"]]
+ 00c0738c ["CALLIND", null, ["register:0:8"]]
- 00c072f0 bytes 00013fd6
+ 00c0738c bytes 00013fd6
- 00c07310 ["INT_ADD", "register:40f0:8", ["const:c07310:8", "const:4:8"]]
- 00c07310 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c073ac ["INT_ADD", "register:40f0:8", ["const:c073ac:8", "const:4:8"]]
+ 00c073ac ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c07310 bytes c44b0194
+ 00c073ac bytes d14b0194
- 00c07338 ["INT_ADD", "register:40f0:8", ["const:c07338:8", "const:4:8"]]
- 00c07338 ["CALL", null, ["callee:00c5a280:8"]]
+ 00c073d4 ["INT_ADD", "register:40f0:8", ["const:c073d4:8", "const:4:8"]]
+ 00c073d4 ["CALL", null, ["callee:00c5a280:8"]]
- 00c07338 bytes 9e4b0194
+ 00c073d4 bytes ab4b0194
~~~


<a id="compare-56a8d0c40db6c9c2de5024b7e526b9f8"></a>

### [`00c0735c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0735c.md) → [`00c073f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c073f8.md) FUN_00c073f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c073c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0735c.md#insn-00c073c4)
- 新版 `00c07460`（命令位置の公開資料なし）

~~~diff
- 00c073c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c073c4 ["INT_ADD", "register:40f0:8", ["const:c073c4:8", "const:4:8"]]
- 00c073c4 ["CALLIND", null, ["register:0:8"]]
+ 00c07460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07460 ["INT_ADD", "register:40f0:8", ["const:c07460:8", "const:4:8"]]
+ 00c07460 ["CALLIND", null, ["register:0:8"]]
- 00c073c4 bytes 00013fd6
+ 00c07460 bytes 00013fd6
~~~


<a id="compare-2606806ff2a90f71af3a07729da76fde"></a>

### [`00c07400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07400.md) → [`00c0749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0749c.md) FUN_00c0749c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md) [`00c5e4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5e5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07400.md#insn-00c07440) · [`00c0748c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07400.md#insn-00c0748c) · [`00c074c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07400.md#insn-00c074c8)
- 新版 `00c074dc`（命令位置の公開資料なし） · `00c07528`（命令位置の公開資料なし） · `00c07564`（命令位置の公開資料なし）

~~~diff
- 00c07440 ["INT_ADD", "register:40f0:8", ["const:c07440:8", "const:4:8"]]
- 00c07440 ["CALL", null, ["callee:00c5e5b0:8"]]
+ 00c074dc ["INT_ADD", "register:40f0:8", ["const:c074dc:8", "const:4:8"]]
+ 00c074dc ["CALL", null, ["callee:00c5e5b0:8"]]
- 00c07440 bytes 285c0194
+ 00c074dc bytes 355c0194
- 00c0748c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0748c ["INT_ADD", "register:40f0:8", ["const:c0748c:8", "const:4:8"]]
- 00c0748c ["CALLIND", null, ["register:0:8"]]
+ 00c07528 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07528 ["INT_ADD", "register:40f0:8", ["const:c07528:8", "const:4:8"]]
+ 00c07528 ["CALLIND", null, ["register:0:8"]]
- 00c0748c bytes 00013fd6
+ 00c07528 bytes 00013fd6
- 00c074c8 ["INT_ADD", "register:40f0:8", ["const:c074c8:8", "const:4:8"]]
- 00c074c8 ["CALL", null, ["callee:00c5a2f0:8"]]
+ 00c07564 ["INT_ADD", "register:40f0:8", ["const:c07564:8", "const:4:8"]]
+ 00c07564 ["CALL", null, ["callee:00c5a2f0:8"]]
- 00c074c8 bytes 564b0194
+ 00c07564 bytes 634b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e580add77b620a5b5a7bc06b85e7d32"></a>

### [`00c07570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07570.md) → [`00c0760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0760c.md) _ZNSt6__ndk17collateIcED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e500.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07570.md#insn-00c07584)
- 新版 `00c07620`（命令位置の公開資料なし）

~~~diff
- 00c07584 ["INT_ADD", "register:40f0:8", ["const:c07584:8", "const:4:8"]]
- 00c07584 ["CALL", null, ["callee:00c5e5d0:8"]]
+ 00c07620 ["INT_ADD", "register:40f0:8", ["const:c07620:8", "const:4:8"]]
+ 00c07620 ["CALL", null, ["callee:00c5e5d0:8"]]
- 00c07584 bytes df5b0194
+ 00c07620 bytes ec5b0194
~~~


<a id="compare-1d9d04649a807cd836a335df1e1fe69b"></a>

### [`00c07600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07600.md) → [`00c0769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0769c.md) _ZNKSt6__ndk17collateIcE12do_transformEPKcS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07600.md#insn-00c07668) · [`00c07690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07600.md#insn-00c07690) · [`00c076b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07600.md#insn-00c076b8)
- 新版 `00c07704`（命令位置の公開資料なし） · `00c0772c`（命令位置の公開資料なし） · `00c07754`（命令位置の公開資料なし）

~~~diff
- 00c07668 ["INT_ADD", "register:40f0:8", ["const:c07668:8", "const:4:8"]]
- 00c07668 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c07704 ["INT_ADD", "register:40f0:8", ["const:c07704:8", "const:4:8"]]
+ 00c07704 ["CALL", null, ["callee:00c57f60:8"]]
- 00c07668 bytes 0a420194
+ 00c07704 bytes 17420194
- 00c07690 ["INT_ADD", "register:40f0:8", ["const:c07690:8", "const:4:8"]]
- 00c07690 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c0772c ["INT_ADD", "register:40f0:8", ["const:c0772c:8", "const:4:8"]]
+ 00c0772c ["CALL", null, ["callee:00c580d0:8"]]
- 00c07690 bytes 5c420194
+ 00c0772c bytes 69420194
- 00c076b8 ["INT_ADD", "register:40f0:8", ["const:c076b8:8", "const:4:8"]]
- 00c076b8 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00c07754 ["INT_ADD", "register:40f0:8", ["const:c07754:8", "const:4:8"]]
+ 00c07754 ["CALL", null, ["callee:0043b7a4:8"]]
- 00c076b8 bytes 2bd0e097
+ 00c07754 bytes 14d0e097
~~~


<a id="compare-c808c389f82856123fd6db04318fb5c7"></a>

### [`00c076fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c076fc.md) → [`00c07798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07798.md) _ZNSt6__ndk17collateIwED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e510.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c076fc.md#insn-00c07710)
- 新版 `00c077ac`（命令位置の公開資料なし）

~~~diff
- 00c07710 ["INT_ADD", "register:40f0:8", ["const:c07710:8", "const:4:8"]]
- 00c07710 ["CALL", null, ["callee:00c5e5e0:8"]]
+ 00c077ac ["INT_ADD", "register:40f0:8", ["const:c077ac:8", "const:4:8"]]
+ 00c077ac ["CALL", null, ["callee:00c5e5e0:8"]]
- 00c07710 bytes 805b0194
+ 00c077ac bytes 8d5b0194
~~~


<a id="compare-858d91164af7b0f8056c6099517d970d"></a>

### [`00c07780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07780.md) → [`00c0781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0781c.md) _ZNKSt6__ndk17collateIwE12do_transformEPKwS3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c077f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07780.md#insn-00c077f4) · [`00c07828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07780.md#insn-00c07828) · [`00c07850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07780.md#insn-00c07850)
- 新版 `00c07890`（命令位置の公開資料なし） · `00c078c4`（命令位置の公開資料なし） · `00c078ec`（命令位置の公開資料なし）

~~~diff
- 00c077f4 ["INT_ADD", "register:40f0:8", ["const:c077f4:8", "const:4:8"]]
- 00c077f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00c07890 ["INT_ADD", "register:40f0:8", ["const:c07890:8", "const:4:8"]]
+ 00c07890 ["CALL", null, ["callee:00c57f60:8"]]
- 00c077f4 bytes a7410194
+ 00c07890 bytes b4410194
- 00c07828 ["INT_ADD", "register:40f0:8", ["const:c07828:8", "const:4:8"]]
- 00c07828 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c078c4 ["INT_ADD", "register:40f0:8", ["const:c078c4:8", "const:4:8"]]
+ 00c078c4 ["CALL", null, ["callee:00c580d0:8"]]
- 00c07828 bytes f6410194
+ 00c078c4 bytes 03420194
- 00c07850 ["INT_ADD", "register:40f0:8", ["const:c07850:8", "const:4:8"]]
- 00c07850 ["CALL", null, ["callee:006d76f8:8"]]
+ 00c078ec ["INT_ADD", "register:40f0:8", ["const:c078ec:8", "const:4:8"]]
+ 00c078ec ["CALL", null, ["callee:006d76f8:8"]]
- 00c07850 bytes 943feb97
+ 00c078ec bytes 833feb97
~~~


<a id="compare-27137f3eaec665ae981ede6fde3f43b2"></a>

### [`00c07b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) → [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md) FUN_00c07bb4

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00c0788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) [`00c13478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13478.md) [`00c135d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c135d0.md) [`00c1368c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c1368c.md) [`00c137dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c137dc.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)
- 新版 呼出元 7件 [`00c07928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07928.md) [`00c13514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md) [`00c1366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1366c.md) [`00c13728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md) [`00c13878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13878.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md#insn-00c07b78) · [`00c07b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md#insn-00c07b84) · [`00c07c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md#insn-00c07c28)
- 新版 `00c07c14`（命令位置の公開資料なし） · `00c07c20`（命令位置の公開資料なし） · `00c07cc4`（命令位置の公開資料なし）

~~~diff
- 00c07b78 ["INT_ADD", "register:40f0:8", ["const:c07b78:8", "const:4:8"]]
- 00c07b78 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c07c14 ["INT_ADD", "register:40f0:8", ["const:c07c14:8", "const:4:8"]]
+ 00c07c14 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c07b78 bytes 2a490194
+ 00c07c14 bytes 37490194
- 00c07b84 ["INT_ADD", "register:40f0:8", ["const:c07b84:8", "const:4:8"]]
- 00c07b84 ["CALL", null, ["callee:00c5e050:8"]]
+ 00c07c20 ["INT_ADD", "register:40f0:8", ["const:c07c20:8", "const:4:8"]]
+ 00c07c20 ["CALL", null, ["callee:00c5e050:8"]]
- 00c07b84 bytes ff580194
+ 00c07c20 bytes 0c590194
- 00c07c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c07c28 ["INT_ADD", "register:40f0:8", ["const:c07c28:8", "const:4:8"]]
- 00c07c28 ["CALLIND", null, ["register:0:8"]]
+ 00c07cc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07cc4 ["INT_ADD", "register:40f0:8", ["const:c07cc4:8", "const:4:8"]]
+ 00c07cc4 ["CALLIND", null, ["register:0:8"]]
- 00c07c28 bytes 00013fd6
+ 00c07cc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc16193301e0122ace6d68aefad5215b"></a>

### [`00c07f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md) → [`00c08028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md) FUN_00c08028

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c07f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f84.md) · 呼出先 6件 [`00c3616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c08020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08020.md) · 呼出先 6件 [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c08014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md#insn-00c08014) · [`00c08030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md#insn-00c08030) · [`00c080b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07f8c.md#insn-00c080b4)
- 新版 `00c080b0`（命令位置の公開資料なし） · `00c080cc`（命令位置の公開資料なし） · `00c08150`（命令位置の公開資料なし）

~~~diff
- 00c08014 ["INT_ADD", "register:40f0:8", ["const:c08014:8", "const:4:8"]]
- 00c08014 ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c080b0 ["INT_ADD", "register:40f0:8", ["const:c080b0:8", "const:4:8"]]
+ 00c080b0 ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c08014 bytes 43590194
+ 00c080b0 bytes 50590194
- 00c08030 ["INT_ADD", "register:40f0:8", ["const:c08030:8", "const:4:8"]]
- 00c08030 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c080cc ["INT_ADD", "register:40f0:8", ["const:c080cc:8", "const:4:8"]]
+ 00c080cc ["CALL", null, ["callee:00c5bf40:8"]]
- 00c08030 bytes 904f0194
+ 00c080cc bytes 9d4f0194
- 00c080b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c080b4 ["INT_ADD", "register:40f0:8", ["const:c080b4:8", "const:4:8"]]
- 00c080b4 ["CALLIND", null, ["register:0:8"]]
+ 00c08150 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08150 ["INT_ADD", "register:40f0:8", ["const:c08150:8", "const:4:8"]]
+ 00c08150 ["CALLIND", null, ["register:0:8"]]
- 00c080b4 bytes 00013fd6
+ 00c08150 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c34b1c109c8acf6818e6276ae5536d4"></a>

### [`00c083c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md) → [`00c08464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md) FUN_00c08464

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c083c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c0.md) · 呼出先 6件 [`00c36294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c0845c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c0845c.md) · 呼出先 6件 [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c08450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md#insn-00c08450) · [`00c0846c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md#insn-00c0846c) · [`00c084f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c083c8.md#insn-00c084f0)
- 新版 `00c084ec`（命令位置の公開資料なし） · `00c08508`（命令位置の公開資料なし） · `00c0858c`（命令位置の公開資料なし）

~~~diff
- 00c08450 ["INT_ADD", "register:40f0:8", ["const:c08450:8", "const:4:8"]]
- 00c08450 ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c084ec ["INT_ADD", "register:40f0:8", ["const:c084ec:8", "const:4:8"]]
+ 00c084ec ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c08450 bytes 34580194
+ 00c084ec bytes 41580194
- 00c0846c ["INT_ADD", "register:40f0:8", ["const:c0846c:8", "const:4:8"]]
- 00c0846c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c08508 ["INT_ADD", "register:40f0:8", ["const:c08508:8", "const:4:8"]]
+ 00c08508 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0846c bytes 814e0194
+ 00c08508 bytes 8e4e0194
- 00c084f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c084f0 ["INT_ADD", "register:40f0:8", ["const:c084f0:8", "const:4:8"]]
- 00c084f0 ["CALLIND", null, ["register:0:8"]]
+ 00c0858c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0858c ["INT_ADD", "register:40f0:8", ["const:c0858c:8", "const:4:8"]]
+ 00c0858c ["CALLIND", null, ["register:0:8"]]
- 00c084f0 bytes 00013fd6
+ 00c0858c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ff24f0c310abb3bf3fa1e615099682"></a>

### [`00c08804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md) → [`00c088a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md) FUN_00c088a0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c087fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c087fc.md) · 呼出先 6件 [`00c363bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c08898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08898.md) · 呼出先 6件 [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0888c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md#insn-00c0888c) · [`00c088a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md#insn-00c088a8) · [`00c0892c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08804.md#insn-00c0892c)
- 新版 `00c08928`（命令位置の公開資料なし） · `00c08944`（命令位置の公開資料なし） · `00c089c8`（命令位置の公開資料なし）

~~~diff
- 00c0888c ["INT_ADD", "register:40f0:8", ["const:c0888c:8", "const:4:8"]]
- 00c0888c ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c08928 ["INT_ADD", "register:40f0:8", ["const:c08928:8", "const:4:8"]]
+ 00c08928 ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c0888c bytes 25570194
+ 00c08928 bytes 32570194
- 00c088a8 ["INT_ADD", "register:40f0:8", ["const:c088a8:8", "const:4:8"]]
- 00c088a8 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c08944 ["INT_ADD", "register:40f0:8", ["const:c08944:8", "const:4:8"]]
+ 00c08944 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c088a8 bytes 724d0194
+ 00c08944 bytes 7f4d0194
- 00c0892c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0892c ["INT_ADD", "register:40f0:8", ["const:c0892c:8", "const:4:8"]]
- 00c0892c ["CALLIND", null, ["register:0:8"]]
+ 00c089c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c089c8 ["INT_ADD", "register:40f0:8", ["const:c089c8:8", "const:4:8"]]
+ 00c089c8 ["CALLIND", null, ["register:0:8"]]
- 00c0892c bytes 00013fd6
+ 00c089c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6738ed4f9d6a3187487f8fdacddb5f2"></a>

### [`00c08c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md) → [`00c08cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md) FUN_00c08cdc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c08c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c38.md) · 呼出先 6件 [`00c36514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c08cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cd4.md) · 呼出先 6件 [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c08cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md#insn-00c08cc8) · [`00c08ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md#insn-00c08ce4) · [`00c08d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c08/00c08c40.md#insn-00c08d68)
- 新版 `00c08d64`（命令位置の公開資料なし） · `00c08d80`（命令位置の公開資料なし） · `00c08e04`（命令位置の公開資料なし）

~~~diff
- 00c08cc8 ["INT_ADD", "register:40f0:8", ["const:c08cc8:8", "const:4:8"]]
- 00c08cc8 ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c08d64 ["INT_ADD", "register:40f0:8", ["const:c08d64:8", "const:4:8"]]
+ 00c08d64 ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c08cc8 bytes 16560194
+ 00c08d64 bytes 23560194
- 00c08ce4 ["INT_ADD", "register:40f0:8", ["const:c08ce4:8", "const:4:8"]]
- 00c08ce4 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c08d80 ["INT_ADD", "register:40f0:8", ["const:c08d80:8", "const:4:8"]]
+ 00c08d80 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c08ce4 bytes 634c0194
+ 00c08d80 bytes 704c0194
- 00c08d68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c08d68 ["INT_ADD", "register:40f0:8", ["const:c08d68:8", "const:4:8"]]
- 00c08d68 ["CALLIND", null, ["register:0:8"]]
+ 00c08e04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08e04 ["INT_ADD", "register:40f0:8", ["const:c08e04:8", "const:4:8"]]
+ 00c08e04 ["CALLIND", null, ["register:0:8"]]
- 00c08d68 bytes 00013fd6
+ 00c08e04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ad883370758256a396b510705a3652b"></a>

### [`00c0907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md) → [`00c09118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md) FUN_00c09118

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c09074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09074.md) · 呼出先 6件 [`00c36668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c09110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09110.md) · 呼出先 6件 [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c09104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md#insn-00c09104) · [`00c09120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md#insn-00c09120) · [`00c091a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c0907c.md#insn-00c091a4)
- 新版 `00c091a0`（命令位置の公開資料なし） · `00c091bc`（命令位置の公開資料なし） · `00c09240`（命令位置の公開資料なし）

~~~diff
- 00c09104 ["INT_ADD", "register:40f0:8", ["const:c09104:8", "const:4:8"]]
- 00c09104 ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c091a0 ["INT_ADD", "register:40f0:8", ["const:c091a0:8", "const:4:8"]]
+ 00c091a0 ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c09104 bytes 07550194
+ 00c091a0 bytes 14550194
- 00c09120 ["INT_ADD", "register:40f0:8", ["const:c09120:8", "const:4:8"]]
- 00c09120 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c091bc ["INT_ADD", "register:40f0:8", ["const:c091bc:8", "const:4:8"]]
+ 00c091bc ["CALL", null, ["callee:00c5bf40:8"]]
- 00c09120 bytes 544b0194
+ 00c091bc bytes 614b0194
- 00c091a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c091a4 ["INT_ADD", "register:40f0:8", ["const:c091a4:8", "const:4:8"]]
- 00c091a4 ["CALLIND", null, ["register:0:8"]]
+ 00c09240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09240 ["INT_ADD", "register:40f0:8", ["const:c09240:8", "const:4:8"]]
+ 00c09240 ["CALLIND", null, ["register:0:8"]]
- 00c091a4 bytes 00013fd6
+ 00c09240 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20393a1e11686fcc9886ac2249b666cc"></a>

### [`00c094b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md) → [`00c09554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md) FUN_00c09554

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c094b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b0.md) · 呼出先 6件 [`00c367b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) [`00c5e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e530.md)
- 新版 呼出元 1件 [`00c0954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c0954c.md) · 呼出先 6件 [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c09540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md#insn-00c09540) · [`00c0955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md#insn-00c0955c) · [`00c095e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c094b8.md#insn-00c095e0)
- 新版 `00c095dc`（命令位置の公開資料なし） · `00c095f8`（命令位置の公開資料なし） · `00c0967c`（命令位置の公開資料なし）

~~~diff
- 00c09540 ["INT_ADD", "register:40f0:8", ["const:c09540:8", "const:4:8"]]
- 00c09540 ["CALL", null, ["callee:00c5e5f0:8"]]
+ 00c095dc ["INT_ADD", "register:40f0:8", ["const:c095dc:8", "const:4:8"]]
+ 00c095dc ["CALL", null, ["callee:00c5e5f0:8"]]
- 00c09540 bytes f8530194
+ 00c095dc bytes 05540194
- 00c0955c ["INT_ADD", "register:40f0:8", ["const:c0955c:8", "const:4:8"]]
- 00c0955c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c095f8 ["INT_ADD", "register:40f0:8", ["const:c095f8:8", "const:4:8"]]
+ 00c095f8 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0955c bytes 454a0194
+ 00c095f8 bytes 524a0194
- 00c095e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c095e0 ["INT_ADD", "register:40f0:8", ["const:c095e0:8", "const:4:8"]]
- 00c095e0 ["CALLIND", null, ["register:0:8"]]
+ 00c0967c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0967c ["INT_ADD", "register:40f0:8", ["const:c0967c:8", "const:4:8"]]
+ 00c0967c ["CALLIND", null, ["register:0:8"]]
- 00c095e0 bytes 00013fd6
+ 00c0967c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de34649b259b4619427a64e9ade5a345"></a>

### [`00c098f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md) → [`00c09990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md) FUN_00c09990

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c098ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098ec.md) · 呼出先 6件 [`00c368f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e550.md)
- 新版 呼出元 1件 [`00c09988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09988.md) · 呼出先 6件 [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c09940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md#insn-00c09940) · [`00c0995c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md#insn-00c0995c) · [`00c099ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c098f4.md#insn-00c099ec)
- 新版 `00c099dc`（命令位置の公開資料なし） · `00c099f8`（命令位置の公開資料なし） · `00c09a88`（命令位置の公開資料なし）

~~~diff
- 00c09940 ["INT_ADD", "register:40f0:8", ["const:c09940:8", "const:4:8"]]
- 00c09940 ["CALL", null, ["callee:00c5e620:8"]]
+ 00c099dc ["INT_ADD", "register:40f0:8", ["const:c099dc:8", "const:4:8"]]
+ 00c099dc ["CALL", null, ["callee:00c5e620:8"]]
- 00c09940 bytes 04530194
+ 00c099dc bytes 11530194
- 00c0995c ["INT_ADD", "register:40f0:8", ["const:c0995c:8", "const:4:8"]]
- 00c0995c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c099f8 ["INT_ADD", "register:40f0:8", ["const:c099f8:8", "const:4:8"]]
+ 00c099f8 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0995c bytes 45490194
+ 00c099f8 bytes 52490194
- 00c099ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00c099ec ["INT_ADD", "register:40f0:8", ["const:c099ec:8", "const:4:8"]]
- 00c099ec ["CALLIND", null, ["register:0:8"]]
+ 00c09a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09a88 ["INT_ADD", "register:40f0:8", ["const:c09a88:8", "const:4:8"]]
+ 00c09a88 ["CALLIND", null, ["register:0:8"]]
- 00c099ec bytes 00013fd6
+ 00c09a88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17239976d904ae53ee01a66dfcd2d23d"></a>

### [`00c09d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md) → [`00c09da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md) FUN_00c09da8

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c09d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d04.md) · 呼出先 6件 [`00c36a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e550.md)
- 新版 呼出元 1件 [`00c09da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da0.md) · 呼出先 6件 [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c09d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md#insn-00c09d58) · [`00c09d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md#insn-00c09d74) · [`00c09e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c09/00c09d0c.md#insn-00c09e04)
- 新版 `00c09df4`（命令位置の公開資料なし） · `00c09e10`（命令位置の公開資料なし） · `00c09ea0`（命令位置の公開資料なし）

~~~diff
- 00c09d58 ["INT_ADD", "register:40f0:8", ["const:c09d58:8", "const:4:8"]]
- 00c09d58 ["CALL", null, ["callee:00c5e620:8"]]
+ 00c09df4 ["INT_ADD", "register:40f0:8", ["const:c09df4:8", "const:4:8"]]
+ 00c09df4 ["CALL", null, ["callee:00c5e620:8"]]
- 00c09d58 bytes fe510194
+ 00c09df4 bytes 0b520194
- 00c09d74 ["INT_ADD", "register:40f0:8", ["const:c09d74:8", "const:4:8"]]
- 00c09d74 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c09e10 ["INT_ADD", "register:40f0:8", ["const:c09e10:8", "const:4:8"]]
+ 00c09e10 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c09d74 bytes 3f480194
+ 00c09e10 bytes 4c480194
- 00c09e04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c09e04 ["INT_ADD", "register:40f0:8", ["const:c09e04:8", "const:4:8"]]
- 00c09e04 ["CALLIND", null, ["register:0:8"]]
+ 00c09ea0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09ea0 ["INT_ADD", "register:40f0:8", ["const:c09ea0:8", "const:4:8"]]
+ 00c09ea0 ["CALLIND", null, ["register:0:8"]]
- 00c09e04 bytes 00013fd6
+ 00c09ea0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d804a9a50f4e30008afb067b6b46e9"></a>

### [`00c0a124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md) → [`00c0a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md) FUN_00c0a1c0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0a11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a11c.md) · 呼出先 6件 [`00c36b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e550.md)
- 新版 呼出元 1件 [`00c0a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1b8.md) · 呼出先 6件 [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0a170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md#insn-00c0a170) · [`00c0a18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md#insn-00c0a18c) · [`00c0a21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a124.md#insn-00c0a21c)
- 新版 `00c0a20c`（命令位置の公開資料なし） · `00c0a228`（命令位置の公開資料なし） · `00c0a2b8`（命令位置の公開資料なし）

~~~diff
- 00c0a170 ["INT_ADD", "register:40f0:8", ["const:c0a170:8", "const:4:8"]]
- 00c0a170 ["CALL", null, ["callee:00c5e620:8"]]
+ 00c0a20c ["INT_ADD", "register:40f0:8", ["const:c0a20c:8", "const:4:8"]]
+ 00c0a20c ["CALL", null, ["callee:00c5e620:8"]]
- 00c0a170 bytes f8500194
+ 00c0a20c bytes 05510194
- 00c0a18c ["INT_ADD", "register:40f0:8", ["const:c0a18c:8", "const:4:8"]]
- 00c0a18c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0a228 ["INT_ADD", "register:40f0:8", ["const:c0a228:8", "const:4:8"]]
+ 00c0a228 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0a18c bytes 39470194
+ 00c0a228 bytes 46470194
- 00c0a21c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0a21c ["INT_ADD", "register:40f0:8", ["const:c0a21c:8", "const:4:8"]]
- 00c0a21c ["CALLIND", null, ["register:0:8"]]
+ 00c0a2b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0a2b8 ["INT_ADD", "register:40f0:8", ["const:c0a2b8:8", "const:4:8"]]
+ 00c0a2b8 ["CALLIND", null, ["register:0:8"]]
- 00c0a21c bytes 00013fd6
+ 00c0a2b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f6708a6d0138c32d77f340c4cb72cb7"></a>

### [`00c0ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md) → [`00c0acc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0acc4.md) FUN_00c0acc4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c0a534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) [`00c0d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5e580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e580.md)
- 新版 呼出元 2件 [`00c0a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a5d0.md) [`00c0da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0da44.md) · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0ac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md#insn-00c0ac8c) · [`00c0aca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md#insn-00c0aca8) · [`00c0acb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md#insn-00c0acb8)
- 新版 `00c0ad28`（命令位置の公開資料なし） · `00c0ad44`（命令位置の公開資料なし） · `00c0ad54`（命令位置の公開資料なし）

~~~diff
- 00c0ac8c ["INT_ADD", "register:40f0:8", ["const:c0ac8c:8", "const:4:8"]]
- 00c0ac8c ["CALL", null, ["callee:00c5e640:8"]]
+ 00c0ad28 ["INT_ADD", "register:40f0:8", ["const:c0ad28:8", "const:4:8"]]
+ 00c0ad28 ["CALL", null, ["callee:00c5e640:8"]]
- 00c0ac8c bytes 394e0194
+ 00c0ad28 bytes 464e0194
- 00c0aca8 ["INT_ADD", "register:40f0:8", ["const:c0aca8:8", "const:4:8"]]
- 00c0aca8 ["CALL", null, ["callee:00c5e650:8"]]
+ 00c0ad44 ["INT_ADD", "register:40f0:8", ["const:c0ad44:8", "const:4:8"]]
+ 00c0ad44 ["CALL", null, ["callee:00c5e650:8"]]
- 00c0aca8 bytes 364e0194
+ 00c0ad44 bytes 434e0194
- 00c0acb8 ["INT_ADD", "register:40f0:8", ["const:c0acb8:8", "const:4:8"]]
- 00c0acb8 ["CALL", null, ["callee:00c5e640:8"]]
+ 00c0ad54 ["INT_ADD", "register:40f0:8", ["const:c0ad54:8", "const:4:8"]]
+ 00c0ad54 ["CALL", null, ["callee:00c5e640:8"]]
- 00c0acb8 bytes 2e4e0194
+ 00c0ad54 bytes 3b4e0194
~~~


<a id="compare-432f8baee29b06549e41328819d01f67"></a>

### [`00c0aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) → [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md) FUN_00c0b08c

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00c0ad64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) [`00c151c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c151c0.md) [`00c15318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15318.md) [`00c153d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c153d4.md) [`00c15524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c15524.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md)
- 新版 呼出元 7件 [`00c0ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0ae00.md) [`00c1525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md) [`00c153b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c153b4.md) [`00c15470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md) [`00c155c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c155c0.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md#insn-00c0b050) · [`00c0b05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md#insn-00c0b05c) · [`00c0b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md#insn-00c0b0f8)
- 新版 `00c0b0ec`（命令位置の公開資料なし） · `00c0b0f8`（命令位置の公開資料なし） · `00c0b194`（命令位置の公開資料なし）

~~~diff
- 00c0b050 ["INT_ADD", "register:40f0:8", ["const:c0b050:8", "const:4:8"]]
- 00c0b050 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c0b0ec ["INT_ADD", "register:40f0:8", ["const:c0b0ec:8", "const:4:8"]]
+ 00c0b0ec ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c0b050 bytes f43b0194
+ 00c0b0ec bytes 013c0194
- 00c0b05c ["INT_ADD", "register:40f0:8", ["const:c0b05c:8", "const:4:8"]]
- 00c0b05c ["CALL", null, ["callee:00c5e050:8"]]
+ 00c0b0f8 ["INT_ADD", "register:40f0:8", ["const:c0b0f8:8", "const:4:8"]]
+ 00c0b0f8 ["CALL", null, ["callee:00c5e050:8"]]
- 00c0b05c bytes c94b0194
+ 00c0b0f8 bytes d64b0194
- 00c0b0f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0b0f8 ["INT_ADD", "register:40f0:8", ["const:c0b0f8:8", "const:4:8"]]
- 00c0b0f8 ["CALLIND", null, ["register:0:8"]]
+ 00c0b194 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0b194 ["INT_ADD", "register:40f0:8", ["const:c0b194:8", "const:4:8"]]
+ 00c0b194 ["CALLIND", null, ["register:0:8"]]
- 00c0b0f8 bytes 00013fd6
+ 00c0b194 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ffc990176f56cd8bd79eebb5b4dea32"></a>

### [`00c0b46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md) → [`00c0b508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md) FUN_00c0b508

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0b464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b464.md) · 呼出先 6件 [`00c3616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c3616c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b500.md) · 呼出先 6件 [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md#insn-00c0b4f4) · [`00c0b510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md#insn-00c0b510) · [`00c0b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b46c.md#insn-00c0b580)
- 新版 `00c0b590`（命令位置の公開資料なし） · `00c0b5ac`（命令位置の公開資料なし） · `00c0b61c`（命令位置の公開資料なし）

~~~diff
- 00c0b4f4 ["INT_ADD", "register:40f0:8", ["const:c0b4f4:8", "const:4:8"]]
- 00c0b4f4 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0b590 ["INT_ADD", "register:40f0:8", ["const:c0b590:8", "const:4:8"]]
+ 00c0b590 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0b4f4 bytes 274c0194
+ 00c0b590 bytes 344c0194
- 00c0b510 ["INT_ADD", "register:40f0:8", ["const:c0b510:8", "const:4:8"]]
- 00c0b510 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0b5ac ["INT_ADD", "register:40f0:8", ["const:c0b5ac:8", "const:4:8"]]
+ 00c0b5ac ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0b510 bytes 58420194
+ 00c0b5ac bytes 65420194
- 00c0b580 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0b580 ["INT_ADD", "register:40f0:8", ["const:c0b580:8", "const:4:8"]]
- 00c0b580 ["CALLIND", null, ["register:0:8"]]
+ 00c0b61c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0b61c ["INT_ADD", "register:40f0:8", ["const:c0b61c:8", "const:4:8"]]
+ 00c0b61c ["CALLIND", null, ["register:0:8"]]
- 00c0b580 bytes 00013fd6
+ 00c0b61c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecde88f093ca8819be17ef736892fc67"></a>

### [`00c0b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md) → [`00c0b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md) FUN_00c0b938

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0b894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b894.md) · 呼出先 6件 [`00c36294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36294.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0b930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b930.md) · 呼出先 6件 [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md#insn-00c0b924) · [`00c0b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md#insn-00c0b940) · [`00c0b9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0b89c.md#insn-00c0b9b0)
- 新版 `00c0b9c0`（命令位置の公開資料なし） · `00c0b9dc`（命令位置の公開資料なし） · `00c0ba4c`（命令位置の公開資料なし）

~~~diff
- 00c0b924 ["INT_ADD", "register:40f0:8", ["const:c0b924:8", "const:4:8"]]
- 00c0b924 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0b9c0 ["INT_ADD", "register:40f0:8", ["const:c0b9c0:8", "const:4:8"]]
+ 00c0b9c0 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0b924 bytes 1b4b0194
+ 00c0b9c0 bytes 284b0194
- 00c0b940 ["INT_ADD", "register:40f0:8", ["const:c0b940:8", "const:4:8"]]
- 00c0b940 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0b9dc ["INT_ADD", "register:40f0:8", ["const:c0b9dc:8", "const:4:8"]]
+ 00c0b9dc ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0b940 bytes 4c410194
+ 00c0b9dc bytes 59410194
- 00c0b9b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0b9b0 ["INT_ADD", "register:40f0:8", ["const:c0b9b0:8", "const:4:8"]]
- 00c0b9b0 ["CALLIND", null, ["register:0:8"]]
+ 00c0ba4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0ba4c ["INT_ADD", "register:40f0:8", ["const:c0ba4c:8", "const:4:8"]]
+ 00c0ba4c ["CALLIND", null, ["register:0:8"]]
- 00c0b9b0 bytes 00013fd6
+ 00c0ba4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03f9d8d3c84abb3d41d38fb44151be7d"></a>

### [`00c0bccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md) → [`00c0bd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md) FUN_00c0bd68

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0bcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bcc4.md) · 呼出先 6件 [`00c363bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c363bc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0bd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd60.md) · 呼出先 6件 [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md#insn-00c0bd54) · [`00c0bd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md#insn-00c0bd70) · [`00c0bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0b/00c0bccc.md#insn-00c0bde0)
- 新版 `00c0bdf0`（命令位置の公開資料なし） · `00c0be0c`（命令位置の公開資料なし） · `00c0be7c`（命令位置の公開資料なし）

~~~diff
- 00c0bd54 ["INT_ADD", "register:40f0:8", ["const:c0bd54:8", "const:4:8"]]
- 00c0bd54 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0bdf0 ["INT_ADD", "register:40f0:8", ["const:c0bdf0:8", "const:4:8"]]
+ 00c0bdf0 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0bd54 bytes 0f4a0194
+ 00c0bdf0 bytes 1c4a0194
- 00c0bd70 ["INT_ADD", "register:40f0:8", ["const:c0bd70:8", "const:4:8"]]
- 00c0bd70 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0be0c ["INT_ADD", "register:40f0:8", ["const:c0be0c:8", "const:4:8"]]
+ 00c0be0c ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0bd70 bytes 40400194
+ 00c0be0c bytes 4d400194
- 00c0bde0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0bde0 ["INT_ADD", "register:40f0:8", ["const:c0bde0:8", "const:4:8"]]
- 00c0bde0 ["CALLIND", null, ["register:0:8"]]
+ 00c0be7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0be7c ["INT_ADD", "register:40f0:8", ["const:c0be7c:8", "const:4:8"]]
+ 00c0be7c ["CALLIND", null, ["register:0:8"]]
- 00c0bde0 bytes 00013fd6
+ 00c0be7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eacc092f1f5efaaeed15f56c29cb3533"></a>

### [`00c0c0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md) → [`00c0c198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md) FUN_00c0c198

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0f4.md) · 呼出先 6件 [`00c36514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36514.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0c190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c190.md) · 呼出先 6件 [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0c184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md#insn-00c0c184) · [`00c0c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md#insn-00c0c1a0) · [`00c0c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c0fc.md#insn-00c0c210)
- 新版 `00c0c220`（命令位置の公開資料なし） · `00c0c23c`（命令位置の公開資料なし） · `00c0c2ac`（命令位置の公開資料なし）

~~~diff
- 00c0c184 ["INT_ADD", "register:40f0:8", ["const:c0c184:8", "const:4:8"]]
- 00c0c184 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0c220 ["INT_ADD", "register:40f0:8", ["const:c0c220:8", "const:4:8"]]
+ 00c0c220 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0c184 bytes 03490194
+ 00c0c220 bytes 10490194
- 00c0c1a0 ["INT_ADD", "register:40f0:8", ["const:c0c1a0:8", "const:4:8"]]
- 00c0c1a0 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0c23c ["INT_ADD", "register:40f0:8", ["const:c0c23c:8", "const:4:8"]]
+ 00c0c23c ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0c1a0 bytes 343f0194
+ 00c0c23c bytes 413f0194
- 00c0c210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0c210 ["INT_ADD", "register:40f0:8", ["const:c0c210:8", "const:4:8"]]
- 00c0c210 ["CALLIND", null, ["register:0:8"]]
+ 00c0c2ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0c2ac ["INT_ADD", "register:40f0:8", ["const:c0c2ac:8", "const:4:8"]]
+ 00c0c2ac ["CALLIND", null, ["register:0:8"]]
- 00c0c210 bytes 00013fd6
+ 00c0c2ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16aa0e6fde2e149f8e9c1c64e0d62ba1"></a>

### [`00c0c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md) → [`00c0c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md) FUN_00c0c5c8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c524.md) · 呼出先 6件 [`00c36668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36668.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0c5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c0.md) · 呼出先 6件 [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0c5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md#insn-00c0c5b4) · [`00c0c5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md#insn-00c0c5d0) · [`00c0c640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c52c.md#insn-00c0c640)
- 新版 `00c0c650`（命令位置の公開資料なし） · `00c0c66c`（命令位置の公開資料なし） · `00c0c6dc`（命令位置の公開資料なし）

~~~diff
- 00c0c5b4 ["INT_ADD", "register:40f0:8", ["const:c0c5b4:8", "const:4:8"]]
- 00c0c5b4 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0c650 ["INT_ADD", "register:40f0:8", ["const:c0c650:8", "const:4:8"]]
+ 00c0c650 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0c5b4 bytes f7470194
+ 00c0c650 bytes 04480194
- 00c0c5d0 ["INT_ADD", "register:40f0:8", ["const:c0c5d0:8", "const:4:8"]]
- 00c0c5d0 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0c66c ["INT_ADD", "register:40f0:8", ["const:c0c66c:8", "const:4:8"]]
+ 00c0c66c ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0c5d0 bytes 283e0194
+ 00c0c66c bytes 353e0194
- 00c0c640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0c640 ["INT_ADD", "register:40f0:8", ["const:c0c640:8", "const:4:8"]]
- 00c0c640 ["CALLIND", null, ["register:0:8"]]
+ 00c0c6dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0c6dc ["INT_ADD", "register:40f0:8", ["const:c0c6dc:8", "const:4:8"]]
+ 00c0c6dc ["CALLIND", null, ["register:0:8"]]
- 00c0c640 bytes 00013fd6
+ 00c0c6dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-849868062306d582d7aa3fb20aaa82de"></a>

### [`00c0c95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md) → [`00c0c9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md) FUN_00c0c9f8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c954.md) · 呼出先 6件 [`00c367b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c367b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md)
- 新版 呼出元 1件 [`00c0c9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f0.md) · 呼出先 6件 [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0c9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md#insn-00c0c9e4) · [`00c0ca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md#insn-00c0ca00) · [`00c0ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0c95c.md#insn-00c0ca70)
- 新版 `00c0ca80`（命令位置の公開資料なし） · `00c0ca9c`（命令位置の公開資料なし） · `00c0cb0c`（命令位置の公開資料なし）

~~~diff
- 00c0c9e4 ["INT_ADD", "register:40f0:8", ["const:c0c9e4:8", "const:4:8"]]
- 00c0c9e4 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c0ca80 ["INT_ADD", "register:40f0:8", ["const:c0ca80:8", "const:4:8"]]
+ 00c0ca80 ["CALL", null, ["callee:00c5e660:8"]]
- 00c0c9e4 bytes eb460194
+ 00c0ca80 bytes f8460194
- 00c0ca00 ["INT_ADD", "register:40f0:8", ["const:c0ca00:8", "const:4:8"]]
- 00c0ca00 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0ca9c ["INT_ADD", "register:40f0:8", ["const:c0ca9c:8", "const:4:8"]]
+ 00c0ca9c ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0ca00 bytes 1c3d0194
+ 00c0ca9c bytes 293d0194
- 00c0ca70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0ca70 ["INT_ADD", "register:40f0:8", ["const:c0ca70:8", "const:4:8"]]
- 00c0ca70 ["CALLIND", null, ["register:0:8"]]
+ 00c0cb0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0cb0c ["INT_ADD", "register:40f0:8", ["const:c0cb0c:8", "const:4:8"]]
+ 00c0cb0c ["CALLIND", null, ["register:0:8"]]
- 00c0ca70 bytes 00013fd6
+ 00c0cb0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8a59e6aba1cdaafe683d93fb1670b7"></a>

### [`00c0cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md) → [`00c0ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md) FUN_00c0ce28

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0cd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd84.md) · 呼出先 6件 [`00c368f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c368f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5b0.md)
- 新版 呼出元 1件 [`00c0ce20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce20.md) · 呼出先 6件 [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0cdd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md#insn-00c0cdd8) · [`00c0cdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md#insn-00c0cdf4) · [`00c0ce74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0c/00c0cd8c.md#insn-00c0ce74)
- 新版 `00c0ce74`（命令位置の公開資料なし） · `00c0ce90`（命令位置の公開資料なし） · `00c0cf10`（命令位置の公開資料なし）

~~~diff
- 00c0cdd8 ["INT_ADD", "register:40f0:8", ["const:c0cdd8:8", "const:4:8"]]
- 00c0cdd8 ["CALL", null, ["callee:00c5e680:8"]]
+ 00c0ce74 ["INT_ADD", "register:40f0:8", ["const:c0ce74:8", "const:4:8"]]
+ 00c0ce74 ["CALL", null, ["callee:00c5e680:8"]]
- 00c0cdd8 bytes f6450194
+ 00c0ce74 bytes 03460194
- 00c0cdf4 ["INT_ADD", "register:40f0:8", ["const:c0cdf4:8", "const:4:8"]]
- 00c0cdf4 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0ce90 ["INT_ADD", "register:40f0:8", ["const:c0ce90:8", "const:4:8"]]
+ 00c0ce90 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0cdf4 bytes 1f3c0194
+ 00c0ce90 bytes 2c3c0194
- 00c0ce74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0ce74 ["INT_ADD", "register:40f0:8", ["const:c0ce74:8", "const:4:8"]]
- 00c0ce74 ["CALLIND", null, ["register:0:8"]]
+ 00c0cf10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0cf10 ["INT_ADD", "register:40f0:8", ["const:c0cf10:8", "const:4:8"]]
+ 00c0cf10 ["CALLIND", null, ["register:0:8"]]
- 00c0ce74 bytes 00013fd6
+ 00c0cf10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edce2b76f98d42a08bc68d70ba27901e"></a>

### [`00c0d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md) → [`00c0d234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md) FUN_00c0d234

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d190.md) · 呼出先 6件 [`00c36a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36a10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5b0.md)
- 新版 呼出元 1件 [`00c0d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d22c.md) · 呼出先 6件 [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0d1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md#insn-00c0d1e4) · [`00c0d200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md#insn-00c0d200) · [`00c0d280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d198.md#insn-00c0d280)
- 新版 `00c0d280`（命令位置の公開資料なし） · `00c0d29c`（命令位置の公開資料なし） · `00c0d31c`（命令位置の公開資料なし）

~~~diff
- 00c0d1e4 ["INT_ADD", "register:40f0:8", ["const:c0d1e4:8", "const:4:8"]]
- 00c0d1e4 ["CALL", null, ["callee:00c5e680:8"]]
+ 00c0d280 ["INT_ADD", "register:40f0:8", ["const:c0d280:8", "const:4:8"]]
+ 00c0d280 ["CALL", null, ["callee:00c5e680:8"]]
- 00c0d1e4 bytes f3440194
+ 00c0d280 bytes 00450194
- 00c0d200 ["INT_ADD", "register:40f0:8", ["const:c0d200:8", "const:4:8"]]
- 00c0d200 ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0d29c ["INT_ADD", "register:40f0:8", ["const:c0d29c:8", "const:4:8"]]
+ 00c0d29c ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0d200 bytes 1c3b0194
+ 00c0d29c bytes 293b0194
- 00c0d280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0d280 ["INT_ADD", "register:40f0:8", ["const:c0d280:8", "const:4:8"]]
- 00c0d280 ["CALLIND", null, ["register:0:8"]]
+ 00c0d31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0d31c ["INT_ADD", "register:40f0:8", ["const:c0d31c:8", "const:4:8"]]
+ 00c0d31c ["CALLIND", null, ["register:0:8"]]
- 00c0d280 bytes 00013fd6
+ 00c0d31c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4932a0cb313c2622ea99d32a23770c2"></a>

### [`00c0d5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md) → [`00c0d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md) FUN_00c0d640

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0d59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d59c.md) · 呼出先 6件 [`00c36b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36b28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md) [`00c5e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e540.md) [`00c5e5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5b0.md)
- 新版 呼出元 1件 [`00c0d638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d638.md) · 呼出先 6件 [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0d5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md#insn-00c0d5f0) · [`00c0d60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md#insn-00c0d60c) · [`00c0d68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d5a4.md#insn-00c0d68c)
- 新版 `00c0d68c`（命令位置の公開資料なし） · `00c0d6a8`（命令位置の公開資料なし） · `00c0d728`（命令位置の公開資料なし）

~~~diff
- 00c0d5f0 ["INT_ADD", "register:40f0:8", ["const:c0d5f0:8", "const:4:8"]]
- 00c0d5f0 ["CALL", null, ["callee:00c5e680:8"]]
+ 00c0d68c ["INT_ADD", "register:40f0:8", ["const:c0d68c:8", "const:4:8"]]
+ 00c0d68c ["CALL", null, ["callee:00c5e680:8"]]
- 00c0d5f0 bytes f0430194
+ 00c0d68c bytes fd430194
- 00c0d60c ["INT_ADD", "register:40f0:8", ["const:c0d60c:8", "const:4:8"]]
- 00c0d60c ["CALL", null, ["callee:00c5bf40:8"]]
+ 00c0d6a8 ["INT_ADD", "register:40f0:8", ["const:c0d6a8:8", "const:4:8"]]
+ 00c0d6a8 ["CALL", null, ["callee:00c5bf40:8"]]
- 00c0d60c bytes 193a0194
+ 00c0d6a8 bytes 263a0194
- 00c0d68c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0d68c ["INT_ADD", "register:40f0:8", ["const:c0d68c:8", "const:4:8"]]
- 00c0d68c ["CALLIND", null, ["register:0:8"]]
+ 00c0d728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0d728 ["INT_ADD", "register:40f0:8", ["const:c0d728:8", "const:4:8"]]
+ 00c0d728 ["CALLIND", null, ["register:0:8"]]
- 00c0d68c bytes 00013fd6
+ 00c0d728 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

