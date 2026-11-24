# v16.0.2 → v16.0.3 · 要調査の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-cc4bcc9dc192b8f7675662e5e57e9b72"></a>

### [`00bffa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md) → [`00c00a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a6c.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3a0.md) [`00c5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f370.md) [`00c5f3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md#insn-00bffaa0) · [`00bffaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md#insn-00bffaac) · [`00bffac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffa78.md#insn-00bffac8)
- 新版 [`00c00a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a6c.md#insn-00c00a94) · [`00c00aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a6c.md#insn-00c00aa0) · [`00c00abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00a6c.md#insn-00c00abc)

~~~diff
- 00bffaa0 ["INT_ADD", "register:40f0:8", ["const:bffaa0:8", "const:4:8"]]
- 00bffaa0 ["CALL", null, ["callee:00c5f370:8"]]
+ 00c00a94 ["INT_ADD", "register:40f0:8", ["const:c00a94:8", "const:4:8"]]
+ 00c00a94 ["CALL", null, ["callee:00c5f370:8"]]
- 00bffaa0 bytes 407a0194
+ 00c00a94 bytes 377a0194
- 00bffaac ["INT_ADD", "register:40f0:8", ["const:bffaac:8", "const:4:8"]]
- 00bffaac ["CALL", null, ["callee:00c5f3b0:8"]]
+ 00c00aa0 ["INT_ADD", "register:40f0:8", ["const:c00aa0:8", "const:4:8"]]
+ 00c00aa0 ["CALL", null, ["callee:00c5f3b0:8"]]
- 00bffaac bytes 4d7a0194
+ 00c00aa0 bytes 447a0194
- 00bffac8 ["INT_ADD", "register:40f0:8", ["const:bffac8:8", "const:4:8"]]
- 00bffac8 ["CALL", null, ["callee:00c5f370:8"]]
+ 00c00abc ["INT_ADD", "register:40f0:8", ["const:c00abc:8", "const:4:8"]]
+ 00c00abc ["CALL", null, ["callee:00c5f370:8"]]
- 00bffac8 bytes 367a0194
+ 00c00abc bytes 2d7a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243c2492d9eeda408d696eea544254b0"></a>

### [`00bffb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb0c.md) → [`00c00b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b00.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f470.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb0c.md#insn-00bffb20)
- 新版 [`00c00b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b00.md#insn-00c00b14)

~~~diff
- 00bffb20 ["INT_ADD", "register:40f0:8", ["const:bffb20:8", "const:4:8"]]
- 00bffb20 ["CALL", null, ["callee:00c5f470:8"]]
+ 00c00b14 ["INT_ADD", "register:40f0:8", ["const:c00b14:8", "const:4:8"]]
+ 00c00b14 ["CALL", null, ["callee:00c5f470:8"]]
- 00bffb20 bytes 607a0194
+ 00c00b14 bytes 577a0194
~~~


<a id="compare-0d8fd7c13fc33dc471b65ccd90207151"></a>

### [`00bffb38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb38.md) → [`00c00b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b2c.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb38.md#insn-00bffb60) · [`00bffb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffb38.md#insn-00bffb6c)
- 新版 [`00c00b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b2c.md#insn-00c00b54) · [`00c00b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00b2c.md#insn-00c00b60)

~~~diff
- 00bffb60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bffb60 ["INT_ADD", "register:40f0:8", ["const:bffb60:8", "const:4:8"]]
- 00bffb60 ["CALLIND", null, ["register:0:8"]]
+ 00c00b54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c00b54 ["INT_ADD", "register:40f0:8", ["const:c00b54:8", "const:4:8"]]
+ 00c00b54 ["CALLIND", null, ["register:0:8"]]
- 00bffb60 bytes 20013fd6
+ 00c00b54 bytes 20013fd6
- 00bffb6c ["INT_ADD", "register:40f0:8", ["const:bffb6c:8", "const:4:8"]]
- 00bffb6c ["CALL", null, ["callee:00c5b870:8"]]
+ 00c00b60 ["INT_ADD", "register:40f0:8", ["const:c00b60:8", "const:4:8"]]
+ 00c00b60 ["CALL", null, ["callee:00c5b870:8"]]
- 00bffb6c bytes 4d6b0194
+ 00c00b60 bytes 446b0194
~~~


<a id="compare-8d9fd6639586c68ca22de860864fb4b1"></a>

### [`00bffc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffc04.md) → [`00c00bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00bf8.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6snextcEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffc04.md#insn-00bffc50)
- 新版 [`00c00c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00bf8.md#insn-00c00c44)

~~~diff
- 00bffc50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bffc50 ["INT_ADD", "register:40f0:8", ["const:bffc50:8", "const:4:8"]]
- 00bffc50 ["CALLIND", null, ["register:0:8"]]
+ 00c00c44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c00c44 ["INT_ADD", "register:40f0:8", ["const:c00c44:8", "const:4:8"]]
+ 00c00c44 ["CALLIND", null, ["register:0:8"]]
- 00bffc50 bytes 00013fd6
+ 00c00c44 bytes 00013fd6
~~~


<a id="compare-e97bd3b0c37cb0ccc58e1e740991fd7d"></a>

### [`00bffe40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe40.md) → [`00c00e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e34.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe40.md#insn-00bffe60)
- 新版 [`00c00e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e34.md#insn-00c00e54)

~~~diff
- 00bffe60 ["INT_ADD", "register:40f0:8", ["const:bffe60:8", "const:4:8"]]
- 00bffe60 ["CALL", null, ["callee:00c5f380:8"]]
+ 00c00e54 ["INT_ADD", "register:40f0:8", ["const:c00e54:8", "const:4:8"]]
+ 00c00e54 ["CALL", null, ["callee:00c5f380:8"]]
- 00bffe60 bytes 54790194
+ 00c00e54 bytes 4b790194
~~~


<a id="compare-1326a1ed3355074f9b7aed283d5f4e77"></a>

### [`00bffe90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md) → [`00c00e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e84.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bffeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md#insn-00bffeb4) · [`00bffec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md#insn-00bffec0) · [`00bffecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe90.md#insn-00bffecc)
- 新版 [`00c00ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e84.md#insn-00c00ea8) · [`00c00eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e84.md#insn-00c00eb4) · [`00c00ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00e84.md#insn-00c00ec0)

~~~diff
- 00bffeb4 ["INT_ADD", "register:40f0:8", ["const:bffeb4:8", "const:4:8"]]
- 00bffeb4 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c00ea8 ["INT_ADD", "register:40f0:8", ["const:c00ea8:8", "const:4:8"]]
+ 00c00ea8 ["CALL", null, ["callee:00c5b870:8"]]
- 00bffeb4 bytes 7b6a0194
+ 00c00ea8 bytes 726a0194
- 00bffec0 ["INT_ADD", "register:40f0:8", ["const:bffec0:8", "const:4:8"]]
- 00bffec0 ["CALL", null, ["callee:00c5f380:8"]]
+ 00c00eb4 ["INT_ADD", "register:40f0:8", ["const:c00eb4:8", "const:4:8"]]
+ 00c00eb4 ["CALL", null, ["callee:00c5f380:8"]]
- 00bffec0 bytes 3c790194
+ 00c00eb4 bytes 33790194
- 00bffecc ["INT_ADD", "register:40f0:8", ["const:bffecc:8", "const:4:8"]]
- 00bffecc ["CALL", null, ["callee:00c5f380:8"]]
+ 00c00ec0 ["INT_ADD", "register:40f0:8", ["const:c00ec0:8", "const:4:8"]]
+ 00c00ec0 ["CALL", null, ["callee:00c5f380:8"]]
- 00bffecc bytes 39790194
+ 00c00ec0 bytes 30790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f1eee283ca7385b1486d096e60b5edd"></a>

### [`00bfffdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bfffdc.md) → [`00c00fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00fd0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bfffdc.md#insn-00c00060) · [`00c00078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bfffdc.md#insn-00c00078)
- 新版 [`00c01054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00fd0.md#insn-00c01054) · [`00c0106c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00fd0.md#insn-00c0106c)

~~~diff
- 00c00060 ["INT_ADD", "register:40f0:8", ["const:c00060:8", "const:4:8"]]
- 00c00060 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c01054 ["INT_ADD", "register:40f0:8", ["const:c01054:8", "const:4:8"]]
+ 00c01054 ["CALL", null, ["callee:00c58fe0:8"]]
- 00c00060 bytes ec5f0194
+ 00c01054 bytes e35f0194
- 00c00078 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00078 ["INT_ADD", "register:40f0:8", ["const:c00078:8", "const:4:8"]]
- 00c00078 ["CALLIND", null, ["register:0:8"]]
+ 00c0106c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0106c ["INT_ADD", "register:40f0:8", ["const:c0106c:8", "const:4:8"]]
+ 00c0106c ["CALLIND", null, ["register:0:8"]]
- 00c00078 bytes 00013fd6
+ 00c0106c bytes 00013fd6
~~~


<a id="compare-92c631c8f0e49c1cf972e5510efde159"></a>

### [`00c000bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c000bc.md) → [`00c010b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c010b0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5uflowEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c000d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c000bc.md#insn-00c000d8)
- 新版 [`00c010cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c010b0.md#insn-00c010cc)

~~~diff
- 00c000d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c000d8 ["INT_ADD", "register:40f0:8", ["const:c000d8:8", "const:4:8"]]
- 00c000d8 ["CALLIND", null, ["register:0:8"]]
+ 00c010cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c010cc ["INT_ADD", "register:40f0:8", ["const:c010cc:8", "const:4:8"]]
+ 00c010cc ["CALLIND", null, ["register:0:8"]]
- 00c000d8 bytes 00013fd6
+ 00c010cc bytes 00013fd6
~~~


<a id="compare-b34fb6cef6b7dc01b756670cae81d36f"></a>

### [`00c0010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0010c.md) → [`00c01100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01100.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsputnEPKwl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0010c.md#insn-00c00188) · [`00c001a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0010c.md#insn-00c001a4)
- 新版 [`00c0117c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01100.md#insn-00c0117c) · [`00c01198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01100.md#insn-00c01198)

~~~diff
- 00c00188 ["INT_ADD", "register:40f0:8", ["const:c00188:8", "const:4:8"]]
- 00c00188 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00c0117c ["INT_ADD", "register:40f0:8", ["const:c0117c:8", "const:4:8"]]
+ 00c0117c ["CALL", null, ["callee:00c58fe0:8"]]
- 00c00188 bytes a25f0194
+ 00c0117c bytes 995f0194
- 00c001a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c001a4 ["INT_ADD", "register:40f0:8", ["const:c001a4:8", "const:4:8"]]
- 00c001a4 ["CALLIND", null, ["register:0:8"]]
+ 00c01198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01198 ["INT_ADD", "register:40f0:8", ["const:c01198:8", "const:4:8"]]
+ 00c01198 ["CALLIND", null, ["register:0:8"]]
- 00c001a4 bytes 00013fd6
+ 00c01198 bytes 00013fd6
~~~


<a id="compare-76f9aa97777b99e95e36a30d1133941a"></a>

### [`00c001f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c001f0.md) → [`00c011e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c011e4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0022c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c001f0.md#insn-00c0022c)
- 新版 [`00c01220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c011e4.md#insn-00c01220)

~~~diff
- 00c0022c ["INT_ADD", "register:40f0:8", ["const:c0022c:8", "const:4:8"]]
- 00c0022c ["CALL", null, ["callee:00c59280:8"]]
+ 00c01220 ["INT_ADD", "register:40f0:8", ["const:c01220:8", "const:4:8"]]
+ 00c01220 ["CALL", null, ["callee:00c59280:8"]]
- 00c0022c bytes 21600194
+ 00c01220 bytes 18600194
~~~


<a id="compare-00f67abf3be1c2b7e449eabb2aa9e900"></a>

### [`00c002e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c002e4.md) → [`00c012d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c012d8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c002fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c002e4.md#insn-00c002fc)
- 新版 [`00c012f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c012d8.md#insn-00c012f0)

~~~diff
- 00c002fc ["INT_ADD", "register:40f0:8", ["const:c002fc:8", "const:4:8"]]
- 00c002fc ["CALL", null, ["callee:00c5e180:8"]]
+ 00c012f0 ["INT_ADD", "register:40f0:8", ["const:c012f0:8", "const:4:8"]]
+ 00c012f0 ["CALL", null, ["callee:00c5e180:8"]]
- 00c002fc bytes ad730194
+ 00c012f0 bytes a4730194
~~~


<a id="compare-d44af55ca1e7fe610f52b54c4037a52b"></a>

### [`00c00314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00314.md) → [`00c01308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01308.md) _ZTv0_n24_NSt6__ndk113basic_istreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00314.md#insn-00c00334)
- 新版 [`00c01328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01308.md#insn-00c01328)

~~~diff
- 00c00334 ["INT_ADD", "register:40f0:8", ["const:c00334:8", "const:4:8"]]
- 00c00334 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c01328 ["INT_ADD", "register:40f0:8", ["const:c01328:8", "const:4:8"]]
+ 00c01328 ["CALL", null, ["callee:00c5e180:8"]]
- 00c00334 bytes 9f730194
+ 00c01328 bytes 96730194
~~~


<a id="compare-d000a1bf202661f4d9aab3246dde7a61"></a>

### [`00c0034c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0034c.md) → [`00c01340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01340.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c0034c.md#insn-00c00384)
- 新版 [`00c01378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c01340.md#insn-00c01378)

~~~diff
- 00c00384 ["INT_ADD", "register:40f0:8", ["const:c00384:8", "const:4:8"]]
- 00c00384 ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c01378 ["INT_ADD", "register:40f0:8", ["const:c01378:8", "const:4:8"]]
+ 00c01378 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00c00384 bytes 1b780194
+ 00c01378 bytes 12780194
~~~


<a id="compare-8e09d3d830a9101c57f3f64afc78de0c"></a>

### [`00c005a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c005a8.md) → [`00c0159c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0159c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4c0.md) · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 1件 [`00c5f490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f490.md) · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c005dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c005a8.md#insn-00c005dc) · [`00c00600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c005a8.md#insn-00c00600) · [`00c00620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c005a8.md#insn-00c00620)
- 新版 [`00c015d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0159c.md#insn-00c015d0) · [`00c015f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0159c.md#insn-00c015f4) · [`00c01614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0159c.md#insn-00c01614)

~~~diff
- 00c005dc ["INT_ADD", "register:40f0:8", ["const:c005dc:8", "const:4:8"]]
- 00c005dc ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c015d0 ["INT_ADD", "register:40f0:8", ["const:c015d0:8", "const:4:8"]]
+ 00c015d0 ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c005dc bytes bd770194
+ 00c015d0 bytes b4770194
- 00c00600 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c00600 ["INT_ADD", "register:40f0:8", ["const:c00600:8", "const:4:8"]]
- 00c00600 ["CALLIND", null, ["register:0:8"]]
+ 00c015f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c015f4 ["INT_ADD", "register:40f0:8", ["const:c015f4:8", "const:4:8"]]
+ 00c015f4 ["CALLIND", null, ["register:0:8"]]
- 00c00600 bytes 00013fd6
+ 00c015f4 bytes 00013fd6
- 00c00620 ["INT_ADD", "register:40f0:8", ["const:c00620:8", "const:4:8"]]
- 00c00620 ["CALL", null, ["callee:00c59340:8"]]
+ 00c01614 ["INT_ADD", "register:40f0:8", ["const:c01614:8", "const:4:8"]]
+ 00c01614 ["CALL", null, ["callee:00c59340:8"]]
- 00c00620 bytes 545f0194
+ 00c01614 bytes 4b5f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-088fbc9246ffaf268e55c98267308bfc"></a>

### [`00c00698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00698.md) → [`00c0168c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0168c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c006b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00698.md#insn-00c006b8)
- 新版 [`00c016ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c0168c.md#insn-00c016ac)

~~~diff
- 00c006b8 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c006b8 ["INT_ADD", "register:40f0:8", ["const:c006b8:8", "const:4:8"]]
- 00c006b8 ["CALLIND", null, ["register:0:8"]]
+ 00c016ac ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c016ac ["INT_ADD", "register:40f0:8", ["const:c016ac:8", "const:4:8"]]
+ 00c016ac ["CALLIND", null, ["register:0:8"]]
- 00c006b8 bytes 20003fd6
+ 00c016ac bytes 20003fd6
~~~


<a id="compare-8e35343fe178a3ab366115c5dd49f746"></a>

### [`00c006d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c006d0.md) → [`00c016c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016c4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c006f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c006d0.md#insn-00c006f0)
- 新版 [`00c016e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016c4.md#insn-00c016e4)

~~~diff
- 00c006f0 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c006f0 ["INT_ADD", "register:40f0:8", ["const:c006f0:8", "const:4:8"]]
- 00c006f0 ["CALLIND", null, ["register:0:8"]]
+ 00c016e4 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c016e4 ["INT_ADD", "register:40f0:8", ["const:c016e4:8", "const:4:8"]]
+ 00c016e4 ["CALLIND", null, ["register:0:8"]]
- 00c006f0 bytes 20003fd6
+ 00c016e4 bytes 20003fd6
~~~


<a id="compare-a0ad46830fab78d3f18fb3370b78435c"></a>

### [`00c00708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00708.md) → [`00c016fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016fc.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEErsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c00738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00708.md#insn-00c00738) · [`00c0079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00708.md#insn-00c0079c) · [`00c007d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c00/00c00708.md#insn-00c007d0)
- 新版 [`00c0172c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016fc.md#insn-00c0172c) · [`00c01790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016fc.md#insn-00c01790) · [`00c017c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c01/00c016fc.md#insn-00c017c4)

~~~diff
- 00c00738 ["INT_ADD", "register:40f0:8", ["const:c00738:8", "const:4:8"]]
- 00c00738 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c0172c ["INT_ADD", "register:40f0:8", ["const:c0172c:8", "const:4:8"]]
+ 00c0172c ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c00738 bytes 6e770194
+ 00c0172c bytes 65770194
- 00c0079c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0079c ["INT_ADD", "register:40f0:8", ["const:c0079c:8", "const:4:8"]]
- 00c0079c ["CALLIND", null, ["register:0:8"]]
+ 00c01790 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c01790 ["INT_ADD", "register:40f0:8", ["const:c01790:8", "const:4:8"]]
+ 00c01790 ["CALLIND", null, ["register:0:8"]]
- 00c0079c bytes 00013fd6
+ 00c01790 bytes 00013fd6
- 00c007d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c007d0 ["INT_ADD", "register:40f0:8", ["const:c007d0:8", "const:4:8"]]
- 00c007d0 ["CALLIND", null, ["register:0:8"]]
+ 00c017c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c017c4 ["INT_ADD", "register:40f0:8", ["const:c017c4:8", "const:4:8"]]
+ 00c017c4 ["CALLIND", null, ["register:0:8"]]
- 00c007d0 bytes 00013fd6
+ 00c017c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e9acc329ef1b9b16772715fa5271c53"></a>

### [`00c01914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01914.md) → [`00c02908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02908.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e500.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 1件 [`00c5f4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4d0.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0193c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01914.md#insn-00c0193c) · [`00c01994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01914.md#insn-00c01994) · [`00c019bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01914.md#insn-00c019bc)
- 新版 [`00c02930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02908.md#insn-00c02930) · [`00c02988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02908.md#insn-00c02988) · [`00c029b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02908.md#insn-00c029b0)

~~~diff
- 00c0193c ["INT_ADD", "register:40f0:8", ["const:c0193c:8", "const:4:8"]]
- 00c0193c ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c02930 ["INT_ADD", "register:40f0:8", ["const:c02930:8", "const:4:8"]]
+ 00c02930 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c0193c bytes ed720194
+ 00c02930 bytes e4720194
- 00c01994 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01994 ["INT_ADD", "register:40f0:8", ["const:c01994:8", "const:4:8"]]
- 00c01994 ["CALLIND", null, ["register:0:8"]]
+ 00c02988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02988 ["INT_ADD", "register:40f0:8", ["const:c02988:8", "const:4:8"]]
+ 00c02988 ["CALLIND", null, ["register:0:8"]]
- 00c01994 bytes 00013fd6
+ 00c02988 bytes 00013fd6
- 00c019bc ["INT_ADD", "register:40f0:8", ["const:c019bc:8", "const:4:8"]]
- 00c019bc ["CALL", null, ["callee:00c59340:8"]]
+ 00c029b0 ["INT_ADD", "register:40f0:8", ["const:c029b0:8", "const:4:8"]]
+ 00c029b0 ["CALL", null, ["callee:00c59340:8"]]
- 00c019bc bytes 6d5a0194
+ 00c029b0 bytes 645a0194
~~~


<a id="compare-e7ee7f9105c2a06f19dc087d6a255519"></a>

### [`00c01a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01a2c.md) → [`00c02a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02a20.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e500.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01a2c.md#insn-00c01a44)
- 新版 [`00c02a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02a20.md#insn-00c02a38)

~~~diff
- 00c01a44 ["INT_ADD", "register:40f0:8", ["const:c01a44:8", "const:4:8"]]
- 00c01a44 ["CALL", null, ["callee:00c5f4d0:8"]]
+ 00c02a38 ["INT_ADD", "register:40f0:8", ["const:c02a38:8", "const:4:8"]]
+ 00c02a38 ["CALL", null, ["callee:00c5f4d0:8"]]
- 00c01a44 bytes af720194
+ 00c02a38 bytes a6720194
~~~


<a id="compare-d263b27d8589584b920533595b74f373"></a>

### [`00c01b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01b0c.md) → [`00c02b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02b00.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e510.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 1件 [`00c5f4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4e0.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01b0c.md#insn-00c01b48) · [`00c01bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01b0c.md#insn-00c01bc0) · [`00c01bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01b0c.md#insn-00c01bfc)
- 新版 [`00c02b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02b00.md#insn-00c02b3c) · [`00c02bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02b00.md#insn-00c02bb4) · [`00c02bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02b00.md#insn-00c02bf0)

~~~diff
- 00c01b48 ["INT_ADD", "register:40f0:8", ["const:c01b48:8", "const:4:8"]]
- 00c01b48 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c02b3c ["INT_ADD", "register:40f0:8", ["const:c02b3c:8", "const:4:8"]]
+ 00c02b3c ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c01b48 bytes 6a720194
+ 00c02b3c bytes 61720194
- 00c01bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01bc0 ["INT_ADD", "register:40f0:8", ["const:c01bc0:8", "const:4:8"]]
- 00c01bc0 ["CALLIND", null, ["register:0:8"]]
+ 00c02bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02bb4 ["INT_ADD", "register:40f0:8", ["const:c02bb4:8", "const:4:8"]]
+ 00c02bb4 ["CALLIND", null, ["register:0:8"]]
- 00c01bc0 bytes 00013fd6
+ 00c02bb4 bytes 00013fd6
- 00c01bfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01bfc ["INT_ADD", "register:40f0:8", ["const:c01bfc:8", "const:4:8"]]
- 00c01bfc ["CALLIND", null, ["register:0:8"]]
+ 00c02bf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02bf0 ["INT_ADD", "register:40f0:8", ["const:c02bf0:8", "const:4:8"]]
+ 00c02bf0 ["CALLIND", null, ["register:0:8"]]
- 00c01bfc bytes 00013fd6
+ 00c02bf0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b05ed20196218bafe09b22c5962b71"></a>

### [`00c01d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01d70.md) → [`00c02d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02d64.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e520.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 1件 [`00c5f4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4f0.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01d70.md#insn-00c01da4) · [`00c01e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01d70.md#insn-00c01e04) · [`00c01e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01d70.md#insn-00c01e40)
- 新版 [`00c02d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02d64.md#insn-00c02d98) · [`00c02df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02d64.md#insn-00c02df8) · [`00c02e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02d64.md#insn-00c02e34)

~~~diff
- 00c01da4 ["INT_ADD", "register:40f0:8", ["const:c01da4:8", "const:4:8"]]
- 00c01da4 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c02d98 ["INT_ADD", "register:40f0:8", ["const:c02d98:8", "const:4:8"]]
+ 00c02d98 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c01da4 bytes d3710194
+ 00c02d98 bytes ca710194
- 00c01e04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01e04 ["INT_ADD", "register:40f0:8", ["const:c01e04:8", "const:4:8"]]
- 00c01e04 ["CALLIND", null, ["register:0:8"]]
+ 00c02df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02df8 ["INT_ADD", "register:40f0:8", ["const:c02df8:8", "const:4:8"]]
+ 00c02df8 ["CALLIND", null, ["register:0:8"]]
- 00c01e04 bytes 00013fd6
+ 00c02df8 bytes 00013fd6
- 00c01e40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c01e40 ["INT_ADD", "register:40f0:8", ["const:c01e40:8", "const:4:8"]]
- 00c01e40 ["CALLIND", null, ["register:0:8"]]
+ 00c02e34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c02e34 ["INT_ADD", "register:40f0:8", ["const:c02e34:8", "const:4:8"]]
+ 00c02e34 ["CALLIND", null, ["register:0:8"]]
- 00c01e40 bytes 00013fd6
+ 00c02e34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d3c017de8415939a9cb9b54ec4142a"></a>

### [`00c01f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01f78.md) → [`00c02f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02f6c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e530.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 1件 [`00c5f500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f500.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c01fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01f78.md#insn-00c01fb8) · [`00c02010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01f78.md#insn-00c02010) · [`00c02058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c01/00c01f78.md#insn-00c02058)
- 新版 [`00c02fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02f6c.md#insn-00c02fac) · [`00c03004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02f6c.md#insn-00c03004) · [`00c0304c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c02/00c02f6c.md#insn-00c0304c)

~~~diff
- 00c01fb8 ["INT_ADD", "register:40f0:8", ["const:c01fb8:8", "const:4:8"]]
- 00c01fb8 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c02fac ["INT_ADD", "register:40f0:8", ["const:c02fac:8", "const:4:8"]]
+ 00c02fac ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c01fb8 bytes 4e710194
+ 00c02fac bytes 45710194
- 00c02010 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02010 ["INT_ADD", "register:40f0:8", ["const:c02010:8", "const:4:8"]]
- 00c02010 ["CALLIND", null, ["register:0:8"]]
+ 00c03004 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03004 ["INT_ADD", "register:40f0:8", ["const:c03004:8", "const:4:8"]]
+ 00c03004 ["CALLIND", null, ["register:0:8"]]
- 00c02010 bytes 00013fd6
+ 00c03004 bytes 00013fd6
- 00c02058 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02058 ["INT_ADD", "register:40f0:8", ["const:c02058:8", "const:4:8"]]
- 00c02058 ["CALLIND", null, ["register:0:8"]]
+ 00c0304c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0304c ["INT_ADD", "register:40f0:8", ["const:c0304c:8", "const:4:8"]]
+ 00c0304c ["CALLIND", null, ["register:0:8"]]
- 00c02058 bytes 00013fd6
+ 00c0304c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-746179b8bcfc455c5ea09cd1c9cef9fc"></a>

### [`00c021b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c021b4.md) → [`00c031a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c031a8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c021e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c021b4.md#insn-00c021e8) · [`00c02240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c021b4.md#insn-00c02240) · [`00c022a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c021b4.md#insn-00c022a8)
- 新版 [`00c031dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c031a8.md#insn-00c031dc) · [`00c03234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c031a8.md#insn-00c03234) · [`00c0329c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c031a8.md#insn-00c0329c)

~~~diff
- 00c021e8 ["INT_ADD", "register:40f0:8", ["const:c021e8:8", "const:4:8"]]
- 00c021e8 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c031dc ["INT_ADD", "register:40f0:8", ["const:c031dc:8", "const:4:8"]]
+ 00c031dc ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c021e8 bytes c2700194
+ 00c031dc bytes b9700194
- 00c02240 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c02240 ["INT_ADD", "register:40f0:8", ["const:c02240:8", "const:4:8"]]
- 00c02240 ["CALLIND", null, ["register:0:8"]]
+ 00c03234 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c03234 ["INT_ADD", "register:40f0:8", ["const:c03234:8", "const:4:8"]]
+ 00c03234 ["CALLIND", null, ["register:0:8"]]
- 00c02240 bytes 20013fd6
+ 00c03234 bytes 20013fd6
- 00c022a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c022a8 ["INT_ADD", "register:40f0:8", ["const:c022a8:8", "const:4:8"]]
- 00c022a8 ["CALLIND", null, ["register:0:8"]]
+ 00c0329c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c0329c ["INT_ADD", "register:40f0:8", ["const:c0329c:8", "const:4:8"]]
+ 00c0329c ["CALLIND", null, ["register:0:8"]]
- 00c022a8 bytes 20013fd6
+ 00c0329c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21e5e9b8834568b70a857e6f3d8c9dc"></a>

### [`00c02368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02368.md) → [`00c0335c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0335c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02368.md#insn-00c02390) · [`00c023d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02368.md#insn-00c023d0) · [`00c023f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02368.md#insn-00c023f8)
- 新版 [`00c03384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0335c.md#insn-00c03384) · [`00c033c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0335c.md#insn-00c033c4) · [`00c033ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0335c.md#insn-00c033ec)

~~~diff
- 00c02390 ["INT_ADD", "register:40f0:8", ["const:c02390:8", "const:4:8"]]
- 00c02390 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03384 ["INT_ADD", "register:40f0:8", ["const:c03384:8", "const:4:8"]]
+ 00c03384 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02390 bytes 58700194
+ 00c03384 bytes 4f700194
- 00c023d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c023d0 ["INT_ADD", "register:40f0:8", ["const:c023d0:8", "const:4:8"]]
- 00c023d0 ["CALLIND", null, ["register:0:8"]]
+ 00c033c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c033c4 ["INT_ADD", "register:40f0:8", ["const:c033c4:8", "const:4:8"]]
+ 00c033c4 ["CALLIND", null, ["register:0:8"]]
- 00c023d0 bytes 00013fd6
+ 00c033c4 bytes 00013fd6
- 00c023f8 ["INT_ADD", "register:40f0:8", ["const:c023f8:8", "const:4:8"]]
- 00c023f8 ["CALL", null, ["callee:00c59340:8"]]
+ 00c033ec ["INT_ADD", "register:40f0:8", ["const:c033ec:8", "const:4:8"]]
+ 00c033ec ["CALL", null, ["callee:00c59340:8"]]
- 00c023f8 bytes de570194
+ 00c033ec bytes d5570194
~~~


<a id="compare-d2955f4be9bbac9968e9b6f16a6d0864"></a>

### [`00c02468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02468.md) → [`00c0345c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0345c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4readEPwl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02468.md#insn-00c02498) · [`00c024c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02468.md#insn-00c024c4) · [`00c024f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02468.md#insn-00c024f4)
- 新版 [`00c0348c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0345c.md#insn-00c0348c) · [`00c034b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0345c.md#insn-00c034b8) · [`00c034e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0345c.md#insn-00c034e8)

~~~diff
- 00c02498 ["INT_ADD", "register:40f0:8", ["const:c02498:8", "const:4:8"]]
- 00c02498 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c0348c ["INT_ADD", "register:40f0:8", ["const:c0348c:8", "const:4:8"]]
+ 00c0348c ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02498 bytes 16700194
+ 00c0348c bytes 0d700194
- 00c024c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c024c4 ["INT_ADD", "register:40f0:8", ["const:c024c4:8", "const:4:8"]]
- 00c024c4 ["CALLIND", null, ["register:0:8"]]
+ 00c034b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c034b8 ["INT_ADD", "register:40f0:8", ["const:c034b8:8", "const:4:8"]]
+ 00c034b8 ["CALLIND", null, ["register:0:8"]]
- 00c024c4 bytes 00013fd6
+ 00c034b8 bytes 00013fd6
- 00c024f4 ["INT_ADD", "register:40f0:8", ["const:c024f4:8", "const:4:8"]]
- 00c024f4 ["CALL", null, ["callee:00c59340:8"]]
+ 00c034e8 ["INT_ADD", "register:40f0:8", ["const:c034e8:8", "const:4:8"]]
+ 00c034e8 ["CALL", null, ["callee:00c59340:8"]]
- 00c024f4 bytes 9f570194
+ 00c034e8 bytes 96570194
~~~


<a id="compare-deee44a6882491de7e9632d4339d54ce"></a>

### [`00c02560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02560.md) → [`00c03554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03554.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE8readsomeEPwl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02560.md#insn-00c02590) · [`00c025d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02560.md#insn-00c025d4) · [`00c02620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02560.md#insn-00c02620)
- 新版 [`00c03584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03554.md#insn-00c03584) · [`00c035c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03554.md#insn-00c035c8) · [`00c03614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03554.md#insn-00c03614)

~~~diff
- 00c02590 ["INT_ADD", "register:40f0:8", ["const:c02590:8", "const:4:8"]]
- 00c02590 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03584 ["INT_ADD", "register:40f0:8", ["const:c03584:8", "const:4:8"]]
+ 00c03584 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02590 bytes d86f0194
+ 00c03584 bytes cf6f0194
- 00c025d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c025d4 ["INT_ADD", "register:40f0:8", ["const:c025d4:8", "const:4:8"]]
- 00c025d4 ["CALLIND", null, ["register:0:8"]]
+ 00c035c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c035c8 ["INT_ADD", "register:40f0:8", ["const:c035c8:8", "const:4:8"]]
+ 00c035c8 ["CALLIND", null, ["register:0:8"]]
- 00c025d4 bytes 00013fd6
+ 00c035c8 bytes 00013fd6
- 00c02620 ["COPY", "register:0:8", ["register:4048:8"]]
- 00c02620 ["INT_ADD", "register:40f0:8", ["const:c02620:8", "const:4:8"]]
- 00c02620 ["CALLIND", null, ["register:0:8"]]
+ 00c03614 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c03614 ["INT_ADD", "register:40f0:8", ["const:c03614:8", "const:4:8"]]
+ 00c03614 ["CALLIND", null, ["register:0:8"]]
- 00c02620 bytes 20013fd6
+ 00c03614 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b64ee4cc6fbbb2b0378a8e6769c02d0a"></a>

### [`00c026b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c026b4.md) → [`00c036a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c036a8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7putbackEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c026f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c026b4.md#insn-00c026f4) · [`00c02704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c026b4.md#insn-00c02704) · [`00c02760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c026b4.md#insn-00c02760)
- 新版 [`00c036e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c036a8.md#insn-00c036e8) · [`00c036f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c036a8.md#insn-00c036f8) · [`00c03754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c036a8.md#insn-00c03754)

~~~diff
- 00c026f4 ["INT_ADD", "register:40f0:8", ["const:c026f4:8", "const:4:8"]]
- 00c026f4 ["CALL", null, ["callee:00c59340:8"]]
+ 00c036e8 ["INT_ADD", "register:40f0:8", ["const:c036e8:8", "const:4:8"]]
+ 00c036e8 ["CALL", null, ["callee:00c59340:8"]]
- 00c026f4 bytes 1f570194
+ 00c036e8 bytes 16570194
- 00c02704 ["INT_ADD", "register:40f0:8", ["const:c02704:8", "const:4:8"]]
- 00c02704 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c036f8 ["INT_ADD", "register:40f0:8", ["const:c036f8:8", "const:4:8"]]
+ 00c036f8 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02704 bytes 7b6f0194
+ 00c036f8 bytes 726f0194
- 00c02760 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02760 ["INT_ADD", "register:40f0:8", ["const:c02760:8", "const:4:8"]]
- 00c02760 ["CALLIND", null, ["register:0:8"]]
+ 00c03754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03754 ["INT_ADD", "register:40f0:8", ["const:c03754:8", "const:4:8"]]
+ 00c03754 ["CALLIND", null, ["register:0:8"]]
- 00c02760 bytes 00013fd6
+ 00c03754 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21b6230530824a7a4c003045cfe7ac6"></a>

### [`00c027f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c027f4.md) → [`00c037e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c037e8.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5ungetEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c027f4.md#insn-00c02830) · [`00c02840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c027f4.md#insn-00c02840) · [`00c02894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c027f4.md#insn-00c02894)
- 新版 [`00c03824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c037e8.md#insn-00c03824) · [`00c03834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c037e8.md#insn-00c03834) · [`00c03888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c037e8.md#insn-00c03888)

~~~diff
- 00c02830 ["INT_ADD", "register:40f0:8", ["const:c02830:8", "const:4:8"]]
- 00c02830 ["CALL", null, ["callee:00c59340:8"]]
+ 00c03824 ["INT_ADD", "register:40f0:8", ["const:c03824:8", "const:4:8"]]
+ 00c03824 ["CALL", null, ["callee:00c59340:8"]]
- 00c02830 bytes d0560194
+ 00c03824 bytes c7560194
- 00c02840 ["INT_ADD", "register:40f0:8", ["const:c02840:8", "const:4:8"]]
- 00c02840 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03834 ["INT_ADD", "register:40f0:8", ["const:c03834:8", "const:4:8"]]
+ 00c03834 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02840 bytes 2c6f0194
+ 00c03834 bytes 236f0194
- 00c02894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02894 ["INT_ADD", "register:40f0:8", ["const:c02894:8", "const:4:8"]]
- 00c02894 ["CALLIND", null, ["register:0:8"]]
+ 00c03888 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03888 ["INT_ADD", "register:40f0:8", ["const:c03888:8", "const:4:8"]]
+ 00c03888 ["CALLIND", null, ["register:0:8"]]
- 00c02894 bytes 00013fd6
+ 00c03888 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2cf2f832bf1ecce5396b0629f32bd6"></a>

### [`00c02928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02928.md) → [`00c0391c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0391c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4syncEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02928.md#insn-00c0294c) · [`00c02974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02928.md#insn-00c02974) · [`00c02998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02928.md#insn-00c02998)
- 新版 [`00c03940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0391c.md#insn-00c03940) · [`00c03968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0391c.md#insn-00c03968) · [`00c0398c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c0391c.md#insn-00c0398c)

~~~diff
- 00c0294c ["INT_ADD", "register:40f0:8", ["const:c0294c:8", "const:4:8"]]
- 00c0294c ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03940 ["INT_ADD", "register:40f0:8", ["const:c03940:8", "const:4:8"]]
+ 00c03940 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c0294c bytes e96e0194
+ 00c03940 bytes e06e0194
- 00c02974 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02974 ["INT_ADD", "register:40f0:8", ["const:c02974:8", "const:4:8"]]
- 00c02974 ["CALLIND", null, ["register:0:8"]]
+ 00c03968 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03968 ["INT_ADD", "register:40f0:8", ["const:c03968:8", "const:4:8"]]
+ 00c03968 ["CALLIND", null, ["register:0:8"]]
- 00c02974 bytes 00013fd6
+ 00c03968 bytes 00013fd6
- 00c02998 ["INT_ADD", "register:40f0:8", ["const:c02998:8", "const:4:8"]]
- 00c02998 ["CALL", null, ["callee:00c59340:8"]]
+ 00c0398c ["INT_ADD", "register:40f0:8", ["const:c0398c:8", "const:4:8"]]
+ 00c0398c ["CALL", null, ["callee:00c59340:8"]]
- 00c02998 bytes 76560194
+ 00c0398c bytes 6d560194
~~~


<a id="compare-9c67fd479e99f553eb5848321b62e330"></a>

### [`00c02a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02a18.md) → [`00c03a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03a0c.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02a18.md#insn-00c02a3c) · [`00c02a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02a18.md#insn-00c02a6c) · [`00c02a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02a18.md#insn-00c02a90)
- 新版 [`00c03a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03a0c.md#insn-00c03a30) · [`00c03a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03a0c.md#insn-00c03a60) · [`00c03a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03a0c.md#insn-00c03a84)

~~~diff
- 00c02a3c ["INT_ADD", "register:40f0:8", ["const:c02a3c:8", "const:4:8"]]
- 00c02a3c ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03a30 ["INT_ADD", "register:40f0:8", ["const:c03a30:8", "const:4:8"]]
+ 00c03a30 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02a3c bytes ad6e0194
+ 00c03a30 bytes a46e0194
- 00c02a6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02a6c ["INT_ADD", "register:40f0:8", ["const:c02a6c:8", "const:4:8"]]
- 00c02a6c ["CALLIND", null, ["register:0:8"]]
+ 00c03a60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03a60 ["INT_ADD", "register:40f0:8", ["const:c03a60:8", "const:4:8"]]
+ 00c03a60 ["CALLIND", null, ["register:0:8"]]
- 00c02a6c bytes 00013fd6
+ 00c03a60 bytes 00013fd6
- 00c02a90 ["INT_ADD", "register:40f0:8", ["const:c02a90:8", "const:4:8"]]
- 00c02a90 ["CALL", null, ["callee:00c59340:8"]]
+ 00c03a84 ["INT_ADD", "register:40f0:8", ["const:c03a84:8", "const:4:8"]]
+ 00c03a84 ["CALL", null, ["callee:00c59340:8"]]
- 00c02a90 bytes 38560194
+ 00c03a84 bytes 2f560194
~~~


<a id="compare-a4ea5398624d2713ceb8b9337257f221"></a>

### [`00c02b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02b14.md) → [`00c03b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03b08.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02b14.md#insn-00c02b50) · [`00c02b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02b14.md#insn-00c02b60) · [`00c02b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02b14.md#insn-00c02b90)
- 新版 [`00c03b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03b08.md#insn-00c03b44) · [`00c03b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03b08.md#insn-00c03b54) · [`00c03b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03b08.md#insn-00c03b84)

~~~diff
- 00c02b50 ["INT_ADD", "register:40f0:8", ["const:c02b50:8", "const:4:8"]]
- 00c02b50 ["CALL", null, ["callee:00c59340:8"]]
+ 00c03b44 ["INT_ADD", "register:40f0:8", ["const:c03b44:8", "const:4:8"]]
+ 00c03b44 ["CALL", null, ["callee:00c59340:8"]]
- 00c02b50 bytes 08560194
+ 00c03b44 bytes ff550194
- 00c02b60 ["INT_ADD", "register:40f0:8", ["const:c02b60:8", "const:4:8"]]
- 00c02b60 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03b54 ["INT_ADD", "register:40f0:8", ["const:c03b54:8", "const:4:8"]]
+ 00c03b54 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02b60 bytes 646e0194
+ 00c03b54 bytes 5b6e0194
- 00c02b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02b90 ["INT_ADD", "register:40f0:8", ["const:c02b90:8", "const:4:8"]]
- 00c02b90 ["CALLIND", null, ["register:0:8"]]
+ 00c03b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03b84 ["INT_ADD", "register:40f0:8", ["const:c03b84:8", "const:4:8"]]
+ 00c03b84 ["CALLIND", null, ["register:0:8"]]
- 00c02b90 bytes 00013fd6
+ 00c03b84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81743cb92cad1d28164b2e09308c6c28"></a>

### [`00c02c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02c24.md) → [`00c03c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03c18.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02c24.md#insn-00c02c60) · [`00c02c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02c24.md#insn-00c02c70) · [`00c02ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02c24.md#insn-00c02ca0)
- 新版 [`00c03c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03c18.md#insn-00c03c54) · [`00c03c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03c18.md#insn-00c03c64) · [`00c03c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03c18.md#insn-00c03c94)

~~~diff
- 00c02c60 ["INT_ADD", "register:40f0:8", ["const:c02c60:8", "const:4:8"]]
- 00c02c60 ["CALL", null, ["callee:00c59340:8"]]
+ 00c03c54 ["INT_ADD", "register:40f0:8", ["const:c03c54:8", "const:4:8"]]
+ 00c03c54 ["CALL", null, ["callee:00c59340:8"]]
- 00c02c60 bytes c4550194
+ 00c03c54 bytes bb550194
- 00c02c70 ["INT_ADD", "register:40f0:8", ["const:c02c70:8", "const:4:8"]]
- 00c02c70 ["CALL", null, ["callee:00c5f4c0:8"]]
+ 00c03c64 ["INT_ADD", "register:40f0:8", ["const:c03c64:8", "const:4:8"]]
+ 00c03c64 ["CALL", null, ["callee:00c5f4c0:8"]]
- 00c02c70 bytes 206e0194
+ 00c03c64 bytes 176e0194
- 00c02ca0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02ca0 ["INT_ADD", "register:40f0:8", ["const:c02ca0:8", "const:4:8"]]
- 00c02ca0 ["CALLIND", null, ["register:0:8"]]
+ 00c03c94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03c94 ["INT_ADD", "register:40f0:8", ["const:c03c94:8", "const:4:8"]]
+ 00c03c94 ["CALLIND", null, ["register:0:8"]]
- 00c02ca0 bytes 00013fd6
+ 00c03c94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e322ec130e0a283f10caa2a843fd04c"></a>

### [`00c02d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02d34.md) → [`00c03d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03d28.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02d34.md#insn-00c02d6c)
- 新版 [`00c03d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03d28.md#insn-00c03d60)

~~~diff
- 00c02d6c ["INT_ADD", "register:40f0:8", ["const:c02d6c:8", "const:4:8"]]
- 00c02d6c ["CALL", null, ["callee:00c59280:8"]]
+ 00c03d60 ["INT_ADD", "register:40f0:8", ["const:c03d60:8", "const:4:8"]]
+ 00c03d60 ["CALL", null, ["callee:00c59280:8"]]
- 00c02d6c bytes 51550194
+ 00c03d60 bytes 48550194
~~~


<a id="compare-722dbfaa816f19248f09528978530e15"></a>

### [`00c02e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e24.md) → [`00c03e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e18.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e24.md#insn-00c02e3c)
- 新版 [`00c03e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e18.md#insn-00c03e30)

~~~diff
- 00c02e3c ["INT_ADD", "register:40f0:8", ["const:c02e3c:8", "const:4:8"]]
- 00c02e3c ["CALL", null, ["callee:00c5e180:8"]]
+ 00c03e30 ["INT_ADD", "register:40f0:8", ["const:c03e30:8", "const:4:8"]]
+ 00c03e30 ["CALL", null, ["callee:00c5e180:8"]]
- 00c02e3c bytes dd680194
+ 00c03e30 bytes d4680194
~~~


<a id="compare-7b0037be2e9f3388f112cdb8887b4d94"></a>

### [`00c02e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e54.md) → [`00c03e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e48.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e54.md#insn-00c02e74)
- 新版 [`00c03e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e48.md#insn-00c03e68)

~~~diff
- 00c02e74 ["INT_ADD", "register:40f0:8", ["const:c02e74:8", "const:4:8"]]
- 00c02e74 ["CALL", null, ["callee:00c5e180:8"]]
+ 00c03e68 ["INT_ADD", "register:40f0:8", ["const:c03e68:8", "const:4:8"]]
+ 00c03e68 ["CALL", null, ["callee:00c5e180:8"]]
- 00c02e74 bytes cf680194
+ 00c03e68 bytes c6680194
~~~


<a id="compare-2a075628b2996db900153851f1af442b"></a>

### [`00c02e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e8c.md) → [`00c03e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e80.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02e8c.md#insn-00c02ebc)
- 新版 [`00c03eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03e80.md#insn-00c03eb0)

~~~diff
- 00c02ebc ["INT_ADD", "register:40f0:8", ["const:c02ebc:8", "const:4:8"]]
- 00c02ebc ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c03eb0 ["INT_ADD", "register:40f0:8", ["const:c03eb0:8", "const:4:8"]]
+ 00c03eb0 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00c02ebc bytes 4d6d0194
+ 00c03eb0 bytes 446d0194
~~~


<a id="compare-b014302c757bf75772aa9262f54d7934"></a>

### [`00c02ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02ef0.md) → [`00c03ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03ee4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryC1ERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) · 呼出先 1件 [`00c5e4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4c0.md)
- 新版 呼出元 1件 [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) · 呼出先 1件 [`00c5f490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02ef0.md#insn-00c02f34)
- 新版 [`00c03f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03ee4.md#insn-00c03f28)

~~~diff
- 00c02f34 ["INT_ADD", "register:40f0:8", ["const:c02f34:8", "const:4:8"]]
- 00c02f34 ["CALL", null, ["callee:00c5f490:8"]]
+ 00c03f28 ["INT_ADD", "register:40f0:8", ["const:c03f28:8", "const:4:8"]]
+ 00c03f28 ["CALL", null, ["callee:00c5f490:8"]]
- 00c02f34 bytes 636d0194
+ 00c03f28 bytes 5a6d0194
~~~


<a id="compare-176925337566dcccb4fcf94a86014eca"></a>

### [`00c02f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02f54.md) → [`00c03f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03f48.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE6sentryD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md)
- 新版 呼出元 1件 [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md) · 呼出先 2件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c02f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02f54.md#insn-00c02f90) · [`00c02fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02f54.md#insn-00c02fb4) · [`00c02fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c02/00c02f54.md#insn-00c02fd8)
- 新版 [`00c03f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03f48.md#insn-00c03f84) · [`00c03fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03f48.md#insn-00c03fa8) · [`00c03fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03f48.md#insn-00c03fcc)

~~~diff
- 00c02f90 ["INT_ADD", "register:40f0:8", ["const:c02f90:8", "const:4:8"]]
- 00c02f90 ["CALL", null, ["callee:00c5e190:8"]]
+ 00c03f84 ["INT_ADD", "register:40f0:8", ["const:c03f84:8", "const:4:8"]]
+ 00c03f84 ["CALL", null, ["callee:00c5e190:8"]]
- 00c02f90 bytes 8c680194
+ 00c03f84 bytes 83680194
- 00c02fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c02fb4 ["INT_ADD", "register:40f0:8", ["const:c02fb4:8", "const:4:8"]]
- 00c02fb4 ["CALLIND", null, ["register:0:8"]]
+ 00c03fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c03fa8 ["INT_ADD", "register:40f0:8", ["const:c03fa8:8", "const:4:8"]]
+ 00c03fa8 ["CALLIND", null, ["register:0:8"]]
- 00c02fb4 bytes 00013fd6
+ 00c03fa8 bytes 00013fd6
- 00c02fd8 ["INT_ADD", "register:40f0:8", ["const:c02fd8:8", "const:4:8"]]
- 00c02fd8 ["CALL", null, ["callee:00c59340:8"]]
+ 00c03fcc ["INT_ADD", "register:40f0:8", ["const:c03fcc:8", "const:4:8"]]
+ 00c03fcc ["CALL", null, ["callee:00c59340:8"]]
- 00c02fd8 bytes e6540194
+ 00c03fcc bytes dd540194
~~~


<a id="compare-a8672828b5d3571e2c15d2ed25e17ea7"></a>

### [`00c03008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03008.md) → [`00c03ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03ffc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_9basic_iosIwS2_EES6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c03028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03008.md#insn-00c03028)
- 新版 [`00c0401c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c03/00c03ffc.md#insn-00c0401c)

~~~diff
- 00c03028 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c03028 ["INT_ADD", "register:40f0:8", ["const:c03028:8", "const:4:8"]]
- 00c03028 ["CALLIND", null, ["register:0:8"]]
+ 00c0401c ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c0401c ["INT_ADD", "register:40f0:8", ["const:c0401c:8", "const:4:8"]]
+ 00c0401c ["CALLIND", null, ["register:0:8"]]
- 00c03028 bytes 20003fd6
+ 00c0401c bytes 20003fd6
~~~


<a id="compare-d965dbcd9d6374e199234705db9687eb"></a>

### [`00c03040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03040.md) → [`00c04034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c04/00c04034.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPFRNS_8ios_baseES5_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c03060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c03/00c03040.md#insn-00c03060)
- 新版 [`00c04054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c04/00c04034.md#insn-00c04054)

~~~diff
- 00c03060 ["COPY", "register:0:8", ["register:4008:8"]]
- 00c03060 ["INT_ADD", "register:40f0:8", ["const:c03060:8", "const:4:8"]]
- 00c03060 ["CALLIND", null, ["register:0:8"]]
+ 00c04054 ["COPY", "register:0:8", ["register:4008:8"]]
+ 00c04054 ["INT_ADD", "register:40f0:8", ["const:c04054:8", "const:4:8"]]
+ 00c04054 ["CALLIND", null, ["register:0:8"]]
- 00c03060 bytes 20003fd6
+ 00c04054 bytes 20003fd6
~~~


<a id="compare-aba77b813dd5fd6084a11e18e13a74b2"></a>

### [`00c04528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04528.md) → [`00c0551c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c0551c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04528.md#insn-00c04550) · [`00c045a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04528.md#insn-00c045a4) · [`00c045d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04528.md#insn-00c045d0)
- 新版 [`00c05544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c0551c.md#insn-00c05544) · [`00c05598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c0551c.md#insn-00c05598) · [`00c055c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c0551c.md#insn-00c055c4)

~~~diff
- 00c04550 ["INT_ADD", "register:40f0:8", ["const:c04550:8", "const:4:8"]]
- 00c04550 ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c05544 ["INT_ADD", "register:40f0:8", ["const:c05544:8", "const:4:8"]]
+ 00c05544 ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c04550 bytes e0670194
+ 00c05544 bytes d7670194
- 00c045a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c045a4 ["INT_ADD", "register:40f0:8", ["const:c045a4:8", "const:4:8"]]
- 00c045a4 ["CALLIND", null, ["register:0:8"]]
+ 00c05598 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05598 ["INT_ADD", "register:40f0:8", ["const:c05598:8", "const:4:8"]]
+ 00c05598 ["CALLIND", null, ["register:0:8"]]
- 00c045a4 bytes 00013fd6
+ 00c05598 bytes 00013fd6
- 00c045d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c045d0 ["INT_ADD", "register:40f0:8", ["const:c045d0:8", "const:4:8"]]
- 00c045d0 ["CALLIND", null, ["register:0:8"]]
+ 00c055c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c055c4 ["INT_ADD", "register:40f0:8", ["const:c055c4:8", "const:4:8"]]
+ 00c055c4 ["CALLIND", null, ["register:0:8"]]
- 00c045d0 bytes 00013fd6
+ 00c055c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-837068f1f02d74b91fb31e02ad800bf0"></a>

### [`00c046f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c046f4.md) → [`00c056e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c056e8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE3putEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c046f4.md#insn-00c04718) · [`00c04764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c046f4.md#insn-00c04764) · [`00c04788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c046f4.md#insn-00c04788)
- 新版 [`00c0570c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c056e8.md#insn-00c0570c) · [`00c05758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c056e8.md#insn-00c05758) · [`00c0577c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c056e8.md#insn-00c0577c)

~~~diff
- 00c04718 ["INT_ADD", "register:40f0:8", ["const:c04718:8", "const:4:8"]]
- 00c04718 ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c0570c ["INT_ADD", "register:40f0:8", ["const:c0570c:8", "const:4:8"]]
+ 00c0570c ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c04718 bytes 6e670194
+ 00c0570c bytes 65670194
- 00c04764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04764 ["INT_ADD", "register:40f0:8", ["const:c04764:8", "const:4:8"]]
- 00c04764 ["CALLIND", null, ["register:0:8"]]
+ 00c05758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05758 ["INT_ADD", "register:40f0:8", ["const:c05758:8", "const:4:8"]]
+ 00c05758 ["CALLIND", null, ["register:0:8"]]
- 00c04764 bytes 00013fd6
+ 00c05758 bytes 00013fd6
- 00c04788 ["INT_ADD", "register:40f0:8", ["const:c04788:8", "const:4:8"]]
- 00c04788 ["CALL", null, ["callee:00c59340:8"]]
+ 00c0577c ["INT_ADD", "register:40f0:8", ["const:c0577c:8", "const:4:8"]]
+ 00c0577c ["CALL", null, ["callee:00c59340:8"]]
- 00c04788 bytes fa4e0194
+ 00c0577c bytes f14e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9623c2074a90a0d1e44139175ea0269"></a>

### [`00c047f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c047f4.md) → [`00c057e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c057e8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5writeEPKwl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c047f4.md#insn-00c04820) · [`00c04850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c047f4.md#insn-00c04850) · [`00c04870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c047f4.md#insn-00c04870)
- 新版 [`00c05814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c057e8.md#insn-00c05814) · [`00c05844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c057e8.md#insn-00c05844) · [`00c05864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c057e8.md#insn-00c05864)

~~~diff
- 00c04820 ["INT_ADD", "register:40f0:8", ["const:c04820:8", "const:4:8"]]
- 00c04820 ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c05814 ["INT_ADD", "register:40f0:8", ["const:c05814:8", "const:4:8"]]
+ 00c05814 ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c04820 bytes 2c670194
+ 00c05814 bytes 23670194
- 00c04850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04850 ["INT_ADD", "register:40f0:8", ["const:c04850:8", "const:4:8"]]
- 00c04850 ["CALLIND", null, ["register:0:8"]]
+ 00c05844 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05844 ["INT_ADD", "register:40f0:8", ["const:c05844:8", "const:4:8"]]
+ 00c05844 ["CALLIND", null, ["register:0:8"]]
- 00c04850 bytes 00013fd6
+ 00c05844 bytes 00013fd6
- 00c04870 ["INT_ADD", "register:40f0:8", ["const:c04870:8", "const:4:8"]]
- 00c04870 ["CALL", null, ["callee:00c59340:8"]]
+ 00c05864 ["INT_ADD", "register:40f0:8", ["const:c05864:8", "const:4:8"]]
+ 00c05864 ["CALL", null, ["callee:00c59340:8"]]
- 00c04870 bytes c04e0194
+ 00c05864 bytes b74e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-493420af2d2348d64d85f39192839ba1"></a>

### [`00c048e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c048e0.md) → [`00c058d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c058d4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5tellpEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c048e0.md#insn-00c04930)
- 新版 [`00c05924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c058d4.md#insn-00c05924)

~~~diff
- 00c04930 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04930 ["INT_ADD", "register:40f0:8", ["const:c04930:8", "const:4:8"]]
- 00c04930 ["CALLIND", null, ["register:0:8"]]
+ 00c05924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05924 ["INT_ADD", "register:40f0:8", ["const:c05924:8", "const:4:8"]]
+ 00c05924 ["CALLIND", null, ["register:0:8"]]
- 00c04930 bytes 00013fd6
+ 00c05924 bytes 00013fd6
~~~


<a id="compare-4384b0622a28807175e52aba28fa5a52"></a>

### [`00c04940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04940.md) → [`00c05934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05934.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0496c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04940.md#insn-00c0496c) · [`00c049a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04940.md#insn-00c049a4) · [`00c049c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04940.md#insn-00c049c4)
- 新版 [`00c05960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05934.md#insn-00c05960) · [`00c05998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05934.md#insn-00c05998) · [`00c059b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05934.md#insn-00c059b8)

~~~diff
- 00c0496c ["INT_ADD", "register:40f0:8", ["const:c0496c:8", "const:4:8"]]
- 00c0496c ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c05960 ["INT_ADD", "register:40f0:8", ["const:c05960:8", "const:4:8"]]
+ 00c05960 ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c0496c bytes d9660194
+ 00c05960 bytes d0660194
- 00c049a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c049a4 ["INT_ADD", "register:40f0:8", ["const:c049a4:8", "const:4:8"]]
- 00c049a4 ["CALLIND", null, ["register:0:8"]]
+ 00c05998 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05998 ["INT_ADD", "register:40f0:8", ["const:c05998:8", "const:4:8"]]
+ 00c05998 ["CALLIND", null, ["register:0:8"]]
- 00c049a4 bytes 00013fd6
+ 00c05998 bytes 00013fd6
- 00c049c4 ["INT_ADD", "register:40f0:8", ["const:c049c4:8", "const:4:8"]]
- 00c049c4 ["CALL", null, ["callee:00c59340:8"]]
+ 00c059b8 ["INT_ADD", "register:40f0:8", ["const:c059b8:8", "const:4:8"]]
+ 00c059b8 ["CALL", null, ["callee:00c59340:8"]]
- 00c049c4 bytes 6b4e0194
+ 00c059b8 bytes 624e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4676d1a4f9753d75c2a9a9c812e772ec"></a>

### [`00c04a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04a04.md) → [`00c059f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c059f8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4d0.md) [`00c5e4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4a0.md) [`00c5f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04a04.md#insn-00c04a30) · [`00c04a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04a04.md#insn-00c04a68) · [`00c04a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04a04.md#insn-00c04a88)
- 新版 [`00c05a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c059f8.md#insn-00c05a24) · [`00c05a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c059f8.md#insn-00c05a5c) · [`00c05a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c059f8.md#insn-00c05a7c)

~~~diff
- 00c04a30 ["INT_ADD", "register:40f0:8", ["const:c04a30:8", "const:4:8"]]
- 00c04a30 ["CALL", null, ["callee:00c5f4a0:8"]]
+ 00c05a24 ["INT_ADD", "register:40f0:8", ["const:c05a24:8", "const:4:8"]]
+ 00c05a24 ["CALL", null, ["callee:00c5f4a0:8"]]
- 00c04a30 bytes a8660194
+ 00c05a24 bytes 9f660194
- 00c04a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04a68 ["INT_ADD", "register:40f0:8", ["const:c04a68:8", "const:4:8"]]
- 00c04a68 ["CALLIND", null, ["register:0:8"]]
+ 00c05a5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05a5c ["INT_ADD", "register:40f0:8", ["const:c05a5c:8", "const:4:8"]]
+ 00c05a5c ["CALLIND", null, ["register:0:8"]]
- 00c04a68 bytes 00013fd6
+ 00c05a5c bytes 00013fd6
- 00c04a88 ["INT_ADD", "register:40f0:8", ["const:c04a88:8", "const:4:8"]]
- 00c04a88 ["CALL", null, ["callee:00c59340:8"]]
+ 00c05a7c ["INT_ADD", "register:40f0:8", ["const:c05a7c:8", "const:4:8"]]
+ 00c05a7c ["CALL", null, ["callee:00c59340:8"]]
- 00c04a88 bytes 3a4e0194
+ 00c05a7c bytes 314e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3e4a3e70417317ff074efa3bb9e87be"></a>

### [`00c04b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04b74.md) → [`00c05b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05b68.md) FUN_00c05b68

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c04ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04ac8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 1件 [`00c05abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05abc.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04b74.md#insn-00c04c2c) · [`00c04cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04b74.md#insn-00c04cd0) · [`00c04ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04b74.md#insn-00c04ce4)
- 新版 [`00c05c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05b68.md#insn-00c05c20) · [`00c05cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05b68.md#insn-00c05cc4) · [`00c05cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05b68.md#insn-00c05cd8)

~~~diff
- 00c04c2c ["INT_ADD", "register:40f0:8", ["const:c04c2c:8", "const:4:8"]]
- 00c04c2c ["CALL", null, ["callee:00c58f50:8"]]
+ 00c05c20 ["INT_ADD", "register:40f0:8", ["const:c05c20:8", "const:4:8"]]
+ 00c05c20 ["CALL", null, ["callee:00c58f50:8"]]
- 00c04c2c bytes d54c0194
+ 00c05c20 bytes cc4c0194
- 00c04cd0 ["INT_ADD", "register:40f0:8", ["const:c04cd0:8", "const:4:8"]]
- 00c04cd0 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c05cc4 ["INT_ADD", "register:40f0:8", ["const:c05cc4:8", "const:4:8"]]
+ 00c05cc4 ["CALL", null, ["callee:00c5b870:8"]]
- 00c04cd0 bytes f4560194
+ 00c05cc4 bytes eb560194
- 00c04ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04ce4 ["INT_ADD", "register:40f0:8", ["const:c04ce4:8", "const:4:8"]]
- 00c04ce4 ["CALLIND", null, ["register:0:8"]]
+ 00c05cd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05cd8 ["INT_ADD", "register:40f0:8", ["const:c05cd8:8", "const:4:8"]]
+ 00c05cd8 ["CALLIND", null, ["register:0:8"]]
- 00c04ce4 bytes 00013fd6
+ 00c05cd8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd86db974cd96c3202ee8aea6ddbc636"></a>

### [`00c04d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04d48.md) → [`00c05d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05d3c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 1件 [`00c5f510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f510.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c04e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04d48.md#insn-00c04e00) · [`00c04ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04d48.md#insn-00c04ec8) · [`00c04edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04d48.md#insn-00c04edc)
- 新版 [`00c05df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05d3c.md#insn-00c05df4) · [`00c05ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05d3c.md#insn-00c05ebc) · [`00c05ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05d3c.md#insn-00c05ed0)

~~~diff
- 00c04e00 ["INT_ADD", "register:40f0:8", ["const:c04e00:8", "const:4:8"]]
- 00c04e00 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c05df4 ["INT_ADD", "register:40f0:8", ["const:c05df4:8", "const:4:8"]]
+ 00c05df4 ["CALL", null, ["callee:00c58f50:8"]]
- 00c04e00 bytes 604c0194
+ 00c05df4 bytes 574c0194
- 00c04ec8 ["INT_ADD", "register:40f0:8", ["const:c04ec8:8", "const:4:8"]]
- 00c04ec8 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c05ebc ["INT_ADD", "register:40f0:8", ["const:c05ebc:8", "const:4:8"]]
+ 00c05ebc ["CALL", null, ["callee:00c5b870:8"]]
- 00c04ec8 bytes 76560194
+ 00c05ebc bytes 6d560194
- 00c04edc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c04edc ["INT_ADD", "register:40f0:8", ["const:c04edc:8", "const:4:8"]]
- 00c04edc ["CALLIND", null, ["register:0:8"]]
+ 00c05ed0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c05ed0 ["INT_ADD", "register:40f0:8", ["const:c05ed0:8", "const:4:8"]]
+ 00c05ed0 ["CALLIND", null, ["register:0:8"]]
- 00c04edc bytes 00013fd6
+ 00c05ed0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08138b8dc161afd539495da6f2c6c5c"></a>

### [`00c04f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04f44.md) → [`00c05f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05f38.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4swapERS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04f44.md#insn-00c05178) · [`00c05184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04f44.md#insn-00c05184) · [`00c05198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c04/00c04f44.md#insn-00c05198)
- 新版 [`00c0616c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05f38.md#insn-00c0616c) · [`00c06178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05f38.md#insn-00c06178) · [`00c0618c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c05/00c05f38.md#insn-00c0618c)

~~~diff
- 00c05178 ["INT_ADD", "register:40f0:8", ["const:c05178:8", "const:4:8"]]
- 00c05178 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c0616c ["INT_ADD", "register:40f0:8", ["const:c0616c:8", "const:4:8"]]
+ 00c0616c ["CALL", null, ["callee:00c5b870:8"]]
- 00c05178 bytes ca550194
+ 00c0616c bytes c1550194
- 00c05184 ["INT_ADD", "register:40f0:8", ["const:c05184:8", "const:4:8"]]
- 00c05184 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c06178 ["INT_ADD", "register:40f0:8", ["const:c06178:8", "const:4:8"]]
+ 00c06178 ["CALL", null, ["callee:00c5b870:8"]]
- 00c05184 bytes c7550194
+ 00c06178 bytes be550194
- 00c05198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c05198 ["INT_ADD", "register:40f0:8", ["const:c05198:8", "const:4:8"]]
- 00c05198 ["CALLIND", null, ["register:0:8"]]
+ 00c0618c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0618c ["INT_ADD", "register:40f0:8", ["const:c0618c:8", "const:4:8"]]
+ 00c0618c ["CALLIND", null, ["register:0:8"]]
- 00c05198 bytes 00013fd6
+ 00c0618c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48a7e482199d57dfaf181f110c7075a"></a>

### [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) → [`00c06210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06210.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00bf2244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md) [`00bf22f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005485b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005485b8.md) [`00bf3238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3238.md) [`00bf32ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf32ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md#insn-00c05278) · [`00c05290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md#insn-00c05290)
- 新版 [`00c0626c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06210.md#insn-00c0626c) · [`00c06284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06210.md#insn-00c06284)

~~~diff
- 00c05278 ["INT_ADD", "register:40f0:8", ["const:c05278:8", "const:4:8"]]
- 00c05278 ["CALL", null, ["callee:00bf32ec:8"]]
+ 00c0626c ["INT_ADD", "register:40f0:8", ["const:c0626c:8", "const:4:8"]]
+ 00c0626c ["CALL", null, ["callee:00bf32ec:8"]]
- 00c05278 bytes 20b4ff97
+ 00c0626c bytes 20b4ff97
- 00c05290 ["INT_ADD", "register:40f0:8", ["const:c05290:8", "const:4:8"]]
- 00c05290 ["CALL", null, ["callee:00bf3238:8"]]
+ 00c06284 ["INT_ADD", "register:40f0:8", ["const:c06284:8", "const:4:8"]]
+ 00c06284 ["CALL", null, ["callee:00bf3238:8"]]
- 00c05290 bytes edb3ff97
+ 00c06284 bytes edb3ff97
~~~


<a id="compare-f702386183a5a2cdce7dc0314e986911"></a>

### [`00c052a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c052a8.md) → [`00c0629c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c0629c.md) _ZNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md) [`00c5f510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c052ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c052a8.md#insn-00c052ec) · [`00c05318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c052a8.md#insn-00c05318)
- 新版 [`00c062e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c0629c.md#insn-00c062e0) · [`00c0630c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c0629c.md#insn-00c0630c)

~~~diff
- 00c052ec ["INT_ADD", "register:40f0:8", ["const:c052ec:8", "const:4:8"]]
- 00c052ec ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c062e0 ["INT_ADD", "register:40f0:8", ["const:c062e0:8", "const:4:8"]]
+ 00c062e0 ["CALL", null, ["callee:00c5f3c0:8"]]
- 00c052ec bytes 41640194
+ 00c062e0 bytes 38640194
- 00c05318 ["INT_ADD", "register:40f0:8", ["const:c05318:8", "const:4:8"]]
- 00c05318 ["CALL", null, ["callee:00c5f510:8"]]
+ 00c0630c ["INT_ADD", "register:40f0:8", ["const:c0630c:8", "const:4:8"]]
+ 00c0630c ["CALL", null, ["callee:00c5f510:8"]]
- 00c05318 bytes 8a640194
+ 00c0630c bytes 81640194
~~~


<a id="compare-00f634321dfe068779c91f4e9d4355ac"></a>

### [`00c05334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05334.md) → [`00c06328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06328.md) _ZNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md) [`00c5f510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05334.md#insn-00c05378) · [`00c053a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05334.md#insn-00c053a4)
- 新版 [`00c0636c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06328.md#insn-00c0636c) · [`00c06398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06328.md#insn-00c06398)

~~~diff
- 00c05378 ["INT_ADD", "register:40f0:8", ["const:c05378:8", "const:4:8"]]
- 00c05378 ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c0636c ["INT_ADD", "register:40f0:8", ["const:c0636c:8", "const:4:8"]]
+ 00c0636c ["CALL", null, ["callee:00c5f3c0:8"]]
- 00c05378 bytes 1e640194
+ 00c0636c bytes 15640194
- 00c053a4 ["INT_ADD", "register:40f0:8", ["const:c053a4:8", "const:4:8"]]
- 00c053a4 ["CALL", null, ["callee:00c5f510:8"]]
+ 00c06398 ["INT_ADD", "register:40f0:8", ["const:c06398:8", "const:4:8"]]
+ 00c06398 ["CALL", null, ["callee:00c5f510:8"]]
- 00c053a4 bytes 67640194
+ 00c06398 bytes 5e640194
~~~


<a id="compare-0579b9b06034897f621dedcafd57773d"></a>

### [`00c053c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c053c4.md) → [`00c063b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c063b8.md) _ZNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3f0.md) [`00c5e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e540.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f3c0.md) [`00c5f510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f510.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c053c4.md#insn-00c05408) · [`00c05434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c053c4.md#insn-00c05434)
- 新版 [`00c063fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c063b8.md#insn-00c063fc) · [`00c06428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c063b8.md#insn-00c06428)

~~~diff
- 00c05408 ["INT_ADD", "register:40f0:8", ["const:c05408:8", "const:4:8"]]
- 00c05408 ["CALL", null, ["callee:00c5f3c0:8"]]
+ 00c063fc ["INT_ADD", "register:40f0:8", ["const:c063fc:8", "const:4:8"]]
+ 00c063fc ["CALL", null, ["callee:00c5f3c0:8"]]
- 00c05408 bytes fa630194
+ 00c063fc bytes f1630194
- 00c05434 ["INT_ADD", "register:40f0:8", ["const:c05434:8", "const:4:8"]]
- 00c05434 ["CALL", null, ["callee:00c5f510:8"]]
+ 00c06428 ["INT_ADD", "register:40f0:8", ["const:c06428:8", "const:4:8"]]
+ 00c06428 ["CALL", null, ["callee:00c5f510:8"]]
- 00c05434 bytes 43640194
+ 00c06428 bytes 3a640194
~~~


<a id="compare-cba224a766a0b78446ad8bd2d657fe98"></a>

### [`00c05450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05450.md) → [`00c06444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06444.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c06e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06e5c.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c054a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05450.md#insn-00c054a8) · [`00c054b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05450.md#insn-00c054b8) · [`00c054d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05450.md#insn-00c054d4)
- 新版 [`00c0649c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06444.md#insn-00c0649c) · [`00c064ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06444.md#insn-00c064ac) · [`00c064c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06444.md#insn-00c064c8)

~~~diff
- 00c054a8 ["INT_ADD", "register:40f0:8", ["const:c054a8:8", "const:4:8"]]
- 00c054a8 ["CALL", null, ["callee:00c06e5c:8"]]
+ 00c0649c ["INT_ADD", "register:40f0:8", ["const:c0649c:8", "const:4:8"]]
+ 00c0649c ["CALL", null, ["callee:00c06e5c:8"]]
- 00c054a8 bytes 70020094
+ 00c0649c bytes 70020094
- 00c054b8 ["INT_ADD", "register:40f0:8", ["const:c054b8:8", "const:4:8"]]
- 00c054b8 ["CALL", null, ["callee:00c5b130:8"]]
+ 00c064ac ["INT_ADD", "register:40f0:8", ["const:c064ac:8", "const:4:8"]]
+ 00c064ac ["CALL", null, ["callee:00c5b130:8"]]
- 00c054b8 bytes 2a530194
+ 00c064ac bytes 21530194
- 00c054d4 ["INT_ADD", "register:40f0:8", ["const:c054d4:8", "const:4:8"]]
- 00c054d4 ["CALL", null, ["callee:00c5b100:8"]]
+ 00c064c8 ["INT_ADD", "register:40f0:8", ["const:c064c8:8", "const:4:8"]]
+ 00c064c8 ["CALL", null, ["callee:00c5b100:8"]]
- 00c054d4 bytes 17530194
+ 00c064c8 bytes 0e530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9257fea8a6ddfe1604de58d521a32900"></a>

### [`00c05500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05500.md) → [`00c064f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c064f4.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c06e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06e5c.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05500.md#insn-00c05564) · [`00c05574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05500.md#insn-00c05574) · [`00c05590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05500.md#insn-00c05590)
- 新版 [`00c06558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c064f4.md#insn-00c06558) · [`00c06568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c064f4.md#insn-00c06568) · [`00c06584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c064f4.md#insn-00c06584)

~~~diff
- 00c05564 ["INT_ADD", "register:40f0:8", ["const:c05564:8", "const:4:8"]]
- 00c05564 ["CALL", null, ["callee:00c06e5c:8"]]
+ 00c06558 ["INT_ADD", "register:40f0:8", ["const:c06558:8", "const:4:8"]]
+ 00c06558 ["CALL", null, ["callee:00c06e5c:8"]]
- 00c05564 bytes 41020094
+ 00c06558 bytes 41020094
- 00c05574 ["INT_ADD", "register:40f0:8", ["const:c05574:8", "const:4:8"]]
- 00c05574 ["CALL", null, ["callee:00c5b130:8"]]
+ 00c06568 ["INT_ADD", "register:40f0:8", ["const:c06568:8", "const:4:8"]]
+ 00c06568 ["CALL", null, ["callee:00c5b130:8"]]
- 00c05574 bytes fb520194
+ 00c06568 bytes f2520194
- 00c05590 ["INT_ADD", "register:40f0:8", ["const:c05590:8", "const:4:8"]]
- 00c05590 ["CALL", null, ["callee:00c5b100:8"]]
+ 00c06584 ["INT_ADD", "register:40f0:8", ["const:c06584:8", "const:4:8"]]
+ 00c06584 ["CALL", null, ["callee:00c5b100:8"]]
- 00c05590 bytes e8520194
+ 00c06584 bytes df520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e259f93da099fac3a3e2d15356eb84bc"></a>

### [`00c055bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c055bc.md) → [`00c065b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c065b0.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c06e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06e5c.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c055bc.md#insn-00c05614) · [`00c05624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c055bc.md#insn-00c05624) · [`00c05640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c055bc.md#insn-00c05640)
- 新版 [`00c06608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c065b0.md#insn-00c06608) · [`00c06618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c065b0.md#insn-00c06618) · [`00c06634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c065b0.md#insn-00c06634)

~~~diff
- 00c05614 ["INT_ADD", "register:40f0:8", ["const:c05614:8", "const:4:8"]]
- 00c05614 ["CALL", null, ["callee:00c06e5c:8"]]
+ 00c06608 ["INT_ADD", "register:40f0:8", ["const:c06608:8", "const:4:8"]]
+ 00c06608 ["CALL", null, ["callee:00c06e5c:8"]]
- 00c05614 bytes 15020094
+ 00c06608 bytes 15020094
- 00c05624 ["INT_ADD", "register:40f0:8", ["const:c05624:8", "const:4:8"]]
- 00c05624 ["CALL", null, ["callee:00c5b130:8"]]
+ 00c06618 ["INT_ADD", "register:40f0:8", ["const:c06618:8", "const:4:8"]]
+ 00c06618 ["CALL", null, ["callee:00c5b130:8"]]
- 00c05624 bytes cf520194
+ 00c06618 bytes c6520194
- 00c05640 ["INT_ADD", "register:40f0:8", ["const:c05640:8", "const:4:8"]]
- 00c05640 ["CALL", null, ["callee:00c5b100:8"]]
+ 00c06634 ["INT_ADD", "register:40f0:8", ["const:c06634:8", "const:4:8"]]
+ 00c06634 ["CALL", null, ["callee:00c5b100:8"]]
- 00c05640 bytes bc520194
+ 00c06634 bytes b3520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a696d8bcad93574b56eb27c9a7f04935"></a>

### [`00c0566c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0566c.md) → [`00c06660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06660.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05e68.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c06e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06e5c.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c056d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0566c.md#insn-00c056d0) · [`00c056e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0566c.md#insn-00c056e0) · [`00c056fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0566c.md#insn-00c056fc)
- 新版 [`00c066c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06660.md#insn-00c066c4) · [`00c066d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06660.md#insn-00c066d4) · [`00c066f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06660.md#insn-00c066f0)

~~~diff
- 00c056d0 ["INT_ADD", "register:40f0:8", ["const:c056d0:8", "const:4:8"]]
- 00c056d0 ["CALL", null, ["callee:00c06e5c:8"]]
+ 00c066c4 ["INT_ADD", "register:40f0:8", ["const:c066c4:8", "const:4:8"]]
+ 00c066c4 ["CALL", null, ["callee:00c06e5c:8"]]
- 00c056d0 bytes e6010094
+ 00c066c4 bytes e6010094
- 00c056e0 ["INT_ADD", "register:40f0:8", ["const:c056e0:8", "const:4:8"]]
- 00c056e0 ["CALL", null, ["callee:00c5b130:8"]]
+ 00c066d4 ["INT_ADD", "register:40f0:8", ["const:c066d4:8", "const:4:8"]]
+ 00c066d4 ["CALL", null, ["callee:00c5b130:8"]]
- 00c056e0 bytes a0520194
+ 00c066d4 bytes 97520194
- 00c056fc ["INT_ADD", "register:40f0:8", ["const:c056fc:8", "const:4:8"]]
- 00c056fc ["CALL", null, ["callee:00c5b100:8"]]
+ 00c066f0 ["INT_ADD", "register:40f0:8", ["const:c066f0:8", "const:4:8"]]
+ 00c066f0 ["CALL", null, ["callee:00c5b100:8"]]
- 00c056fc bytes 8d520194
+ 00c066f0 bytes 84520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7955c46faf1f65e2c68f01a8973f9c0d"></a>

### [`00c05ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ab4.md) → [`00c06aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06aa8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE5closeEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ab4.md#insn-00c05adc) · [`00c05ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ab4.md#insn-00c05ae8) · [`00c05b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ab4.md#insn-00c05b10)
- 新版 [`00c06ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06aa8.md#insn-00c06ad0) · [`00c06adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06aa8.md#insn-00c06adc) · [`00c06b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06aa8.md#insn-00c06b04)

~~~diff
- 00c05adc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c05adc ["INT_ADD", "register:40f0:8", ["const:c05adc:8", "const:4:8"]]
- 00c05adc ["CALLIND", null, ["register:0:8"]]
+ 00c06ad0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06ad0 ["INT_ADD", "register:40f0:8", ["const:c06ad0:8", "const:4:8"]]
+ 00c06ad0 ["CALLIND", null, ["register:0:8"]]
- 00c05adc bytes 00013fd6
+ 00c06ad0 bytes 00013fd6
- 00c05ae8 ["INT_ADD", "register:40f0:8", ["const:c05ae8:8", "const:4:8"]]
- 00c05ae8 ["CALL", null, ["callee:00c5b0a0:8"]]
+ 00c06adc ["INT_ADD", "register:40f0:8", ["const:c06adc:8", "const:4:8"]]
+ 00c06adc ["CALL", null, ["callee:00c5b0a0:8"]]
- 00c05ae8 bytes 7a510194
+ 00c06adc bytes 71510194
- 00c05b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c05b10 ["INT_ADD", "register:40f0:8", ["const:c05b10:8", "const:4:8"]]
- 00c05b10 ["CALLIND", null, ["register:0:8"]]
+ 00c06b04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06b04 ["INT_ADD", "register:40f0:8", ["const:c06b04:8", "const:4:8"]]
+ 00c06b04 ["CALLIND", null, ["register:0:8"]]
- 00c05b10 bytes 00013fd6
+ 00c06b04 bytes 00013fd6
~~~


<a id="compare-6ff7d165b2af08f69a54ef1451bd7bc6"></a>

### [`00c05b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b40.md) → [`00c06b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b34.md) FUN_00c06b34

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b40.md#insn-00c05b54)
- 新版 [`00c06b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b34.md#insn-00c06b48)

~~~diff
- 00c05b54 ["INT_ADD", "register:40f0:8", ["const:c05b54:8", "const:4:8"]]
- 00c05b54 ["CALL", null, ["callee:00c59fc0:8"]]
+ 00c06b48 ["INT_ADD", "register:40f0:8", ["const:c06b48:8", "const:4:8"]]
+ 00c06b48 ["CALL", null, ["callee:00c59fc0:8"]]
- 00c05b54 bytes 274d0194
+ 00c06b48 bytes 1e4d0194
~~~


<a id="compare-df8e60353ec904e42956f70b4fe10a1c"></a>

### [`00c05b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b6c.md) → [`00c06b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b60.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c05b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b6c.md#insn-00c05b90) · [`00c05b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b6c.md#insn-00c05b9c) · [`00c05ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05b6c.md#insn-00c05ba8)
- 新版 [`00c06b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b60.md#insn-00c06b84) · [`00c06b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b60.md#insn-00c06b90) · [`00c06b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06b60.md#insn-00c06b9c)

~~~diff
- 00c05b90 ["INT_ADD", "register:40f0:8", ["const:c05b90:8", "const:4:8"]]
- 00c05b90 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c06b84 ["INT_ADD", "register:40f0:8", ["const:c06b84:8", "const:4:8"]]
+ 00c06b84 ["CALL", null, ["callee:00c5b870:8"]]
- 00c05b90 bytes 44530194
+ 00c06b84 bytes 3b530194
- 00c05b9c ["INT_ADD", "register:40f0:8", ["const:c05b9c:8", "const:4:8"]]
- 00c05b9c ["CALL", null, ["callee:00c5f380:8"]]
+ 00c06b90 ["INT_ADD", "register:40f0:8", ["const:c06b90:8", "const:4:8"]]
+ 00c06b90 ["CALL", null, ["callee:00c5f380:8"]]
- 00c05b9c bytes 05620194
+ 00c06b90 bytes fc610194
- 00c05ba8 ["INT_ADD", "register:40f0:8", ["const:c05ba8:8", "const:4:8"]]
- 00c05ba8 ["CALL", null, ["callee:00c5f380:8"]]
+ 00c06b9c ["INT_ADD", "register:40f0:8", ["const:c06b9c:8", "const:4:8"]]
+ 00c06b9c ["CALL", null, ["callee:00c5f380:8"]]
- 00c05ba8 bytes 02620194
+ 00c06b9c bytes f9610194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb72ac81488f4a54da6800defec8422"></a>

### [`00c068ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c068ac.md) → [`00c078a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c078a0.md) FUN_00c078a0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c068c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c068ac.md#insn-00c068c0)
- 新版 [`00c078b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c078a0.md#insn-00c078b4)

~~~diff
- 00c068c0 ["INT_ADD", "register:40f0:8", ["const:c068c0:8", "const:4:8"]]
- 00c068c0 ["CALL", null, ["callee:00c59040:8"]]
+ 00c078b4 ["INT_ADD", "register:40f0:8", ["const:c078b4:8", "const:4:8"]]
+ 00c078b4 ["CALL", null, ["callee:00c59040:8"]]
- 00c068c0 bytes ec450194
+ 00c078b4 bytes e3450194
~~~


<a id="compare-c9136f28a3f2825193de2ef6446369db"></a>

### [`00c06970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06970.md) → [`00c07964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07964.md) FUN_00c07964

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c069b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06970.md#insn-00c069b0) · [`00c06a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06970.md#insn-00c06a10) · [`00c06a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06970.md#insn-00c06a5c)
- 新版 [`00c079a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07964.md#insn-00c079a4) · [`00c07a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07964.md#insn-00c07a04) · [`00c07a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07964.md#insn-00c07a50)

~~~diff
- 00c069b0 ["INT_ADD", "register:40f0:8", ["const:c069b0:8", "const:4:8"]]
- 00c069b0 ["CALL", null, ["callee:00c5f540:8"]]
+ 00c079a4 ["INT_ADD", "register:40f0:8", ["const:c079a4:8", "const:4:8"]]
+ 00c079a4 ["CALL", null, ["callee:00c5f540:8"]]
- 00c069b0 bytes f05e0194
+ 00c079a4 bytes e75e0194
- 00c06a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06a10 ["INT_ADD", "register:40f0:8", ["const:c06a10:8", "const:4:8"]]
- 00c06a10 ["CALLIND", null, ["register:0:8"]]
+ 00c07a04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07a04 ["INT_ADD", "register:40f0:8", ["const:c07a04:8", "const:4:8"]]
+ 00c07a04 ["CALLIND", null, ["register:0:8"]]
- 00c06a10 bytes 00013fd6
+ 00c07a04 bytes 00013fd6
- 00c06a5c ["INT_ADD", "register:40f0:8", ["const:c06a5c:8", "const:4:8"]]
- 00c06a5c ["CALL", null, ["callee:00c5f540:8"]]
+ 00c07a50 ["INT_ADD", "register:40f0:8", ["const:c07a50:8", "const:4:8"]]
+ 00c07a50 ["CALL", null, ["callee:00c5f540:8"]]
- 00c06a5c bytes c55e0194
+ 00c07a50 bytes bc5e0194
~~~


<a id="compare-4915e97e631cffa2670cb26fc0afe07f"></a>

### [`00c06a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06a98.md) → [`00c07a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07a8c.md) FUN_00c07a8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c06958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06958.md) [`00c06964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06964.md) · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e580.md)
- 新版 呼出元 2件 [`00c0794c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c0794c.md) [`00c07958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07958.md) · 呼出先 2件 [`00c5f540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f540.md) [`00c5f550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06a98.md#insn-00c06ae8) · [`00c06b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06a98.md#insn-00c06b1c) · [`00c06b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06a98.md#insn-00c06b68)
- 新版 [`00c07adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07a8c.md#insn-00c07adc) · [`00c07b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07a8c.md#insn-00c07b10) · [`00c07b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07a8c.md#insn-00c07b5c)

~~~diff
- 00c06ae8 ["INT_ADD", "register:40f0:8", ["const:c06ae8:8", "const:4:8"]]
- 00c06ae8 ["CALL", null, ["callee:00c5f550:8"]]
+ 00c07adc ["INT_ADD", "register:40f0:8", ["const:c07adc:8", "const:4:8"]]
+ 00c07adc ["CALL", null, ["callee:00c5f550:8"]]
- 00c06ae8 bytes a65e0194
+ 00c07adc bytes 9d5e0194
- 00c06b1c ["INT_ADD", "register:40f0:8", ["const:c06b1c:8", "const:4:8"]]
- 00c06b1c ["CALL", null, ["callee:00c5f550:8"]]
+ 00c07b10 ["INT_ADD", "register:40f0:8", ["const:c07b10:8", "const:4:8"]]
+ 00c07b10 ["CALL", null, ["callee:00c5f550:8"]]
- 00c06b1c bytes 995e0194
+ 00c07b10 bytes 905e0194
- 00c06b68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06b68 ["INT_ADD", "register:40f0:8", ["const:c06b68:8", "const:4:8"]]
- 00c06b68 ["CALLIND", null, ["register:0:8"]]
+ 00c07b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07b5c ["INT_ADD", "register:40f0:8", ["const:c07b5c:8", "const:4:8"]]
+ 00c07b5c ["CALLIND", null, ["register:0:8"]]
- 00c06b68 bytes 00013fd6
+ 00c07b5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ced364033f98ec7a2f7b3ee33337615"></a>

### [`00c06c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06c40.md) → [`00c07c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07c34.md) FUN_00c07c34

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06c40.md#insn-00c06c54)
- 新版 [`00c07c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07c34.md#insn-00c07c48)

~~~diff
- 00c06c54 ["INT_ADD", "register:40f0:8", ["const:c06c54:8", "const:4:8"]]
- 00c06c54 ["CALL", null, ["callee:00c59040:8"]]
+ 00c07c48 ["INT_ADD", "register:40f0:8", ["const:c07c48:8", "const:4:8"]]
+ 00c07c48 ["CALL", null, ["callee:00c59040:8"]]
- 00c06c54 bytes 07450194
+ 00c07c48 bytes fe440194
~~~


<a id="compare-14122722167962ff53abd5b756b95fba"></a>

### [`00c06cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06cc8.md) → [`00c07cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07cbc.md) FUN_00c07cbc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06cc8.md#insn-00c06d00) · [`00c06d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06cc8.md#insn-00c06d20) · [`00c06d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06cc8.md#insn-00c06d48)
- 新版 [`00c07cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07cbc.md#insn-00c07cf4) · [`00c07d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07cbc.md#insn-00c07d14) · [`00c07d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07cbc.md#insn-00c07d3c)

~~~diff
- 00c06d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06d00 ["INT_ADD", "register:40f0:8", ["const:c06d00:8", "const:4:8"]]
- 00c06d00 ["CALLIND", null, ["register:0:8"]]
+ 00c07cf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07cf4 ["INT_ADD", "register:40f0:8", ["const:c07cf4:8", "const:4:8"]]
+ 00c07cf4 ["CALLIND", null, ["register:0:8"]]
- 00c06d00 bytes 00013fd6
+ 00c07cf4 bytes 00013fd6
- 00c06d20 ["INT_ADD", "register:40f0:8", ["const:c06d20:8", "const:4:8"]]
- 00c06d20 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c07d14 ["INT_ADD", "register:40f0:8", ["const:c07d14:8", "const:4:8"]]
+ 00c07d14 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c06d20 bytes 744d0194
+ 00c07d14 bytes 6b4d0194
- 00c06d48 ["INT_ADD", "register:40f0:8", ["const:c06d48:8", "const:4:8"]]
- 00c06d48 ["CALL", null, ["callee:00c5b250:8"]]
+ 00c07d3c ["INT_ADD", "register:40f0:8", ["const:c07d3c:8", "const:4:8"]]
+ 00c07d3c ["CALL", null, ["callee:00c5b250:8"]]
- 00c06d48 bytes 4e4d0194
+ 00c07d3c bytes 454d0194
~~~


<a id="compare-bf3d6f9ba41130071046e010ab4e360b"></a>

### [`00c06d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06d6c.md) → [`00c07d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07d60.md) FUN_00c07d60

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06d6c.md#insn-00c06dd4)
- 新版 [`00c07dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07d60.md#insn-00c07dc8)

~~~diff
- 00c06dd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06dd4 ["INT_ADD", "register:40f0:8", ["const:c06dd4:8", "const:4:8"]]
- 00c06dd4 ["CALLIND", null, ["register:0:8"]]
+ 00c07dc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07dc8 ["INT_ADD", "register:40f0:8", ["const:c07dc8:8", "const:4:8"]]
+ 00c07dc8 ["CALLIND", null, ["register:0:8"]]
- 00c06dd4 bytes 00013fd6
+ 00c07dc8 bytes 00013fd6
~~~


<a id="compare-432ed5d689571e9577aea47c3a632c37"></a>

### [`00c06e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06e10.md) → [`00c07e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07e04.md) FUN_00c07e04

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06e10.md#insn-00c06e5c) · [`00c06ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06e10.md#insn-00c06ea8) · [`00c06ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06e10.md#insn-00c06ee4)
- 新版 [`00c07e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07e04.md#insn-00c07e50) · [`00c07e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07e04.md#insn-00c07e9c) · [`00c07ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07e04.md#insn-00c07ed8)

~~~diff
- 00c06e5c ["INT_ADD", "register:40f0:8", ["const:c06e5c:8", "const:4:8"]]
- 00c06e5c ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c07e50 ["INT_ADD", "register:40f0:8", ["const:c07e50:8", "const:4:8"]]
+ 00c07e50 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c06e5c bytes 254d0194
+ 00c07e50 bytes 1c4d0194
- 00c06ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c06ea8 ["INT_ADD", "register:40f0:8", ["const:c06ea8:8", "const:4:8"]]
- 00c06ea8 ["CALLIND", null, ["register:0:8"]]
+ 00c07e9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c07e9c ["INT_ADD", "register:40f0:8", ["const:c07e9c:8", "const:4:8"]]
+ 00c07e9c ["CALLIND", null, ["register:0:8"]]
- 00c06ea8 bytes 00013fd6
+ 00c07e9c bytes 00013fd6
- 00c06ee4 ["INT_ADD", "register:40f0:8", ["const:c06ee4:8", "const:4:8"]]
- 00c06ee4 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c07ed8 ["INT_ADD", "register:40f0:8", ["const:c07ed8:8", "const:4:8"]]
+ 00c07ed8 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c06ee4 bytes 034d0194
+ 00c07ed8 bytes fa4c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f918276a8a53db101262d01dcf9b25a"></a>

### [`00c06f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06f40.md) → [`00c07f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07f34.md) FUN_00c07f34

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c06f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06f40.md#insn-00c06f54)
- 新版 [`00c07f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07f34.md#insn-00c07f48)

~~~diff
- 00c06f54 ["INT_ADD", "register:40f0:8", ["const:c06f54:8", "const:4:8"]]
- 00c06f54 ["CALL", null, ["callee:00c5f460:8"]]
+ 00c07f48 ["INT_ADD", "register:40f0:8", ["const:c07f48:8", "const:4:8"]]
+ 00c07f48 ["CALL", null, ["callee:00c5f460:8"]]
- 00c06f54 bytes 4f5d0194
+ 00c07f48 bytes 465d0194
~~~


<a id="compare-6e04367efaacfb39a32f875dce70d863"></a>

### [`00c07004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07004.md) → [`00c07ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07ff8.md) FUN_00c07ff8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e590.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f540.md) [`00c5f560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f560.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07004.md#insn-00c07044) · [`00c070a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07004.md#insn-00c070a4) · [`00c070f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07004.md#insn-00c070f0)
- 新版 [`00c08038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07ff8.md#insn-00c08038) · [`00c08098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07ff8.md#insn-00c08098) · [`00c080e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07ff8.md#insn-00c080e4)

~~~diff
- 00c07044 ["INT_ADD", "register:40f0:8", ["const:c07044:8", "const:4:8"]]
- 00c07044 ["CALL", null, ["callee:00c5f560:8"]]
+ 00c08038 ["INT_ADD", "register:40f0:8", ["const:c08038:8", "const:4:8"]]
+ 00c08038 ["CALL", null, ["callee:00c5f560:8"]]
- 00c07044 bytes 535d0194
+ 00c08038 bytes 4a5d0194
- 00c070a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c070a4 ["INT_ADD", "register:40f0:8", ["const:c070a4:8", "const:4:8"]]
- 00c070a4 ["CALLIND", null, ["register:0:8"]]
+ 00c08098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08098 ["INT_ADD", "register:40f0:8", ["const:c08098:8", "const:4:8"]]
+ 00c08098 ["CALLIND", null, ["register:0:8"]]
- 00c070a4 bytes 00013fd6
+ 00c08098 bytes 00013fd6
- 00c070f0 ["INT_ADD", "register:40f0:8", ["const:c070f0:8", "const:4:8"]]
- 00c070f0 ["CALL", null, ["callee:00c5f540:8"]]
+ 00c080e4 ["INT_ADD", "register:40f0:8", ["const:c080e4:8", "const:4:8"]]
+ 00c080e4 ["CALL", null, ["callee:00c5f540:8"]]
- 00c070f0 bytes 205d0194
+ 00c080e4 bytes 175d0194
~~~


<a id="compare-92717f254ef7e4182774addc9e795995"></a>

### [`00c0712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0712c.md) → [`00c08120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08120.md) FUN_00c08120

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c06fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06fec.md) [`00c06ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c06/00c06ff8.md) · 呼出先 4件 [`00c5e570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e570.md) [`00c5e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e580.md) [`00c5e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e590.md) [`00c5e5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5a0.md)
- 新版 呼出元 2件 [`00c07fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07fe0.md) [`00c07fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c07/00c07fec.md) · 呼出先 4件 [`00c5f540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f540.md) [`00c5f550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f550.md) [`00c5f560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f560.md) [`00c5f570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f570.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0717c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0712c.md#insn-00c0717c) · [`00c071ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0712c.md#insn-00c071ac) · [`00c071f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0712c.md#insn-00c071f8)
- 新版 [`00c08170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08120.md#insn-00c08170) · [`00c081a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08120.md#insn-00c081a0) · [`00c081ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08120.md#insn-00c081ec)

~~~diff
- 00c0717c ["INT_ADD", "register:40f0:8", ["const:c0717c:8", "const:4:8"]]
- 00c0717c ["CALL", null, ["callee:00c5f570:8"]]
+ 00c08170 ["INT_ADD", "register:40f0:8", ["const:c08170:8", "const:4:8"]]
+ 00c08170 ["CALL", null, ["callee:00c5f570:8"]]
- 00c0717c bytes 095d0194
+ 00c08170 bytes 005d0194
- 00c071ac ["INT_ADD", "register:40f0:8", ["const:c071ac:8", "const:4:8"]]
- 00c071ac ["CALL", null, ["callee:00c5f550:8"]]
+ 00c081a0 ["INT_ADD", "register:40f0:8", ["const:c081a0:8", "const:4:8"]]
+ 00c081a0 ["CALL", null, ["callee:00c5f550:8"]]
- 00c071ac bytes f55c0194
+ 00c081a0 bytes ec5c0194
- 00c071f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c071f8 ["INT_ADD", "register:40f0:8", ["const:c071f8:8", "const:4:8"]]
- 00c071f8 ["CALLIND", null, ["register:0:8"]]
+ 00c081ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c081ec ["INT_ADD", "register:40f0:8", ["const:c081ec:8", "const:4:8"]]
+ 00c081ec ["CALLIND", null, ["register:0:8"]]
- 00c071f8 bytes 00013fd6
+ 00c081ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c814e67b4dc8da60588650c5e033a614"></a>

### [`00c072cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c072cc.md) → [`00c082c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c082c0.md) FUN_00c082c0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c072e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c072cc.md#insn-00c072e0)
- 新版 [`00c082d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c082c0.md#insn-00c082d4)

~~~diff
- 00c072e0 ["INT_ADD", "register:40f0:8", ["const:c072e0:8", "const:4:8"]]
- 00c072e0 ["CALL", null, ["callee:00c5f460:8"]]
+ 00c082d4 ["INT_ADD", "register:40f0:8", ["const:c082d4:8", "const:4:8"]]
+ 00c082d4 ["CALL", null, ["callee:00c5f460:8"]]
- 00c072e0 bytes 6c5c0194
+ 00c082d4 bytes 635c0194
~~~


<a id="compare-845d1d732e6cfa1cf63a7743fa31e98e"></a>

### [`00c07354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07354.md) → [`00c08348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08348.md) FUN_00c08348

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0738c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07354.md#insn-00c0738c) · [`00c073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07354.md#insn-00c073ac) · [`00c073d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07354.md#insn-00c073d4)
- 新版 [`00c08380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08348.md#insn-00c08380) · [`00c083a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08348.md#insn-00c083a0) · [`00c083c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08348.md#insn-00c083c8)

~~~diff
- 00c0738c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0738c ["INT_ADD", "register:40f0:8", ["const:c0738c:8", "const:4:8"]]
- 00c0738c ["CALLIND", null, ["register:0:8"]]
+ 00c08380 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08380 ["INT_ADD", "register:40f0:8", ["const:c08380:8", "const:4:8"]]
+ 00c08380 ["CALLIND", null, ["register:0:8"]]
- 00c0738c bytes 00013fd6
+ 00c08380 bytes 00013fd6
- 00c073ac ["INT_ADD", "register:40f0:8", ["const:c073ac:8", "const:4:8"]]
- 00c073ac ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c083a0 ["INT_ADD", "register:40f0:8", ["const:c083a0:8", "const:4:8"]]
+ 00c083a0 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c073ac bytes d14b0194
+ 00c083a0 bytes c84b0194
- 00c073d4 ["INT_ADD", "register:40f0:8", ["const:c073d4:8", "const:4:8"]]
- 00c073d4 ["CALL", null, ["callee:00c5b250:8"]]
+ 00c083c8 ["INT_ADD", "register:40f0:8", ["const:c083c8:8", "const:4:8"]]
+ 00c083c8 ["CALL", null, ["callee:00c5b250:8"]]
- 00c073d4 bytes ab4b0194
+ 00c083c8 bytes a24b0194
~~~


<a id="compare-06b115c459ad201932d5630903a9e5c1"></a>

### [`00c073f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c073f8.md) → [`00c083ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c083ec.md) FUN_00c083ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c073f8.md#insn-00c07460)
- 新版 [`00c08454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c083ec.md#insn-00c08454)

~~~diff
- 00c07460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c07460 ["INT_ADD", "register:40f0:8", ["const:c07460:8", "const:4:8"]]
- 00c07460 ["CALLIND", null, ["register:0:8"]]
+ 00c08454 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08454 ["INT_ADD", "register:40f0:8", ["const:c08454:8", "const:4:8"]]
+ 00c08454 ["CALLIND", null, ["register:0:8"]]
- 00c07460 bytes 00013fd6
+ 00c08454 bytes 00013fd6
~~~


<a id="compare-b55aecd8af1dff157ecd9e2dff5647bc"></a>

### [`00c0749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0749c.md) → [`00c08490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08490.md) FUN_00c08490

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5e5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md) [`00c5f580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c074dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0749c.md#insn-00c074dc) · [`00c07528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0749c.md#insn-00c07528) · [`00c07564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0749c.md#insn-00c07564)
- 新版 [`00c084d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08490.md#insn-00c084d0) · [`00c0851c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08490.md#insn-00c0851c) · [`00c08558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08490.md#insn-00c08558)

~~~diff
- 00c074dc ["INT_ADD", "register:40f0:8", ["const:c074dc:8", "const:4:8"]]
- 00c074dc ["CALL", null, ["callee:00c5f580:8"]]
+ 00c084d0 ["INT_ADD", "register:40f0:8", ["const:c084d0:8", "const:4:8"]]
+ 00c084d0 ["CALL", null, ["callee:00c5f580:8"]]
- 00c074dc bytes 355c0194
+ 00c084d0 bytes 2c5c0194
- 00c07528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c07528 ["INT_ADD", "register:40f0:8", ["const:c07528:8", "const:4:8"]]
- 00c07528 ["CALLIND", null, ["register:0:8"]]
+ 00c0851c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0851c ["INT_ADD", "register:40f0:8", ["const:c0851c:8", "const:4:8"]]
+ 00c0851c ["CALLIND", null, ["register:0:8"]]
- 00c07528 bytes 00013fd6
+ 00c0851c bytes 00013fd6
- 00c07564 ["INT_ADD", "register:40f0:8", ["const:c07564:8", "const:4:8"]]
- 00c07564 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c08558 ["INT_ADD", "register:40f0:8", ["const:c08558:8", "const:4:8"]]
+ 00c08558 ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c07564 bytes 634b0194
+ 00c08558 bytes 5a4b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef1d98ab2753bc03b6af5878a40ab2c"></a>

### [`00c0760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0760c.md) → [`00c08600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08600.md) _ZNSt6__ndk17collateIcED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0760c.md#insn-00c07620)
- 新版 [`00c08614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08600.md#insn-00c08614)

~~~diff
- 00c07620 ["INT_ADD", "register:40f0:8", ["const:c07620:8", "const:4:8"]]
- 00c07620 ["CALL", null, ["callee:00c5f5a0:8"]]
+ 00c08614 ["INT_ADD", "register:40f0:8", ["const:c08614:8", "const:4:8"]]
+ 00c08614 ["CALL", null, ["callee:00c5f5a0:8"]]
- 00c07620 bytes ec5b0194
+ 00c08614 bytes e35b0194
~~~


<a id="compare-c91e2ba2d9f426e91bc7d987cac9dcf6"></a>

### [`00c0769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0769c.md) → [`00c08690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08690.md) _ZNKSt6__ndk17collateIcE12do_transformEPKcS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0769c.md#insn-00c07704) · [`00c0772c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0769c.md#insn-00c0772c) · [`00c07754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0769c.md#insn-00c07754)
- 新版 [`00c086f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08690.md#insn-00c086f8) · [`00c08720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08690.md#insn-00c08720) · [`00c08748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08690.md#insn-00c08748)

~~~diff
- 00c07704 ["INT_ADD", "register:40f0:8", ["const:c07704:8", "const:4:8"]]
- 00c07704 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c086f8 ["INT_ADD", "register:40f0:8", ["const:c086f8:8", "const:4:8"]]
+ 00c086f8 ["CALL", null, ["callee:00c58f30:8"]]
- 00c07704 bytes 17420194
+ 00c086f8 bytes 0e420194
- 00c0772c ["INT_ADD", "register:40f0:8", ["const:c0772c:8", "const:4:8"]]
- 00c0772c ["CALL", null, ["callee:00c590a0:8"]]
+ 00c08720 ["INT_ADD", "register:40f0:8", ["const:c08720:8", "const:4:8"]]
+ 00c08720 ["CALL", null, ["callee:00c590a0:8"]]
- 00c0772c bytes 69420194
+ 00c08720 bytes 60420194
- 00c07754 ["INT_ADD", "register:40f0:8", ["const:c07754:8", "const:4:8"]]
- 00c07754 ["CALL", null, ["callee:0043bac4:8"]]
+ 00c08748 ["INT_ADD", "register:40f0:8", ["const:c08748:8", "const:4:8"]]
+ 00c08748 ["CALL", null, ["callee:0043bac4:8"]]
- 00c07754 bytes 14d0e097
+ 00c08748 bytes dfcce097
~~~


<a id="compare-15a942e5e48e2f33616b1fc7c29c7e6e"></a>

### [`00c07798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07798.md) → [`00c0878c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c0878c.md) _ZNSt6__ndk17collateIwED0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c077ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07798.md#insn-00c077ac)
- 新版 [`00c087a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c0878c.md#insn-00c087a0)

~~~diff
- 00c077ac ["INT_ADD", "register:40f0:8", ["const:c077ac:8", "const:4:8"]]
- 00c077ac ["CALL", null, ["callee:00c5f5b0:8"]]
+ 00c087a0 ["INT_ADD", "register:40f0:8", ["const:c087a0:8", "const:4:8"]]
+ 00c087a0 ["CALL", null, ["callee:00c5f5b0:8"]]
- 00c077ac bytes 8d5b0194
+ 00c087a0 bytes 845b0194
~~~


<a id="compare-456c037ad3ae07fc0286e768fe9d6672"></a>

### [`00c0781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0781c.md) → [`00c08810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08810.md) _ZNKSt6__ndk17collateIwE12do_transformEPKwS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0781c.md#insn-00c07890) · [`00c078c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0781c.md#insn-00c078c4) · [`00c078ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c0781c.md#insn-00c078ec)
- 新版 [`00c08884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08810.md#insn-00c08884) · [`00c088b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08810.md#insn-00c088b8) · [`00c088e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08810.md#insn-00c088e0)

~~~diff
- 00c07890 ["INT_ADD", "register:40f0:8", ["const:c07890:8", "const:4:8"]]
- 00c07890 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c08884 ["INT_ADD", "register:40f0:8", ["const:c08884:8", "const:4:8"]]
+ 00c08884 ["CALL", null, ["callee:00c58f30:8"]]
- 00c07890 bytes b4410194
+ 00c08884 bytes ab410194
- 00c078c4 ["INT_ADD", "register:40f0:8", ["const:c078c4:8", "const:4:8"]]
- 00c078c4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00c088b8 ["INT_ADD", "register:40f0:8", ["const:c088b8:8", "const:4:8"]]
+ 00c088b8 ["CALL", null, ["callee:00c590a0:8"]]
- 00c078c4 bytes 03420194
+ 00c088b8 bytes fa410194
- 00c078ec ["INT_ADD", "register:40f0:8", ["const:c078ec:8", "const:4:8"]]
- 00c078ec ["CALL", null, ["callee:006d7aa8:8"]]
+ 00c088e0 ["INT_ADD", "register:40f0:8", ["const:c088e0:8", "const:4:8"]]
+ 00c088e0 ["CALL", null, ["callee:006d7aa8:8"]]
- 00c078ec bytes 833feb97
+ 00c088e0 bytes 723ceb97
~~~


<a id="compare-4c047d4d599f507b497b5770029979ee"></a>

### [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md) → [`00c08ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md) FUN_00c08ba8

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00c07928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07928.md) [`00c13514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md) [`00c1366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1366c.md) [`00c13728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md) [`00c13878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13878.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)
- 新版 呼出元 7件 [`00c0891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c0891c.md) [`00c14508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14508.md) [`00c14660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14660.md) [`00c1471c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1471c.md) [`00c1486c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1486c.md) · 呼出先 3件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c07c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md#insn-00c07c14) · [`00c07c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md#insn-00c07c20) · [`00c07cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md#insn-00c07cc4)
- 新版 [`00c08c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md#insn-00c08c08) · [`00c08c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md#insn-00c08c14) · [`00c08cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md#insn-00c08cb8)

~~~diff
- 00c07c14 ["INT_ADD", "register:40f0:8", ["const:c07c14:8", "const:4:8"]]
- 00c07c14 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c08c08 ["INT_ADD", "register:40f0:8", ["const:c08c08:8", "const:4:8"]]
+ 00c08c08 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c07c14 bytes 37490194
+ 00c08c08 bytes 2e490194
- 00c07c20 ["INT_ADD", "register:40f0:8", ["const:c07c20:8", "const:4:8"]]
- 00c07c20 ["CALL", null, ["callee:00c5f020:8"]]
+ 00c08c14 ["INT_ADD", "register:40f0:8", ["const:c08c14:8", "const:4:8"]]
+ 00c08c14 ["CALL", null, ["callee:00c5f020:8"]]
- 00c07c20 bytes 0c590194
+ 00c08c14 bytes 03590194
- 00c07cc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c07cc4 ["INT_ADD", "register:40f0:8", ["const:c07cc4:8", "const:4:8"]]
- 00c07cc4 ["CALLIND", null, ["register:0:8"]]
+ 00c08cb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c08cb8 ["INT_ADD", "register:40f0:8", ["const:c08cb8:8", "const:4:8"]]
+ 00c08cb8 ["CALLIND", null, ["register:0:8"]]
- 00c07cc4 bytes 00013fd6
+ 00c08cb8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc4cdae801e76d3b1b92ee100731a0b"></a>

### [`00c08028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md) → [`00c0901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0901c.md) FUN_00c0901c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c08020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08020.md) · 呼出先 6件 [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c09014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09014.md) · 呼出先 6件 [`00c371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c080b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md#insn-00c080b0) · [`00c080cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md#insn-00c080cc) · [`00c08150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md#insn-00c08150)
- 新版 [`00c090a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0901c.md#insn-00c090a4) · [`00c090c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0901c.md#insn-00c090c0) · [`00c09144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0901c.md#insn-00c09144)

~~~diff
- 00c080b0 ["INT_ADD", "register:40f0:8", ["const:c080b0:8", "const:4:8"]]
- 00c080b0 ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c090a4 ["INT_ADD", "register:40f0:8", ["const:c090a4:8", "const:4:8"]]
+ 00c090a4 ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c080b0 bytes 50590194
+ 00c090a4 bytes 47590194
- 00c080cc ["INT_ADD", "register:40f0:8", ["const:c080cc:8", "const:4:8"]]
- 00c080cc ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c090c0 ["INT_ADD", "register:40f0:8", ["const:c090c0:8", "const:4:8"]]
+ 00c090c0 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c080cc bytes 9d4f0194
+ 00c090c0 bytes 944f0194
- 00c08150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c08150 ["INT_ADD", "register:40f0:8", ["const:c08150:8", "const:4:8"]]
- 00c08150 ["CALLIND", null, ["register:0:8"]]
+ 00c09144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09144 ["INT_ADD", "register:40f0:8", ["const:c09144:8", "const:4:8"]]
+ 00c09144 ["CALLIND", null, ["register:0:8"]]
- 00c08150 bytes 00013fd6
+ 00c09144 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8add1f92290a20538ed2707f8cc2ee04"></a>

### [`00c08464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md) → [`00c09458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09458.md) FUN_00c09458

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0845c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c0845c.md) · 呼出先 6件 [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c09450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09450.md) · 呼出先 6件 [`00c37324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c084ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md#insn-00c084ec) · [`00c08508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md#insn-00c08508) · [`00c0858c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md#insn-00c0858c)
- 新版 [`00c094e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09458.md#insn-00c094e0) · [`00c094fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09458.md#insn-00c094fc) · [`00c09580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09458.md#insn-00c09580)

~~~diff
- 00c084ec ["INT_ADD", "register:40f0:8", ["const:c084ec:8", "const:4:8"]]
- 00c084ec ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c094e0 ["INT_ADD", "register:40f0:8", ["const:c094e0:8", "const:4:8"]]
+ 00c094e0 ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c084ec bytes 41580194
+ 00c094e0 bytes 38580194
- 00c08508 ["INT_ADD", "register:40f0:8", ["const:c08508:8", "const:4:8"]]
- 00c08508 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c094fc ["INT_ADD", "register:40f0:8", ["const:c094fc:8", "const:4:8"]]
+ 00c094fc ["CALL", null, ["callee:00c5cf10:8"]]
- 00c08508 bytes 8e4e0194
+ 00c094fc bytes 854e0194
- 00c0858c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0858c ["INT_ADD", "register:40f0:8", ["const:c0858c:8", "const:4:8"]]
- 00c0858c ["CALLIND", null, ["register:0:8"]]
+ 00c09580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09580 ["INT_ADD", "register:40f0:8", ["const:c09580:8", "const:4:8"]]
+ 00c09580 ["CALLIND", null, ["register:0:8"]]
- 00c0858c bytes 00013fd6
+ 00c09580 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99d97f51614ed5fc8dd58aced9e19444"></a>

### [`00c088a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md) → [`00c09894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09894.md) FUN_00c09894

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c08898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08898.md) · 呼出先 6件 [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c0988c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0988c.md) · 呼出先 6件 [`00c3744c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c08928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md#insn-00c08928) · [`00c08944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md#insn-00c08944) · [`00c089c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md#insn-00c089c8)
- 新版 [`00c0991c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09894.md#insn-00c0991c) · [`00c09938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09894.md#insn-00c09938) · [`00c099bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09894.md#insn-00c099bc)

~~~diff
- 00c08928 ["INT_ADD", "register:40f0:8", ["const:c08928:8", "const:4:8"]]
- 00c08928 ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c0991c ["INT_ADD", "register:40f0:8", ["const:c0991c:8", "const:4:8"]]
+ 00c0991c ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c08928 bytes 32570194
+ 00c0991c bytes 29570194
- 00c08944 ["INT_ADD", "register:40f0:8", ["const:c08944:8", "const:4:8"]]
- 00c08944 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c09938 ["INT_ADD", "register:40f0:8", ["const:c09938:8", "const:4:8"]]
+ 00c09938 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c08944 bytes 7f4d0194
+ 00c09938 bytes 764d0194
- 00c089c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c089c8 ["INT_ADD", "register:40f0:8", ["const:c089c8:8", "const:4:8"]]
- 00c089c8 ["CALLIND", null, ["register:0:8"]]
+ 00c099bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c099bc ["INT_ADD", "register:40f0:8", ["const:c099bc:8", "const:4:8"]]
+ 00c099bc ["CALLIND", null, ["register:0:8"]]
- 00c089c8 bytes 00013fd6
+ 00c099bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d182b4d4f6663ab3466a13ff26da423"></a>

### [`00c08cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md) → [`00c09cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cd0.md) FUN_00c09cd0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c08cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cd4.md) · 呼出先 6件 [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c09cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cc8.md) · 呼出先 6件 [`00c375a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c08d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md#insn-00c08d64) · [`00c08d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md#insn-00c08d80) · [`00c08e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md#insn-00c08e04)
- 新版 [`00c09d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cd0.md#insn-00c09d58) · [`00c09d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cd0.md#insn-00c09d74) · [`00c09df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cd0.md#insn-00c09df8)

~~~diff
- 00c08d64 ["INT_ADD", "register:40f0:8", ["const:c08d64:8", "const:4:8"]]
- 00c08d64 ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c09d58 ["INT_ADD", "register:40f0:8", ["const:c09d58:8", "const:4:8"]]
+ 00c09d58 ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c08d64 bytes 23560194
+ 00c09d58 bytes 1a560194
- 00c08d80 ["INT_ADD", "register:40f0:8", ["const:c08d80:8", "const:4:8"]]
- 00c08d80 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c09d74 ["INT_ADD", "register:40f0:8", ["const:c09d74:8", "const:4:8"]]
+ 00c09d74 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c08d80 bytes 704c0194
+ 00c09d74 bytes 674c0194
- 00c08e04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c08e04 ["INT_ADD", "register:40f0:8", ["const:c08e04:8", "const:4:8"]]
- 00c08e04 ["CALLIND", null, ["register:0:8"]]
+ 00c09df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c09df8 ["INT_ADD", "register:40f0:8", ["const:c09df8:8", "const:4:8"]]
+ 00c09df8 ["CALLIND", null, ["register:0:8"]]
- 00c08e04 bytes 00013fd6
+ 00c09df8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8171d8c91c05018c13e8c9f5051b832e"></a>

### [`00c09118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md) → [`00c0a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a10c.md) FUN_00c0a10c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c09110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09110.md) · 呼出先 6件 [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c0a104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a104.md) · 呼出先 6件 [`00c376f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c091a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md#insn-00c091a0) · [`00c091bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md#insn-00c091bc) · [`00c09240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md#insn-00c09240)
- 新版 [`00c0a194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a10c.md#insn-00c0a194) · [`00c0a1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a10c.md#insn-00c0a1b0) · [`00c0a234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a10c.md#insn-00c0a234)

~~~diff
- 00c091a0 ["INT_ADD", "register:40f0:8", ["const:c091a0:8", "const:4:8"]]
- 00c091a0 ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c0a194 ["INT_ADD", "register:40f0:8", ["const:c0a194:8", "const:4:8"]]
+ 00c0a194 ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c091a0 bytes 14550194
+ 00c0a194 bytes 0b550194
- 00c091bc ["INT_ADD", "register:40f0:8", ["const:c091bc:8", "const:4:8"]]
- 00c091bc ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0a1b0 ["INT_ADD", "register:40f0:8", ["const:c0a1b0:8", "const:4:8"]]
+ 00c0a1b0 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c091bc bytes 614b0194
+ 00c0a1b0 bytes 584b0194
- 00c09240 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c09240 ["INT_ADD", "register:40f0:8", ["const:c09240:8", "const:4:8"]]
- 00c09240 ["CALLIND", null, ["register:0:8"]]
+ 00c0a234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0a234 ["INT_ADD", "register:40f0:8", ["const:c0a234:8", "const:4:8"]]
+ 00c0a234 ["CALLIND", null, ["register:0:8"]]
- 00c09240 bytes 00013fd6
+ 00c0a234 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4ca4ca453218669c1a0bd92ce6490e"></a>

### [`00c09554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md) → [`00c0a548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a548.md) FUN_00c0a548

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c0954c.md) · 呼出先 6件 [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e5f0.md) [`00c5e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e600.md)
- 新版 呼出元 1件 [`00c0a540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a540.md) · 呼出先 6件 [`00c37840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5c0.md) [`00c5f5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c095dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md#insn-00c095dc) · [`00c095f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md#insn-00c095f8) · [`00c0967c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md#insn-00c0967c)
- 新版 [`00c0a5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a548.md#insn-00c0a5d0) · [`00c0a5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a548.md#insn-00c0a5ec) · [`00c0a670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a548.md#insn-00c0a670)

~~~diff
- 00c095dc ["INT_ADD", "register:40f0:8", ["const:c095dc:8", "const:4:8"]]
- 00c095dc ["CALL", null, ["callee:00c5f5c0:8"]]
+ 00c0a5d0 ["INT_ADD", "register:40f0:8", ["const:c0a5d0:8", "const:4:8"]]
+ 00c0a5d0 ["CALL", null, ["callee:00c5f5c0:8"]]
- 00c095dc bytes 05540194
+ 00c0a5d0 bytes fc530194
- 00c095f8 ["INT_ADD", "register:40f0:8", ["const:c095f8:8", "const:4:8"]]
- 00c095f8 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0a5ec ["INT_ADD", "register:40f0:8", ["const:c0a5ec:8", "const:4:8"]]
+ 00c0a5ec ["CALL", null, ["callee:00c5cf10:8"]]
- 00c095f8 bytes 524a0194
+ 00c0a5ec bytes 494a0194
- 00c0967c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0967c ["INT_ADD", "register:40f0:8", ["const:c0967c:8", "const:4:8"]]
- 00c0967c ["CALLIND", null, ["register:0:8"]]
+ 00c0a670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0a670 ["INT_ADD", "register:40f0:8", ["const:c0a670:8", "const:4:8"]]
+ 00c0a670 ["CALLIND", null, ["register:0:8"]]
- 00c0967c bytes 00013fd6
+ 00c0a670 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5826461e902e20b8ffdae472dadafa06"></a>

### [`00c09990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md) → [`00c0a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a984.md) FUN_00c0a984

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c09988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09988.md) · 呼出先 6件 [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)
- 新版 呼出元 1件 [`00c0a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a97c.md) · 呼出先 6件 [`00c37988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c099dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md#insn-00c099dc) · [`00c099f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md#insn-00c099f8) · [`00c09a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md#insn-00c09a88)
- 新版 [`00c0a9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a984.md#insn-00c0a9d0) · [`00c0a9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a984.md#insn-00c0a9ec) · [`00c0aa7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a984.md#insn-00c0aa7c)

~~~diff
- 00c099dc ["INT_ADD", "register:40f0:8", ["const:c099dc:8", "const:4:8"]]
- 00c099dc ["CALL", null, ["callee:00c5f5f0:8"]]
+ 00c0a9d0 ["INT_ADD", "register:40f0:8", ["const:c0a9d0:8", "const:4:8"]]
+ 00c0a9d0 ["CALL", null, ["callee:00c5f5f0:8"]]
- 00c099dc bytes 11530194
+ 00c0a9d0 bytes 08530194
- 00c099f8 ["INT_ADD", "register:40f0:8", ["const:c099f8:8", "const:4:8"]]
- 00c099f8 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0a9ec ["INT_ADD", "register:40f0:8", ["const:c0a9ec:8", "const:4:8"]]
+ 00c0a9ec ["CALL", null, ["callee:00c5cf10:8"]]
- 00c099f8 bytes 52490194
+ 00c0a9ec bytes 49490194
- 00c09a88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c09a88 ["INT_ADD", "register:40f0:8", ["const:c09a88:8", "const:4:8"]]
- 00c09a88 ["CALLIND", null, ["register:0:8"]]
+ 00c0aa7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0aa7c ["INT_ADD", "register:40f0:8", ["const:c0aa7c:8", "const:4:8"]]
+ 00c0aa7c ["CALLIND", null, ["register:0:8"]]
- 00c09a88 bytes 00013fd6
+ 00c0aa7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6cec51c819ae83cd383378f72f4803c"></a>

### [`00c09da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md) → [`00c0ad9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad9c.md) FUN_00c0ad9c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c09da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da0.md) · 呼出先 6件 [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)
- 新版 呼出元 1件 [`00c0ad94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad94.md) · 呼出先 6件 [`00c37aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c09df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md#insn-00c09df4) · [`00c09e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md#insn-00c09e10) · [`00c09ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md#insn-00c09ea0)
- 新版 [`00c0ade8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad9c.md#insn-00c0ade8) · [`00c0ae04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad9c.md#insn-00c0ae04) · [`00c0ae94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad9c.md#insn-00c0ae94)

~~~diff
- 00c09df4 ["INT_ADD", "register:40f0:8", ["const:c09df4:8", "const:4:8"]]
- 00c09df4 ["CALL", null, ["callee:00c5f5f0:8"]]
+ 00c0ade8 ["INT_ADD", "register:40f0:8", ["const:c0ade8:8", "const:4:8"]]
+ 00c0ade8 ["CALL", null, ["callee:00c5f5f0:8"]]
- 00c09df4 bytes 0b520194
+ 00c0ade8 bytes 02520194
- 00c09e10 ["INT_ADD", "register:40f0:8", ["const:c09e10:8", "const:4:8"]]
- 00c09e10 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0ae04 ["INT_ADD", "register:40f0:8", ["const:c0ae04:8", "const:4:8"]]
+ 00c0ae04 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c09e10 bytes 4c480194
+ 00c0ae04 bytes 43480194
- 00c09ea0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c09ea0 ["INT_ADD", "register:40f0:8", ["const:c09ea0:8", "const:4:8"]]
- 00c09ea0 ["CALLIND", null, ["register:0:8"]]
+ 00c0ae94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0ae94 ["INT_ADD", "register:40f0:8", ["const:c0ae94:8", "const:4:8"]]
+ 00c0ae94 ["CALLIND", null, ["register:0:8"]]
- 00c09ea0 bytes 00013fd6
+ 00c0ae94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8e45f32e1187da22361772bf64e85c1"></a>

### [`00c0a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md) → [`00c0b1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1b4.md) FUN_00c0b1b4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1b8.md) · 呼出先 6件 [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e620.md)
- 新版 呼出元 1件 [`00c0b1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1ac.md) · 呼出先 6件 [`00c37bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0a20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md#insn-00c0a20c) · [`00c0a228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md#insn-00c0a228) · [`00c0a2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md#insn-00c0a2b8)
- 新版 [`00c0b200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1b4.md#insn-00c0b200) · [`00c0b21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1b4.md#insn-00c0b21c) · [`00c0b2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1b4.md#insn-00c0b2ac)

~~~diff
- 00c0a20c ["INT_ADD", "register:40f0:8", ["const:c0a20c:8", "const:4:8"]]
- 00c0a20c ["CALL", null, ["callee:00c5f5f0:8"]]
+ 00c0b200 ["INT_ADD", "register:40f0:8", ["const:c0b200:8", "const:4:8"]]
+ 00c0b200 ["CALL", null, ["callee:00c5f5f0:8"]]
- 00c0a20c bytes 05510194
+ 00c0b200 bytes fc500194
- 00c0a228 ["INT_ADD", "register:40f0:8", ["const:c0a228:8", "const:4:8"]]
- 00c0a228 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0b21c ["INT_ADD", "register:40f0:8", ["const:c0b21c:8", "const:4:8"]]
+ 00c0b21c ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0a228 bytes 46470194
+ 00c0b21c bytes 3d470194
- 00c0a2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0a2b8 ["INT_ADD", "register:40f0:8", ["const:c0a2b8:8", "const:4:8"]]
- 00c0a2b8 ["CALLIND", null, ["register:0:8"]]
+ 00c0b2ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0b2ac ["INT_ADD", "register:40f0:8", ["const:c0b2ac:8", "const:4:8"]]
+ 00c0b2ac ["CALLIND", null, ["register:0:8"]]
- 00c0a2b8 bytes 00013fd6
+ 00c0b2ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdde92d2ff1d73aa14a85455489bdb9c"></a>

### [`00c0acc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0acc4.md) → [`00c0bcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bcb8.md) FUN_00c0bcb8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00c0a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a5d0.md) [`00c0da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0da44.md) · 呼出先 2件 [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e650.md)
- 新版 呼出元 2件 [`00c0b5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b5c4.md) [`00c0ea38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0ea38.md) · 呼出先 2件 [`00c5f610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f610.md) [`00c5f620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0ad28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0acc4.md#insn-00c0ad28) · [`00c0ad44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0acc4.md#insn-00c0ad44) · [`00c0ad54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0acc4.md#insn-00c0ad54)
- 新版 [`00c0bd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bcb8.md#insn-00c0bd1c) · [`00c0bd38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bcb8.md#insn-00c0bd38) · [`00c0bd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bcb8.md#insn-00c0bd48)

~~~diff
- 00c0ad28 ["INT_ADD", "register:40f0:8", ["const:c0ad28:8", "const:4:8"]]
- 00c0ad28 ["CALL", null, ["callee:00c5f610:8"]]
+ 00c0bd1c ["INT_ADD", "register:40f0:8", ["const:c0bd1c:8", "const:4:8"]]
+ 00c0bd1c ["CALL", null, ["callee:00c5f610:8"]]
- 00c0ad28 bytes 464e0194
+ 00c0bd1c bytes 3d4e0194
- 00c0ad44 ["INT_ADD", "register:40f0:8", ["const:c0ad44:8", "const:4:8"]]
- 00c0ad44 ["CALL", null, ["callee:00c5f620:8"]]
+ 00c0bd38 ["INT_ADD", "register:40f0:8", ["const:c0bd38:8", "const:4:8"]]
+ 00c0bd38 ["CALL", null, ["callee:00c5f620:8"]]
- 00c0ad44 bytes 434e0194
+ 00c0bd38 bytes 3a4e0194
- 00c0ad54 ["INT_ADD", "register:40f0:8", ["const:c0ad54:8", "const:4:8"]]
- 00c0ad54 ["CALL", null, ["callee:00c5f610:8"]]
+ 00c0bd48 ["INT_ADD", "register:40f0:8", ["const:c0bd48:8", "const:4:8"]]
+ 00c0bd48 ["CALL", null, ["callee:00c5f610:8"]]
- 00c0ad54 bytes 3b4e0194
+ 00c0bd48 bytes 324e0194
~~~


<a id="compare-a3f3e98a43909bca9d8fca407a1b57d2"></a>

### [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md) → [`00c0c080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md) FUN_00c0c080

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00c0ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0ae00.md) [`00c1525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md) [`00c153b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c153b4.md) [`00c15470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md) [`00c155c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c155c0.md) · 呼出先 3件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5e050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e050.md)
- 新版 呼出元 7件 [`00c0bdf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bdf4.md) [`00c16250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16250.md) [`00c163a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c163a8.md) [`00c16464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16464.md) [`00c165b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c165b4.md) · 呼出先 3件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md#insn-00c0b0ec) · [`00c0b0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md#insn-00c0b0f8) · [`00c0b194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md#insn-00c0b194)
- 新版 [`00c0c0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md#insn-00c0c0e0) · [`00c0c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md#insn-00c0c0ec) · [`00c0c188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md#insn-00c0c188)

~~~diff
- 00c0b0ec ["INT_ADD", "register:40f0:8", ["const:c0b0ec:8", "const:4:8"]]
- 00c0b0ec ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c0c0e0 ["INT_ADD", "register:40f0:8", ["const:c0c0e0:8", "const:4:8"]]
+ 00c0c0e0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c0b0ec bytes 013c0194
+ 00c0c0e0 bytes f83b0194
- 00c0b0f8 ["INT_ADD", "register:40f0:8", ["const:c0b0f8:8", "const:4:8"]]
- 00c0b0f8 ["CALL", null, ["callee:00c5f020:8"]]
+ 00c0c0ec ["INT_ADD", "register:40f0:8", ["const:c0c0ec:8", "const:4:8"]]
+ 00c0c0ec ["CALL", null, ["callee:00c5f020:8"]]
- 00c0b0f8 bytes d64b0194
+ 00c0c0ec bytes cd4b0194
- 00c0b194 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0b194 ["INT_ADD", "register:40f0:8", ["const:c0b194:8", "const:4:8"]]
- 00c0b194 ["CALLIND", null, ["register:0:8"]]
+ 00c0c188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0c188 ["INT_ADD", "register:40f0:8", ["const:c0c188:8", "const:4:8"]]
+ 00c0c188 ["CALLIND", null, ["register:0:8"]]
- 00c0b194 bytes 00013fd6
+ 00c0c188 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d62db213182a8d789aa7147c9bfceef6"></a>

### [`00c0b508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md) → [`00c0c4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4fc.md) FUN_00c0c4fc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b500.md) · 呼出先 6件 [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0c4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4f4.md) · 呼出先 6件 [`00c371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md#insn-00c0b590) · [`00c0b5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md#insn-00c0b5ac) · [`00c0b61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md#insn-00c0b61c)
- 新版 [`00c0c584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4fc.md#insn-00c0c584) · [`00c0c5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4fc.md#insn-00c0c5a0) · [`00c0c610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4fc.md#insn-00c0c610)

~~~diff
- 00c0b590 ["INT_ADD", "register:40f0:8", ["const:c0b590:8", "const:4:8"]]
- 00c0b590 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0c584 ["INT_ADD", "register:40f0:8", ["const:c0c584:8", "const:4:8"]]
+ 00c0c584 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0b590 bytes 344c0194
+ 00c0c584 bytes 2b4c0194
- 00c0b5ac ["INT_ADD", "register:40f0:8", ["const:c0b5ac:8", "const:4:8"]]
- 00c0b5ac ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0c5a0 ["INT_ADD", "register:40f0:8", ["const:c0c5a0:8", "const:4:8"]]
+ 00c0c5a0 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0b5ac bytes 65420194
+ 00c0c5a0 bytes 5c420194
- 00c0b61c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0b61c ["INT_ADD", "register:40f0:8", ["const:c0b61c:8", "const:4:8"]]
- 00c0b61c ["CALLIND", null, ["register:0:8"]]
+ 00c0c610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0c610 ["INT_ADD", "register:40f0:8", ["const:c0c610:8", "const:4:8"]]
+ 00c0c610 ["CALLIND", null, ["register:0:8"]]
- 00c0b61c bytes 00013fd6
+ 00c0c610 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef2fde413966ca97e770d019eb33707"></a>

### [`00c0b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md) → [`00c0c92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c92c.md) FUN_00c0c92c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0b930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b930.md) · 呼出先 6件 [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0c924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c924.md) · 呼出先 6件 [`00c37324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0b9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md#insn-00c0b9c0) · [`00c0b9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md#insn-00c0b9dc) · [`00c0ba4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md#insn-00c0ba4c)
- 新版 [`00c0c9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c92c.md#insn-00c0c9b4) · [`00c0c9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c92c.md#insn-00c0c9d0) · [`00c0ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c92c.md#insn-00c0ca40)

~~~diff
- 00c0b9c0 ["INT_ADD", "register:40f0:8", ["const:c0b9c0:8", "const:4:8"]]
- 00c0b9c0 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0c9b4 ["INT_ADD", "register:40f0:8", ["const:c0c9b4:8", "const:4:8"]]
+ 00c0c9b4 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0b9c0 bytes 284b0194
+ 00c0c9b4 bytes 1f4b0194
- 00c0b9dc ["INT_ADD", "register:40f0:8", ["const:c0b9dc:8", "const:4:8"]]
- 00c0b9dc ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0c9d0 ["INT_ADD", "register:40f0:8", ["const:c0c9d0:8", "const:4:8"]]
+ 00c0c9d0 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0b9dc bytes 59410194
+ 00c0c9d0 bytes 50410194
- 00c0ba4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0ba4c ["INT_ADD", "register:40f0:8", ["const:c0ba4c:8", "const:4:8"]]
- 00c0ba4c ["CALLIND", null, ["register:0:8"]]
+ 00c0ca40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0ca40 ["INT_ADD", "register:40f0:8", ["const:c0ca40:8", "const:4:8"]]
+ 00c0ca40 ["CALLIND", null, ["register:0:8"]]
- 00c0ba4c bytes 00013fd6
+ 00c0ca40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3210b201029233216f3a86af3a32540e"></a>

### [`00c0bd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md) → [`00c0cd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd5c.md) FUN_00c0cd5c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0bd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd60.md) · 呼出先 6件 [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0cd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd54.md) · 呼出先 6件 [`00c3744c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0bdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md#insn-00c0bdf0) · [`00c0be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md#insn-00c0be0c) · [`00c0be7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md#insn-00c0be7c)
- 新版 [`00c0cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd5c.md#insn-00c0cde4) · [`00c0ce00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd5c.md#insn-00c0ce00) · [`00c0ce70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd5c.md#insn-00c0ce70)

~~~diff
- 00c0bdf0 ["INT_ADD", "register:40f0:8", ["const:c0bdf0:8", "const:4:8"]]
- 00c0bdf0 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0cde4 ["INT_ADD", "register:40f0:8", ["const:c0cde4:8", "const:4:8"]]
+ 00c0cde4 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0bdf0 bytes 1c4a0194
+ 00c0cde4 bytes 134a0194
- 00c0be0c ["INT_ADD", "register:40f0:8", ["const:c0be0c:8", "const:4:8"]]
- 00c0be0c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0ce00 ["INT_ADD", "register:40f0:8", ["const:c0ce00:8", "const:4:8"]]
+ 00c0ce00 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0be0c bytes 4d400194
+ 00c0ce00 bytes 44400194
- 00c0be7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0be7c ["INT_ADD", "register:40f0:8", ["const:c0be7c:8", "const:4:8"]]
- 00c0be7c ["CALLIND", null, ["register:0:8"]]
+ 00c0ce70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0ce70 ["INT_ADD", "register:40f0:8", ["const:c0ce70:8", "const:4:8"]]
+ 00c0ce70 ["CALLIND", null, ["register:0:8"]]
- 00c0be7c bytes 00013fd6
+ 00c0ce70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6721637fceee568ec075de49ab5a4d7e"></a>

### [`00c0c198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md) → [`00c0d18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d18c.md) FUN_00c0d18c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c190.md) · 呼出先 6件 [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0d184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d184.md) · 呼出先 6件 [`00c375a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md#insn-00c0c220) · [`00c0c23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md#insn-00c0c23c) · [`00c0c2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md#insn-00c0c2ac)
- 新版 [`00c0d214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d18c.md#insn-00c0d214) · [`00c0d230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d18c.md#insn-00c0d230) · [`00c0d2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d18c.md#insn-00c0d2a0)

~~~diff
- 00c0c220 ["INT_ADD", "register:40f0:8", ["const:c0c220:8", "const:4:8"]]
- 00c0c220 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0d214 ["INT_ADD", "register:40f0:8", ["const:c0d214:8", "const:4:8"]]
+ 00c0d214 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0c220 bytes 10490194
+ 00c0d214 bytes 07490194
- 00c0c23c ["INT_ADD", "register:40f0:8", ["const:c0c23c:8", "const:4:8"]]
- 00c0c23c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0d230 ["INT_ADD", "register:40f0:8", ["const:c0d230:8", "const:4:8"]]
+ 00c0d230 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0c23c bytes 413f0194
+ 00c0d230 bytes 383f0194
- 00c0c2ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0c2ac ["INT_ADD", "register:40f0:8", ["const:c0c2ac:8", "const:4:8"]]
- 00c0c2ac ["CALLIND", null, ["register:0:8"]]
+ 00c0d2a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0d2a0 ["INT_ADD", "register:40f0:8", ["const:c0d2a0:8", "const:4:8"]]
+ 00c0d2a0 ["CALLIND", null, ["register:0:8"]]
- 00c0c2ac bytes 00013fd6
+ 00c0d2a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf7360953709e7373479249fd0ded46"></a>

### [`00c0c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md) → [`00c0d5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5bc.md) FUN_00c0d5bc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c0.md) · 呼出先 6件 [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0d5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5b4.md) · 呼出先 6件 [`00c376f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0c650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md#insn-00c0c650) · [`00c0c66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md#insn-00c0c66c) · [`00c0c6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md#insn-00c0c6dc)
- 新版 [`00c0d644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5bc.md#insn-00c0d644) · [`00c0d660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5bc.md#insn-00c0d660) · [`00c0d6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5bc.md#insn-00c0d6d0)

~~~diff
- 00c0c650 ["INT_ADD", "register:40f0:8", ["const:c0c650:8", "const:4:8"]]
- 00c0c650 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0d644 ["INT_ADD", "register:40f0:8", ["const:c0d644:8", "const:4:8"]]
+ 00c0d644 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0c650 bytes 04480194
+ 00c0d644 bytes fb470194
- 00c0c66c ["INT_ADD", "register:40f0:8", ["const:c0c66c:8", "const:4:8"]]
- 00c0c66c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0d660 ["INT_ADD", "register:40f0:8", ["const:c0d660:8", "const:4:8"]]
+ 00c0d660 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0c66c bytes 353e0194
+ 00c0d660 bytes 2c3e0194
- 00c0c6dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0c6dc ["INT_ADD", "register:40f0:8", ["const:c0c6dc:8", "const:4:8"]]
- 00c0c6dc ["CALLIND", null, ["register:0:8"]]
+ 00c0d6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0d6d0 ["INT_ADD", "register:40f0:8", ["const:c0d6d0:8", "const:4:8"]]
+ 00c0d6d0 ["CALLIND", null, ["register:0:8"]]
- 00c0c6dc bytes 00013fd6
+ 00c0d6d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ca339a64bd9fee0a777acf9872db09"></a>

### [`00c0c9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md) → [`00c0d9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9ec.md) FUN_00c0d9ec

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0c9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f0.md) · 呼出先 6件 [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e660.md)
- 新版 呼出元 1件 [`00c0d9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9e4.md) · 呼出先 6件 [`00c37840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f630.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0ca80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md#insn-00c0ca80) · [`00c0ca9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md#insn-00c0ca9c) · [`00c0cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md#insn-00c0cb0c)
- 新版 [`00c0da74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9ec.md#insn-00c0da74) · [`00c0da90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9ec.md#insn-00c0da90) · [`00c0db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9ec.md#insn-00c0db00)

~~~diff
- 00c0ca80 ["INT_ADD", "register:40f0:8", ["const:c0ca80:8", "const:4:8"]]
- 00c0ca80 ["CALL", null, ["callee:00c5f630:8"]]
+ 00c0da74 ["INT_ADD", "register:40f0:8", ["const:c0da74:8", "const:4:8"]]
+ 00c0da74 ["CALL", null, ["callee:00c5f630:8"]]
- 00c0ca80 bytes f8460194
+ 00c0da74 bytes ef460194
- 00c0ca9c ["INT_ADD", "register:40f0:8", ["const:c0ca9c:8", "const:4:8"]]
- 00c0ca9c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0da90 ["INT_ADD", "register:40f0:8", ["const:c0da90:8", "const:4:8"]]
+ 00c0da90 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0ca9c bytes 293d0194
+ 00c0da90 bytes 203d0194
- 00c0cb0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0cb0c ["INT_ADD", "register:40f0:8", ["const:c0cb0c:8", "const:4:8"]]
- 00c0cb0c ["CALLIND", null, ["register:0:8"]]
+ 00c0db00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0db00 ["INT_ADD", "register:40f0:8", ["const:c0db00:8", "const:4:8"]]
+ 00c0db00 ["CALLIND", null, ["register:0:8"]]
- 00c0cb0c bytes 00013fd6
+ 00c0db00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfda0fb5dc66e3c50c50b3598c7eb947"></a>

### [`00c0ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md) → [`00c0de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de1c.md) FUN_00c0de1c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0ce20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce20.md) · 呼出先 6件 [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)
- 新版 呼出元 1件 [`00c0de14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de14.md) · 呼出先 6件 [`00c37988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0ce74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md#insn-00c0ce74) · [`00c0ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md#insn-00c0ce90) · [`00c0cf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md#insn-00c0cf10)
- 新版 [`00c0de68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de1c.md#insn-00c0de68) · [`00c0de84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de1c.md#insn-00c0de84) · [`00c0df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de1c.md#insn-00c0df04)

~~~diff
- 00c0ce74 ["INT_ADD", "register:40f0:8", ["const:c0ce74:8", "const:4:8"]]
- 00c0ce74 ["CALL", null, ["callee:00c5f650:8"]]
+ 00c0de68 ["INT_ADD", "register:40f0:8", ["const:c0de68:8", "const:4:8"]]
+ 00c0de68 ["CALL", null, ["callee:00c5f650:8"]]
- 00c0ce74 bytes 03460194
+ 00c0de68 bytes fa450194
- 00c0ce90 ["INT_ADD", "register:40f0:8", ["const:c0ce90:8", "const:4:8"]]
- 00c0ce90 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0de84 ["INT_ADD", "register:40f0:8", ["const:c0de84:8", "const:4:8"]]
+ 00c0de84 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0ce90 bytes 2c3c0194
+ 00c0de84 bytes 233c0194
- 00c0cf10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0cf10 ["INT_ADD", "register:40f0:8", ["const:c0cf10:8", "const:4:8"]]
- 00c0cf10 ["CALLIND", null, ["register:0:8"]]
+ 00c0df04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0df04 ["INT_ADD", "register:40f0:8", ["const:c0df04:8", "const:4:8"]]
+ 00c0df04 ["CALLIND", null, ["register:0:8"]]
- 00c0cf10 bytes 00013fd6
+ 00c0df04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41e81a0db826799948a8971ee6e7f512"></a>

### [`00c0d234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md) → [`00c0e228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e228.md) FUN_00c0e228

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d22c.md) · 呼出先 6件 [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)
- 新版 呼出元 1件 [`00c0e220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e220.md) · 呼出先 6件 [`00c37aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md#insn-00c0d280) · [`00c0d29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md#insn-00c0d29c) · [`00c0d31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md#insn-00c0d31c)
- 新版 [`00c0e274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e228.md#insn-00c0e274) · [`00c0e290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e228.md#insn-00c0e290) · [`00c0e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e228.md#insn-00c0e310)

~~~diff
- 00c0d280 ["INT_ADD", "register:40f0:8", ["const:c0d280:8", "const:4:8"]]
- 00c0d280 ["CALL", null, ["callee:00c5f650:8"]]
+ 00c0e274 ["INT_ADD", "register:40f0:8", ["const:c0e274:8", "const:4:8"]]
+ 00c0e274 ["CALL", null, ["callee:00c5f650:8"]]
- 00c0d280 bytes 00450194
+ 00c0e274 bytes f7440194
- 00c0d29c ["INT_ADD", "register:40f0:8", ["const:c0d29c:8", "const:4:8"]]
- 00c0d29c ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0e290 ["INT_ADD", "register:40f0:8", ["const:c0e290:8", "const:4:8"]]
+ 00c0e290 ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0d29c bytes 293b0194
+ 00c0e290 bytes 203b0194
- 00c0d31c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0d31c ["INT_ADD", "register:40f0:8", ["const:c0d31c:8", "const:4:8"]]
- 00c0d31c ["CALLIND", null, ["register:0:8"]]
+ 00c0e310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0e310 ["INT_ADD", "register:40f0:8", ["const:c0e310:8", "const:4:8"]]
+ 00c0e310 ["CALLIND", null, ["register:0:8"]]
- 00c0d31c bytes 00013fd6
+ 00c0e310 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19eb270c89d0a4fd4e1c76599acd6893"></a>

### [`00c0d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md) → [`00c0e634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e634.md) FUN_00c0e634

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c0d638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d638.md) · 呼出先 6件 [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md) [`00c5e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e610.md) [`00c5e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e680.md)
- 新版 呼出元 1件 [`00c0e62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e62c.md) · 呼出先 6件 [`00c37bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf10.md) [`00c5f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f5e0.md) [`00c5f650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c0d68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md#insn-00c0d68c) · [`00c0d6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md#insn-00c0d6a8) · [`00c0d728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md#insn-00c0d728)
- 新版 [`00c0e680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e634.md#insn-00c0e680) · [`00c0e69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e634.md#insn-00c0e69c) · [`00c0e71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e634.md#insn-00c0e71c)

~~~diff
- 00c0d68c ["INT_ADD", "register:40f0:8", ["const:c0d68c:8", "const:4:8"]]
- 00c0d68c ["CALL", null, ["callee:00c5f650:8"]]
+ 00c0e680 ["INT_ADD", "register:40f0:8", ["const:c0e680:8", "const:4:8"]]
+ 00c0e680 ["CALL", null, ["callee:00c5f650:8"]]
- 00c0d68c bytes fd430194
+ 00c0e680 bytes f4430194
- 00c0d6a8 ["INT_ADD", "register:40f0:8", ["const:c0d6a8:8", "const:4:8"]]
- 00c0d6a8 ["CALL", null, ["callee:00c5cf10:8"]]
+ 00c0e69c ["INT_ADD", "register:40f0:8", ["const:c0e69c:8", "const:4:8"]]
+ 00c0e69c ["CALL", null, ["callee:00c5cf10:8"]]
- 00c0d6a8 bytes 263a0194
+ 00c0e69c bytes 1d3a0194
- 00c0d728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c0d728 ["INT_ADD", "register:40f0:8", ["const:c0d728:8", "const:4:8"]]
- 00c0d728 ["CALLIND", null, ["register:0:8"]]
+ 00c0e71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0e71c ["INT_ADD", "register:40f0:8", ["const:c0e71c:8", "const:4:8"]]
+ 00c0e71c ["CALLIND", null, ["register:0:8"]]
- 00c0d728 bytes 00013fd6
+ 00c0e71c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce1a5e0b7d05ec88c95d8be148c0fec8"></a>

### [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) → [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) FUN_00c11234

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`00c0ee1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0e/00c0ee1c.md) [`00c0f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f068.md) [`00c0f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f2b4.md) [`00c0f4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f4e4.md) [`00c0f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f714.md) · 呼出先 2件 [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md) [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)
- 新版 呼出元 14件 [`00c0fe10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0f/00c0fe10.md) [`00c1005c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c1005c.md) [`00c102a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c102a8.md) [`00c104d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c104d8.md) [`00c10708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10708.md) · 呼出先 2件 [`00c5c1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1f0.md) [`00c5f610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f610.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00c102a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102a8) · [`00c102c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102c8) · [`00c102d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md#insn-00c102d8)
- 新版 [`00c1129c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md#insn-00c1129c) · [`00c112bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md#insn-00c112bc) · [`00c112cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md#insn-00c112cc)

~~~diff
- 00c102a8 ["INT_ADD", "register:40f0:8", ["const:c102a8:8", "const:4:8"]]
- 00c102a8 ["CALL", null, ["callee:00c5f610:8"]]
+ 00c1129c ["INT_ADD", "register:40f0:8", ["const:c1129c:8", "const:4:8"]]
+ 00c1129c ["CALL", null, ["callee:00c5f610:8"]]
- 00c102a8 bytes e6380194
+ 00c1129c bytes dd380194
- 00c102c8 ["INT_ADD", "register:40f0:8", ["const:c102c8:8", "const:4:8"]]
- 00c102c8 ["CALL", null, ["callee:00c5c1f0:8"]]
+ 00c112bc ["INT_ADD", "register:40f0:8", ["const:c112bc:8", "const:4:8"]]
+ 00c112bc ["CALL", null, ["callee:00c5c1f0:8"]]
- 00c102c8 bytes d62b0194
+ 00c112bc bytes cd2b0194
- 00c102d8 ["INT_ADD", "register:40f0:8", ["const:c102d8:8", "const:4:8"]]
- 00c102d8 ["CALL", null, ["callee:00c5f610:8"]]
+ 00c112cc ["INT_ADD", "register:40f0:8", ["const:c112cc:8", "const:4:8"]]
+ 00c112cc ["CALL", null, ["callee:00c5f610:8"]]
- 00c102d8 bytes da380194
+ 00c112cc bytes d1380194
~~~


