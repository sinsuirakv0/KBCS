# v16.0.1 → v16.0.2 · 要調査の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-f7046df56338fe205f67a7ba172ef22b"></a>

### [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) → [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md) FUN_00480218

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 19件 [`0066b96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b96c.md) [`006a48fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a48fc.md) [`006dc748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc748.md) [`007387ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007387ac.md) [`00744f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744f8c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 19件 [`0066b9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b9ac.md) [`006a4954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4954.md) [`006dc7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc7a0.md) [`00738804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738804.md) [`00744fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fe4.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md#insn-00480204) · [`00480234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md#insn-00480234)
- 新版 `00480244`（命令位置の公開資料なし） · `00480274`（命令位置の公開資料なし）

~~~diff
- 00480204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480204 ["INT_ADD", "register:40f0:8", ["const:480204:8", "const:4:8"]]
- 00480204 ["CALLIND", null, ["register:0:8"]]
+ 00480244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480244 ["INT_ADD", "register:40f0:8", ["const:480244:8", "const:4:8"]]
+ 00480244 ["CALLIND", null, ["register:0:8"]]
- 00480204 bytes 00013fd6
+ 00480244 bytes 00013fd6
- 00480234 ["INT_ADD", "register:40f0:8", ["const:480234:8", "const:4:8"]]
- 00480234 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480274 ["INT_ADD", "register:40f0:8", ["const:480274:8", "const:4:8"]]
+ 00480274 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480234 bytes 2b5f1f94
+ 00480274 bytes 4f5f1f94
~~~


<a id="compare-cc0920e8fe8826c737273c5986cb9467"></a>

### [`00480238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md) → [`00480278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480278.md) FUN_00480278

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md#insn-00480264) · [`00480294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480238.md#insn-00480294)
- 新版 `004802a4`（命令位置の公開資料なし） · `004802d4`（命令位置の公開資料なし）

~~~diff
- 00480264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480264 ["INT_ADD", "register:40f0:8", ["const:480264:8", "const:4:8"]]
- 00480264 ["CALLIND", null, ["register:0:8"]]
+ 004802a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004802a4 ["INT_ADD", "register:40f0:8", ["const:4802a4:8", "const:4:8"]]
+ 004802a4 ["CALLIND", null, ["register:0:8"]]
- 00480264 bytes 00013fd6
+ 004802a4 bytes 00013fd6
- 00480294 ["INT_ADD", "register:40f0:8", ["const:480294:8", "const:4:8"]]
- 00480294 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004802d4 ["INT_ADD", "register:40f0:8", ["const:4802d4:8", "const:4:8"]]
+ 004802d4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480294 bytes 135f1f94
+ 004802d4 bytes 375f1f94
~~~


<a id="compare-1d872f52017c0d74ca9941250935187a"></a>

### [`00480298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md) → [`004802d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004802d8.md) FUN_004802d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004802c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md#insn-004802c4) · [`004802f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480298.md#insn-004802f4)
- 新版 `00480304`（命令位置の公開資料なし） · `00480334`（命令位置の公開資料なし）

~~~diff
- 004802c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004802c4 ["INT_ADD", "register:40f0:8", ["const:4802c4:8", "const:4:8"]]
- 004802c4 ["CALLIND", null, ["register:0:8"]]
+ 00480304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480304 ["INT_ADD", "register:40f0:8", ["const:480304:8", "const:4:8"]]
+ 00480304 ["CALLIND", null, ["register:0:8"]]
- 004802c4 bytes 00013fd6
+ 00480304 bytes 00013fd6
- 004802f4 ["INT_ADD", "register:40f0:8", ["const:4802f4:8", "const:4:8"]]
- 004802f4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480334 ["INT_ADD", "register:40f0:8", ["const:480334:8", "const:4:8"]]
+ 00480334 ["CALL", null, ["callee:00c57fb0:8"]]
- 004802f4 bytes fb5e1f94
+ 00480334 bytes 1f5f1f94
~~~


<a id="compare-5e7e01353f47f24a5ade6816c0e99c4d"></a>

### [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) → [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) FUN_00480338

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 32件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`0066b364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b364.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 32件 [`005b9a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a90.md) [`0066b3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b3a4.md) [`006db0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md) [`0072ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072ed80.md) [`0073299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/0073299c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md#insn-00480324) · [`00480358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md#insn-00480358)
- 新版 `00480364`（命令位置の公開資料なし） · `00480398`（命令位置の公開資料なし）

~~~diff
- 00480324 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480324 ["INT_ADD", "register:40f0:8", ["const:480324:8", "const:4:8"]]
- 00480324 ["CALLIND", null, ["register:0:8"]]
+ 00480364 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480364 ["INT_ADD", "register:40f0:8", ["const:480364:8", "const:4:8"]]
+ 00480364 ["CALLIND", null, ["register:0:8"]]
- 00480324 bytes 00013fd6
+ 00480364 bytes 00013fd6
- 00480358 ["INT_ADD", "register:40f0:8", ["const:480358:8", "const:4:8"]]
- 00480358 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480398 ["INT_ADD", "register:40f0:8", ["const:480398:8", "const:4:8"]]
+ 00480398 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480358 bytes e25e1f94
+ 00480398 bytes 065f1f94
~~~


<a id="compare-28ca41888daf638f2524193134b41f9f"></a>

### [`0048035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md) → [`0048039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/0048039c.md) FUN_0048039c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f51c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f55c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-00480390) · [`004803a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-004803a4) · [`004803c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md#insn-004803c4)
- 新版 `004803d0`（命令位置の公開資料なし） · `004803e4`（命令位置の公開資料なし） · `00480404`（命令位置の公開資料なし）

~~~diff
- 00480390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480390 ["INT_ADD", "register:40f0:8", ["const:480390:8", "const:4:8"]]
- 00480390 ["CALLIND", null, ["register:0:8"]]
+ 004803d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004803d0 ["INT_ADD", "register:40f0:8", ["const:4803d0:8", "const:4:8"]]
+ 004803d0 ["CALLIND", null, ["register:0:8"]]
- 00480390 bytes 00013fd6
+ 004803d0 bytes 00013fd6
- 004803a4 ["INT_ADD", "register:40f0:8", ["const:4803a4:8", "const:4:8"]]
- 004803a4 ["CALL", null, ["callee:0055f504:8"]]
+ 004803e4 ["INT_ADD", "register:40f0:8", ["const:4803e4:8", "const:4:8"]]
+ 004803e4 ["CALL", null, ["callee:0055f504:8"]]
- 004803a4 bytes 487c0394
+ 004803e4 bytes 487c0394
- 004803c4 ["INT_ADD", "register:40f0:8", ["const:4803c4:8", "const:4:8"]]
- 004803c4 ["CALL", null, ["callee:0055f55c:8"]]
+ 00480404 ["INT_ADD", "register:40f0:8", ["const:480404:8", "const:4:8"]]
+ 00480404 ["CALL", null, ["callee:0055f55c:8"]]
- 004803c4 bytes 567c0394
+ 00480404 bytes 567c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b931cd37033709fece080f684640fd3"></a>

### [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) → [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) FUN_00480430

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 36件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`005e0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0074.md) [`005e00b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e00b8.md) [`005e0164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0164.md) [`005e01fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01fc.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 36件 [`005b9a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a90.md) [`005e00b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e00b4.md) [`005e00f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e00f8.md) [`005e01a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e01a4.md) [`005e023c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e023c.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480424) · [`00480438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480438) · [`00480458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md#insn-00480458)
- 新版 `00480464`（命令位置の公開資料なし） · `00480478`（命令位置の公開資料なし） · `00480498`（命令位置の公開資料なし）

~~~diff
- 00480424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480424 ["INT_ADD", "register:40f0:8", ["const:480424:8", "const:4:8"]]
- 00480424 ["CALLIND", null, ["register:0:8"]]
+ 00480464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480464 ["INT_ADD", "register:40f0:8", ["const:480464:8", "const:4:8"]]
+ 00480464 ["CALLIND", null, ["register:0:8"]]
- 00480424 bytes 00013fd6
+ 00480464 bytes 00013fd6
- 00480438 ["INT_ADD", "register:40f0:8", ["const:480438:8", "const:4:8"]]
- 00480438 ["CALL", null, ["callee:0055f504:8"]]
+ 00480478 ["INT_ADD", "register:40f0:8", ["const:480478:8", "const:4:8"]]
+ 00480478 ["CALL", null, ["callee:0055f504:8"]]
- 00480438 bytes 237c0394
+ 00480478 bytes 237c0394
- 00480458 ["INT_ADD", "register:40f0:8", ["const:480458:8", "const:4:8"]]
- 00480458 ["CALL", null, ["callee:0055f578:8"]]
+ 00480498 ["INT_ADD", "register:40f0:8", ["const:480498:8", "const:4:8"]]
+ 00480498 ["CALL", null, ["callee:0055f578:8"]]
- 00480458 bytes 387c0394
+ 00480498 bytes 387c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9825a32c5ea5422f8f03d86031a23179"></a>

### [`00480484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md) → [`004804c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004804c4.md) FUN_004804c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004804b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804b8) · [`004804cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804cc) · [`004804ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md#insn-004804ec)
- 新版 `004804f8`（命令位置の公開資料なし） · `0048050c`（命令位置の公開資料なし） · `0048052c`（命令位置の公開資料なし）

~~~diff
- 004804b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004804b8 ["INT_ADD", "register:40f0:8", ["const:4804b8:8", "const:4:8"]]
- 004804b8 ["CALLIND", null, ["register:0:8"]]
+ 004804f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004804f8 ["INT_ADD", "register:40f0:8", ["const:4804f8:8", "const:4:8"]]
+ 004804f8 ["CALLIND", null, ["register:0:8"]]
- 004804b8 bytes 00013fd6
+ 004804f8 bytes 00013fd6
- 004804cc ["INT_ADD", "register:40f0:8", ["const:4804cc:8", "const:4:8"]]
- 004804cc ["CALL", null, ["callee:0055f504:8"]]
+ 0048050c ["INT_ADD", "register:40f0:8", ["const:48050c:8", "const:4:8"]]
+ 0048050c ["CALL", null, ["callee:0055f504:8"]]
- 004804cc bytes fe7b0394
+ 0048050c bytes fe7b0394
- 004804ec ["INT_ADD", "register:40f0:8", ["const:4804ec:8", "const:4:8"]]
- 004804ec ["CALL", null, ["callee:0055f578:8"]]
+ 0048052c ["INT_ADD", "register:40f0:8", ["const:48052c:8", "const:4:8"]]
+ 0048052c ["CALL", null, ["callee:0055f578:8"]]
- 004804ec bytes 137c0394
+ 0048052c bytes 137c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9fbf8a1ae0a1bcd982b948a3675345d"></a>

### [`00480518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md) → [`00480558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480558.md) FUN_00480558

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008395ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008395ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00839644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839644.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048054c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-0048054c) · [`0048057c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-0048057c) · [`004805b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480518.md#insn-004805b0)
- 新版 `0048058c`（命令位置の公開資料なし） · `004805bc`（命令位置の公開資料なし） · `004805f0`（命令位置の公開資料なし）

~~~diff
- 0048054c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048054c ["INT_ADD", "register:40f0:8", ["const:48054c:8", "const:4:8"]]
- 0048054c ["CALLIND", null, ["register:0:8"]]
+ 0048058c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048058c ["INT_ADD", "register:40f0:8", ["const:48058c:8", "const:4:8"]]
+ 0048058c ["CALLIND", null, ["register:0:8"]]
- 0048054c bytes 00013fd6
+ 0048058c bytes 00013fd6
- 0048057c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048057c ["INT_ADD", "register:40f0:8", ["const:48057c:8", "const:4:8"]]
- 0048057c ["CALLIND", null, ["register:0:8"]]
+ 004805bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004805bc ["INT_ADD", "register:40f0:8", ["const:4805bc:8", "const:4:8"]]
+ 004805bc ["CALLIND", null, ["register:0:8"]]
- 0048057c bytes 00013fd6
+ 004805bc bytes 00013fd6
- 004805b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004805b0 ["INT_ADD", "register:40f0:8", ["const:4805b0:8", "const:4:8"]]
- 004805b0 ["CALLIND", null, ["register:0:8"]]
+ 004805f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004805f0 ["INT_ADD", "register:40f0:8", ["const:4805f0:8", "const:4:8"]]
+ 004805f0 ["CALLIND", null, ["register:0:8"]]
- 004805b0 bytes 00013fd6
+ 004805f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e42cdb80d87000ef8880630040ee3e2e"></a>

### [`00480628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md) → [`00480668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480668.md) FUN_00480668

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f558.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f598.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-0048065c) · [`00480670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-00480670) · [`00480690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md#insn-00480690)
- 新版 `0048069c`（命令位置の公開資料なし） · `004806b0`（命令位置の公開資料なし） · `004806d0`（命令位置の公開資料なし）

~~~diff
- 0048065c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048065c ["INT_ADD", "register:40f0:8", ["const:48065c:8", "const:4:8"]]
- 0048065c ["CALLIND", null, ["register:0:8"]]
+ 0048069c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048069c ["INT_ADD", "register:40f0:8", ["const:48069c:8", "const:4:8"]]
+ 0048069c ["CALLIND", null, ["register:0:8"]]
- 0048065c bytes 00013fd6
+ 0048069c bytes 00013fd6
- 00480670 ["INT_ADD", "register:40f0:8", ["const:480670:8", "const:4:8"]]
- 00480670 ["CALL", null, ["callee:0055f504:8"]]
+ 004806b0 ["INT_ADD", "register:40f0:8", ["const:4806b0:8", "const:4:8"]]
+ 004806b0 ["CALL", null, ["callee:0055f504:8"]]
- 00480670 bytes 957b0394
+ 004806b0 bytes 957b0394
- 00480690 ["INT_ADD", "register:40f0:8", ["const:480690:8", "const:4:8"]]
- 00480690 ["CALL", null, ["callee:0055f598:8"]]
+ 004806d0 ["INT_ADD", "register:40f0:8", ["const:4806d0:8", "const:4:8"]]
+ 004806d0 ["CALL", null, ["callee:0055f598:8"]]
- 00480690 bytes b27b0394
+ 004806d0 bytes b27b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-033b6c1211337c082c2bf316c55a2d5b"></a>

### [`004806bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md) → [`004806fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004806fc.md) FUN_004806fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f548.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f588.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004806f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-004806f0) · [`00480708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-00480708) · [`00480718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md#insn-00480718)
- 新版 `00480730`（命令位置の公開資料なし） · `00480748`（命令位置の公開資料なし） · `00480758`（命令位置の公開資料なし）

~~~diff
- 004806f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004806f0 ["INT_ADD", "register:40f0:8", ["const:4806f0:8", "const:4:8"]]
- 004806f0 ["CALLIND", null, ["register:0:8"]]
+ 00480730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480730 ["INT_ADD", "register:40f0:8", ["const:480730:8", "const:4:8"]]
+ 00480730 ["CALLIND", null, ["register:0:8"]]
- 004806f0 bytes 00013fd6
+ 00480730 bytes 00013fd6
- 00480708 ["INT_ADD", "register:40f0:8", ["const:480708:8", "const:4:8"]]
- 00480708 ["CALL", null, ["callee:0055f504:8"]]
+ 00480748 ["INT_ADD", "register:40f0:8", ["const:480748:8", "const:4:8"]]
+ 00480748 ["CALL", null, ["callee:0055f504:8"]]
- 00480708 bytes 6f7b0394
+ 00480748 bytes 6f7b0394
- 00480718 ["INT_ADD", "register:40f0:8", ["const:480718:8", "const:4:8"]]
- 00480718 ["CALL", null, ["callee:0055f588:8"]]
+ 00480758 ["INT_ADD", "register:40f0:8", ["const:480758:8", "const:4:8"]]
+ 00480758 ["CALL", null, ["callee:0055f588:8"]]
- 00480718 bytes 8c7b0394
+ 00480758 bytes 8c7b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a13ef8fb7b94c3388d8a61cba861e33"></a>

### [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) → [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) FUN_00480784

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`005b9a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a50.md) [`00675b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b94.md) [`006db06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db06c.md) [`0072ed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`00732944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732944.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 27件 [`005b9a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a90.md) [`00675bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675bd4.md) [`006db0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md) [`0072ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072ed80.md) [`0073299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/0073299c.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-00480778) · [`00480790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-00480790) · [`004807a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md#insn-004807a0)
- 新版 `004807b8`（命令位置の公開資料なし） · `004807d0`（命令位置の公開資料なし） · `004807e0`（命令位置の公開資料なし）

~~~diff
- 00480778 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480778 ["INT_ADD", "register:40f0:8", ["const:480778:8", "const:4:8"]]
- 00480778 ["CALLIND", null, ["register:0:8"]]
+ 004807b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004807b8 ["INT_ADD", "register:40f0:8", ["const:4807b8:8", "const:4:8"]]
+ 004807b8 ["CALLIND", null, ["register:0:8"]]
- 00480778 bytes 00013fd6
+ 004807b8 bytes 00013fd6
- 00480790 ["INT_ADD", "register:40f0:8", ["const:480790:8", "const:4:8"]]
- 00480790 ["CALL", null, ["callee:0055f504:8"]]
+ 004807d0 ["INT_ADD", "register:40f0:8", ["const:4807d0:8", "const:4:8"]]
+ 004807d0 ["CALL", null, ["callee:0055f504:8"]]
- 00480790 bytes 4d7b0394
+ 004807d0 bytes 4d7b0394
- 004807a0 ["INT_ADD", "register:40f0:8", ["const:4807a0:8", "const:4:8"]]
- 004807a0 ["CALL", null, ["callee:0055f5a8:8"]]
+ 004807e0 ["INT_ADD", "register:40f0:8", ["const:4807e0:8", "const:4:8"]]
+ 004807e0 ["CALL", null, ["callee:0055f5a8:8"]]
- 004807a0 bytes 727b0394
+ 004807e0 bytes 727b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e965f2950c2036e6717a81ea72e4b728"></a>

### [`004807cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md) → [`0048080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/0048080c.md) FUN_0048080c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`007380e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007380e4.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) [`009a9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9444.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 5件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 6件 [`0073813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/0073813c.md) [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`00981494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981494.md) [`009a9498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9498.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 5件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-00480808) · [`0048081c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-0048081c) · [`0048082c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md#insn-0048082c)
- 新版 `00480848`（命令位置の公開資料なし） · `0048085c`（命令位置の公開資料なし） · `0048086c`（命令位置の公開資料なし）

~~~diff
- 00480808 ["COPY", "register:0:8", ["register:4048:8"]]
- 00480808 ["INT_ADD", "register:40f0:8", ["const:480808:8", "const:4:8"]]
- 00480808 ["CALLIND", null, ["register:0:8"]]
+ 00480848 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00480848 ["INT_ADD", "register:40f0:8", ["const:480848:8", "const:4:8"]]
+ 00480848 ["CALLIND", null, ["register:0:8"]]
- 00480808 bytes 20013fd6
+ 00480848 bytes 20013fd6
- 0048081c ["INT_ADD", "register:40f0:8", ["const:48081c:8", "const:4:8"]]
- 0048081c ["CALL", null, ["callee:0055f504:8"]]
+ 0048085c ["INT_ADD", "register:40f0:8", ["const:48085c:8", "const:4:8"]]
+ 0048085c ["CALL", null, ["callee:0055f504:8"]]
- 0048081c bytes 2a7b0394
+ 0048085c bytes 2a7b0394
- 0048082c ["INT_ADD", "register:40f0:8", ["const:48082c:8", "const:4:8"]]
- 0048082c ["CALL", null, ["callee:0055f578:8"]]
+ 0048086c ["INT_ADD", "register:40f0:8", ["const:48086c:8", "const:4:8"]]
+ 0048086c ["CALL", null, ["callee:0055f578:8"]]
- 0048082c bytes 437b0394
+ 0048086c bytes 437b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d10b04fd04149c8f7a67cbb16841af5"></a>

### [`004808fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md) → [`0048093c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/0048093c.md) FUN_0048093c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 4件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 4件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480944) · [`00480958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480958) · [`00480968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004808fc.md#insn-00480968)
- 新版 `00480984`（命令位置の公開資料なし） · `00480998`（命令位置の公開資料なし） · `004809a8`（命令位置の公開資料なし）

~~~diff
- 00480944 ["COPY", "register:0:8", ["register:4048:8"]]
- 00480944 ["INT_ADD", "register:40f0:8", ["const:480944:8", "const:4:8"]]
- 00480944 ["CALLIND", null, ["register:0:8"]]
+ 00480984 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00480984 ["INT_ADD", "register:40f0:8", ["const:480984:8", "const:4:8"]]
+ 00480984 ["CALLIND", null, ["register:0:8"]]
- 00480944 bytes 20013fd6
+ 00480984 bytes 20013fd6
- 00480958 ["INT_ADD", "register:40f0:8", ["const:480958:8", "const:4:8"]]
- 00480958 ["CALL", null, ["callee:0055f504:8"]]
+ 00480998 ["INT_ADD", "register:40f0:8", ["const:480998:8", "const:4:8"]]
+ 00480998 ["CALL", null, ["callee:0055f504:8"]]
- 00480958 bytes db7a0394
+ 00480998 bytes db7a0394
- 00480968 ["INT_ADD", "register:40f0:8", ["const:480968:8", "const:4:8"]]
- 00480968 ["CALL", null, ["callee:0055f578:8"]]
+ 004809a8 ["INT_ADD", "register:40f0:8", ["const:4809a8:8", "const:4:8"]]
+ 004809a8 ["CALL", null, ["callee:0055f578:8"]]
- 00480968 bytes f47a0394
+ 004809a8 bytes f47a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccbaec1a909692a3dcf0d8b4cfa501f9"></a>

### [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) → [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) FUN_00480b78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 21件 [`005c0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0dc4.md) [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) [`00745434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745434.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 21件 [`005c0e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0e04.md) [`0066b52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b52c.md) [`006db074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md) [`00738628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738628.md) [`0074548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md#insn-00480b68) · [`00480b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md#insn-00480b8c)
- 新版 `00480ba8`（命令位置の公開資料なし） · `00480bcc`（命令位置の公開資料なし）

~~~diff
- 00480b68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480b68 ["INT_ADD", "register:40f0:8", ["const:480b68:8", "const:4:8"]]
- 00480b68 ["CALLIND", null, ["register:0:8"]]
+ 00480ba8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480ba8 ["INT_ADD", "register:40f0:8", ["const:480ba8:8", "const:4:8"]]
+ 00480ba8 ["CALLIND", null, ["register:0:8"]]
- 00480b68 bytes 00013fd6
+ 00480ba8 bytes 00013fd6
- 00480b8c ["INT_ADD", "register:40f0:8", ["const:480b8c:8", "const:4:8"]]
- 00480b8c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480bcc ["INT_ADD", "register:40f0:8", ["const:480bcc:8", "const:4:8"]]
+ 00480bcc ["CALL", null, ["callee:00c57fb0:8"]]
- 00480b8c bytes d55c1f94
+ 00480bcc bytes f95c1f94
~~~


<a id="compare-bfcf5eebd58b1875a3ca0735ae394f8f"></a>

### [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) → [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) FUN_00480bd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 26件 [`005c0dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c0dc4.md) [`00675ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675ed0.md) [`006a4d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 26件 [`005c0e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0e04.md) [`00675f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675f10.md) [`006a4dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md) [`006db074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md) [`00738628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738628.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md#insn-00480bc0) · [`00480be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md#insn-00480be4)
- 新版 `00480c00`（命令位置の公開資料なし） · `00480c24`（命令位置の公開資料なし）

~~~diff
- 00480bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480bc0 ["INT_ADD", "register:40f0:8", ["const:480bc0:8", "const:4:8"]]
- 00480bc0 ["CALLIND", null, ["register:0:8"]]
+ 00480c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480c00 ["INT_ADD", "register:40f0:8", ["const:480c00:8", "const:4:8"]]
+ 00480c00 ["CALLIND", null, ["register:0:8"]]
- 00480bc0 bytes 00013fd6
+ 00480c00 bytes 00013fd6
- 00480be4 ["INT_ADD", "register:40f0:8", ["const:480be4:8", "const:4:8"]]
- 00480be4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480c24 ["INT_ADD", "register:40f0:8", ["const:480c24:8", "const:4:8"]]
+ 00480c24 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480be4 bytes bf5c1f94
+ 00480c24 bytes e35c1f94
~~~


<a id="compare-5959f48be85c1ef0830180337f016c20"></a>

### [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) → [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) FUN_00480c28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 23件 [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`0066b9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b9a4.md) [`006a4d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md) [`006dc6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc6ac.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 23件 [`0066b52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b52c.md) [`0066b9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b9e4.md) [`006a4dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md) [`006dc704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md) [`00738628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738628.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md#insn-00480c18) · [`00480c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md#insn-00480c3c)
- 新版 `00480c58`（命令位置の公開資料なし） · `00480c7c`（命令位置の公開資料なし）

~~~diff
- 00480c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480c18 ["INT_ADD", "register:40f0:8", ["const:480c18:8", "const:4:8"]]
- 00480c18 ["CALLIND", null, ["register:0:8"]]
+ 00480c58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480c58 ["INT_ADD", "register:40f0:8", ["const:480c58:8", "const:4:8"]]
+ 00480c58 ["CALLIND", null, ["register:0:8"]]
- 00480c18 bytes 00013fd6
+ 00480c58 bytes 00013fd6
- 00480c3c ["INT_ADD", "register:40f0:8", ["const:480c3c:8", "const:4:8"]]
- 00480c3c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480c7c ["INT_ADD", "register:40f0:8", ["const:480c7c:8", "const:4:8"]]
+ 00480c7c ["CALL", null, ["callee:00c57fb0:8"]]
- 00480c3c bytes a95c1f94
+ 00480c7c bytes cd5c1f94
~~~


<a id="compare-ca4009993c2c0d293e4709cfb8ec144a"></a>

### [`00480c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md) → [`00480c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c80.md) FUN_00480c80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md#insn-00480c70) · [`00480c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c40.md#insn-00480c94)
- 新版 `00480cb0`（命令位置の公開資料なし） · `00480cd4`（命令位置の公開資料なし）

~~~diff
- 00480c70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480c70 ["INT_ADD", "register:40f0:8", ["const:480c70:8", "const:4:8"]]
- 00480c70 ["CALLIND", null, ["register:0:8"]]
+ 00480cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480cb0 ["INT_ADD", "register:40f0:8", ["const:480cb0:8", "const:4:8"]]
+ 00480cb0 ["CALLIND", null, ["register:0:8"]]
- 00480c70 bytes 00013fd6
+ 00480cb0 bytes 00013fd6
- 00480c94 ["INT_ADD", "register:40f0:8", ["const:480c94:8", "const:4:8"]]
- 00480c94 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480cd4 ["INT_ADD", "register:40f0:8", ["const:480cd4:8", "const:4:8"]]
+ 00480cd4 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480c94 bytes 935c1f94
+ 00480cd4 bytes b75c1f94
~~~


<a id="compare-7b9609da652129b28205d9e3a09af741"></a>

### [`00480c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md) → [`00480cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480cd8.md) FUN_00480cd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md#insn-00480cc8) · [`00480cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480c98.md#insn-00480cec)
- 新版 `00480d08`（命令位置の公開資料なし） · `00480d2c`（命令位置の公開資料なし）

~~~diff
- 00480cc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480cc8 ["INT_ADD", "register:40f0:8", ["const:480cc8:8", "const:4:8"]]
- 00480cc8 ["CALLIND", null, ["register:0:8"]]
+ 00480d08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480d08 ["INT_ADD", "register:40f0:8", ["const:480d08:8", "const:4:8"]]
+ 00480d08 ["CALLIND", null, ["register:0:8"]]
- 00480cc8 bytes 00013fd6
+ 00480d08 bytes 00013fd6
- 00480cec ["INT_ADD", "register:40f0:8", ["const:480cec:8", "const:4:8"]]
- 00480cec ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480d2c ["INT_ADD", "register:40f0:8", ["const:480d2c:8", "const:4:8"]]
+ 00480d2c ["CALL", null, ["callee:00c57fb0:8"]]
- 00480cec bytes 7d5c1f94
+ 00480d2c bytes a15c1f94
~~~


<a id="compare-d58300562bda6b56fa9fc34e91169c2d"></a>

### [`00480cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md) → [`00480d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d30.md) FUN_00480d30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) [`007385d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/007385d0.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`0072efc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072efc4.md) [`00732b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732b54.md) [`00738628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00738/00738628.md) [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md#insn-00480d20) · [`00480d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480cf0.md#insn-00480d44)
- 新版 `00480d60`（命令位置の公開資料なし） · `00480d84`（命令位置の公開資料なし）

~~~diff
- 00480d20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480d20 ["INT_ADD", "register:40f0:8", ["const:480d20:8", "const:4:8"]]
- 00480d20 ["CALLIND", null, ["register:0:8"]]
+ 00480d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480d60 ["INT_ADD", "register:40f0:8", ["const:480d60:8", "const:4:8"]]
+ 00480d60 ["CALLIND", null, ["register:0:8"]]
- 00480d20 bytes 00013fd6
+ 00480d60 bytes 00013fd6
- 00480d44 ["INT_ADD", "register:40f0:8", ["const:480d44:8", "const:4:8"]]
- 00480d44 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480d84 ["INT_ADD", "register:40f0:8", ["const:480d84:8", "const:4:8"]]
+ 00480d84 ["CALL", null, ["callee:00c57fb0:8"]]
- 00480d44 bytes 675c1f94
+ 00480d84 bytes 8b5c1f94
~~~


<a id="compare-3e84acdc3b3a732da306a96a98550e28"></a>

### [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) → [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) FUN_00480d88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 32件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`0066b4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b4ec.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 32件 [`005b9a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a4c.md) [`0066b52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b52c.md) [`006db074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md) [`0072efc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072efc4.md) [`00732b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732b54.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md#insn-00480d78) · [`00480d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md#insn-00480d9c)
- 新版 `00480db8`（命令位置の公開資料なし） · `00480ddc`（命令位置の公開資料なし）

~~~diff
- 00480d78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480d78 ["INT_ADD", "register:40f0:8", ["const:480d78:8", "const:4:8"]]
- 00480d78 ["CALLIND", null, ["register:0:8"]]
+ 00480db8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480db8 ["INT_ADD", "register:40f0:8", ["const:480db8:8", "const:4:8"]]
+ 00480db8 ["CALLIND", null, ["register:0:8"]]
- 00480d78 bytes 00013fd6
+ 00480db8 bytes 00013fd6
- 00480d9c ["INT_ADD", "register:40f0:8", ["const:480d9c:8", "const:4:8"]]
- 00480d9c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00480ddc ["INT_ADD", "register:40f0:8", ["const:480ddc:8", "const:4:8"]]
+ 00480ddc ["CALL", null, ["callee:00c57fb0:8"]]
- 00480d9c bytes 515c1f94
+ 00480ddc bytes 755c1f94
~~~


<a id="compare-be8be127a3dedc2c13fe4ee5556e4d40"></a>

### [`00480da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md) → [`00480de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480de0.md) FUN_00480de0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f51c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f55c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480dcc) · [`00480ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480ddc) · [`00480dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480da0.md#insn-00480dfc)
- 新版 `00480e0c`（命令位置の公開資料なし） · `00480e1c`（命令位置の公開資料なし） · `00480e3c`（命令位置の公開資料なし）

~~~diff
- 00480dcc ["INT_ADD", "register:40f0:8", ["const:480dcc:8", "const:4:8"]]
- 00480dcc ["CALL", null, ["callee:0055f504:8"]]
+ 00480e0c ["INT_ADD", "register:40f0:8", ["const:480e0c:8", "const:4:8"]]
+ 00480e0c ["CALL", null, ["callee:0055f504:8"]]
- 00480dcc bytes be790394
+ 00480e0c bytes be790394
- 00480ddc ["INT_ADD", "register:40f0:8", ["const:480ddc:8", "const:4:8"]]
- 00480ddc ["CALL", null, ["callee:0055f55c:8"]]
+ 00480e1c ["INT_ADD", "register:40f0:8", ["const:480e1c:8", "const:4:8"]]
+ 00480e1c ["CALL", null, ["callee:0055f55c:8"]]
- 00480ddc bytes d0790394
+ 00480e1c bytes d0790394
- 00480dfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00480dfc ["INT_ADD", "register:40f0:8", ["const:480dfc:8", "const:4:8"]]
- 00480dfc ["CALLIND", null, ["register:0:8"]]
+ 00480e3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480e3c ["INT_ADD", "register:40f0:8", ["const:480e3c:8", "const:4:8"]]
+ 00480e3c ["CALLIND", null, ["register:0:8"]]
- 00480dfc bytes 00013fd6
+ 00480e3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deed62bf47f55768da82a4468b83cfa6"></a>

### [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) → [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) FUN_00480e68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 29件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`005e0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0108.md) [`005e01a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e01a8.md) [`005e0254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0254.md) [`006dc6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc6ac.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 29件 [`005b9a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a4c.md) [`005e0148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0148.md) [`005e01e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e01e8.md) [`005e0294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0294.md) [`006dc704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e54) · [`00480e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e64) · [`00480e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md#insn-00480e84)
- 新版 `00480e94`（命令位置の公開資料なし） · `00480ea4`（命令位置の公開資料なし） · `00480ec4`（命令位置の公開資料なし）

~~~diff
- 00480e54 ["INT_ADD", "register:40f0:8", ["const:480e54:8", "const:4:8"]]
- 00480e54 ["CALL", null, ["callee:0055f504:8"]]
+ 00480e94 ["INT_ADD", "register:40f0:8", ["const:480e94:8", "const:4:8"]]
+ 00480e94 ["CALL", null, ["callee:0055f504:8"]]
- 00480e54 bytes 9c790394
+ 00480e94 bytes 9c790394
- 00480e64 ["INT_ADD", "register:40f0:8", ["const:480e64:8", "const:4:8"]]
- 00480e64 ["CALL", null, ["callee:0055f578:8"]]
+ 00480ea4 ["INT_ADD", "register:40f0:8", ["const:480ea4:8", "const:4:8"]]
+ 00480ea4 ["CALL", null, ["callee:0055f578:8"]]
- 00480e64 bytes b5790394
+ 00480ea4 bytes b5790394
- 00480e84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480e84 ["INT_ADD", "register:40f0:8", ["const:480e84:8", "const:4:8"]]
- 00480e84 ["CALLIND", null, ["register:0:8"]]
+ 00480ec4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480ec4 ["INT_ADD", "register:40f0:8", ["const:480ec4:8", "const:4:8"]]
+ 00480ec4 ["CALLIND", null, ["register:0:8"]]
- 00480e84 bytes 00013fd6
+ 00480ec4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2575cb7a2c50322b0df154ba28618dda"></a>

### [`00480eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md) → [`00480ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480ef0.md) FUN_00480ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f580.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480edc) · [`00480eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480eec) · [`00480f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480eb0.md#insn-00480f0c)
- 新版 `00480f1c`（命令位置の公開資料なし） · `00480f2c`（命令位置の公開資料なし） · `00480f4c`（命令位置の公開資料なし）

~~~diff
- 00480edc ["INT_ADD", "register:40f0:8", ["const:480edc:8", "const:4:8"]]
- 00480edc ["CALL", null, ["callee:0055f504:8"]]
+ 00480f1c ["INT_ADD", "register:40f0:8", ["const:480f1c:8", "const:4:8"]]
+ 00480f1c ["CALL", null, ["callee:0055f504:8"]]
- 00480edc bytes 7a790394
+ 00480f1c bytes 7a790394
- 00480eec ["INT_ADD", "register:40f0:8", ["const:480eec:8", "const:4:8"]]
- 00480eec ["CALL", null, ["callee:0055f580:8"]]
+ 00480f2c ["INT_ADD", "register:40f0:8", ["const:480f2c:8", "const:4:8"]]
+ 00480f2c ["CALL", null, ["callee:0055f580:8"]]
- 00480eec bytes 95790394
+ 00480f2c bytes 95790394
- 00480f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00480f0c ["INT_ADD", "register:40f0:8", ["const:480f0c:8", "const:4:8"]]
- 00480f0c ["CALLIND", null, ["register:0:8"]]
+ 00480f4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00480f4c ["INT_ADD", "register:40f0:8", ["const:480f4c:8", "const:4:8"]]
+ 00480f4c ["CALLIND", null, ["register:0:8"]]
- 00480f0c bytes 00013fd6
+ 00480f4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e61030f511e3d00e206b7870ab453469"></a>

### [`00480f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md) → [`00480f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480f78.md) FUN_00480f78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008397ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/008397ec.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00839844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839844.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00480fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md#insn-00480fd0) · [`00481004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480f38.md#insn-00481004)
- 新版 `00481010`（命令位置の公開資料なし） · `00481044`（命令位置の公開資料なし）

~~~diff
- 00480fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00480fd0 ["INT_ADD", "register:40f0:8", ["const:480fd0:8", "const:4:8"]]
- 00480fd0 ["CALLIND", null, ["register:0:8"]]
+ 00481010 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00481010 ["INT_ADD", "register:40f0:8", ["const:481010:8", "const:4:8"]]
+ 00481010 ["CALLIND", null, ["register:0:8"]]
- 00480fd0 bytes 00013fd6
+ 00481010 bytes 00013fd6
- 00481004 ["INT_ADD", "register:40f0:8", ["const:481004:8", "const:4:8"]]
- 00481004 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00481044 ["INT_ADD", "register:40f0:8", ["const:481044:8", "const:4:8"]]
+ 00481044 ["CALL", null, ["callee:00c57fb0:8"]]
- 00481004 bytes b75b1f94
+ 00481044 bytes db5b1f94
~~~


<a id="compare-9b0639bd3cbb1d0abbf09c2bdc4cc432"></a>

### [`00481008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md) → [`00481048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481048.md) FUN_00481048

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f548.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f588.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481038) · [`00481048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481048) · [`00481068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481008.md#insn-00481068)
- 新版 `00481078`（命令位置の公開資料なし） · `00481088`（命令位置の公開資料なし） · `004810a8`（命令位置の公開資料なし）

~~~diff
- 00481038 ["INT_ADD", "register:40f0:8", ["const:481038:8", "const:4:8"]]
- 00481038 ["CALL", null, ["callee:0055f504:8"]]
+ 00481078 ["INT_ADD", "register:40f0:8", ["const:481078:8", "const:4:8"]]
+ 00481078 ["CALL", null, ["callee:0055f504:8"]]
- 00481038 bytes 23790394
+ 00481078 bytes 23790394
- 00481048 ["INT_ADD", "register:40f0:8", ["const:481048:8", "const:4:8"]]
- 00481048 ["CALL", null, ["callee:0055f588:8"]]
+ 00481088 ["INT_ADD", "register:40f0:8", ["const:481088:8", "const:4:8"]]
+ 00481088 ["CALL", null, ["callee:0055f588:8"]]
- 00481048 bytes 40790394
+ 00481088 bytes 40790394
- 00481068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00481068 ["INT_ADD", "register:40f0:8", ["const:481068:8", "const:4:8"]]
- 00481068 ["CALLIND", null, ["register:0:8"]]
+ 004810a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004810a8 ["INT_ADD", "register:40f0:8", ["const:4810a8:8", "const:4:8"]]
+ 004810a8 ["CALLIND", null, ["register:0:8"]]
- 00481068 bytes 00013fd6
+ 004810a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-326c94b7fb33a7277964917cb4153a83"></a>

### [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md) → [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md) FUN_004810d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`005b9a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a0c.md) [`00675ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675ed0.md) [`006db01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db01c.md) [`0072ef6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ef6c.md) [`00732afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732afc.md) · 呼出先 3件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f568.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 25件 [`005b9a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9a4c.md) [`00675f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675f10.md) [`006db074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md) [`0072efc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072e/0072efc4.md) [`00732b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732b54.md) · 呼出先 3件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004810c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810c8) · [`004810d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810d8) · [`004810f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md#insn-004810f8)
- 新版 `00481108`（命令位置の公開資料なし） · `00481118`（命令位置の公開資料なし） · `00481138`（命令位置の公開資料なし）

~~~diff
- 004810c8 ["INT_ADD", "register:40f0:8", ["const:4810c8:8", "const:4:8"]]
- 004810c8 ["CALL", null, ["callee:0055f504:8"]]
+ 00481108 ["INT_ADD", "register:40f0:8", ["const:481108:8", "const:4:8"]]
+ 00481108 ["CALL", null, ["callee:0055f504:8"]]
- 004810c8 bytes ff780394
+ 00481108 bytes ff780394
- 004810d8 ["INT_ADD", "register:40f0:8", ["const:4810d8:8", "const:4:8"]]
- 004810d8 ["CALL", null, ["callee:0055f5a8:8"]]
+ 00481118 ["INT_ADD", "register:40f0:8", ["const:481118:8", "const:4:8"]]
+ 00481118 ["CALL", null, ["callee:0055f5a8:8"]]
- 004810d8 bytes 24790394
+ 00481118 bytes 24790394
- 004810f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004810f8 ["INT_ADD", "register:40f0:8", ["const:4810f8:8", "const:4:8"]]
- 004810f8 ["CALLIND", null, ["register:0:8"]]
+ 00481138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00481138 ["INT_ADD", "register:40f0:8", ["const:481138:8", "const:4:8"]]
+ 00481138 ["CALLIND", null, ["register:0:8"]]
- 004810f8 bytes 00013fd6
+ 00481138 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5610b066a93a57954609a1c5110e91f9"></a>

### [`00481128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md) → [`00481168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481168.md) FUN_00481168

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00737e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737e8c.md) [`0079fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md) [`0098157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098157c.md) [`009a9364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9364.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 6件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 6件 [`00737ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00737/00737ee4.md) [`0079fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md) [`009815d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009815d0.md) [`009a93b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a93b8.md) [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 6件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048116c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048116c) · [`0048117c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048117c) · [`0048119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md#insn-0048119c)
- 新版 `004811ac`（命令位置の公開資料なし） · `004811bc`（命令位置の公開資料なし） · `004811dc`（命令位置の公開資料なし）

~~~diff
- 0048116c ["INT_ADD", "register:40f0:8", ["const:48116c:8", "const:4:8"]]
- 0048116c ["CALL", null, ["callee:0055f504:8"]]
+ 004811ac ["INT_ADD", "register:40f0:8", ["const:4811ac:8", "const:4:8"]]
+ 004811ac ["CALL", null, ["callee:0055f504:8"]]
- 0048116c bytes d6780394
+ 004811ac bytes d6780394
- 0048117c ["INT_ADD", "register:40f0:8", ["const:48117c:8", "const:4:8"]]
- 0048117c ["CALL", null, ["callee:0055f578:8"]]
+ 004811bc ["INT_ADD", "register:40f0:8", ["const:4811bc:8", "const:4:8"]]
+ 004811bc ["CALL", null, ["callee:0055f578:8"]]
- 0048117c bytes ef780394
+ 004811bc bytes ef780394
- 0048119c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048119c ["INT_ADD", "register:40f0:8", ["const:48119c:8", "const:4:8"]]
- 0048119c ["CALLIND", null, ["register:0:8"]]
+ 004811dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004811dc ["INT_ADD", "register:40f0:8", ["const:4811dc:8", "const:4:8"]]
+ 004811dc ["CALLIND", null, ["register:0:8"]]
- 0048119c bytes 00013fd6
+ 004811dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-249ae8fff772d665e02a3e66e7451f8f"></a>

### [`00481240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md) → [`00481280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481280.md) FUN_00481280

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0079fe48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079fe48.md) [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) · 呼出先 9件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f538.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 2件 [`0079fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fea0.md) [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) · 呼出先 9件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f578.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-00481270) · [`0048127c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-0048127c) · [`0048128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481240.md#insn-0048128c)
- 新版 `004812b0`（命令位置の公開資料なし） · `004812bc`（命令位置の公開資料なし） · `004812cc`（命令位置の公開資料なし）

~~~diff
- 00481270 ["INT_ADD", "register:40f0:8", ["const:481270:8", "const:4:8"]]
- 00481270 ["CALL", null, ["callee:00597a8c:8"]]
+ 004812b0 ["INT_ADD", "register:40f0:8", ["const:4812b0:8", "const:4:8"]]
+ 004812b0 ["CALL", null, ["callee:00597a8c:8"]]
- 00481270 bytes f7590494
+ 004812b0 bytes f7590494
- 0048127c ["INT_ADD", "register:40f0:8", ["const:48127c:8", "const:4:8"]]
- 0048127c ["CALL", null, ["callee:0055f504:8"]]
+ 004812bc ["INT_ADD", "register:40f0:8", ["const:4812bc:8", "const:4:8"]]
+ 004812bc ["CALL", null, ["callee:0055f504:8"]]
- 0048127c bytes 92780394
+ 004812bc bytes 92780394
- 0048128c ["INT_ADD", "register:40f0:8", ["const:48128c:8", "const:4:8"]]
- 0048128c ["CALL", null, ["callee:0055f578:8"]]
+ 004812cc ["INT_ADD", "register:40f0:8", ["const:4812cc:8", "const:4:8"]]
+ 004812cc ["CALL", null, ["callee:0055f578:8"]]
- 0048128c bytes ab780394
+ 004812cc bytes ab780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e07d6364a48c881cbf6edd3bd94fec"></a>

### [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) → [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) FUN_00481ec0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 11件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`004b3f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481ebc) · [`00481f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481f10) · [`00481f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md#insn-00481f44)
- 新版 `00481efc`（命令位置の公開資料なし） · `00481f50`（命令位置の公開資料なし） · `00481f84`（命令位置の公開資料なし）

~~~diff
- 00481ebc ["INT_ADD", "register:40f0:8", ["const:481ebc:8", "const:4:8"]]
- 00481ebc ["CALL", null, ["callee:00c580b0:8"]]
+ 00481efc ["INT_ADD", "register:40f0:8", ["const:481efc:8", "const:4:8"]]
+ 00481efc ["CALL", null, ["callee:00c580b0:8"]]
- 00481ebc bytes 49581f94
+ 00481efc bytes 6d581f94
- 00481f10 ["INT_ADD", "register:40f0:8", ["const:481f10:8", "const:4:8"]]
- 00481f10 ["CALL", null, ["callee:00c57f60:8"]]
+ 00481f50 ["INT_ADD", "register:40f0:8", ["const:481f50:8", "const:4:8"]]
+ 00481f50 ["CALL", null, ["callee:00c57f60:8"]]
- 00481f10 bytes e0571f94
+ 00481f50 bytes 04581f94
- 00481f44 ["INT_ADD", "register:40f0:8", ["const:481f44:8", "const:4:8"]]
- 00481f44 ["CALL", null, ["callee:00c58010:8"]]
+ 00481f84 ["INT_ADD", "register:40f0:8", ["const:481f84:8", "const:4:8"]]
+ 00481f84 ["CALL", null, ["callee:00c58010:8"]]
- 00481f44 bytes ff571f94
+ 00481f84 bytes 23581f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3426b3bcc8519d2d5ee40f30132fb7ee"></a>

### [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md) → [`00481fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481fc4.md) FUN_00481fc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`004846dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md) [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 8件 [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`0048471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/0048471c.md) [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00481fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481fc0) · [`00481fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481fe0) · [`00481ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md#insn-00481ff4)
- 新版 `00482000`（命令位置の公開資料なし） · `00482020`（命令位置の公開資料なし） · `00482034`（命令位置の公開資料なし）

~~~diff
- 00481fc0 ["INT_ADD", "register:40f0:8", ["const:481fc0:8", "const:4:8"]]
- 00481fc0 ["CALL", null, ["callee:00550be4:8"]]
+ 00482000 ["INT_ADD", "register:40f0:8", ["const:482000:8", "const:4:8"]]
+ 00482000 ["CALL", null, ["callee:00550be4:8"]]
- 00481fc0 bytes f93a0394
+ 00482000 bytes f93a0394
- 00481fe0 ["INT_ADD", "register:40f0:8", ["const:481fe0:8", "const:4:8"]]
- 00481fe0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00482020 ["INT_ADD", "register:40f0:8", ["const:482020:8", "const:4:8"]]
+ 00482020 ["CALL", null, ["callee:00c53da0:8"]]
- 00481fe0 bytes 48471f94
+ 00482020 bytes 60471f94
- 00481ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00481ff4 ["INT_ADD", "register:40f0:8", ["const:481ff4:8", "const:4:8"]]
- 00481ff4 ["CALLIND", null, ["register:0:8"]]
+ 00482034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482034 ["INT_ADD", "register:40f0:8", ["const:482034:8", "const:4:8"]]
+ 00482034 ["CALLIND", null, ["register:0:8"]]
- 00481ff4 bytes 00013fd6
+ 00482034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3bb642c60243c45a78e3f61dd042e14"></a>

### [`004820e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md) → [`00482120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482120.md) FUN_00482120

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048211c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-0048211c) · [`0048212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-0048212c) · [`00482140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820e0.md#insn-00482140)
- 新版 `0048215c`（命令位置の公開資料なし） · `0048216c`（命令位置の公開資料なし） · `00482180`（命令位置の公開資料なし）

~~~diff
- 0048211c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048211c ["INT_ADD", "register:40f0:8", ["const:48211c:8", "const:4:8"]]
- 0048211c ["CALLIND", null, ["register:0:8"]]
+ 0048215c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0048215c ["INT_ADD", "register:40f0:8", ["const:48215c:8", "const:4:8"]]
+ 0048215c ["CALLIND", null, ["register:0:8"]]
- 0048211c bytes 20013fd6
+ 0048215c bytes 20013fd6
- 0048212c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048212c ["INT_ADD", "register:40f0:8", ["const:48212c:8", "const:4:8"]]
- 0048212c ["CALLIND", null, ["register:0:8"]]
+ 0048216c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048216c ["INT_ADD", "register:40f0:8", ["const:48216c:8", "const:4:8"]]
+ 0048216c ["CALLIND", null, ["register:0:8"]]
- 0048212c bytes 00013fd6
+ 0048216c bytes 00013fd6
- 00482140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482140 ["INT_ADD", "register:40f0:8", ["const:482140:8", "const:4:8"]]
- 00482140 ["CALLIND", null, ["register:0:8"]]
+ 00482180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482180 ["INT_ADD", "register:40f0:8", ["const:482180:8", "const:4:8"]]
+ 00482180 ["CALLIND", null, ["register:0:8"]]
- 00482140 bytes 00013fd6
+ 00482180 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-416f1312fe7e10043505505ff0c6ce18"></a>

### [`00482250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md) → [`00482290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482290.md) FUN_00482290

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 8件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00a14de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 8件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004822cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-004822cc) · [`004822ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-004822ec) · [`00482300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482250.md#insn-00482300)
- 新版 `0048230c`（命令位置の公開資料なし） · `0048232c`（命令位置の公開資料なし） · `00482340`（命令位置の公開資料なし）

~~~diff
- 004822cc ["INT_ADD", "register:40f0:8", ["const:4822cc:8", "const:4:8"]]
- 004822cc ["CALL", null, ["callee:00597650:8"]]
+ 0048230c ["INT_ADD", "register:40f0:8", ["const:48230c:8", "const:4:8"]]
+ 0048230c ["CALL", null, ["callee:00597650:8"]]
- 004822cc bytes d1540494
+ 0048230c bytes d1540494
- 004822ec ["INT_ADD", "register:40f0:8", ["const:4822ec:8", "const:4:8"]]
- 004822ec ["CALL", null, ["callee:00c53da0:8"]]
+ 0048232c ["INT_ADD", "register:40f0:8", ["const:48232c:8", "const:4:8"]]
+ 0048232c ["CALL", null, ["callee:00c53da0:8"]]
- 004822ec bytes 85461f94
+ 0048232c bytes 9d461f94
- 00482300 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482300 ["INT_ADD", "register:40f0:8", ["const:482300:8", "const:4:8"]]
- 00482300 ["CALLIND", null, ["register:0:8"]]
+ 00482340 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482340 ["INT_ADD", "register:40f0:8", ["const:482340:8", "const:4:8"]]
+ 00482340 ["CALLIND", null, ["register:0:8"]]
- 00482300 bytes 00013fd6
+ 00482340 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e7c5fc132dd1f68c939b669a5d5c63"></a>

### [`004823fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md) → [`0048243c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/0048243c.md) FUN_0048243c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0063a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a200.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 5件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 3件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0063a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a240.md) [`009818cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009818cc.md) · 呼出先 5件 [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-00482478) · [`00482498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-00482498) · [`004824ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md#insn-004824ac)
- 新版 `004824b8`（命令位置の公開資料なし） · `004824d8`（命令位置の公開資料なし） · `004824ec`（命令位置の公開資料なし）

~~~diff
- 00482478 ["INT_ADD", "register:40f0:8", ["const:482478:8", "const:4:8"]]
- 00482478 ["CALL", null, ["callee:00597650:8"]]
+ 004824b8 ["INT_ADD", "register:40f0:8", ["const:4824b8:8", "const:4:8"]]
+ 004824b8 ["CALL", null, ["callee:00597650:8"]]
- 00482478 bytes 66540494
+ 004824b8 bytes 66540494
- 00482498 ["INT_ADD", "register:40f0:8", ["const:482498:8", "const:4:8"]]
- 00482498 ["CALL", null, ["callee:00c53da0:8"]]
+ 004824d8 ["INT_ADD", "register:40f0:8", ["const:4824d8:8", "const:4:8"]]
+ 004824d8 ["CALL", null, ["callee:00c53da0:8"]]
- 00482498 bytes 1a461f94
+ 004824d8 bytes 32461f94
- 004824ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004824ac ["INT_ADD", "register:40f0:8", ["const:4824ac:8", "const:4:8"]]
- 004824ac ["CALLIND", null, ["register:0:8"]]
+ 004824ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004824ec ["INT_ADD", "register:40f0:8", ["const:4824ec:8", "const:4:8"]]
+ 004824ec ["CALLIND", null, ["register:0:8"]]
- 004824ac bytes 00013fd6
+ 004824ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8469cd0041a888220ef544ae0727a58e"></a>

### [`00482538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md) → [`00482578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482578.md) FUN_00482578

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0063a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a200.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0063a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a240.md) [`009818cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009818cc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md#insn-00482560)
- 新版 `004825a0`（命令位置の公開資料なし）

~~~diff
- 00482560 ["COPY", "register:0:8", ["register:4048:8"]]
- 00482560 ["INT_ADD", "register:40f0:8", ["const:482560:8", "const:4:8"]]
- 00482560 ["CALLIND", null, ["register:0:8"]]
+ 004825a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004825a0 ["INT_ADD", "register:40f0:8", ["const:4825a0:8", "const:4:8"]]
+ 004825a0 ["CALLIND", null, ["register:0:8"]]
- 00482560 bytes 20013fd6
+ 004825a0 bytes 20013fd6
~~~


<a id="compare-7e458aa3080c97db719cff43f7e69359"></a>

### [`004825e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md) → [`00482620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482620.md) FUN_00482620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 11件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 8件 [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00637890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00637/00637890.md) [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) · 呼出先 11件 [`0055e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b0.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00482620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482620) · [`00482640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482640) · [`00482650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md#insn-00482650)
- 新版 `00482660`（命令位置の公開資料なし） · `00482680`（命令位置の公開資料なし） · `00482690`（命令位置の公開資料なし）

~~~diff
- 00482620 ["COPY", "register:0:8", ["register:4048:8"]]
- 00482620 ["INT_ADD", "register:40f0:8", ["const:482620:8", "const:4:8"]]
- 00482620 ["CALLIND", null, ["register:0:8"]]
+ 00482660 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00482660 ["INT_ADD", "register:40f0:8", ["const:482660:8", "const:4:8"]]
+ 00482660 ["CALLIND", null, ["register:0:8"]]
- 00482620 bytes 20013fd6
+ 00482660 bytes 20013fd6
- 00482640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482640 ["INT_ADD", "register:40f0:8", ["const:482640:8", "const:4:8"]]
- 00482640 ["CALLIND", null, ["register:0:8"]]
+ 00482680 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482680 ["INT_ADD", "register:40f0:8", ["const:482680:8", "const:4:8"]]
+ 00482680 ["CALLIND", null, ["register:0:8"]]
- 00482640 bytes 00013fd6
+ 00482680 bytes 00013fd6
- 00482650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00482650 ["INT_ADD", "register:40f0:8", ["const:482650:8", "const:4:8"]]
- 00482650 ["CALLIND", null, ["register:0:8"]]
+ 00482690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00482690 ["INT_ADD", "register:40f0:8", ["const:482690:8", "const:4:8"]]
+ 00482690 ["CALLIND", null, ["register:0:8"]]
- 00482650 bytes 00013fd6
+ 00482690 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e56ed5122e16f8dd9446019a3820a30c"></a>

### [`0048388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md) → [`004838cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/004838cc.md) FUN_004838cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) · 呼出先 1件 [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md)
- 新版 呼出元 2件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) · 呼出先 1件 [`004856b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004856b8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004838a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md#insn-004838a8)
- 新版 `004838e8`（命令位置の公開資料なし）

~~~diff
- 004838a8 ["INT_ADD", "register:40f0:8", ["const:4838a8:8", "const:4:8"]]
- 004838a8 ["CALL", null, ["callee:004856b8:8"]]
+ 004838e8 ["INT_ADD", "register:40f0:8", ["const:4838e8:8", "const:4:8"]]
+ 004838e8 ["CALL", null, ["callee:004856b8:8"]]
- 004838a8 bytes 74070094
+ 004838e8 bytes 74070094
~~~


<a id="compare-113c1bbe7515774a1149677118a3ff44"></a>

### [`00483eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md) → [`00483ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/00483ef0.md) FUN_00483ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md#insn-00483ecc) · [`00483eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483eb0.md#insn-00483eec)
- 新版 `00483f0c`（命令位置の公開資料なし） · `00483f2c`（命令位置の公開資料なし）

~~~diff
- 00483ecc ["INT_ADD", "register:40f0:8", ["const:483ecc:8", "const:4:8"]]
- 00483ecc ["CALL", null, ["callee:00c53da0:8"]]
+ 00483f0c ["INT_ADD", "register:40f0:8", ["const:483f0c:8", "const:4:8"]]
+ 00483f0c ["CALL", null, ["callee:00c53da0:8"]]
- 00483ecc bytes 8d3f1f94
+ 00483f0c bytes a53f1f94
- 00483eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00483eec ["INT_ADD", "register:40f0:8", ["const:483eec:8", "const:4:8"]]
- 00483eec ["CALLIND", null, ["register:0:8"]]
+ 00483f2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483f2c ["INT_ADD", "register:40f0:8", ["const:483f2c:8", "const:4:8"]]
+ 00483f2c ["CALLIND", null, ["register:0:8"]]
- 00483eec bytes 00013fd6
+ 00483f2c bytes 00013fd6
~~~


<a id="compare-2b8a8fb1932bf7d84ac18dcb5ad89c06"></a>

### [`00483f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md) → [`00483f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/00483f40.md) FUN_00483f40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md#insn-00483f1c) · [`00483f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f00.md#insn-00483f3c)
- 新版 `00483f5c`（命令位置の公開資料なし） · `00483f7c`（命令位置の公開資料なし）

~~~diff
- 00483f1c ["INT_ADD", "register:40f0:8", ["const:483f1c:8", "const:4:8"]]
- 00483f1c ["CALL", null, ["callee:00c53da0:8"]]
+ 00483f5c ["INT_ADD", "register:40f0:8", ["const:483f5c:8", "const:4:8"]]
+ 00483f5c ["CALL", null, ["callee:00c53da0:8"]]
- 00483f1c bytes 793f1f94
+ 00483f5c bytes 913f1f94
- 00483f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00483f3c ["INT_ADD", "register:40f0:8", ["const:483f3c:8", "const:4:8"]]
- 00483f3c ["CALLIND", null, ["register:0:8"]]
+ 00483f7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483f7c ["INT_ADD", "register:40f0:8", ["const:483f7c:8", "const:4:8"]]
+ 00483f7c ["CALLIND", null, ["register:0:8"]]
- 00483f3c bytes 00013fd6
+ 00483f7c bytes 00013fd6
~~~


<a id="compare-903e08f6deee4bc91a09d194c5f1087e"></a>

### [`00483f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md) → [`00483f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/00483f90.md) FUN_00483f90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md#insn-00483f6c) · [`00483f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483f50.md#insn-00483f8c)
- 新版 `00483fac`（命令位置の公開資料なし） · `00483fcc`（命令位置の公開資料なし）

~~~diff
- 00483f6c ["INT_ADD", "register:40f0:8", ["const:483f6c:8", "const:4:8"]]
- 00483f6c ["CALL", null, ["callee:00c53da0:8"]]
+ 00483fac ["INT_ADD", "register:40f0:8", ["const:483fac:8", "const:4:8"]]
+ 00483fac ["CALL", null, ["callee:00c53da0:8"]]
- 00483f6c bytes 653f1f94
+ 00483fac bytes 7d3f1f94
- 00483f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00483f8c ["INT_ADD", "register:40f0:8", ["const:483f8c:8", "const:4:8"]]
- 00483f8c ["CALLIND", null, ["register:0:8"]]
+ 00483fcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00483fcc ["INT_ADD", "register:40f0:8", ["const:483fcc:8", "const:4:8"]]
+ 00483fcc ["CALLIND", null, ["register:0:8"]]
- 00483f8c bytes 00013fd6
+ 00483fcc bytes 00013fd6
~~~


<a id="compare-ac811b6b9604ae39a7f05510984b8de3"></a>

### [`00483fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md) → [`00483fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/00483fe0.md) FUN_00483fe0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00483fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md#insn-00483fbc) · [`00483fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483fa0.md#insn-00483fdc)
- 新版 `00483ffc`（命令位置の公開資料なし） · `0048401c`（命令位置の公開資料なし）

~~~diff
- 00483fbc ["INT_ADD", "register:40f0:8", ["const:483fbc:8", "const:4:8"]]
- 00483fbc ["CALL", null, ["callee:00c53da0:8"]]
+ 00483ffc ["INT_ADD", "register:40f0:8", ["const:483ffc:8", "const:4:8"]]
+ 00483ffc ["CALL", null, ["callee:00c53da0:8"]]
- 00483fbc bytes 513f1f94
+ 00483ffc bytes 693f1f94
- 00483fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00483fdc ["INT_ADD", "register:40f0:8", ["const:483fdc:8", "const:4:8"]]
- 00483fdc ["CALLIND", null, ["register:0:8"]]
+ 0048401c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048401c ["INT_ADD", "register:40f0:8", ["const:48401c:8", "const:4:8"]]
+ 0048401c ["CALLIND", null, ["register:0:8"]]
- 00483fdc bytes 00013fd6
+ 0048401c bytes 00013fd6
~~~


<a id="compare-b6da6b19e34877da6be851f862d44c7f"></a>

### [`00483ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md) → [`00484030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484030.md) FUN_00484030

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 9件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 9件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048405c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-0048405c) · [`004840c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-004840c0) · [`004840d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/00483ff0.md#insn-004840d0)
- 新版 `0048409c`（命令位置の公開資料なし） · `00484100`（命令位置の公開資料なし） · `00484110`（命令位置の公開資料なし）

~~~diff
- 0048405c ["INT_ADD", "register:40f0:8", ["const:48405c:8", "const:4:8"]]
- 0048405c ["CALL", null, ["callee:00c580a0:8"]]
+ 0048409c ["INT_ADD", "register:40f0:8", ["const:48409c:8", "const:4:8"]]
+ 0048409c ["CALL", null, ["callee:00c580a0:8"]]
- 0048405c bytes dd4f1f94
+ 0048409c bytes 01501f94
- 004840c0 ["INT_ADD", "register:40f0:8", ["const:4840c0:8", "const:4:8"]]
- 004840c0 ["CALL", null, ["callee:00597efc:8"]]
+ 00484100 ["INT_ADD", "register:40f0:8", ["const:484100:8", "const:4:8"]]
+ 00484100 ["CALL", null, ["callee:00597efc:8"]]
- 004840c0 bytes 7f4f0494
+ 00484100 bytes 7f4f0494
- 004840d0 ["INT_ADD", "register:40f0:8", ["const:4840d0:8", "const:4:8"]]
- 004840d0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00484110 ["INT_ADD", "register:40f0:8", ["const:484110:8", "const:4:8"]]
+ 00484110 ["CALL", null, ["callee:00c57f80:8"]]
- 004840d0 bytes 784f1f94
+ 00484110 bytes 9c4f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b965bfd4c2950dfeebeabbdcb04359e"></a>

### [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) → [`00484250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484250.md) FUN_00484250

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`008813b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md) [`00881584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md)
- 新版 呼出元 3件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00881408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881408.md) [`008815dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008815dc.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484240) · [`00484250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484250) · [`00484260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md#insn-00484260)
- 新版 `00484280`（命令位置の公開資料なし） · `00484290`（命令位置の公開資料なし） · `004842a0`（命令位置の公開資料なし）

~~~diff
- 00484240 ["INT_ADD", "register:40f0:8", ["const:484240:8", "const:4:8"]]
- 00484240 ["CALL", null, ["callee:00550c68:8"]]
+ 00484280 ["INT_ADD", "register:40f0:8", ["const:484280:8", "const:4:8"]]
+ 00484280 ["CALL", null, ["callee:00550c68:8"]]
- 00484240 bytes 7a320394
+ 00484280 bytes 7a320394
- 00484250 ["INT_ADD", "register:40f0:8", ["const:484250:8", "const:4:8"]]
- 00484250 ["CALL", null, ["callee:0043dbe4:8"]]
+ 00484290 ["INT_ADD", "register:40f0:8", ["const:484290:8", "const:4:8"]]
+ 00484290 ["CALL", null, ["callee:0043dbe4:8"]]
- 00484250 bytes 55e6fe97
+ 00484290 bytes 55e6fe97
- 00484260 ["INT_ADD", "register:40f0:8", ["const:484260:8", "const:4:8"]]
- 00484260 ["CALL", null, ["callee:00c57f80:8"]]
+ 004842a0 ["INT_ADD", "register:40f0:8", ["const:4842a0:8", "const:4:8"]]
+ 004842a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00484260 bytes 144f1f94
+ 004842a0 bytes 384f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a19fbd670d5f3b9a224df46d664b46c"></a>

### [`004846dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md) → [`0048471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/0048471c.md) FUN_0048471c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 5件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md) [`00550c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c24.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) · 呼出先 5件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00481fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481fc4.md) [`00550c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c64.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048470c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048470c) · [`0048471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048471c) · [`0048472c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004846dc.md#insn-0048472c)
- 新版 `0048474c`（命令位置の公開資料なし） · `0048475c`（命令位置の公開資料なし） · `0048476c`（命令位置の公開資料なし）

~~~diff
- 0048470c ["INT_ADD", "register:40f0:8", ["const:48470c:8", "const:4:8"]]
- 0048470c ["CALL", null, ["callee:00550c64:8"]]
+ 0048474c ["INT_ADD", "register:40f0:8", ["const:48474c:8", "const:4:8"]]
+ 0048474c ["CALL", null, ["callee:00550c64:8"]]
- 0048470c bytes 46310394
+ 0048474c bytes 46310394
- 0048471c ["INT_ADD", "register:40f0:8", ["const:48471c:8", "const:4:8"]]
- 0048471c ["CALL", null, ["callee:0043dbe4:8"]]
+ 0048475c ["INT_ADD", "register:40f0:8", ["const:48475c:8", "const:4:8"]]
+ 0048475c ["CALL", null, ["callee:0043dbe4:8"]]
- 0048471c bytes 22e5fe97
+ 0048475c bytes 22e5fe97
- 0048472c ["INT_ADD", "register:40f0:8", ["const:48472c:8", "const:4:8"]]
- 0048472c ["CALL", null, ["callee:00c57f80:8"]]
+ 0048476c ["INT_ADD", "register:40f0:8", ["const:48476c:8", "const:4:8"]]
+ 0048476c ["CALL", null, ["callee:00c57f80:8"]]
- 0048472c bytes e14d1f94
+ 0048476c bytes 054e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca09f52aaec1d55b5757c64d6eea459c"></a>

### [`00484dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md) → [`00484e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484e3c.md) FUN_00484e3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a14a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md) · 呼出先 4件 [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00a14ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14ad4.md) · 呼出先 4件 [`00597658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597658.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e34) · [`00484e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e54) · [`00484e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484dfc.md#insn-00484e68)
- 新版 `00484e74`（命令位置の公開資料なし） · `00484e94`（命令位置の公開資料なし） · `00484ea8`（命令位置の公開資料なし）

~~~diff
- 00484e34 ["INT_ADD", "register:40f0:8", ["const:484e34:8", "const:4:8"]]
- 00484e34 ["CALL", null, ["callee:00597658:8"]]
+ 00484e74 ["INT_ADD", "register:40f0:8", ["const:484e74:8", "const:4:8"]]
+ 00484e74 ["CALL", null, ["callee:00597658:8"]]
- 00484e34 bytes f9490494
+ 00484e74 bytes f9490494
- 00484e54 ["INT_ADD", "register:40f0:8", ["const:484e54:8", "const:4:8"]]
- 00484e54 ["CALL", null, ["callee:00c53da0:8"]]
+ 00484e94 ["INT_ADD", "register:40f0:8", ["const:484e94:8", "const:4:8"]]
+ 00484e94 ["CALL", null, ["callee:00c53da0:8"]]
- 00484e54 bytes ab3b1f94
+ 00484e94 bytes c33b1f94
- 00484e68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484e68 ["INT_ADD", "register:40f0:8", ["const:484e68:8", "const:4:8"]]
- 00484e68 ["CALLIND", null, ["register:0:8"]]
+ 00484ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484ea8 ["INT_ADD", "register:40f0:8", ["const:484ea8:8", "const:4:8"]]
+ 00484ea8 ["CALLIND", null, ["register:0:8"]]
- 00484e68 bytes 00013fd6
+ 00484ea8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b3126a8b6276b6ae79465c7b7bed22c"></a>

### [`00484ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md) → [`00484f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484f28.md) FUN_00484f28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f1c) · [`00484f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f38) · [`00484f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484ee8.md#insn-00484f50)
- 新版 `00484f5c`（命令位置の公開資料なし） · `00484f78`（命令位置の公開資料なし） · `00484f90`（命令位置の公開資料なし）

~~~diff
- 00484f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00484f1c ["INT_ADD", "register:40f0:8", ["const:484f1c:8", "const:4:8"]]
- 00484f1c ["CALLIND", null, ["register:0:8"]]
+ 00484f5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484f5c ["INT_ADD", "register:40f0:8", ["const:484f5c:8", "const:4:8"]]
+ 00484f5c ["CALLIND", null, ["register:0:8"]]
- 00484f1c bytes 00013fd6
+ 00484f5c bytes 00013fd6
- 00484f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484f38 ["INT_ADD", "register:40f0:8", ["const:484f38:8", "const:4:8"]]
- 00484f38 ["CALLIND", null, ["register:0:8"]]
+ 00484f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484f78 ["INT_ADD", "register:40f0:8", ["const:484f78:8", "const:4:8"]]
+ 00484f78 ["CALLIND", null, ["register:0:8"]]
- 00484f38 bytes 00013fd6
+ 00484f78 bytes 00013fd6
- 00484f50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484f50 ["INT_ADD", "register:40f0:8", ["const:484f50:8", "const:4:8"]]
- 00484f50 ["CALLIND", null, ["register:0:8"]]
+ 00484f90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00484f90 ["INT_ADD", "register:40f0:8", ["const:484f90:8", "const:4:8"]]
+ 00484f90 ["CALLIND", null, ["register:0:8"]]
- 00484f50 bytes 20013fd6
+ 00484f90 bytes 20013fd6
~~~


<a id="compare-b472803d44db7ee6fa1c9cd4d4b629bd"></a>

### [`00484f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md) → [`00484fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484fb4.md) FUN_00484fb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00484fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fa0) · [`00484fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fc0) · [`00484fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484f74.md#insn-00484fd8)
- 新版 `00484fe0`（命令位置の公開資料なし） · `00485000`（命令位置の公開資料なし） · `00485018`（命令位置の公開資料なし）

~~~diff
- 00484fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00484fa0 ["INT_ADD", "register:40f0:8", ["const:484fa0:8", "const:4:8"]]
- 00484fa0 ["CALLIND", null, ["register:0:8"]]
+ 00484fe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00484fe0 ["INT_ADD", "register:40f0:8", ["const:484fe0:8", "const:4:8"]]
+ 00484fe0 ["CALLIND", null, ["register:0:8"]]
- 00484fa0 bytes 00013fd6
+ 00484fe0 bytes 00013fd6
- 00484fc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484fc0 ["INT_ADD", "register:40f0:8", ["const:484fc0:8", "const:4:8"]]
- 00484fc0 ["CALLIND", null, ["register:0:8"]]
+ 00485000 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00485000 ["INT_ADD", "register:40f0:8", ["const:485000:8", "const:4:8"]]
+ 00485000 ["CALLIND", null, ["register:0:8"]]
- 00484fc0 bytes 20013fd6
+ 00485000 bytes 20013fd6
- 00484fd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00484fd8 ["INT_ADD", "register:40f0:8", ["const:484fd8:8", "const:4:8"]]
- 00484fd8 ["CALLIND", null, ["register:0:8"]]
+ 00485018 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00485018 ["INT_ADD", "register:40f0:8", ["const:485018:8", "const:4:8"]]
+ 00485018 ["CALLIND", null, ["register:0:8"]]
- 00484fd8 bytes 20013fd6
+ 00485018 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddcad487ec7d4a1e97082b21f8193067"></a>

### [`0048507c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md) → [`004850bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004850bc.md) FUN_004850bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 9件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 9件 [`0055e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b0.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004850ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850ac) · [`004850c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850c0) · [`004850d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/0048507c.md#insn-004850d8)
- 新版 `004850ec`（命令位置の公開資料なし） · `00485100`（命令位置の公開資料なし） · `00485118`（命令位置の公開資料なし）

~~~diff
- 004850ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004850ac ["INT_ADD", "register:40f0:8", ["const:4850ac:8", "const:4:8"]]
- 004850ac ["CALLIND", null, ["register:0:8"]]
+ 004850ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004850ec ["INT_ADD", "register:40f0:8", ["const:4850ec:8", "const:4:8"]]
+ 004850ec ["CALLIND", null, ["register:0:8"]]
- 004850ac bytes 00013fd6
+ 004850ec bytes 00013fd6
- 004850c0 ["INT_ADD", "register:40f0:8", ["const:4850c0:8", "const:4:8"]]
- 004850c0 ["CALL", null, ["callee:0055e8b0:8"]]
+ 00485100 ["INT_ADD", "register:40f0:8", ["const:485100:8", "const:4:8"]]
+ 00485100 ["CALL", null, ["callee:0055e8b0:8"]]
- 004850c0 bytes ec650394
+ 00485100 bytes ec650394
- 004850d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004850d8 ["INT_ADD", "register:40f0:8", ["const:4850d8:8", "const:4:8"]]
- 004850d8 ["CALLIND", null, ["register:0:8"]]
+ 00485118 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00485118 ["INT_ADD", "register:40f0:8", ["const:485118:8", "const:4:8"]]
+ 00485118 ["CALLIND", null, ["register:0:8"]]
- 004850d8 bytes 20013fd6
+ 00485118 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cdaa2b0123f74ef41e9fb388e8ec92e"></a>

### [`00485620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md) → [`00485660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/00485660.md) FUN_00485660

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 3件 [`004853b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 3件 [`004853f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004853f0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00485630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-00485630) · [`00485648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-00485648) · [`0048565c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md#insn-0048565c)
- 新版 `00485670`（命令位置の公開資料なし） · `00485688`（命令位置の公開資料なし） · `0048569c`（命令位置の公開資料なし）

~~~diff
- 00485630 ["INT_ADD", "register:40f0:8", ["const:485630:8", "const:4:8"]]
- 00485630 ["CALL", null, ["callee:004853f0:8"]]
+ 00485670 ["INT_ADD", "register:40f0:8", ["const:485670:8", "const:4:8"]]
+ 00485670 ["CALL", null, ["callee:004853f0:8"]]
- 00485630 bytes 60ffff97
+ 00485670 bytes 60ffff97
- 00485648 ["INT_ADD", "register:40f0:8", ["const:485648:8", "const:4:8"]]
- 00485648 ["CALL", null, ["callee:00c53da0:8"]]
+ 00485688 ["INT_ADD", "register:40f0:8", ["const:485688:8", "const:4:8"]]
+ 00485688 ["CALL", null, ["callee:00c53da0:8"]]
- 00485648 bytes ae391f94
+ 00485688 bytes c6391f94
- 0048565c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048565c ["INT_ADD", "register:40f0:8", ["const:48565c:8", "const:4:8"]]
- 0048565c ["CALLIND", null, ["register:0:8"]]
+ 0048569c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048569c ["INT_ADD", "register:40f0:8", ["const:48569c:8", "const:4:8"]]
+ 0048569c ["CALLIND", null, ["register:0:8"]]
- 0048565c bytes 00013fd6
+ 0048569c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea73e99366b625a09b56f7cb66f73080"></a>

### [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md) → [`004856b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004856b8.md) FUN_004856b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`0048388c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/0048388c.md) [`0048e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md) [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`004858ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`004838cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/004838cc.md) [`0048e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 6件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`004858ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004858ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004856dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-004856dc) · [`00485718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-00485718) · [`004857b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md#insn-004857b8)
- 新版 `0048571c`（命令位置の公開資料なし） · `00485758`（命令位置の公開資料なし） · `004857f8`（命令位置の公開資料なし）

~~~diff
- 004856dc ["INT_ADD", "register:40f0:8", ["const:4856dc:8", "const:4:8"]]
- 004856dc ["CALL", null, ["callee:00c57f80:8"]]
+ 0048571c ["INT_ADD", "register:40f0:8", ["const:48571c:8", "const:4:8"]]
+ 0048571c ["CALL", null, ["callee:00c57f80:8"]]
- 004856dc bytes f5491f94
+ 0048571c bytes 194a1f94
- 00485718 ["INT_ADD", "register:40f0:8", ["const:485718:8", "const:4:8"]]
- 00485718 ["CALL", null, ["callee:00c580a0:8"]]
+ 00485758 ["INT_ADD", "register:40f0:8", ["const:485758:8", "const:4:8"]]
+ 00485758 ["CALL", null, ["callee:00c580a0:8"]]
- 00485718 bytes 2e4a1f94
+ 00485758 bytes 524a1f94
- 004857b8 ["INT_ADD", "register:40f0:8", ["const:4857b8:8", "const:4:8"]]
- 004857b8 ["CALL", null, ["callee:004858ec:8"]]
+ 004857f8 ["INT_ADD", "register:40f0:8", ["const:4857f8:8", "const:4:8"]]
+ 004857f8 ["CALL", null, ["callee:004858ec:8"]]
- 004857b8 bytes 3d000094
+ 004857f8 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f00c3f85d196a629a0d6798bdf3e97"></a>

### [`004858ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md) → [`004858ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004858ec.md) FUN_004858ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00485678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485678.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004856b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004856b8.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00485954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485954) · [`00485a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485a10) · [`00485a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004858ac.md#insn-00485a68)
- 新版 `00485994`（命令位置の公開資料なし） · `00485a50`（命令位置の公開資料なし） · `00485aa8`（命令位置の公開資料なし）

~~~diff
- 00485954 ["INT_ADD", "register:40f0:8", ["const:485954:8", "const:4:8"]]
- 00485954 ["CALL", null, ["callee:00c57f60:8"]]
+ 00485994 ["INT_ADD", "register:40f0:8", ["const:485994:8", "const:4:8"]]
+ 00485994 ["CALL", null, ["callee:00c57f60:8"]]
- 00485954 bytes 4f491f94
+ 00485994 bytes 73491f94
- 00485a10 ["INT_ADD", "register:40f0:8", ["const:485a10:8", "const:4:8"]]
- 00485a10 ["CALL", null, ["callee:00c57f60:8"]]
+ 00485a50 ["INT_ADD", "register:40f0:8", ["const:485a50:8", "const:4:8"]]
+ 00485a50 ["CALL", null, ["callee:00c57f60:8"]]
- 00485a10 bytes 20491f94
+ 00485a50 bytes 44491f94
- 00485a68 ["INT_ADD", "register:40f0:8", ["const:485a68:8", "const:4:8"]]
- 00485a68 ["CALL", null, ["callee:00c580d0:8"]]
+ 00485aa8 ["INT_ADD", "register:40f0:8", ["const:485aa8:8", "const:4:8"]]
+ 00485aa8 ["CALL", null, ["callee:00c580d0:8"]]
- 00485a68 bytes 66491f94
+ 00485aa8 bytes 8a491f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de532e021affd9fd4bd51c6217a58031"></a>

### [`00486e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e2c.md) → [`00486e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486e6c.md) FUN_00486e6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e2c.md#insn-00486e54)
- 新版 `00486e94`（命令位置の公開資料なし）

~~~diff
- 00486e54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00486e54 ["INT_ADD", "register:40f0:8", ["const:486e54:8", "const:4:8"]]
- 00486e54 ["CALLIND", null, ["register:0:8"]]
+ 00486e94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00486e94 ["INT_ADD", "register:40f0:8", ["const:486e94:8", "const:4:8"]]
+ 00486e94 ["CALLIND", null, ["register:0:8"]]
- 00486e54 bytes 20013fd6
+ 00486e94 bytes 20013fd6
~~~


<a id="compare-ab8d034355ae5786f2f33c0c8a4060cf"></a>

### [`00486f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md) → [`00486f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486f84.md) FUN_00486f84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md#insn-00486f60) · [`00486f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f44.md#insn-00486f80)
- 新版 `00486fa0`（命令位置の公開資料なし） · `00486fc0`（命令位置の公開資料なし）

~~~diff
- 00486f60 ["INT_ADD", "register:40f0:8", ["const:486f60:8", "const:4:8"]]
- 00486f60 ["CALL", null, ["callee:00c53da0:8"]]
+ 00486fa0 ["INT_ADD", "register:40f0:8", ["const:486fa0:8", "const:4:8"]]
+ 00486fa0 ["CALL", null, ["callee:00c53da0:8"]]
- 00486f60 bytes 68331f94
+ 00486fa0 bytes 80331f94
- 00486f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486f80 ["INT_ADD", "register:40f0:8", ["const:486f80:8", "const:4:8"]]
- 00486f80 ["CALLIND", null, ["register:0:8"]]
+ 00486fc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486fc0 ["INT_ADD", "register:40f0:8", ["const:486fc0:8", "const:4:8"]]
+ 00486fc0 ["CALLIND", null, ["register:0:8"]]
- 00486f80 bytes 00013fd6
+ 00486fc0 bytes 00013fd6
~~~


<a id="compare-ddec250e21324e37d17e46965de7227b"></a>

### [`00486f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md) → [`00486fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486fd4.md) FUN_00486fd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00486fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00486fd4) · [`00486ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00486ff0) · [`00487010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486f94.md#insn-00487010)
- 新版 `00487014`（命令位置の公開資料なし） · `00487030`（命令位置の公開資料なし） · `00487050`（命令位置の公開資料なし）

~~~diff
- 00486fd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00486fd4 ["INT_ADD", "register:40f0:8", ["const:486fd4:8", "const:4:8"]]
- 00486fd4 ["CALLIND", null, ["register:0:8"]]
+ 00487014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487014 ["INT_ADD", "register:40f0:8", ["const:487014:8", "const:4:8"]]
+ 00487014 ["CALLIND", null, ["register:0:8"]]
- 00486fd4 bytes 20013fd6
+ 00487014 bytes 20013fd6
- 00486ff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486ff0 ["INT_ADD", "register:40f0:8", ["const:486ff0:8", "const:4:8"]]
- 00486ff0 ["CALLIND", null, ["register:0:8"]]
+ 00487030 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487030 ["INT_ADD", "register:40f0:8", ["const:487030:8", "const:4:8"]]
+ 00487030 ["CALLIND", null, ["register:0:8"]]
- 00486ff0 bytes 00013fd6
+ 00487030 bytes 00013fd6
- 00487010 ["COPY", "register:0:8", ["register:4048:8"]]
- 00487010 ["INT_ADD", "register:40f0:8", ["const:487010:8", "const:4:8"]]
- 00487010 ["CALLIND", null, ["register:0:8"]]
+ 00487050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487050 ["INT_ADD", "register:40f0:8", ["const:487050:8", "const:4:8"]]
+ 00487050 ["CALLIND", null, ["register:0:8"]]
- 00487010 bytes 20013fd6
+ 00487050 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02b412b706b8dd17012f6d0a84f4994"></a>

### [`004873a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md) → [`004873e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004873e0.md) FUN_004873e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004873d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-004873d8) · [`004873f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-004873f4) · [`00487408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004873a0.md#insn-00487408)
- 新版 `00487418`（命令位置の公開資料なし） · `00487434`（命令位置の公開資料なし） · `00487448`（命令位置の公開資料なし）

~~~diff
- 004873d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004873d8 ["INT_ADD", "register:40f0:8", ["const:4873d8:8", "const:4:8"]]
- 004873d8 ["CALLIND", null, ["register:0:8"]]
+ 00487418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487418 ["INT_ADD", "register:40f0:8", ["const:487418:8", "const:4:8"]]
+ 00487418 ["CALLIND", null, ["register:0:8"]]
- 004873d8 bytes 00013fd6
+ 00487418 bytes 00013fd6
- 004873f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004873f4 ["INT_ADD", "register:40f0:8", ["const:4873f4:8", "const:4:8"]]
- 004873f4 ["CALLIND", null, ["register:0:8"]]
+ 00487434 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487434 ["INT_ADD", "register:40f0:8", ["const:487434:8", "const:4:8"]]
+ 00487434 ["CALLIND", null, ["register:0:8"]]
- 004873f4 bytes 20013fd6
+ 00487434 bytes 20013fd6
- 00487408 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487408 ["INT_ADD", "register:40f0:8", ["const:487408:8", "const:4:8"]]
- 00487408 ["CALLIND", null, ["register:0:8"]]
+ 00487448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487448 ["INT_ADD", "register:40f0:8", ["const:487448:8", "const:4:8"]]
+ 00487448 ["CALLIND", null, ["register:0:8"]]
- 00487408 bytes 00013fd6
+ 00487448 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e6c5b16396d6fe163ab73100a02e34"></a>

### [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) → [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) FUN_0048797c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 132件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md)
- 新版 呼出元 132件 [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487960) · [`00487974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487974) · [`00487998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md#insn-00487998)
- 新版 `004879a0`（命令位置の公開資料なし） · `004879b4`（命令位置の公開資料なし） · `004879d8`（命令位置の公開資料なし）

~~~diff
- 00487960 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487960 ["INT_ADD", "register:40f0:8", ["const:487960:8", "const:4:8"]]
- 00487960 ["CALLIND", null, ["register:0:8"]]
+ 004879a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004879a0 ["INT_ADD", "register:40f0:8", ["const:4879a0:8", "const:4:8"]]
+ 004879a0 ["CALLIND", null, ["register:0:8"]]
- 00487960 bytes 00013fd6
+ 004879a0 bytes 00013fd6
- 00487974 ["INT_ADD", "register:40f0:8", ["const:487974:8", "const:4:8"]]
- 00487974 ["CALL", null, ["callee:00c58660:8"]]
+ 004879b4 ["INT_ADD", "register:40f0:8", ["const:4879b4:8", "const:4:8"]]
+ 004879b4 ["CALL", null, ["callee:00c58660:8"]]
- 00487974 bytes 07431f94
+ 004879b4 bytes 2b431f94
- 00487998 ["INT_ADD", "register:40f0:8", ["const:487998:8", "const:4:8"]]
- 00487998 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004879d8 ["INT_ADD", "register:40f0:8", ["const:4879d8:8", "const:4:8"]]
+ 004879d8 ["CALL", null, ["callee:00c57fb0:8"]]
- 00487998 bytes 52411f94
+ 004879d8 bytes 76411f94
~~~


<a id="compare-75f82c7a630d9b62f924a65c6be57841"></a>

### [`0048799c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md) → [`004879dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004879dc.md) FUN_004879dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006dfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfdc8.md) [`006e29f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e29f0.md) [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md)
- 新版 呼出元 4件 [`006dfe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md) [`006e2a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2a48.md) [`00812f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00812/00812f24.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004879c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879c0) · [`004879d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879d0) · [`004879fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md#insn-004879fc)
- 新版 `00487a00`（命令位置の公開資料なし） · `00487a10`（命令位置の公開資料なし） · `00487a3c`（命令位置の公開資料なし）

~~~diff
- 004879c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004879c0 ["INT_ADD", "register:40f0:8", ["const:4879c0:8", "const:4:8"]]
- 004879c0 ["CALLIND", null, ["register:0:8"]]
+ 00487a00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487a00 ["INT_ADD", "register:40f0:8", ["const:487a00:8", "const:4:8"]]
+ 00487a00 ["CALLIND", null, ["register:0:8"]]
- 004879c0 bytes 00013fd6
+ 00487a00 bytes 00013fd6
- 004879d0 ["INT_ADD", "register:40f0:8", ["const:4879d0:8", "const:4:8"]]
- 004879d0 ["CALL", null, ["callee:00c58680:8"]]
+ 00487a10 ["INT_ADD", "register:40f0:8", ["const:487a10:8", "const:4:8"]]
+ 00487a10 ["CALL", null, ["callee:00c58680:8"]]
- 004879d0 bytes f8421f94
+ 00487a10 bytes 1c431f94
- 004879fc ["INT_ADD", "register:40f0:8", ["const:4879fc:8", "const:4:8"]]
- 004879fc ["CALL", null, ["callee:00c57fb0:8"]]
+ 00487a3c ["INT_ADD", "register:40f0:8", ["const:487a3c:8", "const:4:8"]]
+ 00487a3c ["CALL", null, ["callee:00c57fb0:8"]]
- 004879fc bytes 39411f94
+ 00487a3c bytes 5d411f94
~~~


<a id="compare-bec7efcce73f7cff70e25535ff498300"></a>

### [`00487a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md) → [`00487a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487a40.md) FUN_00487a40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007267c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md)
- 新版 呼出元 1件 [`00726818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/00726818.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a24) · [`00487a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a34) · [`00487a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md#insn-00487a60)
- 新版 `00487a64`（命令位置の公開資料なし） · `00487a74`（命令位置の公開資料なし） · `00487aa0`（命令位置の公開資料なし）

~~~diff
- 00487a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487a24 ["INT_ADD", "register:40f0:8", ["const:487a24:8", "const:4:8"]]
- 00487a24 ["CALLIND", null, ["register:0:8"]]
+ 00487a64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487a64 ["INT_ADD", "register:40f0:8", ["const:487a64:8", "const:4:8"]]
+ 00487a64 ["CALLIND", null, ["register:0:8"]]
- 00487a24 bytes 00013fd6
+ 00487a64 bytes 00013fd6
- 00487a34 ["INT_ADD", "register:40f0:8", ["const:487a34:8", "const:4:8"]]
- 00487a34 ["CALL", null, ["callee:00c58690:8"]]
+ 00487a74 ["INT_ADD", "register:40f0:8", ["const:487a74:8", "const:4:8"]]
+ 00487a74 ["CALL", null, ["callee:00c58690:8"]]
- 00487a34 bytes e3421f94
+ 00487a74 bytes 07431f94
- 00487a60 ["INT_ADD", "register:40f0:8", ["const:487a60:8", "const:4:8"]]
- 00487a60 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00487aa0 ["INT_ADD", "register:40f0:8", ["const:487aa0:8", "const:4:8"]]
+ 00487aa0 ["CALL", null, ["callee:00c57fb0:8"]]
- 00487a60 bytes 20411f94
+ 00487aa0 bytes 44411f94
~~~


<a id="compare-464c5d241c33e9e9be20f34444323267"></a>

### [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) → [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) FUN_00487aa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 63件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) · 呼出先 2件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 63件 [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) [`005c6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md) · 呼出先 2件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487a80) · [`00487ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487ae4) · [`00487b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md#insn-00487b7c)
- 新版 `00487ac0`（命令位置の公開資料なし） · `00487b24`（命令位置の公開資料なし） · `00487bbc`（命令位置の公開資料なし）

~~~diff
- 00487a80 ["COPY", "register:0:8", ["register:4048:8"]]
- 00487a80 ["INT_ADD", "register:40f0:8", ["const:487a80:8", "const:4:8"]]
- 00487a80 ["CALLIND", null, ["register:0:8"]]
+ 00487ac0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00487ac0 ["INT_ADD", "register:40f0:8", ["const:487ac0:8", "const:4:8"]]
+ 00487ac0 ["CALLIND", null, ["register:0:8"]]
- 00487a80 bytes 20013fd6
+ 00487ac0 bytes 20013fd6
- 00487ae4 ["INT_ADD", "register:40f0:8", ["const:487ae4:8", "const:4:8"]]
- 00487ae4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00487b24 ["INT_ADD", "register:40f0:8", ["const:487b24:8", "const:4:8"]]
+ 00487b24 ["CALL", null, ["callee:00c57f60:8"]]
- 00487ae4 bytes eb401f94
+ 00487b24 bytes 0f411f94
- 00487b7c ["INT_ADD", "register:40f0:8", ["const:487b7c:8", "const:4:8"]]
- 00487b7c ["CALL", null, ["callee:0043b7a4:8"]]
+ 00487bbc ["INT_ADD", "register:40f0:8", ["const:487bbc:8", "const:4:8"]]
+ 00487bbc ["CALL", null, ["callee:0043b7a4:8"]]
- 00487b7c bytes facefe97
+ 00487bbc bytes facefe97
~~~


<a id="compare-b79c2b236a874d7de0a6c2fa73dcd6ba"></a>

### [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) → [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md) FUN_00487bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 29件 [`005bb384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bb384.md) [`005bbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bb/005bbf14.md) [`005bc238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc238.md) [`005bc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc518.md) [`005e581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e581c.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md)
- 新版 呼出元 29件 [`005bb3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bb3c4.md) [`005bbf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bb/005bbf54.md) [`005bc278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc278.md) [`005bc558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc558.md) [`005e585c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e5/005e585c.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487bb4) · [`00487bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487bd0) · [`00487c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md#insn-00487c48)
- 新版 `00487bf4`（命令位置の公開資料なし） · `00487c10`（命令位置の公開資料なし） · `00487c88`（命令位置の公開資料なし）

~~~diff
- 00487bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487bb4 ["INT_ADD", "register:40f0:8", ["const:487bb4:8", "const:4:8"]]
- 00487bb4 ["CALLIND", null, ["register:0:8"]]
+ 00487bf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487bf4 ["INT_ADD", "register:40f0:8", ["const:487bf4:8", "const:4:8"]]
+ 00487bf4 ["CALLIND", null, ["register:0:8"]]
- 00487bb4 bytes 00013fd6
+ 00487bf4 bytes 00013fd6
- 00487bd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00487bd0 ["INT_ADD", "register:40f0:8", ["const:487bd0:8", "const:4:8"]]
- 00487bd0 ["CALLIND", null, ["register:0:8"]]
+ 00487c10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487c10 ["INT_ADD", "register:40f0:8", ["const:487c10:8", "const:4:8"]]
+ 00487c10 ["CALLIND", null, ["register:0:8"]]
- 00487bd0 bytes 00013fd6
+ 00487c10 bytes 00013fd6
- 00487c48 ["INT_ADD", "register:40f0:8", ["const:487c48:8", "const:4:8"]]
- 00487c48 ["CALL", null, ["callee:00c57f60:8"]]
+ 00487c88 ["INT_ADD", "register:40f0:8", ["const:487c88:8", "const:4:8"]]
+ 00487c88 ["CALL", null, ["callee:00c57f60:8"]]
- 00487c48 bytes 92401f94
+ 00487c88 bytes b6401f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa2b4e22af6bd63ade4ae71fda2990a"></a>

### [`00487f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md) → [`00487fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487fa8.md) FUN_00487fa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c585d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585d0.md)
- 新版 呼出元 1件 [`00488094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488094.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c586a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00487f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-00487f90) · [`00487fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-00487fb4) · [`0048800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md#insn-0048800c)
- 新版 `00487fd0`（命令位置の公開資料なし） · `00487ff4`（命令位置の公開資料なし） · `0048804c`（命令位置の公開資料なし）

~~~diff
- 00487f90 ["INT_ADD", "register:40f0:8", ["const:487f90:8", "const:4:8"]]
- 00487f90 ["CALL", null, ["callee:00c586a0:8"]]
+ 00487fd0 ["INT_ADD", "register:40f0:8", ["const:487fd0:8", "const:4:8"]]
+ 00487fd0 ["CALL", null, ["callee:00c586a0:8"]]
- 00487f90 bytes 90411f94
+ 00487fd0 bytes b4411f94
- 00487fb4 ["INT_ADD", "register:40f0:8", ["const:487fb4:8", "const:4:8"]]
- 00487fb4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00487ff4 ["INT_ADD", "register:40f0:8", ["const:487ff4:8", "const:4:8"]]
+ 00487ff4 ["CALL", null, ["callee:00c57f80:8"]]
- 00487fb4 bytes bf3f1f94
+ 00487ff4 bytes e33f1f94
- 0048800c ["INT_ADD", "register:40f0:8", ["const:48800c:8", "const:4:8"]]
- 0048800c ["CALL", null, ["callee:00c58370:8"]]
+ 0048804c ["INT_ADD", "register:40f0:8", ["const:48804c:8", "const:4:8"]]
+ 0048804c ["CALL", null, ["callee:00c58370:8"]]
- 0048800c bytes a5401f94
+ 0048804c bytes c9401f94
~~~


<a id="compare-cd191c9bb5ef78fef6ca2d0b4d2a8c47"></a>

### [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md) → [`00488094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488094.md) FUN_00488094

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 4件 [`00487f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487f68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)
- 新版 呼出元 5件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`004887d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004887d0.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) · 呼出先 4件 [`00487fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487fa8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-00488090) · [`0048809c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-0048809c) · [`004880ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md#insn-004880ac)
- 新版 `004880d0`（命令位置の公開資料なし） · `004880dc`（命令位置の公開資料なし） · `004880ec`（命令位置の公開資料なし）

~~~diff
- 00488090 ["COPY", "register:0:8", ["register:4048:8"]]
- 00488090 ["INT_ADD", "register:40f0:8", ["const:488090:8", "const:4:8"]]
- 00488090 ["CALLIND", null, ["register:0:8"]]
+ 004880d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004880d0 ["INT_ADD", "register:40f0:8", ["const:4880d0:8", "const:4:8"]]
+ 004880d0 ["CALLIND", null, ["register:0:8"]]
- 00488090 bytes 20013fd6
+ 004880d0 bytes 20013fd6
- 0048809c ["INT_ADD", "register:40f0:8", ["const:48809c:8", "const:4:8"]]
- 0048809c ["CALL", null, ["callee:00487fa8:8"]]
+ 004880dc ["INT_ADD", "register:40f0:8", ["const:4880dc:8", "const:4:8"]]
+ 004880dc ["CALL", null, ["callee:00487fa8:8"]]
- 0048809c bytes b3ffff97
+ 004880dc bytes b3ffff97
- 004880ac ["INT_ADD", "register:40f0:8", ["const:4880ac:8", "const:4:8"]]
- 004880ac ["CALL", null, ["callee:00c57f80:8"]]
+ 004880ec ["INT_ADD", "register:40f0:8", ["const:4880ec:8", "const:4:8"]]
+ 004880ec ["CALL", null, ["callee:00c57f80:8"]]
- 004880ac bytes 813f1f94
+ 004880ec bytes a53f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5496535b74a791cc81d54850caf7ead"></a>

### [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md) → [`004881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004881b8.md) FUN_004881b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 14件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004881c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-004881c0) · [`0048820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-0048820c) · [`00488268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md#insn-00488268)
- 新版 `00488200`（命令位置の公開資料なし） · `0048824c`（命令位置の公開資料なし） · `004882a8`（命令位置の公開資料なし）

~~~diff
- 004881c0 ["INT_ADD", "register:40f0:8", ["const:4881c0:8", "const:4:8"]]
- 004881c0 ["CALL", null, ["callee:00c580a0:8"]]
+ 00488200 ["INT_ADD", "register:40f0:8", ["const:488200:8", "const:4:8"]]
+ 00488200 ["CALL", null, ["callee:00c580a0:8"]]
- 004881c0 bytes 843f1f94
+ 00488200 bytes a83f1f94
- 0048820c ["INT_ADD", "register:40f0:8", ["const:48820c:8", "const:4:8"]]
- 0048820c ["CALL", null, ["callee:00c580a0:8"]]
+ 0048824c ["INT_ADD", "register:40f0:8", ["const:48824c:8", "const:4:8"]]
+ 0048824c ["CALL", null, ["callee:00c580a0:8"]]
- 0048820c bytes 713f1f94
+ 0048824c bytes 953f1f94
- 00488268 ["INT_ADD", "register:40f0:8", ["const:488268:8", "const:4:8"]]
- 00488268 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004882a8 ["INT_ADD", "register:40f0:8", ["const:4882a8:8", "const:4:8"]]
+ 004882a8 ["CALL", null, ["callee:00c57fb0:8"]]
- 00488268 bytes 1e3f1f94
+ 004882a8 bytes 423f1f94
~~~


<a id="compare-e2ff5dcede79c5eb0344964edb6742be"></a>

### [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) → [`004882ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004882ac.md) FUN_004882ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`005c6300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6300.md) [`0063dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dd10.md) [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) [`0080b824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b824.md) [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) · 呼出先 2件 [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 15件 [`005c6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md) [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`0080b87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080b/0080b87c.md) [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) · 呼出先 2件 [`0048832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/0048832c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004882a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882a4) · [`004882bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882bc) · [`004882e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md#insn-004882e8)
- 新版 `004882e4`（命令位置の公開資料なし） · `004882fc`（命令位置の公開資料なし） · `00488328`（命令位置の公開資料なし）

~~~diff
- 004882a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004882a4 ["INT_ADD", "register:40f0:8", ["const:4882a4:8", "const:4:8"]]
- 004882a4 ["CALLIND", null, ["register:0:8"]]
+ 004882e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004882e4 ["INT_ADD", "register:40f0:8", ["const:4882e4:8", "const:4:8"]]
+ 004882e4 ["CALLIND", null, ["register:0:8"]]
- 004882a4 bytes 00013fd6
+ 004882e4 bytes 00013fd6
- 004882bc ["INT_ADD", "register:40f0:8", ["const:4882bc:8", "const:4:8"]]
- 004882bc ["CALL", null, ["callee:0048832c:8"]]
+ 004882fc ["INT_ADD", "register:40f0:8", ["const:4882fc:8", "const:4:8"]]
+ 004882fc ["CALL", null, ["callee:0048832c:8"]]
- 004882bc bytes 0c000094
+ 004882fc bytes 0c000094
- 004882e8 ["INT_ADD", "register:40f0:8", ["const:4882e8:8", "const:4:8"]]
- 004882e8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00488328 ["INT_ADD", "register:40f0:8", ["const:488328:8", "const:4:8"]]
+ 00488328 ["CALL", null, ["callee:00c57fb0:8"]]
- 004882e8 bytes fe3e1f94
+ 00488328 bytes 223f1f94
~~~


<a id="compare-011056c94dcc514ad9b0c38e044a6ed6"></a>

### [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) → [`0048832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/0048832c.md) FUN_0048832c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00488dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 1件 [`004882ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004882ac.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00488e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488e04.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048833c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-0048833c) · [`004883a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-004883a8) · [`004883d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md#insn-004883d4)
- 新版 `0048837c`（命令位置の公開資料なし） · `004883e8`（命令位置の公開資料なし） · `00488414`（命令位置の公開資料なし）

~~~diff
- 0048833c ["INT_ADD", "register:40f0:8", ["const:48833c:8", "const:4:8"]]
- 0048833c ["CALL", null, ["callee:00c580a0:8"]]
+ 0048837c ["INT_ADD", "register:40f0:8", ["const:48837c:8", "const:4:8"]]
+ 0048837c ["CALL", null, ["callee:00c580a0:8"]]
- 0048833c bytes 253f1f94
+ 0048837c bytes 493f1f94
- 004883a8 ["INT_ADD", "register:40f0:8", ["const:4883a8:8", "const:4:8"]]
- 004883a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004883e8 ["INT_ADD", "register:40f0:8", ["const:4883e8:8", "const:4:8"]]
+ 004883e8 ["CALL", null, ["callee:00c57f60:8"]]
- 004883a8 bytes ba3e1f94
+ 004883e8 bytes de3e1f94
- 004883d4 ["INT_ADD", "register:40f0:8", ["const:4883d4:8", "const:4:8"]]
- 004883d4 ["CALL", null, ["callee:00c580d0:8"]]
+ 00488414 ["INT_ADD", "register:40f0:8", ["const:488414:8", "const:4:8"]]
+ 00488414 ["CALL", null, ["callee:00c580d0:8"]]
- 004883d4 bytes 0b3f1f94
+ 00488414 bytes 2f3f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa6d88f2d124b5f5b9f092de58baecd4"></a>

### [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) → [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) FUN_00488474

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 28件 [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`00662df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662df4.md) [`00668df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00668/00668df0.md) [`00685ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685ae4.md) [`006a3dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a3dc4.md) · 呼出先 2件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 28件 [`005e9534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e9/005e9534.md) [`00662e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/00662e34.md) [`00668e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00668/00668e30.md) [`00685b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/00685b24.md) [`006a3e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3e1c.md) · 呼出先 2件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004884b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md#insn-004884b4) · [`00488554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md#insn-00488554)
- 新版 `004884f4`（命令位置の公開資料なし） · `00488594`（命令位置の公開資料なし）

~~~diff
- 004884b4 ["INT_ADD", "register:40f0:8", ["const:4884b4:8", "const:4:8"]]
- 004884b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004884f4 ["INT_ADD", "register:40f0:8", ["const:4884f4:8", "const:4:8"]]
+ 004884f4 ["CALL", null, ["callee:00c57f60:8"]]
- 004884b4 bytes 773e1f94
+ 004884f4 bytes 9b3e1f94
- 00488554 ["INT_ADD", "register:40f0:8", ["const:488554:8", "const:4:8"]]
- 00488554 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00488594 ["INT_ADD", "register:40f0:8", ["const:488594:8", "const:4:8"]]
+ 00488594 ["CALL", null, ["callee:0043b7a4:8"]]
- 00488554 bytes 84ccfe97
+ 00488594 bytes 84ccfe97
~~~


<a id="compare-8e92bfdc6057268bcac4baf867895623"></a>

### [`004885a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md) → [`004885e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004885e4.md) FUN_004885e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004885cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885cc) · [`004885ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885ec) · [`004885fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004885a4.md#insn-004885fc)
- 新版 `0048860c`（命令位置の公開資料なし） · `0048862c`（命令位置の公開資料なし） · `0048863c`（命令位置の公開資料なし）

~~~diff
- 004885cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004885cc ["INT_ADD", "register:40f0:8", ["const:4885cc:8", "const:4:8"]]
- 004885cc ["CALLIND", null, ["register:0:8"]]
+ 0048860c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048860c ["INT_ADD", "register:40f0:8", ["const:48860c:8", "const:4:8"]]
+ 0048860c ["CALLIND", null, ["register:0:8"]]
- 004885cc bytes 00013fd6
+ 0048860c bytes 00013fd6
- 004885ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004885ec ["INT_ADD", "register:40f0:8", ["const:4885ec:8", "const:4:8"]]
- 004885ec ["CALLIND", null, ["register:0:8"]]
+ 0048862c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048862c ["INT_ADD", "register:40f0:8", ["const:48862c:8", "const:4:8"]]
+ 0048862c ["CALLIND", null, ["register:0:8"]]
- 004885ec bytes 00013fd6
+ 0048862c bytes 00013fd6
- 004885fc ["INT_ADD", "register:40f0:8", ["const:4885fc:8", "const:4:8"]]
- 004885fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0048863c ["INT_ADD", "register:40f0:8", ["const:48863c:8", "const:4:8"]]
+ 0048863c ["CALL", null, ["callee:00c57f80:8"]]
- 004885fc bytes 2d3e1f94
+ 0048863c bytes 513e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be8c7e58b696032ece5bc50101bf9cb"></a>

### [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) → [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) FUN_00488698

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 144件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 1件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)
- 新版 呼出元 144件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) · 呼出先 1件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md#insn-00488678)
- 新版 `004886b8`（命令位置の公開資料なし）

~~~diff
- 00488678 ["INT_ADD", "register:40f0:8", ["const:488678:8", "const:4:8"]]
- 00488678 ["CALL", null, ["callee:00c58370:8"]]
+ 004886b8 ["INT_ADD", "register:40f0:8", ["const:4886b8:8", "const:4:8"]]
+ 004886b8 ["CALL", null, ["callee:00c58370:8"]]
- 00488678 bytes 0a3f1f94
+ 004886b8 bytes 2e3f1f94
~~~


<a id="compare-819c2ccbddcea69f989059486462983d"></a>

### [`004886c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md) → [`00488704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488704.md) FUN_00488704

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00550d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00550d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488704) · [`00488710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488710) · [`00488720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004886c4.md#insn-00488720)
- 新版 `00488744`（命令位置の公開資料なし） · `00488750`（命令位置の公開資料なし） · `00488760`（命令位置の公開資料なし）

~~~diff
- 00488704 ["INT_ADD", "register:40f0:8", ["const:488704:8", "const:4:8"]]
- 00488704 ["CALL", null, ["callee:00c58280:8"]]
+ 00488744 ["INT_ADD", "register:40f0:8", ["const:488744:8", "const:4:8"]]
+ 00488744 ["CALL", null, ["callee:00c58280:8"]]
- 00488704 bytes ab3e1f94
+ 00488744 bytes cf3e1f94
- 00488710 ["INT_ADD", "register:40f0:8", ["const:488710:8", "const:4:8"]]
- 00488710 ["CALL", null, ["callee:00550d78:8"]]
+ 00488750 ["INT_ADD", "register:40f0:8", ["const:488750:8", "const:4:8"]]
+ 00488750 ["CALL", null, ["callee:00550d78:8"]]
- 00488710 bytes 8a210394
+ 00488750 bytes 8a210394
- 00488720 ["INT_ADD", "register:40f0:8", ["const:488720:8", "const:4:8"]]
- 00488720 ["CALL", null, ["callee:00c57f80:8"]]
+ 00488760 ["INT_ADD", "register:40f0:8", ["const:488760:8", "const:4:8"]]
+ 00488760 ["CALL", null, ["callee:00c57f80:8"]]
- 00488720 bytes e43d1f94
+ 00488760 bytes 083e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81de56e45aad5a3cd341e54d49c68699"></a>

### [`00488da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md) → [`00488de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488de0.md) FUN_00488de0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00488cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00488d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488d08.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00488db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md#insn-00488db0)
- 新版 `00488df0`（命令位置の公開資料なし）

~~~diff
- 00488db0 ["INT_ADD", "register:40f0:8", ["const:488db0:8", "const:4:8"]]
- 00488db0 ["CALL", null, ["callee:00488d08:8"]]
+ 00488df0 ["INT_ADD", "register:40f0:8", ["const:488df0:8", "const:4:8"]]
+ 00488df0 ["CALL", null, ["callee:00488d08:8"]]
- 00488db0 bytes c6ffff97
+ 00488df0 bytes c6ffff97
~~~


<a id="compare-5a737678a42f95b36c211fe4a9776350"></a>

### [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) → [`004891d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004891d4.md) FUN_004891d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`00629dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00629/00629dc0.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 2件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md)
- 新版 呼出元 3件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`00629e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00629/00629e00.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 2件 [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004891a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md#insn-004891a4) · [`004891b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md#insn-004891b0)
- 新版 `004891e4`（命令位置の公開資料なし） · `004891f0`（命令位置の公開資料なし）

~~~diff
- 004891a4 ["INT_ADD", "register:40f0:8", ["const:4891a4:8", "const:4:8"]]
- 004891a4 ["CALL", null, ["callee:00489204:8"]]
+ 004891e4 ["INT_ADD", "register:40f0:8", ["const:4891e4:8", "const:4:8"]]
+ 004891e4 ["CALL", null, ["callee:00489204:8"]]
- 004891a4 bytes 08000094
+ 004891e4 bytes 08000094
- 004891b0 ["INT_ADD", "register:40f0:8", ["const:4891b0:8", "const:4:8"]]
- 004891b0 ["CALL", null, ["callee:004894e8:8"]]
+ 004891f0 ["INT_ADD", "register:40f0:8", ["const:4891f0:8", "const:4:8"]]
+ 004891f0 ["CALL", null, ["callee:004894e8:8"]]
- 004891b0 bytes be000094
+ 004891f0 bytes be000094
~~~


<a id="compare-adcf588f745f8bbd8827c6ced8956285"></a>

### [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) → [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) FUN_004894e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md) [`0048ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`0049ad24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md) · 呼出先 6件 [`0055c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md) [`0055e614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e614.md) [`0055e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e61c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 6件 [`004891d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004891d4.md) [`0048a848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a848.md) [`0048ac60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md) [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) [`0049ad64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md) · 呼出先 6件 [`0055c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c3a0.md) [`0055e654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e654.md) [`0055e65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e65c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004894d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-004894d8) · [`004894f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-004894f8) · [`0048950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md#insn-0048950c)
- 新版 `00489518`（命令位置の公開資料なし） · `00489538`（命令位置の公開資料なし） · `0048954c`（命令位置の公開資料なし）

~~~diff
- 004894d8 ["INT_ADD", "register:40f0:8", ["const:4894d8:8", "const:4:8"]]
- 004894d8 ["CALL", null, ["callee:0055c3a0:8"]]
+ 00489518 ["INT_ADD", "register:40f0:8", ["const:489518:8", "const:4:8"]]
+ 00489518 ["CALL", null, ["callee:0055c3a0:8"]]
- 004894d8 bytes a24b0394
+ 00489518 bytes a24b0394
- 004894f8 ["INT_ADD", "register:40f0:8", ["const:4894f8:8", "const:4:8"]]
- 004894f8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00489538 ["INT_ADD", "register:40f0:8", ["const:489538:8", "const:4:8"]]
+ 00489538 ["CALL", null, ["callee:00c53da0:8"]]
- 004894f8 bytes 022a1f94
+ 00489538 bytes 1a2a1f94
- 0048950c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048950c ["INT_ADD", "register:40f0:8", ["const:48950c:8", "const:4:8"]]
- 0048950c ["CALLIND", null, ["register:0:8"]]
+ 0048954c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048954c ["INT_ADD", "register:40f0:8", ["const:48954c:8", "const:4:8"]]
+ 0048954c ["CALLIND", null, ["register:0:8"]]
- 0048950c bytes 00013fd6
+ 0048954c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770cb23cf4a63d7629655362392b47a0"></a>

### [`004895c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md) → [`00489604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489604.md) FUN_00489604

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`00489e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) [`00489edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489edc.md) [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004895f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-004895f0) · [`00489604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-00489604) · [`0048960c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md#insn-0048960c)
- 新版 `00489630`（命令位置の公開資料なし） · `00489644`（命令位置の公開資料なし） · `0048964c`（命令位置の公開資料なし）

~~~diff
- 004895f0 ["INT_ADD", "register:40f0:8", ["const:4895f0:8", "const:4:8"]]
- 004895f0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00489630 ["INT_ADD", "register:40f0:8", ["const:489630:8", "const:4:8"]]
+ 00489630 ["CALL", null, ["callee:00c53da0:8"]]
- 004895f0 bytes c4291f94
+ 00489630 bytes dc291f94
- 00489604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00489604 ["INT_ADD", "register:40f0:8", ["const:489604:8", "const:4:8"]]
- 00489604 ["CALLIND", null, ["register:0:8"]]
+ 00489644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00489644 ["INT_ADD", "register:40f0:8", ["const:489644:8", "const:4:8"]]
+ 00489644 ["CALLIND", null, ["register:0:8"]]
- 00489604 bytes 00013fd6
+ 00489644 bytes 00013fd6
- 0048960c ["INT_ADD", "register:40f0:8", ["const:48960c:8", "const:4:8"]]
- 0048960c ["CALL", null, ["callee:00c57f50:8"]]
+ 0048964c ["INT_ADD", "register:40f0:8", ["const:48964c:8", "const:4:8"]]
+ 0048964c ["CALL", null, ["callee:00c57f50:8"]]
- 0048960c bytes 1d3a1f94
+ 0048964c bytes 413a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7195f055bcc8125dff30999d638ed22d"></a>

### [`00489e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md) → [`00489e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489e8c.md) FUN_00489e8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md#insn-00489e68) · [`00489e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e4c.md#insn-00489e88)
- 新版 `00489ea8`（命令位置の公開資料なし） · `00489ec8`（命令位置の公開資料なし）

~~~diff
- 00489e68 ["INT_ADD", "register:40f0:8", ["const:489e68:8", "const:4:8"]]
- 00489e68 ["CALL", null, ["callee:00c53da0:8"]]
+ 00489ea8 ["INT_ADD", "register:40f0:8", ["const:489ea8:8", "const:4:8"]]
+ 00489ea8 ["CALL", null, ["callee:00c53da0:8"]]
- 00489e68 bytes a6271f94
+ 00489ea8 bytes be271f94
- 00489e88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00489e88 ["INT_ADD", "register:40f0:8", ["const:489e88:8", "const:4:8"]]
- 00489e88 ["CALLIND", null, ["register:0:8"]]
+ 00489ec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00489ec8 ["INT_ADD", "register:40f0:8", ["const:489ec8:8", "const:4:8"]]
+ 00489ec8 ["CALLIND", null, ["register:0:8"]]
- 00489e88 bytes 00013fd6
+ 00489ec8 bytes 00013fd6
~~~


<a id="compare-e423ecb7d175edaa72b27d19eac704d3"></a>

### [`00489e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md) → [`00489edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489edc.md) FUN_00489edc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 7件 [`004895c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004895c4.md) [`0055e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e60c.md) [`0055e614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e614.md) [`0055e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e61c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`00a99514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a99/00a99514.md) · 呼出先 7件 [`00489604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489604.md) [`0055e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e64c.md) [`0055e654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e654.md) [`0055e65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e65c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00489eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489eb8) · [`00489ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489ecc) · [`00489ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489e9c.md#insn-00489ee4)
- 新版 `00489ef8`（命令位置の公開資料なし） · `00489f0c`（命令位置の公開資料なし） · `00489f24`（命令位置の公開資料なし）

~~~diff
- 00489eb8 ["INT_ADD", "register:40f0:8", ["const:489eb8:8", "const:4:8"]]
- 00489eb8 ["CALL", null, ["callee:00489604:8"]]
+ 00489ef8 ["INT_ADD", "register:40f0:8", ["const:489ef8:8", "const:4:8"]]
+ 00489ef8 ["CALL", null, ["callee:00489604:8"]]
- 00489eb8 bytes c3fdff97
+ 00489ef8 bytes c3fdff97
- 00489ecc ["INT_ADD", "register:40f0:8", ["const:489ecc:8", "const:4:8"]]
- 00489ecc ["CALL", null, ["callee:00c53d70:8"]]
+ 00489f0c ["INT_ADD", "register:40f0:8", ["const:489f0c:8", "const:4:8"]]
+ 00489f0c ["CALL", null, ["callee:00c53d70:8"]]
- 00489ecc bytes 81271f94
+ 00489f0c bytes 99271f94
- 00489ee4 ["INT_ADD", "register:40f0:8", ["const:489ee4:8", "const:4:8"]]
- 00489ee4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00489f24 ["INT_ADD", "register:40f0:8", ["const:489f24:8", "const:4:8"]]
+ 00489f24 ["CALL", null, ["callee:00c53da0:8"]]
- 00489ee4 bytes 87271f94
+ 00489f24 bytes 9f271f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5ec314e96a4a708225cb98b886a7a76"></a>

### [`0048a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md) → [`0048a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a6d0.md) FUN_0048a6d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6bc) · [`0048a6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6d0) · [`0048a6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md#insn-0048a6d8)
- 新版 `0048a6fc`（命令位置の公開資料なし） · `0048a710`（命令位置の公開資料なし） · `0048a718`（命令位置の公開資料なし）

~~~diff
- 0048a6bc ["INT_ADD", "register:40f0:8", ["const:48a6bc:8", "const:4:8"]]
- 0048a6bc ["CALL", null, ["callee:00c53da0:8"]]
+ 0048a6fc ["INT_ADD", "register:40f0:8", ["const:48a6fc:8", "const:4:8"]]
+ 0048a6fc ["CALL", null, ["callee:00c53da0:8"]]
- 0048a6bc bytes 91251f94
+ 0048a6fc bytes a9251f94
- 0048a6d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048a6d0 ["INT_ADD", "register:40f0:8", ["const:48a6d0:8", "const:4:8"]]
- 0048a6d0 ["CALLIND", null, ["register:0:8"]]
+ 0048a710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048a710 ["INT_ADD", "register:40f0:8", ["const:48a710:8", "const:4:8"]]
+ 0048a710 ["CALLIND", null, ["register:0:8"]]
- 0048a6d0 bytes 00013fd6
+ 0048a710 bytes 00013fd6
- 0048a6d8 ["INT_ADD", "register:40f0:8", ["const:48a6d8:8", "const:4:8"]]
- 0048a6d8 ["CALL", null, ["callee:00c57f50:8"]]
+ 0048a718 ["INT_ADD", "register:40f0:8", ["const:48a718:8", "const:4:8"]]
+ 0048a718 ["CALL", null, ["callee:00c57f50:8"]]
- 0048a6d8 bytes ea351f94
+ 0048a718 bytes 0e361f94
~~~


<a id="compare-731b1bbd1588ed28e48b98f4c0412190"></a>

### [`0048a6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md) → [`0048a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a72c.md) FUN_0048a72c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) [`00590d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590d18.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) [`00590d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590d58.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md#insn-0048a708) · [`0048a728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md#insn-0048a728)
- 新版 `0048a748`（命令位置の公開資料なし） · `0048a768`（命令位置の公開資料なし）

~~~diff
- 0048a708 ["INT_ADD", "register:40f0:8", ["const:48a708:8", "const:4:8"]]
- 0048a708 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048a748 ["INT_ADD", "register:40f0:8", ["const:48a748:8", "const:4:8"]]
+ 0048a748 ["CALL", null, ["callee:00c53da0:8"]]
- 0048a708 bytes 7e251f94
+ 0048a748 bytes 96251f94
- 0048a728 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048a728 ["INT_ADD", "register:40f0:8", ["const:48a728:8", "const:4:8"]]
- 0048a728 ["CALLIND", null, ["register:0:8"]]
+ 0048a768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048a768 ["INT_ADD", "register:40f0:8", ["const:48a768:8", "const:4:8"]]
+ 0048a768 ["CALLIND", null, ["register:0:8"]]
- 0048a728 bytes 00013fd6
+ 0048a768 bytes 00013fd6
~~~


<a id="compare-36202d2050aa27b4abf794abf25d1b7f"></a>

### [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md) → [`0048a848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a848.md) FUN_0048a848

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 2件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`0048a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a834.md)
- 新版 呼出元 2件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 2件 [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) [`0048a874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a874.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md#insn-0048a818) · [`0048a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md#insn-0048a820)
- 新版 `0048a858`（命令位置の公開資料なし） · `0048a860`（命令位置の公開資料なし）

~~~diff
- 0048a818 ["INT_ADD", "register:40f0:8", ["const:48a818:8", "const:4:8"]]
- 0048a818 ["CALL", null, ["callee:0048a874:8"]]
+ 0048a858 ["INT_ADD", "register:40f0:8", ["const:48a858:8", "const:4:8"]]
+ 0048a858 ["CALL", null, ["callee:0048a874:8"]]
- 0048a818 bytes 07000094
+ 0048a858 bytes 07000094
- 0048a820 ["INT_ADD", "register:40f0:8", ["const:48a820:8", "const:4:8"]]
- 0048a820 ["CALL", null, ["callee:004894e8:8"]]
+ 0048a860 ["INT_ADD", "register:40f0:8", ["const:48a860:8", "const:4:8"]]
+ 0048a860 ["CALL", null, ["callee:004894e8:8"]]
- 0048a820 bytes 22fbff97
+ 0048a860 bytes 22fbff97
~~~


<a id="compare-5d6291e81c7aef455350c2a2dde178f0"></a>

### [`0048aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md) → [`0048aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048aa90.md) FUN_0048aa90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md) [`0086b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0048ac60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md) [`0086b22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aa98) · [`0048aab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aab8) · [`0048aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md#insn-0048aacc)
- 新版 `0048aad8`（命令位置の公開資料なし） · `0048aaf8`（命令位置の公開資料なし） · `0048ab0c`（命令位置の公開資料なし）

~~~diff
- 0048aa98 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048aa98 ["INT_ADD", "register:40f0:8", ["const:48aa98:8", "const:4:8"]]
- 0048aa98 ["CALLIND", null, ["register:0:8"]]
+ 0048aad8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0048aad8 ["INT_ADD", "register:40f0:8", ["const:48aad8:8", "const:4:8"]]
+ 0048aad8 ["CALLIND", null, ["register:0:8"]]
- 0048aa98 bytes 20013fd6
+ 0048aad8 bytes 20013fd6
- 0048aab8 ["INT_ADD", "register:40f0:8", ["const:48aab8:8", "const:4:8"]]
- 0048aab8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048aaf8 ["INT_ADD", "register:40f0:8", ["const:48aaf8:8", "const:4:8"]]
+ 0048aaf8 ["CALL", null, ["callee:00c53da0:8"]]
- 0048aab8 bytes 92241f94
+ 0048aaf8 bytes aa241f94
- 0048aacc ["COPY", "register:0:8", ["register:4040:8"]]
- 0048aacc ["INT_ADD", "register:40f0:8", ["const:48aacc:8", "const:4:8"]]
- 0048aacc ["CALLIND", null, ["register:0:8"]]
+ 0048ab0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048ab0c ["INT_ADD", "register:40f0:8", ["const:48ab0c:8", "const:4:8"]]
+ 0048ab0c ["CALLIND", null, ["register:0:8"]]
- 0048aacc bytes 00013fd6
+ 0048ab0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9f2f69b43fb6a3edfc17a0f8740944c"></a>

### [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) → [`0048acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048acd0.md) FUN_0048acd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) · 呼出先 6件 [`0046c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1f8.md) [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae34) · [`0048ae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae40) · [`0048ae54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md#insn-0048ae54)
- 新版 `0048ae74`（命令位置の公開資料なし） · `0048ae80`（命令位置の公開資料なし） · `0048ae94`（命令位置の公開資料なし）

~~~diff
- 0048ae34 ["INT_ADD", "register:40f0:8", ["const:48ae34:8", "const:4:8"]]
- 0048ae34 ["CALL", null, ["callee:00c53d70:8"]]
+ 0048ae74 ["INT_ADD", "register:40f0:8", ["const:48ae74:8", "const:4:8"]]
+ 0048ae74 ["CALL", null, ["callee:00c53d70:8"]]
- 0048ae34 bytes a7231f94
+ 0048ae74 bytes bf231f94
- 0048ae40 ["INT_ADD", "register:40f0:8", ["const:48ae40:8", "const:4:8"]]
- 0048ae40 ["CALL", null, ["callee:0046c1f8:8"]]
+ 0048ae80 ["INT_ADD", "register:40f0:8", ["const:48ae80:8", "const:4:8"]]
+ 0048ae80 ["CALL", null, ["callee:0046c1f8:8"]]
- 0048ae40 bytes de84ff97
+ 0048ae80 bytes de84ff97
- 0048ae54 ["INT_ADD", "register:40f0:8", ["const:48ae54:8", "const:4:8"]]
- 0048ae54 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048ae94 ["INT_ADD", "register:40f0:8", ["const:48ae94:8", "const:4:8"]]
+ 0048ae94 ["CALL", null, ["callee:00c53da0:8"]]
- 0048ae54 bytes ab231f94
+ 0048ae94 bytes c3231f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9138ce175a344b1e2c63455ee327f1"></a>

### [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) → [`0048af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048af18.md) FUN_0048af18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) · 呼出先 6件 [`0046c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1f8.md) [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b038) · [`0048b044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b044) · [`0048b058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md#insn-0048b058)
- 新版 `0048b078`（命令位置の公開資料なし） · `0048b084`（命令位置の公開資料なし） · `0048b098`（命令位置の公開資料なし）

~~~diff
- 0048b038 ["INT_ADD", "register:40f0:8", ["const:48b038:8", "const:4:8"]]
- 0048b038 ["CALL", null, ["callee:00c53d70:8"]]
+ 0048b078 ["INT_ADD", "register:40f0:8", ["const:48b078:8", "const:4:8"]]
+ 0048b078 ["CALL", null, ["callee:00c53d70:8"]]
- 0048b038 bytes 26231f94
+ 0048b078 bytes 3e231f94
- 0048b044 ["INT_ADD", "register:40f0:8", ["const:48b044:8", "const:4:8"]]
- 0048b044 ["CALL", null, ["callee:0046c1f8:8"]]
+ 0048b084 ["INT_ADD", "register:40f0:8", ["const:48b084:8", "const:4:8"]]
+ 0048b084 ["CALL", null, ["callee:0046c1f8:8"]]
- 0048b044 bytes 5d84ff97
+ 0048b084 bytes 5d84ff97
- 0048b058 ["INT_ADD", "register:40f0:8", ["const:48b058:8", "const:4:8"]]
- 0048b058 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048b098 ["INT_ADD", "register:40f0:8", ["const:48b098:8", "const:4:8"]]
+ 0048b098 ["CALL", null, ["callee:00c53da0:8"]]
- 0048b058 bytes 2a231f94
+ 0048b098 bytes 42231f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c31022380d243f16ae1d6212ae632139"></a>

### [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) → [`0048b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b11c.md) FUN_0048b11c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0046aa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046aa3c.md) [`0046ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ace0.md) · 呼出先 6件 [`0046c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1f8.md) [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1ac) · [`0048b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1b8) · [`0048b1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md#insn-0048b1cc)
- 新版 `0048b1ec`（命令位置の公開資料なし） · `0048b1f8`（命令位置の公開資料なし） · `0048b20c`（命令位置の公開資料なし）

~~~diff
- 0048b1ac ["INT_ADD", "register:40f0:8", ["const:48b1ac:8", "const:4:8"]]
- 0048b1ac ["CALL", null, ["callee:00c53d70:8"]]
+ 0048b1ec ["INT_ADD", "register:40f0:8", ["const:48b1ec:8", "const:4:8"]]
+ 0048b1ec ["CALL", null, ["callee:00c53d70:8"]]
- 0048b1ac bytes c9221f94
+ 0048b1ec bytes e1221f94
- 0048b1b8 ["INT_ADD", "register:40f0:8", ["const:48b1b8:8", "const:4:8"]]
- 0048b1b8 ["CALL", null, ["callee:0046c1f8:8"]]
+ 0048b1f8 ["INT_ADD", "register:40f0:8", ["const:48b1f8:8", "const:4:8"]]
+ 0048b1f8 ["CALL", null, ["callee:0046c1f8:8"]]
- 0048b1b8 bytes 0084ff97
+ 0048b1f8 bytes 0084ff97
- 0048b1cc ["INT_ADD", "register:40f0:8", ["const:48b1cc:8", "const:4:8"]]
- 0048b1cc ["CALL", null, ["callee:00c53da0:8"]]
+ 0048b20c ["INT_ADD", "register:40f0:8", ["const:48b20c:8", "const:4:8"]]
+ 0048b20c ["CALL", null, ["callee:00c53da0:8"]]
- 0048b1cc bytes cd221f94
+ 0048b20c bytes e5221f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad055826c6a7151a252e348661bc3bdb"></a>

### [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) → [`0048b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b290.md) FUN_0048b290

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) · 呼出先 6件 [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0046ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ab88.md) · 呼出先 6件 [`0046c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1f8.md) [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b2ec) · [`0048b2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b2f8) · [`0048b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md#insn-0048b30c)
- 新版 `0048b32c`（命令位置の公開資料なし） · `0048b338`（命令位置の公開資料なし） · `0048b34c`（命令位置の公開資料なし）

~~~diff
- 0048b2ec ["INT_ADD", "register:40f0:8", ["const:48b2ec:8", "const:4:8"]]
- 0048b2ec ["CALL", null, ["callee:00c53d70:8"]]
+ 0048b32c ["INT_ADD", "register:40f0:8", ["const:48b32c:8", "const:4:8"]]
+ 0048b32c ["CALL", null, ["callee:00c53d70:8"]]
- 0048b2ec bytes 79221f94
+ 0048b32c bytes 91221f94
- 0048b2f8 ["INT_ADD", "register:40f0:8", ["const:48b2f8:8", "const:4:8"]]
- 0048b2f8 ["CALL", null, ["callee:0046c1f8:8"]]
+ 0048b338 ["INT_ADD", "register:40f0:8", ["const:48b338:8", "const:4:8"]]
+ 0048b338 ["CALL", null, ["callee:0046c1f8:8"]]
- 0048b2f8 bytes b083ff97
+ 0048b338 bytes b083ff97
- 0048b30c ["INT_ADD", "register:40f0:8", ["const:48b30c:8", "const:4:8"]]
- 0048b30c ["CALL", null, ["callee:00c53da0:8"]]
+ 0048b34c ["INT_ADD", "register:40f0:8", ["const:48b34c:8", "const:4:8"]]
+ 0048b34c ["CALL", null, ["callee:00c53da0:8"]]
- 0048b30c bytes 7d221f94
+ 0048b34c bytes 95221f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2726b7a5323ec2108db46d7b478f5c24"></a>

### [`0048b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md) → [`0048b410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b410.md) FUN_0048b410

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daec.md) [`0048b544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046db2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db2c.md) [`0048b584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b448) · [`0048b468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b468) · [`0048b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md#insn-0048b4a0)
- 新版 `0048b488`（命令位置の公開資料なし） · `0048b4a8`（命令位置の公開資料なし） · `0048b4e0`（命令位置の公開資料なし）

~~~diff
- 0048b448 ["INT_ADD", "register:40f0:8", ["const:48b448:8", "const:4:8"]]
- 0048b448 ["CALL", null, ["callee:00c57f60:8"]]
+ 0048b488 ["INT_ADD", "register:40f0:8", ["const:48b488:8", "const:4:8"]]
+ 0048b488 ["CALL", null, ["callee:00c57f60:8"]]
- 0048b448 bytes 92321f94
+ 0048b488 bytes b6321f94
- 0048b468 ["INT_ADD", "register:40f0:8", ["const:48b468:8", "const:4:8"]]
- 0048b468 ["CALL", null, ["callee:0046db2c:8"]]
+ 0048b4a8 ["INT_ADD", "register:40f0:8", ["const:48b4a8:8", "const:4:8"]]
+ 0048b4a8 ["CALL", null, ["callee:0046db2c:8"]]
- 0048b468 bytes a189ff97
+ 0048b4a8 bytes a189ff97
- 0048b4a0 ["INT_ADD", "register:40f0:8", ["const:48b4a0:8", "const:4:8"]]
- 0048b4a0 ["CALL", null, ["callee:0046db2c:8"]]
+ 0048b4e0 ["INT_ADD", "register:40f0:8", ["const:48b4e0:8", "const:4:8"]]
+ 0048b4e0 ["CALL", null, ["callee:0046db2c:8"]]
- 0048b4a0 bytes 9389ff97
+ 0048b4e0 bytes 9389ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d99328192c9ab100c395e604bd8ca46d"></a>

### [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) → [`0048b598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b598.md) FUN_0048b598

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00489f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f68.md) [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) · 呼出先 4件 [`0048b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00489fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fa8.md) [`0048b598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b598.md) · 呼出先 4件 [`0048b598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b598.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b574) · [`0048b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b580) · [`0048b594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b558.md#insn-0048b594)
- 新版 `0048b5b4`（命令位置の公開資料なし） · `0048b5c0`（命令位置の公開資料なし） · `0048b5d4`（命令位置の公開資料なし）

~~~diff
- 0048b574 ["INT_ADD", "register:40f0:8", ["const:48b574:8", "const:4:8"]]
- 0048b574 ["CALL", null, ["local:b0:8"]]
+ 0048b5b4 ["INT_ADD", "register:40f0:8", ["const:48b5b4:8", "const:4:8"]]
+ 0048b5b4 ["CALL", null, ["local:b0:8"]]
- 0048b574 bytes f9ffff97
+ 0048b5b4 bytes f9ffff97
- 0048b580 ["INT_ADD", "register:40f0:8", ["const:48b580:8", "const:4:8"]]
- 0048b580 ["CALL", null, ["local:b0:8"]]
+ 0048b5c0 ["INT_ADD", "register:40f0:8", ["const:48b5c0:8", "const:4:8"]]
+ 0048b5c0 ["CALL", null, ["local:b0:8"]]
- 0048b580 bytes f6ffff97
+ 0048b5c0 bytes f6ffff97
- 0048b594 ["INT_ADD", "register:40f0:8", ["const:48b594:8", "const:4:8"]]
- 0048b594 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048b5d4 ["INT_ADD", "register:40f0:8", ["const:48b5d4:8", "const:4:8"]]
+ 0048b5d4 ["CALL", null, ["callee:00c53da0:8"]]
- 0048b594 bytes db211f94
+ 0048b5d4 bytes f3211f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d93ce6a3ee7f8b65e0311ad5c8bf4116"></a>

### [`0048b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md) → [`0048b624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b624.md) FUN_0048b624

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 2件 [`0048b6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) · 呼出先 2件 [`0048b71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b71c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b60c) · [`0048b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b664) · [`0048b6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md#insn-0048b6ac)
- 新版 `0048b64c`（命令位置の公開資料なし） · `0048b6a4`（命令位置の公開資料なし） · `0048b6ec`（命令位置の公開資料なし）

~~~diff
- 0048b60c ["INT_ADD", "register:40f0:8", ["const:48b60c:8", "const:4:8"]]
- 0048b60c ["CALL", null, ["callee:0048b71c:8"]]
+ 0048b64c ["INT_ADD", "register:40f0:8", ["const:48b64c:8", "const:4:8"]]
+ 0048b64c ["CALL", null, ["callee:0048b71c:8"]]
- 0048b60c bytes 34000094
+ 0048b64c bytes 34000094
- 0048b664 ["INT_ADD", "register:40f0:8", ["const:48b664:8", "const:4:8"]]
- 0048b664 ["CALL", null, ["callee:00c58120:8"]]
+ 0048b6a4 ["INT_ADD", "register:40f0:8", ["const:48b6a4:8", "const:4:8"]]
+ 0048b6a4 ["CALL", null, ["callee:00c58120:8"]]
- 0048b664 bytes 7b321f94
+ 0048b6a4 bytes 9f321f94
- 0048b6ac ["INT_ADD", "register:40f0:8", ["const:48b6ac:8", "const:4:8"]]
- 0048b6ac ["CALL", null, ["callee:00c58120:8"]]
+ 0048b6ec ["INT_ADD", "register:40f0:8", ["const:48b6ec:8", "const:4:8"]]
+ 0048b6ec ["CALL", null, ["callee:00c58120:8"]]
- 0048b6ac bytes 69321f94
+ 0048b6ec bytes 8d321f94
~~~


<a id="compare-277440863e6d931f70417d1921375f45"></a>

### [`0048b6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md) → [`0048b71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b71c.md) FUN_0048b71c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0048b624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b624.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md#insn-0048b764) · [`0048b790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b6dc.md#insn-0048b790)
- 新版 `0048b7a4`（命令位置の公開資料なし） · `0048b7d0`（命令位置の公開資料なし）

~~~diff
- 0048b764 ["INT_ADD", "register:40f0:8", ["const:48b764:8", "const:4:8"]]
- 0048b764 ["CALL", null, ["callee:00c58120:8"]]
+ 0048b7a4 ["INT_ADD", "register:40f0:8", ["const:48b7a4:8", "const:4:8"]]
+ 0048b7a4 ["CALL", null, ["callee:00c58120:8"]]
- 0048b764 bytes 3b321f94
+ 0048b7a4 bytes 5f321f94
- 0048b790 ["INT_ADD", "register:40f0:8", ["const:48b790:8", "const:4:8"]]
- 0048b790 ["CALL", null, ["callee:00c58120:8"]]
+ 0048b7d0 ["INT_ADD", "register:40f0:8", ["const:48b7d0:8", "const:4:8"]]
+ 0048b7d0 ["CALL", null, ["callee:00c58120:8"]]
- 0048b790 bytes 30321f94
+ 0048b7d0 bytes 54321f94
~~~


<a id="compare-a732cc9280dd235487f0effb492c8ae5"></a>

### [`0048b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md) → [`0048b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b838.md) FUN_0048b838

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048b96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b96c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b82c) · [`0048b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b84c) · [`0048b888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md#insn-0048b888)
- 新版 `0048b86c`（命令位置の公開資料なし） · `0048b88c`（命令位置の公開資料なし） · `0048b8c8`（命令位置の公開資料なし）

~~~diff
- 0048b82c ["INT_ADD", "register:40f0:8", ["const:48b82c:8", "const:4:8"]]
- 0048b82c ["CALL", null, ["callee:0048b96c:8"]]
+ 0048b86c ["INT_ADD", "register:40f0:8", ["const:48b86c:8", "const:4:8"]]
+ 0048b86c ["CALL", null, ["callee:0048b96c:8"]]
- 0048b82c bytes 40000094
+ 0048b86c bytes 40000094
- 0048b84c ["INT_ADD", "register:40f0:8", ["const:48b84c:8", "const:4:8"]]
- 0048b84c ["CALL", null, ["callee:00c57f60:8"]]
+ 0048b88c ["INT_ADD", "register:40f0:8", ["const:48b88c:8", "const:4:8"]]
+ 0048b88c ["CALL", null, ["callee:00c57f60:8"]]
- 0048b84c bytes 91311f94
+ 0048b88c bytes b5311f94
- 0048b888 ["INT_ADD", "register:40f0:8", ["const:48b888:8", "const:4:8"]]
- 0048b888 ["CALL", null, ["callee:0043bb60:8"]]
+ 0048b8c8 ["INT_ADD", "register:40f0:8", ["const:48b8c8:8", "const:4:8"]]
+ 0048b8c8 ["CALL", null, ["callee:0043bb60:8"]]
- 0048b888 bytes a6c0fe97
+ 0048b8c8 bytes a6c0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f8a8ca3841492a46a8a24e0a8e2cd6"></a>

### [`0048b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md) → [`0048b96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b96c.md) FUN_0048b96c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`0048b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b838.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048b9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048b9b8) · [`0048b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048b9e0) · [`0048ba1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b92c.md#insn-0048ba1c)
- 新版 `0048b9f8`（命令位置の公開資料なし） · `0048ba20`（命令位置の公開資料なし） · `0048ba5c`（命令位置の公開資料なし）

~~~diff
- 0048b9b8 ["INT_ADD", "register:40f0:8", ["const:48b9b8:8", "const:4:8"]]
- 0048b9b8 ["CALL", null, ["callee:00c58120:8"]]
+ 0048b9f8 ["INT_ADD", "register:40f0:8", ["const:48b9f8:8", "const:4:8"]]
+ 0048b9f8 ["CALL", null, ["callee:00c58120:8"]]
- 0048b9b8 bytes a6311f94
+ 0048b9f8 bytes ca311f94
- 0048b9e0 ["INT_ADD", "register:40f0:8", ["const:48b9e0:8", "const:4:8"]]
- 0048b9e0 ["CALL", null, ["callee:00c58120:8"]]
+ 0048ba20 ["INT_ADD", "register:40f0:8", ["const:48ba20:8", "const:4:8"]]
+ 0048ba20 ["CALL", null, ["callee:00c58120:8"]]
- 0048b9e0 bytes 9c311f94
+ 0048ba20 bytes c0311f94
- 0048ba1c ["INT_ADD", "register:40f0:8", ["const:48ba1c:8", "const:4:8"]]
- 0048ba1c ["CALL", null, ["callee:00c58120:8"]]
+ 0048ba5c ["INT_ADD", "register:40f0:8", ["const:48ba5c:8", "const:4:8"]]
+ 0048ba5c ["CALL", null, ["callee:00c58120:8"]]
- 0048ba1c bytes 8d311f94
+ 0048ba5c bytes b1311f94
~~~


<a id="compare-bc5da73df306258f5b738c0fb21c839b"></a>

### [`0048ba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md) → [`0048bab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048bab4.md) FUN_0048bab4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048baa4) · [`0048bab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048bab8) · [`0048bac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048ba74.md#insn-0048bac0)
- 新版 `0048bae4`（命令位置の公開資料なし） · `0048baf8`（命令位置の公開資料なし） · `0048bb00`（命令位置の公開資料なし）

~~~diff
- 0048baa4 ["INT_ADD", "register:40f0:8", ["const:48baa4:8", "const:4:8"]]
- 0048baa4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048bae4 ["INT_ADD", "register:40f0:8", ["const:48bae4:8", "const:4:8"]]
+ 0048bae4 ["CALL", null, ["callee:00c53da0:8"]]
- 0048baa4 bytes 97201f94
+ 0048bae4 bytes af201f94
- 0048bab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048bab8 ["INT_ADD", "register:40f0:8", ["const:48bab8:8", "const:4:8"]]
- 0048bab8 ["CALLIND", null, ["register:0:8"]]
+ 0048baf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048baf8 ["INT_ADD", "register:40f0:8", ["const:48baf8:8", "const:4:8"]]
+ 0048baf8 ["CALLIND", null, ["register:0:8"]]
- 0048bab8 bytes 00013fd6
+ 0048baf8 bytes 00013fd6
- 0048bac0 ["INT_ADD", "register:40f0:8", ["const:48bac0:8", "const:4:8"]]
- 0048bac0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0048bb00 ["INT_ADD", "register:40f0:8", ["const:48bb00:8", "const:4:8"]]
+ 0048bb00 ["CALL", null, ["callee:00c57f50:8"]]
- 0048bac0 bytes f0301f94
+ 0048bb00 bytes 14311f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64c1dd348e3ab573c6567fdc459b5792"></a>

### [`0048cd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md) → [`0048cdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cdb4.md) FUN_0048cdb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dcb8.md) [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e4f0.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048dcf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dcf8.md) [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e530.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048cd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cd94) · [`0048cda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cda8) · [`0048cdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md#insn-0048cdb0)
- 新版 `0048cdd4`（命令位置の公開資料なし） · `0048cde8`（命令位置の公開資料なし） · `0048cdf0`（命令位置の公開資料なし）

~~~diff
- 0048cd94 ["INT_ADD", "register:40f0:8", ["const:48cd94:8", "const:4:8"]]
- 0048cd94 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048cdd4 ["INT_ADD", "register:40f0:8", ["const:48cdd4:8", "const:4:8"]]
+ 0048cdd4 ["CALL", null, ["callee:00c53da0:8"]]
- 0048cd94 bytes db1b1f94
+ 0048cdd4 bytes f31b1f94
- 0048cda8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048cda8 ["INT_ADD", "register:40f0:8", ["const:48cda8:8", "const:4:8"]]
- 0048cda8 ["CALLIND", null, ["register:0:8"]]
+ 0048cde8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048cde8 ["INT_ADD", "register:40f0:8", ["const:48cde8:8", "const:4:8"]]
+ 0048cde8 ["CALLIND", null, ["register:0:8"]]
- 0048cda8 bytes 00013fd6
+ 0048cde8 bytes 00013fd6
- 0048cdb0 ["INT_ADD", "register:40f0:8", ["const:48cdb0:8", "const:4:8"]]
- 0048cdb0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0048cdf0 ["INT_ADD", "register:40f0:8", ["const:48cdf0:8", "const:4:8"]]
+ 0048cdf0 ["CALL", null, ["callee:00c57f50:8"]]
- 0048cdb0 bytes 342c1f94
+ 0048cdf0 bytes 582c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e92ea1b837f099cd3ed0daa7df1a09"></a>

### [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) → [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) FUN_0048ce94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 368件 [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) · 呼出先 2件 [`0046d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md) [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md)
- 新版 呼出元 368件 [`0047a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1c0.md) [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) [`005b17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b17f8.md) [`005b1bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1bc4.md) [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) · 呼出先 2件 [`0046d0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d0e4.md) [`0046d43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d43c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md#insn-0048ce68)
- 新版 `0048cea8`（命令位置の公開資料なし）

~~~diff
- 0048ce68 ["INT_ADD", "register:40f0:8", ["const:48ce68:8", "const:4:8"]]
- 0048ce68 ["CALL", null, ["callee:0046d0e4:8"]]
+ 0048cea8 ["INT_ADD", "register:40f0:8", ["const:48cea8:8", "const:4:8"]]
+ 0048cea8 ["CALL", null, ["callee:0046d0e4:8"]]
- 0048ce68 bytes 8f80ff97
+ 0048cea8 bytes 8f80ff97
~~~


<a id="compare-f3aadae62115f20193698fac149ad751"></a>

### [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) → [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) FUN_0048cec4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 108件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d5b4.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`005b9a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9a98.md) · 呼出先 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md)
- 新版 呼出元 108件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d5f4.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`005b9ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9ad8.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048ce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md#insn-0048ce8c)
- 新版 `0048cecc`（命令位置の公開資料なし）

~~~diff
- 0048ce8c ["INT_ADD", "register:40f0:8", ["const:48ce8c:8", "const:4:8"]]
- 0048ce8c ["CALL", null, ["callee:00c58650:8"]]
+ 0048cecc ["INT_ADD", "register:40f0:8", ["const:48cecc:8", "const:4:8"]]
+ 0048cecc ["CALL", null, ["callee:00c58650:8"]]
- 0048ce8c bytes bd2d1f94
+ 0048cecc bytes e12d1f94
~~~


<a id="compare-ec3585c5b4a66d38bf75c98006a2e991"></a>

### [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) → [`0048cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cef8.md) FUN_0048cef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0074e384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074e/0074e384.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) [`00478690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md) [`00478c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c14.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0074e3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e3dc.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 4件 [`00478354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478354.md) [`004786d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/004786d0.md) [`00478c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478c54.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cee0) · [`0048cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cf04) · [`0048cf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md#insn-0048cf10)
- 新版 `0048cf20`（命令位置の公開資料なし） · `0048cf44`（命令位置の公開資料なし） · `0048cf50`（命令位置の公開資料なし）

~~~diff
- 0048cee0 ["INT_ADD", "register:40f0:8", ["const:48cee0:8", "const:4:8"]]
- 0048cee0 ["CALL", null, ["callee:004786d0:8"]]
+ 0048cf20 ["INT_ADD", "register:40f0:8", ["const:48cf20:8", "const:4:8"]]
+ 0048cf20 ["CALL", null, ["callee:004786d0:8"]]
- 0048cee0 bytes ecadff97
+ 0048cf20 bytes ecadff97
- 0048cf04 ["INT_ADD", "register:40f0:8", ["const:48cf04:8", "const:4:8"]]
- 0048cf04 ["CALL", null, ["callee:00478354:8"]]
+ 0048cf44 ["INT_ADD", "register:40f0:8", ["const:48cf44:8", "const:4:8"]]
+ 0048cf44 ["CALL", null, ["callee:00478354:8"]]
- 0048cf04 bytes 04adff97
+ 0048cf44 bytes 04adff97
- 0048cf10 ["INT_ADD", "register:40f0:8", ["const:48cf10:8", "const:4:8"]]
- 0048cf10 ["CALL", null, ["callee:00478c54:8"]]
+ 0048cf50 ["INT_ADD", "register:40f0:8", ["const:48cf50:8", "const:4:8"]]
+ 0048cf50 ["CALL", null, ["callee:00478c54:8"]]
- 0048cf10 bytes 41afff97
+ 0048cf50 bytes 41afff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc05d400e6a0bba8bc76bb259fe96ffb"></a>

### [`0048d2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md) → [`0048d2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2fc.md) FUN_0048d2fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) · 呼出先 5件 [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) · 呼出先 5件 [`0055e8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d2e4) · [`0048d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d2f4) · [`0048d308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d2bc.md#insn-0048d308)
- 新版 `0048d324`（命令位置の公開資料なし） · `0048d334`（命令位置の公開資料なし） · `0048d348`（命令位置の公開資料なし）

~~~diff
- 0048d2e4 ["INT_ADD", "register:40f0:8", ["const:48d2e4:8", "const:4:8"]]
- 0048d2e4 ["CALL", null, ["callee:0055e8b4:8"]]
+ 0048d324 ["INT_ADD", "register:40f0:8", ["const:48d324:8", "const:4:8"]]
+ 0048d324 ["CALL", null, ["callee:0055e8b4:8"]]
- 0048d2e4 bytes 64450394
+ 0048d324 bytes 64450394
- 0048d2f4 ["INT_ADD", "register:40f0:8", ["const:48d2f4:8", "const:4:8"]]
- 0048d2f4 ["CALL", null, ["callee:00560498:8"]]
+ 0048d334 ["INT_ADD", "register:40f0:8", ["const:48d334:8", "const:4:8"]]
+ 0048d334 ["CALL", null, ["callee:00560498:8"]]
- 0048d2f4 bytes 594c0394
+ 0048d334 bytes 594c0394
- 0048d308 ["INT_ADD", "register:40f0:8", ["const:48d308:8", "const:4:8"]]
- 0048d308 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048d348 ["INT_ADD", "register:40f0:8", ["const:48d348:8", "const:4:8"]]
+ 0048d348 ["CALL", null, ["callee:00c53da0:8"]]
- 0048d308 bytes 7e1a1f94
+ 0048d348 bytes 961a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751788080d55c58ea3c939c171bda871"></a>

### [`0048d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md) → [`0048d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d3b0.md) FUN_0048d3b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 15件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) · 呼出先 5件 [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 15件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`004887d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004887d0.md) · 呼出先 5件 [`0055e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d398) · [`0048d3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d3a8) · [`0048d3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d370.md#insn-0048d3bc)
- 新版 `0048d3d8`（命令位置の公開資料なし） · `0048d3e8`（命令位置の公開資料なし） · `0048d3fc`（命令位置の公開資料なし）

~~~diff
- 0048d398 ["INT_ADD", "register:40f0:8", ["const:48d398:8", "const:4:8"]]
- 0048d398 ["CALL", null, ["callee:0055e790:8"]]
+ 0048d3d8 ["INT_ADD", "register:40f0:8", ["const:48d3d8:8", "const:4:8"]]
+ 0048d3d8 ["CALL", null, ["callee:0055e790:8"]]
- 0048d398 bytes ee440394
+ 0048d3d8 bytes ee440394
- 0048d3a8 ["INT_ADD", "register:40f0:8", ["const:48d3a8:8", "const:4:8"]]
- 0048d3a8 ["CALL", null, ["callee:00560498:8"]]
+ 0048d3e8 ["INT_ADD", "register:40f0:8", ["const:48d3e8:8", "const:4:8"]]
+ 0048d3e8 ["CALL", null, ["callee:00560498:8"]]
- 0048d3a8 bytes 2c4c0394
+ 0048d3e8 bytes 2c4c0394
- 0048d3bc ["INT_ADD", "register:40f0:8", ["const:48d3bc:8", "const:4:8"]]
- 0048d3bc ["CALL", null, ["callee:00c53da0:8"]]
+ 0048d3fc ["INT_ADD", "register:40f0:8", ["const:48d3fc:8", "const:4:8"]]
+ 0048d3fc ["CALL", null, ["callee:00c53da0:8"]]
- 0048d3bc bytes 511a1f94
+ 0048d3fc bytes 691a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1bf6e26c9ea9491b80d4fb3c6c55426"></a>

### [`0048d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md) → [`0048d464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d464.md) FUN_0048d464

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) · 呼出先 5件 [`0055ed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`009818cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/009818cc.md) · 呼出先 5件 [`0055ed48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ed48.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d450) · [`0048d46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d46c) · [`0048d48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md#insn-0048d48c)
- 新版 `0048d490`（命令位置の公開資料なし） · `0048d4ac`（命令位置の公開資料なし） · `0048d4cc`（命令位置の公開資料なし）

~~~diff
- 0048d450 ["INT_ADD", "register:40f0:8", ["const:48d450:8", "const:4:8"]]
- 0048d450 ["CALL", null, ["callee:00597648:8"]]
+ 0048d490 ["INT_ADD", "register:40f0:8", ["const:48d490:8", "const:4:8"]]
+ 0048d490 ["CALL", null, ["callee:00597648:8"]]
- 0048d450 bytes 6e280494
+ 0048d490 bytes 6e280494
- 0048d46c ["INT_ADD", "register:40f0:8", ["const:48d46c:8", "const:4:8"]]
- 0048d46c ["CALL", null, ["callee:0055ed48:8"]]
+ 0048d4ac ["INT_ADD", "register:40f0:8", ["const:48d4ac:8", "const:4:8"]]
+ 0048d4ac ["CALL", null, ["callee:0055ed48:8"]]
- 0048d46c bytes 27460394
+ 0048d4ac bytes 27460394
- 0048d48c ["INT_ADD", "register:40f0:8", ["const:48d48c:8", "const:4:8"]]
- 0048d48c ["CALL", null, ["callee:00c53da0:8"]]
+ 0048d4cc ["INT_ADD", "register:40f0:8", ["const:48d4cc:8", "const:4:8"]]
+ 0048d4cc ["CALL", null, ["callee:00c53da0:8"]]
- 0048d48c bytes 1d1a1f94
+ 0048d4cc bytes 351a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521db7b32b0777256e42ff810909f156"></a>

### [`0048d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md) → [`0048d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d85c.md) FUN_0048d85c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) · 呼出先 5件 [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 7件 [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`004887d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004887d0.md) [`004896dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004896dc.md) [`00637890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00637/00637890.md) · 呼出先 5件 [`0055f0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048d848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d848) · [`0048d864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d864) · [`0048d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d81c.md#insn-0048d878)
- 新版 `0048d888`（命令位置の公開資料なし） · `0048d8a4`（命令位置の公開資料なし） · `0048d8b8`（命令位置の公開資料なし）

~~~diff
- 0048d848 ["INT_ADD", "register:40f0:8", ["const:48d848:8", "const:4:8"]]
- 0048d848 ["CALL", null, ["callee:00597648:8"]]
+ 0048d888 ["INT_ADD", "register:40f0:8", ["const:48d888:8", "const:4:8"]]
+ 0048d888 ["CALL", null, ["callee:00597648:8"]]
- 0048d848 bytes 70270494
+ 0048d888 bytes 70270494
- 0048d864 ["INT_ADD", "register:40f0:8", ["const:48d864:8", "const:4:8"]]
- 0048d864 ["CALL", null, ["callee:0055f0d8:8"]]
+ 0048d8a4 ["INT_ADD", "register:40f0:8", ["const:48d8a4:8", "const:4:8"]]
+ 0048d8a4 ["CALL", null, ["callee:0055f0d8:8"]]
- 0048d864 bytes 0d460394
+ 0048d8a4 bytes 0d460394
- 0048d878 ["INT_ADD", "register:40f0:8", ["const:48d878:8", "const:4:8"]]
- 0048d878 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048d8b8 ["INT_ADD", "register:40f0:8", ["const:48d8b8:8", "const:4:8"]]
+ 0048d8b8 ["CALL", null, ["callee:00c53da0:8"]]
- 0048d878 bytes 22191f94
+ 0048d8b8 bytes 3a191f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8474977387aa75419b7af0843f76f655"></a>

### [`0048dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md) → [`0048dca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dca8.md) FUN_0048dca8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00494e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00494e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494e48.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md#insn-0048dc84) · [`0048dca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md#insn-0048dca4)
- 新版 `0048dcc4`（命令位置の公開資料なし） · `0048dce4`（命令位置の公開資料なし）

~~~diff
- 0048dc84 ["INT_ADD", "register:40f0:8", ["const:48dc84:8", "const:4:8"]]
- 0048dc84 ["CALL", null, ["callee:00c53da0:8"]]
+ 0048dcc4 ["INT_ADD", "register:40f0:8", ["const:48dcc4:8", "const:4:8"]]
+ 0048dcc4 ["CALL", null, ["callee:00c53da0:8"]]
- 0048dc84 bytes 1f181f94
+ 0048dcc4 bytes 37181f94
- 0048dca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048dca4 ["INT_ADD", "register:40f0:8", ["const:48dca4:8", "const:4:8"]]
- 0048dca4 ["CALLIND", null, ["register:0:8"]]
+ 0048dce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048dce4 ["INT_ADD", "register:40f0:8", ["const:48dce4:8", "const:4:8"]]
+ 0048dce4 ["CALLIND", null, ["register:0:8"]]
- 0048dca4 bytes 00013fd6
+ 0048dce4 bytes 00013fd6
~~~


<a id="compare-62bbc243a62aae8c5c5cbdfb549fdf00"></a>

### [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) → [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) FUN_0048e0f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 23件 [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md) · 呼出先 2件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 23件 [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md) [`004901b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md) [`004906dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md) · 呼出先 2件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048e164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md#insn-0048e164) · [`0048e178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md#insn-0048e178)
- 新版 `0048e1a4`（命令位置の公開資料なし） · `0048e1b8`（命令位置の公開資料なし）

~~~diff
- 0048e164 ["INT_ADD", "register:40f0:8", ["const:48e164:8", "const:4:8"]]
- 0048e164 ["CALL", null, ["callee:00c580a0:8"]]
+ 0048e1a4 ["INT_ADD", "register:40f0:8", ["const:48e1a4:8", "const:4:8"]]
+ 0048e1a4 ["CALL", null, ["callee:00c580a0:8"]]
- 0048e164 bytes 9b271f94
+ 0048e1a4 bytes bf271f94
- 0048e178 ["INT_ADD", "register:40f0:8", ["const:48e178:8", "const:4:8"]]
- 0048e178 ["CALL", null, ["callee:00c58120:8"]]
+ 0048e1b8 ["INT_ADD", "register:40f0:8", ["const:48e1b8:8", "const:4:8"]]
+ 0048e1b8 ["CALL", null, ["callee:00c58120:8"]]
- 0048e178 bytes b6271f94
+ 0048e1b8 bytes da271f94
~~~


<a id="compare-fc09e19f904c762aff08011e5d1ab52e"></a>

### [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) → [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) FUN_0048e820

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 44件 [`005b5814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md) [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) [`0061e6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md) [`00626a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a34.md) [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 44件 [`005b5854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5854.md) [`005b5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md) [`0061e6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6e8.md) [`00626a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/00626a74.md) [`007832cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007832cc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048e824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e824) · [`0048e83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e83c) · [`0048e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md#insn-0048e850)
- 新版 `0048e864`（命令位置の公開資料なし） · `0048e87c`（命令位置の公開資料なし） · `0048e890`（命令位置の公開資料なし）

~~~diff
- 0048e824 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048e824 ["INT_ADD", "register:40f0:8", ["const:48e824:8", "const:4:8"]]
- 0048e824 ["CALLIND", null, ["register:0:8"]]
+ 0048e864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048e864 ["INT_ADD", "register:40f0:8", ["const:48e864:8", "const:4:8"]]
+ 0048e864 ["CALLIND", null, ["register:0:8"]]
- 0048e824 bytes 00013fd6
+ 0048e864 bytes 00013fd6
- 0048e83c ["INT_ADD", "register:40f0:8", ["const:48e83c:8", "const:4:8"]]
- 0048e83c ["CALL", null, ["callee:00c53da0:8"]]
+ 0048e87c ["INT_ADD", "register:40f0:8", ["const:48e87c:8", "const:4:8"]]
+ 0048e87c ["CALL", null, ["callee:00c53da0:8"]]
- 0048e83c bytes 31151f94
+ 0048e87c bytes 49151f94
- 0048e850 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048e850 ["INT_ADD", "register:40f0:8", ["const:48e850:8", "const:4:8"]]
- 0048e850 ["CALLIND", null, ["register:0:8"]]
+ 0048e890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048e890 ["INT_ADD", "register:40f0:8", ["const:48e890:8", "const:4:8"]]
+ 0048e890 ["CALLIND", null, ["register:0:8"]]
- 0048e850 bytes 00013fd6
+ 0048e890 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

