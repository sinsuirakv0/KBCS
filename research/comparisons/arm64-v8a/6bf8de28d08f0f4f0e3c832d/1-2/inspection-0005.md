# v16.0.1 → v16.0.2 · 要調査の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-6e6ba2052589f877316b141ec69801e9"></a>

### [`0048f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f410.md) → [`0048f450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md) FUN_0048f450

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f410.md#insn-0048f42c) · [`0048f44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f410.md#insn-0048f44c)
- 新版 [`0048f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md#insn-0048f46c) · [`0048f48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md#insn-0048f48c)

~~~diff
- 0048f42c ["INT_ADD", "register:40f0:8", ["const:48f42c:8", "const:4:8"]]
- 0048f42c ["CALL", null, ["callee:00c53da0:8"]]
+ 0048f46c ["INT_ADD", "register:40f0:8", ["const:48f46c:8", "const:4:8"]]
+ 0048f46c ["CALL", null, ["callee:00c53da0:8"]]
- 0048f42c bytes 35121f94
+ 0048f46c bytes 4d121f94
- 0048f44c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f44c ["INT_ADD", "register:40f0:8", ["const:48f44c:8", "const:4:8"]]
- 0048f44c ["CALLIND", null, ["register:0:8"]]
+ 0048f48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f48c ["INT_ADD", "register:40f0:8", ["const:48f48c:8", "const:4:8"]]
+ 0048f48c ["CALLIND", null, ["register:0:8"]]
- 0048f44c bytes 00013fd6
+ 0048f48c bytes 00013fd6
~~~


<a id="compare-c751030e2461c78274be307d4da232c1"></a>

### [`004927c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004927c4.md) → [`00492804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md) FUN_00492804

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004927c4.md#insn-00492810) · [`00492824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004927c4.md#insn-00492824) · [`0049282c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004927c4.md#insn-0049282c)
- 新版 [`00492850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-00492850) · [`00492864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-00492864) · [`0049286c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-0049286c)

~~~diff
- 00492810 ["INT_ADD", "register:40f0:8", ["const:492810:8", "const:4:8"]]
- 00492810 ["CALL", null, ["callee:00c53da0:8"]]
+ 00492850 ["INT_ADD", "register:40f0:8", ["const:492850:8", "const:4:8"]]
+ 00492850 ["CALL", null, ["callee:00c53da0:8"]]
- 00492810 bytes 3c051f94
+ 00492850 bytes 54051f94
- 00492824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00492824 ["INT_ADD", "register:40f0:8", ["const:492824:8", "const:4:8"]]
- 00492824 ["CALLIND", null, ["register:0:8"]]
+ 00492864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492864 ["INT_ADD", "register:40f0:8", ["const:492864:8", "const:4:8"]]
+ 00492864 ["CALLIND", null, ["register:0:8"]]
- 00492824 bytes 00013fd6
+ 00492864 bytes 00013fd6
- 0049282c ["INT_ADD", "register:40f0:8", ["const:49282c:8", "const:4:8"]]
- 0049282c ["CALL", null, ["callee:00c57f50:8"]]
+ 0049286c ["INT_ADD", "register:40f0:8", ["const:49286c:8", "const:4:8"]]
+ 0049286c ["CALL", null, ["callee:00c57f50:8"]]
- 0049282c bytes 95151f94
+ 0049286c bytes b9151f94
~~~


<a id="compare-b994433877538d975f19f33fe6df4dcb"></a>

### [`0049285c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049285c.md) → [`0049289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md) FUN_0049289c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049285c.md#insn-00492878) · [`00492898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049285c.md#insn-00492898)
- 新版 [`004928b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md#insn-004928b8) · [`004928d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md#insn-004928d8)

~~~diff
- 00492878 ["INT_ADD", "register:40f0:8", ["const:492878:8", "const:4:8"]]
- 00492878 ["CALL", null, ["callee:00c53da0:8"]]
+ 004928b8 ["INT_ADD", "register:40f0:8", ["const:4928b8:8", "const:4:8"]]
+ 004928b8 ["CALL", null, ["callee:00c53da0:8"]]
- 00492878 bytes 22051f94
+ 004928b8 bytes 3a051f94
- 00492898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00492898 ["INT_ADD", "register:40f0:8", ["const:492898:8", "const:4:8"]]
- 00492898 ["CALLIND", null, ["register:0:8"]]
+ 004928d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004928d8 ["INT_ADD", "register:40f0:8", ["const:4928d8:8", "const:4:8"]]
+ 004928d8 ["CALLIND", null, ["register:0:8"]]
- 00492898 bytes 00013fd6
+ 004928d8 bytes 00013fd6
~~~


<a id="compare-c5241238d6b6817be3bf7e130a7bd194"></a>

### [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) → [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) FUN_00492d44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`00872020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md) [`00872250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 27件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) [`00872078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872078.md) [`008722a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008722a8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md#insn-00492d6c) · [`00492d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md#insn-00492d7c) · [`00492d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md#insn-00492d8c)
- 新版 [`00492dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dac) · [`00492dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dbc) · [`00492dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dcc)

~~~diff
- 00492d6c ["INT_ADD", "register:40f0:8", ["const:492d6c:8", "const:4:8"]]
- 00492d6c ["CALL", null, ["callee:0043bb60:8"]]
+ 00492dac ["INT_ADD", "register:40f0:8", ["const:492dac:8", "const:4:8"]]
+ 00492dac ["CALL", null, ["callee:0043bb60:8"]]
- 00492d6c bytes 6da3fe97
+ 00492dac bytes 6da3fe97
- 00492d7c ["INT_ADD", "register:40f0:8", ["const:492d7c:8", "const:4:8"]]
- 00492d7c ["CALL", null, ["callee:00492e48:8"]]
+ 00492dbc ["INT_ADD", "register:40f0:8", ["const:492dbc:8", "const:4:8"]]
+ 00492dbc ["CALL", null, ["callee:00492e48:8"]]
- 00492d7c bytes 23000094
+ 00492dbc bytes 23000094
- 00492d8c ["INT_ADD", "register:40f0:8", ["const:492d8c:8", "const:4:8"]]
- 00492d8c ["CALL", null, ["callee:00c57f80:8"]]
+ 00492dcc ["INT_ADD", "register:40f0:8", ["const:492dcc:8", "const:4:8"]]
+ 00492dcc ["CALL", null, ["callee:00c57f80:8"]]
- 00492d8c bytes 49141f94
+ 00492dcc bytes 6d141f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94540c3de22f741513eeba508fe94b2f"></a>

### [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) → [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) FUN_00492e48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 96件 [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`005b9b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9b54.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00441f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441f14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 96件 [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005d9f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d9/005d9f8c.md) [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md#insn-00492e58) · [`00492e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md#insn-00492e6c) · [`00492e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md#insn-00492e98)
- 新版 [`00492e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492e98) · [`00492eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492eac) · [`00492ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492ed8)

~~~diff
- 00492e58 ["INT_ADD", "register:40f0:8", ["const:492e58:8", "const:4:8"]]
- 00492e58 ["CALL", null, ["callee:0043bb60:8"]]
+ 00492e98 ["INT_ADD", "register:40f0:8", ["const:492e98:8", "const:4:8"]]
+ 00492e98 ["CALL", null, ["callee:0043bb60:8"]]
- 00492e58 bytes 32a3fe97
+ 00492e98 bytes 32a3fe97
- 00492e6c ["INT_ADD", "register:40f0:8", ["const:492e6c:8", "const:4:8"]]
- 00492e6c ["CALL", null, ["callee:0043bb60:8"]]
+ 00492eac ["INT_ADD", "register:40f0:8", ["const:492eac:8", "const:4:8"]]
+ 00492eac ["CALL", null, ["callee:0043bb60:8"]]
- 00492e6c bytes 2da3fe97
+ 00492eac bytes 2da3fe97
- 00492e98 ["INT_ADD", "register:40f0:8", ["const:492e98:8", "const:4:8"]]
- 00492e98 ["CALL", null, ["callee:00441f54:8"]]
+ 00492ed8 ["INT_ADD", "register:40f0:8", ["const:492ed8:8", "const:4:8"]]
+ 00492ed8 ["CALL", null, ["callee:00441f54:8"]]
- 00492e98 bytes 1fbcfe97
+ 00492ed8 bytes 1fbcfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2650ccb737d5691971982bb7cd198a"></a>

### [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md) → [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md) FUN_00492f68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007ae998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md) [`007aef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 5件 [`00493008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 25件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ae9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md) [`007aefa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 5件 [`00493048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md#insn-00492f68) · [`00492f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md#insn-00492f7c) · [`00492f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md#insn-00492f90)
- 新版 [`00492fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fa8) · [`00492fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fbc) · [`00492fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fd0)

~~~diff
- 00492f68 ["INT_ADD", "register:40f0:8", ["const:492f68:8", "const:4:8"]]
- 00492f68 ["CALL", null, ["callee:00493048:8"]]
+ 00492fa8 ["INT_ADD", "register:40f0:8", ["const:492fa8:8", "const:4:8"]]
+ 00492fa8 ["CALL", null, ["callee:00493048:8"]]
- 00492f68 bytes 28000094
+ 00492fa8 bytes 28000094
- 00492f7c ["INT_ADD", "register:40f0:8", ["const:492f7c:8", "const:4:8"]]
- 00492f7c ["CALL", null, ["callee:00c53da0:8"]]
+ 00492fbc ["INT_ADD", "register:40f0:8", ["const:492fbc:8", "const:4:8"]]
+ 00492fbc ["CALL", null, ["callee:00c53da0:8"]]
- 00492f7c bytes 61031f94
+ 00492fbc bytes 79031f94
- 00492f90 ["INT_ADD", "register:40f0:8", ["const:492f90:8", "const:4:8"]]
- 00492f90 ["CALL", null, ["callee:00c57f80:8"]]
+ 00492fd0 ["INT_ADD", "register:40f0:8", ["const:492fd0:8", "const:4:8"]]
+ 00492fd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00492f90 bytes c8131f94
+ 00492fd0 bytes ec131f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c50540831011835356eebd5d8ac68c"></a>

### [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) → [`004936d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md) FUN_004936d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 5件 [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 16件 [`005b17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b17f8.md) [`005b1bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1bc4.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061308c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 5件 [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004936d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md#insn-004936d4) · [`00493700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md#insn-00493700) · [`00493710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md#insn-00493710)
- 新版 [`00493714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493714) · [`00493740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493740) · [`00493750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493750)

~~~diff
- 004936d4 ["INT_ADD", "register:40f0:8", ["const:4936d4:8", "const:4:8"]]
- 004936d4 ["CALL", null, ["callee:00550a50:8"]]
+ 00493714 ["INT_ADD", "register:40f0:8", ["const:493714:8", "const:4:8"]]
+ 00493714 ["CALL", null, ["callee:00550a50:8"]]
- 004936d4 bytes cff40294
+ 00493714 bytes cff40294
- 00493700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00493700 ["INT_ADD", "register:40f0:8", ["const:493700:8", "const:4:8"]]
- 00493700 ["CALLIND", null, ["register:0:8"]]
+ 00493740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493740 ["INT_ADD", "register:40f0:8", ["const:493740:8", "const:4:8"]]
+ 00493740 ["CALLIND", null, ["register:0:8"]]
- 00493700 bytes 00013fd6
+ 00493740 bytes 00013fd6
- 00493710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00493710 ["INT_ADD", "register:40f0:8", ["const:493710:8", "const:4:8"]]
- 00493710 ["CALLIND", null, ["register:0:8"]]
+ 00493750 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493750 ["INT_ADD", "register:40f0:8", ["const:493750:8", "const:4:8"]]
+ 00493750 ["CALLIND", null, ["register:0:8"]]
- 00493710 bytes 00013fd6
+ 00493750 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eddf4478c1eb9ce48b0e49640f341448"></a>

### [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) → [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) FUN_00493914

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00479fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md) [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) [`007ae854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 8件 [`0047a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a02c.md) [`007ad8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md) [`007ad9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md) [`007ae8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md#insn-00493900) · [`00493918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md#insn-00493918) · [`0049392c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md#insn-0049392c)
- 新版 [`00493940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-00493940) · [`00493958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-00493958) · [`0049396c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-0049396c)

~~~diff
- 00493900 ["COPY", "register:0:8", ["register:4048:8"]]
- 00493900 ["INT_ADD", "register:40f0:8", ["const:493900:8", "const:4:8"]]
- 00493900 ["CALLIND", null, ["register:0:8"]]
+ 00493940 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00493940 ["INT_ADD", "register:40f0:8", ["const:493940:8", "const:4:8"]]
+ 00493940 ["CALLIND", null, ["register:0:8"]]
- 00493900 bytes 20013fd6
+ 00493940 bytes 20013fd6
- 00493918 ["INT_ADD", "register:40f0:8", ["const:493918:8", "const:4:8"]]
- 00493918 ["CALL", null, ["callee:00c53da0:8"]]
+ 00493958 ["INT_ADD", "register:40f0:8", ["const:493958:8", "const:4:8"]]
+ 00493958 ["CALL", null, ["callee:00c53da0:8"]]
- 00493918 bytes fa001f94
+ 00493958 bytes 12011f94
- 0049392c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049392c ["INT_ADD", "register:40f0:8", ["const:49392c:8", "const:4:8"]]
- 0049392c ["CALLIND", null, ["register:0:8"]]
+ 0049396c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049396c ["INT_ADD", "register:40f0:8", ["const:49396c:8", "const:4:8"]]
+ 0049396c ["CALLIND", null, ["register:0:8"]]
- 0049392c bytes 00013fd6
+ 0049396c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e81578fa4496ecb24321780d1905a4"></a>

### [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) → [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) FUN_004939d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 50件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`0062ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062ecfc.md) [`00645294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645294.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 50件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`00612324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00612/00612324.md) [`0062ed3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062e/0062ed3c.md) [`006452d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/006452d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md#insn-00493a04)
- 新版 [`00493a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md#insn-00493a44)

~~~diff
- 00493a04 ["INT_ADD", "register:40f0:8", ["const:493a04:8", "const:4:8"]]
- 00493a04 ["CALL", null, ["callee:00c58120:8"]]
+ 00493a44 ["INT_ADD", "register:40f0:8", ["const:493a44:8", "const:4:8"]]
+ 00493a44 ["CALL", null, ["callee:00c58120:8"]]
- 00493a04 bytes 93111f94
+ 00493a44 bytes b7111f94
~~~


<a id="compare-dc76e2ef978e53549924f6f61a2d204e"></a>

### [`00493a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md) → [`00493a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md) FUN_00493a88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 4件 [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md#insn-00493ad4) · [`00493af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md#insn-00493af4) · [`00493b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md#insn-00493b14)
- 新版 [`00493b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b14) · [`00493b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b34) · [`00493b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b54)

~~~diff
- 00493ad4 ["INT_ADD", "register:40f0:8", ["const:493ad4:8", "const:4:8"]]
- 00493ad4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00493b14 ["INT_ADD", "register:40f0:8", ["const:493b14:8", "const:4:8"]]
+ 00493b14 ["CALL", null, ["callee:00c57f60:8"]]
- 00493ad4 bytes ef101f94
+ 00493b14 bytes 13111f94
- 00493af4 ["INT_ADD", "register:40f0:8", ["const:493af4:8", "const:4:8"]]
- 00493af4 ["CALL", null, ["callee:00c58010:8"]]
+ 00493b34 ["INT_ADD", "register:40f0:8", ["const:493b34:8", "const:4:8"]]
+ 00493b34 ["CALL", null, ["callee:00c58010:8"]]
- 00493af4 bytes 13111f94
+ 00493b34 bytes 37111f94
- 00493b14 ["INT_ADD", "register:40f0:8", ["const:493b14:8", "const:4:8"]]
- 00493b14 ["CALL", null, ["callee:0044295c:8"]]
+ 00493b54 ["INT_ADD", "register:40f0:8", ["const:493b54:8", "const:4:8"]]
+ 00493b54 ["CALL", null, ["callee:0044295c:8"]]
- 00493b14 bytes 82bbfe97
+ 00493b54 bytes 82bbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d4206479b1d8fb9adc710f47d38f671"></a>

### [`00493c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c80.md) → [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) FUN_00493cc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md)
- 新版 呼出元 7件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c80.md#insn-00493c94)
- 新版 [`00493cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md#insn-00493cd4)

~~~diff
- 00493c94 ["INT_ADD", "register:40f0:8", ["const:493c94:8", "const:4:8"]]
- 00493c94 ["CALL", null, ["callee:00493e08:8"]]
+ 00493cd4 ["INT_ADD", "register:40f0:8", ["const:493cd4:8", "const:4:8"]]
+ 00493cd4 ["CALL", null, ["callee:00493e08:8"]]
- 00493c94 bytes 4d000094
+ 00493cd4 bytes 4d000094
~~~


<a id="compare-8e115361e015aed6b869214bfbb1b727"></a>

### [`00493ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493ce8.md) → [`00493d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md) FUN_00493d28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 7件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493ce8.md#insn-00493d58) · [`00493d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493ce8.md#insn-00493d80)
- 新版 [`00493d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md#insn-00493d98) · [`00493dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md#insn-00493dc0)

~~~diff
- 00493d58 ["INT_ADD", "register:40f0:8", ["const:493d58:8", "const:4:8"]]
- 00493d58 ["CALL", null, ["callee:00c58120:8"]]
+ 00493d98 ["INT_ADD", "register:40f0:8", ["const:493d98:8", "const:4:8"]]
+ 00493d98 ["CALL", null, ["callee:00c58120:8"]]
- 00493d58 bytes be101f94
+ 00493d98 bytes e2101f94
- 00493d80 ["INT_ADD", "register:40f0:8", ["const:493d80:8", "const:4:8"]]
- 00493d80 ["CALL", null, ["callee:00c58120:8"]]
+ 00493dc0 ["INT_ADD", "register:40f0:8", ["const:493dc0:8", "const:4:8"]]
+ 00493dc0 ["CALL", null, ["callee:00c58120:8"]]
- 00493d80 bytes b4101f94
+ 00493dc0 bytes d8101f94
~~~


<a id="compare-63fa4e02712e1d841b6c585b7b732f7b"></a>

### [`00493dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md) → [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) FUN_00493e08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00493c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c80.md) [`00563c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00563/00563c60.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md) [`0087d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d2a0.md) [`00b59ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b59/00b59ca4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 7件 [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) [`00563ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563ca0.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md) [`0087d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md) [`00b59d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md#insn-00493e34) · [`00493e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493dc8.md#insn-00493e90)
- 新版 [`00493e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md#insn-00493e74) · [`00493ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md#insn-00493ed0)

~~~diff
- 00493e34 ["INT_ADD", "register:40f0:8", ["const:493e34:8", "const:4:8"]]
- 00493e34 ["CALL", null, ["callee:00c58120:8"]]
+ 00493e74 ["INT_ADD", "register:40f0:8", ["const:493e74:8", "const:4:8"]]
+ 00493e74 ["CALL", null, ["callee:00c58120:8"]]
- 00493e34 bytes 87101f94
+ 00493e74 bytes ab101f94
- 00493e90 ["INT_ADD", "register:40f0:8", ["const:493e90:8", "const:4:8"]]
- 00493e90 ["CALL", null, ["callee:00c58120:8"]]
+ 00493ed0 ["INT_ADD", "register:40f0:8", ["const:493ed0:8", "const:4:8"]]
+ 00493ed0 ["CALL", null, ["callee:00c58120:8"]]
- 00493e90 bytes 70101f94
+ 00493ed0 bytes 94101f94
~~~


<a id="compare-1d6488aab981bede0622529e498d9e01"></a>

### [`00494308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494308.md) → [`00494348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md) FUN_00494348

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494308.md#insn-00494378) · [`0049438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494308.md#insn-0049438c) · [`00494394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494308.md#insn-00494394)
- 新版 [`004943b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943b8) · [`004943cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943cc) · [`004943d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943d4)

~~~diff
- 00494378 ["INT_ADD", "register:40f0:8", ["const:494378:8", "const:4:8"]]
- 00494378 ["CALL", null, ["callee:00c53da0:8"]]
+ 004943b8 ["INT_ADD", "register:40f0:8", ["const:4943b8:8", "const:4:8"]]
+ 004943b8 ["CALL", null, ["callee:00c53da0:8"]]
- 00494378 bytes 62fe1e94
+ 004943b8 bytes 7afe1e94
- 0049438c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049438c ["INT_ADD", "register:40f0:8", ["const:49438c:8", "const:4:8"]]
- 0049438c ["CALLIND", null, ["register:0:8"]]
+ 004943cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004943cc ["INT_ADD", "register:40f0:8", ["const:4943cc:8", "const:4:8"]]
+ 004943cc ["CALLIND", null, ["register:0:8"]]
- 0049438c bytes 00013fd6
+ 004943cc bytes 00013fd6
- 00494394 ["INT_ADD", "register:40f0:8", ["const:494394:8", "const:4:8"]]
- 00494394 ["CALL", null, ["callee:00c57f50:8"]]
+ 004943d4 ["INT_ADD", "register:40f0:8", ["const:4943d4:8", "const:4:8"]]
+ 004943d4 ["CALL", null, ["callee:00c57f50:8"]]
- 00494394 bytes bb0e1f94
+ 004943d4 bytes df0e1f94
~~~


<a id="compare-ded65b4490afd60bec04d7b9ceda4fd5"></a>

### [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) → [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) FUN_004943fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004932d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932d4.md) [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) · 呼出先 4件 [`004943bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00493314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493314.md) [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) · 呼出先 4件 [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004943d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md#insn-004943d8) · [`004943e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md#insn-004943e4) · [`004943f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004943bc.md#insn-004943f8)
- 新版 [`00494418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494418) · [`00494424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494424) · [`00494438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494438)

~~~diff
- 004943d8 ["INT_ADD", "register:40f0:8", ["const:4943d8:8", "const:4:8"]]
- 004943d8 ["CALL", null, ["local:b0:8"]]
+ 00494418 ["INT_ADD", "register:40f0:8", ["const:494418:8", "const:4:8"]]
+ 00494418 ["CALL", null, ["local:b0:8"]]
- 004943d8 bytes f9ffff97
+ 00494418 bytes f9ffff97
- 004943e4 ["INT_ADD", "register:40f0:8", ["const:4943e4:8", "const:4:8"]]
- 004943e4 ["CALL", null, ["local:b0:8"]]
+ 00494424 ["INT_ADD", "register:40f0:8", ["const:494424:8", "const:4:8"]]
+ 00494424 ["CALL", null, ["local:b0:8"]]
- 004943e4 bytes f6ffff97
+ 00494424 bytes f6ffff97
- 004943f8 ["INT_ADD", "register:40f0:8", ["const:4943f8:8", "const:4:8"]]
- 004943f8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00494438 ["INT_ADD", "register:40f0:8", ["const:494438:8", "const:4:8"]]
+ 00494438 ["CALL", null, ["callee:00c53da0:8"]]
- 004943f8 bytes 42fe1e94
+ 00494438 bytes 5afe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e37e0a7c381339157818af918c828a54"></a>

### [`00494514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md) → [`00494554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md) FUN_00494554

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049448c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049448c.md) [`00494bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md) · 呼出先 4件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`004944cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944cc.md) [`00494c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md) · 呼出先 4件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004945c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md#insn-004945c4) · [`004945d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md#insn-004945d8) · [`004945ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md#insn-004945ec)
- 新版 [`00494604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-00494604) · [`00494618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-00494618) · [`0049462c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-0049462c)

~~~diff
- 004945c4 ["INT_ADD", "register:40f0:8", ["const:4945c4:8", "const:4:8"]]
- 004945c4 ["CALL", null, ["callee:00494650:8"]]
+ 00494604 ["INT_ADD", "register:40f0:8", ["const:494604:8", "const:4:8"]]
+ 00494604 ["CALL", null, ["callee:00494650:8"]]
- 004945c4 bytes 13000094
+ 00494604 bytes 13000094
- 004945d8 ["INT_ADD", "register:40f0:8", ["const:4945d8:8", "const:4:8"]]
- 004945d8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00494618 ["INT_ADD", "register:40f0:8", ["const:494618:8", "const:4:8"]]
+ 00494618 ["CALL", null, ["callee:00c53da0:8"]]
- 004945d8 bytes cafd1e94
+ 00494618 bytes e2fd1e94
- 004945ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004945ec ["INT_ADD", "register:40f0:8", ["const:4945ec:8", "const:4:8"]]
- 004945ec ["CALLIND", null, ["register:0:8"]]
+ 0049462c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049462c ["INT_ADD", "register:40f0:8", ["const:49462c:8", "const:4:8"]]
+ 0049462c ["CALLIND", null, ["register:0:8"]]
- 004945ec bytes 00013fd6
+ 0049462c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3bb02480ae5a430287ac5697d4949f"></a>

### [`00494b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494b7c.md) → [`00494bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494bbc.md) FUN_00494bbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004932dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049331c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494b7c.md#insn-00494bb8)
- 新版 [`00494bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494bbc.md#insn-00494bf8)

~~~diff
- 00494bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494bb8 ["INT_ADD", "register:40f0:8", ["const:494bb8:8", "const:4:8"]]
- 00494bb8 ["CALLIND", null, ["register:0:8"]]
+ 00494bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494bf8 ["INT_ADD", "register:40f0:8", ["const:494bf8:8", "const:4:8"]]
+ 00494bf8 ["CALLIND", null, ["register:0:8"]]
- 00494bb8 bytes 00013fd6
+ 00494bf8 bytes 00013fd6
~~~


<a id="compare-8ccc599747a4f48f196e338c573d05f0"></a>

### [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) → [`00494cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md) FUN_00494cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0048e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md) [`004fe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md) [`00796fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796fcc.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 8件 [`0048e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`004fe468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md) [`00797024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md) [`007aaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md#insn-00494cb0) · [`00494cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md#insn-00494cd0) · [`00494d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md#insn-00494d0c)
- 新版 [`00494cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494cf0) · [`00494d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494d10) · [`00494d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494d4c)

~~~diff
- 00494cb0 ["INT_ADD", "register:40f0:8", ["const:494cb0:8", "const:4:8"]]
- 00494cb0 ["CALL", null, ["callee:0046d5e8:8"]]
+ 00494cf0 ["INT_ADD", "register:40f0:8", ["const:494cf0:8", "const:4:8"]]
+ 00494cf0 ["CALL", null, ["callee:0046d5e8:8"]]
- 00494cb0 bytes 3e62ff97
+ 00494cf0 bytes 3e62ff97
- 00494cd0 ["INT_ADD", "register:40f0:8", ["const:494cd0:8", "const:4:8"]]
- 00494cd0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00494d10 ["INT_ADD", "register:40f0:8", ["const:494d10:8", "const:4:8"]]
+ 00494d10 ["CALL", null, ["callee:00c57f60:8"]]
- 00494cd0 bytes 700c1f94
+ 00494d10 bytes 940c1f94
- 00494d0c ["INT_ADD", "register:40f0:8", ["const:494d0c:8", "const:4:8"]]
- 00494d0c ["CALL", null, ["callee:0043bb60:8"]]
+ 00494d4c ["INT_ADD", "register:40f0:8", ["const:494d4c:8", "const:4:8"]]
+ 00494d4c ["CALL", null, ["callee:0043bb60:8"]]
- 00494d0c bytes 859bfe97
+ 00494d4c bytes 859bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b510540b0b989a0248a20627bfbac672"></a>

### [`00494dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494dac.md) → [`00494dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md) FUN_00494dec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494dac.md#insn-00494dd8) · [`00494de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494dac.md#insn-00494de8)
- 新版 [`00494e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md#insn-00494e18) · [`00494e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md#insn-00494e28)

~~~diff
- 00494dd8 ["INT_ADD", "register:40f0:8", ["const:494dd8:8", "const:4:8"]]
- 00494dd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00494e18 ["INT_ADD", "register:40f0:8", ["const:494e18:8", "const:4:8"]]
+ 00494e18 ["CALL", null, ["callee:00c57f80:8"]]
- 00494dd8 bytes 360c1f94
+ 00494e18 bytes 5a0c1f94
- 00494de8 ["INT_ADD", "register:40f0:8", ["const:494de8:8", "const:4:8"]]
- 00494de8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00494e28 ["INT_ADD", "register:40f0:8", ["const:494e28:8", "const:4:8"]]
+ 00494e28 ["CALL", null, ["callee:00c57f80:8"]]
- 00494de8 bytes 320c1f94
+ 00494e28 bytes 560c1f94
~~~


<a id="compare-d3429c9783025de62ff6b32627ab8920"></a>

### [`00495b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495b64.md) → [`00495ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md) FUN_00495ba4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495b64.md#insn-00495b80) · [`00495ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495b64.md#insn-00495ba0)
- 新版 [`00495bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md#insn-00495bc0) · [`00495be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md#insn-00495be0)

~~~diff
- 00495b80 ["INT_ADD", "register:40f0:8", ["const:495b80:8", "const:4:8"]]
- 00495b80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00495bc0 ["INT_ADD", "register:40f0:8", ["const:495bc0:8", "const:4:8"]]
+ 00495bc0 ["CALL", null, ["callee:00c53da0:8"]]
- 00495b80 bytes 60f81e94
+ 00495bc0 bytes 78f81e94
- 00495ba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495ba0 ["INT_ADD", "register:40f0:8", ["const:495ba0:8", "const:4:8"]]
- 00495ba0 ["CALLIND", null, ["register:0:8"]]
+ 00495be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495be0 ["INT_ADD", "register:40f0:8", ["const:495be0:8", "const:4:8"]]
+ 00495be0 ["CALLIND", null, ["register:0:8"]]
- 00495ba0 bytes 00013fd6
+ 00495be0 bytes 00013fd6
~~~


<a id="compare-06d7fd98c57479135b878bf06fae556b"></a>

### [`00495bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495bb4.md) → [`00495bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md) FUN_00495bf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049527c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/0049527c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004952bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952bc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495bb4.md#insn-00495c30) · [`00495c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495bb4.md#insn-00495c44) · [`00495c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495bb4.md#insn-00495c4c)
- 新版 [`00495c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c70) · [`00495c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c84) · [`00495c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c8c)

~~~diff
- 00495c30 ["INT_ADD", "register:40f0:8", ["const:495c30:8", "const:4:8"]]
- 00495c30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00495c70 ["INT_ADD", "register:40f0:8", ["const:495c70:8", "const:4:8"]]
+ 00495c70 ["CALL", null, ["callee:00c53da0:8"]]
- 00495c30 bytes 34f81e94
+ 00495c70 bytes 4cf81e94
- 00495c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495c44 ["INT_ADD", "register:40f0:8", ["const:495c44:8", "const:4:8"]]
- 00495c44 ["CALLIND", null, ["register:0:8"]]
+ 00495c84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495c84 ["INT_ADD", "register:40f0:8", ["const:495c84:8", "const:4:8"]]
+ 00495c84 ["CALLIND", null, ["register:0:8"]]
- 00495c44 bytes 00013fd6
+ 00495c84 bytes 00013fd6
- 00495c4c ["INT_ADD", "register:40f0:8", ["const:495c4c:8", "const:4:8"]]
- 00495c4c ["CALL", null, ["callee:00c57f50:8"]]
+ 00495c8c ["INT_ADD", "register:40f0:8", ["const:495c8c:8", "const:4:8"]]
+ 00495c8c ["CALL", null, ["callee:00c57f50:8"]]
- 00495c4c bytes 8d081f94
+ 00495c8c bytes b1081f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9512b838bef5c62d74681d1759603b8"></a>

### [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) → [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) FUN_00495d84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004953d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00496204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md) [`0049638c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md) [`00496518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00495414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00496244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md) [`004963cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md) [`00496558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md#insn-00495ddc) · [`00495e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md#insn-00495e20) · [`00495e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md#insn-00495e30)
- 新版 [`00495e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e1c) · [`00495e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e60) · [`00495e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e70)

~~~diff
- 00495ddc ["INT_ADD", "register:40f0:8", ["const:495ddc:8", "const:4:8"]]
- 00495ddc ["CALL", null, ["callee:00c58010:8"]]
+ 00495e1c ["INT_ADD", "register:40f0:8", ["const:495e1c:8", "const:4:8"]]
+ 00495e1c ["CALL", null, ["callee:00c58010:8"]]
- 00495ddc bytes 59081f94
+ 00495e1c bytes 7d081f94
- 00495e20 ["INT_ADD", "register:40f0:8", ["const:495e20:8", "const:4:8"]]
- 00495e20 ["CALL", null, ["callee:00c57f60:8"]]
+ 00495e60 ["INT_ADD", "register:40f0:8", ["const:495e60:8", "const:4:8"]]
+ 00495e60 ["CALL", null, ["callee:00c57f60:8"]]
- 00495e20 bytes 1c081f94
+ 00495e60 bytes 40081f94
- 00495e30 ["INT_ADD", "register:40f0:8", ["const:495e30:8", "const:4:8"]]
- 00495e30 ["CALL", null, ["callee:00496244:8"]]
+ 00495e70 ["INT_ADD", "register:40f0:8", ["const:495e70:8", "const:4:8"]]
+ 00495e70 ["CALL", null, ["callee:00496244:8"]]
- 00495e30 bytes f5000094
+ 00495e70 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660b761d49af636ab49d7b7839510c21"></a>

### [`00496204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md) → [`00496244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md) FUN_00496244

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md#insn-0049626c) · [`004962a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md#insn-004962a4) · [`00496354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496204.md#insn-00496354)
- 新版 [`004962ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-004962ac) · [`004962e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-004962e4) · [`00496394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-00496394)

~~~diff
- 0049626c ["INT_ADD", "register:40f0:8", ["const:49626c:8", "const:4:8"]]
- 0049626c ["CALL", null, ["callee:00c58010:8"]]
+ 004962ac ["INT_ADD", "register:40f0:8", ["const:4962ac:8", "const:4:8"]]
+ 004962ac ["CALL", null, ["callee:00c58010:8"]]
- 0049626c bytes 35071f94
+ 004962ac bytes 59071f94
- 004962a4 ["INT_ADD", "register:40f0:8", ["const:4962a4:8", "const:4:8"]]
- 004962a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004962e4 ["INT_ADD", "register:40f0:8", ["const:4962e4:8", "const:4:8"]]
+ 004962e4 ["CALL", null, ["callee:00c57f60:8"]]
- 004962a4 bytes fb061f94
+ 004962e4 bytes 1f071f94
- 00496354 ["INT_ADD", "register:40f0:8", ["const:496354:8", "const:4:8"]]
- 00496354 ["CALL", null, ["callee:00c57f80:8"]]
+ 00496394 ["INT_ADD", "register:40f0:8", ["const:496394:8", "const:4:8"]]
+ 00496394 ["CALL", null, ["callee:00c57f80:8"]]
- 00496354 bytes d7061f94
+ 00496394 bytes fb061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d39226e7ac178a6faee3734bf12cb35"></a>

### [`0049638c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md) → [`004963cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md) FUN_004963cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004963fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md#insn-004963fc) · [`00496434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md#insn-00496434) · [`004964e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/0049638c.md#insn-004964e4)
- 新版 [`0049643c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-0049643c) · [`00496474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-00496474) · [`00496524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-00496524)

~~~diff
- 004963fc ["INT_ADD", "register:40f0:8", ["const:4963fc:8", "const:4:8"]]
- 004963fc ["CALL", null, ["callee:00c58010:8"]]
+ 0049643c ["INT_ADD", "register:40f0:8", ["const:49643c:8", "const:4:8"]]
+ 0049643c ["CALL", null, ["callee:00c58010:8"]]
- 004963fc bytes d1061f94
+ 0049643c bytes f5061f94
- 00496434 ["INT_ADD", "register:40f0:8", ["const:496434:8", "const:4:8"]]
- 00496434 ["CALL", null, ["callee:00c57f60:8"]]
+ 00496474 ["INT_ADD", "register:40f0:8", ["const:496474:8", "const:4:8"]]
+ 00496474 ["CALL", null, ["callee:00c57f60:8"]]
- 00496434 bytes 97061f94
+ 00496474 bytes bb061f94
- 004964e4 ["INT_ADD", "register:40f0:8", ["const:4964e4:8", "const:4:8"]]
- 004964e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00496524 ["INT_ADD", "register:40f0:8", ["const:496524:8", "const:4:8"]]
+ 00496524 ["CALL", null, ["callee:00c57f80:8"]]
- 004964e4 bytes 73061f94
+ 00496524 bytes 97061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e3611b054f671886ddf542515fb93f"></a>

### [`00496518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md) → [`00496558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md) FUN_00496558

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md#insn-00496588) · [`004965c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md#insn-004965c0) · [`00496670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496518.md#insn-00496670)
- 新版 [`004965c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-004965c8) · [`00496600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-00496600) · [`004966b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-004966b0)

~~~diff
- 00496588 ["INT_ADD", "register:40f0:8", ["const:496588:8", "const:4:8"]]
- 00496588 ["CALL", null, ["callee:00c58010:8"]]
+ 004965c8 ["INT_ADD", "register:40f0:8", ["const:4965c8:8", "const:4:8"]]
+ 004965c8 ["CALL", null, ["callee:00c58010:8"]]
- 00496588 bytes 6e061f94
+ 004965c8 bytes 92061f94
- 004965c0 ["INT_ADD", "register:40f0:8", ["const:4965c0:8", "const:4:8"]]
- 004965c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00496600 ["INT_ADD", "register:40f0:8", ["const:496600:8", "const:4:8"]]
+ 00496600 ["CALL", null, ["callee:00c57f60:8"]]
- 004965c0 bytes 34061f94
+ 00496600 bytes 58061f94
- 00496670 ["INT_ADD", "register:40f0:8", ["const:496670:8", "const:4:8"]]
- 00496670 ["CALL", null, ["callee:00c57f80:8"]]
+ 004966b0 ["INT_ADD", "register:40f0:8", ["const:4966b0:8", "const:4:8"]]
+ 004966b0 ["CALL", null, ["callee:00c57f80:8"]]
- 00496670 bytes 10061f94
+ 004966b0 bytes 34061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a793657586deca41528514739e34f0e5"></a>

### [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) → [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) FUN_00496eb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004974f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md) [`004975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md) [`0049763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md#insn-00496e88)
- 新版 [`00496ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md#insn-00496ec8)

~~~diff
- 00496e88 ["INT_ADD", "register:40f0:8", ["const:496e88:8", "const:4:8"]]
- 00496e88 ["CALL", null, ["callee:00497538:8"]]
+ 00496ec8 ["INT_ADD", "register:40f0:8", ["const:496ec8:8", "const:4:8"]]
+ 00496ec8 ["CALL", null, ["callee:00497538:8"]]
- 00496e88 bytes 9c010094
+ 00496ec8 bytes 9c010094
~~~


<a id="compare-77f056c75d0fff5849d1406434c4ce8c"></a>

### [`00496eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496eb8.md) → [`00496ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496ef8.md) FUN_00496ef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496eb8.md#insn-00496ecc)
- 新版 [`00496f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496ef8.md#insn-00496f0c)

~~~diff
- 00496ecc ["INT_ADD", "register:40f0:8", ["const:496ecc:8", "const:4:8"]]
- 00496ecc ["CALL", null, ["callee:004410cc:8"]]
+ 00496f0c ["INT_ADD", "register:40f0:8", ["const:496f0c:8", "const:4:8"]]
+ 00496f0c ["CALL", null, ["callee:004410cc:8"]]
- 00496ecc bytes 70a8fe97
+ 00496f0c bytes 70a8fe97
~~~


<a id="compare-4c8e0d8cd0f5d2c5a312ab1bf7f04ba4"></a>

### [`00496f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f04.md) → [`00496f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f44.md) FUN_00496f44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f04.md#insn-00496f18)
- 新版 [`00496f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f44.md#insn-00496f58)

~~~diff
- 00496f18 ["INT_ADD", "register:40f0:8", ["const:496f18:8", "const:4:8"]]
- 00496f18 ["CALL", null, ["callee:004410cc:8"]]
+ 00496f58 ["INT_ADD", "register:40f0:8", ["const:496f58:8", "const:4:8"]]
+ 00496f58 ["CALL", null, ["callee:004410cc:8"]]
- 00496f18 bytes 5da8fe97
+ 00496f58 bytes 5da8fe97
~~~


<a id="compare-5379dbd7024c14b4d29d8a80dfe133b3"></a>

### [`00496f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f50.md) → [`00496f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f90.md) FUN_00496f90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f50.md#insn-00496f64)
- 新版 [`00496fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f90.md#insn-00496fa4)

~~~diff
- 00496f64 ["INT_ADD", "register:40f0:8", ["const:496f64:8", "const:4:8"]]
- 00496f64 ["CALL", null, ["callee:004410cc:8"]]
+ 00496fa4 ["INT_ADD", "register:40f0:8", ["const:496fa4:8", "const:4:8"]]
+ 00496fa4 ["CALL", null, ["callee:004410cc:8"]]
- 00496f64 bytes 4aa8fe97
+ 00496fa4 bytes 4aa8fe97
~~~


<a id="compare-7dfd69a8c52d8b88104c847cf0d05d38"></a>

### [`00496f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f9c.md) → [`00496fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md) FUN_00496fdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f9c.md#insn-00496fb0) · [`00496fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496f9c.md#insn-00496fcc)
- 新版 [`00496ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md#insn-00496ff0) · [`0049700c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md#insn-0049700c)

~~~diff
- 00496fb0 ["INT_ADD", "register:40f0:8", ["const:496fb0:8", "const:4:8"]]
- 00496fb0 ["CALL", null, ["callee:004410cc:8"]]
+ 00496ff0 ["INT_ADD", "register:40f0:8", ["const:496ff0:8", "const:4:8"]]
+ 00496ff0 ["CALL", null, ["callee:004410cc:8"]]
- 00496fb0 bytes 37a8fe97
+ 00496ff0 bytes 37a8fe97
- 00496fcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00496fcc ["INT_ADD", "register:40f0:8", ["const:496fcc:8", "const:4:8"]]
- 00496fcc ["CALLIND", null, ["register:0:8"]]
+ 0049700c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049700c ["INT_ADD", "register:40f0:8", ["const:49700c:8", "const:4:8"]]
+ 0049700c ["CALLIND", null, ["register:0:8"]]
- 00496fcc bytes 00013fd6
+ 0049700c bytes 00013fd6
~~~


<a id="compare-3c10cfa0ef1bad03381eb416607a555d"></a>

### [`00496fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496fe4.md) → [`00497024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497024.md) FUN_00497024

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496fe4.md#insn-00496ffc)
- 新版 [`0049703c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497024.md#insn-0049703c)

~~~diff
- 00496ffc ["INT_ADD", "register:40f0:8", ["const:496ffc:8", "const:4:8"]]
- 00496ffc ["CALL", null, ["callee:004410cc:8"]]
+ 0049703c ["INT_ADD", "register:40f0:8", ["const:49703c:8", "const:4:8"]]
+ 0049703c ["CALL", null, ["callee:004410cc:8"]]
- 00496ffc bytes 24a8fe97
+ 0049703c bytes 24a8fe97
~~~


<a id="compare-1c726ee781549f0002c25abf6cba7311"></a>

### [`004974f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md) → [`00497538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md) FUN_00497538

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md#insn-00497564) · [`004975c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004974f8.md#insn-004975c0)
- 新版 [`004975a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md#insn-004975a4) · [`00497600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md#insn-00497600)

~~~diff
- 00497564 ["INT_ADD", "register:40f0:8", ["const:497564:8", "const:4:8"]]
- 00497564 ["CALL", null, ["callee:00c58120:8"]]
+ 004975a4 ["INT_ADD", "register:40f0:8", ["const:4975a4:8", "const:4:8"]]
+ 004975a4 ["CALL", null, ["callee:00c58120:8"]]
- 00497564 bytes bb021f94
+ 004975a4 bytes df021f94
- 004975c0 ["INT_ADD", "register:40f0:8", ["const:4975c0:8", "const:4:8"]]
- 004975c0 ["CALL", null, ["callee:00c58120:8"]]
+ 00497600 ["INT_ADD", "register:40f0:8", ["const:497600:8", "const:4:8"]]
+ 00497600 ["CALL", null, ["callee:00c58120:8"]]
- 004975c0 bytes a4021f94
+ 00497600 bytes c8021f94
~~~


<a id="compare-c0b0077b0d6a7e225439240a5b2a4570"></a>

### [`004975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md) → [`0049763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md) FUN_0049763c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00496e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496e74.md) · 呼出先 2件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md#insn-00497660) · [`00497678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md#insn-00497678) · [`00497688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004975fc.md#insn-00497688)
- 新版 [`004976a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976a0) · [`004976b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976b8) · [`004976c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976c8)

~~~diff
- 00497660 ["INT_ADD", "register:40f0:8", ["const:497660:8", "const:4:8"]]
- 00497660 ["CALL", null, ["callee:00494650:8"]]
+ 004976a0 ["INT_ADD", "register:40f0:8", ["const:4976a0:8", "const:4:8"]]
+ 004976a0 ["CALL", null, ["callee:00494650:8"]]
- 00497660 bytes ecf3ff97
+ 004976a0 bytes ecf3ff97
- 00497678 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497678 ["INT_ADD", "register:40f0:8", ["const:497678:8", "const:4:8"]]
- 00497678 ["CALLIND", null, ["register:0:8"]]
+ 004976b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004976b8 ["INT_ADD", "register:40f0:8", ["const:4976b8:8", "const:4:8"]]
+ 004976b8 ["CALLIND", null, ["register:0:8"]]
- 00497678 bytes 00013fd6
+ 004976b8 bytes 00013fd6
- 00497688 ["INT_ADD", "register:40f0:8", ["const:497688:8", "const:4:8"]]
- 00497688 ["CALL", null, ["callee:00c57f80:8"]]
+ 004976c8 ["INT_ADD", "register:40f0:8", ["const:4976c8:8", "const:4:8"]]
+ 004976c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00497688 bytes 0a021f94
+ 004976c8 bytes 2e021f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7568b4b0fdf425f10d5d171aad32655"></a>

### [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) → [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) FUN_00497874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 135件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`00578910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md) [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) [`0057f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 135件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00578950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md) [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) [`0057f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004978a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md#insn-004978a8) · [`004978cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md#insn-004978cc)
- 新版 [`004978e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md#insn-004978e8) · [`0049790c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md#insn-0049790c)

~~~diff
- 004978a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004978a8 ["INT_ADD", "register:40f0:8", ["const:4978a8:8", "const:4:8"]]
- 004978a8 ["CALLIND", null, ["register:0:8"]]
+ 004978e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004978e8 ["INT_ADD", "register:40f0:8", ["const:4978e8:8", "const:4:8"]]
+ 004978e8 ["CALLIND", null, ["register:0:8"]]
- 004978a8 bytes 00013fd6
+ 004978e8 bytes 00013fd6
- 004978cc ["INT_ADD", "register:40f0:8", ["const:4978cc:8", "const:4:8"]]
- 004978cc ["CALL", null, ["callee:00c57fb0:8"]]
+ 0049790c ["INT_ADD", "register:40f0:8", ["const:49790c:8", "const:4:8"]]
+ 0049790c ["CALL", null, ["callee:00c57fb0:8"]]
- 004978cc bytes 85011f94
+ 0049790c bytes a9011f94
~~~


<a id="compare-5763098ded73caaccc081652ba7a2fdd"></a>

### [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) → [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) FUN_00497a88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 46件 [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) [`005729e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005729e4.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 46件 [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) [`00572a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md#insn-00497abc) · [`00497ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md#insn-00497ae0)
- 新版 [`00497afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md#insn-00497afc) · [`00497b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md#insn-00497b20)

~~~diff
- 00497abc ["COPY", "register:0:8", ["register:4040:8"]]
- 00497abc ["INT_ADD", "register:40f0:8", ["const:497abc:8", "const:4:8"]]
- 00497abc ["CALLIND", null, ["register:0:8"]]
+ 00497afc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497afc ["INT_ADD", "register:40f0:8", ["const:497afc:8", "const:4:8"]]
+ 00497afc ["CALLIND", null, ["register:0:8"]]
- 00497abc bytes 00013fd6
+ 00497afc bytes 00013fd6
- 00497ae0 ["INT_ADD", "register:40f0:8", ["const:497ae0:8", "const:4:8"]]
- 00497ae0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00497b20 ["INT_ADD", "register:40f0:8", ["const:497b20:8", "const:4:8"]]
+ 00497b20 ["CALL", null, ["callee:00c57fb0:8"]]
- 00497ae0 bytes 00011f94
+ 00497b20 bytes 24011f94
~~~


<a id="compare-bb27c6ea0a93e5977530d920bb42be83"></a>

### [`00497bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497bdc.md) → [`00497c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md) FUN_00497c1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497bdc.md#insn-00497bf8) · [`00497c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497bdc.md#insn-00497c18)
- 新版 [`00497c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md#insn-00497c38) · [`00497c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md#insn-00497c58)

~~~diff
- 00497bf8 ["INT_ADD", "register:40f0:8", ["const:497bf8:8", "const:4:8"]]
- 00497bf8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00497c38 ["INT_ADD", "register:40f0:8", ["const:497c38:8", "const:4:8"]]
+ 00497c38 ["CALL", null, ["callee:00c53da0:8"]]
- 00497bf8 bytes 42f01e94
+ 00497c38 bytes 5af01e94
- 00497c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497c18 ["INT_ADD", "register:40f0:8", ["const:497c18:8", "const:4:8"]]
- 00497c18 ["CALLIND", null, ["register:0:8"]]
+ 00497c58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497c58 ["INT_ADD", "register:40f0:8", ["const:497c58:8", "const:4:8"]]
+ 00497c58 ["CALLIND", null, ["register:0:8"]]
- 00497c18 bytes 00013fd6
+ 00497c58 bytes 00013fd6
~~~


<a id="compare-79bca9df5a7bcbd363264da5423575f3"></a>

### [`00497c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c2c.md) → [`00497c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md) FUN_00497c6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c2c.md#insn-00497c48) · [`00497c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c2c.md#insn-00497c68)
- 新版 [`00497c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md#insn-00497c88) · [`00497ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md#insn-00497ca8)

~~~diff
- 00497c48 ["INT_ADD", "register:40f0:8", ["const:497c48:8", "const:4:8"]]
- 00497c48 ["CALL", null, ["callee:00c53da0:8"]]
+ 00497c88 ["INT_ADD", "register:40f0:8", ["const:497c88:8", "const:4:8"]]
+ 00497c88 ["CALL", null, ["callee:00c53da0:8"]]
- 00497c48 bytes 2ef01e94
+ 00497c88 bytes 46f01e94
- 00497c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497c68 ["INT_ADD", "register:40f0:8", ["const:497c68:8", "const:4:8"]]
- 00497c68 ["CALLIND", null, ["register:0:8"]]
+ 00497ca8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497ca8 ["INT_ADD", "register:40f0:8", ["const:497ca8:8", "const:4:8"]]
+ 00497ca8 ["CALLIND", null, ["register:0:8"]]
- 00497c68 bytes 00013fd6
+ 00497ca8 bytes 00013fd6
~~~


<a id="compare-0f05648c4c1ba656f899a2198af4f964"></a>

### [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) → [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) FUN_00498114

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) [`00497df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md) [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) · 呼出先 4件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 3件 [`00497cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md) [`00497e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md) [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) · 呼出先 4件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004980f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md#insn-004980f0) · [`00498128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md#insn-00498128) · [`00498174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md#insn-00498174)
- 新版 [`00498130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-00498130) · [`00498168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-00498168) · [`004981b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-004981b4)

~~~diff
- 004980f0 ["INT_ADD", "register:40f0:8", ["const:4980f0:8", "const:4:8"]]
- 004980f0 ["CALL", null, ["callee:00c581b0:8"]]
+ 00498130 ["INT_ADD", "register:40f0:8", ["const:498130:8", "const:4:8"]]
+ 00498130 ["CALL", null, ["callee:00c581b0:8"]]
- 004980f0 bytes fcff1e94
+ 00498130 bytes 20001f94
- 00498128 ["INT_ADD", "register:40f0:8", ["const:498128:8", "const:4:8"]]
- 00498128 ["CALL", null, ["callee:004997dc:8"]]
+ 00498168 ["INT_ADD", "register:40f0:8", ["const:498168:8", "const:4:8"]]
+ 00498168 ["CALL", null, ["callee:004997dc:8"]]
- 00498128 bytes 9d050094
+ 00498168 bytes 9d050094
- 00498174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498174 ["INT_ADD", "register:40f0:8", ["const:498174:8", "const:4:8"]]
- 00498174 ["CALLIND", null, ["register:0:8"]]
+ 004981b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004981b4 ["INT_ADD", "register:40f0:8", ["const:4981b4:8", "const:4:8"]]
+ 004981b4 ["CALLIND", null, ["register:0:8"]]
- 00498174 bytes 00013fd6
+ 004981b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81740bf2aefdabf2dfe08b4fe5dd7108"></a>

### [`004985e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md) → [`00498620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md) FUN_00498620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) · 呼出先 4件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) · 呼出先 4件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004985fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md#insn-004985fc) · [`00498634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md#insn-00498634) · [`00498684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md#insn-00498684)
- 新版 [`0049863c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-0049863c) · [`00498674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-00498674) · [`004986c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-004986c4)

~~~diff
- 004985fc ["INT_ADD", "register:40f0:8", ["const:4985fc:8", "const:4:8"]]
- 004985fc ["CALL", null, ["callee:00c581b0:8"]]
+ 0049863c ["INT_ADD", "register:40f0:8", ["const:49863c:8", "const:4:8"]]
+ 0049863c ["CALL", null, ["callee:00c581b0:8"]]
- 004985fc bytes b9fe1e94
+ 0049863c bytes ddfe1e94
- 00498634 ["INT_ADD", "register:40f0:8", ["const:498634:8", "const:4:8"]]
- 00498634 ["CALL", null, ["callee:0049a2e4:8"]]
+ 00498674 ["INT_ADD", "register:40f0:8", ["const:498674:8", "const:4:8"]]
+ 00498674 ["CALL", null, ["callee:0049a2e4:8"]]
- 00498634 bytes 1c070094
+ 00498674 bytes 1c070094
- 00498684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498684 ["INT_ADD", "register:40f0:8", ["const:498684:8", "const:4:8"]]
- 00498684 ["CALLIND", null, ["register:0:8"]]
+ 004986c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004986c4 ["INT_ADD", "register:40f0:8", ["const:4986c4:8", "const:4:8"]]
+ 004986c4 ["CALLIND", null, ["register:0:8"]]
- 00498684 bytes 00013fd6
+ 004986c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40a8277ec6f5bf2430a47fbc06b51b2b"></a>

### [`00498804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md) → [`00498844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md) FUN_00498844

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 22件 [`0067fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067fdac.md) [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`006b5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b5/006b5404.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 22件 [`0067fdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067f/0067fdec.md) [`00680e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00680/00680e48.md) [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) [`006b545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b5/006b545c.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 2件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md#insn-00498830) · [`0049883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md#insn-0049883c) · [`00498854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md#insn-00498854)
- 新版 [`00498870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-00498870) · [`0049887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-0049887c) · [`00498894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-00498894)

~~~diff
- 00498830 ["INT_ADD", "register:40f0:8", ["const:498830:8", "const:4:8"]]
- 00498830 ["CALL", null, ["callee:00c581b0:8"]]
+ 00498870 ["INT_ADD", "register:40f0:8", ["const:498870:8", "const:4:8"]]
+ 00498870 ["CALL", null, ["callee:00c581b0:8"]]
- 00498830 bytes 2cfe1e94
+ 00498870 bytes 50fe1e94
- 0049883c ["INT_ADD", "register:40f0:8", ["const:49883c:8", "const:4:8"]]
- 0049883c ["CALL", null, ["callee:00c581c0:8"]]
+ 0049887c ["INT_ADD", "register:40f0:8", ["const:49887c:8", "const:4:8"]]
+ 0049887c ["CALL", null, ["callee:00c581c0:8"]]
- 0049883c bytes 2dfe1e94
+ 0049887c bytes 51fe1e94
- 00498854 ["INT_ADD", "register:40f0:8", ["const:498854:8", "const:4:8"]]
- 00498854 ["CALL", null, ["callee:00c581b0:8"]]
+ 00498894 ["INT_ADD", "register:40f0:8", ["const:498894:8", "const:4:8"]]
+ 00498894 ["CALL", null, ["callee:00c581b0:8"]]
- 00498854 bytes 23fe1e94
+ 00498894 bytes 47fe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9d559c004c03206cf073353880b8063"></a>

### [`0049887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md) → [`004988bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md) FUN_004988bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086b354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b354.md) [`0086b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b56c.md) · 呼出先 2件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 2件 [`0086b3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b3ac.md) [`0086b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b5c4.md) · 呼出先 2件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049889c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md#insn-0049889c) · [`004988a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md#insn-004988a8) · [`004988b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md#insn-004988b8)
- 新版 [`004988dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988dc) · [`004988e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988e8) · [`004988f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988f8)

~~~diff
- 0049889c ["INT_ADD", "register:40f0:8", ["const:49889c:8", "const:4:8"]]
- 0049889c ["CALL", null, ["callee:00c581b0:8"]]
+ 004988dc ["INT_ADD", "register:40f0:8", ["const:4988dc:8", "const:4:8"]]
+ 004988dc ["CALL", null, ["callee:00c581b0:8"]]
- 0049889c bytes 11fe1e94
+ 004988dc bytes 35fe1e94
- 004988a8 ["INT_ADD", "register:40f0:8", ["const:4988a8:8", "const:4:8"]]
- 004988a8 ["CALL", null, ["callee:00c581c0:8"]]
+ 004988e8 ["INT_ADD", "register:40f0:8", ["const:4988e8:8", "const:4:8"]]
+ 004988e8 ["CALL", null, ["callee:00c581c0:8"]]
- 004988a8 bytes 12fe1e94
+ 004988e8 bytes 36fe1e94
- 004988b8 ["INT_ADD", "register:40f0:8", ["const:4988b8:8", "const:4:8"]]
- 004988b8 ["CALL", null, ["callee:00c581b0:8"]]
+ 004988f8 ["INT_ADD", "register:40f0:8", ["const:4988f8:8", "const:4:8"]]
+ 004988f8 ["CALL", null, ["callee:00c581b0:8"]]
- 004988b8 bytes 0afe1e94
+ 004988f8 bytes 2efe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82a37f98ecb66bc698b5fa0713b10f8c"></a>

### [`0049891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md) → [`0049895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md) FUN_0049895c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md#insn-00498930) · [`00498938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md#insn-00498938)
- 新版 [`00498970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md#insn-00498970) · [`00498978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md#insn-00498978)

~~~diff
- 00498930 ["INT_ADD", "register:40f0:8", ["const:498930:8", "const:4:8"]]
- 00498930 ["CALL", null, ["callee:00c581a0:8"]]
+ 00498970 ["INT_ADD", "register:40f0:8", ["const:498970:8", "const:4:8"]]
+ 00498970 ["CALL", null, ["callee:00c581a0:8"]]
- 00498930 bytes e8fd1e94
+ 00498970 bytes 0cfe1e94
- 00498938 ["INT_ADD", "register:40f0:8", ["const:498938:8", "const:4:8"]]
- 00498938 ["CALL", null, ["callee:00c57f30:8"]]
+ 00498978 ["INT_ADD", "register:40f0:8", ["const:498978:8", "const:4:8"]]
+ 00498978 ["CALL", null, ["callee:00c57f30:8"]]
- 00498938 bytes 4afd1e94
+ 00498978 bytes 6efd1e94
~~~


<a id="compare-faa7c3dfb88dccd448135a3847aaa7e0"></a>

### [`00498950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md) → [`00498990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md) FUN_00498990

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049891c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004989f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md#insn-004989f0) · [`00498a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md#insn-00498a3c) · [`00498a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498950.md#insn-00498a88)
- 新版 [`00498a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498a30) · [`00498a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498a7c) · [`00498ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498ac8)

~~~diff
- 004989f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004989f0 ["INT_ADD", "register:40f0:8", ["const:4989f0:8", "const:4:8"]]
- 004989f0 ["CALLIND", null, ["register:0:8"]]
+ 00498a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498a30 ["INT_ADD", "register:40f0:8", ["const:498a30:8", "const:4:8"]]
+ 00498a30 ["CALLIND", null, ["register:0:8"]]
- 004989f0 bytes 00013fd6
+ 00498a30 bytes 00013fd6
- 00498a3c ["INT_ADD", "register:40f0:8", ["const:498a3c:8", "const:4:8"]]
- 00498a3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00498a7c ["INT_ADD", "register:40f0:8", ["const:498a7c:8", "const:4:8"]]
+ 00498a7c ["CALL", null, ["callee:00c57f80:8"]]
- 00498a3c bytes 1dfd1e94
+ 00498a7c bytes 41fd1e94
- 00498a88 ["INT_ADD", "register:40f0:8", ["const:498a88:8", "const:4:8"]]
- 00498a88 ["CALL", null, ["callee:00c57f80:8"]]
+ 00498ac8 ["INT_ADD", "register:40f0:8", ["const:498ac8:8", "const:4:8"]]
+ 00498ac8 ["CALL", null, ["callee:00c57f80:8"]]
- 00498a88 bytes 0afd1e94
+ 00498ac8 bytes 2efd1e94
~~~


<a id="compare-1b6dcf4b74db1cae4b7bb44f0ba48ea6"></a>

### [`00498b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md) → [`00498b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md) FUN_00498b6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md#insn-00498b40) · [`00498b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md#insn-00498b48)
- 新版 [`00498b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md#insn-00498b80) · [`00498b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md#insn-00498b88)

~~~diff
- 00498b40 ["INT_ADD", "register:40f0:8", ["const:498b40:8", "const:4:8"]]
- 00498b40 ["CALL", null, ["callee:00c581a0:8"]]
+ 00498b80 ["INT_ADD", "register:40f0:8", ["const:498b80:8", "const:4:8"]]
+ 00498b80 ["CALL", null, ["callee:00c581a0:8"]]
- 00498b40 bytes 64fd1e94
+ 00498b80 bytes 88fd1e94
- 00498b48 ["INT_ADD", "register:40f0:8", ["const:498b48:8", "const:4:8"]]
- 00498b48 ["CALL", null, ["callee:00c57f30:8"]]
+ 00498b88 ["INT_ADD", "register:40f0:8", ["const:498b88:8", "const:4:8"]]
+ 00498b88 ["CALL", null, ["callee:00c57f30:8"]]
- 00498b48 bytes c6fc1e94
+ 00498b88 bytes eafc1e94
~~~


<a id="compare-902587b855461a548ce9e5404218fbdc"></a>

### [`00498b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md) → [`00498ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md) FUN_00498ba0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00498b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md#insn-00498c00) · [`00498c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md#insn-00498c4c) · [`00498c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498b60.md#insn-00498c98)
- 新版 [`00498c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498c40) · [`00498c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498c8c) · [`00498cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498cd8)

~~~diff
- 00498c00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498c00 ["INT_ADD", "register:40f0:8", ["const:498c00:8", "const:4:8"]]
- 00498c00 ["CALLIND", null, ["register:0:8"]]
+ 00498c40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498c40 ["INT_ADD", "register:40f0:8", ["const:498c40:8", "const:4:8"]]
+ 00498c40 ["CALLIND", null, ["register:0:8"]]
- 00498c00 bytes 00013fd6
+ 00498c40 bytes 00013fd6
- 00498c4c ["INT_ADD", "register:40f0:8", ["const:498c4c:8", "const:4:8"]]
- 00498c4c ["CALL", null, ["callee:00c57f80:8"]]
+ 00498c8c ["INT_ADD", "register:40f0:8", ["const:498c8c:8", "const:4:8"]]
+ 00498c8c ["CALL", null, ["callee:00c57f80:8"]]
- 00498c4c bytes 99fc1e94
+ 00498c8c bytes bdfc1e94
- 00498c98 ["INT_ADD", "register:40f0:8", ["const:498c98:8", "const:4:8"]]
- 00498c98 ["CALL", null, ["callee:00c57f80:8"]]
+ 00498cd8 ["INT_ADD", "register:40f0:8", ["const:498cd8:8", "const:4:8"]]
+ 00498cd8 ["CALL", null, ["callee:00c57f80:8"]]
- 00498c98 bytes 86fc1e94
+ 00498cd8 bytes aafc1e94
~~~


<a id="compare-9c5438efa6ba88233669230959e20c83"></a>

### [`00499214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499214.md) → [`00499254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md) FUN_00499254

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499214.md#insn-00499264) · [`00499278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499214.md#insn-00499278) · [`00499280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499214.md#insn-00499280)
- 新版 [`004992a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992a4) · [`004992b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992b8) · [`004992c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992c0)

~~~diff
- 00499264 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499264 ["INT_ADD", "register:40f0:8", ["const:499264:8", "const:4:8"]]
- 00499264 ["CALLIND", null, ["register:0:8"]]
+ 004992a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004992a4 ["INT_ADD", "register:40f0:8", ["const:4992a4:8", "const:4:8"]]
+ 004992a4 ["CALLIND", null, ["register:0:8"]]
- 00499264 bytes 00013fd6
+ 004992a4 bytes 00013fd6
- 00499278 ["INT_ADD", "register:40f0:8", ["const:499278:8", "const:4:8"]]
- 00499278 ["CALL", null, ["callee:00c58220:8"]]
+ 004992b8 ["INT_ADD", "register:40f0:8", ["const:4992b8:8", "const:4:8"]]
+ 004992b8 ["CALL", null, ["callee:00c58220:8"]]
- 00499278 bytes b6fb1e94
+ 004992b8 bytes dafb1e94
- 00499280 ["INT_ADD", "register:40f0:8", ["const:499280:8", "const:4:8"]]
- 00499280 ["CALL", null, ["callee:00c57f80:8"]]
+ 004992c0 ["INT_ADD", "register:40f0:8", ["const:4992c0:8", "const:4:8"]]
+ 004992c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00499280 bytes 0cfb1e94
+ 004992c0 bytes 30fb1e94
~~~


<a id="compare-eac455f1d7fa13ac75ddf969070da7d2"></a>

### [`00499294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499294.md) → [`004992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004992d4.md) FUN_004992d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004992b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499294.md#insn-004992b0)
- 新版 [`004992f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004992d4.md#insn-004992f0)

~~~diff
- 004992b0 ["INT_ADD", "register:40f0:8", ["const:4992b0:8", "const:4:8"]]
- 004992b0 ["CALL", null, ["callee:00c58220:8"]]
+ 004992f0 ["INT_ADD", "register:40f0:8", ["const:4992f0:8", "const:4:8"]]
+ 004992f0 ["CALL", null, ["callee:00c58220:8"]]
- 004992b0 bytes a8fb1e94
+ 004992f0 bytes ccfb1e94
~~~


<a id="compare-bd6591bc14f17df8f163e114c87e4d43"></a>

### [`004992d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md) → [`00499310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md) FUN_00499310

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) · 呼出先 4件 [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) · 呼出先 4件 [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md#insn-00499344) · [`0049936c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md#insn-0049936c) · [`0049937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md#insn-0049937c)
- 新版 [`00499384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-00499384) · [`004993ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-004993ac) · [`004993bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-004993bc)

~~~diff
- 00499344 ["COPY", "register:0:8", ["register:4048:8"]]
- 00499344 ["INT_ADD", "register:40f0:8", ["const:499344:8", "const:4:8"]]
- 00499344 ["CALLIND", null, ["register:0:8"]]
+ 00499384 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00499384 ["INT_ADD", "register:40f0:8", ["const:499384:8", "const:4:8"]]
+ 00499384 ["CALLIND", null, ["register:0:8"]]
- 00499344 bytes 20013fd6
+ 00499384 bytes 20013fd6
- 0049936c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049936c ["INT_ADD", "register:40f0:8", ["const:49936c:8", "const:4:8"]]
- 0049936c ["CALLIND", null, ["register:0:8"]]
+ 004993ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004993ac ["INT_ADD", "register:40f0:8", ["const:4993ac:8", "const:4:8"]]
+ 004993ac ["CALLIND", null, ["register:0:8"]]
- 0049936c bytes 00013fd6
+ 004993ac bytes 00013fd6
- 0049937c ["INT_ADD", "register:40f0:8", ["const:49937c:8", "const:4:8"]]
- 0049937c ["CALL", null, ["callee:004994b0:8"]]
+ 004993bc ["INT_ADD", "register:40f0:8", ["const:4993bc:8", "const:4:8"]]
+ 004993bc ["CALL", null, ["callee:004994b0:8"]]
- 0049937c bytes 3d000094
+ 004993bc bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb85505dd9832b4efb5708b7cce51d5b"></a>

### [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) → [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) FUN_004994b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) [`004992d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md) [`0049a0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) [`00499310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md) [`0049a13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004994dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md#insn-004994dc) · [`004994ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md#insn-004994ec) · [`0049950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md#insn-0049950c)
- 新版 [`0049951c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049951c) · [`0049952c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049952c) · [`0049954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049954c)

~~~diff
- 004994dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004994dc ["INT_ADD", "register:40f0:8", ["const:4994dc:8", "const:4:8"]]
- 004994dc ["CALLIND", null, ["register:0:8"]]
+ 0049951c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049951c ["INT_ADD", "register:40f0:8", ["const:49951c:8", "const:4:8"]]
+ 0049951c ["CALLIND", null, ["register:0:8"]]
- 004994dc bytes 00013fd6
+ 0049951c bytes 00013fd6
- 004994ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004994ec ["INT_ADD", "register:40f0:8", ["const:4994ec:8", "const:4:8"]]
- 004994ec ["CALLIND", null, ["register:0:8"]]
+ 0049952c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049952c ["INT_ADD", "register:40f0:8", ["const:49952c:8", "const:4:8"]]
+ 0049952c ["CALLIND", null, ["register:0:8"]]
- 004994ec bytes 00013fd6
+ 0049952c bytes 00013fd6
- 0049950c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049950c ["INT_ADD", "register:40f0:8", ["const:49950c:8", "const:4:8"]]
- 0049950c ["CALLIND", null, ["register:0:8"]]
+ 0049954c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049954c ["INT_ADD", "register:40f0:8", ["const:49954c:8", "const:4:8"]]
+ 0049954c ["CALLIND", null, ["register:0:8"]]
- 0049950c bytes 00013fd6
+ 0049954c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86cc8928de3397c781a810703e99795c"></a>

### [`00499644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499644.md) → [`00499684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md) FUN_00499684

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499644.md#insn-00499688) · [`004996bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499644.md#insn-004996bc) · [`004996c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499644.md#insn-004996c0)
- 新版 [`004996c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-004996c8) · [`004996fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-004996fc) · [`00499700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-00499700)

~~~diff
- 00499688 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499688 ["INT_ADD", "register:40f0:8", ["const:499688:8", "const:4:8"]]
- 00499688 ["CALLIND", null, ["register:0:8"]]
+ 004996c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004996c8 ["INT_ADD", "register:40f0:8", ["const:4996c8:8", "const:4:8"]]
+ 004996c8 ["CALLIND", null, ["register:0:8"]]
- 00499688 bytes 00013fd6
+ 004996c8 bytes 00013fd6
- 004996bc ["INT_ADD", "register:40f0:8", ["const:4996bc:8", "const:4:8"]]
- 004996bc ["CALL", null, ["callee:00459db4:8"]]
+ 004996fc ["INT_ADD", "register:40f0:8", ["const:4996fc:8", "const:4:8"]]
+ 004996fc ["CALL", null, ["callee:00459db4:8"]]
- 004996bc bytes ae01ff97
+ 004996fc bytes ae01ff97
- 004996c0 ["INT_ADD", "register:40f0:8", ["const:4996c0:8", "const:4:8"]]
- 004996c0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00499700 ["INT_ADD", "register:40f0:8", ["const:499700:8", "const:4:8"]]
+ 00499700 ["CALL", null, ["callee:00c57fb0:8"]]
- 004996c0 bytes 08fa1e94
+ 00499700 bytes 2cfa1e94
~~~


<a id="compare-8dc7f882485cc5be14e2cf025f0c4f0c"></a>

### [`00499748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499748.md) → [`00499788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499788.md) FUN_00499788

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499748.md#insn-00499770)
- 新版 [`004997b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499788.md#insn-004997b0)

~~~diff
- 00499770 ["INT_ADD", "register:40f0:8", ["const:499770:8", "const:4:8"]]
- 00499770 ["CALL", null, ["callee:00459db4:8"]]
+ 004997b0 ["INT_ADD", "register:40f0:8", ["const:4997b0:8", "const:4:8"]]
+ 004997b0 ["CALL", null, ["callee:00459db4:8"]]
- 00499770 bytes 8101ff97
+ 004997b0 bytes 8101ff97
~~~


<a id="compare-6a44b99f4f091f544909970cd041a9ba"></a>

### [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) → [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) FUN_004997dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00499c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md) [`00499de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md) [`00499f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00499c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md) [`00499e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md) [`00499fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md#insn-00499834) · [`00499878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md#insn-00499878) · [`00499888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md#insn-00499888)
- 新版 [`00499874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-00499874) · [`004998b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-004998b8) · [`004998c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-004998c8)

~~~diff
- 00499834 ["INT_ADD", "register:40f0:8", ["const:499834:8", "const:4:8"]]
- 00499834 ["CALL", null, ["callee:00c58010:8"]]
+ 00499874 ["INT_ADD", "register:40f0:8", ["const:499874:8", "const:4:8"]]
+ 00499874 ["CALL", null, ["callee:00c58010:8"]]
- 00499834 bytes c3f91e94
+ 00499874 bytes e7f91e94
- 00499878 ["INT_ADD", "register:40f0:8", ["const:499878:8", "const:4:8"]]
- 00499878 ["CALL", null, ["callee:00c57f60:8"]]
+ 004998b8 ["INT_ADD", "register:40f0:8", ["const:4998b8:8", "const:4:8"]]
+ 004998b8 ["CALL", null, ["callee:00c57f60:8"]]
- 00499878 bytes 86f91e94
+ 004998b8 bytes aaf91e94
- 00499888 ["INT_ADD", "register:40f0:8", ["const:499888:8", "const:4:8"]]
- 00499888 ["CALL", null, ["callee:00499c9c:8"]]
+ 004998c8 ["INT_ADD", "register:40f0:8", ["const:4998c8:8", "const:4:8"]]
+ 004998c8 ["CALL", null, ["callee:00499c9c:8"]]
- 00499888 bytes f5000094
+ 004998c8 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a184a1d60febf9b1dffccf8b237bafd2"></a>

### [`00499c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md) → [`00499c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md) FUN_00499c9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md#insn-00499cc4) · [`00499cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md#insn-00499cfc) · [`00499dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499c5c.md#insn-00499dac)
- 新版 [`00499d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499d04) · [`00499d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499d3c) · [`00499dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499dec)

~~~diff
- 00499cc4 ["INT_ADD", "register:40f0:8", ["const:499cc4:8", "const:4:8"]]
- 00499cc4 ["CALL", null, ["callee:00c58010:8"]]
+ 00499d04 ["INT_ADD", "register:40f0:8", ["const:499d04:8", "const:4:8"]]
+ 00499d04 ["CALL", null, ["callee:00c58010:8"]]
- 00499cc4 bytes 9ff81e94
+ 00499d04 bytes c3f81e94
- 00499cfc ["INT_ADD", "register:40f0:8", ["const:499cfc:8", "const:4:8"]]
- 00499cfc ["CALL", null, ["callee:00c57f60:8"]]
+ 00499d3c ["INT_ADD", "register:40f0:8", ["const:499d3c:8", "const:4:8"]]
+ 00499d3c ["CALL", null, ["callee:00c57f60:8"]]
- 00499cfc bytes 65f81e94
+ 00499d3c bytes 89f81e94
- 00499dac ["INT_ADD", "register:40f0:8", ["const:499dac:8", "const:4:8"]]
- 00499dac ["CALL", null, ["callee:00c57f80:8"]]
+ 00499dec ["INT_ADD", "register:40f0:8", ["const:499dec:8", "const:4:8"]]
+ 00499dec ["CALL", null, ["callee:00c57f80:8"]]
- 00499dac bytes 41f81e94
+ 00499dec bytes 65f81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e38b6cb200a9d1b668b62e6034e6d8b"></a>

### [`00499de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md) → [`00499e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md) FUN_00499e24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md#insn-00499e54) · [`00499e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md#insn-00499e8c) · [`00499f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499de4.md#insn-00499f3c)
- 新版 [`00499e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499e94) · [`00499ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499ecc) · [`00499f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499f7c)

~~~diff
- 00499e54 ["INT_ADD", "register:40f0:8", ["const:499e54:8", "const:4:8"]]
- 00499e54 ["CALL", null, ["callee:00c58010:8"]]
+ 00499e94 ["INT_ADD", "register:40f0:8", ["const:499e94:8", "const:4:8"]]
+ 00499e94 ["CALL", null, ["callee:00c58010:8"]]
- 00499e54 bytes 3bf81e94
+ 00499e94 bytes 5ff81e94
- 00499e8c ["INT_ADD", "register:40f0:8", ["const:499e8c:8", "const:4:8"]]
- 00499e8c ["CALL", null, ["callee:00c57f60:8"]]
+ 00499ecc ["INT_ADD", "register:40f0:8", ["const:499ecc:8", "const:4:8"]]
+ 00499ecc ["CALL", null, ["callee:00c57f60:8"]]
- 00499e8c bytes 01f81e94
+ 00499ecc bytes 25f81e94
- 00499f3c ["INT_ADD", "register:40f0:8", ["const:499f3c:8", "const:4:8"]]
- 00499f3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00499f7c ["INT_ADD", "register:40f0:8", ["const:499f7c:8", "const:4:8"]]
+ 00499f7c ["CALL", null, ["callee:00c57f80:8"]]
- 00499f3c bytes ddf71e94
+ 00499f7c bytes 01f81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c21db6f49d69d4b270692d94abd4861"></a>

### [`00499f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md) → [`00499fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md) FUN_00499fb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049979c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049979c.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md#insn-00499fe0) · [`0049a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md#insn-0049a018) · [`0049a0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499f70.md#insn-0049a0c8)
- 新版 [`0049a020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a020) · [`0049a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a058) · [`0049a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a108)

~~~diff
- 00499fe0 ["INT_ADD", "register:40f0:8", ["const:499fe0:8", "const:4:8"]]
- 00499fe0 ["CALL", null, ["callee:00c58010:8"]]
+ 0049a020 ["INT_ADD", "register:40f0:8", ["const:49a020:8", "const:4:8"]]
+ 0049a020 ["CALL", null, ["callee:00c58010:8"]]
- 00499fe0 bytes d8f71e94
+ 0049a020 bytes fcf71e94
- 0049a018 ["INT_ADD", "register:40f0:8", ["const:49a018:8", "const:4:8"]]
- 0049a018 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049a058 ["INT_ADD", "register:40f0:8", ["const:49a058:8", "const:4:8"]]
+ 0049a058 ["CALL", null, ["callee:00c57f60:8"]]
- 0049a018 bytes 9ef71e94
+ 0049a058 bytes c2f71e94
- 0049a0c8 ["INT_ADD", "register:40f0:8", ["const:49a0c8:8", "const:4:8"]]
- 0049a0c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049a108 ["INT_ADD", "register:40f0:8", ["const:49a108:8", "const:4:8"]]
+ 0049a108 ["CALL", null, ["callee:00c57f80:8"]]
- 0049a0c8 bytes 7af71e94
+ 0049a108 bytes 9ef71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58226cafa1d30b94e2eeea631a9a0990"></a>

### [`0049a0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md) → [`0049a13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md) FUN_0049a13c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) · 呼出先 4件 [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) · 呼出先 4件 [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md#insn-0049a178) · [`0049a1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md#insn-0049a1a0) · [`0049a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a0fc.md#insn-0049a1b0)
- 新版 [`0049a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1b8) · [`0049a1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1e0) · [`0049a1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1f0)

~~~diff
- 0049a178 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049a178 ["INT_ADD", "register:40f0:8", ["const:49a178:8", "const:4:8"]]
- 0049a178 ["CALLIND", null, ["register:0:8"]]
+ 0049a1b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0049a1b8 ["INT_ADD", "register:40f0:8", ["const:49a1b8:8", "const:4:8"]]
+ 0049a1b8 ["CALLIND", null, ["register:0:8"]]
- 0049a178 bytes 20013fd6
+ 0049a1b8 bytes 20013fd6
- 0049a1a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049a1a0 ["INT_ADD", "register:40f0:8", ["const:49a1a0:8", "const:4:8"]]
- 0049a1a0 ["CALLIND", null, ["register:0:8"]]
+ 0049a1e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049a1e0 ["INT_ADD", "register:40f0:8", ["const:49a1e0:8", "const:4:8"]]
+ 0049a1e0 ["CALLIND", null, ["register:0:8"]]
- 0049a1a0 bytes 00013fd6
+ 0049a1e0 bytes 00013fd6
- 0049a1b0 ["INT_ADD", "register:40f0:8", ["const:49a1b0:8", "const:4:8"]]
- 0049a1b0 ["CALL", null, ["callee:004994b0:8"]]
+ 0049a1f0 ["INT_ADD", "register:40f0:8", ["const:49a1f0:8", "const:4:8"]]
+ 0049a1f0 ["CALL", null, ["callee:004994b0:8"]]
- 0049a1b0 bytes b0fcff97
+ 0049a1f0 bytes b0fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c4b0df115029314d701ca7a4424479"></a>

### [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) → [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) FUN_0049a2e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004985e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0049a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md) [`0049a8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md) [`0049aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00498620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0049a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md) [`0049a92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md) [`0049aab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md#insn-0049a33c) · [`0049a380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md#insn-0049a380) · [`0049a390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md#insn-0049a390)
- 新版 [`0049a37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a37c) · [`0049a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a3c0) · [`0049a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a3d0)

~~~diff
- 0049a33c ["INT_ADD", "register:40f0:8", ["const:49a33c:8", "const:4:8"]]
- 0049a33c ["CALL", null, ["callee:00c58010:8"]]
+ 0049a37c ["INT_ADD", "register:40f0:8", ["const:49a37c:8", "const:4:8"]]
+ 0049a37c ["CALL", null, ["callee:00c58010:8"]]
- 0049a33c bytes 01f71e94
+ 0049a37c bytes 25f71e94
- 0049a380 ["INT_ADD", "register:40f0:8", ["const:49a380:8", "const:4:8"]]
- 0049a380 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049a3c0 ["INT_ADD", "register:40f0:8", ["const:49a3c0:8", "const:4:8"]]
+ 0049a3c0 ["CALL", null, ["callee:00c57f60:8"]]
- 0049a380 bytes c4f61e94
+ 0049a3c0 bytes e8f61e94
- 0049a390 ["INT_ADD", "register:40f0:8", ["const:49a390:8", "const:4:8"]]
- 0049a390 ["CALL", null, ["callee:0049a7a4:8"]]
+ 0049a3d0 ["INT_ADD", "register:40f0:8", ["const:49a3d0:8", "const:4:8"]]
+ 0049a3d0 ["CALL", null, ["callee:0049a7a4:8"]]
- 0049a390 bytes f5000094
+ 0049a3d0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3016b193a123c5b9c971bc0cec235e8"></a>

### [`0049a764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md) → [`0049a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md) FUN_0049a7a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md#insn-0049a7cc) · [`0049a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md#insn-0049a804) · [`0049a8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a764.md#insn-0049a8b4)
- 新版 [`0049a80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a80c) · [`0049a844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a844) · [`0049a8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a8f4)

~~~diff
- 0049a7cc ["INT_ADD", "register:40f0:8", ["const:49a7cc:8", "const:4:8"]]
- 0049a7cc ["CALL", null, ["callee:00c58010:8"]]
+ 0049a80c ["INT_ADD", "register:40f0:8", ["const:49a80c:8", "const:4:8"]]
+ 0049a80c ["CALL", null, ["callee:00c58010:8"]]
- 0049a7cc bytes ddf51e94
+ 0049a80c bytes 01f61e94
- 0049a804 ["INT_ADD", "register:40f0:8", ["const:49a804:8", "const:4:8"]]
- 0049a804 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049a844 ["INT_ADD", "register:40f0:8", ["const:49a844:8", "const:4:8"]]
+ 0049a844 ["CALL", null, ["callee:00c57f60:8"]]
- 0049a804 bytes a3f51e94
+ 0049a844 bytes c7f51e94
- 0049a8b4 ["INT_ADD", "register:40f0:8", ["const:49a8b4:8", "const:4:8"]]
- 0049a8b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049a8f4 ["INT_ADD", "register:40f0:8", ["const:49a8f4:8", "const:4:8"]]
+ 0049a8f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0049a8b4 bytes 7ff51e94
+ 0049a8f4 bytes a3f51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43099061eaee0423a644307b515fef13"></a>

### [`0049a8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md) → [`0049a92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md) FUN_0049a92c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md#insn-0049a95c) · [`0049a994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md#insn-0049a994) · [`0049aa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a8ec.md#insn-0049aa44)
- 新版 [`0049a99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049a99c) · [`0049a9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049a9d4) · [`0049aa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049aa84)

~~~diff
- 0049a95c ["INT_ADD", "register:40f0:8", ["const:49a95c:8", "const:4:8"]]
- 0049a95c ["CALL", null, ["callee:00c58010:8"]]
+ 0049a99c ["INT_ADD", "register:40f0:8", ["const:49a99c:8", "const:4:8"]]
+ 0049a99c ["CALL", null, ["callee:00c58010:8"]]
- 0049a95c bytes 79f51e94
+ 0049a99c bytes 9df51e94
- 0049a994 ["INT_ADD", "register:40f0:8", ["const:49a994:8", "const:4:8"]]
- 0049a994 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049a9d4 ["INT_ADD", "register:40f0:8", ["const:49a9d4:8", "const:4:8"]]
+ 0049a9d4 ["CALL", null, ["callee:00c57f60:8"]]
- 0049a994 bytes 3ff51e94
+ 0049a9d4 bytes 63f51e94
- 0049aa44 ["INT_ADD", "register:40f0:8", ["const:49aa44:8", "const:4:8"]]
- 0049aa44 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049aa84 ["INT_ADD", "register:40f0:8", ["const:49aa84:8", "const:4:8"]]
+ 0049aa84 ["CALL", null, ["callee:00c57f80:8"]]
- 0049aa44 bytes 1bf51e94
+ 0049aa84 bytes 3ff51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2983218623f2de9d6bfb15c0c8e355c8"></a>

### [`0049aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md) → [`0049aab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md) FUN_0049aab8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049a2a4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049aae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md#insn-0049aae8) · [`0049ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md#insn-0049ab20) · [`0049abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049aa78.md#insn-0049abd0)
- 新版 [`0049ab28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ab28) · [`0049ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ab60) · [`0049ac10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ac10)

~~~diff
- 0049aae8 ["INT_ADD", "register:40f0:8", ["const:49aae8:8", "const:4:8"]]
- 0049aae8 ["CALL", null, ["callee:00c58010:8"]]
+ 0049ab28 ["INT_ADD", "register:40f0:8", ["const:49ab28:8", "const:4:8"]]
+ 0049ab28 ["CALL", null, ["callee:00c58010:8"]]
- 0049aae8 bytes 16f51e94
+ 0049ab28 bytes 3af51e94
- 0049ab20 ["INT_ADD", "register:40f0:8", ["const:49ab20:8", "const:4:8"]]
- 0049ab20 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049ab60 ["INT_ADD", "register:40f0:8", ["const:49ab60:8", "const:4:8"]]
+ 0049ab60 ["CALL", null, ["callee:00c57f60:8"]]
- 0049ab20 bytes dcf41e94
+ 0049ab60 bytes 00f51e94
- 0049abd0 ["INT_ADD", "register:40f0:8", ["const:49abd0:8", "const:4:8"]]
- 0049abd0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049ac10 ["INT_ADD", "register:40f0:8", ["const:49ac10:8", "const:4:8"]]
+ 0049ac10 ["CALL", null, ["callee:00c57f80:8"]]
- 0049abd0 bytes b8f41e94
+ 0049ac10 bytes dcf41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0078eee81baedd82ec6a062665a29d"></a>

### [`0049acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acf4.md) → [`0049ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad34.md) FUN_0049ad34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acf4.md#insn-0049ad10)
- 新版 [`0049ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad34.md#insn-0049ad50)

~~~diff
- 0049ad10 ["INT_ADD", "register:40f0:8", ["const:49ad10:8", "const:4:8"]]
- 0049ad10 ["CALL", null, ["callee:00c57f50:8"]]
+ 0049ad50 ["INT_ADD", "register:40f0:8", ["const:49ad50:8", "const:4:8"]]
+ 0049ad50 ["CALL", null, ["callee:00c57f50:8"]]
- 0049ad10 bytes 5cf41e94
+ 0049ad50 bytes 80f41e94
~~~


<a id="compare-230153febfdb779fd20a33d9e222c679"></a>

### [`0049ad24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md) → [`0049ad64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md) FUN_0049ad64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c584f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c585c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md#insn-0049ad50) · [`0049ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md#insn-0049ad6c) · [`0049ad78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ad24.md#insn-0049ad78)
- 新版 [`0049ad90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049ad90) · [`0049adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049adac) · [`0049adb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049adb8)

~~~diff
- 0049ad50 ["INT_ADD", "register:40f0:8", ["const:49ad50:8", "const:4:8"]]
- 0049ad50 ["CALL", null, ["callee:00c585c0:8"]]
+ 0049ad90 ["INT_ADD", "register:40f0:8", ["const:49ad90:8", "const:4:8"]]
+ 0049ad90 ["CALL", null, ["callee:00c585c0:8"]]
- 0049ad50 bytes e8f51e94
+ 0049ad90 bytes 0cf61e94
- 0049ad6c ["INT_ADD", "register:40f0:8", ["const:49ad6c:8", "const:4:8"]]
- 0049ad6c ["CALL", null, ["callee:004894e8:8"]]
+ 0049adac ["INT_ADD", "register:40f0:8", ["const:49adac:8", "const:4:8"]]
+ 0049adac ["CALL", null, ["callee:004894e8:8"]]
- 0049ad6c bytes cfb9ff97
+ 0049adac bytes cfb9ff97
- 0049ad78 ["INT_ADD", "register:40f0:8", ["const:49ad78:8", "const:4:8"]]
- 0049ad78 ["CALL", null, ["callee:00c53da0:8"]]
+ 0049adb8 ["INT_ADD", "register:40f0:8", ["const:49adb8:8", "const:4:8"]]
+ 0049adb8 ["CALL", null, ["callee:00c53da0:8"]]
- 0049ad78 bytes e2e31e94
+ 0049adb8 bytes fae31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-354130829ea36a736f1097dd6b4132a6"></a>

### [`0049b3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3d4.md) → [`0049b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md) FUN_0049b414

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3d4.md#insn-0049b410) · [`0049b42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3d4.md#insn-0049b42c)
- 新版 [`0049b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md#insn-0049b450) · [`0049b46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md#insn-0049b46c)

~~~diff
- 0049b410 ["INT_ADD", "register:40f0:8", ["const:49b410:8", "const:4:8"]]
- 0049b410 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049b450 ["INT_ADD", "register:40f0:8", ["const:49b450:8", "const:4:8"]]
+ 0049b450 ["CALL", null, ["callee:00c57f60:8"]]
- 0049b410 bytes a0f21e94
+ 0049b450 bytes c4f21e94
- 0049b42c ["INT_ADD", "register:40f0:8", ["const:49b42c:8", "const:4:8"]]
- 0049b42c ["CALL", null, ["callee:00c58160:8"]]
+ 0049b46c ["INT_ADD", "register:40f0:8", ["const:49b46c:8", "const:4:8"]]
+ 0049b46c ["CALL", null, ["callee:00c58160:8"]]
- 0049b42c bytes 19f31e94
+ 0049b46c bytes 3df31e94
~~~


<a id="compare-f58f562b6a36838468a4c4544f289498"></a>

### [`0049b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md) → [`0049b5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md) FUN_0049b5ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 4件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a99514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a99/00a99514.md) · 呼出先 4件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md#insn-0049b5d8) · [`0049b5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md#insn-0049b5f8) · [`0049b62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md#insn-0049b62c)
- 新版 [`0049b618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b618) · [`0049b638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b638) · [`0049b66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b66c)

~~~diff
- 0049b5d8 ["INT_ADD", "register:40f0:8", ["const:49b5d8:8", "const:4:8"]]
- 0049b5d8 ["CALL", null, ["callee:0049ff90:8"]]
+ 0049b618 ["INT_ADD", "register:40f0:8", ["const:49b618:8", "const:4:8"]]
+ 0049b618 ["CALL", null, ["callee:0049ff90:8"]]
- 0049b5d8 bytes 5e120094
+ 0049b618 bytes 5e120094
- 0049b5f8 ["INT_ADD", "register:40f0:8", ["const:49b5f8:8", "const:4:8"]]
- 0049b5f8 ["CALL", null, ["callee:0049b6cc:8"]]
+ 0049b638 ["INT_ADD", "register:40f0:8", ["const:49b638:8", "const:4:8"]]
+ 0049b638 ["CALL", null, ["callee:0049b6cc:8"]]
- 0049b5f8 bytes 25000094
+ 0049b638 bytes 25000094
- 0049b62c ["INT_ADD", "register:40f0:8", ["const:49b62c:8", "const:4:8"]]
- 0049b62c ["CALL", null, ["callee:00c57f80:8"]]
+ 0049b66c ["INT_ADD", "register:40f0:8", ["const:49b66c:8", "const:4:8"]]
+ 0049b66c ["CALL", null, ["callee:00c57f80:8"]]
- 0049b62c bytes 21f21e94
+ 0049b66c bytes 45f21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-238c6285a71bef2b9c972db3fa264425"></a>

### [`0049bbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bbe8.md) → [`0049bc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc28.md) FUN_0049bc28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049bc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bbe8.md#insn-0049bc2c)
- 新版 [`0049bc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc28.md#insn-0049bc6c)

~~~diff
- 0049bc2c ["INT_ADD", "register:40f0:8", ["const:49bc2c:8", "const:4:8"]]
- 0049bc2c ["CALL", null, ["callee:00c57f80:8"]]
+ 0049bc6c ["INT_ADD", "register:40f0:8", ["const:49bc6c:8", "const:4:8"]]
+ 0049bc6c ["CALL", null, ["callee:00c57f80:8"]]
- 0049bc2c bytes a1f01e94
+ 0049bc6c bytes c5f01e94
~~~


<a id="compare-d0f3bbc907dcb08814c78b158e98d936"></a>

### [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) → [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) FUN_0049c064

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 8件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) [`0049d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md)
- 新版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 8件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) [`0049d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049c078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md#insn-0049c078) · [`0049c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md#insn-0049c08c) · [`0049c118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md#insn-0049c118)
- 新版 [`0049c0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c0b8) · [`0049c0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c0cc) · [`0049c158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c158)

~~~diff
- 0049c078 ["INT_ADD", "register:40f0:8", ["const:49c078:8", "const:4:8"]]
- 0049c078 ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049c0b8 ["INT_ADD", "register:40f0:8", ["const:49c0b8:8", "const:4:8"]]
+ 0049c0b8 ["CALL", null, ["callee:0049d1d8:8"]]
- 0049c078 bytes 48040094
+ 0049c0b8 bytes 48040094
- 0049c08c ["INT_ADD", "register:40f0:8", ["const:49c08c:8", "const:4:8"]]
- 0049c08c ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049c0cc ["INT_ADD", "register:40f0:8", ["const:49c0cc:8", "const:4:8"]]
+ 0049c0cc ["CALL", null, ["callee:0049d1d8:8"]]
- 0049c08c bytes 43040094
+ 0049c0cc bytes 43040094
- 0049c118 ["INT_ADD", "register:40f0:8", ["const:49c118:8", "const:4:8"]]
- 0049c118 ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049c158 ["INT_ADD", "register:40f0:8", ["const:49c158:8", "const:4:8"]]
+ 0049c158 ["CALL", null, ["callee:0049d1d8:8"]]
- 0049c118 bytes 20040094
+ 0049c158 bytes 20040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee9377a6633a99100dac696227b4425"></a>

### [`0049d088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d088.md) → [`0049d0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d0c8.md) FUN_0049d0c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d088.md#insn-0049d0c8)
- 新版 [`0049d108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d0c8.md#insn-0049d108)

~~~diff
- 0049d0c8 ["INT_ADD", "register:40f0:8", ["const:49d0c8:8", "const:4:8"]]
- 0049d0c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049d108 ["INT_ADD", "register:40f0:8", ["const:49d108:8", "const:4:8"]]
+ 0049d108 ["CALL", null, ["callee:00c57f80:8"]]
- 0049d0c8 bytes 7aeb1e94
+ 0049d108 bytes 9eeb1e94
~~~


<a id="compare-f2c03c97cc2eda88eaa1a746877b440f"></a>

### [`0049d100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md) → [`0049d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md) FUN_0049d140

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)
- 新版 呼出元 1件 [`00a99514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a99/00a99514.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md#insn-0049d190) · [`0049d194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md#insn-0049d194)
- 新版 [`0049d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md#insn-0049d1d0) · [`0049d1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md#insn-0049d1d4)

~~~diff
- 0049d190 ["INT_ADD", "register:40f0:8", ["const:49d190:8", "const:4:8"]]
- 0049d190 ["CALL", null, ["callee:0049f444:8"]]
+ 0049d1d0 ["INT_ADD", "register:40f0:8", ["const:49d1d0:8", "const:4:8"]]
+ 0049d1d0 ["CALL", null, ["callee:0049f444:8"]]
- 0049d190 bytes 9d080094
+ 0049d1d0 bytes 9d080094
- 0049d194 ["INT_ADD", "register:40f0:8", ["const:49d194:8", "const:4:8"]]
- 0049d194 ["CALL", null, ["callee:0049f458:8"]]
+ 0049d1d4 ["INT_ADD", "register:40f0:8", ["const:49d1d4:8", "const:4:8"]]
+ 0049d1d4 ["CALL", null, ["callee:0049f458:8"]]
- 0049d194 bytes a1080094
+ 0049d1d4 bytes a1080094
~~~


<a id="compare-8027e0bd025eeb57e270a9362839690c"></a>

### [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) → [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) FUN_0049d1d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) [`0049d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)
- 新版 呼出元 4件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) [`0049d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md#insn-0049d260) · [`0049d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md#insn-0049d268) · [`0049d26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md#insn-0049d26c)
- 新版 [`0049d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2a0) · [`0049d2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2a8) · [`0049d2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2ac)

~~~diff
- 0049d260 ["INT_ADD", "register:40f0:8", ["const:49d260:8", "const:4:8"]]
- 0049d260 ["CALL", null, ["callee:0049f444:8"]]
+ 0049d2a0 ["INT_ADD", "register:40f0:8", ["const:49d2a0:8", "const:4:8"]]
+ 0049d2a0 ["CALL", null, ["callee:0049f444:8"]]
- 0049d260 bytes 69080094
+ 0049d2a0 bytes 69080094
- 0049d268 ["INT_ADD", "register:40f0:8", ["const:49d268:8", "const:4:8"]]
- 0049d268 ["CALL", null, ["callee:0049f458:8"]]
+ 0049d2a8 ["INT_ADD", "register:40f0:8", ["const:49d2a8:8", "const:4:8"]]
+ 0049d2a8 ["CALL", null, ["callee:0049f458:8"]]
- 0049d268 bytes 6c080094
+ 0049d2a8 bytes 6c080094
- 0049d26c ["INT_ADD", "register:40f0:8", ["const:49d26c:8", "const:4:8"]]
- 0049d26c ["CALL", null, ["callee:0049f444:8"]]
+ 0049d2ac ["INT_ADD", "register:40f0:8", ["const:49d2ac:8", "const:4:8"]]
+ 0049d2ac ["CALL", null, ["callee:0049f444:8"]]
- 0049d26c bytes 66080094
+ 0049d2ac bytes 66080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c3fb3f246553327ef16bdf121174be2"></a>

### [`0049d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md) → [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) FUN_0049d438

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) · 呼出先 1件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md)
- 新版 呼出元 1件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) · 呼出先 1件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md#insn-0049d440) · [`0049d460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md#insn-0049d460) · [`0049d474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d3f8.md#insn-0049d474)
- 新版 [`0049d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d480) · [`0049d4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d4a0) · [`0049d4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d4b4)

~~~diff
- 0049d440 ["INT_ADD", "register:40f0:8", ["const:49d440:8", "const:4:8"]]
- 0049d440 ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049d480 ["INT_ADD", "register:40f0:8", ["const:49d480:8", "const:4:8"]]
+ 0049d480 ["CALL", null, ["callee:0049d1d8:8"]]
- 0049d440 bytes 56ffff97
+ 0049d480 bytes 56ffff97
- 0049d460 ["INT_ADD", "register:40f0:8", ["const:49d460:8", "const:4:8"]]
- 0049d460 ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049d4a0 ["INT_ADD", "register:40f0:8", ["const:49d4a0:8", "const:4:8"]]
+ 0049d4a0 ["CALL", null, ["callee:0049d1d8:8"]]
- 0049d460 bytes 4effff97
+ 0049d4a0 bytes 4effff97
- 0049d474 ["INT_ADD", "register:40f0:8", ["const:49d474:8", "const:4:8"]]
- 0049d474 ["CALL", null, ["callee:0049d1d8:8"]]
+ 0049d4b4 ["INT_ADD", "register:40f0:8", ["const:49d4b4:8", "const:4:8"]]
+ 0049d4b4 ["CALL", null, ["callee:0049d1d8:8"]]
- 0049d474 bytes 49ffff97
+ 0049d4b4 bytes 49ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d0c6941f85c2251f1610722fb090ee"></a>

### [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) → [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) FUN_0049da60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 8件 [`0049eaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 8件 [`0049eaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049da68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md#insn-0049da68) · [`0049da84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md#insn-0049da84) · [`0049dadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md#insn-0049dadc)
- 新版 [`0049daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049daa8) · [`0049dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049dac4) · [`0049db1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049db1c)

~~~diff
- 0049da68 ["INT_ADD", "register:40f0:8", ["const:49da68:8", "const:4:8"]]
- 0049da68 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049daa8 ["INT_ADD", "register:40f0:8", ["const:49daa8:8", "const:4:8"]]
+ 0049daa8 ["CALL", null, ["callee:00c57f60:8"]]
- 0049da68 bytes 0ae91e94
+ 0049daa8 bytes 2ee91e94
- 0049da84 ["INT_ADD", "register:40f0:8", ["const:49da84:8", "const:4:8"]]
- 0049da84 ["CALL", null, ["callee:00c58160:8"]]
+ 0049dac4 ["INT_ADD", "register:40f0:8", ["const:49dac4:8", "const:4:8"]]
+ 0049dac4 ["CALL", null, ["callee:00c58160:8"]]
- 0049da84 bytes 83e91e94
+ 0049dac4 bytes a7e91e94
- 0049dadc ["INT_ADD", "register:40f0:8", ["const:49dadc:8", "const:4:8"]]
- 0049dadc ["CALL", null, ["callee:00c58010:8"]]
+ 0049db1c ["INT_ADD", "register:40f0:8", ["const:49db1c:8", "const:4:8"]]
+ 0049db1c ["CALL", null, ["callee:00c58010:8"]]
- 0049dadc bytes 19e91e94
+ 0049db1c bytes 3de91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f4b8ea8093ac6e32524ea5c9a74dba"></a>

### [`0049dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dc58.md) → [`0049dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dc98.md) FUN_0049dc98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049dca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dc58.md#insn-0049dca4)
- 新版 [`0049dce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dc98.md#insn-0049dce4)

~~~diff
- 0049dca4 ["INT_ADD", "register:40f0:8", ["const:49dca4:8", "const:4:8"]]
- 0049dca4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049dce4 ["INT_ADD", "register:40f0:8", ["const:49dce4:8", "const:4:8"]]
+ 0049dce4 ["CALL", null, ["callee:00c57f80:8"]]
- 0049dca4 bytes 83e81e94
+ 0049dce4 bytes a7e81e94
~~~


<a id="compare-66a3d58fc851b6fe2b09c342119dd4f4"></a>

### [`0049df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md) → [`0049df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md) FUN_0049df80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md) · 呼出先 2件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md)
- 新版 呼出元 1件 [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md#insn-0049e268) · [`0049e494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md#insn-0049e494) · [`0049e49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md#insn-0049e49c)
- 新版 [`0049e2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e2a8) · [`0049e4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e4d4) · [`0049e4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e4dc)

~~~diff
- 0049e268 ["INT_ADD", "register:40f0:8", ["const:49e268:8", "const:4:8"]]
- 0049e268 ["CALL", null, ["callee:0049f458:8"]]
+ 0049e2a8 ["INT_ADD", "register:40f0:8", ["const:49e2a8:8", "const:4:8"]]
+ 0049e2a8 ["CALL", null, ["callee:0049f458:8"]]
- 0049e268 bytes 6c040094
+ 0049e2a8 bytes 6c040094
- 0049e494 ["INT_ADD", "register:40f0:8", ["const:49e494:8", "const:4:8"]]
- 0049e494 ["CALL", null, ["callee:0049f458:8"]]
+ 0049e4d4 ["INT_ADD", "register:40f0:8", ["const:49e4d4:8", "const:4:8"]]
+ 0049e4d4 ["CALL", null, ["callee:0049f458:8"]]
- 0049e494 bytes e1030094
+ 0049e4d4 bytes e1030094
- 0049e49c ["INT_ADD", "register:40f0:8", ["const:49e49c:8", "const:4:8"]]
- 0049e49c ["CALL", null, ["callee:0049f444:8"]]
+ 0049e4dc ["INT_ADD", "register:40f0:8", ["const:49e4dc:8", "const:4:8"]]
+ 0049e4dc ["CALL", null, ["callee:0049f444:8"]]
- 0049e49c bytes da030094
+ 0049e4dc bytes da030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4429f013440339f932454c806fe303e6"></a>

### [`0049e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md) → [`0049e504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md) FUN_0049e504

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) [`008c7b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c7/008c7b40.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 4件 [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008c7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c7/008c7b94.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md#insn-0049e568) · [`0049e5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md#insn-0049e5dc) · [`0049e618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md#insn-0049e618)
- 新版 [`0049e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e5a8) · [`0049e61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e61c) · [`0049e658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e658)

~~~diff
- 0049e568 ["INT_ADD", "register:40f0:8", ["const:49e568:8", "const:4:8"]]
- 0049e568 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049e5a8 ["INT_ADD", "register:40f0:8", ["const:49e5a8:8", "const:4:8"]]
+ 0049e5a8 ["CALL", null, ["callee:00c57f60:8"]]
- 0049e568 bytes 4ae61e94
+ 0049e5a8 bytes 6ee61e94
- 0049e5dc ["INT_ADD", "register:40f0:8", ["const:49e5dc:8", "const:4:8"]]
- 0049e5dc ["CALL", null, ["callee:00c58010:8"]]
+ 0049e61c ["INT_ADD", "register:40f0:8", ["const:49e61c:8", "const:4:8"]]
+ 0049e61c ["CALL", null, ["callee:00c58010:8"]]
- 0049e5dc bytes 59e61e94
+ 0049e61c bytes 7de61e94
- 0049e618 ["INT_ADD", "register:40f0:8", ["const:49e618:8", "const:4:8"]]
- 0049e618 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049e658 ["INT_ADD", "register:40f0:8", ["const:49e658:8", "const:4:8"]]
+ 0049e658 ["CALL", null, ["callee:00c57f60:8"]]
- 0049e618 bytes 1ee61e94
+ 0049e658 bytes 42e61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d6bbf6053ca02331a27f95a83461b5"></a>

### [`0049e6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md) → [`0049e714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md) FUN_0049e714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0049f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0049f934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md#insn-0049e78c) · [`0049e7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md#insn-0049e7cc) · [`0049e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md#insn-0049e7e0)
- 新版 [`0049e7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e7cc) · [`0049e80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e80c) · [`0049e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e820)

~~~diff
- 0049e78c ["INT_ADD", "register:40f0:8", ["const:49e78c:8", "const:4:8"]]
- 0049e78c ["CALL", null, ["callee:00c57f60:8"]]
+ 0049e7cc ["INT_ADD", "register:40f0:8", ["const:49e7cc:8", "const:4:8"]]
+ 0049e7cc ["CALL", null, ["callee:00c57f60:8"]]
- 0049e78c bytes c1e51e94
+ 0049e7cc bytes e5e51e94
- 0049e7cc ["INT_ADD", "register:40f0:8", ["const:49e7cc:8", "const:4:8"]]
- 0049e7cc ["CALL", null, ["callee:0049f934:8"]]
+ 0049e80c ["INT_ADD", "register:40f0:8", ["const:49e80c:8", "const:4:8"]]
+ 0049e80c ["CALL", null, ["callee:0049f934:8"]]
- 0049e7cc bytes 4a040094
+ 0049e80c bytes 4a040094
- 0049e7e0 ["INT_ADD", "register:40f0:8", ["const:49e7e0:8", "const:4:8"]]
- 0049e7e0 ["CALL", null, ["callee:00c580d0:8"]]
+ 0049e820 ["INT_ADD", "register:40f0:8", ["const:49e820:8", "const:4:8"]]
+ 0049e820 ["CALL", null, ["callee:00c580d0:8"]]
- 0049e7e0 bytes 08e61e94
+ 0049e820 bytes 2ce61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40df312541e47ee279415960f69311c5"></a>

### [`0049eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md) → [`0049ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md) FUN_0049ebe0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ebdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md#insn-0049ebdc) · [`0049eca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md#insn-0049eca0)
- 新版 [`0049ec1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md#insn-0049ec1c) · [`0049ece0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md#insn-0049ece0)

~~~diff
- 0049ebdc ["INT_ADD", "register:40f0:8", ["const:49ebdc:8", "const:4:8"]]
- 0049ebdc ["CALL", null, ["callee:00c57f60:8"]]
+ 0049ec1c ["INT_ADD", "register:40f0:8", ["const:49ec1c:8", "const:4:8"]]
+ 0049ec1c ["CALL", null, ["callee:00c57f60:8"]]
- 0049ebdc bytes ade41e94
+ 0049ec1c bytes d1e41e94
- 0049eca0 ["INT_ADD", "register:40f0:8", ["const:49eca0:8", "const:4:8"]]
- 0049eca0 ["CALL", null, ["callee:0047d6f8:8"]]
+ 0049ece0 ["INT_ADD", "register:40f0:8", ["const:49ece0:8", "const:4:8"]]
+ 0049ece0 ["CALL", null, ["callee:0047d6f8:8"]]
- 0049eca0 bytes 867aff97
+ 0049ece0 bytes 867aff97
~~~


<a id="compare-aaa1cdfeb1dd8c7a7f33acab02e6dc47"></a>

### [`0049eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md) → [`0049ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md) FUN_0049ece4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 7件 [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`0049f17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f17c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 7件 [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`0049f1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f1bc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ee0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md#insn-0049ee0c) · [`0049ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md#insn-0049ee64) · [`0049ee7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md#insn-0049ee7c)
- 新版 [`0049ee4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049ee4c) · [`0049eea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049eea4) · [`0049eebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049eebc)

~~~diff
- 0049ee0c ["INT_ADD", "register:40f0:8", ["const:49ee0c:8", "const:4:8"]]
- 0049ee0c ["CALL", null, ["callee:00c58010:8"]]
+ 0049ee4c ["INT_ADD", "register:40f0:8", ["const:49ee4c:8", "const:4:8"]]
+ 0049ee4c ["CALL", null, ["callee:00c58010:8"]]
- 0049ee0c bytes 4de41e94
+ 0049ee4c bytes 71e41e94
- 0049ee64 ["INT_ADD", "register:40f0:8", ["const:49ee64:8", "const:4:8"]]
- 0049ee64 ["CALL", null, ["callee:0049f1bc:8"]]
+ 0049eea4 ["INT_ADD", "register:40f0:8", ["const:49eea4:8", "const:4:8"]]
+ 0049eea4 ["CALL", null, ["callee:0049f1bc:8"]]
- 0049ee64 bytes c6000094
+ 0049eea4 bytes c6000094
- 0049ee7c ["INT_ADD", "register:40f0:8", ["const:49ee7c:8", "const:4:8"]]
- 0049ee7c ["CALL", null, ["callee:0047d5f4:8"]]
+ 0049eebc ["INT_ADD", "register:40f0:8", ["const:49eebc:8", "const:4:8"]]
+ 0049eebc ["CALL", null, ["callee:0047d5f4:8"]]
- 0049ee7c bytes ce79ff97
+ 0049eebc bytes ce79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-594da5cfab7184876329a488a5554979"></a>

### [`0049f370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f370.md) → [`0049f3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f3b0.md) FUN_0049f3b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f370.md#insn-0049f3cc)
- 新版 [`0049f40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f3b0.md#insn-0049f40c)

~~~diff
- 0049f3cc ["INT_ADD", "register:40f0:8", ["const:49f3cc:8", "const:4:8"]]
- 0049f3cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0049f40c ["INT_ADD", "register:40f0:8", ["const:49f40c:8", "const:4:8"]]
+ 0049f40c ["CALL", null, ["callee:00c57f80:8"]]
- 0049f3cc bytes b9e21e94
+ 0049f40c bytes dde21e94
~~~


<a id="compare-e85436394e444d91f792930fe6852102"></a>

### [`0049f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md) → [`0049f480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md) FUN_0049f480

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md#insn-0049f4c0) · [`0049f4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md#insn-0049f4f4) · [`0049f604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md#insn-0049f604)
- 新版 [`0049f500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f500) · [`0049f534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f534) · [`0049f644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f644)

~~~diff
- 0049f4c0 ["INT_ADD", "register:40f0:8", ["const:49f4c0:8", "const:4:8"]]
- 0049f4c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049f500 ["INT_ADD", "register:40f0:8", ["const:49f500:8", "const:4:8"]]
+ 0049f500 ["CALL", null, ["callee:00c57f60:8"]]
- 0049f4c0 bytes 74e21e94
+ 0049f500 bytes 98e21e94
- 0049f4f4 ["INT_ADD", "register:40f0:8", ["const:49f4f4:8", "const:4:8"]]
- 0049f4f4 ["CALL", null, ["callee:00c58010:8"]]
+ 0049f534 ["INT_ADD", "register:40f0:8", ["const:49f534:8", "const:4:8"]]
+ 0049f534 ["CALL", null, ["callee:00c58010:8"]]
- 0049f4f4 bytes 93e21e94
+ 0049f534 bytes b7e21e94
- 0049f604 ["INT_ADD", "register:40f0:8", ["const:49f604:8", "const:4:8"]]
- 0049f604 ["CALL", null, ["callee:00c58010:8"]]
+ 0049f644 ["INT_ADD", "register:40f0:8", ["const:49f644:8", "const:4:8"]]
+ 0049f644 ["CALL", null, ["callee:00c58010:8"]]
- 0049f604 bytes 4fe21e94
+ 0049f644 bytes 73e21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794b03cf850c4829cda8101e12672459"></a>

### [`0049f72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md) → [`0049f76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md) FUN_0049f76c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0049f8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0049f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md#insn-0049f7b8) · [`0049f870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md#insn-0049f870) · [`0049f88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md#insn-0049f88c)
- 新版 [`0049f7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f7f8) · [`0049f8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f8b0) · [`0049f8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f8cc)

~~~diff
- 0049f7b8 ["INT_ADD", "register:40f0:8", ["const:49f7b8:8", "const:4:8"]]
- 0049f7b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049f7f8 ["INT_ADD", "register:40f0:8", ["const:49f7f8:8", "const:4:8"]]
+ 0049f7f8 ["CALL", null, ["callee:00c57f60:8"]]
- 0049f7b8 bytes b6e11e94
+ 0049f7f8 bytes dae11e94
- 0049f870 ["INT_ADD", "register:40f0:8", ["const:49f870:8", "const:4:8"]]
- 0049f870 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049f8b0 ["INT_ADD", "register:40f0:8", ["const:49f8b0:8", "const:4:8"]]
+ 0049f8b0 ["CALL", null, ["callee:00c57f80:8"]]
- 0049f870 bytes 90e11e94
+ 0049f8b0 bytes b4e11e94
- 0049f88c ["INT_ADD", "register:40f0:8", ["const:49f88c:8", "const:4:8"]]
- 0049f88c ["CALL", null, ["callee:00c57f80:8"]]
+ 0049f8cc ["INT_ADD", "register:40f0:8", ["const:49f8cc:8", "const:4:8"]]
+ 0049f8cc ["CALL", null, ["callee:00c57f80:8"]]
- 0049f88c bytes 89e11e94
+ 0049f8cc bytes ade11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1868dd57c1cf571207ad76893b27727a"></a>

### [`0049f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md) → [`0049f934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md) FUN_0049f934

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049e6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0049e714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md#insn-0049f95c) · [`0049f994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md#insn-0049f994) · [`0049fa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8f4.md#insn-0049fa44)
- 新版 [`0049f99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049f99c) · [`0049f9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049f9d4) · [`0049fa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049fa84)

~~~diff
- 0049f95c ["INT_ADD", "register:40f0:8", ["const:49f95c:8", "const:4:8"]]
- 0049f95c ["CALL", null, ["callee:00c58010:8"]]
+ 0049f99c ["INT_ADD", "register:40f0:8", ["const:49f99c:8", "const:4:8"]]
+ 0049f99c ["CALL", null, ["callee:00c58010:8"]]
- 0049f95c bytes 79e11e94
+ 0049f99c bytes 9de11e94
- 0049f994 ["INT_ADD", "register:40f0:8", ["const:49f994:8", "const:4:8"]]
- 0049f994 ["CALL", null, ["callee:00c57f60:8"]]
+ 0049f9d4 ["INT_ADD", "register:40f0:8", ["const:49f9d4:8", "const:4:8"]]
+ 0049f9d4 ["CALL", null, ["callee:00c57f60:8"]]
- 0049f994 bytes 3fe11e94
+ 0049f9d4 bytes 63e11e94
- 0049fa44 ["INT_ADD", "register:40f0:8", ["const:49fa44:8", "const:4:8"]]
- 0049fa44 ["CALL", null, ["callee:00c57f80:8"]]
+ 0049fa84 ["INT_ADD", "register:40f0:8", ["const:49fa84:8", "const:4:8"]]
+ 0049fa84 ["CALL", null, ["callee:00c57f80:8"]]
- 0049fa44 bytes 1be11e94
+ 0049fa84 bytes 3fe11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43250c068f74e4cbcec6cdf5681490e9"></a>

### [`004a0368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md) → [`004a03a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md) FUN_004a03a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004a04e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004a0528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0528.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a03f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md#insn-004a03f0) · [`004a04a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md#insn-004a04a4) · [`004a04c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md#insn-004a04c0)
- 新版 [`004a0430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a0430) · [`004a04e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a04e4) · [`004a0500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a0500)

~~~diff
- 004a03f0 ["INT_ADD", "register:40f0:8", ["const:4a03f0:8", "const:4:8"]]
- 004a03f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 004a0430 ["INT_ADD", "register:40f0:8", ["const:4a0430:8", "const:4:8"]]
+ 004a0430 ["CALL", null, ["callee:00c57f60:8"]]
- 004a03f0 bytes a8de1e94
+ 004a0430 bytes ccde1e94
- 004a04a4 ["INT_ADD", "register:40f0:8", ["const:4a04a4:8", "const:4:8"]]
- 004a04a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004a04e4 ["INT_ADD", "register:40f0:8", ["const:4a04e4:8", "const:4:8"]]
+ 004a04e4 ["CALL", null, ["callee:00c57f80:8"]]
- 004a04a4 bytes 83de1e94
+ 004a04e4 bytes a7de1e94
- 004a04c0 ["INT_ADD", "register:40f0:8", ["const:4a04c0:8", "const:4:8"]]
- 004a04c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 004a0500 ["INT_ADD", "register:40f0:8", ["const:4a0500:8", "const:4:8"]]
+ 004a0500 ["CALL", null, ["callee:00c57f80:8"]]
- 004a04c0 bytes 7cde1e94
+ 004a0500 bytes a0de1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff619306e0f603a1e48af673505b0fa9"></a>

### [`004a1ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1ab4.md) → [`004a1af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md) _ZN5Botan7AES_1285clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1ab4.md#insn-004a1ad8) · [`004a1ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1ab4.md#insn-004a1ae8) · [`004a1b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1ab4.md#insn-004a1b00)
- 新版 [`004a1b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b18) · [`004a1b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b28) · [`004a1b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b40)

~~~diff
- 004a1ad8 ["INT_ADD", "register:40f0:8", ["const:4a1ad8:8", "const:4:8"]]
- 004a1ad8 ["CALL", null, ["callee:00c58160:8"]]
+ 004a1b18 ["INT_ADD", "register:40f0:8", ["const:4a1b18:8", "const:4:8"]]
+ 004a1b18 ["CALL", null, ["callee:00c58160:8"]]
- 004a1ad8 bytes 6ed91e94
+ 004a1b18 bytes 92d91e94
- 004a1ae8 ["INT_ADD", "register:40f0:8", ["const:4a1ae8:8", "const:4:8"]]
- 004a1ae8 ["CALL", null, ["callee:00540ac8:8"]]
+ 004a1b28 ["INT_ADD", "register:40f0:8", ["const:4a1b28:8", "const:4:8"]]
+ 004a1b28 ["CALL", null, ["callee:00540ac8:8"]]
- 004a1ae8 bytes e87b0294
+ 004a1b28 bytes e87b0294
- 004a1b00 ["INT_ADD", "register:40f0:8", ["const:4a1b00:8", "const:4:8"]]
- 004a1b00 ["CALL", null, ["callee:00c58160:8"]]
+ 004a1b40 ["INT_ADD", "register:40f0:8", ["const:4a1b40:8", "const:4:8"]]
+ 004a1b40 ["CALL", null, ["callee:00c58160:8"]]
- 004a1b00 bytes 64d91e94
+ 004a1b40 bytes 88d91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09a217d5e78351f95b854a276765ab0"></a>

### [`004a1dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1dd0.md) → [`004a1e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md) _ZN5Botan7AES_1925clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1dd0.md#insn-004a1df4) · [`004a1e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1dd0.md#insn-004a1e04) · [`004a1e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1dd0.md#insn-004a1e1c)
- 新版 [`004a1e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e34) · [`004a1e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e44) · [`004a1e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e5c)

~~~diff
- 004a1df4 ["INT_ADD", "register:40f0:8", ["const:4a1df4:8", "const:4:8"]]
- 004a1df4 ["CALL", null, ["callee:00c58160:8"]]
+ 004a1e34 ["INT_ADD", "register:40f0:8", ["const:4a1e34:8", "const:4:8"]]
+ 004a1e34 ["CALL", null, ["callee:00c58160:8"]]
- 004a1df4 bytes a7d81e94
+ 004a1e34 bytes cbd81e94
- 004a1e04 ["INT_ADD", "register:40f0:8", ["const:4a1e04:8", "const:4:8"]]
- 004a1e04 ["CALL", null, ["callee:00540ac8:8"]]
+ 004a1e44 ["INT_ADD", "register:40f0:8", ["const:4a1e44:8", "const:4:8"]]
+ 004a1e44 ["CALL", null, ["callee:00540ac8:8"]]
- 004a1e04 bytes 217b0294
+ 004a1e44 bytes 217b0294
- 004a1e1c ["INT_ADD", "register:40f0:8", ["const:4a1e1c:8", "const:4:8"]]
- 004a1e1c ["CALL", null, ["callee:00c58160:8"]]
+ 004a1e5c ["INT_ADD", "register:40f0:8", ["const:4a1e5c:8", "const:4:8"]]
+ 004a1e5c ["CALL", null, ["callee:00c58160:8"]]
- 004a1e1c bytes 9dd81e94
+ 004a1e5c bytes c1d81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9474b123dda0cc7c380e663fd7d65d8"></a>

### [`004a20ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20ec.md) → [`004a212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md) _ZN5Botan7AES_2565clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540a88.md) [`00540b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540b78.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a2110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20ec.md#insn-004a2110) · [`004a2120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20ec.md#insn-004a2120) · [`004a2138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20ec.md#insn-004a2138)
- 新版 [`004a2150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2150) · [`004a2160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2160) · [`004a2178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2178)

~~~diff
- 004a2110 ["INT_ADD", "register:40f0:8", ["const:4a2110:8", "const:4:8"]]
- 004a2110 ["CALL", null, ["callee:00c58160:8"]]
+ 004a2150 ["INT_ADD", "register:40f0:8", ["const:4a2150:8", "const:4:8"]]
+ 004a2150 ["CALL", null, ["callee:00c58160:8"]]
- 004a2110 bytes e0d71e94
+ 004a2150 bytes 04d81e94
- 004a2120 ["INT_ADD", "register:40f0:8", ["const:4a2120:8", "const:4:8"]]
- 004a2120 ["CALL", null, ["callee:00540ac8:8"]]
+ 004a2160 ["INT_ADD", "register:40f0:8", ["const:4a2160:8", "const:4:8"]]
+ 004a2160 ["CALL", null, ["callee:00540ac8:8"]]
- 004a2120 bytes 5a7a0294
+ 004a2160 bytes 5a7a0294
- 004a2138 ["INT_ADD", "register:40f0:8", ["const:4a2138:8", "const:4:8"]]
- 004a2138 ["CALL", null, ["callee:00c58160:8"]]
+ 004a2178 ["INT_ADD", "register:40f0:8", ["const:4a2178:8", "const:4:8"]]
+ 004a2178 ["CALL", null, ["callee:00c58160:8"]]
- 004a2138 bytes d6d71e94
+ 004a2178 bytes fad71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3487bfd063afb5f0deb1a8edb6dfa17d"></a>

### [`004a5198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5198.md) → [`004a51d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a51d8.md) _ZN5BotaneqERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5198.md#insn-004a5268)
- 新版 [`004a52a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a51d8.md#insn-004a52a8)

~~~diff
- 004a5268 ["INT_ADD", "register:40f0:8", ["const:4a5268:8", "const:4:8"]]
- 004a5268 ["CALL", null, ["callee:00c58120:8"]]
+ 004a52a8 ["INT_ADD", "register:40f0:8", ["const:4a52a8:8", "const:4:8"]]
+ 004a52a8 ["CALL", null, ["callee:00c58120:8"]]
- 004a5268 bytes 7acb1e94
+ 004a52a8 bytes 9ecb1e94
~~~


<a id="compare-c62724bb4ce30f3531a7000c7b047e97"></a>

### [`004a52ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a52ec.md) → [`004a532c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a532c.md) _ZN5BotanneERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c586a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a52f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a52ec.md#insn-004a52f4)
- 新版 [`004a5334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a532c.md#insn-004a5334)

~~~diff
- 004a52f4 ["INT_ADD", "register:40f0:8", ["const:4a52f4:8", "const:4:8"]]
- 004a52f4 ["CALL", null, ["callee:00c58770:8"]]
+ 004a5334 ["INT_ADD", "register:40f0:8", ["const:4a5334:8", "const:4:8"]]
+ 004a5334 ["CALL", null, ["callee:00c58770:8"]]
- 004a52f4 bytes ebcc1e94
+ 004a5334 bytes 0fcd1e94
~~~


<a id="compare-65542afce01394352cc1c50daa7f34a0"></a>

### [`004a5308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5308.md) → [`004a5348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md) _ZNK5Botan19AlgorithmIdentifier11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5308.md#insn-004a5330) · [`004a5344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5308.md#insn-004a5344) · [`004a5360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5308.md#insn-004a5360)
- 新版 [`004a5370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a5370) · [`004a5384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a5384) · [`004a53a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a53a0)

~~~diff
- 004a5330 ["INT_ADD", "register:40f0:8", ["const:4a5330:8", "const:4:8"]]
- 004a5330 ["CALL", null, ["callee:00c58780:8"]]
+ 004a5370 ["INT_ADD", "register:40f0:8", ["const:4a5370:8", "const:4:8"]]
+ 004a5370 ["CALL", null, ["callee:00c58780:8"]]
- 004a5330 bytes e0cc1e94
+ 004a5370 bytes 04cd1e94
- 004a5344 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5344 ["INT_ADD", "register:40f0:8", ["const:4a5344:8", "const:4:8"]]
- 004a5344 ["CALLIND", null, ["register:0:8"]]
+ 004a5384 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5384 ["INT_ADD", "register:40f0:8", ["const:4a5384:8", "const:4:8"]]
+ 004a5384 ["CALLIND", null, ["register:0:8"]]
- 004a5344 bytes 00013fd6
+ 004a5384 bytes 00013fd6
- 004a5360 ["INT_ADD", "register:40f0:8", ["const:4a5360:8", "const:4:8"]]
- 004a5360 ["CALL", null, ["callee:00c58790:8"]]
+ 004a53a0 ["INT_ADD", "register:40f0:8", ["const:4a53a0:8", "const:4:8"]]
+ 004a53a0 ["CALL", null, ["callee:00c58790:8"]]
- 004a5360 bytes d8cc1e94
+ 004a53a0 bytes fccc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f854304fba002e95e6a2be6576e58bfd"></a>

### [`004a5568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5568.md) → [`004a55a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55a8.md) _ZN5Botan11DER_Encoder6encodeERKNS_11ASN1_ObjectE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5568.md#insn-004a5588)
- 新版 [`004a55c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55a8.md#insn-004a55c8)

~~~diff
- 004a5588 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5588 ["INT_ADD", "register:40f0:8", ["const:4a5588:8", "const:4:8"]]
- 004a5588 ["CALLIND", null, ["register:0:8"]]
+ 004a55c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a55c8 ["INT_ADD", "register:40f0:8", ["const:4a55c8:8", "const:4:8"]]
+ 004a55c8 ["CALLIND", null, ["register:0:8"]]
- 004a5588 bytes 00013fd6
+ 004a55c8 bytes 00013fd6
~~~


<a id="compare-d8abd1c563d597682958c37bb580ff43"></a>

### [`004a594c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a594c.md) → [`004a598c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a598c.md) _ZN5Botan11BER_Decoder6decodeERNS_11ASN1_ObjectENS_8ASN1_TagES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a596c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a594c.md#insn-004a596c)
- 新版 [`004a59ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a598c.md#insn-004a59ac)

~~~diff
- 004a596c ["COPY", "register:0:8", ["register:4040:8"]]
- 004a596c ["INT_ADD", "register:40f0:8", ["const:4a596c:8", "const:4:8"]]
- 004a596c ["CALLIND", null, ["register:0:8"]]
+ 004a59ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a59ac ["INT_ADD", "register:40f0:8", ["const:4a59ac:8", "const:4:8"]]
+ 004a59ac ["CALLIND", null, ["register:0:8"]]
- 004a596c bytes 00013fd6
+ 004a59ac bytes 00013fd6
~~~


<a id="compare-58372e2ce2d0a7841bcd962af2ef665f"></a>

### [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) → [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) FUN_004a59c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md) [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) [`0051f1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a5fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md) [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) [`0051f234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a59d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md#insn-004a59d0) · [`004a5a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md#insn-004a5a04) · [`004a5a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md#insn-004a5a48)
- 新版 [`004a5a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a10) · [`004a5a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a44) · [`004a5a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a88)

~~~diff
- 004a59d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a59d0 ["INT_ADD", "register:40f0:8", ["const:4a59d0:8", "const:4:8"]]
- 004a59d0 ["CALLIND", null, ["register:0:8"]]
+ 004a5a10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5a10 ["INT_ADD", "register:40f0:8", ["const:4a5a10:8", "const:4:8"]]
+ 004a5a10 ["CALLIND", null, ["register:0:8"]]
- 004a59d0 bytes 00013fd6
+ 004a5a10 bytes 00013fd6
- 004a5a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5a04 ["INT_ADD", "register:40f0:8", ["const:4a5a04:8", "const:4:8"]]
- 004a5a04 ["CALLIND", null, ["register:0:8"]]
+ 004a5a44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5a44 ["INT_ADD", "register:40f0:8", ["const:4a5a44:8", "const:4:8"]]
+ 004a5a44 ["CALLIND", null, ["register:0:8"]]
- 004a5a04 bytes 00013fd6
+ 004a5a44 bytes 00013fd6
- 004a5a48 ["INT_ADD", "register:40f0:8", ["const:4a5a48:8", "const:4:8"]]
- 004a5a48 ["CALL", null, ["callee:00c57f60:8"]]
+ 004a5a88 ["INT_ADD", "register:40f0:8", ["const:4a5a88:8", "const:4:8"]]
+ 004a5a88 ["CALL", null, ["callee:00c57f60:8"]]
- 004a5a48 bytes 12c91e94
+ 004a5a88 bytes 36c91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0a9257a34aba70095db9b71dd95a3d"></a>

### [`004a5ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ebc.md) → [`004a5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md) _ZNK5Botan9Attribute11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) [`00c586c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ebc.md#insn-004a5ee4) · [`004a5ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ebc.md#insn-004a5ef8) · [`004a5f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ebc.md#insn-004a5f08)
- 新版 [`004a5f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f24) · [`004a5f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f38) · [`004a5f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f48)

~~~diff
- 004a5ee4 ["INT_ADD", "register:40f0:8", ["const:4a5ee4:8", "const:4:8"]]
- 004a5ee4 ["CALL", null, ["callee:00c58780:8"]]
+ 004a5f24 ["INT_ADD", "register:40f0:8", ["const:4a5f24:8", "const:4:8"]]
+ 004a5f24 ["CALL", null, ["callee:00c58780:8"]]
- 004a5ee4 bytes f3c91e94
+ 004a5f24 bytes 17ca1e94
- 004a5ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5ef8 ["INT_ADD", "register:40f0:8", ["const:4a5ef8:8", "const:4:8"]]
- 004a5ef8 ["CALLIND", null, ["register:0:8"]]
+ 004a5f38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5f38 ["INT_ADD", "register:40f0:8", ["const:4a5f38:8", "const:4:8"]]
+ 004a5f38 ["CALLIND", null, ["register:0:8"]]
- 004a5ef8 bytes 00013fd6
+ 004a5f38 bytes 00013fd6
- 004a5f08 ["INT_ADD", "register:40f0:8", ["const:4a5f08:8", "const:4:8"]]
- 004a5f08 ["CALL", null, ["callee:00c58780:8"]]
+ 004a5f48 ["INT_ADD", "register:40f0:8", ["const:4a5f48:8", "const:4:8"]]
+ 004a5f48 ["CALL", null, ["callee:00c58780:8"]]
- 004a5f08 bytes eac91e94
+ 004a5f48 bytes 0eca1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e80da11e188e191f3a54cfe8f8deaedf"></a>

### [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) → [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) FUN_004a688c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`004af484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md) [`004bc3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md) [`004bef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md) [`004d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7edc.md) [`004e8e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8e00.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 12件 [`004af4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4c4.md) [`004bc3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md) [`004bef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md) [`004d7f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7f1c.md) [`004e8e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8e40.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a6874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md#insn-004a6874)
- 新版 [`004a68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md#insn-004a68b4)

~~~diff
- 004a6874 ["INT_ADD", "register:40f0:8", ["const:4a6874:8", "const:4:8"]]
- 004a6874 ["CALL", null, ["callee:00c58050:8"]]
+ 004a68b4 ["INT_ADD", "register:40f0:8", ["const:4a68b4:8", "const:4:8"]]
+ 004a68b4 ["CALL", null, ["callee:00c58050:8"]]
- 004a6874 bytes c3c51e94
+ 004a68b4 bytes e7c51e94
~~~


<a id="compare-9b0c3d6d93f81e21a3ae9a811ef89cca"></a>

### [`004a7c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md) → [`004a7c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md) _ZN5Botan3OIDpLEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58810.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c588e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588e0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a7c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md#insn-004a7c84) · [`004a7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md#insn-004a7cb0) · [`004a7cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7c08.md#insn-004a7cc4)
- 新版 [`004a7cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7cc4) · [`004a7cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7cf0) · [`004a7d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7d04)

~~~diff
- 004a7c84 ["INT_ADD", "register:40f0:8", ["const:4a7c84:8", "const:4:8"]]
- 004a7c84 ["CALL", null, ["callee:00c57f60:8"]]
+ 004a7cc4 ["INT_ADD", "register:40f0:8", ["const:4a7cc4:8", "const:4:8"]]
+ 004a7cc4 ["CALL", null, ["callee:00c57f60:8"]]
- 004a7c84 bytes 83c01e94
+ 004a7cc4 bytes a7c01e94
- 004a7cb0 ["INT_ADD", "register:40f0:8", ["const:4a7cb0:8", "const:4:8"]]
- 004a7cb0 ["CALL", null, ["callee:00c580d0:8"]]
+ 004a7cf0 ["INT_ADD", "register:40f0:8", ["const:4a7cf0:8", "const:4:8"]]
+ 004a7cf0 ["CALL", null, ["callee:00c580d0:8"]]
- 004a7cb0 bytes d4c01e94
+ 004a7cf0 bytes f8c01e94
- 004a7cc4 ["INT_ADD", "register:40f0:8", ["const:4a7cc4:8", "const:4:8"]]
- 004a7cc4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004a7d04 ["INT_ADD", "register:40f0:8", ["const:4a7d04:8", "const:4:8"]]
+ 004a7d04 ["CALL", null, ["callee:00c57f80:8"]]
- 004a7cc4 bytes 7bc01e94
+ 004a7d04 bytes 9fc01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4fb8bde29ddfc1c1209c226563ec92"></a>

### [`004ac028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac028.md) → [`004ac068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md) _ZN5Botan6BigInt6encodeERKS0_NS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c588d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588d0.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) [`00c58950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md)
- 新版 呼出元 1件 [`00c589a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589a0.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) [`00c58a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac028.md#insn-004ac048) · [`004ac064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac028.md#insn-004ac064) · [`004ac080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac028.md#insn-004ac080)
- 新版 [`004ac088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac088) · [`004ac0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac0a4) · [`004ac0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac0c0)

~~~diff
- 004ac048 ["INT_ADD", "register:40f0:8", ["const:4ac048:8", "const:4:8"]]
- 004ac048 ["CALL", null, ["callee:00c58a10:8"]]
+ 004ac088 ["INT_ADD", "register:40f0:8", ["const:4ac088:8", "const:4:8"]]
+ 004ac088 ["CALL", null, ["callee:00c58a10:8"]]
- 004ac048 bytes 3eb21e94
+ 004ac088 bytes 62b21e94
- 004ac064 ["INT_ADD", "register:40f0:8", ["const:4ac064:8", "const:4:8"]]
- 004ac064 ["CALL", null, ["callee:00c57f60:8"]]
+ 004ac0a4 ["INT_ADD", "register:40f0:8", ["const:4ac0a4:8", "const:4:8"]]
+ 004ac0a4 ["CALL", null, ["callee:00c57f60:8"]]
- 004ac064 bytes 8baf1e94
+ 004ac0a4 bytes afaf1e94
- 004ac080 ["INT_ADD", "register:40f0:8", ["const:4ac080:8", "const:4:8"]]
- 004ac080 ["CALL", null, ["callee:00c58160:8"]]
+ 004ac0c0 ["INT_ADD", "register:40f0:8", ["const:4ac0c0:8", "const:4:8"]]
+ 004ac0c0 ["CALL", null, ["callee:00c58160:8"]]
- 004ac080 bytes 04b01e94
+ 004ac0c0 bytes 28b01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f564dea452678f9a23243cebb1e52421"></a>

### [`004ac1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1a0.md) → [`004ac1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac1e0.md) FUN_004ac1e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1a0.md#insn-004ac1bc)
- 新版 [`004ac1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac1e0.md#insn-004ac1fc)

~~~diff
- 004ac1bc ["INT_ADD", "register:40f0:8", ["const:4ac1bc:8", "const:4:8"]]
- 004ac1bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004ac1fc ["INT_ADD", "register:40f0:8", ["const:4ac1fc:8", "const:4:8"]]
+ 004ac1fc ["CALL", null, ["callee:00c57f80:8"]]
- 004ac1bc bytes 3daf1e94
+ 004ac1fc bytes 61af1e94
~~~


<a id="compare-b34f2e2ed1046ce540fabaf57359b2a7"></a>

### [`004acc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md) → [`004acc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md) FUN_004acc64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004acc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md#insn-004acc3c) · [`004acc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md#insn-004acc78) · [`004acc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md#insn-004acc9c)
- 新版 [`004acc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004acc7c) · [`004accb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004accb8) · [`004accdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004accdc)

~~~diff
- 004acc3c ["INT_ADD", "register:40f0:8", ["const:4acc3c:8", "const:4:8"]]
- 004acc3c ["CALL", null, ["callee:00c580b0:8"]]
+ 004acc7c ["INT_ADD", "register:40f0:8", ["const:4acc7c:8", "const:4:8"]]
+ 004acc7c ["CALL", null, ["callee:00c580b0:8"]]
- 004acc3c bytes e9ac1e94
+ 004acc7c bytes 0dad1e94
- 004acc78 ["INT_ADD", "register:40f0:8", ["const:4acc78:8", "const:4:8"]]
- 004acc78 ["CALL", null, ["callee:00c58120:8"]]
+ 004accb8 ["INT_ADD", "register:40f0:8", ["const:4accb8:8", "const:4:8"]]
+ 004accb8 ["CALL", null, ["callee:00c58120:8"]]
- 004acc78 bytes f6ac1e94
+ 004accb8 bytes 1aad1e94
- 004acc9c ["INT_ADD", "register:40f0:8", ["const:4acc9c:8", "const:4:8"]]
- 004acc9c ["CALL", null, ["callee:0044295c:8"]]
+ 004accdc ["INT_ADD", "register:40f0:8", ["const:4accdc:8", "const:4:8"]]
+ 004accdc ["CALL", null, ["callee:0044295c:8"]]
- 004acc9c bytes 2057fe97
+ 004accdc bytes 2057fe97
~~~


<a id="compare-a8d62efef5863d0fd7e24b81a55662d3"></a>

### [`004af160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af160.md) → [`004af1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md) _ZNK5Botan9X509_Time16to_std_timepointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ad0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af160.md#insn-004af190) · [`004af1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af160.md#insn-004af1b4)
- 新版 [`004af1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md#insn-004af1d0) · [`004af1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md#insn-004af1f4)

~~~diff
- 004af190 ["INT_ADD", "register:40f0:8", ["const:4af190:8", "const:4:8"]]
- 004af190 ["CALL", null, ["callee:00c58ad0:8"]]
+ 004af1d0 ["INT_ADD", "register:40f0:8", ["const:4af1d0:8", "const:4:8"]]
+ 004af1d0 ["CALL", null, ["callee:00c58ad0:8"]]
- 004af190 bytes 1ca61e94
+ 004af1d0 bytes 40a61e94
- 004af1b4 ["INT_ADD", "register:40f0:8", ["const:4af1b4:8", "const:4:8"]]
- 004af1b4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004af1f4 ["INT_ADD", "register:40f0:8", ["const:4af1f4:8", "const:4:8"]]
+ 004af1f4 ["CALL", null, ["callee:00c57fb0:8"]]
- 004af1b4 bytes 4ba31e94
+ 004af1f4 bytes 6fa31e94
~~~


<a id="compare-7ece268606c13e4e20b4806fbd6ed409"></a>

### [`004af3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3e0.md) → [`004af420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af420.md) _ZN5BotaneqERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3e0.md#insn-004af3e8)
- 新版 [`004af428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af420.md#insn-004af428)

~~~diff
- 004af3e8 ["INT_ADD", "register:40f0:8", ["const:4af3e8:8", "const:4:8"]]
- 004af3e8 ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af428 ["INT_ADD", "register:40f0:8", ["const:4af428:8", "const:4:8"]]
+ 004af428 ["CALL", null, ["callee:00c58ab0:8"]]
- 004af3e8 bytes 7ea51e94
+ 004af428 bytes a2a51e94
~~~


<a id="compare-47692c928de08031837d6f2ce3b10103"></a>

### [`004af3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3fc.md) → [`004af43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af43c.md) _ZN5BotanneERKNS_9X509_TimeES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af3fc.md#insn-004af404)
- 新版 [`004af444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af43c.md#insn-004af444)

~~~diff
- 004af404 ["INT_ADD", "register:40f0:8", ["const:4af404:8", "const:4:8"]]
- 004af404 ["CALL", null, ["callee:00c58ab0:8"]]
+ 004af444 ["INT_ADD", "register:40f0:8", ["const:4af444:8", "const:4:8"]]
+ 004af444 ["CALL", null, ["callee:00c58ab0:8"]]
- 004af404 bytes 77a51e94
+ 004af444 bytes 9ba51e94
~~~


