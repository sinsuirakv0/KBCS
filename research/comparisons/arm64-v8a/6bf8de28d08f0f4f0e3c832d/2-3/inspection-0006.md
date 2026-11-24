# v16.0.2 → v16.0.3 · 要調査の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-956b1faadda2aed81c0389cb53f3a33a"></a>

### [`004af458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af458.md) → [`004af778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af778.md) _ZN5BotanleERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af458.md#insn-004af460)
- 新版 [`004af780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af778.md#insn-004af780)

~~~diff
- 004af460 ["INT_ADD", "register:40f0:8", ["const:4af460:8", "const:4:8"]]
- 004af460 ["CALL", null, ["callee:00c59a80:8"]]
+ 004af780 ["INT_ADD", "register:40f0:8", ["const:4af780:8", "const:4:8"]]
+ 004af780 ["CALL", null, ["callee:00c59a80:8"]]
- 004af460 bytes 94a51e94
+ 004af780 bytes c0a81e94
~~~


<a id="compare-68fb004c2de65723ec68a3a2e7614d88"></a>

### [`004af474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af474.md) → [`004af794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af794.md) _ZN5BotangeERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af474.md#insn-004af47c)
- 新版 [`004af79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af794.md#insn-004af79c)

~~~diff
- 004af47c ["INT_ADD", "register:40f0:8", ["const:4af47c:8", "const:4:8"]]
- 004af47c ["CALL", null, ["callee:00c59a80:8"]]
+ 004af79c ["INT_ADD", "register:40f0:8", ["const:4af79c:8", "const:4:8"]]
+ 004af79c ["CALL", null, ["callee:00c59a80:8"]]
- 004af47c bytes 8da51e94
+ 004af79c bytes b9a81e94
~~~


<a id="compare-517a92e41e43d47f5aa012a14b176e7d"></a>

### [`004af490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af490.md) → [`004af7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af7b0.md) _ZN5BotanltERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af490.md#insn-004af498)
- 新版 [`004af7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af7b0.md#insn-004af7b8)

~~~diff
- 004af498 ["INT_ADD", "register:40f0:8", ["const:4af498:8", "const:4:8"]]
- 004af498 ["CALL", null, ["callee:00c59a80:8"]]
+ 004af7b8 ["INT_ADD", "register:40f0:8", ["const:4af7b8:8", "const:4:8"]]
+ 004af7b8 ["CALL", null, ["callee:00c59a80:8"]]
- 004af498 bytes 86a51e94
+ 004af7b8 bytes b2a81e94
~~~


<a id="compare-6ff41ef86b632fe90129dcc1954cc60e"></a>

### [`004af4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4a8.md) → [`004af7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af7c8.md) _ZN5BotangtERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4a8.md#insn-004af4b0)
- 新版 [`004af7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af7c8.md#insn-004af7d0)

~~~diff
- 004af4b0 ["INT_ADD", "register:40f0:8", ["const:4af4b0:8", "const:4:8"]]
- 004af4b0 ["CALL", null, ["callee:00c59a80:8"]]
+ 004af7d0 ["INT_ADD", "register:40f0:8", ["const:4af7d0:8", "const:4:8"]]
+ 004af7d0 ["CALL", null, ["callee:00c59a80:8"]]
- 004af4b0 bytes 80a51e94
+ 004af7d0 bytes aca81e94
~~~


<a id="compare-939d2a2bbf2ce9e7745e327f1dfd6a84"></a>

### [`004af890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af890.md) → [`004afbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004afbb0.md) _ZNK5Botan11BER_Decoder10more_itemsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af890.md#insn-004af8ac)
- 新版 [`004afbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004afbb0.md#insn-004afbcc)

~~~diff
- 004af8ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004af8ac ["INT_ADD", "register:40f0:8", ["const:4af8ac:8", "const:4:8"]]
- 004af8ac ["CALLIND", null, ["register:0:8"]]
+ 004afbcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004afbcc ["INT_ADD", "register:40f0:8", ["const:4afbcc:8", "const:4:8"]]
+ 004afbcc ["CALLIND", null, ["register:0:8"]]
- 004af8ac bytes 00013fd6
+ 004afbcc bytes 00013fd6
~~~


<a id="compare-7e969f57bd4666eea0c5663d321aaad2"></a>

### [`004af9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md) → [`004afd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004afd14.md) _ZN5Botan11BER_Decoder17discard_remainingEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004afa28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md#insn-004afa28) · [`004afa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md#insn-004afa54)
- 新版 [`004afd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004afd14.md#insn-004afd48) · [`004afd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004afd14.md#insn-004afd74)

~~~diff
- 004afa28 ["COPY", "register:0:8", ["register:4040:8"]]
- 004afa28 ["INT_ADD", "register:40f0:8", ["const:4afa28:8", "const:4:8"]]
- 004afa28 ["CALLIND", null, ["register:0:8"]]
+ 004afd48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004afd48 ["INT_ADD", "register:40f0:8", ["const:4afd48:8", "const:4:8"]]
+ 004afd48 ["CALLIND", null, ["register:0:8"]]
- 004afa28 bytes 00013fd6
+ 004afd48 bytes 00013fd6
- 004afa54 ["INT_ADD", "register:40f0:8", ["const:4afa54:8", "const:4:8"]]
- 004afa54 ["CALL", null, ["callee:00c58f80:8"]]
+ 004afd74 ["INT_ADD", "register:40f0:8", ["const:4afd74:8", "const:4:8"]]
+ 004afd74 ["CALL", null, ["callee:00c58f80:8"]]
- 004afa54 bytes 57a11e94
+ 004afd74 bytes 83a41e94
~~~


<a id="compare-e6564b3f4b9fc4d0783afe9019a25eb2"></a>

### [`004b1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1488.md) → [`004b17a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b1/004b17a8.md) _ZN5Botan11BER_Decoder21get_next_octet_stringEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58970.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1488.md#insn-004b14b0)
- 新版 [`004b17d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b1/004b17a8.md#insn-004b17d0)

~~~diff
- 004b14b0 ["INT_ADD", "register:40f0:8", ["const:4b14b0:8", "const:4:8"]]
- 004b14b0 ["CALL", null, ["callee:00c59940:8"]]
+ 004b17d0 ["INT_ADD", "register:40f0:8", ["const:4b17d0:8", "const:4:8"]]
+ 004b17d0 ["CALL", null, ["callee:00c59940:8"]]
- 004b14b0 bytes 309d1e94
+ 004b17d0 bytes 5ca01e94
~~~


<a id="compare-06aab30364ced1b69a86458d9c6927ab"></a>

### [`004b2600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) → [`004b2920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2920.md) FUN_004b2920

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004ad4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) [`004b1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) · 呼出先 2件 [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`004ad810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ad/004ad810.md) [`004b224c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b224c.md) · 呼出先 2件 [`00541504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541504.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b2648) · [`004b26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b26f4) · [`004b273c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b273c)
- 新版 [`004b2968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2920.md#insn-004b2968) · [`004b2a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2920.md#insn-004b2a14) · [`004b2a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2920.md#insn-004b2a5c)

~~~diff
- 004b2648 ["INT_ADD", "register:40f0:8", ["const:4b2648:8", "const:4:8"]]
- 004b2648 ["CALL", null, ["callee:00541504:8"]]
+ 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
+ 004b2968 ["CALL", null, ["callee:00541504:8"]]
- 004b2648 bytes e73a0294
+ 004b2968 bytes e73a0294
- 004b26f4 ["INT_ADD", "register:40f0:8", ["const:4b26f4:8", "const:4:8"]]
- 004b26f4 ["CALL", null, ["callee:00541504:8"]]
+ 004b2a14 ["INT_ADD", "register:40f0:8", ["const:4b2a14:8", "const:4:8"]]
+ 004b2a14 ["CALL", null, ["callee:00541504:8"]]
- 004b26f4 bytes bc3a0294
+ 004b2a14 bytes bc3a0294
- 004b273c ["INT_ADD", "register:40f0:8", ["const:4b273c:8", "const:4:8"]]
- 004b273c ["CALL", null, ["callee:00541504:8"]]
+ 004b2a5c ["INT_ADD", "register:40f0:8", ["const:4b2a5c:8", "const:4:8"]]
+ 004b2a5c ["CALL", null, ["callee:00541504:8"]]
- 004b273c bytes aa3a0294
+ 004b2a5c bytes aa3a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880a4a002cb4b358e011916f5ba1cc8e"></a>

### [`004b2c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md) → [`004b2f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2f40.md) _ZN5Botan11DER_Encoder9raw_bytesEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59760.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c44) · [`004b2c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c70) · [`004b2c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c98)
- 新版 [`004b2f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2f40.md#insn-004b2f64) · [`004b2f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2f40.md#insn-004b2f90) · [`004b2fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2f40.md#insn-004b2fb8)

~~~diff
- 004b2c44 ["INT_ADD", "register:40f0:8", ["const:4b2c44:8", "const:4:8"]]
- 004b2c44 ["CALL", null, ["callee:00c59760:8"]]
+ 004b2f64 ["INT_ADD", "register:40f0:8", ["const:4b2f64:8", "const:4:8"]]
+ 004b2f64 ["CALL", null, ["callee:00c59760:8"]]
- 004b2c44 bytes d3961e94
+ 004b2f64 bytes ff991e94
- 004b2c70 ["INT_ADD", "register:40f0:8", ["const:4b2c70:8", "const:4:8"]]
- 004b2c70 ["CALL", null, ["callee:0054084c:8"]]
+ 004b2f90 ["INT_ADD", "register:40f0:8", ["const:4b2f90:8", "const:4:8"]]
+ 004b2f90 ["CALL", null, ["callee:0054084c:8"]]
- 004b2c70 bytes 2f360294
+ 004b2f90 bytes 2f360294
- 004b2c98 ["INT_ADD", "register:40f0:8", ["const:4b2c98:8", "const:4:8"]]
- 004b2c98 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004b2fb8 ["INT_ADD", "register:40f0:8", ["const:4b2fb8:8", "const:4:8"]]
+ 004b2fb8 ["CALL", null, ["callee:00c58fe0:8"]]
- 004b2c98 bytes de941e94
+ 004b2fb8 bytes 0a981e94
~~~


<a id="compare-d4d57bcd00dbd80fbbb806f9c49d4b54"></a>

### [`004b2cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md) → [`004b2fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2fe4.md) _ZN5Botan11DER_Encoder6encodeEb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md#insn-004b2cf8) · [`004b2d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md#insn-004b2d1c)
- 新版 [`004b3018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2fe4.md#insn-004b3018) · [`004b303c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2fe4.md#insn-004b303c)

~~~diff
- 004b2cf8 ["INT_ADD", "register:40f0:8", ["const:4b2cf8:8", "const:4:8"]]
- 004b2cf8 ["CALL", null, ["callee:00c598c0:8"]]
+ 004b3018 ["INT_ADD", "register:40f0:8", ["const:4b3018:8", "const:4:8"]]
+ 004b3018 ["CALL", null, ["callee:00c598c0:8"]]
- 004b2cf8 bytes fe961e94
+ 004b3018 bytes 2a9a1e94
- 004b2d1c ["INT_ADD", "register:40f0:8", ["const:4b2d1c:8", "const:4:8"]]
- 004b2d1c ["CALL", null, ["callee:00c58f80:8"]]
+ 004b303c ["INT_ADD", "register:40f0:8", ["const:4b303c:8", "const:4:8"]]
+ 004b303c ["CALL", null, ["callee:00c58f80:8"]]
- 004b2d1c bytes a5941e94
+ 004b303c bytes d1971e94
~~~


<a id="compare-1a6ff617ca427cb23926d1cbd13ad91a"></a>

### [`004b2d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md) → [`004b3040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3040.md) _ZN5Botan11DER_Encoder6encodeEbNS_8ASN1_TagES1_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md#insn-004b2d58) · [`004b2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md#insn-004b2d7c)
- 新版 [`004b3078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3040.md#insn-004b3078) · [`004b309c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3040.md#insn-004b309c)

~~~diff
- 004b2d58 ["INT_ADD", "register:40f0:8", ["const:4b2d58:8", "const:4:8"]]
- 004b2d58 ["CALL", null, ["callee:00c598c0:8"]]
+ 004b3078 ["INT_ADD", "register:40f0:8", ["const:4b3078:8", "const:4:8"]]
+ 004b3078 ["CALL", null, ["callee:00c598c0:8"]]
- 004b2d58 bytes e6961e94
+ 004b3078 bytes 129a1e94
- 004b2d7c ["INT_ADD", "register:40f0:8", ["const:4b2d7c:8", "const:4:8"]]
- 004b2d7c ["CALL", null, ["callee:00c58f80:8"]]
+ 004b309c ["INT_ADD", "register:40f0:8", ["const:4b309c:8", "const:4:8"]]
+ 004b309c ["CALL", null, ["callee:00c58f80:8"]]
- 004b2d7c bytes 8d941e94
+ 004b309c bytes b9971e94
~~~


<a id="compare-163f132ce2e9c4609500ee0abcc266a5"></a>

### [`004b3464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md) → [`004b3784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3784.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_h

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b348c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md#insn-004b348c) · [`004b34b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md#insn-004b34b0)
- 新版 [`004b37ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3784.md#insn-004b37ac) · [`004b37d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3784.md#insn-004b37d0)

~~~diff
- 004b348c ["INT_ADD", "register:40f0:8", ["const:4b348c:8", "const:4:8"]]
- 004b348c ["CALL", null, ["callee:00c598c0:8"]]
+ 004b37ac ["INT_ADD", "register:40f0:8", ["const:4b37ac:8", "const:4:8"]]
+ 004b37ac ["CALL", null, ["callee:00c598c0:8"]]
- 004b348c bytes 19951e94
+ 004b37ac bytes 45981e94
- 004b34b0 ["INT_ADD", "register:40f0:8", ["const:4b34b0:8", "const:4:8"]]
- 004b34b0 ["CALL", null, ["callee:00c58f80:8"]]
+ 004b37d0 ["INT_ADD", "register:40f0:8", ["const:4b37d0:8", "const:4:8"]]
+ 004b37d0 ["CALL", null, ["callee:00c58f80:8"]]
- 004b34b0 bytes c0921e94
+ 004b37d0 bytes ec951e94
~~~


<a id="compare-7b2202d4a9ba1ce46c5de030abd33e9f"></a>

### [`004b3dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3dbc.md) → [`004b40dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b40dc.md) _ZN5Botan11DER_Encoder9encode_ifEbRKNS_11ASN1_ObjectE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b3de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3dbc.md#insn-004b3de0)
- 新版 [`004b4100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b40dc.md#insn-004b4100)

~~~diff
- 004b3de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004b3de0 ["INT_ADD", "register:40f0:8", ["const:4b3de0:8", "const:4:8"]]
- 004b3de0 ["CALLIND", null, ["register:0:8"]]
+ 004b4100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004b4100 ["INT_ADD", "register:40f0:8", ["const:4b4100:8", "const:4:8"]]
+ 004b4100 ["CALLIND", null, ["register:0:8"]]
- 004b3de0 bytes 00013fd6
+ 004b4100 bytes 00013fd6
~~~


<a id="compare-b42d6dd061b363515727a399c4e9c773"></a>

### [`004b3df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md) → [`004b4114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4114.md) _ZN5Botan9SCAN_NameC1EPKc

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b3e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e24) · [`004b3e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e70) · [`004b3e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e90)
- 新版 [`004b4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4114.md#insn-004b4144) · [`004b4190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4114.md#insn-004b4190) · [`004b41b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4114.md#insn-004b41b0)

~~~diff
- 004b3e24 ["INT_ADD", "register:40f0:8", ["const:4b3e24:8", "const:4:8"]]
- 004b3e24 ["CALL", null, ["callee:00c59080:8"]]
+ 004b4144 ["INT_ADD", "register:40f0:8", ["const:4b4144:8", "const:4:8"]]
+ 004b4144 ["CALL", null, ["callee:00c59080:8"]]
- 004b3e24 bytes a3901e94
+ 004b4144 bytes cf931e94
- 004b3e70 ["INT_ADD", "register:40f0:8", ["const:4b3e70:8", "const:4:8"]]
- 004b3e70 ["CALL", null, ["callee:00c58f30:8"]]
+ 004b4190 ["INT_ADD", "register:40f0:8", ["const:4b4190:8", "const:4:8"]]
+ 004b4190 ["CALL", null, ["callee:00c58f30:8"]]
- 004b3e70 bytes 3c901e94
+ 004b4190 bytes 68931e94
- 004b3e90 ["INT_ADD", "register:40f0:8", ["const:4b3e90:8", "const:4:8"]]
- 004b3e90 ["CALL", null, ["callee:00c590a0:8"]]
+ 004b41b0 ["INT_ADD", "register:40f0:8", ["const:4b41b0:8", "const:4:8"]]
+ 004b41b0 ["CALL", null, ["callee:00c590a0:8"]]
- 004b3e90 bytes 90901e94
+ 004b41b0 bytes bc931e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1129e526a901a387692b799f33d55c"></a>

### [`004b4a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4a80.md) → [`004b4da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4da0.md) FUN_004b4da0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4a80.md#insn-004b4ac8)
- 新版 [`004b4de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4da0.md#insn-004b4de8)

~~~diff
- 004b4ac8 ["INT_ADD", "register:40f0:8", ["const:4b4ac8:8", "const:4:8"]]
- 004b4ac8 ["CALL", null, ["callee:00c58f50:8"]]
+ 004b4de8 ["INT_ADD", "register:40f0:8", ["const:4b4de8:8", "const:4:8"]]
+ 004b4de8 ["CALL", null, ["callee:00c58f50:8"]]
- 004b4ac8 bytes 2e8d1e94
+ 004b4de8 bytes 5a901e94
~~~


<a id="compare-454d9fdea531e75614a24750c3f9ee80"></a>

### [`004b4e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e08.md) → [`004b5128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5128.md) _ZNK5Botan9SCAN_Name14arg_as_integerEmm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c588c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59890.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e08.md#insn-004b4e3c)
- 新版 [`004b515c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5128.md#insn-004b515c)

~~~diff
- 004b4e3c ["INT_ADD", "register:40f0:8", ["const:4b4e3c:8", "const:4:8"]]
- 004b4e3c ["CALL", null, ["callee:00c59890:8"]]
+ 004b515c ["INT_ADD", "register:40f0:8", ["const:4b515c:8", "const:4:8"]]
+ 004b515c ["CALL", null, ["callee:00c59890:8"]]
- 004b4e3c bytes a18e1e94
+ 004b515c bytes cd911e94
~~~


<a id="compare-61791b6bab7ad3efc7fac855e366f2f0"></a>

### [`004b4f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md) → [`004b5268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5268.md) _ZN5Botan11OctetStringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c59b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59b80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4f80) · [`004b4fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4fa4) · [`004b4fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4fbc)
- 新版 [`004b52a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5268.md#insn-004b52a0) · [`004b52c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5268.md#insn-004b52c4) · [`004b52dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5268.md#insn-004b52dc)

~~~diff
- 004b4f80 ["INT_ADD", "register:40f0:8", ["const:4b4f80:8", "const:4:8"]]
- 004b4f80 ["CALL", null, ["callee:0054084c:8"]]
+ 004b52a0 ["INT_ADD", "register:40f0:8", ["const:4b52a0:8", "const:4:8"]]
+ 004b52a0 ["CALL", null, ["callee:0054084c:8"]]
- 004b4f80 bytes 6b2d0294
+ 004b52a0 bytes 6b2d0294
- 004b4fa4 ["INT_ADD", "register:40f0:8", ["const:4b4fa4:8", "const:4:8"]]
- 004b4fa4 ["CALL", null, ["callee:00c59b80:8"]]
+ 004b52c4 ["INT_ADD", "register:40f0:8", ["const:4b52c4:8", "const:4:8"]]
+ 004b52c4 ["CALL", null, ["callee:00c59b80:8"]]
- 004b4fa4 bytes 038f1e94
+ 004b52c4 bytes 2f921e94
- 004b4fbc ["INT_ADD", "register:40f0:8", ["const:4b4fbc:8", "const:4:8"]]
- 004b4fbc ["CALL", null, ["callee:0054084c:8"]]
+ 004b52dc ["INT_ADD", "register:40f0:8", ["const:4b52dc:8", "const:4:8"]]
+ 004b52dc ["CALL", null, ["callee:0054084c:8"]]
- 004b4fbc bytes 5c2d0294
+ 004b52dc bytes 5c2d0294
~~~


<a id="compare-045b1dd81ea92d6c504b7802d7d07540"></a>

### [`004b5010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5010.md) → [`004b5330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5330.md) _ZN5Botan11OctetStringC1EPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b5030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5010.md#insn-004b5030)
- 新版 [`004b5350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5330.md#insn-004b5350)

~~~diff
- 004b5030 ["INT_ADD", "register:40f0:8", ["const:4b5030:8", "const:4:8"]]
- 004b5030 ["CALL", null, ["callee:00543720:8"]]
+ 004b5350 ["INT_ADD", "register:40f0:8", ["const:4b5350:8", "const:4:8"]]
+ 004b5350 ["CALL", null, ["callee:00543720:8"]]
- 004b5030 bytes f4380294
+ 004b5350 bytes f4380294
~~~


<a id="compare-fb0d2ef446829c6126cecfb8a9407585"></a>

### [`004b5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5298.md) → [`004b55b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b55b8.md) _ZN5Botan11OctetStringeOERKS0_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5298.md#insn-004b534c)
- 新版 [`004b566c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b55b8.md#insn-004b566c)

~~~diff
- 004b534c ["INT_ADD", "register:40f0:8", ["const:4b534c:8", "const:4:8"]]
- 004b534c ["CALL", null, ["callee:00c59130:8"]]
+ 004b566c ["INT_ADD", "register:40f0:8", ["const:4b566c:8", "const:4:8"]]
+ 004b566c ["CALL", null, ["callee:00c59130:8"]]
- 004b534c bytes 858b1e94
+ 004b566c bytes b18e1e94
~~~


<a id="compare-9ce1ef290c194270591f7b0559888091"></a>

### [`004b54e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b54e4.md) → [`004b5804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5804.md) _ZN5BotanneERKNS_11OctetStringES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b54ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b54e4.md#insn-004b54ec)
- 新版 [`004b580c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5804.md#insn-004b580c)

~~~diff
- 004b54ec ["INT_ADD", "register:40f0:8", ["const:4b54ec:8", "const:4:8"]]
- 004b54ec ["CALL", null, ["callee:00c59c50:8"]]
+ 004b580c ["INT_ADD", "register:40f0:8", ["const:4b580c:8", "const:4:8"]]
+ 004b580c ["CALL", null, ["callee:00c59c50:8"]]
- 004b54ec bytes e58d1e94
+ 004b580c bytes 11911e94
~~~


<a id="compare-1bc2a9a7dc8a04f8d0a98e9171c29392"></a>

### [`004b61a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md) → [`004b64c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b64c0.md) _ZN5Botan13base64_decodeEPKcmb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c59c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b61e4) · [`004b61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b61f8) · [`004b6210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b6210)
- 新版 [`004b6504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b64c0.md#insn-004b6504) · [`004b6518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b64c0.md#insn-004b6518) · [`004b6530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b64c0.md#insn-004b6530)

~~~diff
- 004b61e4 ["INT_ADD", "register:40f0:8", ["const:4b61e4:8", "const:4:8"]]
- 004b61e4 ["CALL", null, ["callee:004b3868:8"]]
+ 004b6504 ["INT_ADD", "register:40f0:8", ["const:4b6504:8", "const:4:8"]]
+ 004b6504 ["CALL", null, ["callee:004b3868:8"]]
- 004b61e4 bytes d9f4ff97
+ 004b6504 bytes d9f4ff97
- 004b61f8 ["INT_ADD", "register:40f0:8", ["const:4b61f8:8", "const:4:8"]]
- 004b61f8 ["CALL", null, ["callee:00c59c90:8"]]
+ 004b6518 ["INT_ADD", "register:40f0:8", ["const:4b6518:8", "const:4:8"]]
+ 004b6518 ["CALL", null, ["callee:00c59c90:8"]]
- 004b61f8 bytes b28a1e94
+ 004b6518 bytes de8d1e94
- 004b6210 ["INT_ADD", "register:40f0:8", ["const:4b6210:8", "const:4:8"]]
- 004b6210 ["CALL", null, ["callee:0054084c:8"]]
+ 004b6530 ["INT_ADD", "register:40f0:8", ["const:4b6530:8", "const:4:8"]]
+ 004b6530 ["CALL", null, ["callee:0054084c:8"]]
- 004b6210 bytes c7280294
+ 004b6530 bytes c7280294
~~~


<a id="compare-071133923cce8471f2eb611bf9e70c47"></a>

### [`004b626c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md) → [`004b658c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b658c.md) _ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cd0.md) · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md)
- 新版 呼出元 1件 [`00c59ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ca0.md) · 呼出先 3件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c59c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b62c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62c0) · [`004b62d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62d4) · [`004b62ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62ec)
- 新版 [`004b65e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b658c.md#insn-004b65e0) · [`004b65f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b658c.md#insn-004b65f4) · [`004b660c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b658c.md#insn-004b660c)

~~~diff
- 004b62c0 ["INT_ADD", "register:40f0:8", ["const:4b62c0:8", "const:4:8"]]
- 004b62c0 ["CALL", null, ["callee:004b3868:8"]]
+ 004b65e0 ["INT_ADD", "register:40f0:8", ["const:4b65e0:8", "const:4:8"]]
+ 004b65e0 ["CALL", null, ["callee:004b3868:8"]]
- 004b62c0 bytes a2f4ff97
+ 004b65e0 bytes a2f4ff97
- 004b62d4 ["INT_ADD", "register:40f0:8", ["const:4b62d4:8", "const:4:8"]]
- 004b62d4 ["CALL", null, ["callee:00c59c90:8"]]
+ 004b65f4 ["INT_ADD", "register:40f0:8", ["const:4b65f4:8", "const:4:8"]]
+ 004b65f4 ["CALL", null, ["callee:00c59c90:8"]]
- 004b62d4 bytes 7b8a1e94
+ 004b65f4 bytes a78d1e94
- 004b62ec ["INT_ADD", "register:40f0:8", ["const:4b62ec:8", "const:4:8"]]
- 004b62ec ["CALL", null, ["callee:0054084c:8"]]
+ 004b660c ["INT_ADD", "register:40f0:8", ["const:4b660c:8", "const:4:8"]]
+ 004b660c ["CALL", null, ["callee:0054084c:8"]]
- 004b62ec bytes 90280294
+ 004b660c bytes 90280294
~~~


<a id="compare-892dbf105bfbaced11a0f4fe6cbbc2ec"></a>

### [`004b745c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md) → [`004b777c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b777c.md) _ZN5Botan6BigInt13encode_lockedERKS0_NS0_4BaseE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) [`00c58a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00c599e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599e0.md) [`00c599f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b7478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7478) · [`004b7484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7484) · [`004b7494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7494)
- 新版 [`004b7798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b777c.md#insn-004b7798) · [`004b77a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b777c.md#insn-004b77a4) · [`004b77b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b777c.md#insn-004b77b4)

~~~diff
- 004b7478 ["INT_ADD", "register:40f0:8", ["const:4b7478:8", "const:4:8"]]
- 004b7478 ["CALL", null, ["callee:00c599e0:8"]]
+ 004b7798 ["INT_ADD", "register:40f0:8", ["const:4b7798:8", "const:4:8"]]
+ 004b7798 ["CALL", null, ["callee:00c599e0:8"]]
- 004b7478 bytes 66851e94
+ 004b7798 bytes 92881e94
- 004b7484 ["INT_ADD", "register:40f0:8", ["const:4b7484:8", "const:4:8"]]
- 004b7484 ["CALL", null, ["callee:004b3868:8"]]
+ 004b77a4 ["INT_ADD", "register:40f0:8", ["const:4b77a4:8", "const:4:8"]]
+ 004b77a4 ["CALL", null, ["callee:004b3868:8"]]
- 004b7484 bytes 31f0ff97
+ 004b77a4 bytes 31f0ff97
- 004b7494 ["INT_ADD", "register:40f0:8", ["const:4b7494:8", "const:4:8"]]
- 004b7494 ["CALL", null, ["callee:00c599f0:8"]]
+ 004b77b4 ["INT_ADD", "register:40f0:8", ["const:4b77b4:8", "const:4:8"]]
+ 004b77b4 ["CALL", null, ["callee:00c599f0:8"]]
- 004b7494 bytes 63851e94
+ 004b77b4 bytes 8f881e94
~~~


<a id="compare-dcab72ccbb214fed0393149ea940d995"></a>

### [`004b7500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md) → [`004b7820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7820.md) _ZN5Botan6BigInt11encode_1363ERKS0_m

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00c59d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md#insn-004b7518) · [`004b7528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md#insn-004b7528)
- 新版 [`004b7838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7820.md#insn-004b7838) · [`004b7848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7820.md#insn-004b7848)

~~~diff
- 004b7518 ["INT_ADD", "register:40f0:8", ["const:4b7518:8", "const:4:8"]]
- 004b7518 ["CALL", null, ["callee:004b3868:8"]]
+ 004b7838 ["INT_ADD", "register:40f0:8", ["const:4b7838:8", "const:4:8"]]
+ 004b7838 ["CALL", null, ["callee:004b3868:8"]]
- 004b7518 bytes 0cf0ff97
+ 004b7838 bytes 0cf0ff97
- 004b7528 ["INT_ADD", "register:40f0:8", ["const:4b7528:8", "const:4:8"]]
- 004b7528 ["CALL", null, ["callee:00c59d00:8"]]
+ 004b7848 ["INT_ADD", "register:40f0:8", ["const:4b7848:8", "const:4:8"]]
+ 004b7848 ["CALL", null, ["callee:00c59d00:8"]]
- 004b7528 bytes 02861e94
+ 004b7848 bytes 2e891e94
~~~


<a id="compare-00c5b0e4425a69cd1207e0cf8ad3c512"></a>

### [`004b76e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md) → [`004b7a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7a04.md) _ZN5Botan6BigInt28encode_fixed_length_int_pairERKS0_S2_m

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00c59d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b770c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b770c) · [`004b771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b771c) · [`004b7730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b7730)
- 新版 [`004b7a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7a04.md#insn-004b7a2c) · [`004b7a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7a04.md#insn-004b7a3c) · [`004b7a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7a04.md#insn-004b7a50)

~~~diff
- 004b770c ["INT_ADD", "register:40f0:8", ["const:4b770c:8", "const:4:8"]]
- 004b770c ["CALL", null, ["callee:004b3868:8"]]
+ 004b7a2c ["INT_ADD", "register:40f0:8", ["const:4b7a2c:8", "const:4:8"]]
+ 004b7a2c ["CALL", null, ["callee:004b3868:8"]]
- 004b770c bytes 8fefff97
+ 004b7a2c bytes 8fefff97
- 004b771c ["INT_ADD", "register:40f0:8", ["const:4b771c:8", "const:4:8"]]
- 004b771c ["CALL", null, ["callee:00c59d00:8"]]
+ 004b7a3c ["INT_ADD", "register:40f0:8", ["const:4b7a3c:8", "const:4:8"]]
+ 004b7a3c ["CALL", null, ["callee:00c59d00:8"]]
- 004b771c bytes 85851e94
+ 004b7a3c bytes b1881e94
- 004b7730 ["INT_ADD", "register:40f0:8", ["const:4b7730:8", "const:4:8"]]
- 004b7730 ["CALL", null, ["callee:00c59d00:8"]]
+ 004b7a50 ["INT_ADD", "register:40f0:8", ["const:4b7a50:8", "const:4:8"]]
+ 004b7a50 ["CALL", null, ["callee:00c59d00:8"]]
- 004b7730 bytes 80851e94
+ 004b7a50 bytes ac881e94
~~~


<a id="compare-b03d8fbd9d77f2a013b5da8d49342b8f"></a>

### [`004b7a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md) → [`004b7da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7da4.md) _ZN5Botan17hex_decode_lockedEPKcmb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c59b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59b80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b7ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7ab0) · [`004b7ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7ac4) · [`004b7adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7adc)
- 新版 [`004b7dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7da4.md#insn-004b7dd0) · [`004b7de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7da4.md#insn-004b7de4) · [`004b7dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7da4.md#insn-004b7dfc)

~~~diff
- 004b7ab0 ["INT_ADD", "register:40f0:8", ["const:4b7ab0:8", "const:4:8"]]
- 004b7ab0 ["CALL", null, ["callee:004b3868:8"]]
+ 004b7dd0 ["INT_ADD", "register:40f0:8", ["const:4b7dd0:8", "const:4:8"]]
+ 004b7dd0 ["CALL", null, ["callee:004b3868:8"]]
- 004b7ab0 bytes a6eeff97
+ 004b7dd0 bytes a6eeff97
- 004b7ac4 ["INT_ADD", "register:40f0:8", ["const:4b7ac4:8", "const:4:8"]]
- 004b7ac4 ["CALL", null, ["callee:00c59b80:8"]]
+ 004b7de4 ["INT_ADD", "register:40f0:8", ["const:4b7de4:8", "const:4:8"]]
+ 004b7de4 ["CALL", null, ["callee:00c59b80:8"]]
- 004b7ac4 bytes 3b841e94
+ 004b7de4 bytes 67871e94
- 004b7adc ["INT_ADD", "register:40f0:8", ["const:4b7adc:8", "const:4:8"]]
- 004b7adc ["CALL", null, ["callee:0054084c:8"]]
+ 004b7dfc ["INT_ADD", "register:40f0:8", ["const:4b7dfc:8", "const:4:8"]]
+ 004b7dfc ["CALL", null, ["callee:0054084c:8"]]
- 004b7adc bytes 94220294
+ 004b7dfc bytes 94220294
~~~


<a id="compare-33d7e34c070b08fdbf7ae17cc089f2dd"></a>

### [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) → [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md) FUN_004b8b14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) [`004b9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md) [`004b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md) · 呼出先 1件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md)
- 新版 呼出元 9件 [`004b8328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8328.md) [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md) [`004b9074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md) [`004ba118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba118.md) [`004ba2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba2a0.md) · 呼出先 1件 [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b881c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md#insn-004b881c)
- 新版 [`004b8b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md#insn-004b8b3c)

~~~diff
- 004b881c ["INT_ADD", "register:40f0:8", ["const:4b881c:8", "const:4:8"]]
- 004b881c ["CALL", null, ["local:b0:8"]]
+ 004b8b3c ["INT_ADD", "register:40f0:8", ["const:4b8b3c:8", "const:4:8"]]
+ 004b8b3c ["CALL", null, ["local:b0:8"]]
- 004b881c bytes f6ffff97
+ 004b8b3c bytes f6ffff97
~~~


<a id="compare-7ae84e17ef7ffa36f56fd98721fc79de"></a>

### [`004b947c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md) → [`004b979c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b979c.md) _ZN5Botan6BigIntrSEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d00.md) · 呼出先 1件 [`004b9c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md)
- 新版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cd0.md) · 呼出先 1件 [`004b9f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9f98.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b94c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md#insn-004b94c4)
- 新版 [`004b97e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b979c.md#insn-004b97e4)

~~~diff
- 004b94c4 ["INT_ADD", "register:40f0:8", ["const:4b94c4:8", "const:4:8"]]
- 004b94c4 ["CALL", null, ["callee:004b9f98:8"]]
+ 004b97e4 ["INT_ADD", "register:40f0:8", ["const:4b97e4:8", "const:4:8"]]
+ 004b97e4 ["CALL", null, ["callee:004b9f98:8"]]
- 004b94c4 bytes ed010094
+ 004b97e4 bytes ed010094
~~~


<a id="compare-9c1bdc1796d525a9462d1417922acf81"></a>

### [`004b9b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md) → [`004b9e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9e68.md) _ZN5Botan6BigIntlSEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ce0.md) · 呼出先 3件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c59cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cb0.md) · 呼出先 3件 [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9bd8) · [`004b9c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9c14) · [`004b9c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9c24)
- 新版 [`004b9ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9e68.md#insn-004b9ef8) · [`004b9f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9e68.md#insn-004b9f34) · [`004b9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9e68.md#insn-004b9f44)

~~~diff
- 004b9bd8 ["INT_ADD", "register:40f0:8", ["const:4b9bd8:8", "const:4:8"]]
- 004b9bd8 ["CALL", null, ["callee:00540c80:8"]]
+ 004b9ef8 ["INT_ADD", "register:40f0:8", ["const:4b9ef8:8", "const:4:8"]]
+ 004b9ef8 ["CALL", null, ["callee:00540c80:8"]]
- 004b9bd8 bytes 621b0294
+ 004b9ef8 bytes 621b0294
- 004b9c14 ["INT_ADD", "register:40f0:8", ["const:4b9c14:8", "const:4:8"]]
- 004b9c14 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004b9f34 ["INT_ADD", "register:40f0:8", ["const:4b9f34:8", "const:4:8"]]
+ 004b9f34 ["CALL", null, ["callee:00c58fe0:8"]]
- 004b9c14 bytes ff781e94
+ 004b9f34 bytes 2b7c1e94
- 004b9c24 ["INT_ADD", "register:40f0:8", ["const:4b9c24:8", "const:4:8"]]
- 004b9c24 ["CALL", null, ["callee:00c59130:8"]]
+ 004b9f44 ["INT_ADD", "register:40f0:8", ["const:4b9f44:8", "const:4:8"]]
+ 004b9f44 ["CALL", null, ["callee:00c59130:8"]]
- 004b9c24 bytes 4f791e94
+ 004b9f44 bytes 7b7c1e94
~~~


<a id="compare-c245c8fba6b2fdd5af68e503f3dde084"></a>

### [`004b9c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md) → [`004b9f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9f98.md) FUN_004b9f98

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004b947c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md) [`004d9558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9558.md) [`004da6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004da/004da6e8.md) [`004dd348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dd/004dd348.md) [`004dfe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004dfe3c.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 5件 [`004b979c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b979c.md) [`004d9878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d9/004d9878.md) [`004daa08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004da/004daa08.md) [`004dd668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004dd/004dd668.md) [`004e015c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e0/004e015c.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md#insn-004b9ce0) · [`004b9d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md#insn-004b9d20)
- 新版 [`004ba000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9f98.md#insn-004ba000) · [`004ba040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9f98.md#insn-004ba040)

~~~diff
- 004b9ce0 ["INT_ADD", "register:40f0:8", ["const:4b9ce0:8", "const:4:8"]]
- 004b9ce0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004ba000 ["INT_ADD", "register:40f0:8", ["const:4ba000:8", "const:4:8"]]
+ 004ba000 ["CALL", null, ["callee:00c58fe0:8"]]
- 004b9ce0 bytes cc781e94
+ 004ba000 bytes f87b1e94
- 004b9d20 ["INT_ADD", "register:40f0:8", ["const:4b9d20:8", "const:4:8"]]
- 004b9d20 ["CALL", null, ["callee:00c59130:8"]]
+ 004ba040 ["INT_ADD", "register:40f0:8", ["const:4ba040:8", "const:4:8"]]
+ 004ba040 ["CALL", null, ["callee:00c59130:8"]]
- 004b9d20 bytes 10791e94
+ 004ba040 bytes 3c7c1e94
~~~


<a id="compare-892e0529adb265972f696ffa04e5c6f0"></a>

### [`004b9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md) → [`004ba118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba118.md) _ZN5BotanplERKNS_6BigIntES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d80.md) · 呼出先 4件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004d6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6d54.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)
- 新版 呼出元 1件 [`00c59d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d50.md) · 呼出先 4件 [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md) [`004b8cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8cac.md) [`004d7074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d7/004d7074.md) [`00c59cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9e74) · [`004b9ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9ea0) · [`004b9ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9ed0)
- 新版 [`004ba194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba118.md#insn-004ba194) · [`004ba1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba118.md#insn-004ba1c0) · [`004ba1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba118.md#insn-004ba1f0)

~~~diff
- 004b9e74 ["INT_ADD", "register:40f0:8", ["const:4b9e74:8", "const:4:8"]]
- 004b9e74 ["CALL", null, ["callee:00c59cc0:8"]]
+ 004ba194 ["INT_ADD", "register:40f0:8", ["const:4ba194:8", "const:4:8"]]
+ 004ba194 ["CALL", null, ["callee:00c59cc0:8"]]
- 004b9e74 bytes 9f7b1e94
+ 004ba194 bytes cb7e1e94
- 004b9ea0 ["INT_ADD", "register:40f0:8", ["const:4b9ea0:8", "const:4:8"]]
- 004b9ea0 ["CALL", null, ["callee:004d7074:8"]]
+ 004ba1c0 ["INT_ADD", "register:40f0:8", ["const:4ba1c0:8", "const:4:8"]]
+ 004ba1c0 ["CALL", null, ["callee:004d7074:8"]]
- 004b9ea0 bytes ad730094
+ 004ba1c0 bytes ad730094
- 004b9ed0 ["INT_ADD", "register:40f0:8", ["const:4b9ed0:8", "const:4:8"]]
- 004b9ed0 ["CALL", null, ["callee:004b8b14:8"]]
+ 004ba1f0 ["INT_ADD", "register:40f0:8", ["const:4ba1f0:8", "const:4:8"]]
+ 004ba1f0 ["CALL", null, ["callee:004b8b14:8"]]
- 004b9ed0 bytes 49faff97
+ 004ba1f0 bytes 49faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3babb592e2a5d414f08624b14688254d"></a>

### [`004b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md) → [`004ba2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba2a0.md) _ZN5BotanmiERKNS_6BigIntES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d90.md) · 呼出先 4件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004d6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6d54.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)
- 新版 呼出元 1件 [`00c59d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d60.md) · 呼出先 4件 [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md) [`004b8cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8cac.md) [`004d7074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d7/004d7074.md) [`00c59cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004b9ff8) · [`004ba014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004ba014) · [`004ba048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004ba048)
- 新版 [`004ba318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba2a0.md#insn-004ba318) · [`004ba334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba2a0.md#insn-004ba334) · [`004ba368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba2a0.md#insn-004ba368)

~~~diff
- 004b9ff8 ["INT_ADD", "register:40f0:8", ["const:4b9ff8:8", "const:4:8"]]
- 004b9ff8 ["CALL", null, ["callee:004b8b14:8"]]
+ 004ba318 ["INT_ADD", "register:40f0:8", ["const:4ba318:8", "const:4:8"]]
+ 004ba318 ["CALL", null, ["callee:004b8b14:8"]]
- 004b9ff8 bytes fff9ff97
+ 004ba318 bytes fff9ff97
- 004ba014 ["INT_ADD", "register:40f0:8", ["const:4ba014:8", "const:4:8"]]
- 004ba014 ["CALL", null, ["callee:00c59cc0:8"]]
+ 004ba334 ["INT_ADD", "register:40f0:8", ["const:4ba334:8", "const:4:8"]]
+ 004ba334 ["CALL", null, ["callee:00c59cc0:8"]]
- 004ba014 bytes 377b1e94
+ 004ba334 bytes 637e1e94
- 004ba048 ["INT_ADD", "register:40f0:8", ["const:4ba048:8", "const:4:8"]]
- 004ba048 ["CALL", null, ["callee:004b8cac:8"]]
+ 004ba368 ["INT_ADD", "register:40f0:8", ["const:4ba368:8", "const:4:8"]]
+ 004ba368 ["CALL", null, ["callee:004b8cac:8"]]
- 004ba048 bytes 51faff97
+ 004ba368 bytes 51faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823f331d2c3464617542aa3df05b1459"></a>

### [`004ba63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba63c.md) → [`004ba95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba95c.md) _ZN5BotanlsERKNS_6BigIntEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md) [`00c59cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ba69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba63c.md#insn-004ba69c)
- 新版 [`004ba9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba95c.md#insn-004ba9bc)

~~~diff
- 004ba69c ["INT_ADD", "register:40f0:8", ["const:4ba69c:8", "const:4:8"]]
- 004ba69c ["CALL", null, ["callee:00c59cc0:8"]]
+ 004ba9bc ["INT_ADD", "register:40f0:8", ["const:4ba9bc:8", "const:4:8"]]
+ 004ba9bc ["CALL", null, ["callee:00c59cc0:8"]]
- 004ba69c bytes 95791e94
+ 004ba9bc bytes c17c1e94
~~~


<a id="compare-e5e6114d66fff1495e49f3f08c4aa0d6"></a>

### [`004ba78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba78c.md) → [`004baaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baaac.md) _ZN5BotanrsERKNS_6BigIntEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58db0.md) · 呼出先 3件 [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)
- 新版 呼出元 1件 [`00c59d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d80.md) · 呼出先 3件 [`00c599c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599c0.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md) [`00c59cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ba868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba78c.md#insn-004ba868)
- 新版 [`004bab88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baaac.md#insn-004bab88)

~~~diff
- 004ba868 ["INT_ADD", "register:40f0:8", ["const:4ba868:8", "const:4:8"]]
- 004ba868 ["CALL", null, ["callee:00c59cc0:8"]]
+ 004bab88 ["INT_ADD", "register:40f0:8", ["const:4bab88:8", "const:4:8"]]
+ 004bab88 ["CALL", null, ["callee:00c59cc0:8"]]
- 004ba868 bytes 22791e94
+ 004bab88 bytes 4e7c1e94
~~~


<a id="compare-b1f243ca328ec2b3d41676ef6de17dc9"></a>

### [`004bab0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md) → [`004bae2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004bae2c.md) _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dd0.md) · 呼出先 2件 [`00c58bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bf0.md) [`00c58dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dc0.md)
- 新版 呼出元 1件 [`00c59da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59da0.md) · 呼出先 2件 [`00c59bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59bc0.md) [`00c59d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004babc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babc8) · [`004babd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babd8) · [`004babec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babec)
- 新版 [`004baee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004bae2c.md#insn-004baee8) · [`004baef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004bae2c.md#insn-004baef8) · [`004baf0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004bae2c.md#insn-004baf0c)

~~~diff
- 004babc8 ["INT_ADD", "register:40f0:8", ["const:4babc8:8", "const:4:8"]]
- 004babc8 ["CALL", null, ["callee:00c59d90:8"]]
+ 004baee8 ["INT_ADD", "register:40f0:8", ["const:4baee8:8", "const:4:8"]]
+ 004baee8 ["CALL", null, ["callee:00c59d90:8"]]
- 004babc8 bytes 7e781e94
+ 004baee8 bytes aa7b1e94
- 004babd8 ["INT_ADD", "register:40f0:8", ["const:4babd8:8", "const:4:8"]]
- 004babd8 ["CALL", null, ["callee:00c59bc0:8"]]
+ 004baef8 ["INT_ADD", "register:40f0:8", ["const:4baef8:8", "const:4:8"]]
+ 004baef8 ["CALL", null, ["callee:00c59bc0:8"]]
- 004babd8 bytes 06781e94
+ 004baef8 bytes 327b1e94
- 004babec ["INT_ADD", "register:40f0:8", ["const:4babec:8", "const:4:8"]]
- 004babec ["CALL", null, ["callee:00c59bc0:8"]]
+ 004baf0c ["INT_ADD", "register:40f0:8", ["const:4baf0c:8", "const:4:8"]]
+ 004baf0c ["CALL", null, ["callee:00c59bc0:8"]]
- 004babec bytes 01781e94
+ 004baf0c bytes 2d7b1e94
~~~


<a id="compare-f531ff7113a3d9b3ffe3860aa5d9313c"></a>

### [`004bac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac1c.md) → [`004baf3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baf3c.md) _ZN5Botan6BigIntC1Em

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)
- 新版 呼出元 1件 [`00c599c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599c0.md) · 呼出先 1件 [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bac48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac1c.md#insn-004bac48)
- 新版 [`004baf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baf3c.md#insn-004baf68)

~~~diff
- 004bac48 ["INT_ADD", "register:40f0:8", ["const:4bac48:8", "const:4:8"]]
- 004bac48 ["CALL", null, ["callee:00540c80:8"]]
+ 004baf68 ["INT_ADD", "register:40f0:8", ["const:4baf68:8", "const:4:8"]]
+ 004baf68 ["CALL", null, ["callee:00540c80:8"]]
- 004bac48 bytes 46170294
+ 004baf68 bytes 46170294
~~~


<a id="compare-767919a7c751f48dd6939ce6db82c12b"></a>

### [`004bac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac74.md) → [`004baf94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baf94.md) _ZN5Botan6BigIntC1ENS0_4SignEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md) · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)
- 新版 呼出元 1件 [`00c59cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59cc0.md) · 呼出先 1件 [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bacb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac74.md#insn-004bacb8)
- 新版 [`004bafd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004baf94.md#insn-004bafd8)

~~~diff
- 004bacb8 ["INT_ADD", "register:40f0:8", ["const:4bacb8:8", "const:4:8"]]
- 004bacb8 ["CALL", null, ["callee:00540c80:8"]]
+ 004bafd8 ["INT_ADD", "register:40f0:8", ["const:4bafd8:8", "const:4:8"]]
+ 004bafd8 ["CALL", null, ["callee:00540c80:8"]]
- 004bacb8 bytes 2a170294
+ 004bafd8 bytes 2a170294
~~~


<a id="compare-064333fdb9dfd43a8eef750f44d10eaa"></a>

### [`004bace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bace0.md) → [`004bb000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb000.md) _ZN5Botan6BigIntC2ERKS0_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) · 呼出先 1件 [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md)
- 新版 呼出元 1件 [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md) · 呼出先 1件 [`00543a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bad1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bace0.md#insn-004bad1c)
- 新版 [`004bb03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb000.md#insn-004bb03c)

~~~diff
- 004bad1c ["INT_ADD", "register:40f0:8", ["const:4bad1c:8", "const:4:8"]]
- 004bad1c ["CALL", null, ["callee:00543a3c:8"]]
+ 004bb03c ["INT_ADD", "register:40f0:8", ["const:4bb03c:8", "const:4:8"]]
+ 004bb03c ["CALL", null, ["callee:00543a3c:8"]]
- 004bad1c bytes 80220294
+ 004bb03c bytes 80220294
~~~


<a id="compare-a182004ce5eece85852d5a78a0a47d80"></a>

### [`004bb034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb034.md) → [`004bb354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb354.md) _ZN5Botan6BigIntC2ERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59420.md) · 呼出先 1件 [`00c58dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dc0.md)
- 新版 呼出元 1件 [`00c5a3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a3f0.md) · 呼出先 1件 [`00c59d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb034.md#insn-004bb054)
- 新版 [`004bb374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb354.md#insn-004bb374)

~~~diff
- 004bb054 ["INT_ADD", "register:40f0:8", ["const:4bb054:8", "const:4:8"]]
- 004bb054 ["CALL", null, ["callee:00c59d90:8"]]
+ 004bb374 ["INT_ADD", "register:40f0:8", ["const:4bb374:8", "const:4:8"]]
+ 004bb374 ["CALL", null, ["callee:00c59d90:8"]]
- 004bb054 bytes 5b771e94
+ 004bb374 bytes 877a1e94
~~~


<a id="compare-945ee80e7feb82e31cdb406dd4be4eff"></a>

### [`004bb078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb078.md) → [`004bb398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb398.md) _ZNK5Botan6BigInt3cmpERKS0_b

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bf0.md) · 呼出先 1件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md)
- 新版 呼出元 1件 [`00c59bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59bc0.md) · 呼出先 1件 [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb078.md#insn-004bb108)
- 新版 [`004bb428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb398.md#insn-004bb428)

~~~diff
- 004bb108 ["INT_ADD", "register:40f0:8", ["const:4bb108:8", "const:4:8"]]
- 004bb108 ["CALL", null, ["callee:004b8b14:8"]]
+ 004bb428 ["INT_ADD", "register:40f0:8", ["const:4bb428:8", "const:4:8"]]
+ 004bb428 ["CALL", null, ["callee:004b8b14:8"]]
- 004bb108 bytes bbf5ff97
+ 004bb428 bytes bbf5ff97
~~~


<a id="compare-d51388f9179a84aec13b9ece9251f555"></a>

### [`004bb5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb5bc.md) → [`004bb8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb8dc.md) _ZN5Botan6BigInt7set_bitEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb5bc.md#insn-004bb60c)
- 新版 [`004bb92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb8dc.md#insn-004bb92c)

~~~diff
- 004bb60c ["INT_ADD", "register:40f0:8", ["const:4bb60c:8", "const:4:8"]]
- 004bb60c ["CALL", null, ["callee:00540c80:8"]]
+ 004bb92c ["INT_ADD", "register:40f0:8", ["const:4bb92c:8", "const:4:8"]]
+ 004bb92c ["CALL", null, ["callee:00540c80:8"]]
- 004bb60c bytes d5140294
+ 004bb92c bytes d5140294
~~~


<a id="compare-838a640640f8bc65813da6a632db521b"></a>

### [`004bb66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb66c.md) → [`004bb98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb98c.md) _ZNK5Botan6BigIntngEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb66c.md#insn-004bb684)
- 新版 [`004bb9a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb98c.md#insn-004bb9a4)

~~~diff
- 004bb684 ["INT_ADD", "register:40f0:8", ["const:4bb684:8", "const:4:8"]]
- 004bb684 ["CALL", null, ["callee:00c59be0:8"]]
+ 004bb9a4 ["INT_ADD", "register:40f0:8", ["const:4bb9a4:8", "const:4:8"]]
+ 004bb9a4 ["CALL", null, ["callee:00c59be0:8"]]
- 004bb684 bytes 63751e94
+ 004bb9a4 bytes 8f781e94
~~~


<a id="compare-88ea64639e631cbd48de19c6c3a1fb2a"></a>

### [`004bb6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb6e4.md) → [`004bba04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba04.md) _ZNK5Botan6BigInt3absEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb6e4.md#insn-004bb6fc)
- 新版 [`004bba1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba04.md#insn-004bba1c)

~~~diff
- 004bb6fc ["INT_ADD", "register:40f0:8", ["const:4bb6fc:8", "const:4:8"]]
- 004bb6fc ["CALL", null, ["callee:00c59be0:8"]]
+ 004bba1c ["INT_ADD", "register:40f0:8", ["const:4bba1c:8", "const:4:8"]]
+ 004bba1c ["CALL", null, ["callee:00c59be0:8"]]
- 004bb6fc bytes 45751e94
+ 004bba1c bytes 71781e94
~~~


<a id="compare-10a5db118a54dccd90b1714b2d993915"></a>

### [`004bbf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md) → [`004bc278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc278.md) FUN_004bc278

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c130c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004c162c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c162c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bbfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbfa4) · [`004bbfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbfb4) · [`004bbff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbff0)
- 新版 [`004bc2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc278.md#insn-004bc2c4) · [`004bc2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc278.md#insn-004bc2d4) · [`004bc310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc278.md#insn-004bc310)

~~~diff
- 004bbfa4 ["INT_ADD", "register:40f0:8", ["const:4bbfa4:8", "const:4:8"]]
- 004bbfa4 ["CALL", null, ["callee:00c58f50:8"]]
+ 004bc2c4 ["INT_ADD", "register:40f0:8", ["const:4bc2c4:8", "const:4:8"]]
+ 004bc2c4 ["CALL", null, ["callee:00c58f50:8"]]
- 004bbfa4 bytes f76f1e94
+ 004bc2c4 bytes 23731e94
- 004bbfb4 ["INT_ADD", "register:40f0:8", ["const:4bbfb4:8", "const:4:8"]]
- 004bbfb4 ["CALL", null, ["callee:00c58f50:8"]]
+ 004bc2d4 ["INT_ADD", "register:40f0:8", ["const:4bc2d4:8", "const:4:8"]]
+ 004bc2d4 ["CALL", null, ["callee:00c58f50:8"]]
- 004bbfb4 bytes f36f1e94
+ 004bc2d4 bytes 1f731e94
- 004bbff0 ["INT_ADD", "register:40f0:8", ["const:4bbff0:8", "const:4:8"]]
- 004bbff0 ["CALL", null, ["callee:00c58f50:8"]]
+ 004bc310 ["INT_ADD", "register:40f0:8", ["const:4bc310:8", "const:4:8"]]
+ 004bc310 ["CALL", null, ["callee:00c58f50:8"]]
- 004bbff0 bytes e46f1e94
+ 004bc310 bytes 10731e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83067ab7075775adce6084db0a402db"></a>

### [`004bc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md) → [`004bc474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc474.md) _ZN5Botan11BlockCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004bc2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`004bc5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc5d8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc1c4) · [`004bc1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc1d4) · [`004bc210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc210)
- 新版 [`004bc4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc474.md#insn-004bc4e4) · [`004bc4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc474.md#insn-004bc4f4) · [`004bc530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc474.md#insn-004bc530)

~~~diff
- 004bc1c4 ["INT_ADD", "register:40f0:8", ["const:4bc1c4:8", "const:4:8"]]
- 004bc1c4 ["CALL", null, ["callee:004738a0:8"]]
+ 004bc4e4 ["INT_ADD", "register:40f0:8", ["const:4bc4e4:8", "const:4:8"]]
+ 004bc4e4 ["CALL", null, ["callee:004738a0:8"]]
- 004bc1c4 bytes efdcfe97
+ 004bc4e4 bytes efdcfe97
- 004bc1d4 ["INT_ADD", "register:40f0:8", ["const:4bc1d4:8", "const:4:8"]]
- 004bc1d4 ["CALL", null, ["callee:004bc5d8:8"]]
+ 004bc4f4 ["INT_ADD", "register:40f0:8", ["const:4bc4f4:8", "const:4:8"]]
+ 004bc4f4 ["CALL", null, ["callee:004bc5d8:8"]]
- 004bc1d4 bytes 39000094
+ 004bc4f4 bytes 39000094
- 004bc210 ["INT_ADD", "register:40f0:8", ["const:4bc210:8", "const:4:8"]]
- 004bc210 ["CALL", null, ["callee:00c58f50:8"]]
+ 004bc530 ["INT_ADD", "register:40f0:8", ["const:4bc530:8", "const:4:8"]]
+ 004bc530 ["CALL", null, ["callee:00c58f50:8"]]
- 004bc210 bytes 5c6f1e94
+ 004bc530 bytes 88721e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed6a8528ffa8f9eb054dd28bbf78888"></a>

### [`004bc2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md) → [`004bc5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc5d8.md) FUN_004bc5d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004bc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e00.md)
- 新版 呼出元 1件 [`004bc474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc474.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59dd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc308) · [`004bc31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc31c) · [`004bc338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc338)
- 新版 [`004bc628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc5d8.md#insn-004bc628) · [`004bc63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc5d8.md#insn-004bc63c) · [`004bc658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc5d8.md#insn-004bc658)

~~~diff
- 004bc308 ["INT_ADD", "register:40f0:8", ["const:4bc308:8", "const:4:8"]]
- 004bc308 ["CALL", null, ["callee:005410dc:8"]]
+ 004bc628 ["INT_ADD", "register:40f0:8", ["const:4bc628:8", "const:4:8"]]
+ 004bc628 ["CALL", null, ["callee:005410dc:8"]]
- 004bc308 bytes ad120294
+ 004bc628 bytes ad120294
- 004bc31c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc31c ["INT_ADD", "register:40f0:8", ["const:4bc31c:8", "const:4:8"]]
- 004bc31c ["CALLIND", null, ["register:0:8"]]
+ 004bc63c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc63c ["INT_ADD", "register:40f0:8", ["const:4bc63c:8", "const:4:8"]]
+ 004bc63c ["CALLIND", null, ["register:0:8"]]
- 004bc31c bytes 00013fd6
+ 004bc63c bytes 00013fd6
- 004bc338 ["INT_ADD", "register:40f0:8", ["const:4bc338:8", "const:4:8"]]
- 004bc338 ["CALL", null, ["callee:00c59dd0:8"]]
+ 004bc658 ["INT_ADD", "register:40f0:8", ["const:4bc658:8", "const:4:8"]]
+ 004bc658 ["CALL", null, ["callee:00c59dd0:8"]]
- 004bc338 bytes b2721e94
+ 004bc658 bytes de751e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d9a75cd21187b7795a9c88033f0b99"></a>

### [`004bc720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc720.md) → [`004bca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca40.md) _ZN5Botan8CBC_Mode5clearEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc720.md#insn-004bc73c)
- 新版 [`004bca5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca40.md#insn-004bca5c)

~~~diff
- 004bc73c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc73c ["INT_ADD", "register:40f0:8", ["const:4bc73c:8", "const:4:8"]]
- 004bc73c ["CALLIND", null, ["register:0:8"]]
+ 004bca5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bca5c ["INT_ADD", "register:40f0:8", ["const:4bca5c:8", "const:4:8"]]
+ 004bca5c ["CALLIND", null, ["register:0:8"]]
- 004bc73c bytes 00013fd6
+ 004bca5c bytes 00013fd6
~~~


<a id="compare-ed57e87d0ebdf92872324651689293a3"></a>

### [`004bc9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md) → [`004bccdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bccdc.md) _ZNK5Botan8CBC_Mode18update_granularityEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md#insn-004bc9d8) · [`004bc9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md#insn-004bc9ec)
- 新版 [`004bccf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bccdc.md#insn-004bccf8) · [`004bcd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bccdc.md#insn-004bcd0c)

~~~diff
- 004bc9d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc9d8 ["INT_ADD", "register:40f0:8", ["const:4bc9d8:8", "const:4:8"]]
- 004bc9d8 ["CALLIND", null, ["register:0:8"]]
+ 004bccf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bccf8 ["INT_ADD", "register:40f0:8", ["const:4bccf8:8", "const:4:8"]]
+ 004bccf8 ["CALLIND", null, ["register:0:8"]]
- 004bc9d8 bytes 00013fd6
+ 004bccf8 bytes 00013fd6
- 004bc9ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc9ec ["INT_ADD", "register:40f0:8", ["const:4bc9ec:8", "const:4:8"]]
- 004bc9ec ["CALLIND", null, ["register:0:8"]]
+ 004bcd0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcd0c ["INT_ADD", "register:40f0:8", ["const:4bcd0c:8", "const:4:8"]]
+ 004bcd0c ["CALLIND", null, ["register:0:8"]]
- 004bc9ec bytes 00013fd6
+ 004bcd0c bytes 00013fd6
~~~


<a id="compare-102bef0366cd86c8e46a016512bc5b17"></a>

### [`004bdda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bdda8.md) → [`004be0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be0c8.md) _ZN5Botan14CBC_Decryption5resetEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bdda8.md#insn-004bddcc)
- 新版 [`004be0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be0c8.md#insn-004be0ec)

~~~diff
- 004bddcc ["INT_ADD", "register:40f0:8", ["const:4bddcc:8", "const:4:8"]]
- 004bddcc ["CALL", null, ["callee:00c59130:8"]]
+ 004be0ec ["INT_ADD", "register:40f0:8", ["const:4be0ec:8", "const:4:8"]]
+ 004be0ec ["CALL", null, ["callee:00c59130:8"]]
- 004bddcc bytes e5681e94
+ 004be0ec bytes 116c1e94
~~~


<a id="compare-254ea20ca1d3b7c870012d76c34c2bc9"></a>

### [`004beb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md) → [`004bee34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004bee34.md) _ZN5Botan11string_joinERKNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEc

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c596a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004beb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md#insn-004beb60) · [`004beb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md#insn-004beb88)
- 新版 [`004bee80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004bee34.md#insn-004bee80) · [`004beea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004bee34.md#insn-004beea8)

~~~diff
- 004beb60 ["INT_ADD", "register:40f0:8", ["const:4beb60:8", "const:4:8"]]
- 004beb60 ["CALL", null, ["callee:00c596a0:8"]]
+ 004bee80 ["INT_ADD", "register:40f0:8", ["const:4bee80:8", "const:4:8"]]
+ 004bee80 ["CALL", null, ["callee:00c596a0:8"]]
- 004beb60 bytes dc661e94
+ 004bee80 bytes 086a1e94
- 004beb88 ["INT_ADD", "register:40f0:8", ["const:4beb88:8", "const:4:8"]]
- 004beb88 ["CALL", null, ["callee:00c59020:8"]]
+ 004beea8 ["INT_ADD", "register:40f0:8", ["const:4beea8:8", "const:4:8"]]
+ 004beea8 ["CALL", null, ["callee:00c59020:8"]]
- 004beb88 bytes 32651e94
+ 004beea8 bytes 5e681e94
~~~


<a id="compare-1fc08b25e2d8401b9a79f54dcae89d29"></a>

### [`004becd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md) → [`004beff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beff8.md) _ZN5Botan5CPUID15bit_from_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004beee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bf200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bed58) · [`004bedbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bedbc) · [`004bee08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bee08)
- 新版 [`004bf078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beff8.md#insn-004bf078) · [`004bf0dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beff8.md#insn-004bf0dc) · [`004bf128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beff8.md#insn-004bf128)

~~~diff
- 004bed58 ["INT_ADD", "register:40f0:8", ["const:4bed58:8", "const:4:8"]]
- 004bed58 ["CALL", null, ["callee:00c58f30:8"]]
+ 004bf078 ["INT_ADD", "register:40f0:8", ["const:4bf078:8", "const:4:8"]]
+ 004bf078 ["CALL", null, ["callee:00c58f30:8"]]
- 004bed58 bytes 82641e94
+ 004bf078 bytes ae671e94
- 004bedbc ["INT_ADD", "register:40f0:8", ["const:4bedbc:8", "const:4:8"]]
- 004bedbc ["CALL", null, ["callee:004bf200:8"]]
+ 004bf0dc ["INT_ADD", "register:40f0:8", ["const:4bf0dc:8", "const:4:8"]]
+ 004bf0dc ["CALL", null, ["callee:004bf200:8"]]
- 004bedbc bytes 49000094
+ 004bf0dc bytes 49000094
- 004bee08 ["INT_ADD", "register:40f0:8", ["const:4bee08:8", "const:4:8"]]
- 004bee08 ["CALL", null, ["callee:00c58f30:8"]]
+ 004bf128 ["INT_ADD", "register:40f0:8", ["const:4bf128:8", "const:4:8"]]
+ 004bf128 ["CALL", null, ["callee:00c58f30:8"]]
- 004bee08 bytes 56641e94
+ 004bf128 bytes 82671e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8124dd82f7edba2e56d724e577cd0c12"></a>

### [`004beee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md) → [`004bf200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md) FUN_004bf200

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004becd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md) · 呼出先 5件 [`00543a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`004beff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beff8.md) · 呼出先 5件 [`00543d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d20.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bef14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef14) · [`004bef2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef2c) · [`004bef48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef48)
- 新版 [`004bf234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md#insn-004bf234) · [`004bf24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md#insn-004bf24c) · [`004bf268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md#insn-004bf268)

~~~diff
- 004bef14 ["INT_ADD", "register:40f0:8", ["const:4bef14:8", "const:4:8"]]
- 004bef14 ["CALL", null, ["callee:00c58f30:8"]]
+ 004bf234 ["INT_ADD", "register:40f0:8", ["const:4bf234:8", "const:4:8"]]
+ 004bf234 ["CALL", null, ["callee:00c58f30:8"]]
- 004bef14 bytes 13641e94
+ 004bf234 bytes 3f671e94
- 004bef2c ["INT_ADD", "register:40f0:8", ["const:4bef2c:8", "const:4:8"]]
- 004bef2c ["CALL", null, ["callee:00c58fe0:8"]]
+ 004bf24c ["INT_ADD", "register:40f0:8", ["const:4bf24c:8", "const:4:8"]]
+ 004bf24c ["CALL", null, ["callee:00c58fe0:8"]]
- 004bef2c bytes 39641e94
+ 004bf24c bytes 65671e94
- 004bef48 ["INT_ADD", "register:40f0:8", ["const:4bef48:8", "const:4:8"]]
- 004bef48 ["CALL", null, ["callee:00543d20:8"]]
+ 004bf268 ["INT_ADD", "register:40f0:8", ["const:4bf268:8", "const:4:8"]]
+ 004bf268 ["CALL", null, ["callee:00543d20:8"]]
- 004bef48 bytes ae120294
+ 004bf268 bytes ae120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87194875bfe487996d97fca167c7741c"></a>

### [`004bf418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md) → [`004bf738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf738.md) _ZNK5Botan8ECB_Mode18update_granularityEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bf434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md#insn-004bf434) · [`004bf448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md#insn-004bf448)
- 新版 [`004bf754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf738.md#insn-004bf754) · [`004bf768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf738.md#insn-004bf768)

~~~diff
- 004bf434 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf434 ["INT_ADD", "register:40f0:8", ["const:4bf434:8", "const:4:8"]]
- 004bf434 ["CALLIND", null, ["register:0:8"]]
+ 004bf754 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf754 ["INT_ADD", "register:40f0:8", ["const:4bf754:8", "const:4:8"]]
+ 004bf754 ["CALLIND", null, ["register:0:8"]]
- 004bf434 bytes 00013fd6
+ 004bf754 bytes 00013fd6
- 004bf448 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf448 ["INT_ADD", "register:40f0:8", ["const:4bf448:8", "const:4:8"]]
- 004bf448 ["CALLIND", null, ["register:0:8"]]
+ 004bf768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf768 ["INT_ADD", "register:40f0:8", ["const:4bf768:8", "const:4:8"]]
+ 004bf768 ["CALLIND", null, ["register:0:8"]]
- 004bf448 bytes 00013fd6
+ 004bf768 bytes 00013fd6
~~~


<a id="compare-067dd93d8b034fb5a26e61ca693ae37f"></a>

### [`004bfc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md) → [`004bffa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bffa0.md) _ZN5Botan13EMSA_PKCS1v158raw_dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bfca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfca0) · [`004bfcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfcac) · [`004bfcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfcc0)
- 新版 [`004bffc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bffa0.md#insn-004bffc0) · [`004bffcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bffa0.md#insn-004bffcc) · [`004bffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bffa0.md#insn-004bffe0)

~~~diff
- 004bfca0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bfca0 ["INT_ADD", "register:40f0:8", ["const:4bfca0:8", "const:4:8"]]
- 004bfca0 ["CALLIND", null, ["register:0:8"]]
+ 004bffc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bffc0 ["INT_ADD", "register:40f0:8", ["const:4bffc0:8", "const:4:8"]]
+ 004bffc0 ["CALLIND", null, ["register:0:8"]]
- 004bfca0 bytes 20013fd6
+ 004bffc0 bytes 20013fd6
- 004bfcac ["INT_ADD", "register:40f0:8", ["const:4bfcac:8", "const:4:8"]]
- 004bfcac ["CALL", null, ["callee:004b3868:8"]]
+ 004bffcc ["INT_ADD", "register:40f0:8", ["const:4bffcc:8", "const:4:8"]]
+ 004bffcc ["CALL", null, ["callee:004b3868:8"]]
- 004bfcac bytes 27ceff97
+ 004bffcc bytes 27ceff97
- 004bfcc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfcc0 ["INT_ADD", "register:40f0:8", ["const:4bfcc0:8", "const:4:8"]]
- 004bfcc0 ["CALLIND", null, ["register:0:8"]]
+ 004bffe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bffe0 ["INT_ADD", "register:40f0:8", ["const:4bffe0:8", "const:4:8"]]
+ 004bffe0 ["CALLIND", null, ["register:0:8"]]
- 004bfcc0 bytes 00013fd6
+ 004bffe0 bytes 00013fd6
~~~


<a id="compare-222daa45079f49947059e3a87300c7c5"></a>

### [`004bfce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md) → [`004c0004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0004.md) FUN_004c0004

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md) · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)
- 新版 呼出元 1件 [`004c21a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md) · 呼出先 1件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bfd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd00) · [`004bfd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd0c) · [`004bfd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd20)
- 新版 [`004c0020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0004.md#insn-004c0020) · [`004c002c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0004.md#insn-004c002c) · [`004c0040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0004.md#insn-004c0040)

~~~diff
- 004bfd00 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bfd00 ["INT_ADD", "register:40f0:8", ["const:4bfd00:8", "const:4:8"]]
- 004bfd00 ["CALLIND", null, ["register:0:8"]]
+ 004c0020 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0020 ["INT_ADD", "register:40f0:8", ["const:4c0020:8", "const:4:8"]]
+ 004c0020 ["CALLIND", null, ["register:0:8"]]
- 004bfd00 bytes 20013fd6
+ 004c0020 bytes 20013fd6
- 004bfd0c ["INT_ADD", "register:40f0:8", ["const:4bfd0c:8", "const:4:8"]]
- 004bfd0c ["CALL", null, ["callee:004b3868:8"]]
+ 004c002c ["INT_ADD", "register:40f0:8", ["const:4c002c:8", "const:4:8"]]
+ 004c002c ["CALL", null, ["callee:004b3868:8"]]
- 004bfd0c bytes 0fceff97
+ 004c002c bytes 0fceff97
- 004bfd20 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfd20 ["INT_ADD", "register:40f0:8", ["const:4bfd20:8", "const:4:8"]]
- 004bfd20 ["CALLIND", null, ["register:0:8"]]
+ 004c0040 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c0040 ["INT_ADD", "register:40f0:8", ["const:4c0040:8", "const:4:8"]]
+ 004c0040 ["CALLIND", null, ["register:0:8"]]
- 004bfd20 bytes 00013fd6
+ 004c0040 bytes 00013fd6
~~~


<a id="compare-0008d3616d2dc4d91f78e681246a6499"></a>

### [`004c0744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0744.md) → [`004c0a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0a64.md) FUN_004c0a64

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`004fdcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fd/004fdcdc.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c07b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0744.md#insn-004c07b0)
- 新版 [`004c0ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0a64.md#insn-004c0ad0)

~~~diff
- 004c07b0 ["INT_ADD", "register:40f0:8", ["const:4c07b0:8", "const:4:8"]]
- 004c07b0 ["CALL", null, ["callee:00c590f0:8"]]
+ 004c0ad0 ["INT_ADD", "register:40f0:8", ["const:4c0ad0:8", "const:4:8"]]
+ 004c0ad0 ["CALL", null, ["callee:00c590f0:8"]]
- 004c07b0 bytes 5c5e1e94
+ 004c0ad0 bytes 88611e94
~~~


<a id="compare-5d510ebc480793a9e220368fc8e22e40"></a>

### [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) → [`004c0b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md) FUN_004c0b14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ea0.md)
- 新版 呼出元 2件 [`004c04e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md) [`004c285c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c59e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c0840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c0840) · [`004c084c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c084c) · [`004c085c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c085c)
- 新版 [`004c0b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md#insn-004c0b60) · [`004c0b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md#insn-004c0b6c) · [`004c0b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md#insn-004c0b7c)

~~~diff
- 004c0840 ["INT_ADD", "register:40f0:8", ["const:4c0840:8", "const:4:8"]]
- 004c0840 ["CALL", null, ["callee:0043be80:8"]]
+ 004c0b60 ["INT_ADD", "register:40f0:8", ["const:4c0b60:8", "const:4:8"]]
+ 004c0b60 ["CALL", null, ["callee:0043be80:8"]]
- 004c0840 bytes c8ecfd97
+ 004c0b60 bytes c8ecfd97
- 004c084c ["INT_ADD", "register:40f0:8", ["const:4c084c:8", "const:4:8"]]
- 004c084c ["CALL", null, ["callee:00c59e70:8"]]
+ 004c0b6c ["INT_ADD", "register:40f0:8", ["const:4c0b6c:8", "const:4:8"]]
+ 004c0b6c ["CALL", null, ["callee:00c59e70:8"]]
- 004c084c bytes 95611e94
+ 004c0b6c bytes c1641e94
- 004c085c ["INT_ADD", "register:40f0:8", ["const:4c085c:8", "const:4:8"]]
- 004c085c ["CALL", null, ["callee:00c58f50:8"]]
+ 004c0b7c ["INT_ADD", "register:40f0:8", ["const:4c0b7c:8", "const:4:8"]]
+ 004c0b7c ["CALL", null, ["callee:00c58f50:8"]]
- 004c085c bytes c95d1e94
+ 004c0b7c bytes f5601e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-416d09191cb6d5f4e00efa7c55e027e6"></a>

### [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) → [`004c0dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0dd8.md) FUN_004c0dd8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c0ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md#insn-004c0ad4)
- 新版 [`004c0df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0dd8.md#insn-004c0df4)

~~~diff
- 004c0ad4 ["INT_ADD", "register:40f0:8", ["const:4c0ad4:8", "const:4:8"]]
- 004c0ad4 ["CALL", null, ["callee:00c58f50:8"]]
+ 004c0df4 ["INT_ADD", "register:40f0:8", ["const:4c0df4:8", "const:4:8"]]
+ 004c0df4 ["CALL", null, ["callee:00c58f50:8"]]
- 004c0ad4 bytes 2b5d1e94
+ 004c0df4 bytes 57601e94
~~~


<a id="compare-2e520fc8fdd39f1ac4d32d9eb0e9508c"></a>

### [`004c130c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md) → [`004c162c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c162c.md) _ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004bbf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md) [`004cb76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb76c.md) [`004cb928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb928.md) [`004cbadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbadc.md)
- 新版 呼出元 1件 [`00c59e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e90.md) · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004bc278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc278.md) [`004cba8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cba8c.md) [`004cbc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbc48.md) [`004cbdfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbdfc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c1444) · [`004c144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c144c) · [`004c1480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c1480)
- 新版 [`004c1764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c162c.md#insn-004c1764) · [`004c176c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c162c.md#insn-004c176c) · [`004c17a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c162c.md#insn-004c17a0)

~~~diff
- 004c1444 ["INT_ADD", "register:40f0:8", ["const:4c1444:8", "const:4:8"]]
- 004c1444 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c1764 ["INT_ADD", "register:40f0:8", ["const:4c1764:8", "const:4:8"]]
+ 004c1764 ["CALL", null, ["callee:00c58f30:8"]]
- 004c1444 bytes c75a1e94
+ 004c1764 bytes f35d1e94
- 004c144c ["INT_ADD", "register:40f0:8", ["const:4c144c:8", "const:4:8"]]
- 004c144c ["CALL", null, ["callee:004cbdfc:8"]]
+ 004c176c ["INT_ADD", "register:40f0:8", ["const:4c176c:8", "const:4:8"]]
+ 004c176c ["CALL", null, ["callee:004cbdfc:8"]]
- 004c144c bytes a4290094
+ 004c176c bytes a4290094
- 004c1480 ["INT_ADD", "register:40f0:8", ["const:4c1480:8", "const:4:8"]]
- 004c1480 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c17a0 ["INT_ADD", "register:40f0:8", ["const:4c17a0:8", "const:4:8"]]
+ 004c17a0 ["CALL", null, ["callee:00c58f30:8"]]
- 004c1480 bytes b85a1e94
+ 004c17a0 bytes e45d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff492385ef95aee95835a63fb325965"></a>

### [`004c15a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c15a0.md) → [`004c18c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c18c0.md) _ZN5Botan17EMSA_PKCS1v15_Raw6updateEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c15d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c15a0.md#insn-004c15d8)
- 新版 [`004c18f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c18c0.md#insn-004c18f8)

~~~diff
- 004c15d8 ["INT_ADD", "register:40f0:8", ["const:4c15d8:8", "const:4:8"]]
- 004c15d8 ["CALL", null, ["callee:0054084c:8"]]
+ 004c18f8 ["INT_ADD", "register:40f0:8", ["const:4c18f8:8", "const:4:8"]]
+ 004c18f8 ["CALL", null, ["callee:0054084c:8"]]
- 004c15d8 bytes d5fb0194
+ 004c18f8 bytes d5fb0194
~~~


<a id="compare-37fbd97b78e5b02409ce471d1b2e17ef"></a>

### [`004c18f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md) → [`004c1c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1c10.md) _ZN5Botan4PSSR8raw_dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c1910) · [`004c191c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c191c) · [`004c1930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c1930)
- 新版 [`004c1c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1c10.md#insn-004c1c30) · [`004c1c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1c10.md#insn-004c1c3c) · [`004c1c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1c10.md#insn-004c1c50)

~~~diff
- 004c1910 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1910 ["INT_ADD", "register:40f0:8", ["const:4c1910:8", "const:4:8"]]
- 004c1910 ["CALLIND", null, ["register:0:8"]]
+ 004c1c30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1c30 ["INT_ADD", "register:40f0:8", ["const:4c1c30:8", "const:4:8"]]
+ 004c1c30 ["CALLIND", null, ["register:0:8"]]
- 004c1910 bytes 20013fd6
+ 004c1c30 bytes 20013fd6
- 004c191c ["INT_ADD", "register:40f0:8", ["const:4c191c:8", "const:4:8"]]
- 004c191c ["CALL", null, ["callee:004b3868:8"]]
+ 004c1c3c ["INT_ADD", "register:40f0:8", ["const:4c1c3c:8", "const:4:8"]]
+ 004c1c3c ["CALL", null, ["callee:004b3868:8"]]
- 004c191c bytes 0bc7ff97
+ 004c1c3c bytes 0bc7ff97
- 004c1930 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1930 ["INT_ADD", "register:40f0:8", ["const:4c1930:8", "const:4:8"]]
- 004c1930 ["CALLIND", null, ["register:0:8"]]
+ 004c1c50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1c50 ["INT_ADD", "register:40f0:8", ["const:4c1c50:8", "const:4:8"]]
+ 004c1c50 ["CALLIND", null, ["register:0:8"]]
- 004c1930 bytes 00013fd6
+ 004c1c50 bytes 00013fd6
~~~


<a id="compare-4882ffea1fe2c58aaa937f118640e8e3"></a>

### [`004c332c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md) → [`004c364c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c364c.md) _ZN5Botan15Entropy_Sources10add_sourceENSt6__ndk110unique_ptrINS_14Entropy_SourceENS1_14default_deleteIS3_EEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f00.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00543c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c59ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ed0.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00543fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c33b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33b0) · [`004c33e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33e8) · [`004c33fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33fc)
- 新版 [`004c36d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c364c.md#insn-004c36d0) · [`004c3708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c364c.md#insn-004c3708) · [`004c371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c364c.md#insn-004c371c)

~~~diff
- 004c33b0 ["INT_ADD", "register:40f0:8", ["const:4c33b0:8", "const:4:8"]]
- 004c33b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c36d0 ["INT_ADD", "register:40f0:8", ["const:4c36d0:8", "const:4:8"]]
+ 004c36d0 ["CALL", null, ["callee:00c58f30:8"]]
- 004c33b0 bytes ec521e94
+ 004c36d0 bytes 18561e94
- 004c33e8 ["INT_ADD", "register:40f0:8", ["const:4c33e8:8", "const:4:8"]]
- 004c33e8 ["CALL", null, ["callee:00c590a0:8"]]
+ 004c3708 ["INT_ADD", "register:40f0:8", ["const:4c3708:8", "const:4:8"]]
+ 004c3708 ["CALL", null, ["callee:00c590a0:8"]]
- 004c33e8 bytes 3a531e94
+ 004c3708 bytes 66561e94
- 004c33fc ["INT_ADD", "register:40f0:8", ["const:4c33fc:8", "const:4:8"]]
- 004c33fc ["CALL", null, ["callee:00c58f50:8"]]
+ 004c371c ["INT_ADD", "register:40f0:8", ["const:4c371c:8", "const:4:8"]]
+ 004c371c ["CALL", null, ["callee:00c58f50:8"]]
- 004c33fc bytes e1521e94
+ 004c371c bytes 0d561e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feed632f3b859d9a01147fd034ebdbe8"></a>

### [`004c3424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md) → [`004c3744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3744.md) _ZNK5Botan15Entropy_Sources15enabled_sourcesEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c34c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c34c8) · [`004c3530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c3530) · [`004c3574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c3574)
- 新版 [`004c37e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3744.md#insn-004c37e8) · [`004c3850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3744.md#insn-004c3850) · [`004c3894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3744.md#insn-004c3894)

~~~diff
- 004c34c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c34c8 ["INT_ADD", "register:40f0:8", ["const:4c34c8:8", "const:4:8"]]
- 004c34c8 ["CALLIND", null, ["register:0:8"]]
+ 004c37e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c37e8 ["INT_ADD", "register:40f0:8", ["const:4c37e8:8", "const:4:8"]]
+ 004c37e8 ["CALLIND", null, ["register:0:8"]]
- 004c34c8 bytes 20013fd6
+ 004c37e8 bytes 20013fd6
- 004c3530 ["INT_ADD", "register:40f0:8", ["const:4c3530:8", "const:4:8"]]
- 004c3530 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c3850 ["INT_ADD", "register:40f0:8", ["const:4c3850:8", "const:4:8"]]
+ 004c3850 ["CALL", null, ["callee:00c58f30:8"]]
- 004c3530 bytes 8c521e94
+ 004c3850 bytes b8551e94
- 004c3574 ["INT_ADD", "register:40f0:8", ["const:4c3574:8", "const:4:8"]]
- 004c3574 ["CALL", null, ["callee:00c590a0:8"]]
+ 004c3894 ["INT_ADD", "register:40f0:8", ["const:4c3894:8", "const:4:8"]]
+ 004c3894 ["CALL", null, ["callee:00c590a0:8"]]
- 004c3574 bytes d7521e94
+ 004c3894 bytes 03561e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f6b7e094b66c9379960a14ddcfe0097"></a>

### [`004c366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md) → [`004c398c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c398c.md) _ZN5Botan15Entropy_Sources4pollERNS_21RandomNumberGeneratorEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c3690) · [`004c36c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c36c0) · [`004c36d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c36d0)
- 新版 [`004c39b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c398c.md#insn-004c39b0) · [`004c39e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c398c.md#insn-004c39e0) · [`004c39f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c398c.md#insn-004c39f0)

~~~diff
- 004c3690 ["INT_ADD", "register:40f0:8", ["const:4c3690:8", "const:4:8"]]
- 004c3690 ["CALL", null, ["callee:00c59620:8"]]
+ 004c39b0 ["INT_ADD", "register:40f0:8", ["const:4c39b0:8", "const:4:8"]]
+ 004c39b0 ["CALL", null, ["callee:00c59620:8"]]
- 004c3690 bytes f0531e94
+ 004c39b0 bytes 1c571e94
- 004c36c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c36c0 ["INT_ADD", "register:40f0:8", ["const:4c36c0:8", "const:4:8"]]
- 004c36c0 ["CALLIND", null, ["register:0:8"]]
+ 004c39e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c39e0 ["INT_ADD", "register:40f0:8", ["const:4c39e0:8", "const:4:8"]]
+ 004c39e0 ["CALLIND", null, ["register:0:8"]]
- 004c36c0 bytes 00013fd6
+ 004c39e0 bytes 00013fd6
- 004c36d0 ["INT_ADD", "register:40f0:8", ["const:4c36d0:8", "const:4:8"]]
- 004c36d0 ["CALL", null, ["callee:00c59620:8"]]
+ 004c39f0 ["INT_ADD", "register:40f0:8", ["const:4c39f0:8", "const:4:8"]]
+ 004c39f0 ["CALL", null, ["callee:00c59620:8"]]
- 004c36d0 bytes e0531e94
+ 004c39f0 bytes 0c571e94
~~~


<a id="compare-7d7d132c07e6298d3b6b6a938e5670a7"></a>

### [`004c3710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md) → [`004c3a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3a30.md) _ZN5Botan15Entropy_Sources9poll_justERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c376c) · [`004c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c3778) · [`004c37a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c37a4)
- 新版 [`004c3a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3a30.md#insn-004c3a8c) · [`004c3a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3a30.md#insn-004c3a98) · [`004c3ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3a30.md#insn-004c3ac4)

~~~diff
- 004c376c ["INT_ADD", "register:40f0:8", ["const:4c376c:8", "const:4:8"]]
- 004c376c ["CALL", null, ["callee:00c590f0:8"]]
+ 004c3a8c ["INT_ADD", "register:40f0:8", ["const:4c3a8c:8", "const:4:8"]]
+ 004c3a8c ["CALL", null, ["callee:00c590f0:8"]]
- 004c376c bytes 6d521e94
+ 004c3a8c bytes 99551e94
- 004c3778 ["INT_ADD", "register:40f0:8", ["const:4c3778:8", "const:4:8"]]
- 004c3778 ["CALL", null, ["callee:00c58f50:8"]]
+ 004c3a98 ["INT_ADD", "register:40f0:8", ["const:4c3a98:8", "const:4:8"]]
+ 004c3a98 ["CALL", null, ["callee:00c58f50:8"]]
- 004c3778 bytes 02521e94
+ 004c3a98 bytes 2e551e94
- 004c37a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c37a4 ["INT_ADD", "register:40f0:8", ["const:4c37a4:8", "const:4:8"]]
- 004c37a4 ["CALLIND", null, ["register:0:8"]]
+ 004c3ac4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c3ac4 ["INT_ADD", "register:40f0:8", ["const:4c3ac4:8", "const:4:8"]]
+ 004c3ac4 ["CALLIND", null, ["register:0:8"]]
- 004c37a4 bytes 20013fd6
+ 004c3ac4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8ae1c29a2809044f9e4c560a79c22c"></a>

### [`004c3890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3890.md) → [`004c3bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3bb0.md) FUN_004c3bb0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`004fdcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fd/004fdcdc.md) [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c38fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3890.md#insn-004c38fc)
- 新版 [`004c3c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3bb0.md#insn-004c3c1c)

~~~diff
- 004c38fc ["INT_ADD", "register:40f0:8", ["const:4c38fc:8", "const:4:8"]]
- 004c38fc ["CALL", null, ["callee:00c590f0:8"]]
+ 004c3c1c ["INT_ADD", "register:40f0:8", ["const:4c3c1c:8", "const:4:8"]]
+ 004c3c1c ["CALL", null, ["callee:00c590f0:8"]]
- 004c38fc bytes 09521e94
+ 004c3c1c bytes 35551e94
~~~


<a id="compare-89b6212bcba3b1eaa942a2b258a94e23"></a>

### [`004c3b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b00.md) → [`004c3e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e20.md) FUN_004c3e20

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b00.md#insn-004c3b4c)
- 新版 [`004c3e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e20.md#insn-004c3e6c)

~~~diff
- 004c3b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c3b4c ["INT_ADD", "register:40f0:8", ["const:4c3b4c:8", "const:4:8"]]
- 004c3b4c ["CALLIND", null, ["register:0:8"]]
+ 004c3e6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3e6c ["INT_ADD", "register:40f0:8", ["const:4c3e6c:8", "const:4:8"]]
+ 004c3e6c ["CALLIND", null, ["register:0:8"]]
- 004c3b4c bytes 00013fd6
+ 004c3e6c bytes 00013fd6
~~~


<a id="compare-9e87733e4402797b83f7c0046eef14de"></a>

### [`004c3edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md) → [`004c41fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c41fc.md) FUN_004c41fc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004c3e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e9c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md#insn-004c3f28)
- 新版 [`004c4248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c41fc.md#insn-004c4248)

~~~diff
- 004c3f28 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c3f28 ["INT_ADD", "register:40f0:8", ["const:4c3f28:8", "const:4:8"]]
- 004c3f28 ["CALLIND", null, ["register:0:8"]]
+ 004c4248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c4248 ["INT_ADD", "register:40f0:8", ["const:4c4248:8", "const:4:8"]]
+ 004c4248 ["CALLIND", null, ["register:0:8"]]
- 004c3f28 bytes 00013fd6
+ 004c4248 bytes 00013fd6
~~~


<a id="compare-b219bc94cf61e5b5c0eff792dddc836f"></a>

### [`004c46b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md) → [`004c49d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c49d8.md) _ZN5Botan19StreamCipher_Filter5writeEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c46fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md#insn-004c46fc) · [`004c4714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md#insn-004c4714)
- 新版 [`004c4a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c49d8.md#insn-004c4a1c) · [`004c4a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c49d8.md#insn-004c4a34)

~~~diff
- 004c46fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004c46fc ["INT_ADD", "register:40f0:8", ["const:4c46fc:8", "const:4:8"]]
- 004c46fc ["CALLIND", null, ["register:0:8"]]
+ 004c4a1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c4a1c ["INT_ADD", "register:40f0:8", ["const:4c4a1c:8", "const:4:8"]]
+ 004c4a1c ["CALLIND", null, ["register:0:8"]]
- 004c46fc bytes 20013fd6
+ 004c4a1c bytes 20013fd6
- 004c4714 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c4714 ["INT_ADD", "register:40f0:8", ["const:4c4714:8", "const:4:8"]]
- 004c4714 ["CALLIND", null, ["register:0:8"]]
+ 004c4a34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c4a34 ["INT_ADD", "register:40f0:8", ["const:4c4a34:8", "const:4:8"]]
+ 004c4a34 ["CALLIND", null, ["register:0:8"]]
- 004c4714 bytes 00013fd6
+ 004c4a34 bytes 00013fd6
~~~


<a id="compare-57f9319f6a58aace543b1bd614e117ae"></a>

### [`004c57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md) → [`004c5af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5af0.md) _ZN5Botan15Buffered_Filter5writeEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f80.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c59f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f50.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c5830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c5830) · [`004c587c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c587c) · [`004c5898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c5898)
- 新版 [`004c5b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5af0.md#insn-004c5b50) · [`004c5b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5af0.md#insn-004c5b9c) · [`004c5bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5af0.md#insn-004c5bb8)

~~~diff
- 004c5830 ["INT_ADD", "register:40f0:8", ["const:4c5830:8", "const:4:8"]]
- 004c5830 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004c5b50 ["INT_ADD", "register:40f0:8", ["const:4c5b50:8", "const:4:8"]]
+ 004c5b50 ["CALL", null, ["callee:00c58fe0:8"]]
- 004c5830 bytes f8491e94
+ 004c5b50 bytes 244d1e94
- 004c587c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c587c ["INT_ADD", "register:40f0:8", ["const:4c587c:8", "const:4:8"]]
- 004c587c ["CALLIND", null, ["register:0:8"]]
+ 004c5b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5b9c ["INT_ADD", "register:40f0:8", ["const:4c5b9c:8", "const:4:8"]]
+ 004c5b9c ["CALLIND", null, ["register:0:8"]]
- 004c587c bytes 00013fd6
+ 004c5b9c bytes 00013fd6
- 004c5898 ["INT_ADD", "register:40f0:8", ["const:4c5898:8", "const:4:8"]]
- 004c5898 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004c5bb8 ["INT_ADD", "register:40f0:8", ["const:4c5bb8:8", "const:4:8"]]
+ 004c5bb8 ["CALL", null, ["callee:00c58fe0:8"]]
- 004c5898 bytes de491e94
+ 004c5bb8 bytes 0a4d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c858f0faac0e67983d278951cf3da8ca"></a>

### [`004c602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md) → [`004c634c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c634c.md) _ZN5Botan18Cipher_Mode_Filter14buffered_blockEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fa0.md) · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md)
- 新版 呼出元 1件 [`00c59f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f70.md) · 呼出先 2件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00543720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c605c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c605c) · [`004c6074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c6074) · [`004c6090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c6090)
- 新版 [`004c637c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c634c.md#insn-004c637c) · [`004c6394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c634c.md#insn-004c6394) · [`004c63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c634c.md#insn-004c63b0)

~~~diff
- 004c605c ["INT_ADD", "register:40f0:8", ["const:4c605c:8", "const:4:8"]]
- 004c605c ["CALL", null, ["callee:0054084c:8"]]
+ 004c637c ["INT_ADD", "register:40f0:8", ["const:4c637c:8", "const:4:8"]]
+ 004c637c ["CALL", null, ["callee:0054084c:8"]]
- 004c605c bytes 34e90194
+ 004c637c bytes 34e90194
- 004c6074 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6074 ["INT_ADD", "register:40f0:8", ["const:4c6074:8", "const:4:8"]]
- 004c6074 ["CALLIND", null, ["register:0:8"]]
+ 004c6394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6394 ["INT_ADD", "register:40f0:8", ["const:4c6394:8", "const:4:8"]]
+ 004c6394 ["CALLIND", null, ["register:0:8"]]
- 004c6074 bytes 00013fd6
+ 004c6394 bytes 00013fd6
- 004c6090 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6090 ["INT_ADD", "register:40f0:8", ["const:4c6090:8", "const:4:8"]]
- 004c6090 ["CALLIND", null, ["register:0:8"]]
+ 004c63b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c63b0 ["INT_ADD", "register:40f0:8", ["const:4c63b0:8", "const:4:8"]]
+ 004c63b0 ["CALLIND", null, ["register:0:8"]]
- 004c6090 bytes 00013fd6
+ 004c63b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e4790ebbc072e4ee96815f35325a06b"></a>

### [`004c67c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67c8.md) → [`004c6ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ae8.md) _ZN5Botan15DataSink_StreamD0Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c59000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c67d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67c8.md#insn-004c67d8)
- 新版 [`004c6af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ae8.md#insn-004c6af8)

~~~diff
- 004c67d8 ["INT_ADD", "register:40f0:8", ["const:4c67d8:8", "const:4:8"]]
- 004c67d8 ["CALL", null, ["callee:00c59fd0:8"]]
+ 004c6af8 ["INT_ADD", "register:40f0:8", ["const:4c6af8:8", "const:4:8"]]
+ 004c6af8 ["CALL", null, ["callee:00c59fd0:8"]]
- 004c67d8 bytes 0a4a1e94
+ 004c6af8 bytes 364d1e94
~~~


<a id="compare-f624cf949e6f4da22aab79067b5fe4e2"></a>

### [`004c67ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md) → [`004c6b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6b0c.md) _ZN5Botan6Filter4sendEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59010.md) · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c59fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fe0.md) · 呼出先 2件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c6858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c6858) · [`004c6874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c6874) · [`004c68c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c68c0)
- 新版 [`004c6b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6b0c.md#insn-004c6b78) · [`004c6b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6b0c.md#insn-004c6b94) · [`004c6be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6b0c.md#insn-004c6be0)

~~~diff
- 004c6858 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6858 ["INT_ADD", "register:40f0:8", ["const:4c6858:8", "const:4:8"]]
- 004c6858 ["CALLIND", null, ["register:0:8"]]
+ 004c6b78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6b78 ["INT_ADD", "register:40f0:8", ["const:4c6b78:8", "const:4:8"]]
+ 004c6b78 ["CALLIND", null, ["register:0:8"]]
- 004c6858 bytes 00013fd6
+ 004c6b78 bytes 00013fd6
- 004c6874 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6874 ["INT_ADD", "register:40f0:8", ["const:4c6874:8", "const:4:8"]]
- 004c6874 ["CALLIND", null, ["register:0:8"]]
+ 004c6b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6b94 ["INT_ADD", "register:40f0:8", ["const:4c6b94:8", "const:4:8"]]
+ 004c6b94 ["CALLIND", null, ["register:0:8"]]
- 004c6874 bytes 00013fd6
+ 004c6b94 bytes 00013fd6
- 004c68c0 ["INT_ADD", "register:40f0:8", ["const:4c68c0:8", "const:4:8"]]
- 004c68c0 ["CALL", null, ["callee:0054084c:8"]]
+ 004c6be0 ["INT_ADD", "register:40f0:8", ["const:4c6be0:8", "const:4:8"]]
+ 004c6be0 ["CALL", null, ["callee:0054084c:8"]]
- 004c68c0 bytes 1be70194
+ 004c6be0 bytes 1be70194
~~~


<a id="compare-02b1ff9fd73581410da5b86302ac4181"></a>

### [`004c6924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md) → [`004c6c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6c44.md) _ZN5Botan6Filter7new_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59020.md) · 呼出先 1件 [`00c59020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59020.md)
- 新版 呼出元 1件 [`00c59ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ff0.md) · 呼出先 1件 [`00c59ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md#insn-004c693c) · [`004c696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md#insn-004c696c)
- 新版 [`004c6c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6c44.md#insn-004c6c5c) · [`004c6c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6c44.md#insn-004c6c8c)

~~~diff
- 004c693c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c693c ["INT_ADD", "register:40f0:8", ["const:4c693c:8", "const:4:8"]]
- 004c693c ["CALLIND", null, ["register:0:8"]]
+ 004c6c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6c5c ["INT_ADD", "register:40f0:8", ["const:4c6c5c:8", "const:4:8"]]
+ 004c6c5c ["CALLIND", null, ["register:0:8"]]
- 004c693c bytes 00013fd6
+ 004c6c5c bytes 00013fd6
- 004c696c ["INT_ADD", "register:40f0:8", ["const:4c696c:8", "const:4:8"]]
- 004c696c ["CALL", null, ["callee:00c59ff0:8"]]
+ 004c6c8c ["INT_ADD", "register:40f0:8", ["const:4c6c8c:8", "const:4:8"]]
+ 004c6c8c ["CALL", null, ["callee:00c59ff0:8"]]
- 004c696c bytes ad491e94
+ 004c6c8c bytes d94c1e94
~~~


<a id="compare-147ac5ee95676d8ba475bdeb38c54562"></a>

### [`004c6984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md) → [`004c6ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ca4.md) _ZN5Botan6Filter10finish_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59030.md) · 呼出先 1件 [`00c59030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59030.md)
- 新版 呼出元 1件 [`00c5a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a000.md) · 呼出先 1件 [`00c5a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c699c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md#insn-004c699c) · [`004c69cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md#insn-004c69cc)
- 新版 [`004c6cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ca4.md#insn-004c6cbc) · [`004c6cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ca4.md#insn-004c6cec)

~~~diff
- 004c699c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c699c ["INT_ADD", "register:40f0:8", ["const:4c699c:8", "const:4:8"]]
- 004c699c ["CALLIND", null, ["register:0:8"]]
+ 004c6cbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6cbc ["INT_ADD", "register:40f0:8", ["const:4c6cbc:8", "const:4:8"]]
+ 004c6cbc ["CALLIND", null, ["register:0:8"]]
- 004c699c bytes 00013fd6
+ 004c6cbc bytes 00013fd6
- 004c69cc ["INT_ADD", "register:40f0:8", ["const:4c69cc:8", "const:4:8"]]
- 004c69cc ["CALL", null, ["callee:00c5a000:8"]]
+ 004c6cec ["INT_ADD", "register:40f0:8", ["const:4c6cec:8", "const:4:8"]]
+ 004c6cec ["CALL", null, ["callee:00c5a000:8"]]
- 004c69cc bytes 99491e94
+ 004c6cec bytes c54c1e94
~~~


<a id="compare-c142ea3a5503764620902dbcd7af6ec5"></a>

### [`004c77e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md) → [`004c7b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b08.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringESB_NS_10Cipher_DirE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7804) · [`004c7818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7818) · [`004c7838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7838)
- 新版 [`004c7b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b08.md#insn-004c7b24) · [`004c7b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b08.md#insn-004c7b38) · [`004c7b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b08.md#insn-004c7b58)

~~~diff
- 004c7804 ["INT_ADD", "register:40f0:8", ["const:4c7804:8", "const:4:8"]]
- 004c7804 ["CALL", null, ["callee:00c5a010:8"]]
+ 004c7b24 ["INT_ADD", "register:40f0:8", ["const:4c7b24:8", "const:4:8"]]
+ 004c7b24 ["CALL", null, ["callee:00c5a010:8"]]
- 004c7804 bytes 0f461e94
+ 004c7b24 bytes 3b491e94
- 004c7818 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c7818 ["INT_ADD", "register:40f0:8", ["const:4c7818:8", "const:4:8"]]
- 004c7818 ["CALLIND", null, ["register:0:8"]]
+ 004c7b38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7b38 ["INT_ADD", "register:40f0:8", ["const:4c7b38:8", "const:4:8"]]
+ 004c7b38 ["CALLIND", null, ["register:0:8"]]
- 004c7818 bytes 00013fd6
+ 004c7b38 bytes 00013fd6
- 004c7838 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c7838 ["INT_ADD", "register:40f0:8", ["const:4c7838:8", "const:4:8"]]
- 004c7838 ["CALLIND", null, ["register:0:8"]]
+ 004c7b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7b58 ["INT_ADD", "register:40f0:8", ["const:4c7b58:8", "const:4:8"]]
+ 004c7b58 ["CALLIND", null, ["register:0:8"]]
- 004c7838 bytes 00013fd6
+ 004c7b58 bytes 00013fd6
~~~


<a id="compare-53fc4bea3790706498c67cfd539cecd6"></a>

### [`004c7850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md) → [`004c7b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b70.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringENS_10Cipher_DirE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md#insn-004c7864) · [`004c7878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md#insn-004c7878)
- 新版 [`004c7b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b70.md#insn-004c7b84) · [`004c7b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7b70.md#insn-004c7b98)

~~~diff
- 004c7864 ["INT_ADD", "register:40f0:8", ["const:4c7864:8", "const:4:8"]]
- 004c7864 ["CALL", null, ["callee:00c5a010:8"]]
+ 004c7b84 ["INT_ADD", "register:40f0:8", ["const:4c7b84:8", "const:4:8"]]
+ 004c7b84 ["CALL", null, ["callee:00c5a010:8"]]
- 004c7864 bytes f7451e94
+ 004c7b84 bytes 23491e94
- 004c7878 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c7878 ["INT_ADD", "register:40f0:8", ["const:4c7878:8", "const:4:8"]]
- 004c7878 ["CALLIND", null, ["register:0:8"]]
+ 004c7b98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7b98 ["INT_ADD", "register:40f0:8", ["const:4c7b98:8", "const:4:8"]]
+ 004c7b98 ["CALLIND", null, ["register:0:8"]]
- 004c7878 bytes 00013fd6
+ 004c7b98 bytes 00013fd6
~~~


<a id="compare-9b2337b5378b7bdecfbe73e1c7077bbc"></a>

### [`004c79b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md) → [`004c7cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7cd0.md) _ZNK5Botan11SecureQueue4peekEPhmm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590d0.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5a0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0a0.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md#insn-004c7a48) · [`004c7aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md#insn-004c7aa0)
- 新版 [`004c7d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7cd0.md#insn-004c7d68) · [`004c7dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7cd0.md#insn-004c7dc0)

~~~diff
- 004c7a48 ["INT_ADD", "register:40f0:8", ["const:4c7a48:8", "const:4:8"]]
- 004c7a48 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004c7d68 ["INT_ADD", "register:40f0:8", ["const:4c7d68:8", "const:4:8"]]
+ 004c7d68 ["CALL", null, ["callee:00c58fe0:8"]]
- 004c7a48 bytes 72411e94
+ 004c7d68 bytes 9e441e94
- 004c7aa0 ["INT_ADD", "register:40f0:8", ["const:4c7aa0:8", "const:4:8"]]
- 004c7aa0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004c7dc0 ["INT_ADD", "register:40f0:8", ["const:4c7dc0:8", "const:4:8"]]
+ 004c7dc0 ["CALL", null, ["callee:00c58fe0:8"]]
- 004c7aa0 bytes 5c411e94
+ 004c7dc0 bytes 88441e94
~~~


<a id="compare-0e424417b72b442f23a9dd0ae184d839"></a>

### [`004c7c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md) → [`004c7f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7f84.md) FUN_004c7f84

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00530b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md#insn-004c7c80)
- 新版 [`004c7fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7f84.md#insn-004c7fa0)

~~~diff
- 004c7c80 ["INT_ADD", "register:40f0:8", ["const:4c7c80:8", "const:4:8"]]
- 004c7c80 ["CALL", null, ["callee:00530b2c:8"]]
+ 004c7fa0 ["INT_ADD", "register:40f0:8", ["const:4c7fa0:8", "const:4:8"]]
+ 004c7fa0 ["CALL", null, ["callee:00530b2c:8"]]
- 004c7c80 bytes e3a20194
+ 004c7fa0 bytes e3a20194
~~~


<a id="compare-7b8202ec439db5304a69026f326341c1"></a>

### [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) → [`004c7fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md) FUN_004c7fc0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md) · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004c8b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8b78.md) · 呼出先 2件 [`00530b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7ccc) · [`004c7cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7cd4) · [`004c7d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7d88)
- 新版 [`004c7fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md#insn-004c7fec) · [`004c7ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md#insn-004c7ff4) · [`004c80a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md#insn-004c80a8)

~~~diff
- 004c7ccc ["INT_ADD", "register:40f0:8", ["const:4c7ccc:8", "const:4:8"]]
- 004c7ccc ["CALL", null, ["callee:00530b2c:8"]]
+ 004c7fec ["INT_ADD", "register:40f0:8", ["const:4c7fec:8", "const:4:8"]]
+ 004c7fec ["CALL", null, ["callee:00530b2c:8"]]
- 004c7ccc bytes d0a20194
+ 004c7fec bytes d0a20194
- 004c7cd4 ["INT_ADD", "register:40f0:8", ["const:4c7cd4:8", "const:4:8"]]
- 004c7cd4 ["CALL", null, ["callee:00c58f50:8"]]
+ 004c7ff4 ["INT_ADD", "register:40f0:8", ["const:4c7ff4:8", "const:4:8"]]
+ 004c7ff4 ["CALL", null, ["callee:00c58f50:8"]]
- 004c7cd4 bytes ab401e94
+ 004c7ff4 bytes d7431e94
- 004c7d88 ["INT_ADD", "register:40f0:8", ["const:4c7d88:8", "const:4:8"]]
- 004c7d88 ["CALL", null, ["callee:00c58f50:8"]]
+ 004c80a8 ["INT_ADD", "register:40f0:8", ["const:4c80a8:8", "const:4:8"]]
+ 004c80a8 ["CALL", null, ["callee:00c58f50:8"]]
- 004c7d88 bytes 7e401e94
+ 004c80a8 bytes aa431e94
~~~


<a id="compare-89f6eb4c366ea1c8b861d3debe5aeb32"></a>

### [`004c8150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8150.md) → [`004c8470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8470.md) FUN_004c8470

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054486c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/0054486c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00544b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c816c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8150.md#insn-004c816c)
- 新版 [`004c848c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8470.md#insn-004c848c)

~~~diff
- 004c816c ["INT_ADD", "register:40f0:8", ["const:4c816c:8", "const:4:8"]]
- 004c816c ["CALL", null, ["callee:00544b8c:8"]]
+ 004c848c ["INT_ADD", "register:40f0:8", ["const:4c848c:8", "const:4:8"]]
+ 004c848c ["CALL", null, ["callee:00544b8c:8"]]
- 004c816c bytes c0f10194
+ 004c848c bytes c0f10194
~~~


<a id="compare-82064a74baa6d661420e8c0169cdce0c"></a>

### [`004c818c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md) → [`004c84ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84ac.md) _ZN5Botan4PipeD2Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59100.md) · 呼出先 3件 [`0054486c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/0054486c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)
- 新版 呼出元 1件 [`00c5a0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0d0.md) · 呼出先 3件 [`00544b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5a0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c81a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md#insn-004c81a0) · [`004c81b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md#insn-004c81b4)
- 新版 [`004c84c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84ac.md#insn-004c84c0) · [`004c84d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84ac.md#insn-004c84d4)

~~~diff
- 004c81a0 ["INT_ADD", "register:40f0:8", ["const:4c81a0:8", "const:4:8"]]
- 004c81a0 ["CALL", null, ["callee:00c5a0c0:8"]]
+ 004c84c0 ["INT_ADD", "register:40f0:8", ["const:4c84c0:8", "const:4:8"]]
+ 004c84c0 ["CALL", null, ["callee:00c5a0c0:8"]]
- 004c81a0 bytes d4431e94
+ 004c84c0 bytes 00471e94
- 004c81b4 ["INT_ADD", "register:40f0:8", ["const:4c81b4:8", "const:4:8"]]
- 004c81b4 ["CALL", null, ["callee:00544b8c:8"]]
+ 004c84d4 ["INT_ADD", "register:40f0:8", ["const:4c84d4:8", "const:4:8"]]
+ 004c84d4 ["CALL", null, ["callee:00544b8c:8"]]
- 004c81b4 bytes aef10194
+ 004c84d4 bytes aef10194
~~~


<a id="compare-a52ee2ae6b5240f0ffa99806ce62714e"></a>

### [`004c8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8268.md) → [`004c8588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8588.md) _ZN5Botan4PipeD0Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c59100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5a0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8268.md#insn-004c8278)
- 新版 [`004c8598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8588.md#insn-004c8598)

~~~diff
- 004c8278 ["INT_ADD", "register:40f0:8", ["const:4c8278:8", "const:4:8"]]
- 004c8278 ["CALL", null, ["callee:00c5a0d0:8"]]
+ 004c8598 ["INT_ADD", "register:40f0:8", ["const:4c8598:8", "const:4:8"]]
+ 004c8598 ["CALL", null, ["callee:00c5a0d0:8"]]
- 004c8278 bytes a2431e94
+ 004c8598 bytes ce461e94
~~~


<a id="compare-574651426908c9a1d348fa7ee75f4636"></a>

### [`004c828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c828c.md) → [`004c85ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85ac.md) _ZN5Botan4Pipe5resetEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c82a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c828c.md#insn-004c82a0)
- 新版 [`004c85c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85ac.md#insn-004c85c0)

~~~diff
- 004c82a0 ["INT_ADD", "register:40f0:8", ["const:4c82a0:8", "const:4:8"]]
- 004c82a0 ["CALL", null, ["callee:00c5a0c0:8"]]
+ 004c85c0 ["INT_ADD", "register:40f0:8", ["const:4c85c0:8", "const:4:8"]]
+ 004c85c0 ["CALL", null, ["callee:00c5a0c0:8"]]
- 004c82a0 bytes 94431e94
+ 004c85c0 bytes c0461e94
~~~


<a id="compare-3d32608184d809141a9f81d9888ecd35"></a>

### [`004c82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82b8.md) → [`004c85d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85d8.md) _ZNK5Botan4Pipe11end_of_dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c82c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82b8.md#insn-004c82c4)
- 新版 [`004c85e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85d8.md#insn-004c85e4)

~~~diff
- 004c82c4 ["INT_ADD", "register:40f0:8", ["const:4c82c4:8", "const:4:8"]]
- 004c82c4 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 004c85e4 ["INT_ADD", "register:40f0:8", ["const:4c85e4:8", "const:4:8"]]
+ 004c85e4 ["CALL", null, ["callee:00c5a0e0:8"]]
- 004c82c4 bytes 93431e94
+ 004c85e4 bytes bf461e94
~~~


<a id="compare-78ab27e5050032d7027f99539b33559f"></a>

### [`004c856c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md) → [`004c888c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c888c.md) _ZN5Botan4Pipe11process_msgEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md) [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md#insn-004c8588) · [`004c8598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md#insn-004c8598)
- 新版 [`004c88a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c888c.md#insn-004c88a8) · [`004c88b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c888c.md#insn-004c88b8)

~~~diff
- 004c8588 ["INT_ADD", "register:40f0:8", ["const:4c8588:8", "const:4:8"]]
- 004c8588 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 004c88a8 ["INT_ADD", "register:40f0:8", ["const:4c88a8:8", "const:4:8"]]
+ 004c88a8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 004c8588 bytes e6421e94
+ 004c88a8 bytes 12461e94
- 004c8598 ["INT_ADD", "register:40f0:8", ["const:4c8598:8", "const:4:8"]]
- 004c8598 ["CALL", null, ["callee:00c5a100:8"]]
+ 004c88b8 ["INT_ADD", "register:40f0:8", ["const:4c88b8:8", "const:4:8"]]
+ 004c88b8 ["CALL", null, ["callee:00c5a100:8"]]
- 004c8598 bytes e6421e94
+ 004c88b8 bytes 12461e94
~~~


<a id="compare-0c708b20491b253425b0e91987bd24c3"></a>

### [`004c89e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md) → [`004c8d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d04.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md) [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md#insn-004c8a00) · [`004c8a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md#insn-004c8a10)
- 新版 [`004c8d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d04.md#insn-004c8d20) · [`004c8d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d04.md#insn-004c8d30)

~~~diff
- 004c8a00 ["INT_ADD", "register:40f0:8", ["const:4c8a00:8", "const:4:8"]]
- 004c8a00 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 004c8d20 ["INT_ADD", "register:40f0:8", ["const:4c8d20:8", "const:4:8"]]
+ 004c8d20 ["CALL", null, ["callee:00c5a0f0:8"]]
- 004c8a00 bytes c8411e94
+ 004c8d20 bytes f4441e94
- 004c8a10 ["INT_ADD", "register:40f0:8", ["const:4c8a10:8", "const:4:8"]]
- 004c8a10 ["CALL", null, ["callee:00c5a100:8"]]
+ 004c8d30 ["INT_ADD", "register:40f0:8", ["const:4c8d30:8", "const:4:8"]]
+ 004c8d30 ["CALL", null, ["callee:00c5a100:8"]]
- 004c8a10 bytes c8411e94
+ 004c8d30 bytes f4441e94
~~~


<a id="compare-a4af07c17895fa0618d9f9f3059e4c16"></a>

### [`004c8a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md) → [`004c8d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d48.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md) [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md#insn-004c8a44) · [`004c8a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md#insn-004c8a54)
- 新版 [`004c8d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d48.md#insn-004c8d64) · [`004c8d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d48.md#insn-004c8d74)

~~~diff
- 004c8a44 ["INT_ADD", "register:40f0:8", ["const:4c8a44:8", "const:4:8"]]
- 004c8a44 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 004c8d64 ["INT_ADD", "register:40f0:8", ["const:4c8d64:8", "const:4:8"]]
+ 004c8d64 ["CALL", null, ["callee:00c5a0f0:8"]]
- 004c8a44 bytes b7411e94
+ 004c8d64 bytes e3441e94
- 004c8a54 ["INT_ADD", "register:40f0:8", ["const:4c8a54:8", "const:4:8"]]
- 004c8a54 ["CALL", null, ["callee:00c5a100:8"]]
+ 004c8d74 ["INT_ADD", "register:40f0:8", ["const:4c8d74:8", "const:4:8"]]
+ 004c8d74 ["CALL", null, ["callee:00c5a100:8"]]
- 004c8a54 bytes b7411e94
+ 004c8d74 bytes e3441e94
~~~


<a id="compare-669ce5c27577d7ef32f7375c34a65c3c"></a>

### [`004c8a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md) → [`004c8d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d8c.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md) [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md#insn-004c8a98) · [`004c8aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md#insn-004c8aa8)
- 新版 [`004c8db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d8c.md#insn-004c8db8) · [`004c8dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8d8c.md#insn-004c8dc8)

~~~diff
- 004c8a98 ["INT_ADD", "register:40f0:8", ["const:4c8a98:8", "const:4:8"]]
- 004c8a98 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 004c8db8 ["INT_ADD", "register:40f0:8", ["const:4c8db8:8", "const:4:8"]]
+ 004c8db8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 004c8a98 bytes a2411e94
+ 004c8db8 bytes ce441e94
- 004c8aa8 ["INT_ADD", "register:40f0:8", ["const:4c8aa8:8", "const:4:8"]]
- 004c8aa8 ["CALL", null, ["callee:00c5a100:8"]]
+ 004c8dc8 ["INT_ADD", "register:40f0:8", ["const:4c8dc8:8", "const:4:8"]]
+ 004c8dc8 ["CALL", null, ["callee:00c5a100:8"]]
- 004c8aa8 bytes a2411e94
+ 004c8dc8 bytes ce441e94
~~~


<a id="compare-43adc252d0c590d88b83d8fefba9e473"></a>

### [`004c8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md) → [`004c8de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8de0.md) _ZN5Botan4Pipe11process_msgERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md) [`00c59170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md) [`00c5a140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md#insn-004c8ad4) · [`004c8ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md#insn-004c8ae0)
- 新版 [`004c8df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8de0.md#insn-004c8df4) · [`004c8e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8de0.md#insn-004c8e00)

~~~diff
- 004c8ad4 ["INT_ADD", "register:40f0:8", ["const:4c8ad4:8", "const:4:8"]]
- 004c8ad4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 004c8df4 ["INT_ADD", "register:40f0:8", ["const:4c8df4:8", "const:4:8"]]
+ 004c8df4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 004c8ad4 bytes 93411e94
+ 004c8df4 bytes bf441e94
- 004c8ae0 ["INT_ADD", "register:40f0:8", ["const:4c8ae0:8", "const:4:8"]]
- 004c8ae0 ["CALL", null, ["callee:00c5a140:8"]]
+ 004c8e00 ["INT_ADD", "register:40f0:8", ["const:4c8e00:8", "const:4:8"]]
+ 004c8e00 ["CALL", null, ["callee:00c5a140:8"]]
- 004c8ae0 bytes a4411e94
+ 004c8e00 bytes d0441e94
~~~


<a id="compare-e15e433a2f8286ca34e94bb5881cae54"></a>

### [`004c9970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md) → [`004c9c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9c90.md) _ZN5Botan4Pipe5writeEh

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md#insn-004c9998) · [`004c99bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md#insn-004c99bc)
- 新版 [`004c9cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9c90.md#insn-004c9cb8) · [`004c9cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9c90.md#insn-004c9cdc)

~~~diff
- 004c9998 ["INT_ADD", "register:40f0:8", ["const:4c9998:8", "const:4:8"]]
- 004c9998 ["CALL", null, ["callee:00c5a100:8"]]
+ 004c9cb8 ["INT_ADD", "register:40f0:8", ["const:4c9cb8:8", "const:4:8"]]
+ 004c9cb8 ["CALL", null, ["callee:00c5a100:8"]]
- 004c9998 bytes e63d1e94
+ 004c9cb8 bytes 12411e94
- 004c99bc ["INT_ADD", "register:40f0:8", ["const:4c99bc:8", "const:4:8"]]
- 004c99bc ["CALL", null, ["callee:00c58f80:8"]]
+ 004c9cdc ["INT_ADD", "register:40f0:8", ["const:4c9cdc:8", "const:4:8"]]
+ 004c9cdc ["CALL", null, ["callee:00c58f80:8"]]
- 004c99bc bytes 7d391e94
+ 004c9cdc bytes a93c1e94
~~~


<a id="compare-2afa2e1f9d60227b7edc2e994a6c37b0"></a>

### [`004c9b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md) → [`004c9e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9e3c.md) _ZN5Botan4Pipe8read_allEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md) [`00c59190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59190.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c5a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0e0.md) [`00c5a160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b44) · [`004c9b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b50) · [`004c9b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b64)
- 新版 [`004c9e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9e3c.md#insn-004c9e64) · [`004c9e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9e3c.md#insn-004c9e70) · [`004c9e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9e3c.md#insn-004c9e84)

~~~diff
- 004c9b44 ["INT_ADD", "register:40f0:8", ["const:4c9b44:8", "const:4:8"]]
- 004c9b44 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 004c9e64 ["INT_ADD", "register:40f0:8", ["const:4c9e64:8", "const:4:8"]]
+ 004c9e64 ["CALL", null, ["callee:00c5a0e0:8"]]
- 004c9b44 bytes 733d1e94
+ 004c9e64 bytes 9f401e94
- 004c9b50 ["INT_ADD", "register:40f0:8", ["const:4c9b50:8", "const:4:8"]]
- 004c9b50 ["CALL", null, ["callee:004b3868:8"]]
+ 004c9e70 ["INT_ADD", "register:40f0:8", ["const:4c9e70:8", "const:4:8"]]
+ 004c9e70 ["CALL", null, ["callee:004b3868:8"]]
- 004c9b50 bytes 7ea6ff97
+ 004c9e70 bytes 7ea6ff97
- 004c9b64 ["INT_ADD", "register:40f0:8", ["const:4c9b64:8", "const:4:8"]]
- 004c9b64 ["CALL", null, ["callee:00c5a160:8"]]
+ 004c9e84 ["INT_ADD", "register:40f0:8", ["const:4c9e84:8", "const:4:8"]]
+ 004c9e84 ["CALL", null, ["callee:00c5a160:8"]]
- 004c9b64 bytes 8b3d1e94
+ 004c9e84 bytes b7401e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a9bdc70cd460b98295b6636b6dd62e"></a>

### [`004c9fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9fc8.md) → [`004ca2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004ca2e8.md) _ZN5Botan4Pipe15check_availableEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9fc8.md#insn-004c9fe0)
- 新版 [`004ca300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004ca2e8.md#insn-004ca300)

~~~diff
- 004c9fe0 ["INT_ADD", "register:40f0:8", ["const:4c9fe0:8", "const:4:8"]]
- 004c9fe0 ["CALL", null, ["callee:00c5a0e0:8"]]
+ 004ca300 ["INT_ADD", "register:40f0:8", ["const:4ca300:8", "const:4:8"]]
+ 004ca300 ["CALL", null, ["callee:00c5a0e0:8"]]
- 004c9fe0 bytes 4c3c1e94
+ 004ca300 bytes 783f1e94
~~~


<a id="compare-afd032dbf9855f911f10a6f15769d48b"></a>

### [`004c9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9ff8.md) → [`004ca318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004ca318.md) _ZN5Botan4Pipe19check_available_msgEmm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ca00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9ff8.md#insn-004ca00c)
- 新版 [`004ca32c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004ca318.md#insn-004ca32c)

~~~diff
- 004ca00c ["INT_ADD", "register:40f0:8", ["const:4ca00c:8", "const:4:8"]]
- 004ca00c ["CALL", null, ["callee:00c5a0e0:8"]]
+ 004ca32c ["INT_ADD", "register:40f0:8", ["const:4ca32c:8", "const:4:8"]]
+ 004ca32c ["CALL", null, ["callee:00c5a0e0:8"]]
- 004ca00c bytes 413c1e94
+ 004ca32c bytes 6d3f1e94
~~~


<a id="compare-96900627bb3aeea65d0cc5f2ac668f25"></a>

### [`004cabd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md) → [`004caef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caef4.md) FUN_004caef4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cabf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cabf0) · [`004cabf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cabf8) · [`004cac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cac00)
- 新版 [`004caf10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caef4.md#insn-004caf10) · [`004caf18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caef4.md#insn-004caf18) · [`004caf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caef4.md#insn-004caf20)

~~~diff
- 004cabf0 ["INT_ADD", "register:40f0:8", ["const:4cabf0:8", "const:4:8"]]
- 004cabf0 ["CALL", null, ["callee:00c59170:8"]]
+ 004caf10 ["INT_ADD", "register:40f0:8", ["const:4caf10:8", "const:4:8"]]
+ 004caf10 ["CALL", null, ["callee:00c59170:8"]]
- 004cabf0 bytes 6c351e94
+ 004caf10 bytes 98381e94
- 004cabf8 ["INT_ADD", "register:40f0:8", ["const:4cabf8:8", "const:4:8"]]
- 004cabf8 ["CALL", null, ["callee:00c58f00:8"]]
+ 004caf18 ["INT_ADD", "register:40f0:8", ["const:4caf18:8", "const:4:8"]]
+ 004caf18 ["CALL", null, ["callee:00c58f00:8"]]
- 004cabf8 bytes ce341e94
+ 004caf18 bytes fa371e94
- 004cac00 ["INT_ADD", "register:40f0:8", ["const:4cac00:8", "const:4:8"]]
- 004cac00 ["CALL", null, ["callee:00c59170:8"]]
+ 004caf20 ["INT_ADD", "register:40f0:8", ["const:4caf20:8", "const:4:8"]]
+ 004caf20 ["CALL", null, ["callee:00c59170:8"]]
- 004cac00 bytes 68351e94
+ 004caf20 bytes 94381e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d00a2184ad10412d91eed1a9baf9fd16"></a>

### [`004cac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md) → [`004caf48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caf48.md) FUN_004caf48

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac74) · [`004cac88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac88) · [`004cac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac90)
- 新版 [`004caf94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caf48.md#insn-004caf94) · [`004cafa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caf48.md#insn-004cafa8) · [`004cafb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004caf48.md#insn-004cafb0)

~~~diff
- 004cac74 ["INT_ADD", "register:40f0:8", ["const:4cac74:8", "const:4:8"]]
- 004cac74 ["CALL", null, ["callee:00c54d90:8"]]
+ 004caf94 ["INT_ADD", "register:40f0:8", ["const:4caf94:8", "const:4:8"]]
+ 004caf94 ["CALL", null, ["callee:00c54d90:8"]]
- 004cac74 bytes 4b241e94
+ 004caf94 bytes 7f271e94
- 004cac88 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cac88 ["INT_ADD", "register:40f0:8", ["const:4cac88:8", "const:4:8"]]
- 004cac88 ["CALLIND", null, ["register:0:8"]]
+ 004cafa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cafa8 ["INT_ADD", "register:40f0:8", ["const:4cafa8:8", "const:4:8"]]
+ 004cafa8 ["CALLIND", null, ["register:0:8"]]
- 004cac88 bytes 00013fd6
+ 004cafa8 bytes 00013fd6
- 004cac90 ["INT_ADD", "register:40f0:8", ["const:4cac90:8", "const:4:8"]]
- 004cac90 ["CALL", null, ["callee:00c58f20:8"]]
+ 004cafb0 ["INT_ADD", "register:40f0:8", ["const:4cafb0:8", "const:4:8"]]
+ 004cafb0 ["CALL", null, ["callee:00c58f20:8"]]
- 004cac90 bytes b0341e94
+ 004cafb0 bytes dc371e94
~~~


<a id="compare-8014bc84ce6d65d7c2a5f446e449065c"></a>

### [`004caf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004caf94.md) → [`004cb2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb2b4.md) _ZN5Botan13Threaded_ForkD0Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c591f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5a1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cafa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004caf94.md#insn-004cafa4)
- 新版 [`004cb2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb2b4.md#insn-004cb2c4)

~~~diff
- 004cafa4 ["INT_ADD", "register:40f0:8", ["const:4cafa4:8", "const:4:8"]]
- 004cafa4 ["CALL", null, ["callee:00c5a1c0:8"]]
+ 004cb2c4 ["INT_ADD", "register:40f0:8", ["const:4cb2c4:8", "const:4:8"]]
+ 004cb2c4 ["CALL", null, ["callee:00c5a1c0:8"]]
- 004cafa4 bytes 93381e94
+ 004cb2c4 bytes bf3b1e94
~~~


<a id="compare-63a62b723084cac5635bdf8ae63f3170"></a>

### [`004cafe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md) → [`004cb300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb300.md) FUN_004cb300

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ca9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004ca9b0.md) · 呼出先 5件 [`005449f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004cacd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004cacd0.md) · 呼出先 5件 [`00544d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544d10.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb024) · [`004cb078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb078) · [`004cb08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb08c)
- 新版 [`004cb344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb300.md#insn-004cb344) · [`004cb398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb300.md#insn-004cb398) · [`004cb3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb300.md#insn-004cb3ac)

~~~diff
- 004cb024 ["INT_ADD", "register:40f0:8", ["const:4cb024:8", "const:4:8"]]
- 004cb024 ["CALL", null, ["callee:00c58f30:8"]]
+ 004cb344 ["INT_ADD", "register:40f0:8", ["const:4cb344:8", "const:4:8"]]
+ 004cb344 ["CALL", null, ["callee:00c58f30:8"]]
- 004cb024 bytes cf331e94
+ 004cb344 bytes fb361e94
- 004cb078 ["INT_ADD", "register:40f0:8", ["const:4cb078:8", "const:4:8"]]
- 004cb078 ["CALL", null, ["callee:00c54d90:8"]]
+ 004cb398 ["INT_ADD", "register:40f0:8", ["const:4cb398:8", "const:4:8"]]
+ 004cb398 ["CALL", null, ["callee:00c54d90:8"]]
- 004cb078 bytes 4a231e94
+ 004cb398 bytes 7e261e94
- 004cb08c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb08c ["INT_ADD", "register:40f0:8", ["const:4cb08c:8", "const:4:8"]]
- 004cb08c ["CALLIND", null, ["register:0:8"]]
+ 004cb3ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb3ac ["INT_ADD", "register:40f0:8", ["const:4cb3ac:8", "const:4:8"]]
+ 004cb3ac ["CALLIND", null, ["register:0:8"]]
- 004cb08c bytes 00013fd6
+ 004cb3ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde45f746dbc8c0dbb9496cee08ad1e5"></a>

### [`004cb0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md) → [`004cb408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb408.md) _ZN5Botan13Threaded_Fork12thread_entryEPNS_6FilterE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ca9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004ca9b0.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)
- 新版 呼出元 1件 [`004cacd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004cacd0.md) · 呼出先 5件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md) [`00c59520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb130) · [`004cb138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb138) · [`004cb14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb14c)
- 新版 [`004cb450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb408.md#insn-004cb450) · [`004cb458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb408.md#insn-004cb458) · [`004cb46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb408.md#insn-004cb46c)

~~~diff
- 004cb130 ["INT_ADD", "register:40f0:8", ["const:4cb130:8", "const:4:8"]]
- 004cb130 ["CALL", null, ["callee:00c59420:8"]]
+ 004cb450 ["INT_ADD", "register:40f0:8", ["const:4cb450:8", "const:4:8"]]
+ 004cb450 ["CALL", null, ["callee:00c59420:8"]]
- 004cb130 bytes c8341e94
+ 004cb450 bytes f4371e94
- 004cb138 ["INT_ADD", "register:40f0:8", ["const:4cb138:8", "const:4:8"]]
- 004cb138 ["CALL", null, ["callee:00c59190:8"]]
+ 004cb458 ["INT_ADD", "register:40f0:8", ["const:4cb458:8", "const:4:8"]]
+ 004cb458 ["CALL", null, ["callee:00c59190:8"]]
- 004cb138 bytes 22341e94
+ 004cb458 bytes 4e371e94
- 004cb14c ["INT_ADD", "register:40f0:8", ["const:4cb14c:8", "const:4:8"]]
- 004cb14c ["CALL", null, ["callee:00c59180:8"]]
+ 004cb46c ["INT_ADD", "register:40f0:8", ["const:4cb46c:8", "const:4:8"]]
+ 004cb46c ["CALL", null, ["callee:00c59180:8"]]
- 004cb14c bytes 19341e94
+ 004cb46c bytes 45371e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2bd4d4db901c37e289964834e8577d9"></a>

### [`004cb340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md) → [`004cb660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb660.md) FUN_004cb660

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md#insn-004cb35c) · [`004cb37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md#insn-004cb37c)
- 新版 [`004cb67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb660.md#insn-004cb67c) · [`004cb69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb660.md#insn-004cb69c)

~~~diff
- 004cb35c ["INT_ADD", "register:40f0:8", ["const:4cb35c:8", "const:4:8"]]
- 004cb35c ["CALL", null, ["callee:00c54d90:8"]]
+ 004cb67c ["INT_ADD", "register:40f0:8", ["const:4cb67c:8", "const:4:8"]]
+ 004cb67c ["CALL", null, ["callee:00c54d90:8"]]
- 004cb35c bytes 91221e94
+ 004cb67c bytes c5251e94
- 004cb37c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb37c ["INT_ADD", "register:40f0:8", ["const:4cb37c:8", "const:4:8"]]
- 004cb37c ["CALLIND", null, ["register:0:8"]]
+ 004cb69c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb69c ["INT_ADD", "register:40f0:8", ["const:4cb69c:8", "const:4:8"]]
+ 004cb69c ["CALLIND", null, ["register:0:8"]]
- 004cb37c bytes 00013fd6
+ 004cb69c bytes 00013fd6
~~~


