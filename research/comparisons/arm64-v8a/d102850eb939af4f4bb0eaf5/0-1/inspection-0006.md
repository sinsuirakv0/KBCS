# v16.0.1 → v16.0.2 · 要調査の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-15d2dc8007cc9641f537234e094a2e49"></a>

### [`004af418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af418.md) → [`004af458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af458.md) _ZN5BotanleERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af418.md#insn-004af420)
- 新版 [`004af460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af458.md#insn-004af460)

~~~diff
- 004af420 ["INT_ADD", "register:40f0:8", ["const:4af420:8", "const:4:8"]]
- 004af420 ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af460 ["INT_ADD", "register:40f0:8", ["const:4af460:8", "const:4:8"]]
+ 004af460 ["CALL", null, ["callee:00c58ab0:8"]]
- 004af420 bytes 70a51e94
+ 004af460 bytes 94a51e94
~~~


<a id="compare-10956457a23d77d8867647872fbf3165"></a>

### [`004af434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af434.md) → [`004af474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af474.md) _ZN5BotangeERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af434.md#insn-004af43c)
- 新版 [`004af47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af474.md#insn-004af47c)

~~~diff
- 004af43c ["INT_ADD", "register:40f0:8", ["const:4af43c:8", "const:4:8"]]
- 004af43c ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af47c ["INT_ADD", "register:40f0:8", ["const:4af47c:8", "const:4:8"]]
+ 004af47c ["CALL", null, ["callee:00c58ab0:8"]]
- 004af43c bytes 69a51e94
+ 004af47c bytes 8da51e94
~~~


<a id="compare-ba1207db1eed48126ac551ebea3ceb73"></a>

### [`004af450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af450.md) → [`004af490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af490.md) _ZN5BotanltERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af450.md#insn-004af458)
- 新版 [`004af498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af490.md#insn-004af498)

~~~diff
- 004af458 ["INT_ADD", "register:40f0:8", ["const:4af458:8", "const:4:8"]]
- 004af458 ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af498 ["INT_ADD", "register:40f0:8", ["const:4af498:8", "const:4:8"]]
+ 004af498 ["CALL", null, ["callee:00c58ab0:8"]]
- 004af458 bytes 62a51e94
+ 004af498 bytes 86a51e94
~~~


<a id="compare-78103123bc75ee5ecb0259786059c22e"></a>

### [`004af468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af468.md) → [`004af4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4a8.md) _ZN5BotangtERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af468.md#insn-004af470)
- 新版 [`004af4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4a8.md#insn-004af4b0)

~~~diff
- 004af470 ["INT_ADD", "register:40f0:8", ["const:4af470:8", "const:4:8"]]
- 004af470 ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af4b0 ["INT_ADD", "register:40f0:8", ["const:4af4b0:8", "const:4:8"]]
+ 004af4b0 ["CALL", null, ["callee:00c58ab0:8"]]
- 004af470 bytes 5ca51e94
+ 004af4b0 bytes 80a51e94
~~~


<a id="compare-57f18e0ca67c7de82123e296db831c37"></a>

### [`004af850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af850.md) → [`004af890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af890.md) _ZNK5Botan11BER_Decoder10more_itemsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af850.md#insn-004af86c)
- 新版 [`004af8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af890.md#insn-004af8ac)

~~~diff
- 004af86c ["COPY", "register:0:8", ["register:4040:8"]]
- 004af86c ["INT_ADD", "register:40f0:8", ["const:4af86c:8", "const:4:8"]]
- 004af86c ["CALLIND", null, ["register:0:8"]]
+ 004af8ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af8ac ["INT_ADD", "register:40f0:8", ["const:4af8ac:8", "const:4:8"]]
+ 004af8ac ["CALLIND", null, ["register:0:8"]]
- 004af86c bytes 00013fd6
+ 004af8ac bytes 00013fd6
~~~


<a id="compare-5611887e21c03aeb666a5f08bfb365c8"></a>

### [`004af9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af9b4.md) → [`004af9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md) _ZN5Botan11BER_Decoder17discard_remainingEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af9b4.md#insn-004af9e8) · [`004afa14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af9b4.md#insn-004afa14)
- 新版 [`004afa28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md#insn-004afa28) · [`004afa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af9f4.md#insn-004afa54)

~~~diff
- 004af9e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004af9e8 ["INT_ADD", "register:40f0:8", ["const:4af9e8:8", "const:4:8"]]
- 004af9e8 ["CALLIND", null, ["register:0:8"]]
+ 004afa28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004afa28 ["INT_ADD", "register:40f0:8", ["const:4afa28:8", "const:4:8"]]
+ 004afa28 ["CALLIND", null, ["register:0:8"]]
- 004af9e8 bytes 00013fd6
+ 004afa28 bytes 00013fd6
- 004afa14 ["INT_ADD", "register:40f0:8", ["const:4afa14:8", "const:4:8"]]
- 004afa14 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004afa54 ["INT_ADD", "register:40f0:8", ["const:4afa54:8", "const:4:8"]]
+ 004afa54 ["CALL", null, ["callee:00c57fb0:8"]]
- 004afa14 bytes 33a11e94
+ 004afa54 bytes 57a11e94
~~~


<a id="compare-e2c8edd47cb1f72c7cd0db2b9ce7f10e"></a>

### [`004b1448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1448.md) → [`004b1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1488.md) _ZN5Botan11BER_Decoder21get_next_octet_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c588a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1448.md#insn-004b1470)
- 新版 [`004b14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1488.md#insn-004b14b0)

~~~diff
- 004b1470 ["INT_ADD", "register:40f0:8", ["const:4b1470:8", "const:4:8"]]
- 004b1470 ["CALL", null, ["callee:00c58970:8"]]
+ 004b14b0 ["INT_ADD", "register:40f0:8", ["const:4b14b0:8", "const:4:8"]]
+ 004b14b0 ["CALL", null, ["callee:00c58970:8"]]
- 004b1470 bytes 0c9d1e94
+ 004b14b0 bytes 309d1e94
~~~


<a id="compare-34869a77dabf53ba46dbf27d90ca847c"></a>

### [`004b25c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) → [`004b2600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) FUN_004b2600

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004ad4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) · 呼出先 2件 [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`004ad4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) [`004b1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) · 呼出先 2件 [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md#insn-004b2608) · [`004b26b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md#insn-004b26b4) · [`004b26fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md#insn-004b26fc)
- 新版 [`004b2648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b2648) · [`004b26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b26f4) · [`004b273c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md#insn-004b273c)

~~~diff
- 004b2608 ["INT_ADD", "register:40f0:8", ["const:4b2608:8", "const:4:8"]]
- 004b2608 ["CALL", null, ["callee:005411e4:8"]]
+ 004b2648 ["INT_ADD", "register:40f0:8", ["const:4b2648:8", "const:4:8"]]
+ 004b2648 ["CALL", null, ["callee:005411e4:8"]]
- 004b2608 bytes e73a0294
+ 004b2648 bytes e73a0294
- 004b26b4 ["INT_ADD", "register:40f0:8", ["const:4b26b4:8", "const:4:8"]]
- 004b26b4 ["CALL", null, ["callee:005411e4:8"]]
+ 004b26f4 ["INT_ADD", "register:40f0:8", ["const:4b26f4:8", "const:4:8"]]
+ 004b26f4 ["CALL", null, ["callee:005411e4:8"]]
- 004b26b4 bytes bc3a0294
+ 004b26f4 bytes bc3a0294
- 004b26fc ["INT_ADD", "register:40f0:8", ["const:4b26fc:8", "const:4:8"]]
- 004b26fc ["CALL", null, ["callee:005411e4:8"]]
+ 004b273c ["INT_ADD", "register:40f0:8", ["const:4b273c:8", "const:4:8"]]
+ 004b273c ["CALL", null, ["callee:005411e4:8"]]
- 004b26fc bytes aa3a0294
+ 004b273c bytes aa3a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-585d774190db3963524f3aeb29b50c1d"></a>

### [`004b2be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2be0.md) → [`004b2c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md) _ZN5Botan11DER_Encoder9raw_bytesEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2be0.md#insn-004b2c04) · [`004b2c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2be0.md#insn-004b2c30) · [`004b2c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2be0.md#insn-004b2c58)
- 新版 [`004b2c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c44) · [`004b2c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c70) · [`004b2c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2c20.md#insn-004b2c98)

~~~diff
- 004b2c04 ["INT_ADD", "register:40f0:8", ["const:4b2c04:8", "const:4:8"]]
- 004b2c04 ["CALL", null, ["callee:00c58790:8"]]
+ 004b2c44 ["INT_ADD", "register:40f0:8", ["const:4b2c44:8", "const:4:8"]]
+ 004b2c44 ["CALL", null, ["callee:00c58790:8"]]
- 004b2c04 bytes af961e94
+ 004b2c44 bytes d3961e94
- 004b2c30 ["INT_ADD", "register:40f0:8", ["const:4b2c30:8", "const:4:8"]]
- 004b2c30 ["CALL", null, ["callee:0054052c:8"]]
+ 004b2c70 ["INT_ADD", "register:40f0:8", ["const:4b2c70:8", "const:4:8"]]
+ 004b2c70 ["CALL", null, ["callee:0054052c:8"]]
- 004b2c30 bytes 2f360294
+ 004b2c70 bytes 2f360294
- 004b2c58 ["INT_ADD", "register:40f0:8", ["const:4b2c58:8", "const:4:8"]]
- 004b2c58 ["CALL", null, ["callee:00c58010:8"]]
+ 004b2c98 ["INT_ADD", "register:40f0:8", ["const:4b2c98:8", "const:4:8"]]
+ 004b2c98 ["CALL", null, ["callee:00c58010:8"]]
- 004b2c58 bytes ba941e94
+ 004b2c98 bytes de941e94
~~~


<a id="compare-becfc5dedd7c09bd3043bd9316a21c65"></a>

### [`004b2c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2c84.md) → [`004b2cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md) _ZN5Botan11DER_Encoder6encodeEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2c84.md#insn-004b2cb8) · [`004b2cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2c84.md#insn-004b2cdc)
- 新版 [`004b2cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md#insn-004b2cf8) · [`004b2d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2cc4.md#insn-004b2d1c)

~~~diff
- 004b2cb8 ["INT_ADD", "register:40f0:8", ["const:4b2cb8:8", "const:4:8"]]
- 004b2cb8 ["CALL", null, ["callee:00c588f0:8"]]
+ 004b2cf8 ["INT_ADD", "register:40f0:8", ["const:4b2cf8:8", "const:4:8"]]
+ 004b2cf8 ["CALL", null, ["callee:00c588f0:8"]]
- 004b2cb8 bytes da961e94
+ 004b2cf8 bytes fe961e94
- 004b2cdc ["INT_ADD", "register:40f0:8", ["const:4b2cdc:8", "const:4:8"]]
- 004b2cdc ["CALL", null, ["callee:00c57fb0:8"]]
+ 004b2d1c ["INT_ADD", "register:40f0:8", ["const:4b2d1c:8", "const:4:8"]]
+ 004b2d1c ["CALL", null, ["callee:00c57fb0:8"]]
- 004b2cdc bytes 81941e94
+ 004b2d1c bytes a5941e94
~~~


<a id="compare-42fe2b78a8caa064418401db91936b40"></a>

### [`004b2ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ce0.md) → [`004b2d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md) _ZN5Botan11DER_Encoder6encodeEbNS_8ASN1_TagES1_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b2d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ce0.md#insn-004b2d18) · [`004b2d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ce0.md#insn-004b2d3c)
- 新版 [`004b2d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md#insn-004b2d58) · [`004b2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2d20.md#insn-004b2d7c)

~~~diff
- 004b2d18 ["INT_ADD", "register:40f0:8", ["const:4b2d18:8", "const:4:8"]]
- 004b2d18 ["CALL", null, ["callee:00c588f0:8"]]
+ 004b2d58 ["INT_ADD", "register:40f0:8", ["const:4b2d58:8", "const:4:8"]]
+ 004b2d58 ["CALL", null, ["callee:00c588f0:8"]]
- 004b2d18 bytes c2961e94
+ 004b2d58 bytes e6961e94
- 004b2d3c ["INT_ADD", "register:40f0:8", ["const:4b2d3c:8", "const:4:8"]]
- 004b2d3c ["CALL", null, ["callee:00c57fb0:8"]]
+ 004b2d7c ["INT_ADD", "register:40f0:8", ["const:4b2d7c:8", "const:4:8"]]
+ 004b2d7c ["CALL", null, ["callee:00c57fb0:8"]]
- 004b2d3c bytes 69941e94
+ 004b2d7c bytes 8d941e94
~~~


<a id="compare-ee848cd0c340ee7226159030eb47bb41"></a>

### [`004b3424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3424.md) → [`004b3464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_h

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3424.md#insn-004b344c) · [`004b3470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3424.md#insn-004b3470)
- 新版 [`004b348c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md#insn-004b348c) · [`004b34b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3464.md#insn-004b34b0)

~~~diff
- 004b344c ["INT_ADD", "register:40f0:8", ["const:4b344c:8", "const:4:8"]]
- 004b344c ["CALL", null, ["callee:00c588f0:8"]]
+ 004b348c ["INT_ADD", "register:40f0:8", ["const:4b348c:8", "const:4:8"]]
+ 004b348c ["CALL", null, ["callee:00c588f0:8"]]
- 004b344c bytes f5941e94
+ 004b348c bytes 19951e94
- 004b3470 ["INT_ADD", "register:40f0:8", ["const:4b3470:8", "const:4:8"]]
- 004b3470 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004b34b0 ["INT_ADD", "register:40f0:8", ["const:4b34b0:8", "const:4:8"]]
+ 004b34b0 ["CALL", null, ["callee:00c57fb0:8"]]
- 004b3470 bytes 9c921e94
+ 004b34b0 bytes c0921e94
~~~


<a id="compare-80ee60cb960279e730a004d1c8678226"></a>

### [`004b3d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3d7c.md) → [`004b3dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3dbc.md) _ZN5Botan11DER_Encoder9encode_ifEbRKNS_11ASN1_ObjectE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b3da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3d7c.md#insn-004b3da0)
- 新版 [`004b3de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3dbc.md#insn-004b3de0)

~~~diff
- 004b3da0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004b3da0 ["INT_ADD", "register:40f0:8", ["const:4b3da0:8", "const:4:8"]]
- 004b3da0 ["CALLIND", null, ["register:0:8"]]
+ 004b3de0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004b3de0 ["INT_ADD", "register:40f0:8", ["const:4b3de0:8", "const:4:8"]]
+ 004b3de0 ["CALLIND", null, ["register:0:8"]]
- 004b3da0 bytes 00013fd6
+ 004b3de0 bytes 00013fd6
~~~


<a id="compare-d2e64df43c1f7c7b73121455450c84ce"></a>

### [`004b3db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3db4.md) → [`004b3df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md) _ZN5Botan9SCAN_NameC1EPKc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b3de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3db4.md#insn-004b3de4) · [`004b3e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3db4.md#insn-004b3e30) · [`004b3e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3db4.md#insn-004b3e50)
- 新版 [`004b3e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e24) · [`004b3e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e70) · [`004b3e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3df4.md#insn-004b3e90)

~~~diff
- 004b3de4 ["INT_ADD", "register:40f0:8", ["const:4b3de4:8", "const:4:8"]]
- 004b3de4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004b3e24 ["INT_ADD", "register:40f0:8", ["const:4b3e24:8", "const:4:8"]]
+ 004b3e24 ["CALL", null, ["callee:00c580b0:8"]]
- 004b3de4 bytes 7f901e94
+ 004b3e24 bytes a3901e94
- 004b3e30 ["INT_ADD", "register:40f0:8", ["const:4b3e30:8", "const:4:8"]]
- 004b3e30 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b3e70 ["INT_ADD", "register:40f0:8", ["const:4b3e70:8", "const:4:8"]]
+ 004b3e70 ["CALL", null, ["callee:00c57f60:8"]]
- 004b3e30 bytes 18901e94
+ 004b3e70 bytes 3c901e94
- 004b3e50 ["INT_ADD", "register:40f0:8", ["const:4b3e50:8", "const:4:8"]]
- 004b3e50 ["CALL", null, ["callee:00c580d0:8"]]
+ 004b3e90 ["INT_ADD", "register:40f0:8", ["const:4b3e90:8", "const:4:8"]]
+ 004b3e90 ["CALL", null, ["callee:00c580d0:8"]]
- 004b3e50 bytes 6c901e94
+ 004b3e90 bytes 90901e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d1a3310a04ef090e4e3ae41cdb787b0"></a>

### [`004b4a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4a40.md) → [`004b4a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4a80.md) FUN_004b4a80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4a40.md#insn-004b4a88)
- 新版 [`004b4ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4a80.md#insn-004b4ac8)

~~~diff
- 004b4a88 ["INT_ADD", "register:40f0:8", ["const:4b4a88:8", "const:4:8"]]
- 004b4a88 ["CALL", null, ["callee:00c57f80:8"]]
+ 004b4ac8 ["INT_ADD", "register:40f0:8", ["const:4b4ac8:8", "const:4:8"]]
+ 004b4ac8 ["CALL", null, ["callee:00c57f80:8"]]
- 004b4a88 bytes 0a8d1e94
+ 004b4ac8 bytes 2e8d1e94
~~~


<a id="compare-d0b4054ee75d1e2526c823eb32c13c3c"></a>

### [`004b4dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4dc8.md) → [`004b4e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e08.md) _ZNK5Botan9SCAN_Name14arg_as_integerEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c587f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c588c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4dc8.md#insn-004b4dfc)
- 新版 [`004b4e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e08.md#insn-004b4e3c)

~~~diff
- 004b4dfc ["INT_ADD", "register:40f0:8", ["const:4b4dfc:8", "const:4:8"]]
- 004b4dfc ["CALL", null, ["callee:00c588c0:8"]]
+ 004b4e3c ["INT_ADD", "register:40f0:8", ["const:4b4e3c:8", "const:4:8"]]
+ 004b4e3c ["CALL", null, ["callee:00c588c0:8"]]
- 004b4dfc bytes 7d8e1e94
+ 004b4e3c bytes a18e1e94
~~~


<a id="compare-40e3d0cfebd33a5e2c8eb0c59bbd0b43"></a>

### [`004b4f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4f08.md) → [`004b4f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md) _ZN5Botan11OctetStringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4f08.md#insn-004b4f40) · [`004b4f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4f08.md#insn-004b4f64) · [`004b4f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4f08.md#insn-004b4f7c)
- 新版 [`004b4f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4f80) · [`004b4fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4fa4) · [`004b4fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4f48.md#insn-004b4fbc)

~~~diff
- 004b4f40 ["INT_ADD", "register:40f0:8", ["const:4b4f40:8", "const:4:8"]]
- 004b4f40 ["CALL", null, ["callee:0054052c:8"]]
+ 004b4f80 ["INT_ADD", "register:40f0:8", ["const:4b4f80:8", "const:4:8"]]
+ 004b4f80 ["CALL", null, ["callee:0054052c:8"]]
- 004b4f40 bytes 6b2d0294
+ 004b4f80 bytes 6b2d0294
- 004b4f64 ["INT_ADD", "register:40f0:8", ["const:4b4f64:8", "const:4:8"]]
- 004b4f64 ["CALL", null, ["callee:00c58bb0:8"]]
+ 004b4fa4 ["INT_ADD", "register:40f0:8", ["const:4b4fa4:8", "const:4:8"]]
+ 004b4fa4 ["CALL", null, ["callee:00c58bb0:8"]]
- 004b4f64 bytes df8e1e94
+ 004b4fa4 bytes 038f1e94
- 004b4f7c ["INT_ADD", "register:40f0:8", ["const:4b4f7c:8", "const:4:8"]]
- 004b4f7c ["CALL", null, ["callee:0054052c:8"]]
+ 004b4fbc ["INT_ADD", "register:40f0:8", ["const:4b4fbc:8", "const:4:8"]]
+ 004b4fbc ["CALL", null, ["callee:0054052c:8"]]
- 004b4f7c bytes 5c2d0294
+ 004b4fbc bytes 5c2d0294
~~~


<a id="compare-cbf67f1c2544416d73fd7368c1906ed0"></a>

### [`004b4fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4fd0.md) → [`004b5010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5010.md) _ZN5Botan11OctetStringC1EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`005433c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005433c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4fd0.md#insn-004b4ff0)
- 新版 [`004b5030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5010.md#insn-004b5030)

~~~diff
- 004b4ff0 ["INT_ADD", "register:40f0:8", ["const:4b4ff0:8", "const:4:8"]]
- 004b4ff0 ["CALL", null, ["callee:00543400:8"]]
+ 004b5030 ["INT_ADD", "register:40f0:8", ["const:4b5030:8", "const:4:8"]]
+ 004b5030 ["CALL", null, ["callee:00543400:8"]]
- 004b4ff0 bytes f4380294
+ 004b5030 bytes f4380294
~~~


<a id="compare-1eefbf2491e0e759b05abd7f3b93ae05"></a>

### [`004b5258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5258.md) → [`004b5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5298.md) _ZN5Botan11OctetStringeOERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b530c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5258.md#insn-004b530c)
- 新版 [`004b534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5298.md#insn-004b534c)

~~~diff
- 004b530c ["INT_ADD", "register:40f0:8", ["const:4b530c:8", "const:4:8"]]
- 004b530c ["CALL", null, ["callee:00c58160:8"]]
+ 004b534c ["INT_ADD", "register:40f0:8", ["const:4b534c:8", "const:4:8"]]
+ 004b534c ["CALL", null, ["callee:00c58160:8"]]
- 004b530c bytes 618b1e94
+ 004b534c bytes 858b1e94
~~~


<a id="compare-0ab7f19c30b930e4f9b3f4d2901b6d83"></a>

### [`004b54a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54a4.md) → [`004b54e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b54e4.md) _ZN5BotanneERKNS_11OctetStringES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b54ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54a4.md#insn-004b54ac)
- 新版 [`004b54ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b54e4.md#insn-004b54ec)

~~~diff
- 004b54ac ["INT_ADD", "register:40f0:8", ["const:4b54ac:8", "const:4:8"]]
- 004b54ac ["CALL", null, ["callee:00c58c80:8"]]
+ 004b54ec ["INT_ADD", "register:40f0:8", ["const:4b54ec:8", "const:4:8"]]
+ 004b54ec ["CALL", null, ["callee:00c58c80:8"]]
- 004b54ac bytes c18d1e94
+ 004b54ec bytes e58d1e94
~~~


<a id="compare-b784354c7aff0593f8651c3658fb5bf3"></a>

### [`004b6160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6160.md) → [`004b61a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md) _ZN5Botan13base64_decodeEPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b61a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6160.md#insn-004b61a4) · [`004b61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6160.md#insn-004b61b8) · [`004b61d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6160.md#insn-004b61d0)
- 新版 [`004b61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b61e4) · [`004b61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b61f8) · [`004b6210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b61a0.md#insn-004b6210)

~~~diff
- 004b61a4 ["INT_ADD", "register:40f0:8", ["const:4b61a4:8", "const:4:8"]]
- 004b61a4 ["CALL", null, ["callee:004b3548:8"]]
+ 004b61e4 ["INT_ADD", "register:40f0:8", ["const:4b61e4:8", "const:4:8"]]
+ 004b61e4 ["CALL", null, ["callee:004b3548:8"]]
- 004b61a4 bytes d9f4ff97
+ 004b61e4 bytes d9f4ff97
- 004b61b8 ["INT_ADD", "register:40f0:8", ["const:4b61b8:8", "const:4:8"]]
- 004b61b8 ["CALL", null, ["callee:00c58cc0:8"]]
+ 004b61f8 ["INT_ADD", "register:40f0:8", ["const:4b61f8:8", "const:4:8"]]
+ 004b61f8 ["CALL", null, ["callee:00c58cc0:8"]]
- 004b61b8 bytes 8e8a1e94
+ 004b61f8 bytes b28a1e94
- 004b61d0 ["INT_ADD", "register:40f0:8", ["const:4b61d0:8", "const:4:8"]]
- 004b61d0 ["CALL", null, ["callee:0054052c:8"]]
+ 004b6210 ["INT_ADD", "register:40f0:8", ["const:4b6210:8", "const:4:8"]]
+ 004b6210 ["CALL", null, ["callee:0054052c:8"]]
- 004b61d0 bytes c7280294
+ 004b6210 bytes c7280294
~~~


<a id="compare-9aaa8c4e42bb745e50dca73c6feaa6ef"></a>

### [`004b622c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b622c.md) → [`004b626c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md) _ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c00.md) · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bf0.md)
- 新版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cd0.md) · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b6280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b622c.md#insn-004b6280) · [`004b6294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b622c.md#insn-004b6294) · [`004b62ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b622c.md#insn-004b62ac)
- 新版 [`004b62c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62c0) · [`004b62d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62d4) · [`004b62ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b626c.md#insn-004b62ec)

~~~diff
- 004b6280 ["INT_ADD", "register:40f0:8", ["const:4b6280:8", "const:4:8"]]
- 004b6280 ["CALL", null, ["callee:004b3548:8"]]
+ 004b62c0 ["INT_ADD", "register:40f0:8", ["const:4b62c0:8", "const:4:8"]]
+ 004b62c0 ["CALL", null, ["callee:004b3548:8"]]
- 004b6280 bytes a2f4ff97
+ 004b62c0 bytes a2f4ff97
- 004b6294 ["INT_ADD", "register:40f0:8", ["const:4b6294:8", "const:4:8"]]
- 004b6294 ["CALL", null, ["callee:00c58cc0:8"]]
+ 004b62d4 ["INT_ADD", "register:40f0:8", ["const:4b62d4:8", "const:4:8"]]
+ 004b62d4 ["CALL", null, ["callee:00c58cc0:8"]]
- 004b6294 bytes 578a1e94
+ 004b62d4 bytes 7b8a1e94
- 004b62ac ["INT_ADD", "register:40f0:8", ["const:4b62ac:8", "const:4:8"]]
- 004b62ac ["CALL", null, ["callee:0054052c:8"]]
+ 004b62ec ["INT_ADD", "register:40f0:8", ["const:4b62ec:8", "const:4:8"]]
+ 004b62ec ["CALL", null, ["callee:0054052c:8"]]
- 004b62ac bytes 90280294
+ 004b62ec bytes 90280294
~~~


<a id="compare-a213bf3f0ea87ff1dd251dfd4255c551"></a>

### [`004b741c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b741c.md) → [`004b745c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md) _ZN5Botan6BigInt13encode_lockedERKS0_NS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c58940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) [`00c58950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) [`00c58a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b7438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b741c.md#insn-004b7438) · [`004b7444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b741c.md#insn-004b7444) · [`004b7454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b741c.md#insn-004b7454)
- 新版 [`004b7478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7478) · [`004b7484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7484) · [`004b7494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b745c.md#insn-004b7494)

~~~diff
- 004b7438 ["INT_ADD", "register:40f0:8", ["const:4b7438:8", "const:4:8"]]
- 004b7438 ["CALL", null, ["callee:00c58a10:8"]]
+ 004b7478 ["INT_ADD", "register:40f0:8", ["const:4b7478:8", "const:4:8"]]
+ 004b7478 ["CALL", null, ["callee:00c58a10:8"]]
- 004b7438 bytes 42851e94
+ 004b7478 bytes 66851e94
- 004b7444 ["INT_ADD", "register:40f0:8", ["const:4b7444:8", "const:4:8"]]
- 004b7444 ["CALL", null, ["callee:004b3548:8"]]
+ 004b7484 ["INT_ADD", "register:40f0:8", ["const:4b7484:8", "const:4:8"]]
+ 004b7484 ["CALL", null, ["callee:004b3548:8"]]
- 004b7444 bytes 31f0ff97
+ 004b7484 bytes 31f0ff97
- 004b7454 ["INT_ADD", "register:40f0:8", ["const:4b7454:8", "const:4:8"]]
- 004b7454 ["CALL", null, ["callee:00c58a20:8"]]
+ 004b7494 ["INT_ADD", "register:40f0:8", ["const:4b7494:8", "const:4:8"]]
+ 004b7494 ["CALL", null, ["callee:00c58a20:8"]]
- 004b7454 bytes 3f851e94
+ 004b7494 bytes 63851e94
~~~


<a id="compare-a082120c1b00e139012fa5c03ec8c413"></a>

### [`004b74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b74c0.md) → [`004b7500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md) _ZN5Botan6BigInt11encode_1363ERKS0_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c58c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b74d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b74c0.md#insn-004b74d8) · [`004b74e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b74c0.md#insn-004b74e8)
- 新版 [`004b7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md#insn-004b7518) · [`004b7528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7500.md#insn-004b7528)

~~~diff
- 004b74d8 ["INT_ADD", "register:40f0:8", ["const:4b74d8:8", "const:4:8"]]
- 004b74d8 ["CALL", null, ["callee:004b3548:8"]]
+ 004b7518 ["INT_ADD", "register:40f0:8", ["const:4b7518:8", "const:4:8"]]
+ 004b7518 ["CALL", null, ["callee:004b3548:8"]]
- 004b74d8 bytes 0cf0ff97
+ 004b7518 bytes 0cf0ff97
- 004b74e8 ["INT_ADD", "register:40f0:8", ["const:4b74e8:8", "const:4:8"]]
- 004b74e8 ["CALL", null, ["callee:00c58d30:8"]]
+ 004b7528 ["INT_ADD", "register:40f0:8", ["const:4b7528:8", "const:4:8"]]
+ 004b7528 ["CALL", null, ["callee:00c58d30:8"]]
- 004b74e8 bytes de851e94
+ 004b7528 bytes 02861e94
~~~


<a id="compare-e2ec121d6f6f910e9184412810e37ee1"></a>

### [`004b76a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b76a4.md) → [`004b76e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md) _ZN5Botan6BigInt28encode_fixed_length_int_pairERKS0_S2_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c58c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c58d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b76cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b76a4.md#insn-004b76cc) · [`004b76dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b76a4.md#insn-004b76dc) · [`004b76f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b76a4.md#insn-004b76f0)
- 新版 [`004b770c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b770c) · [`004b771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b771c) · [`004b7730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b76e4.md#insn-004b7730)

~~~diff
- 004b76cc ["INT_ADD", "register:40f0:8", ["const:4b76cc:8", "const:4:8"]]
- 004b76cc ["CALL", null, ["callee:004b3548:8"]]
+ 004b770c ["INT_ADD", "register:40f0:8", ["const:4b770c:8", "const:4:8"]]
+ 004b770c ["CALL", null, ["callee:004b3548:8"]]
- 004b76cc bytes 8fefff97
+ 004b770c bytes 8fefff97
- 004b76dc ["INT_ADD", "register:40f0:8", ["const:4b76dc:8", "const:4:8"]]
- 004b76dc ["CALL", null, ["callee:00c58d30:8"]]
+ 004b771c ["INT_ADD", "register:40f0:8", ["const:4b771c:8", "const:4:8"]]
+ 004b771c ["CALL", null, ["callee:00c58d30:8"]]
- 004b76dc bytes 61851e94
+ 004b771c bytes 85851e94
- 004b76f0 ["INT_ADD", "register:40f0:8", ["const:4b76f0:8", "const:4:8"]]
- 004b76f0 ["CALL", null, ["callee:00c58d30:8"]]
+ 004b7730 ["INT_ADD", "register:40f0:8", ["const:4b7730:8", "const:4:8"]]
+ 004b7730 ["CALL", null, ["callee:00c58d30:8"]]
- 004b76f0 bytes 5c851e94
+ 004b7730 bytes 80851e94
~~~


<a id="compare-e9fa84eb95348520deeaa7d68f1d8d58"></a>

### [`004b7a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7a44.md) → [`004b7a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md) _ZN5Botan17hex_decode_lockedEPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c58ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b7a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7a44.md#insn-004b7a70) · [`004b7a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7a44.md#insn-004b7a84) · [`004b7a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7a44.md#insn-004b7a9c)
- 新版 [`004b7ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7ab0) · [`004b7ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7ac4) · [`004b7adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7a84.md#insn-004b7adc)

~~~diff
- 004b7a70 ["INT_ADD", "register:40f0:8", ["const:4b7a70:8", "const:4:8"]]
- 004b7a70 ["CALL", null, ["callee:004b3548:8"]]
+ 004b7ab0 ["INT_ADD", "register:40f0:8", ["const:4b7ab0:8", "const:4:8"]]
+ 004b7ab0 ["CALL", null, ["callee:004b3548:8"]]
- 004b7a70 bytes a6eeff97
+ 004b7ab0 bytes a6eeff97
- 004b7a84 ["INT_ADD", "register:40f0:8", ["const:4b7a84:8", "const:4:8"]]
- 004b7a84 ["CALL", null, ["callee:00c58bb0:8"]]
+ 004b7ac4 ["INT_ADD", "register:40f0:8", ["const:4b7ac4:8", "const:4:8"]]
+ 004b7ac4 ["CALL", null, ["callee:00c58bb0:8"]]
- 004b7a84 bytes 17841e94
+ 004b7ac4 bytes 3b841e94
- 004b7a9c ["INT_ADD", "register:40f0:8", ["const:4b7a9c:8", "const:4:8"]]
- 004b7a9c ["CALL", null, ["callee:0054052c:8"]]
+ 004b7adc ["INT_ADD", "register:40f0:8", ["const:4b7adc:8", "const:4:8"]]
+ 004b7adc ["CALL", null, ["callee:0054052c:8"]]
- 004b7a9c bytes 94220294
+ 004b7adc bytes 94220294
~~~


<a id="compare-2b965986371d1c6e1d359a5722673357"></a>

### [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) → [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) FUN_004b87f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) [`004b9db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md) [`004b9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md) · 呼出先 1件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md)
- 新版 呼出元 9件 [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) [`004b9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md) [`004b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md) · 呼出先 1件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b87dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md#insn-004b87dc)
- 新版 [`004b881c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md#insn-004b881c)

~~~diff
- 004b87dc ["INT_ADD", "register:40f0:8", ["const:4b87dc:8", "const:4:8"]]
- 004b87dc ["CALL", null, ["local:b0:8"]]
+ 004b881c ["INT_ADD", "register:40f0:8", ["const:4b881c:8", "const:4:8"]]
+ 004b881c ["CALL", null, ["local:b0:8"]]
- 004b87dc bytes f6ffff97
+ 004b881c bytes f6ffff97
~~~


<a id="compare-dc23bc6ed0cef6fe5a1f181b6b129ae5"></a>

### [`004b943c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b943c.md) → [`004b947c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md) _ZN5Botan6BigIntrSEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c30.md) · 呼出先 1件 [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md)
- 新版 呼出元 1件 [`00c58d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d00.md) · 呼出先 1件 [`004b9c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b943c.md#insn-004b9484)
- 新版 [`004b94c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md#insn-004b94c4)

~~~diff
- 004b9484 ["INT_ADD", "register:40f0:8", ["const:4b9484:8", "const:4:8"]]
- 004b9484 ["CALL", null, ["callee:004b9c78:8"]]
+ 004b94c4 ["INT_ADD", "register:40f0:8", ["const:4b94c4:8", "const:4:8"]]
+ 004b94c4 ["CALL", null, ["callee:004b9c78:8"]]
- 004b9484 bytes ed010094
+ 004b94c4 bytes ed010094
~~~


<a id="compare-a5a5f0fa6a46184dcf8d0b5cfe79e4f8"></a>

### [`004b9b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9b08.md) → [`004b9b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md) _ZN5Botan6BigIntlSEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c10.md) · 呼出先 3件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c58ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ce0.md) · 呼出先 3件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9b08.md#insn-004b9b98) · [`004b9bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9b08.md#insn-004b9bd4) · [`004b9be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9b08.md#insn-004b9be4)
- 新版 [`004b9bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9bd8) · [`004b9c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9c14) · [`004b9c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9b48.md#insn-004b9c24)

~~~diff
- 004b9b98 ["INT_ADD", "register:40f0:8", ["const:4b9b98:8", "const:4:8"]]
- 004b9b98 ["CALL", null, ["callee:00540960:8"]]
+ 004b9bd8 ["INT_ADD", "register:40f0:8", ["const:4b9bd8:8", "const:4:8"]]
+ 004b9bd8 ["CALL", null, ["callee:00540960:8"]]
- 004b9b98 bytes 621b0294
+ 004b9bd8 bytes 621b0294
- 004b9bd4 ["INT_ADD", "register:40f0:8", ["const:4b9bd4:8", "const:4:8"]]
- 004b9bd4 ["CALL", null, ["callee:00c58010:8"]]
+ 004b9c14 ["INT_ADD", "register:40f0:8", ["const:4b9c14:8", "const:4:8"]]
+ 004b9c14 ["CALL", null, ["callee:00c58010:8"]]
- 004b9bd4 bytes db781e94
+ 004b9c14 bytes ff781e94
- 004b9be4 ["INT_ADD", "register:40f0:8", ["const:4b9be4:8", "const:4:8"]]
- 004b9be4 ["CALL", null, ["callee:00c58160:8"]]
+ 004b9c24 ["INT_ADD", "register:40f0:8", ["const:4b9c24:8", "const:4:8"]]
+ 004b9c24 ["CALL", null, ["callee:00c58160:8"]]
- 004b9be4 bytes 2b791e94
+ 004b9c24 bytes 4f791e94
~~~


<a id="compare-e7c36e29f93a47a2331f02541bb58e85"></a>

### [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md) → [`004b9c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md) FUN_004b9c78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004b943c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b943c.md) [`004d9518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9518.md) [`004da6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004da/004da6a8.md) [`004dd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dd/004dd308.md) [`004dfdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004dfdfc.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 5件 [`004b947c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b947c.md) [`004d9558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d9/004d9558.md) [`004da6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004da/004da6e8.md) [`004dd348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dd/004dd348.md) [`004dfe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004dfe3c.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md#insn-004b9ca0) · [`004b9ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md#insn-004b9ce0)
- 新版 [`004b9ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md#insn-004b9ce0) · [`004b9d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9c78.md#insn-004b9d20)

~~~diff
- 004b9ca0 ["INT_ADD", "register:40f0:8", ["const:4b9ca0:8", "const:4:8"]]
- 004b9ca0 ["CALL", null, ["callee:00c58010:8"]]
+ 004b9ce0 ["INT_ADD", "register:40f0:8", ["const:4b9ce0:8", "const:4:8"]]
+ 004b9ce0 ["CALL", null, ["callee:00c58010:8"]]
- 004b9ca0 bytes a8781e94
+ 004b9ce0 bytes cc781e94
- 004b9ce0 ["INT_ADD", "register:40f0:8", ["const:4b9ce0:8", "const:4:8"]]
- 004b9ce0 ["CALL", null, ["callee:00c58160:8"]]
+ 004b9d20 ["INT_ADD", "register:40f0:8", ["const:4b9d20:8", "const:4:8"]]
+ 004b9d20 ["CALL", null, ["callee:00c58160:8"]]
- 004b9ce0 bytes ec781e94
+ 004b9d20 bytes 10791e94
~~~


<a id="compare-454c056f5fc32d75ed0e50727e66c55c"></a>

### [`004b9db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md) → [`004b9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md) _ZN5BotanplERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cb0.md) · 呼出先 4件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004d6d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6d14.md) [`00c58c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c20.md)
- 新版 呼出元 1件 [`00c58d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d80.md) · 呼出先 4件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004d6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6d54.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md#insn-004b9e34) · [`004b9e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md#insn-004b9e60) · [`004b9e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md#insn-004b9e90)
- 新版 [`004b9e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9e74) · [`004b9ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9ea0) · [`004b9ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md#insn-004b9ed0)

~~~diff
- 004b9e34 ["INT_ADD", "register:40f0:8", ["const:4b9e34:8", "const:4:8"]]
- 004b9e34 ["CALL", null, ["callee:00c58cf0:8"]]
+ 004b9e74 ["INT_ADD", "register:40f0:8", ["const:4b9e74:8", "const:4:8"]]
+ 004b9e74 ["CALL", null, ["callee:00c58cf0:8"]]
- 004b9e34 bytes 7b7b1e94
+ 004b9e74 bytes 9f7b1e94
- 004b9e60 ["INT_ADD", "register:40f0:8", ["const:4b9e60:8", "const:4:8"]]
- 004b9e60 ["CALL", null, ["callee:004d6d54:8"]]
+ 004b9ea0 ["INT_ADD", "register:40f0:8", ["const:4b9ea0:8", "const:4:8"]]
+ 004b9ea0 ["CALL", null, ["callee:004d6d54:8"]]
- 004b9e60 bytes ad730094
+ 004b9ea0 bytes ad730094
- 004b9e90 ["INT_ADD", "register:40f0:8", ["const:4b9e90:8", "const:4:8"]]
- 004b9e90 ["CALL", null, ["callee:004b87f4:8"]]
+ 004b9ed0 ["INT_ADD", "register:40f0:8", ["const:4b9ed0:8", "const:4:8"]]
+ 004b9ed0 ["CALL", null, ["callee:004b87f4:8"]]
- 004b9e90 bytes 49faff97
+ 004b9ed0 bytes 49faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffabefeb5c2bbc5cde88121dbecadcab"></a>

### [`004b9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md) → [`004b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md) _ZN5BotanmiERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cc0.md) · 呼出先 4件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004d6d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6d14.md) [`00c58c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c20.md)
- 新版 呼出元 1件 [`00c58d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d90.md) · 呼出先 4件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004d6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6d54.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b9fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md#insn-004b9fb8) · [`004b9fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md#insn-004b9fd4) · [`004ba008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md#insn-004ba008)
- 新版 [`004b9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004b9ff8) · [`004ba014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004ba014) · [`004ba048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md#insn-004ba048)

~~~diff
- 004b9fb8 ["INT_ADD", "register:40f0:8", ["const:4b9fb8:8", "const:4:8"]]
- 004b9fb8 ["CALL", null, ["callee:004b87f4:8"]]
+ 004b9ff8 ["INT_ADD", "register:40f0:8", ["const:4b9ff8:8", "const:4:8"]]
+ 004b9ff8 ["CALL", null, ["callee:004b87f4:8"]]
- 004b9fb8 bytes fff9ff97
+ 004b9ff8 bytes fff9ff97
- 004b9fd4 ["INT_ADD", "register:40f0:8", ["const:4b9fd4:8", "const:4:8"]]
- 004b9fd4 ["CALL", null, ["callee:00c58cf0:8"]]
+ 004ba014 ["INT_ADD", "register:40f0:8", ["const:4ba014:8", "const:4:8"]]
+ 004ba014 ["CALL", null, ["callee:00c58cf0:8"]]
- 004b9fd4 bytes 137b1e94
+ 004ba014 bytes 377b1e94
- 004ba008 ["INT_ADD", "register:40f0:8", ["const:4ba008:8", "const:4:8"]]
- 004ba008 ["CALL", null, ["callee:004b898c:8"]]
+ 004ba048 ["INT_ADD", "register:40f0:8", ["const:4ba048:8", "const:4:8"]]
+ 004ba048 ["CALL", null, ["callee:004b898c:8"]]
- 004ba008 bytes 51faff97
+ 004ba048 bytes 51faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e1e87782a1f996cf341813a3c10c0c"></a>

### [`004ba5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba5fc.md) → [`004ba63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba63c.md) _ZN5BotanlsERKNS_6BigIntEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md) [`00c58c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ba65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba5fc.md#insn-004ba65c)
- 新版 [`004ba69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba63c.md#insn-004ba69c)

~~~diff
- 004ba65c ["INT_ADD", "register:40f0:8", ["const:4ba65c:8", "const:4:8"]]
- 004ba65c ["CALL", null, ["callee:00c58cf0:8"]]
+ 004ba69c ["INT_ADD", "register:40f0:8", ["const:4ba69c:8", "const:4:8"]]
+ 004ba69c ["CALL", null, ["callee:00c58cf0:8"]]
- 004ba65c bytes 71791e94
+ 004ba69c bytes 95791e94
~~~


<a id="compare-8dabb283afaba156d22ca4cd9f1380cc"></a>

### [`004ba74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba74c.md) → [`004ba78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba78c.md) _ZN5BotanrsERKNS_6BigIntEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ce0.md) · 呼出先 3件 [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md) [`00c58c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c20.md)
- 新版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58db0.md) · 呼出先 3件 [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ba828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba74c.md#insn-004ba828)
- 新版 [`004ba868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba78c.md#insn-004ba868)

~~~diff
- 004ba828 ["INT_ADD", "register:40f0:8", ["const:4ba828:8", "const:4:8"]]
- 004ba828 ["CALL", null, ["callee:00c58cf0:8"]]
+ 004ba868 ["INT_ADD", "register:40f0:8", ["const:4ba868:8", "const:4:8"]]
+ 004ba868 ["CALL", null, ["callee:00c58cf0:8"]]
- 004ba828 bytes fe781e94
+ 004ba868 bytes 22791e94
~~~


<a id="compare-274c909760b51210ee088bda69251f09"></a>

### [`004baacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baacc.md) → [`004bab0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md) _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d00.md) · 呼出先 2件 [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md) [`00c58cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cf0.md)
- 新版 呼出元 1件 [`00c58dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dd0.md) · 呼出先 2件 [`00c58bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bf0.md) [`00c58dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bab88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baacc.md#insn-004bab88) · [`004bab98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baacc.md#insn-004bab98) · [`004babac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baacc.md#insn-004babac)
- 新版 [`004babc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babc8) · [`004babd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babd8) · [`004babec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md#insn-004babec)

~~~diff
- 004bab88 ["INT_ADD", "register:40f0:8", ["const:4bab88:8", "const:4:8"]]
- 004bab88 ["CALL", null, ["callee:00c58dc0:8"]]
+ 004babc8 ["INT_ADD", "register:40f0:8", ["const:4babc8:8", "const:4:8"]]
+ 004babc8 ["CALL", null, ["callee:00c58dc0:8"]]
- 004bab88 bytes 5a781e94
+ 004babc8 bytes 7e781e94
- 004bab98 ["INT_ADD", "register:40f0:8", ["const:4bab98:8", "const:4:8"]]
- 004bab98 ["CALL", null, ["callee:00c58bf0:8"]]
+ 004babd8 ["INT_ADD", "register:40f0:8", ["const:4babd8:8", "const:4:8"]]
+ 004babd8 ["CALL", null, ["callee:00c58bf0:8"]]
- 004bab98 bytes e2771e94
+ 004babd8 bytes 06781e94
- 004babac ["INT_ADD", "register:40f0:8", ["const:4babac:8", "const:4:8"]]
- 004babac ["CALL", null, ["callee:00c58bf0:8"]]
+ 004babec ["INT_ADD", "register:40f0:8", ["const:4babec:8", "const:4:8"]]
+ 004babec ["CALL", null, ["callee:00c58bf0:8"]]
- 004babac bytes dd771e94
+ 004babec bytes 01781e94
~~~


<a id="compare-6caa57ce40d8a7b0bf89ad39f7784613"></a>

### [`004babdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004babdc.md) → [`004bac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac1c.md) _ZN5Botan6BigIntC1Em

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) · 呼出先 1件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bac08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004babdc.md#insn-004bac08)
- 新版 [`004bac48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac1c.md#insn-004bac48)

~~~diff
- 004bac08 ["INT_ADD", "register:40f0:8", ["const:4bac08:8", "const:4:8"]]
- 004bac08 ["CALL", null, ["callee:00540960:8"]]
+ 004bac48 ["INT_ADD", "register:40f0:8", ["const:4bac48:8", "const:4:8"]]
+ 004bac48 ["CALL", null, ["callee:00540960:8"]]
- 004bac08 bytes 46170294
+ 004bac48 bytes 46170294
~~~


<a id="compare-cb2314fc1597dcd164bf32ad261b4443"></a>

### [`004bac34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004bac34.md) → [`004bac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac74.md) _ZN5Botan6BigIntC1ENS0_4SignEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c20.md) · 呼出先 1件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cf0.md) · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bac78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004bac34.md#insn-004bac78)
- 新版 [`004bacb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac74.md#insn-004bacb8)

~~~diff
- 004bac78 ["INT_ADD", "register:40f0:8", ["const:4bac78:8", "const:4:8"]]
- 004bac78 ["CALL", null, ["callee:00540960:8"]]
+ 004bacb8 ["INT_ADD", "register:40f0:8", ["const:4bacb8:8", "const:4:8"]]
+ 004bacb8 ["CALL", null, ["callee:00540960:8"]]
- 004bac78 bytes 2a170294
+ 004bacb8 bytes 2a170294
~~~


<a id="compare-c2b7690f8591c04e02c905f3bd05d5bc"></a>

### [`004baca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baca0.md) → [`004bace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bace0.md) _ZN5Botan6BigIntC2ERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md) · 呼出先 1件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)
- 新版 呼出元 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) · 呼出先 1件 [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bacdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baca0.md#insn-004bacdc)
- 新版 [`004bad1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bace0.md#insn-004bad1c)

~~~diff
- 004bacdc ["INT_ADD", "register:40f0:8", ["const:4bacdc:8", "const:4:8"]]
- 004bacdc ["CALL", null, ["callee:0054371c:8"]]
+ 004bad1c ["INT_ADD", "register:40f0:8", ["const:4bad1c:8", "const:4:8"]]
+ 004bad1c ["CALL", null, ["callee:0054371c:8"]]
- 004bacdc bytes 80220294
+ 004bad1c bytes 80220294
~~~


<a id="compare-220c3c18ca9e4ef2c9e86983ae3884a2"></a>

### [`004baff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baff4.md) → [`004bb034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb034.md) _ZN5Botan6BigIntC2ERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59350.md) · 呼出先 1件 [`00c58cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cf0.md)
- 新版 呼出元 1件 [`00c59420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59420.md) · 呼出先 1件 [`00c58dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58dc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004baff4.md#insn-004bb014)
- 新版 [`004bb054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb034.md#insn-004bb054)

~~~diff
- 004bb014 ["INT_ADD", "register:40f0:8", ["const:4bb014:8", "const:4:8"]]
- 004bb014 ["CALL", null, ["callee:00c58dc0:8"]]
+ 004bb054 ["INT_ADD", "register:40f0:8", ["const:4bb054:8", "const:4:8"]]
+ 004bb054 ["CALL", null, ["callee:00c58dc0:8"]]
- 004bb014 bytes 37771e94
+ 004bb054 bytes 5b771e94
~~~


<a id="compare-1fe69dfe716a143ce0bfbd372b68fd9a"></a>

### [`004bb038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb038.md) → [`004bb078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb078.md) _ZNK5Botan6BigInt3cmpERKS0_b

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md) · 呼出先 1件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md)
- 新版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58bf0.md) · 呼出先 1件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb038.md#insn-004bb0c8)
- 新版 [`004bb108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb078.md#insn-004bb108)

~~~diff
- 004bb0c8 ["INT_ADD", "register:40f0:8", ["const:4bb0c8:8", "const:4:8"]]
- 004bb0c8 ["CALL", null, ["callee:004b87f4:8"]]
+ 004bb108 ["INT_ADD", "register:40f0:8", ["const:4bb108:8", "const:4:8"]]
+ 004bb108 ["CALL", null, ["callee:004b87f4:8"]]
- 004bb0c8 bytes bbf5ff97
+ 004bb108 bytes bbf5ff97
~~~


<a id="compare-0716e328a77080c90e897b9debd4f805"></a>

### [`004bb57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb57c.md) → [`004bb5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb5bc.md) _ZN5Botan6BigInt7set_bitEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb57c.md#insn-004bb5cc)
- 新版 [`004bb60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb5bc.md#insn-004bb60c)

~~~diff
- 004bb5cc ["INT_ADD", "register:40f0:8", ["const:4bb5cc:8", "const:4:8"]]
- 004bb5cc ["CALL", null, ["callee:00540960:8"]]
+ 004bb60c ["INT_ADD", "register:40f0:8", ["const:4bb60c:8", "const:4:8"]]
+ 004bb60c ["CALL", null, ["callee:00540960:8"]]
- 004bb5cc bytes d5140294
+ 004bb60c bytes d5140294
~~~


<a id="compare-7c3130720463782fb7371428b7e08860"></a>

### [`004bb62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb62c.md) → [`004bb66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb66c.md) _ZNK5Botan6BigIntngEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb62c.md#insn-004bb644)
- 新版 [`004bb684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb66c.md#insn-004bb684)

~~~diff
- 004bb644 ["INT_ADD", "register:40f0:8", ["const:4bb644:8", "const:4:8"]]
- 004bb644 ["CALL", null, ["callee:00c58c10:8"]]
+ 004bb684 ["INT_ADD", "register:40f0:8", ["const:4bb684:8", "const:4:8"]]
+ 004bb684 ["CALL", null, ["callee:00c58c10:8"]]
- 004bb644 bytes 3f751e94
+ 004bb684 bytes 63751e94
~~~


<a id="compare-628c767e775e53003327103901eb51e3"></a>

### [`004bb6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb6a4.md) → [`004bb6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb6e4.md) _ZNK5Botan6BigInt3absEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bb6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb6a4.md#insn-004bb6bc)
- 新版 [`004bb6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb6e4.md#insn-004bb6fc)

~~~diff
- 004bb6bc ["INT_ADD", "register:40f0:8", ["const:4bb6bc:8", "const:4:8"]]
- 004bb6bc ["CALL", null, ["callee:00c58c10:8"]]
+ 004bb6fc ["INT_ADD", "register:40f0:8", ["const:4bb6fc:8", "const:4:8"]]
+ 004bb6fc ["CALL", null, ["callee:00c58c10:8"]]
- 004bb6bc bytes 21751e94
+ 004bb6fc bytes 45751e94
~~~


<a id="compare-6b85453cc447db39cf994d93c777609e"></a>

### [`004bbf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbf18.md) → [`004bbf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md) FUN_004bbf58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004c130c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bbf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbf18.md#insn-004bbf64) · [`004bbf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbf18.md#insn-004bbf74) · [`004bbfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbf18.md#insn-004bbfb0)
- 新版 [`004bbfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbfa4) · [`004bbfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbfb4) · [`004bbff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md#insn-004bbff0)

~~~diff
- 004bbf64 ["INT_ADD", "register:40f0:8", ["const:4bbf64:8", "const:4:8"]]
- 004bbf64 ["CALL", null, ["callee:00c57f80:8"]]
+ 004bbfa4 ["INT_ADD", "register:40f0:8", ["const:4bbfa4:8", "const:4:8"]]
+ 004bbfa4 ["CALL", null, ["callee:00c57f80:8"]]
- 004bbf64 bytes d36f1e94
+ 004bbfa4 bytes f76f1e94
- 004bbf74 ["INT_ADD", "register:40f0:8", ["const:4bbf74:8", "const:4:8"]]
- 004bbf74 ["CALL", null, ["callee:00c57f80:8"]]
+ 004bbfb4 ["INT_ADD", "register:40f0:8", ["const:4bbfb4:8", "const:4:8"]]
+ 004bbfb4 ["CALL", null, ["callee:00c57f80:8"]]
- 004bbf74 bytes cf6f1e94
+ 004bbfb4 bytes f36f1e94
- 004bbfb0 ["INT_ADD", "register:40f0:8", ["const:4bbfb0:8", "const:4:8"]]
- 004bbfb0 ["CALL", null, ["callee:00c57f80:8"]]
+ 004bbff0 ["INT_ADD", "register:40f0:8", ["const:4bbff0:8", "const:4:8"]]
+ 004bbff0 ["CALL", null, ["callee:00c57f80:8"]]
- 004bbfb0 bytes c06f1e94
+ 004bbff0 bytes e46f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577b21ba0ef44adb6f2b5ab4be95ba87"></a>

### [`004bc114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md) → [`004bc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md) _ZN5Botan11BlockCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004bc278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004bc2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md#insn-004bc184) · [`004bc194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md#insn-004bc194) · [`004bc1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md#insn-004bc1d0)
- 新版 [`004bc1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc1c4) · [`004bc1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc1d4) · [`004bc210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md#insn-004bc210)

~~~diff
- 004bc184 ["INT_ADD", "register:40f0:8", ["const:4bc184:8", "const:4:8"]]
- 004bc184 ["CALL", null, ["callee:00473580:8"]]
+ 004bc1c4 ["INT_ADD", "register:40f0:8", ["const:4bc1c4:8", "const:4:8"]]
+ 004bc1c4 ["CALL", null, ["callee:00473580:8"]]
- 004bc184 bytes efdcfe97
+ 004bc1c4 bytes efdcfe97
- 004bc194 ["INT_ADD", "register:40f0:8", ["const:4bc194:8", "const:4:8"]]
- 004bc194 ["CALL", null, ["callee:004bc2b8:8"]]
+ 004bc1d4 ["INT_ADD", "register:40f0:8", ["const:4bc1d4:8", "const:4:8"]]
+ 004bc1d4 ["CALL", null, ["callee:004bc2b8:8"]]
- 004bc194 bytes 39000094
+ 004bc1d4 bytes 39000094
- 004bc1d0 ["INT_ADD", "register:40f0:8", ["const:4bc1d0:8", "const:4:8"]]
- 004bc1d0 ["CALL", null, ["callee:00c57f80:8"]]
+ 004bc210 ["INT_ADD", "register:40f0:8", ["const:4bc210:8", "const:4:8"]]
+ 004bc210 ["CALL", null, ["callee:00c57f80:8"]]
- 004bc1d0 bytes 386f1e94
+ 004bc210 bytes 5c6f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a82b40421df8d9709999c975d3ac89"></a>

### [`004bc278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md) → [`004bc2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md) FUN_004bc2b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004bc114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc114.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d30.md)
- 新版 呼出元 1件 [`004bc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc154.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md#insn-004bc2c8) · [`004bc2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md#insn-004bc2dc) · [`004bc2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc278.md#insn-004bc2f8)
- 新版 [`004bc308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc308) · [`004bc31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc31c) · [`004bc338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc2b8.md#insn-004bc338)

~~~diff
- 004bc2c8 ["INT_ADD", "register:40f0:8", ["const:4bc2c8:8", "const:4:8"]]
- 004bc2c8 ["CALL", null, ["callee:00540dbc:8"]]
+ 004bc308 ["INT_ADD", "register:40f0:8", ["const:4bc308:8", "const:4:8"]]
+ 004bc308 ["CALL", null, ["callee:00540dbc:8"]]
- 004bc2c8 bytes ad120294
+ 004bc308 bytes ad120294
- 004bc2dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc2dc ["INT_ADD", "register:40f0:8", ["const:4bc2dc:8", "const:4:8"]]
- 004bc2dc ["CALLIND", null, ["register:0:8"]]
+ 004bc31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc31c ["INT_ADD", "register:40f0:8", ["const:4bc31c:8", "const:4:8"]]
+ 004bc31c ["CALLIND", null, ["register:0:8"]]
- 004bc2dc bytes 00013fd6
+ 004bc31c bytes 00013fd6
- 004bc2f8 ["INT_ADD", "register:40f0:8", ["const:4bc2f8:8", "const:4:8"]]
- 004bc2f8 ["CALL", null, ["callee:00c58e00:8"]]
+ 004bc338 ["INT_ADD", "register:40f0:8", ["const:4bc338:8", "const:4:8"]]
+ 004bc338 ["CALL", null, ["callee:00c58e00:8"]]
- 004bc2f8 bytes 8e721e94
+ 004bc338 bytes b2721e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88434a8d1ff2a5e6396d16cae1051e00"></a>

### [`004bc6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc6e0.md) → [`004bc720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc720.md) _ZN5Botan8CBC_Mode5clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc6e0.md#insn-004bc6fc)
- 新版 [`004bc73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc720.md#insn-004bc73c)

~~~diff
- 004bc6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc6fc ["INT_ADD", "register:40f0:8", ["const:4bc6fc:8", "const:4:8"]]
- 004bc6fc ["CALLIND", null, ["register:0:8"]]
+ 004bc73c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc73c ["INT_ADD", "register:40f0:8", ["const:4bc73c:8", "const:4:8"]]
+ 004bc73c ["CALLIND", null, ["register:0:8"]]
- 004bc6fc bytes 00013fd6
+ 004bc73c bytes 00013fd6
~~~


<a id="compare-4b87a7992a963c963e233bee94a35ab8"></a>

### [`004bc97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc97c.md) → [`004bc9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md) _ZNK5Botan8CBC_Mode18update_granularityEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bc998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc97c.md#insn-004bc998) · [`004bc9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc97c.md#insn-004bc9ac)
- 新版 [`004bc9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md#insn-004bc9d8) · [`004bc9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc9bc.md#insn-004bc9ec)

~~~diff
- 004bc998 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc998 ["INT_ADD", "register:40f0:8", ["const:4bc998:8", "const:4:8"]]
- 004bc998 ["CALLIND", null, ["register:0:8"]]
+ 004bc9d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc9d8 ["INT_ADD", "register:40f0:8", ["const:4bc9d8:8", "const:4:8"]]
+ 004bc9d8 ["CALLIND", null, ["register:0:8"]]
- 004bc998 bytes 00013fd6
+ 004bc9d8 bytes 00013fd6
- 004bc9ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004bc9ac ["INT_ADD", "register:40f0:8", ["const:4bc9ac:8", "const:4:8"]]
- 004bc9ac ["CALLIND", null, ["register:0:8"]]
+ 004bc9ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc9ec ["INT_ADD", "register:40f0:8", ["const:4bc9ec:8", "const:4:8"]]
+ 004bc9ec ["CALLIND", null, ["register:0:8"]]
- 004bc9ac bytes 00013fd6
+ 004bc9ec bytes 00013fd6
~~~


<a id="compare-e7cae63f68f70ebd3a009226ebf91883"></a>

### [`004bdd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdd68.md) → [`004bdda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bdda8.md) _ZN5Botan14CBC_Decryption5resetEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bdd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdd68.md#insn-004bdd8c)
- 新版 [`004bddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bdda8.md#insn-004bddcc)

~~~diff
- 004bdd8c ["INT_ADD", "register:40f0:8", ["const:4bdd8c:8", "const:4:8"]]
- 004bdd8c ["CALL", null, ["callee:00c58160:8"]]
+ 004bddcc ["INT_ADD", "register:40f0:8", ["const:4bddcc:8", "const:4:8"]]
+ 004bddcc ["CALL", null, ["callee:00c58160:8"]]
- 004bdd8c bytes c1681e94
+ 004bddcc bytes e5681e94
~~~


<a id="compare-7875ed439cf304e7d6c39b507c60fa87"></a>

### [`004bead4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bead4.md) → [`004beb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md) _ZN5Botan11string_joinERKNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004beb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bead4.md#insn-004beb20) · [`004beb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bead4.md#insn-004beb48)
- 新版 [`004beb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md#insn-004beb60) · [`004beb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beb14.md#insn-004beb88)

~~~diff
- 004beb20 ["INT_ADD", "register:40f0:8", ["const:4beb20:8", "const:4:8"]]
- 004beb20 ["CALL", null, ["callee:00c586d0:8"]]
+ 004beb60 ["INT_ADD", "register:40f0:8", ["const:4beb60:8", "const:4:8"]]
+ 004beb60 ["CALL", null, ["callee:00c586d0:8"]]
- 004beb20 bytes b8661e94
+ 004beb60 bytes dc661e94
- 004beb48 ["INT_ADD", "register:40f0:8", ["const:4beb48:8", "const:4:8"]]
- 004beb48 ["CALL", null, ["callee:00c58050:8"]]
+ 004beb88 ["INT_ADD", "register:40f0:8", ["const:4beb88:8", "const:4:8"]]
+ 004beb88 ["CALL", null, ["callee:00c58050:8"]]
- 004beb48 bytes 0e651e94
+ 004beb88 bytes 32651e94
~~~


<a id="compare-b671f34eb4d60d693313d5ca951ec1a2"></a>

### [`004bec98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec98.md) → [`004becd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md) _ZN5Botan5CPUID15bit_from_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`004beea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beea0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004beee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bed18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec98.md#insn-004bed18) · [`004bed7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec98.md#insn-004bed7c) · [`004bedc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec98.md#insn-004bedc8)
- 新版 [`004bed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bed58) · [`004bedbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bedbc) · [`004bee08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md#insn-004bee08)

~~~diff
- 004bed18 ["INT_ADD", "register:40f0:8", ["const:4bed18:8", "const:4:8"]]
- 004bed18 ["CALL", null, ["callee:00c57f60:8"]]
+ 004bed58 ["INT_ADD", "register:40f0:8", ["const:4bed58:8", "const:4:8"]]
+ 004bed58 ["CALL", null, ["callee:00c57f60:8"]]
- 004bed18 bytes 5e641e94
+ 004bed58 bytes 82641e94
- 004bed7c ["INT_ADD", "register:40f0:8", ["const:4bed7c:8", "const:4:8"]]
- 004bed7c ["CALL", null, ["callee:004beee0:8"]]
+ 004bedbc ["INT_ADD", "register:40f0:8", ["const:4bedbc:8", "const:4:8"]]
+ 004bedbc ["CALL", null, ["callee:004beee0:8"]]
- 004bed7c bytes 49000094
+ 004bedbc bytes 49000094
- 004bedc8 ["INT_ADD", "register:40f0:8", ["const:4bedc8:8", "const:4:8"]]
- 004bedc8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004bee08 ["INT_ADD", "register:40f0:8", ["const:4bee08:8", "const:4:8"]]
+ 004bee08 ["CALL", null, ["callee:00c57f60:8"]]
- 004bedc8 bytes 32641e94
+ 004bee08 bytes 56641e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e9ee9023a917a1ae497881bdaa1015"></a>

### [`004beea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beea0.md) → [`004beee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md) FUN_004beee0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004bec98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec98.md) · 呼出先 5件 [`005439c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005439c0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`004becd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becd8.md) · 呼出先 5件 [`00543a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004beed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beea0.md#insn-004beed4) · [`004beeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beea0.md#insn-004beeec) · [`004bef08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beea0.md#insn-004bef08)
- 新版 [`004bef14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef14) · [`004bef2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef2c) · [`004bef48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md#insn-004bef48)

~~~diff
- 004beed4 ["INT_ADD", "register:40f0:8", ["const:4beed4:8", "const:4:8"]]
- 004beed4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004bef14 ["INT_ADD", "register:40f0:8", ["const:4bef14:8", "const:4:8"]]
+ 004bef14 ["CALL", null, ["callee:00c57f60:8"]]
- 004beed4 bytes ef631e94
+ 004bef14 bytes 13641e94
- 004beeec ["INT_ADD", "register:40f0:8", ["const:4beeec:8", "const:4:8"]]
- 004beeec ["CALL", null, ["callee:00c58010:8"]]
+ 004bef2c ["INT_ADD", "register:40f0:8", ["const:4bef2c:8", "const:4:8"]]
+ 004bef2c ["CALL", null, ["callee:00c58010:8"]]
- 004beeec bytes 15641e94
+ 004bef2c bytes 39641e94
- 004bef08 ["INT_ADD", "register:40f0:8", ["const:4bef08:8", "const:4:8"]]
- 004bef08 ["CALL", null, ["callee:00543a00:8"]]
+ 004bef48 ["INT_ADD", "register:40f0:8", ["const:4bef48:8", "const:4:8"]]
+ 004bef48 ["CALL", null, ["callee:00543a00:8"]]
- 004bef08 bytes ae120294
+ 004bef48 bytes ae120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc520ff7e7191d261b65c6e10fb22ae"></a>

### [`004bf3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf3d8.md) → [`004bf418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md) _ZNK5Botan8ECB_Mode18update_granularityEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bf3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf3d8.md#insn-004bf3f4) · [`004bf408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf3d8.md#insn-004bf408)
- 新版 [`004bf434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md#insn-004bf434) · [`004bf448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf418.md#insn-004bf448)

~~~diff
- 004bf3f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf3f4 ["INT_ADD", "register:40f0:8", ["const:4bf3f4:8", "const:4:8"]]
- 004bf3f4 ["CALLIND", null, ["register:0:8"]]
+ 004bf434 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf434 ["INT_ADD", "register:40f0:8", ["const:4bf434:8", "const:4:8"]]
+ 004bf434 ["CALLIND", null, ["register:0:8"]]
- 004bf3f4 bytes 00013fd6
+ 004bf434 bytes 00013fd6
- 004bf408 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf408 ["INT_ADD", "register:40f0:8", ["const:4bf408:8", "const:4:8"]]
- 004bf408 ["CALLIND", null, ["register:0:8"]]
+ 004bf448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf448 ["INT_ADD", "register:40f0:8", ["const:4bf448:8", "const:4:8"]]
+ 004bf448 ["CALLIND", null, ["register:0:8"]]
- 004bf408 bytes 00013fd6
+ 004bf448 bytes 00013fd6
~~~


<a id="compare-932f3e561be1c28fbb0c23c482705537"></a>

### [`004bfc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfc40.md) → [`004bfc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md) _ZN5Botan13EMSA_PKCS1v158raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bfc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfc40.md#insn-004bfc60) · [`004bfc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfc40.md#insn-004bfc6c) · [`004bfc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfc40.md#insn-004bfc80)
- 新版 [`004bfca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfca0) · [`004bfcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfcac) · [`004bfcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfc80.md#insn-004bfcc0)

~~~diff
- 004bfc60 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bfc60 ["INT_ADD", "register:40f0:8", ["const:4bfc60:8", "const:4:8"]]
- 004bfc60 ["CALLIND", null, ["register:0:8"]]
+ 004bfca0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bfca0 ["INT_ADD", "register:40f0:8", ["const:4bfca0:8", "const:4:8"]]
+ 004bfca0 ["CALLIND", null, ["register:0:8"]]
- 004bfc60 bytes 20013fd6
+ 004bfca0 bytes 20013fd6
- 004bfc6c ["INT_ADD", "register:40f0:8", ["const:4bfc6c:8", "const:4:8"]]
- 004bfc6c ["CALL", null, ["callee:004b3548:8"]]
+ 004bfcac ["INT_ADD", "register:40f0:8", ["const:4bfcac:8", "const:4:8"]]
+ 004bfcac ["CALL", null, ["callee:004b3548:8"]]
- 004bfc6c bytes 27ceff97
+ 004bfcac bytes 27ceff97
- 004bfc80 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfc80 ["INT_ADD", "register:40f0:8", ["const:4bfc80:8", "const:4:8"]]
- 004bfc80 ["CALLIND", null, ["register:0:8"]]
+ 004bfcc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfcc0 ["INT_ADD", "register:40f0:8", ["const:4bfcc0:8", "const:4:8"]]
+ 004bfcc0 ["CALLIND", null, ["register:0:8"]]
- 004bfc80 bytes 00013fd6
+ 004bfcc0 bytes 00013fd6
~~~


<a id="compare-a49b2b69f70e38e4c642ee0b52bd8b51"></a>

### [`004bfca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md) → [`004bfce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md) FUN_004bfce4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c1e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md) · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)
- 新版 呼出元 1件 [`004c1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md) · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004bfcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md#insn-004bfcc0) · [`004bfccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md#insn-004bfccc) · [`004bfce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md#insn-004bfce0)
- 新版 [`004bfd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd00) · [`004bfd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd0c) · [`004bfd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md#insn-004bfd20)

~~~diff
- 004bfcc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bfcc0 ["INT_ADD", "register:40f0:8", ["const:4bfcc0:8", "const:4:8"]]
- 004bfcc0 ["CALLIND", null, ["register:0:8"]]
+ 004bfd00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bfd00 ["INT_ADD", "register:40f0:8", ["const:4bfd00:8", "const:4:8"]]
+ 004bfd00 ["CALLIND", null, ["register:0:8"]]
- 004bfcc0 bytes 20013fd6
+ 004bfd00 bytes 20013fd6
- 004bfccc ["INT_ADD", "register:40f0:8", ["const:4bfccc:8", "const:4:8"]]
- 004bfccc ["CALL", null, ["callee:004b3548:8"]]
+ 004bfd0c ["INT_ADD", "register:40f0:8", ["const:4bfd0c:8", "const:4:8"]]
+ 004bfd0c ["CALL", null, ["callee:004b3548:8"]]
- 004bfccc bytes 0fceff97
+ 004bfd0c bytes 0fceff97
- 004bfce0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfce0 ["INT_ADD", "register:40f0:8", ["const:4bfce0:8", "const:4:8"]]
- 004bfce0 ["CALLIND", null, ["register:0:8"]]
+ 004bfd20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfd20 ["INT_ADD", "register:40f0:8", ["const:4bfd20:8", "const:4:8"]]
+ 004bfd20 ["CALLIND", null, ["register:0:8"]]
- 004bfce0 bytes 00013fd6
+ 004bfd20 bytes 00013fd6
~~~


<a id="compare-cce4b7eeb8bf7d19ef732d770bdfc449"></a>

### [`004c0704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0704.md) → [`004c0744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0744.md) FUN_004c0744

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c0770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0704.md#insn-004c0770)
- 新版 [`004c07b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0744.md#insn-004c07b0)

~~~diff
- 004c0770 ["INT_ADD", "register:40f0:8", ["const:4c0770:8", "const:4:8"]]
- 004c0770 ["CALL", null, ["callee:00c58120:8"]]
+ 004c07b0 ["INT_ADD", "register:40f0:8", ["const:4c07b0:8", "const:4:8"]]
+ 004c07b0 ["CALL", null, ["callee:00c58120:8"]]
- 004c0770 bytes 385e1e94
+ 004c07b0 bytes 5c5e1e94
~~~


<a id="compare-901b38dc34b60133c186016f083102ec"></a>

### [`004c07b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md) → [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) FUN_004c07f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004c0188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md) [`004c24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58dd0.md)
- 新版 呼出元 2件 [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c0800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md#insn-004c0800) · [`004c080c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md#insn-004c080c) · [`004c081c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md#insn-004c081c)
- 新版 [`004c0840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c0840) · [`004c084c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c084c) · [`004c085c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md#insn-004c085c)

~~~diff
- 004c0800 ["INT_ADD", "register:40f0:8", ["const:4c0800:8", "const:4:8"]]
- 004c0800 ["CALL", null, ["callee:0043bb60:8"]]
+ 004c0840 ["INT_ADD", "register:40f0:8", ["const:4c0840:8", "const:4:8"]]
+ 004c0840 ["CALL", null, ["callee:0043bb60:8"]]
- 004c0800 bytes c8ecfd97
+ 004c0840 bytes c8ecfd97
- 004c080c ["INT_ADD", "register:40f0:8", ["const:4c080c:8", "const:4:8"]]
- 004c080c ["CALL", null, ["callee:00c58ea0:8"]]
+ 004c084c ["INT_ADD", "register:40f0:8", ["const:4c084c:8", "const:4:8"]]
+ 004c084c ["CALL", null, ["callee:00c58ea0:8"]]
- 004c080c bytes 71611e94
+ 004c084c bytes 95611e94
- 004c081c ["INT_ADD", "register:40f0:8", ["const:4c081c:8", "const:4:8"]]
- 004c081c ["CALL", null, ["callee:00c57f80:8"]]
+ 004c085c ["INT_ADD", "register:40f0:8", ["const:4c085c:8", "const:4:8"]]
+ 004c085c ["CALL", null, ["callee:00c57f80:8"]]
- 004c081c bytes a55d1e94
+ 004c085c bytes c95d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660c50e4ce71bb17d7ea66c776bebbd3"></a>

### [`004c0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md) → [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) FUN_004c0ab8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c0a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md#insn-004c0a94)
- 新版 [`004c0ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md#insn-004c0ad4)

~~~diff
- 004c0a94 ["INT_ADD", "register:40f0:8", ["const:4c0a94:8", "const:4:8"]]
- 004c0a94 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c0ad4 ["INT_ADD", "register:40f0:8", ["const:4c0ad4:8", "const:4:8"]]
+ 004c0ad4 ["CALL", null, ["callee:00c57f80:8"]]
- 004c0a94 bytes 075d1e94
+ 004c0ad4 bytes 2b5d1e94
~~~


<a id="compare-448ca5468c75596f5395f59ce89a9f35"></a>

### [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) → [`004c130c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md) _ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004bbf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbf18.md) [`004cb72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb72c.md) [`004cb8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb8e8.md) [`004cba9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md)
- 新版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004bbf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbf58.md) [`004cb76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb76c.md) [`004cb928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb928.md) [`004cbadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbadc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md#insn-004c1404) · [`004c140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md#insn-004c140c) · [`004c1440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md#insn-004c1440)
- 新版 [`004c1444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c1444) · [`004c144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c144c) · [`004c1480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c130c.md#insn-004c1480)

~~~diff
- 004c1404 ["INT_ADD", "register:40f0:8", ["const:4c1404:8", "const:4:8"]]
- 004c1404 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c1444 ["INT_ADD", "register:40f0:8", ["const:4c1444:8", "const:4:8"]]
+ 004c1444 ["CALL", null, ["callee:00c57f60:8"]]
- 004c1404 bytes a35a1e94
+ 004c1444 bytes c75a1e94
- 004c140c ["INT_ADD", "register:40f0:8", ["const:4c140c:8", "const:4:8"]]
- 004c140c ["CALL", null, ["callee:004cbadc:8"]]
+ 004c144c ["INT_ADD", "register:40f0:8", ["const:4c144c:8", "const:4:8"]]
+ 004c144c ["CALL", null, ["callee:004cbadc:8"]]
- 004c140c bytes a4290094
+ 004c144c bytes a4290094
- 004c1440 ["INT_ADD", "register:40f0:8", ["const:4c1440:8", "const:4:8"]]
- 004c1440 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c1480 ["INT_ADD", "register:40f0:8", ["const:4c1480:8", "const:4:8"]]
+ 004c1480 ["CALL", null, ["callee:00c57f60:8"]]
- 004c1440 bytes 945a1e94
+ 004c1480 bytes b85a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b43ce9b9accdb6656f1522633dbb1f8"></a>

### [`004c1560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1560.md) → [`004c15a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c15a0.md) _ZN5Botan17EMSA_PKCS1v15_Raw6updateEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c1598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1560.md#insn-004c1598)
- 新版 [`004c15d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c15a0.md#insn-004c15d8)

~~~diff
- 004c1598 ["INT_ADD", "register:40f0:8", ["const:4c1598:8", "const:4:8"]]
- 004c1598 ["CALL", null, ["callee:0054052c:8"]]
+ 004c15d8 ["INT_ADD", "register:40f0:8", ["const:4c15d8:8", "const:4:8"]]
+ 004c15d8 ["CALL", null, ["callee:0054052c:8"]]
- 004c1598 bytes d5fb0194
+ 004c15d8 bytes d5fb0194
~~~


<a id="compare-fd867bdaa88c701771cec338e29b32e0"></a>

### [`004c18b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c18b0.md) → [`004c18f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md) _ZN5Botan4PSSR8raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c18b0.md#insn-004c18d0) · [`004c18dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c18b0.md#insn-004c18dc) · [`004c18f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c18b0.md#insn-004c18f0)
- 新版 [`004c1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c1910) · [`004c191c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c191c) · [`004c1930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c18f0.md#insn-004c1930)

~~~diff
- 004c18d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c18d0 ["INT_ADD", "register:40f0:8", ["const:4c18d0:8", "const:4:8"]]
- 004c18d0 ["CALLIND", null, ["register:0:8"]]
+ 004c1910 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1910 ["INT_ADD", "register:40f0:8", ["const:4c1910:8", "const:4:8"]]
+ 004c1910 ["CALLIND", null, ["register:0:8"]]
- 004c18d0 bytes 20013fd6
+ 004c1910 bytes 20013fd6
- 004c18dc ["INT_ADD", "register:40f0:8", ["const:4c18dc:8", "const:4:8"]]
- 004c18dc ["CALL", null, ["callee:004b3548:8"]]
+ 004c191c ["INT_ADD", "register:40f0:8", ["const:4c191c:8", "const:4:8"]]
+ 004c191c ["CALL", null, ["callee:004b3548:8"]]
- 004c18dc bytes 0bc7ff97
+ 004c191c bytes 0bc7ff97
- 004c18f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c18f0 ["INT_ADD", "register:40f0:8", ["const:4c18f0:8", "const:4:8"]]
- 004c18f0 ["CALLIND", null, ["register:0:8"]]
+ 004c1930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1930 ["INT_ADD", "register:40f0:8", ["const:4c1930:8", "const:4:8"]]
+ 004c1930 ["CALLIND", null, ["register:0:8"]]
- 004c18f0 bytes 00013fd6
+ 004c1930 bytes 00013fd6
~~~


<a id="compare-9dae550c6f36526a0214b3bf43222bee"></a>

### [`004c32ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c32ec.md) → [`004c332c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md) _ZN5Botan15Entropy_Sources10add_sourceENSt6__ndk110unique_ptrINS_14Entropy_SourceENS1_14default_deleteIS3_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e30.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00543c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c58f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f00.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00543c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c32ec.md#insn-004c3370) · [`004c33a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c32ec.md#insn-004c33a8) · [`004c33bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c32ec.md#insn-004c33bc)
- 新版 [`004c33b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33b0) · [`004c33e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33e8) · [`004c33fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md#insn-004c33fc)

~~~diff
- 004c3370 ["INT_ADD", "register:40f0:8", ["const:4c3370:8", "const:4:8"]]
- 004c3370 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c33b0 ["INT_ADD", "register:40f0:8", ["const:4c33b0:8", "const:4:8"]]
+ 004c33b0 ["CALL", null, ["callee:00c57f60:8"]]
- 004c3370 bytes c8521e94
+ 004c33b0 bytes ec521e94
- 004c33a8 ["INT_ADD", "register:40f0:8", ["const:4c33a8:8", "const:4:8"]]
- 004c33a8 ["CALL", null, ["callee:00c580d0:8"]]
+ 004c33e8 ["INT_ADD", "register:40f0:8", ["const:4c33e8:8", "const:4:8"]]
+ 004c33e8 ["CALL", null, ["callee:00c580d0:8"]]
- 004c33a8 bytes 16531e94
+ 004c33e8 bytes 3a531e94
- 004c33bc ["INT_ADD", "register:40f0:8", ["const:4c33bc:8", "const:4:8"]]
- 004c33bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004c33fc ["INT_ADD", "register:40f0:8", ["const:4c33fc:8", "const:4:8"]]
+ 004c33fc ["CALL", null, ["callee:00c57f80:8"]]
- 004c33bc bytes bd521e94
+ 004c33fc bytes e1521e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c93162c54ea28965fcd71f46815338"></a>

### [`004c33e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c33e4.md) → [`004c3424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md) _ZNK5Botan15Entropy_Sources15enabled_sourcesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c33e4.md#insn-004c3488) · [`004c34f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c33e4.md#insn-004c34f0) · [`004c3534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c33e4.md#insn-004c3534)
- 新版 [`004c34c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c34c8) · [`004c3530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c3530) · [`004c3574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3424.md#insn-004c3574)

~~~diff
- 004c3488 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c3488 ["INT_ADD", "register:40f0:8", ["const:4c3488:8", "const:4:8"]]
- 004c3488 ["CALLIND", null, ["register:0:8"]]
+ 004c34c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c34c8 ["INT_ADD", "register:40f0:8", ["const:4c34c8:8", "const:4:8"]]
+ 004c34c8 ["CALLIND", null, ["register:0:8"]]
- 004c3488 bytes 20013fd6
+ 004c34c8 bytes 20013fd6
- 004c34f0 ["INT_ADD", "register:40f0:8", ["const:4c34f0:8", "const:4:8"]]
- 004c34f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c3530 ["INT_ADD", "register:40f0:8", ["const:4c3530:8", "const:4:8"]]
+ 004c3530 ["CALL", null, ["callee:00c57f60:8"]]
- 004c34f0 bytes 68521e94
+ 004c3530 bytes 8c521e94
- 004c3534 ["INT_ADD", "register:40f0:8", ["const:4c3534:8", "const:4:8"]]
- 004c3534 ["CALL", null, ["callee:00c580d0:8"]]
+ 004c3574 ["INT_ADD", "register:40f0:8", ["const:4c3574:8", "const:4:8"]]
+ 004c3574 ["CALL", null, ["callee:00c580d0:8"]]
- 004c3534 bytes b3521e94
+ 004c3574 bytes d7521e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f3c642d14a1597bc83dd2330ce594d"></a>

### [`004c362c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c362c.md) → [`004c366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md) _ZN5Botan15Entropy_Sources4pollERNS_21RandomNumberGeneratorEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c362c.md#insn-004c3650) · [`004c3680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c362c.md#insn-004c3680) · [`004c3690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c362c.md#insn-004c3690)
- 新版 [`004c3690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c3690) · [`004c36c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c36c0) · [`004c36d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c366c.md#insn-004c36d0)

~~~diff
- 004c3650 ["INT_ADD", "register:40f0:8", ["const:4c3650:8", "const:4:8"]]
- 004c3650 ["CALL", null, ["callee:00c58650:8"]]
+ 004c3690 ["INT_ADD", "register:40f0:8", ["const:4c3690:8", "const:4:8"]]
+ 004c3690 ["CALL", null, ["callee:00c58650:8"]]
- 004c3650 bytes cc531e94
+ 004c3690 bytes f0531e94
- 004c3680 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c3680 ["INT_ADD", "register:40f0:8", ["const:4c3680:8", "const:4:8"]]
- 004c3680 ["CALLIND", null, ["register:0:8"]]
+ 004c36c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c36c0 ["INT_ADD", "register:40f0:8", ["const:4c36c0:8", "const:4:8"]]
+ 004c36c0 ["CALLIND", null, ["register:0:8"]]
- 004c3680 bytes 00013fd6
+ 004c36c0 bytes 00013fd6
- 004c3690 ["INT_ADD", "register:40f0:8", ["const:4c3690:8", "const:4:8"]]
- 004c3690 ["CALL", null, ["callee:00c58650:8"]]
+ 004c36d0 ["INT_ADD", "register:40f0:8", ["const:4c36d0:8", "const:4:8"]]
+ 004c36d0 ["CALL", null, ["callee:00c58650:8"]]
- 004c3690 bytes bc531e94
+ 004c36d0 bytes e0531e94
~~~


<a id="compare-d3150d2f7f60182dc51fb73a24ed0452"></a>

### [`004c36d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c36d0.md) → [`004c3710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md) _ZN5Botan15Entropy_Sources9poll_justERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c36d0.md#insn-004c372c) · [`004c3738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c36d0.md#insn-004c3738) · [`004c3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c36d0.md#insn-004c3764)
- 新版 [`004c376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c376c) · [`004c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c3778) · [`004c37a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3710.md#insn-004c37a4)

~~~diff
- 004c372c ["INT_ADD", "register:40f0:8", ["const:4c372c:8", "const:4:8"]]
- 004c372c ["CALL", null, ["callee:00c58120:8"]]
+ 004c376c ["INT_ADD", "register:40f0:8", ["const:4c376c:8", "const:4:8"]]
+ 004c376c ["CALL", null, ["callee:00c58120:8"]]
- 004c372c bytes 49521e94
+ 004c376c bytes 6d521e94
- 004c3738 ["INT_ADD", "register:40f0:8", ["const:4c3738:8", "const:4:8"]]
- 004c3738 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c3778 ["INT_ADD", "register:40f0:8", ["const:4c3778:8", "const:4:8"]]
+ 004c3778 ["CALL", null, ["callee:00c57f80:8"]]
- 004c3738 bytes de511e94
+ 004c3778 bytes 02521e94
- 004c3764 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c3764 ["INT_ADD", "register:40f0:8", ["const:4c3764:8", "const:4:8"]]
- 004c3764 ["CALLIND", null, ["register:0:8"]]
+ 004c37a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c37a4 ["INT_ADD", "register:40f0:8", ["const:4c37a4:8", "const:4:8"]]
+ 004c37a4 ["CALLIND", null, ["register:0:8"]]
- 004c3764 bytes 20013fd6
+ 004c37a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946b6e212b75ad4f4fbff73a86cf703d"></a>

### [`004c3850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3850.md) → [`004c3890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3890.md) FUN_004c3890

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 3件 [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c38bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3850.md#insn-004c38bc)
- 新版 [`004c38fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3890.md#insn-004c38fc)

~~~diff
- 004c38bc ["INT_ADD", "register:40f0:8", ["const:4c38bc:8", "const:4:8"]]
- 004c38bc ["CALL", null, ["callee:00c58120:8"]]
+ 004c38fc ["INT_ADD", "register:40f0:8", ["const:4c38fc:8", "const:4:8"]]
+ 004c38fc ["CALL", null, ["callee:00c58120:8"]]
- 004c38bc bytes e5511e94
+ 004c38fc bytes 09521e94
~~~


<a id="compare-5e18cd139a80ad2d9df8b6fb67a833c0"></a>

### [`004c3ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3ac0.md) → [`004c3b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b00.md) FUN_004c3b00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3ac0.md#insn-004c3b0c)
- 新版 [`004c3b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b00.md#insn-004c3b4c)

~~~diff
- 004c3b0c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c3b0c ["INT_ADD", "register:40f0:8", ["const:4c3b0c:8", "const:4:8"]]
- 004c3b0c ["CALLIND", null, ["register:0:8"]]
+ 004c3b4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3b4c ["INT_ADD", "register:40f0:8", ["const:4c3b4c:8", "const:4:8"]]
+ 004c3b4c ["CALLIND", null, ["register:0:8"]]
- 004c3b0c bytes 00013fd6
+ 004c3b4c bytes 00013fd6
~~~


<a id="compare-de443daddbd26afe843da8a03e36babe"></a>

### [`004c3e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3e9c.md) → [`004c3edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md) FUN_004c3edc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c3ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3e9c.md#insn-004c3ee8)
- 新版 [`004c3f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md#insn-004c3f28)

~~~diff
- 004c3ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c3ee8 ["INT_ADD", "register:40f0:8", ["const:4c3ee8:8", "const:4:8"]]
- 004c3ee8 ["CALLIND", null, ["register:0:8"]]
+ 004c3f28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3f28 ["INT_ADD", "register:40f0:8", ["const:4c3f28:8", "const:4:8"]]
+ 004c3f28 ["CALLIND", null, ["register:0:8"]]
- 004c3ee8 bytes 00013fd6
+ 004c3f28 bytes 00013fd6
~~~


<a id="compare-f6dfb5f39440ad7527d521e00075daa0"></a>

### [`004c4678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4678.md) → [`004c46b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md) _ZN5Botan19StreamCipher_Filter5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c46bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4678.md#insn-004c46bc) · [`004c46d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4678.md#insn-004c46d4)
- 新版 [`004c46fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md#insn-004c46fc) · [`004c4714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c46b8.md#insn-004c4714)

~~~diff
- 004c46bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004c46bc ["INT_ADD", "register:40f0:8", ["const:4c46bc:8", "const:4:8"]]
- 004c46bc ["CALLIND", null, ["register:0:8"]]
+ 004c46fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c46fc ["INT_ADD", "register:40f0:8", ["const:4c46fc:8", "const:4:8"]]
+ 004c46fc ["CALLIND", null, ["register:0:8"]]
- 004c46bc bytes 20013fd6
+ 004c46fc bytes 20013fd6
- 004c46d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c46d4 ["INT_ADD", "register:40f0:8", ["const:4c46d4:8", "const:4:8"]]
- 004c46d4 ["CALLIND", null, ["register:0:8"]]
+ 004c4714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c4714 ["INT_ADD", "register:40f0:8", ["const:4c4714:8", "const:4:8"]]
+ 004c4714 ["CALLIND", null, ["register:0:8"]]
- 004c46d4 bytes 00013fd6
+ 004c4714 bytes 00013fd6
~~~


<a id="compare-a3ef1919eead05bc143300d031f363fb"></a>

### [`004c5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5790.md) → [`004c57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md) _ZN5Botan15Buffered_Filter5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58eb0.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f80.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c57f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5790.md#insn-004c57f0) · [`004c583c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5790.md#insn-004c583c) · [`004c5858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5790.md#insn-004c5858)
- 新版 [`004c5830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c5830) · [`004c587c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c587c) · [`004c5898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c57d0.md#insn-004c5898)

~~~diff
- 004c57f0 ["INT_ADD", "register:40f0:8", ["const:4c57f0:8", "const:4:8"]]
- 004c57f0 ["CALL", null, ["callee:00c58010:8"]]
+ 004c5830 ["INT_ADD", "register:40f0:8", ["const:4c5830:8", "const:4:8"]]
+ 004c5830 ["CALL", null, ["callee:00c58010:8"]]
- 004c57f0 bytes d4491e94
+ 004c5830 bytes f8491e94
- 004c583c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c583c ["INT_ADD", "register:40f0:8", ["const:4c583c:8", "const:4:8"]]
- 004c583c ["CALLIND", null, ["register:0:8"]]
+ 004c587c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c587c ["INT_ADD", "register:40f0:8", ["const:4c587c:8", "const:4:8"]]
+ 004c587c ["CALLIND", null, ["register:0:8"]]
- 004c583c bytes 00013fd6
+ 004c587c bytes 00013fd6
- 004c5858 ["INT_ADD", "register:40f0:8", ["const:4c5858:8", "const:4:8"]]
- 004c5858 ["CALL", null, ["callee:00c58010:8"]]
+ 004c5898 ["INT_ADD", "register:40f0:8", ["const:4c5898:8", "const:4:8"]]
+ 004c5898 ["CALL", null, ["callee:00c58010:8"]]
- 004c5858 bytes ba491e94
+ 004c5898 bytes de491e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17409f6767289b7211df009129fb4d5c"></a>

### [`004c5fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5fec.md) → [`004c602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md) _ZN5Botan18Cipher_Mode_Filter14buffered_blockEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ed0.md) · 呼出先 2件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005433c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005433c0.md)
- 新版 呼出元 1件 [`00c58fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fa0.md) · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c601c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5fec.md#insn-004c601c) · [`004c6034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5fec.md#insn-004c6034) · [`004c6050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5fec.md#insn-004c6050)
- 新版 [`004c605c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c605c) · [`004c6074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c6074) · [`004c6090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md#insn-004c6090)

~~~diff
- 004c601c ["INT_ADD", "register:40f0:8", ["const:4c601c:8", "const:4:8"]]
- 004c601c ["CALL", null, ["callee:0054052c:8"]]
+ 004c605c ["INT_ADD", "register:40f0:8", ["const:4c605c:8", "const:4:8"]]
+ 004c605c ["CALL", null, ["callee:0054052c:8"]]
- 004c601c bytes 34e90194
+ 004c605c bytes 34e90194
- 004c6034 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6034 ["INT_ADD", "register:40f0:8", ["const:4c6034:8", "const:4:8"]]
- 004c6034 ["CALLIND", null, ["register:0:8"]]
+ 004c6074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6074 ["INT_ADD", "register:40f0:8", ["const:4c6074:8", "const:4:8"]]
+ 004c6074 ["CALLIND", null, ["register:0:8"]]
- 004c6034 bytes 00013fd6
+ 004c6074 bytes 00013fd6
- 004c6050 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6050 ["INT_ADD", "register:40f0:8", ["const:4c6050:8", "const:4:8"]]
- 004c6050 ["CALLIND", null, ["register:0:8"]]
+ 004c6090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6090 ["INT_ADD", "register:40f0:8", ["const:4c6090:8", "const:4:8"]]
+ 004c6090 ["CALLIND", null, ["register:0:8"]]
- 004c6050 bytes 00013fd6
+ 004c6090 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83cb38c42cf18bf707318ffe2023dbd4"></a>

### [`004c6788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6788.md) → [`004c67c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67c8.md) _ZN5Botan15DataSink_StreamD0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c59000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c6798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6788.md#insn-004c6798)
- 新版 [`004c67d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67c8.md#insn-004c67d8)

~~~diff
- 004c6798 ["INT_ADD", "register:40f0:8", ["const:4c6798:8", "const:4:8"]]
- 004c6798 ["CALL", null, ["callee:00c59000:8"]]
+ 004c67d8 ["INT_ADD", "register:40f0:8", ["const:4c67d8:8", "const:4:8"]]
+ 004c67d8 ["CALL", null, ["callee:00c59000:8"]]
- 004c6798 bytes e6491e94
+ 004c67d8 bytes 0a4a1e94
~~~


<a id="compare-01158582ddca51bae57785b5ab28c55c"></a>

### [`004c67ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c67ac.md) → [`004c67ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md) _ZN5Botan6Filter4sendEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f40.md) · 呼出先 2件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c59010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59010.md) · 呼出先 2件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c6818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c67ac.md#insn-004c6818) · [`004c6834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c67ac.md#insn-004c6834) · [`004c6880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c67ac.md#insn-004c6880)
- 新版 [`004c6858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c6858) · [`004c6874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c6874) · [`004c68c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c67ec.md#insn-004c68c0)

~~~diff
- 004c6818 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6818 ["INT_ADD", "register:40f0:8", ["const:4c6818:8", "const:4:8"]]
- 004c6818 ["CALLIND", null, ["register:0:8"]]
+ 004c6858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6858 ["INT_ADD", "register:40f0:8", ["const:4c6858:8", "const:4:8"]]
+ 004c6858 ["CALLIND", null, ["register:0:8"]]
- 004c6818 bytes 00013fd6
+ 004c6858 bytes 00013fd6
- 004c6834 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c6834 ["INT_ADD", "register:40f0:8", ["const:4c6834:8", "const:4:8"]]
- 004c6834 ["CALLIND", null, ["register:0:8"]]
+ 004c6874 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6874 ["INT_ADD", "register:40f0:8", ["const:4c6874:8", "const:4:8"]]
+ 004c6874 ["CALLIND", null, ["register:0:8"]]
- 004c6834 bytes 00013fd6
+ 004c6874 bytes 00013fd6
- 004c6880 ["INT_ADD", "register:40f0:8", ["const:4c6880:8", "const:4:8"]]
- 004c6880 ["CALL", null, ["callee:0054052c:8"]]
+ 004c68c0 ["INT_ADD", "register:40f0:8", ["const:4c68c0:8", "const:4:8"]]
+ 004c68c0 ["CALL", null, ["callee:0054052c:8"]]
- 004c6880 bytes 1be70194
+ 004c68c0 bytes 1be70194
~~~


<a id="compare-3e11c3268c47cfad13ea97db63438642"></a>

### [`004c68e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c68e4.md) → [`004c6924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md) _ZN5Botan6Filter7new_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f50.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f50.md)
- 新版 呼出元 1件 [`00c59020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59020.md) · 呼出先 1件 [`00c59020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c68fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c68e4.md#insn-004c68fc) · [`004c692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c68e4.md#insn-004c692c)
- 新版 [`004c693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md#insn-004c693c) · [`004c696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6924.md#insn-004c696c)

~~~diff
- 004c68fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004c68fc ["INT_ADD", "register:40f0:8", ["const:4c68fc:8", "const:4:8"]]
- 004c68fc ["CALLIND", null, ["register:0:8"]]
+ 004c693c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c693c ["INT_ADD", "register:40f0:8", ["const:4c693c:8", "const:4:8"]]
+ 004c693c ["CALLIND", null, ["register:0:8"]]
- 004c68fc bytes 00013fd6
+ 004c693c bytes 00013fd6
- 004c692c ["INT_ADD", "register:40f0:8", ["const:4c692c:8", "const:4:8"]]
- 004c692c ["CALL", null, ["callee:00c59020:8"]]
+ 004c696c ["INT_ADD", "register:40f0:8", ["const:4c696c:8", "const:4:8"]]
+ 004c696c ["CALL", null, ["callee:00c59020:8"]]
- 004c692c bytes 89491e94
+ 004c696c bytes ad491e94
~~~


<a id="compare-63efab96ee1dcc8b1c6a88ed81bbf316"></a>

### [`004c6944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6944.md) → [`004c6984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md) _ZN5Botan6Filter10finish_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f60.md) · 呼出先 1件 [`00c58f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f60.md)
- 新版 呼出元 1件 [`00c59030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59030.md) · 呼出先 1件 [`00c59030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6944.md#insn-004c695c) · [`004c698c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6944.md#insn-004c698c)
- 新版 [`004c699c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md#insn-004c699c) · [`004c69cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6984.md#insn-004c69cc)

~~~diff
- 004c695c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c695c ["INT_ADD", "register:40f0:8", ["const:4c695c:8", "const:4:8"]]
- 004c695c ["CALLIND", null, ["register:0:8"]]
+ 004c699c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c699c ["INT_ADD", "register:40f0:8", ["const:4c699c:8", "const:4:8"]]
+ 004c699c ["CALLIND", null, ["register:0:8"]]
- 004c695c bytes 00013fd6
+ 004c699c bytes 00013fd6
- 004c698c ["INT_ADD", "register:40f0:8", ["const:4c698c:8", "const:4:8"]]
- 004c698c ["CALL", null, ["callee:00c59030:8"]]
+ 004c69cc ["INT_ADD", "register:40f0:8", ["const:4c69cc:8", "const:4:8"]]
+ 004c69cc ["CALL", null, ["callee:00c59030:8"]]
- 004c698c bytes 75491e94
+ 004c69cc bytes 99491e94
~~~


<a id="compare-9ef49cc56e98f6e3c1ca01129517bdc3"></a>

### [`004c77a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c77a8.md) → [`004c77e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringESB_NS_10Cipher_DirE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c77c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c77a8.md#insn-004c77c4) · [`004c77d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c77a8.md#insn-004c77d8) · [`004c77f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c77a8.md#insn-004c77f8)
- 新版 [`004c7804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7804) · [`004c7818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7818) · [`004c7838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c77e8.md#insn-004c7838)

~~~diff
- 004c77c4 ["INT_ADD", "register:40f0:8", ["const:4c77c4:8", "const:4:8"]]
- 004c77c4 ["CALL", null, ["callee:00c59040:8"]]
+ 004c7804 ["INT_ADD", "register:40f0:8", ["const:4c7804:8", "const:4:8"]]
+ 004c7804 ["CALL", null, ["callee:00c59040:8"]]
- 004c77c4 bytes eb451e94
+ 004c7804 bytes 0f461e94
- 004c77d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c77d8 ["INT_ADD", "register:40f0:8", ["const:4c77d8:8", "const:4:8"]]
- 004c77d8 ["CALLIND", null, ["register:0:8"]]
+ 004c7818 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7818 ["INT_ADD", "register:40f0:8", ["const:4c7818:8", "const:4:8"]]
+ 004c7818 ["CALLIND", null, ["register:0:8"]]
- 004c77d8 bytes 00013fd6
+ 004c7818 bytes 00013fd6
- 004c77f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c77f8 ["INT_ADD", "register:40f0:8", ["const:4c77f8:8", "const:4:8"]]
- 004c77f8 ["CALLIND", null, ["register:0:8"]]
+ 004c7838 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7838 ["INT_ADD", "register:40f0:8", ["const:4c7838:8", "const:4:8"]]
+ 004c7838 ["CALLIND", null, ["register:0:8"]]
- 004c77f8 bytes 00013fd6
+ 004c7838 bytes 00013fd6
~~~


<a id="compare-88015deaa0a9c5e34cbf2b6cf32598f0"></a>

### [`004c7810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7810.md) → [`004c7850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringENS_10Cipher_DirE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7810.md#insn-004c7824) · [`004c7838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7810.md#insn-004c7838)
- 新版 [`004c7864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md#insn-004c7864) · [`004c7878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7850.md#insn-004c7878)

~~~diff
- 004c7824 ["INT_ADD", "register:40f0:8", ["const:4c7824:8", "const:4:8"]]
- 004c7824 ["CALL", null, ["callee:00c59040:8"]]
+ 004c7864 ["INT_ADD", "register:40f0:8", ["const:4c7864:8", "const:4:8"]]
+ 004c7864 ["CALL", null, ["callee:00c59040:8"]]
- 004c7824 bytes d3451e94
+ 004c7864 bytes f7451e94
- 004c7838 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c7838 ["INT_ADD", "register:40f0:8", ["const:4c7838:8", "const:4:8"]]
- 004c7838 ["CALLIND", null, ["register:0:8"]]
+ 004c7878 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7878 ["INT_ADD", "register:40f0:8", ["const:4c7878:8", "const:4:8"]]
+ 004c7878 ["CALLIND", null, ["register:0:8"]]
- 004c7838 bytes 00013fd6
+ 004c7878 bytes 00013fd6
~~~


<a id="compare-d08839a40c272200aef3078f4100de51"></a>

### [`004c7970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7970.md) → [`004c79b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md) _ZNK5Botan11SecureQueue4peekEPhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59000.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590d0.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7970.md#insn-004c7a08) · [`004c7a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7970.md#insn-004c7a60)
- 新版 [`004c7a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md#insn-004c7a48) · [`004c7aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c79b0.md#insn-004c7aa0)

~~~diff
- 004c7a08 ["INT_ADD", "register:40f0:8", ["const:4c7a08:8", "const:4:8"]]
- 004c7a08 ["CALL", null, ["callee:00c58010:8"]]
+ 004c7a48 ["INT_ADD", "register:40f0:8", ["const:4c7a48:8", "const:4:8"]]
+ 004c7a48 ["CALL", null, ["callee:00c58010:8"]]
- 004c7a08 bytes 4e411e94
+ 004c7a48 bytes 72411e94
- 004c7a60 ["INT_ADD", "register:40f0:8", ["const:4c7a60:8", "const:4:8"]]
- 004c7a60 ["CALL", null, ["callee:00c58010:8"]]
+ 004c7aa0 ["INT_ADD", "register:40f0:8", ["const:4c7aa0:8", "const:4:8"]]
+ 004c7aa0 ["CALL", null, ["callee:00c58010:8"]]
- 004c7a60 bytes 38411e94
+ 004c7aa0 bytes 5c411e94
~~~


<a id="compare-8fe028879cafc91b2bbc6741a85f522e"></a>

### [`004c7c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c24.md) → [`004c7c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md) FUN_004c7c64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c24.md#insn-004c7c40)
- 新版 [`004c7c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md#insn-004c7c80)

~~~diff
- 004c7c40 ["INT_ADD", "register:40f0:8", ["const:4c7c40:8", "const:4:8"]]
- 004c7c40 ["CALL", null, ["callee:0053080c:8"]]
+ 004c7c80 ["INT_ADD", "register:40f0:8", ["const:4c7c80:8", "const:4:8"]]
+ 004c7c80 ["CALL", null, ["callee:0053080c:8"]]
- 004c7c40 bytes e3a20194
+ 004c7c80 bytes e3a20194
~~~


<a id="compare-aeb1f596f997af50e84d0160044d4190"></a>

### [`004c7c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md) → [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) FUN_004c7ca0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004c8818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md) · 呼出先 2件 [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004c8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md) · 呼出先 2件 [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c7c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md#insn-004c7c8c) · [`004c7c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md#insn-004c7c94) · [`004c7d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md#insn-004c7d48)
- 新版 [`004c7ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7ccc) · [`004c7cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7cd4) · [`004c7d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md#insn-004c7d88)

~~~diff
- 004c7c8c ["INT_ADD", "register:40f0:8", ["const:4c7c8c:8", "const:4:8"]]
- 004c7c8c ["CALL", null, ["callee:0053080c:8"]]
+ 004c7ccc ["INT_ADD", "register:40f0:8", ["const:4c7ccc:8", "const:4:8"]]
+ 004c7ccc ["CALL", null, ["callee:0053080c:8"]]
- 004c7c8c bytes d0a20194
+ 004c7ccc bytes d0a20194
- 004c7c94 ["INT_ADD", "register:40f0:8", ["const:4c7c94:8", "const:4:8"]]
- 004c7c94 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c7cd4 ["INT_ADD", "register:40f0:8", ["const:4c7cd4:8", "const:4:8"]]
+ 004c7cd4 ["CALL", null, ["callee:00c57f80:8"]]
- 004c7c94 bytes 87401e94
+ 004c7cd4 bytes ab401e94
- 004c7d48 ["INT_ADD", "register:40f0:8", ["const:4c7d48:8", "const:4:8"]]
- 004c7d48 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c7d88 ["INT_ADD", "register:40f0:8", ["const:4c7d88:8", "const:4:8"]]
+ 004c7d88 ["CALL", null, ["callee:00c57f80:8"]]
- 004c7d48 bytes 5a401e94
+ 004c7d88 bytes 7e401e94
~~~


<a id="compare-e061eb9a899015ecc1b533b27b0fe321"></a>

### [`004c8110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8110.md) → [`004c8150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8150.md) FUN_004c8150

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0054482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/0054482c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054486c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/0054486c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c812c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8110.md#insn-004c812c)
- 新版 [`004c816c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8150.md#insn-004c816c)

~~~diff
- 004c812c ["INT_ADD", "register:40f0:8", ["const:4c812c:8", "const:4:8"]]
- 004c812c ["CALL", null, ["callee:0054486c:8"]]
+ 004c816c ["INT_ADD", "register:40f0:8", ["const:4c816c:8", "const:4:8"]]
+ 004c816c ["CALL", null, ["callee:0054486c:8"]]
- 004c812c bytes c0f10194
+ 004c816c bytes c0f10194
~~~


<a id="compare-0b6c9b31f3574158a427f88bb2e11faa"></a>

### [`004c814c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c814c.md) → [`004c818c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md) _ZN5Botan4PipeD2Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59030.md) · 呼出先 3件 [`0054482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/0054482c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md)
- 新版 呼出元 1件 [`00c59100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59100.md) · 呼出先 3件 [`0054486c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/0054486c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c814c.md#insn-004c8160) · [`004c8174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c814c.md#insn-004c8174)
- 新版 [`004c81a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md#insn-004c81a0) · [`004c81b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c818c.md#insn-004c81b4)

~~~diff
- 004c8160 ["INT_ADD", "register:40f0:8", ["const:4c8160:8", "const:4:8"]]
- 004c8160 ["CALL", null, ["callee:00c590f0:8"]]
+ 004c81a0 ["INT_ADD", "register:40f0:8", ["const:4c81a0:8", "const:4:8"]]
+ 004c81a0 ["CALL", null, ["callee:00c590f0:8"]]
- 004c8160 bytes b0431e94
+ 004c81a0 bytes d4431e94
- 004c8174 ["INT_ADD", "register:40f0:8", ["const:4c8174:8", "const:4:8"]]
- 004c8174 ["CALL", null, ["callee:0054486c:8"]]
+ 004c81b4 ["INT_ADD", "register:40f0:8", ["const:4c81b4:8", "const:4:8"]]
+ 004c81b4 ["CALL", null, ["callee:0054486c:8"]]
- 004c8174 bytes aef10194
+ 004c81b4 bytes aef10194
~~~


<a id="compare-abc6fd16bedeb0ccb1edfd97620d6fd8"></a>

### [`004c8228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8228.md) → [`004c8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8268.md) _ZN5Botan4PipeD0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c59100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59100.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8228.md#insn-004c8238)
- 新版 [`004c8278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8268.md#insn-004c8278)

~~~diff
- 004c8238 ["INT_ADD", "register:40f0:8", ["const:4c8238:8", "const:4:8"]]
- 004c8238 ["CALL", null, ["callee:00c59100:8"]]
+ 004c8278 ["INT_ADD", "register:40f0:8", ["const:4c8278:8", "const:4:8"]]
+ 004c8278 ["CALL", null, ["callee:00c59100:8"]]
- 004c8238 bytes 7e431e94
+ 004c8278 bytes a2431e94
~~~


<a id="compare-4050306aa81f40aaad04a4f73e2b743f"></a>

### [`004c824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c824c.md) → [`004c828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c828c.md) _ZN5Botan4Pipe5resetEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c824c.md#insn-004c8260)
- 新版 [`004c82a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c828c.md#insn-004c82a0)

~~~diff
- 004c8260 ["INT_ADD", "register:40f0:8", ["const:4c8260:8", "const:4:8"]]
- 004c8260 ["CALL", null, ["callee:00c590f0:8"]]
+ 004c82a0 ["INT_ADD", "register:40f0:8", ["const:4c82a0:8", "const:4:8"]]
+ 004c82a0 ["CALL", null, ["callee:00c590f0:8"]]
- 004c8260 bytes 70431e94
+ 004c82a0 bytes 94431e94
~~~


<a id="compare-e0bc84851be426c34471cd420a64d266"></a>

### [`004c8278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8278.md) → [`004c82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82b8.md) _ZNK5Botan4Pipe11end_of_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8278.md#insn-004c8284)
- 新版 [`004c82c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82b8.md#insn-004c82c4)

~~~diff
- 004c8284 ["INT_ADD", "register:40f0:8", ["const:4c8284:8", "const:4:8"]]
- 004c8284 ["CALL", null, ["callee:00c59110:8"]]
+ 004c82c4 ["INT_ADD", "register:40f0:8", ["const:4c82c4:8", "const:4:8"]]
+ 004c82c4 ["CALL", null, ["callee:00c59110:8"]]
- 004c8284 bytes 6f431e94
+ 004c82c4 bytes 93431e94
~~~


<a id="compare-c21587709342951224e1ca39937622ea"></a>

### [`004c852c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c852c.md) → [`004c856c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md) _ZN5Botan4Pipe11process_msgEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c852c.md#insn-004c8548) · [`004c8558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c852c.md#insn-004c8558)
- 新版 [`004c8588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md#insn-004c8588) · [`004c8598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c856c.md#insn-004c8598)

~~~diff
- 004c8548 ["INT_ADD", "register:40f0:8", ["const:4c8548:8", "const:4:8"]]
- 004c8548 ["CALL", null, ["callee:00c59120:8"]]
+ 004c8588 ["INT_ADD", "register:40f0:8", ["const:4c8588:8", "const:4:8"]]
+ 004c8588 ["CALL", null, ["callee:00c59120:8"]]
- 004c8548 bytes c2421e94
+ 004c8588 bytes e6421e94
- 004c8558 ["INT_ADD", "register:40f0:8", ["const:4c8558:8", "const:4:8"]]
- 004c8558 ["CALL", null, ["callee:00c59130:8"]]
+ 004c8598 ["INT_ADD", "register:40f0:8", ["const:4c8598:8", "const:4:8"]]
+ 004c8598 ["CALL", null, ["callee:00c59130:8"]]
- 004c8558 bytes c2421e94
+ 004c8598 bytes e6421e94
~~~


<a id="compare-0a50598c9b6d99a51058169c9749f0cb"></a>

### [`004c89a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89a4.md) → [`004c89e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c89c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89a4.md#insn-004c89c0) · [`004c89d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89a4.md#insn-004c89d0)
- 新版 [`004c8a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md#insn-004c8a00) · [`004c8a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c89e4.md#insn-004c8a10)

~~~diff
- 004c89c0 ["INT_ADD", "register:40f0:8", ["const:4c89c0:8", "const:4:8"]]
- 004c89c0 ["CALL", null, ["callee:00c59120:8"]]
+ 004c8a00 ["INT_ADD", "register:40f0:8", ["const:4c8a00:8", "const:4:8"]]
+ 004c8a00 ["CALL", null, ["callee:00c59120:8"]]
- 004c89c0 bytes a4411e94
+ 004c8a00 bytes c8411e94
- 004c89d0 ["INT_ADD", "register:40f0:8", ["const:4c89d0:8", "const:4:8"]]
- 004c89d0 ["CALL", null, ["callee:00c59130:8"]]
+ 004c8a10 ["INT_ADD", "register:40f0:8", ["const:4c8a10:8", "const:4:8"]]
+ 004c8a10 ["CALL", null, ["callee:00c59130:8"]]
- 004c89d0 bytes a4411e94
+ 004c8a10 bytes c8411e94
~~~


<a id="compare-bda8157e5ec3a00af81a9569eae394ae"></a>

### [`004c89e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89e8.md) → [`004c8a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89e8.md#insn-004c8a04) · [`004c8a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c89e8.md#insn-004c8a14)
- 新版 [`004c8a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md#insn-004c8a44) · [`004c8a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a28.md#insn-004c8a54)

~~~diff
- 004c8a04 ["INT_ADD", "register:40f0:8", ["const:4c8a04:8", "const:4:8"]]
- 004c8a04 ["CALL", null, ["callee:00c59120:8"]]
+ 004c8a44 ["INT_ADD", "register:40f0:8", ["const:4c8a44:8", "const:4:8"]]
+ 004c8a44 ["CALL", null, ["callee:00c59120:8"]]
- 004c8a04 bytes 93411e94
+ 004c8a44 bytes b7411e94
- 004c8a14 ["INT_ADD", "register:40f0:8", ["const:4c8a14:8", "const:4:8"]]
- 004c8a14 ["CALL", null, ["callee:00c59130:8"]]
+ 004c8a54 ["INT_ADD", "register:40f0:8", ["const:4c8a54:8", "const:4:8"]]
+ 004c8a54 ["CALL", null, ["callee:00c59130:8"]]
- 004c8a14 bytes 93411e94
+ 004c8a54 bytes b7411e94
~~~


<a id="compare-795ca32048589026afbc6d4dc2e668e6"></a>

### [`004c8a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a2c.md) → [`004c8a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a2c.md#insn-004c8a58) · [`004c8a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a2c.md#insn-004c8a68)
- 新版 [`004c8a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md#insn-004c8a98) · [`004c8aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8a6c.md#insn-004c8aa8)

~~~diff
- 004c8a58 ["INT_ADD", "register:40f0:8", ["const:4c8a58:8", "const:4:8"]]
- 004c8a58 ["CALL", null, ["callee:00c59120:8"]]
+ 004c8a98 ["INT_ADD", "register:40f0:8", ["const:4c8a98:8", "const:4:8"]]
+ 004c8a98 ["CALL", null, ["callee:00c59120:8"]]
- 004c8a58 bytes 7e411e94
+ 004c8a98 bytes a2411e94
- 004c8a68 ["INT_ADD", "register:40f0:8", ["const:4c8a68:8", "const:4:8"]]
- 004c8a68 ["CALL", null, ["callee:00c59130:8"]]
+ 004c8aa8 ["INT_ADD", "register:40f0:8", ["const:4c8aa8:8", "const:4:8"]]
+ 004c8aa8 ["CALL", null, ["callee:00c59130:8"]]
- 004c8a68 bytes 7e411e94
+ 004c8aa8 bytes a2411e94
~~~


<a id="compare-d43d070bf18369f5769c9d6d70abd9a8"></a>

### [`004c8a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a80.md) → [`004c8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md) _ZN5Botan4Pipe11process_msgERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md) [`00c590a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md) [`00c59170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c8a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a80.md#insn-004c8a94) · [`004c8aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8a80.md#insn-004c8aa0)
- 新版 [`004c8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md#insn-004c8ad4) · [`004c8ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8ac0.md#insn-004c8ae0)

~~~diff
- 004c8a94 ["INT_ADD", "register:40f0:8", ["const:4c8a94:8", "const:4:8"]]
- 004c8a94 ["CALL", null, ["callee:00c59120:8"]]
+ 004c8ad4 ["INT_ADD", "register:40f0:8", ["const:4c8ad4:8", "const:4:8"]]
+ 004c8ad4 ["CALL", null, ["callee:00c59120:8"]]
- 004c8a94 bytes 6f411e94
+ 004c8ad4 bytes 93411e94
- 004c8aa0 ["INT_ADD", "register:40f0:8", ["const:4c8aa0:8", "const:4:8"]]
- 004c8aa0 ["CALL", null, ["callee:00c59170:8"]]
+ 004c8ae0 ["INT_ADD", "register:40f0:8", ["const:4c8ae0:8", "const:4:8"]]
+ 004c8ae0 ["CALL", null, ["callee:00c59170:8"]]
- 004c8aa0 bytes 80411e94
+ 004c8ae0 bytes a4411e94
~~~


<a id="compare-f27ec306d479eca9d74fed57533b13b4"></a>

### [`004c9930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9930.md) → [`004c9970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md) _ZN5Botan4Pipe5writeEh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9930.md#insn-004c9958) · [`004c997c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9930.md#insn-004c997c)
- 新版 [`004c9998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md#insn-004c9998) · [`004c99bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9970.md#insn-004c99bc)

~~~diff
- 004c9958 ["INT_ADD", "register:40f0:8", ["const:4c9958:8", "const:4:8"]]
- 004c9958 ["CALL", null, ["callee:00c59130:8"]]
+ 004c9998 ["INT_ADD", "register:40f0:8", ["const:4c9998:8", "const:4:8"]]
+ 004c9998 ["CALL", null, ["callee:00c59130:8"]]
- 004c9958 bytes c23d1e94
+ 004c9998 bytes e63d1e94
- 004c997c ["INT_ADD", "register:40f0:8", ["const:4c997c:8", "const:4:8"]]
- 004c997c ["CALL", null, ["callee:00c57fb0:8"]]
+ 004c99bc ["INT_ADD", "register:40f0:8", ["const:4c99bc:8", "const:4:8"]]
+ 004c99bc ["CALL", null, ["callee:00c57fb0:8"]]
- 004c997c bytes 59391e94
+ 004c99bc bytes 7d391e94
~~~


<a id="compare-b9f2b5bdd2b2ede599dd389dc1ac115c"></a>

### [`004c9adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9adc.md) → [`004c9b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md) _ZN5Botan4Pipe8read_allEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md) [`00c590c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md) [`00c59190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9adc.md#insn-004c9b04) · [`004c9b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9adc.md#insn-004c9b10) · [`004c9b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9adc.md#insn-004c9b24)
- 新版 [`004c9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b44) · [`004c9b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b50) · [`004c9b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9b1c.md#insn-004c9b64)

~~~diff
- 004c9b04 ["INT_ADD", "register:40f0:8", ["const:4c9b04:8", "const:4:8"]]
- 004c9b04 ["CALL", null, ["callee:00c59110:8"]]
+ 004c9b44 ["INT_ADD", "register:40f0:8", ["const:4c9b44:8", "const:4:8"]]
+ 004c9b44 ["CALL", null, ["callee:00c59110:8"]]
- 004c9b04 bytes 4f3d1e94
+ 004c9b44 bytes 733d1e94
- 004c9b10 ["INT_ADD", "register:40f0:8", ["const:4c9b10:8", "const:4:8"]]
- 004c9b10 ["CALL", null, ["callee:004b3548:8"]]
+ 004c9b50 ["INT_ADD", "register:40f0:8", ["const:4c9b50:8", "const:4:8"]]
+ 004c9b50 ["CALL", null, ["callee:004b3548:8"]]
- 004c9b10 bytes 7ea6ff97
+ 004c9b50 bytes 7ea6ff97
- 004c9b24 ["INT_ADD", "register:40f0:8", ["const:4c9b24:8", "const:4:8"]]
- 004c9b24 ["CALL", null, ["callee:00c59190:8"]]
+ 004c9b64 ["INT_ADD", "register:40f0:8", ["const:4c9b64:8", "const:4:8"]]
+ 004c9b64 ["CALL", null, ["callee:00c59190:8"]]
- 004c9b24 bytes 673d1e94
+ 004c9b64 bytes 8b3d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5051f9b0e04c95b57490f0f9912ffefe"></a>

### [`004c9f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9f88.md) → [`004c9fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9fc8.md) _ZN5Botan4Pipe15check_availableEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9f88.md#insn-004c9fa0)
- 新版 [`004c9fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9fc8.md#insn-004c9fe0)

~~~diff
- 004c9fa0 ["INT_ADD", "register:40f0:8", ["const:4c9fa0:8", "const:4:8"]]
- 004c9fa0 ["CALL", null, ["callee:00c59110:8"]]
+ 004c9fe0 ["INT_ADD", "register:40f0:8", ["const:4c9fe0:8", "const:4:8"]]
+ 004c9fe0 ["CALL", null, ["callee:00c59110:8"]]
- 004c9fa0 bytes 283c1e94
+ 004c9fe0 bytes 4c3c1e94
~~~


<a id="compare-98c7baafbdd0dd211a7d74232419a627"></a>

### [`004c9fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9fb8.md) → [`004c9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9ff8.md) _ZN5Botan4Pipe19check_available_msgEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004c9fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9fb8.md#insn-004c9fcc)
- 新版 [`004ca00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9ff8.md#insn-004ca00c)

~~~diff
- 004c9fcc ["INT_ADD", "register:40f0:8", ["const:4c9fcc:8", "const:4:8"]]
- 004c9fcc ["CALL", null, ["callee:00c59110:8"]]
+ 004ca00c ["INT_ADD", "register:40f0:8", ["const:4ca00c:8", "const:4:8"]]
+ 004ca00c ["CALL", null, ["callee:00c59110:8"]]
- 004c9fcc bytes 1d3c1e94
+ 004ca00c bytes 413c1e94
~~~


<a id="compare-1b102d032b1cba86da6411da6373a185"></a>

### [`004cab94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cab94.md) → [`004cabd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md) FUN_004cabd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cabb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cab94.md#insn-004cabb0) · [`004cabb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cab94.md#insn-004cabb8) · [`004cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cab94.md#insn-004cabc0)
- 新版 [`004cabf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cabf0) · [`004cabf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cabf8) · [`004cac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cabd4.md#insn-004cac00)

~~~diff
- 004cabb0 ["INT_ADD", "register:40f0:8", ["const:4cabb0:8", "const:4:8"]]
- 004cabb0 ["CALL", null, ["callee:00c581a0:8"]]
+ 004cabf0 ["INT_ADD", "register:40f0:8", ["const:4cabf0:8", "const:4:8"]]
+ 004cabf0 ["CALL", null, ["callee:00c581a0:8"]]
- 004cabb0 bytes 48351e94
+ 004cabf0 bytes 6c351e94
- 004cabb8 ["INT_ADD", "register:40f0:8", ["const:4cabb8:8", "const:4:8"]]
- 004cabb8 ["CALL", null, ["callee:00c57f30:8"]]
+ 004cabf8 ["INT_ADD", "register:40f0:8", ["const:4cabf8:8", "const:4:8"]]
+ 004cabf8 ["CALL", null, ["callee:00c57f30:8"]]
- 004cabb8 bytes aa341e94
+ 004cabf8 bytes ce341e94
- 004cabc0 ["INT_ADD", "register:40f0:8", ["const:4cabc0:8", "const:4:8"]]
- 004cabc0 ["CALL", null, ["callee:00c581a0:8"]]
+ 004cac00 ["INT_ADD", "register:40f0:8", ["const:4cac00:8", "const:4:8"]]
+ 004cac00 ["CALL", null, ["callee:00c581a0:8"]]
- 004cabc0 bytes 44351e94
+ 004cac00 bytes 68351e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde98e2e29fafb6125c2e60c40602f0d"></a>

### [`004cabe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cabe8.md) → [`004cac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md) FUN_004cac28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cac34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cabe8.md#insn-004cac34) · [`004cac48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cabe8.md#insn-004cac48) · [`004cac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cabe8.md#insn-004cac50)
- 新版 [`004cac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac74) · [`004cac88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac88) · [`004cac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cac28.md#insn-004cac90)

~~~diff
- 004cac34 ["INT_ADD", "register:40f0:8", ["const:4cac34:8", "const:4:8"]]
- 004cac34 ["CALL", null, ["callee:00c53da0:8"]]
+ 004cac74 ["INT_ADD", "register:40f0:8", ["const:4cac74:8", "const:4:8"]]
+ 004cac74 ["CALL", null, ["callee:00c53da0:8"]]
- 004cac34 bytes 33241e94
+ 004cac74 bytes 4b241e94
- 004cac48 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cac48 ["INT_ADD", "register:40f0:8", ["const:4cac48:8", "const:4:8"]]
- 004cac48 ["CALLIND", null, ["register:0:8"]]
+ 004cac88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cac88 ["INT_ADD", "register:40f0:8", ["const:4cac88:8", "const:4:8"]]
+ 004cac88 ["CALLIND", null, ["register:0:8"]]
- 004cac48 bytes 00013fd6
+ 004cac88 bytes 00013fd6
- 004cac50 ["INT_ADD", "register:40f0:8", ["const:4cac50:8", "const:4:8"]]
- 004cac50 ["CALL", null, ["callee:00c57f50:8"]]
+ 004cac90 ["INT_ADD", "register:40f0:8", ["const:4cac90:8", "const:4:8"]]
+ 004cac90 ["CALL", null, ["callee:00c57f50:8"]]
- 004cac50 bytes 8c341e94
+ 004cac90 bytes b0341e94
~~~


<a id="compare-7c2ca839f43d154e5f804a7868acb9db"></a>

### [`004caf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004caf54.md) → [`004caf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004caf94.md) _ZN5Botan13Threaded_ForkD0Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c59120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c591f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c591f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004caf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004caf54.md#insn-004caf64)
- 新版 [`004cafa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004caf94.md#insn-004cafa4)

~~~diff
- 004caf64 ["INT_ADD", "register:40f0:8", ["const:4caf64:8", "const:4:8"]]
- 004caf64 ["CALL", null, ["callee:00c591f0:8"]]
+ 004cafa4 ["INT_ADD", "register:40f0:8", ["const:4cafa4:8", "const:4:8"]]
+ 004cafa4 ["CALL", null, ["callee:00c591f0:8"]]
- 004caf64 bytes 6f381e94
+ 004cafa4 bytes 93381e94
~~~


<a id="compare-1907f23a0b923d9a76dabb3bd7ade9d3"></a>

### [`004cafa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cafa0.md) → [`004cafe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md) FUN_004cafe0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 5件 [`005449b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005449b0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004ca9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004ca9b0.md) · 呼出先 5件 [`005449f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cafe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cafa0.md#insn-004cafe4) · [`004cb038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cafa0.md#insn-004cb038) · [`004cb04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cafa0.md#insn-004cb04c)
- 新版 [`004cb024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb024) · [`004cb078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb078) · [`004cb08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md#insn-004cb08c)

~~~diff
- 004cafe4 ["INT_ADD", "register:40f0:8", ["const:4cafe4:8", "const:4:8"]]
- 004cafe4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004cb024 ["INT_ADD", "register:40f0:8", ["const:4cb024:8", "const:4:8"]]
+ 004cb024 ["CALL", null, ["callee:00c57f60:8"]]
- 004cafe4 bytes ab331e94
+ 004cb024 bytes cf331e94
- 004cb038 ["INT_ADD", "register:40f0:8", ["const:4cb038:8", "const:4:8"]]
- 004cb038 ["CALL", null, ["callee:00c53da0:8"]]
+ 004cb078 ["INT_ADD", "register:40f0:8", ["const:4cb078:8", "const:4:8"]]
+ 004cb078 ["CALL", null, ["callee:00c53da0:8"]]
- 004cb038 bytes 32231e94
+ 004cb078 bytes 4a231e94
- 004cb04c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb04c ["INT_ADD", "register:40f0:8", ["const:4cb04c:8", "const:4:8"]]
- 004cb04c ["CALLIND", null, ["register:0:8"]]
+ 004cb08c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb08c ["INT_ADD", "register:40f0:8", ["const:4cb08c:8", "const:4:8"]]
+ 004cb08c ["CALLIND", null, ["register:0:8"]]
- 004cb04c bytes 00013fd6
+ 004cb08c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32922c709e0d291ab02817c94a4eb1f6"></a>

### [`004cb0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb0a8.md) → [`004cb0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md) _ZN5Botan13Threaded_Fork12thread_entryEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`004ca9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004ca9b0.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md) [`00c58550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb0a8.md#insn-004cb0f0) · [`004cb0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb0a8.md#insn-004cb0f8) · [`004cb10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb0a8.md#insn-004cb10c)
- 新版 [`004cb130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb130) · [`004cb138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb138) · [`004cb14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb0e8.md#insn-004cb14c)

~~~diff
- 004cb0f0 ["INT_ADD", "register:40f0:8", ["const:4cb0f0:8", "const:4:8"]]
- 004cb0f0 ["CALL", null, ["callee:00c58450:8"]]
+ 004cb130 ["INT_ADD", "register:40f0:8", ["const:4cb130:8", "const:4:8"]]
+ 004cb130 ["CALL", null, ["callee:00c58450:8"]]
- 004cb0f0 bytes a4341e94
+ 004cb130 bytes c8341e94
- 004cb0f8 ["INT_ADD", "register:40f0:8", ["const:4cb0f8:8", "const:4:8"]]
- 004cb0f8 ["CALL", null, ["callee:00c581c0:8"]]
+ 004cb138 ["INT_ADD", "register:40f0:8", ["const:4cb138:8", "const:4:8"]]
+ 004cb138 ["CALL", null, ["callee:00c581c0:8"]]
- 004cb0f8 bytes fe331e94
+ 004cb138 bytes 22341e94
- 004cb10c ["INT_ADD", "register:40f0:8", ["const:4cb10c:8", "const:4:8"]]
- 004cb10c ["CALL", null, ["callee:00c581b0:8"]]
+ 004cb14c ["INT_ADD", "register:40f0:8", ["const:4cb14c:8", "const:4:8"]]
+ 004cb14c ["CALL", null, ["callee:00c581b0:8"]]
- 004cb10c bytes f5331e94
+ 004cb14c bytes 19341e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b52990da98ad60bc41ca774436d796cd"></a>

### [`004cb300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb300.md) → [`004cb340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md) FUN_004cb340

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004cb31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb300.md#insn-004cb31c) · [`004cb33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb300.md#insn-004cb33c)
- 新版 [`004cb35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md#insn-004cb35c) · [`004cb37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cb340.md#insn-004cb37c)

~~~diff
- 004cb31c ["INT_ADD", "register:40f0:8", ["const:4cb31c:8", "const:4:8"]]
- 004cb31c ["CALL", null, ["callee:00c53da0:8"]]
+ 004cb35c ["INT_ADD", "register:40f0:8", ["const:4cb35c:8", "const:4:8"]]
+ 004cb35c ["CALL", null, ["callee:00c53da0:8"]]
- 004cb31c bytes 79221e94
+ 004cb35c bytes 91221e94
- 004cb33c ["COPY", "register:0:8", ["register:4040:8"]]
- 004cb33c ["INT_ADD", "register:40f0:8", ["const:4cb33c:8", "const:4:8"]]
- 004cb33c ["CALLIND", null, ["register:0:8"]]
+ 004cb37c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb37c ["INT_ADD", "register:40f0:8", ["const:4cb37c:8", "const:4:8"]]
+ 004cb37c ["CALLIND", null, ["register:0:8"]]
- 004cb33c bytes 00013fd6
+ 004cb37c bytes 00013fd6
~~~


