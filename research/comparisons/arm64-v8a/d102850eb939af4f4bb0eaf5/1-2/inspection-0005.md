# v16.0.2 → v16.0.3 · 要調査の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-b87e81a7c36e5c00c7b6e39cd88c2113"></a>

### [`0048f450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md) → [`0048f770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f770.md) FUN_0048f770

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0048f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md#insn-0048f46c) · [`0048f48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f450.md#insn-0048f48c)
- 新版 [`0048f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f770.md#insn-0048f78c) · [`0048f7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f770.md#insn-0048f7ac)

~~~diff
- 0048f46c ["INT_ADD", "register:40f0:8", ["const:48f46c:8", "const:4:8"]]
- 0048f46c ["CALL", null, ["callee:00c54d90:8"]]
+ 0048f78c ["INT_ADD", "register:40f0:8", ["const:48f78c:8", "const:4:8"]]
+ 0048f78c ["CALL", null, ["callee:00c54d90:8"]]
- 0048f46c bytes 4d121f94
+ 0048f78c bytes 81151f94
- 0048f48c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f48c ["INT_ADD", "register:40f0:8", ["const:48f48c:8", "const:4:8"]]
- 0048f48c ["CALLIND", null, ["register:0:8"]]
+ 0048f7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f7ac ["INT_ADD", "register:40f0:8", ["const:48f7ac:8", "const:4:8"]]
+ 0048f7ac ["CALLIND", null, ["register:0:8"]]
- 0048f48c bytes 00013fd6
+ 0048f7ac bytes 00013fd6
~~~


<a id="compare-d38423b714a0744da2a423df61e8c79e"></a>

### [`00492804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md) → [`00492b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492b24.md) FUN_00492b24

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-00492850) · [`00492864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-00492864) · [`0049286c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492804.md#insn-0049286c)
- 新版 [`00492b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492b24.md#insn-00492b70) · [`00492b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492b24.md#insn-00492b84) · [`00492b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492b24.md#insn-00492b8c)

~~~diff
- 00492850 ["INT_ADD", "register:40f0:8", ["const:492850:8", "const:4:8"]]
- 00492850 ["CALL", null, ["callee:00c54d90:8"]]
+ 00492b70 ["INT_ADD", "register:40f0:8", ["const:492b70:8", "const:4:8"]]
+ 00492b70 ["CALL", null, ["callee:00c54d90:8"]]
- 00492850 bytes 54051f94
+ 00492b70 bytes 88081f94
- 00492864 ["COPY", "register:0:8", ["register:4040:8"]]
- 00492864 ["INT_ADD", "register:40f0:8", ["const:492864:8", "const:4:8"]]
- 00492864 ["CALLIND", null, ["register:0:8"]]
+ 00492b84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492b84 ["INT_ADD", "register:40f0:8", ["const:492b84:8", "const:4:8"]]
+ 00492b84 ["CALLIND", null, ["register:0:8"]]
- 00492864 bytes 00013fd6
+ 00492b84 bytes 00013fd6
- 0049286c ["INT_ADD", "register:40f0:8", ["const:49286c:8", "const:4:8"]]
- 0049286c ["CALL", null, ["callee:00c58f20:8"]]
+ 00492b8c ["INT_ADD", "register:40f0:8", ["const:492b8c:8", "const:4:8"]]
+ 00492b8c ["CALL", null, ["callee:00c58f20:8"]]
- 0049286c bytes b9151f94
+ 00492b8c bytes e5181f94
~~~


<a id="compare-e115ba704ce54b941513fc5ed08fc7f2"></a>

### [`0049289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md) → [`00492bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492bbc.md) FUN_00492bbc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004928b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md#insn-004928b8) · [`004928d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/0049289c.md#insn-004928d8)
- 新版 [`00492bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492bbc.md#insn-00492bd8) · [`00492bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492bbc.md#insn-00492bf8)

~~~diff
- 004928b8 ["INT_ADD", "register:40f0:8", ["const:4928b8:8", "const:4:8"]]
- 004928b8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00492bd8 ["INT_ADD", "register:40f0:8", ["const:492bd8:8", "const:4:8"]]
+ 00492bd8 ["CALL", null, ["callee:00c54d90:8"]]
- 004928b8 bytes 3a051f94
+ 00492bd8 bytes 6e081f94
- 004928d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004928d8 ["INT_ADD", "register:40f0:8", ["const:4928d8:8", "const:4:8"]]
- 004928d8 ["CALLIND", null, ["register:0:8"]]
+ 00492bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492bf8 ["INT_ADD", "register:40f0:8", ["const:492bf8:8", "const:4:8"]]
+ 00492bf8 ["CALLIND", null, ["register:0:8"]]
- 004928d8 bytes 00013fd6
+ 00492bf8 bytes 00013fd6
~~~


<a id="compare-730bc56c8449bed5cafce1188625cf11"></a>

### [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) → [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md) FUN_00493064

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 27件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) [`00872078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872078.md) [`008722a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008722a8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 27件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00866114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866114.md) [`00873024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873024.md) [`00873254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873254.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dac) · [`00492dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dbc) · [`00492dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md#insn-00492dcc)
- 新版 [`004930cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md#insn-004930cc) · [`004930dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md#insn-004930dc) · [`004930ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md#insn-004930ec)

~~~diff
- 00492dac ["INT_ADD", "register:40f0:8", ["const:492dac:8", "const:4:8"]]
- 00492dac ["CALL", null, ["callee:0043be80:8"]]
+ 004930cc ["INT_ADD", "register:40f0:8", ["const:4930cc:8", "const:4:8"]]
+ 004930cc ["CALL", null, ["callee:0043be80:8"]]
- 00492dac bytes 6da3fe97
+ 004930cc bytes 6da3fe97
- 00492dbc ["INT_ADD", "register:40f0:8", ["const:492dbc:8", "const:4:8"]]
- 00492dbc ["CALL", null, ["callee:00493168:8"]]
+ 004930dc ["INT_ADD", "register:40f0:8", ["const:4930dc:8", "const:4:8"]]
+ 004930dc ["CALL", null, ["callee:00493168:8"]]
- 00492dbc bytes 23000094
+ 004930dc bytes 23000094
- 00492dcc ["INT_ADD", "register:40f0:8", ["const:492dcc:8", "const:4:8"]]
- 00492dcc ["CALL", null, ["callee:00c58f50:8"]]
+ 004930ec ["INT_ADD", "register:40f0:8", ["const:4930ec:8", "const:4:8"]]
+ 004930ec ["CALL", null, ["callee:00c58f50:8"]]
- 00492dcc bytes 6d141f94
+ 004930ec bytes 99171f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701c9473a126bfe88754e4f0da3e3836"></a>

### [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) → [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md) FUN_00493168

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 96件 [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`005b9b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9b94.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`005d9f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d9/005d9f8c.md) [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 96件 [`00493064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493064.md) [`005b9f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b9/005b9f44.md) [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) [`005da33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da33c.md) [`005e1fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1fa8.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492e98) · [`00492eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492eac) · [`00492ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md#insn-00492ed8)
- 新版 [`004931b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md#insn-004931b8) · [`004931cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md#insn-004931cc) · [`004931f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md#insn-004931f8)

~~~diff
- 00492e98 ["INT_ADD", "register:40f0:8", ["const:492e98:8", "const:4:8"]]
- 00492e98 ["CALL", null, ["callee:0043be80:8"]]
+ 004931b8 ["INT_ADD", "register:40f0:8", ["const:4931b8:8", "const:4:8"]]
+ 004931b8 ["CALL", null, ["callee:0043be80:8"]]
- 00492e98 bytes 32a3fe97
+ 004931b8 bytes 32a3fe97
- 00492eac ["INT_ADD", "register:40f0:8", ["const:492eac:8", "const:4:8"]]
- 00492eac ["CALL", null, ["callee:0043be80:8"]]
+ 004931cc ["INT_ADD", "register:40f0:8", ["const:4931cc:8", "const:4:8"]]
+ 004931cc ["CALL", null, ["callee:0043be80:8"]]
- 00492eac bytes 2da3fe97
+ 004931cc bytes 2da3fe97
- 00492ed8 ["INT_ADD", "register:40f0:8", ["const:492ed8:8", "const:4:8"]]
- 00492ed8 ["CALL", null, ["callee:00442274:8"]]
+ 004931f8 ["INT_ADD", "register:40f0:8", ["const:4931f8:8", "const:4:8"]]
+ 004931f8 ["CALL", null, ["callee:00442274:8"]]
- 00492ed8 bytes 1fbcfe97
+ 004931f8 bytes 1fbcfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3548d2b8f63c3c4829c7b07f6ad204"></a>

### [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md) → [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md) FUN_00493288

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ae9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md) [`007aefa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 5件 [`00493048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 25件 [`00482e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482e6c.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`007af1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af1d4.md) [`007af78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af78c.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 5件 [`00493368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493368.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fa8) · [`00492fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fbc) · [`00492fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md#insn-00492fd0)
- 新版 [`004932c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md#insn-004932c8) · [`004932dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md#insn-004932dc) · [`004932f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md#insn-004932f0)

~~~diff
- 00492fa8 ["INT_ADD", "register:40f0:8", ["const:492fa8:8", "const:4:8"]]
- 00492fa8 ["CALL", null, ["callee:00493368:8"]]
+ 004932c8 ["INT_ADD", "register:40f0:8", ["const:4932c8:8", "const:4:8"]]
+ 004932c8 ["CALL", null, ["callee:00493368:8"]]
- 00492fa8 bytes 28000094
+ 004932c8 bytes 28000094
- 00492fbc ["INT_ADD", "register:40f0:8", ["const:492fbc:8", "const:4:8"]]
- 00492fbc ["CALL", null, ["callee:00c54d90:8"]]
+ 004932dc ["INT_ADD", "register:40f0:8", ["const:4932dc:8", "const:4:8"]]
+ 004932dc ["CALL", null, ["callee:00c54d90:8"]]
- 00492fbc bytes 79031f94
+ 004932dc bytes ad061f94
- 00492fd0 ["INT_ADD", "register:40f0:8", ["const:492fd0:8", "const:4:8"]]
- 00492fd0 ["CALL", null, ["callee:00c58f50:8"]]
+ 004932f0 ["INT_ADD", "register:40f0:8", ["const:4932f0:8", "const:4:8"]]
+ 004932f0 ["CALL", null, ["callee:00c58f50:8"]]
- 00492fd0 bytes ec131f94
+ 004932f0 bytes 18171f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c14cb4df35d583c0baff1d549932647"></a>

### [`004936d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md) → [`004939f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/004939f0.md) FUN_004939f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 16件 [`005b17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b17f8.md) [`005b1bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1bc4.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061308c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 5件 [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 16件 [`005b1ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b1/005b1ba8.md) [`005b1f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b1/005b1f74.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0061343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00613/0061343c.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 5件 [`00550d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d70.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493714) · [`00493740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493740) · [`00493750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md#insn-00493750)
- 新版 [`00493a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/004939f0.md#insn-00493a34) · [`00493a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/004939f0.md#insn-00493a60) · [`00493a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/004939f0.md#insn-00493a70)

~~~diff
- 00493714 ["INT_ADD", "register:40f0:8", ["const:493714:8", "const:4:8"]]
- 00493714 ["CALL", null, ["callee:00550d70:8"]]
+ 00493a34 ["INT_ADD", "register:40f0:8", ["const:493a34:8", "const:4:8"]]
+ 00493a34 ["CALL", null, ["callee:00550d70:8"]]
- 00493714 bytes cff40294
+ 00493a34 bytes cff40294
- 00493740 ["COPY", "register:0:8", ["register:4040:8"]]
- 00493740 ["INT_ADD", "register:40f0:8", ["const:493740:8", "const:4:8"]]
- 00493740 ["CALLIND", null, ["register:0:8"]]
+ 00493a60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493a60 ["INT_ADD", "register:40f0:8", ["const:493a60:8", "const:4:8"]]
+ 00493a60 ["CALLIND", null, ["register:0:8"]]
- 00493740 bytes 00013fd6
+ 00493a60 bytes 00013fd6
- 00493750 ["COPY", "register:0:8", ["register:4040:8"]]
- 00493750 ["INT_ADD", "register:40f0:8", ["const:493750:8", "const:4:8"]]
- 00493750 ["CALLIND", null, ["register:0:8"]]
+ 00493a70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493a70 ["INT_ADD", "register:40f0:8", ["const:493a70:8", "const:4:8"]]
+ 00493a70 ["CALLIND", null, ["register:0:8"]]
- 00493750 bytes 00013fd6
+ 00493a70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff985bce0527e02408aec92612fda843"></a>

### [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) → [`00493c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md) FUN_00493c34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0047a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a02c.md) [`007ad8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md) [`007ad9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md) [`007ae8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 8件 [`0047a34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047a/0047a34c.md) [`007adcc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ad/007adcc4.md) [`007ade00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ad/007ade00.md) [`007af090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af090.md) [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) · 呼出先 3件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-00493940) · [`00493958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-00493958) · [`0049396c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md#insn-0049396c)
- 新版 [`00493c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md#insn-00493c60) · [`00493c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md#insn-00493c78) · [`00493c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md#insn-00493c8c)

~~~diff
- 00493940 ["COPY", "register:0:8", ["register:4048:8"]]
- 00493940 ["INT_ADD", "register:40f0:8", ["const:493940:8", "const:4:8"]]
- 00493940 ["CALLIND", null, ["register:0:8"]]
+ 00493c60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00493c60 ["INT_ADD", "register:40f0:8", ["const:493c60:8", "const:4:8"]]
+ 00493c60 ["CALLIND", null, ["register:0:8"]]
- 00493940 bytes 20013fd6
+ 00493c60 bytes 20013fd6
- 00493958 ["INT_ADD", "register:40f0:8", ["const:493958:8", "const:4:8"]]
- 00493958 ["CALL", null, ["callee:00c54d90:8"]]
+ 00493c78 ["INT_ADD", "register:40f0:8", ["const:493c78:8", "const:4:8"]]
+ 00493c78 ["CALL", null, ["callee:00c54d90:8"]]
- 00493958 bytes 12011f94
+ 00493c78 bytes 46041f94
- 0049396c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049396c ["INT_ADD", "register:40f0:8", ["const:49396c:8", "const:4:8"]]
- 0049396c ["CALLIND", null, ["register:0:8"]]
+ 00493c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493c8c ["INT_ADD", "register:40f0:8", ["const:493c8c:8", "const:4:8"]]
+ 00493c8c ["CALLIND", null, ["register:0:8"]]
- 0049396c bytes 00013fd6
+ 00493c8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19f5ef9b054966a0a903214b190a81f9"></a>

### [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) → [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) FUN_00493cf8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 50件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`00612324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00612/00612324.md) [`0062ed3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062e/0062ed3c.md) [`006452d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/006452d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 50件 [`0043dadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md) [`005f4a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f4/005f4a9c.md) [`006126d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00612/006126d4.md) [`0062f0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062f/0062f0ec.md) [`00645684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/00645684.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md#insn-00493a44)
- 新版 [`00493d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md#insn-00493d64)

~~~diff
- 00493a44 ["INT_ADD", "register:40f0:8", ["const:493a44:8", "const:4:8"]]
- 00493a44 ["CALL", null, ["callee:00c590f0:8"]]
+ 00493d64 ["INT_ADD", "register:40f0:8", ["const:493d64:8", "const:4:8"]]
+ 00493d64 ["CALL", null, ["callee:00c590f0:8"]]
- 00493a44 bytes b7111f94
+ 00493d64 bytes e3141f94
~~~


<a id="compare-bf352b489e842ea1535fbacfc96086f6"></a>

### [`00493a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md) → [`00493da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493da8.md) FUN_00493da8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 4件 [`00865914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/00865914.md) [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) [`00b2d4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d4e0.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b14) · [`00493b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b34) · [`00493b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md#insn-00493b54)
- 新版 [`00493e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493da8.md#insn-00493e34) · [`00493e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493da8.md#insn-00493e54) · [`00493e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493da8.md#insn-00493e74)

~~~diff
- 00493b14 ["INT_ADD", "register:40f0:8", ["const:493b14:8", "const:4:8"]]
- 00493b14 ["CALL", null, ["callee:00c58f30:8"]]
+ 00493e34 ["INT_ADD", "register:40f0:8", ["const:493e34:8", "const:4:8"]]
+ 00493e34 ["CALL", null, ["callee:00c58f30:8"]]
- 00493b14 bytes 13111f94
+ 00493e34 bytes 3f141f94
- 00493b34 ["INT_ADD", "register:40f0:8", ["const:493b34:8", "const:4:8"]]
- 00493b34 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00493e54 ["INT_ADD", "register:40f0:8", ["const:493e54:8", "const:4:8"]]
+ 00493e54 ["CALL", null, ["callee:00c58fe0:8"]]
- 00493b34 bytes 37111f94
+ 00493e54 bytes 63141f94
- 00493b54 ["INT_ADD", "register:40f0:8", ["const:493b54:8", "const:4:8"]]
- 00493b54 ["CALL", null, ["callee:00442c7c:8"]]
+ 00493e74 ["INT_ADD", "register:40f0:8", ["const:493e74:8", "const:4:8"]]
+ 00493e74 ["CALL", null, ["callee:00442c7c:8"]]
- 00493b54 bytes 82bbfe97
+ 00493e74 bytes 82bbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4102b6736a2e83f35e9481b247867606"></a>

### [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) → [`00493fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md) FUN_00493fe0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md)
- 新版 呼出元 7件 [`007ac83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac83c.md) [`00865914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/00865914.md) [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00494128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md#insn-00493cd4)
- 新版 [`00493ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md#insn-00493ff4)

~~~diff
- 00493cd4 ["INT_ADD", "register:40f0:8", ["const:493cd4:8", "const:4:8"]]
- 00493cd4 ["CALL", null, ["callee:00494128:8"]]
+ 00493ff4 ["INT_ADD", "register:40f0:8", ["const:493ff4:8", "const:4:8"]]
+ 00493ff4 ["CALL", null, ["callee:00494128:8"]]
- 00493cd4 bytes 4d000094
+ 00493ff4 bytes 4d000094
~~~


<a id="compare-fa12b764fe0fef05ee74802ca36de7c9"></a>

### [`00493d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md) → [`00494048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494048.md) FUN_00494048

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 7件 [`007ac83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac83c.md) [`00865914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/00865914.md) [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md#insn-00493d98) · [`00493dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md#insn-00493dc0)
- 新版 [`004940b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494048.md#insn-004940b8) · [`004940e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494048.md#insn-004940e0)

~~~diff
- 00493d98 ["INT_ADD", "register:40f0:8", ["const:493d98:8", "const:4:8"]]
- 00493d98 ["CALL", null, ["callee:00c590f0:8"]]
+ 004940b8 ["INT_ADD", "register:40f0:8", ["const:4940b8:8", "const:4:8"]]
+ 004940b8 ["CALL", null, ["callee:00c590f0:8"]]
- 00493d98 bytes e2101f94
+ 004940b8 bytes 0e141f94
- 00493dc0 ["INT_ADD", "register:40f0:8", ["const:493dc0:8", "const:4:8"]]
- 00493dc0 ["CALL", null, ["callee:00c590f0:8"]]
+ 004940e0 ["INT_ADD", "register:40f0:8", ["const:4940e0:8", "const:4:8"]]
+ 004940e0 ["CALL", null, ["callee:00c590f0:8"]]
- 00493dc0 bytes d8101f94
+ 004940e0 bytes 04141f94
~~~


<a id="compare-6bb190cd5a3326874bb46b51889595fa"></a>

### [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) → [`00494128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md) FUN_00494128

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) [`00563ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563ca0.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md) [`0087d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md) [`00b59d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 7件 [`00493fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md) [`00563fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563fc0.md) [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md) [`0087e2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e2a4.md) [`00b5ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5ad34.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00493e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md#insn-00493e74) · [`00493ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md#insn-00493ed0)
- 新版 [`00494194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md#insn-00494194) · [`004941f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md#insn-004941f0)

~~~diff
- 00493e74 ["INT_ADD", "register:40f0:8", ["const:493e74:8", "const:4:8"]]
- 00493e74 ["CALL", null, ["callee:00c590f0:8"]]
+ 00494194 ["INT_ADD", "register:40f0:8", ["const:494194:8", "const:4:8"]]
+ 00494194 ["CALL", null, ["callee:00c590f0:8"]]
- 00493e74 bytes ab101f94
+ 00494194 bytes d7131f94
- 00493ed0 ["INT_ADD", "register:40f0:8", ["const:493ed0:8", "const:4:8"]]
- 00493ed0 ["CALL", null, ["callee:00c590f0:8"]]
+ 004941f0 ["INT_ADD", "register:40f0:8", ["const:4941f0:8", "const:4:8"]]
+ 004941f0 ["CALL", null, ["callee:00c590f0:8"]]
- 00493ed0 bytes 94101f94
+ 004941f0 bytes c0131f94
~~~


<a id="compare-fa363e0aeb589aeaa6dc7ba30d63e842"></a>

### [`00494348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md) → [`00494668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494668.md) FUN_00494668

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004943b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943b8) · [`004943cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943cc) · [`004943d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494348.md#insn-004943d4)
- 新版 [`004946d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494668.md#insn-004946d8) · [`004946ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494668.md#insn-004946ec) · [`004946f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494668.md#insn-004946f4)

~~~diff
- 004943b8 ["INT_ADD", "register:40f0:8", ["const:4943b8:8", "const:4:8"]]
- 004943b8 ["CALL", null, ["callee:00c54d90:8"]]
+ 004946d8 ["INT_ADD", "register:40f0:8", ["const:4946d8:8", "const:4:8"]]
+ 004946d8 ["CALL", null, ["callee:00c54d90:8"]]
- 004943b8 bytes 7afe1e94
+ 004946d8 bytes ae011f94
- 004943cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004943cc ["INT_ADD", "register:40f0:8", ["const:4943cc:8", "const:4:8"]]
- 004943cc ["CALLIND", null, ["register:0:8"]]
+ 004946ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004946ec ["INT_ADD", "register:40f0:8", ["const:4946ec:8", "const:4:8"]]
+ 004946ec ["CALLIND", null, ["register:0:8"]]
- 004943cc bytes 00013fd6
+ 004946ec bytes 00013fd6
- 004943d4 ["INT_ADD", "register:40f0:8", ["const:4943d4:8", "const:4:8"]]
- 004943d4 ["CALL", null, ["callee:00c58f20:8"]]
+ 004946f4 ["INT_ADD", "register:40f0:8", ["const:4946f4:8", "const:4:8"]]
+ 004946f4 ["CALL", null, ["callee:00c58f20:8"]]
- 004943d4 bytes df0e1f94
+ 004946f4 bytes 0b121f94
~~~


<a id="compare-ee4d812d748d9bb2acfdb4a4e6c61c33"></a>

### [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) → [`0049471c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md) FUN_0049471c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00493314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493314.md) [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) · 呼出先 4件 [`004943fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00493634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493634.md) [`0049471c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md) · 呼出先 4件 [`0049471c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494418) · [`00494424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494424) · [`00494438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004943fc.md#insn-00494438)
- 新版 [`00494738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md#insn-00494738) · [`00494744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md#insn-00494744) · [`00494758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049471c.md#insn-00494758)

~~~diff
- 00494418 ["INT_ADD", "register:40f0:8", ["const:494418:8", "const:4:8"]]
- 00494418 ["CALL", null, ["local:b0:8"]]
+ 00494738 ["INT_ADD", "register:40f0:8", ["const:494738:8", "const:4:8"]]
+ 00494738 ["CALL", null, ["local:b0:8"]]
- 00494418 bytes f9ffff97
+ 00494738 bytes f9ffff97
- 00494424 ["INT_ADD", "register:40f0:8", ["const:494424:8", "const:4:8"]]
- 00494424 ["CALL", null, ["local:b0:8"]]
+ 00494744 ["INT_ADD", "register:40f0:8", ["const:494744:8", "const:4:8"]]
+ 00494744 ["CALL", null, ["local:b0:8"]]
- 00494424 bytes f6ffff97
+ 00494744 bytes f6ffff97
- 00494438 ["INT_ADD", "register:40f0:8", ["const:494438:8", "const:4:8"]]
- 00494438 ["CALL", null, ["callee:00c54d90:8"]]
+ 00494758 ["INT_ADD", "register:40f0:8", ["const:494758:8", "const:4:8"]]
+ 00494758 ["CALL", null, ["callee:00c54d90:8"]]
- 00494438 bytes 5afe1e94
+ 00494758 bytes 8e011f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8147aba775128e4ad29cebc6ee7b961"></a>

### [`00494554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md) → [`00494874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494874.md) FUN_00494874

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004944cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944cc.md) [`00494c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md) · 呼出先 4件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`004947ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947ec.md) [`00494f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494f2c.md) · 呼出先 4件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-00494604) · [`00494618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-00494618) · [`0049462c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md#insn-0049462c)
- 新版 [`00494924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494874.md#insn-00494924) · [`00494938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494874.md#insn-00494938) · [`0049494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494874.md#insn-0049494c)

~~~diff
- 00494604 ["INT_ADD", "register:40f0:8", ["const:494604:8", "const:4:8"]]
- 00494604 ["CALL", null, ["callee:00494970:8"]]
+ 00494924 ["INT_ADD", "register:40f0:8", ["const:494924:8", "const:4:8"]]
+ 00494924 ["CALL", null, ["callee:00494970:8"]]
- 00494604 bytes 13000094
+ 00494924 bytes 13000094
- 00494618 ["INT_ADD", "register:40f0:8", ["const:494618:8", "const:4:8"]]
- 00494618 ["CALL", null, ["callee:00c54d90:8"]]
+ 00494938 ["INT_ADD", "register:40f0:8", ["const:494938:8", "const:4:8"]]
+ 00494938 ["CALL", null, ["callee:00c54d90:8"]]
- 00494618 bytes e2fd1e94
+ 00494938 bytes 16011f94
- 0049462c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049462c ["INT_ADD", "register:40f0:8", ["const:49462c:8", "const:4:8"]]
- 0049462c ["CALLIND", null, ["register:0:8"]]
+ 0049494c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049494c ["INT_ADD", "register:40f0:8", ["const:49494c:8", "const:4:8"]]
+ 0049494c ["CALLIND", null, ["register:0:8"]]
- 0049462c bytes 00013fd6
+ 0049494c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7fb921007dae7c0d4f870a2954c3ab1"></a>

### [`00494bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494bbc.md) → [`00494edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494edc.md) FUN_00494edc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049331c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049363c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494bbc.md#insn-00494bf8)
- 新版 [`00494f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494edc.md#insn-00494f18)

~~~diff
- 00494bf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494bf8 ["INT_ADD", "register:40f0:8", ["const:494bf8:8", "const:4:8"]]
- 00494bf8 ["CALLIND", null, ["register:0:8"]]
+ 00494f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494f18 ["INT_ADD", "register:40f0:8", ["const:494f18:8", "const:4:8"]]
+ 00494f18 ["CALLIND", null, ["register:0:8"]]
- 00494bf8 bytes 00013fd6
+ 00494f18 bytes 00013fd6
~~~


<a id="compare-8dd22e0542ecf73d8af08587c723d49a"></a>

### [`00494cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md) → [`00494fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494fdc.md) FUN_00494fdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0048e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`004fe468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md) [`00797024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md) [`007aaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 8件 [`0048e4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e4f4.md) [`004fe788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fe788.md) [`00797400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797400.md) [`007aae5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007aa/007aae5c.md) [`00865914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/00865914.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d908.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494cf0) · [`00494d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494d10) · [`00494d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md#insn-00494d4c)
- 新版 [`00495010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494fdc.md#insn-00495010) · [`00495030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494fdc.md#insn-00495030) · [`0049506c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494fdc.md#insn-0049506c)

~~~diff
- 00494cf0 ["INT_ADD", "register:40f0:8", ["const:494cf0:8", "const:4:8"]]
- 00494cf0 ["CALL", null, ["callee:0046d908:8"]]
+ 00495010 ["INT_ADD", "register:40f0:8", ["const:495010:8", "const:4:8"]]
+ 00495010 ["CALL", null, ["callee:0046d908:8"]]
- 00494cf0 bytes 3e62ff97
+ 00495010 bytes 3e62ff97
- 00494d10 ["INT_ADD", "register:40f0:8", ["const:494d10:8", "const:4:8"]]
- 00494d10 ["CALL", null, ["callee:00c58f30:8"]]
+ 00495030 ["INT_ADD", "register:40f0:8", ["const:495030:8", "const:4:8"]]
+ 00495030 ["CALL", null, ["callee:00c58f30:8"]]
- 00494d10 bytes 940c1f94
+ 00495030 bytes c00f1f94
- 00494d4c ["INT_ADD", "register:40f0:8", ["const:494d4c:8", "const:4:8"]]
- 00494d4c ["CALL", null, ["callee:0043be80:8"]]
+ 0049506c ["INT_ADD", "register:40f0:8", ["const:49506c:8", "const:4:8"]]
+ 0049506c ["CALL", null, ["callee:0043be80:8"]]
- 00494d4c bytes 859bfe97
+ 0049506c bytes 859bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b1cdd353a737cf7ce43dccee3ab2181"></a>

### [`00494dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md) → [`0049510c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/0049510c.md) FUN_0049510c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md#insn-00494e18) · [`00494e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494dec.md#insn-00494e28)
- 新版 [`00495138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/0049510c.md#insn-00495138) · [`00495148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/0049510c.md#insn-00495148)

~~~diff
- 00494e18 ["INT_ADD", "register:40f0:8", ["const:494e18:8", "const:4:8"]]
- 00494e18 ["CALL", null, ["callee:00c58f50:8"]]
+ 00495138 ["INT_ADD", "register:40f0:8", ["const:495138:8", "const:4:8"]]
+ 00495138 ["CALL", null, ["callee:00c58f50:8"]]
- 00494e18 bytes 5a0c1f94
+ 00495138 bytes 860f1f94
- 00494e28 ["INT_ADD", "register:40f0:8", ["const:494e28:8", "const:4:8"]]
- 00494e28 ["CALL", null, ["callee:00c58f50:8"]]
+ 00495148 ["INT_ADD", "register:40f0:8", ["const:495148:8", "const:4:8"]]
+ 00495148 ["CALL", null, ["callee:00c58f50:8"]]
- 00494e28 bytes 560c1f94
+ 00495148 bytes 820f1f94
~~~


<a id="compare-ddfea181cb5956d417440845b33f9c4b"></a>

### [`00495ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md) → [`00495ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495ec4.md) FUN_00495ec4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md#insn-00495bc0) · [`00495be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495ba4.md#insn-00495be0)
- 新版 [`00495ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495ec4.md#insn-00495ee0) · [`00495f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495ec4.md#insn-00495f00)

~~~diff
- 00495bc0 ["INT_ADD", "register:40f0:8", ["const:495bc0:8", "const:4:8"]]
- 00495bc0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00495ee0 ["INT_ADD", "register:40f0:8", ["const:495ee0:8", "const:4:8"]]
+ 00495ee0 ["CALL", null, ["callee:00c54d90:8"]]
- 00495bc0 bytes 78f81e94
+ 00495ee0 bytes acfb1e94
- 00495be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495be0 ["INT_ADD", "register:40f0:8", ["const:495be0:8", "const:4:8"]]
- 00495be0 ["CALLIND", null, ["register:0:8"]]
+ 00495f00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495f00 ["INT_ADD", "register:40f0:8", ["const:495f00:8", "const:4:8"]]
+ 00495f00 ["CALLIND", null, ["register:0:8"]]
- 00495be0 bytes 00013fd6
+ 00495f00 bytes 00013fd6
~~~


<a id="compare-10e624e37f9ceea28e97a57ff5d31f7d"></a>

### [`00495bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md) → [`00495f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495f14.md) FUN_00495f14

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004952bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952bc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004955dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955dc.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c70) · [`00495c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c84) · [`00495c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495bf4.md#insn-00495c8c)
- 新版 [`00495f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495f14.md#insn-00495f90) · [`00495fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495f14.md#insn-00495fa4) · [`00495fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495f14.md#insn-00495fac)

~~~diff
- 00495c70 ["INT_ADD", "register:40f0:8", ["const:495c70:8", "const:4:8"]]
- 00495c70 ["CALL", null, ["callee:00c54d90:8"]]
+ 00495f90 ["INT_ADD", "register:40f0:8", ["const:495f90:8", "const:4:8"]]
+ 00495f90 ["CALL", null, ["callee:00c54d90:8"]]
- 00495c70 bytes 4cf81e94
+ 00495f90 bytes 80fb1e94
- 00495c84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00495c84 ["INT_ADD", "register:40f0:8", ["const:495c84:8", "const:4:8"]]
- 00495c84 ["CALLIND", null, ["register:0:8"]]
+ 00495fa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00495fa4 ["INT_ADD", "register:40f0:8", ["const:495fa4:8", "const:4:8"]]
+ 00495fa4 ["CALLIND", null, ["register:0:8"]]
- 00495c84 bytes 00013fd6
+ 00495fa4 bytes 00013fd6
- 00495c8c ["INT_ADD", "register:40f0:8", ["const:495c8c:8", "const:4:8"]]
- 00495c8c ["CALL", null, ["callee:00c58f20:8"]]
+ 00495fac ["INT_ADD", "register:40f0:8", ["const:495fac:8", "const:4:8"]]
+ 00495fac ["CALL", null, ["callee:00c58f20:8"]]
- 00495c8c bytes b1081f94
+ 00495fac bytes dd0b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e351e552b8db501e66ec43223ee8545"></a>

### [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) → [`004960a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md) FUN_004960a4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00496244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md) [`004963cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md) [`00496558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00495734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00496564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496564.md) [`004966ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004966ec.md) [`00496878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496878.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e1c) · [`00495e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e60) · [`00495e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md#insn-00495e70)
- 新版 [`0049613c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md#insn-0049613c) · [`00496180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md#insn-00496180) · [`00496190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md#insn-00496190)

~~~diff
- 00495e1c ["INT_ADD", "register:40f0:8", ["const:495e1c:8", "const:4:8"]]
- 00495e1c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049613c ["INT_ADD", "register:40f0:8", ["const:49613c:8", "const:4:8"]]
+ 0049613c ["CALL", null, ["callee:00c58fe0:8"]]
- 00495e1c bytes 7d081f94
+ 0049613c bytes a90b1f94
- 00495e60 ["INT_ADD", "register:40f0:8", ["const:495e60:8", "const:4:8"]]
- 00495e60 ["CALL", null, ["callee:00c58f30:8"]]
+ 00496180 ["INT_ADD", "register:40f0:8", ["const:496180:8", "const:4:8"]]
+ 00496180 ["CALL", null, ["callee:00c58f30:8"]]
- 00495e60 bytes 40081f94
+ 00496180 bytes 6c0b1f94
- 00495e70 ["INT_ADD", "register:40f0:8", ["const:495e70:8", "const:4:8"]]
- 00495e70 ["CALL", null, ["callee:00496564:8"]]
+ 00496190 ["INT_ADD", "register:40f0:8", ["const:496190:8", "const:4:8"]]
+ 00496190 ["CALL", null, ["callee:00496564:8"]]
- 00495e70 bytes f5000094
+ 00496190 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-819305186a5341050a0eed00753c4421"></a>

### [`00496244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md) → [`00496564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496564.md) FUN_00496564

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`004960a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004962ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-004962ac) · [`004962e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-004962e4) · [`00496394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496244.md#insn-00496394)
- 新版 [`004965cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496564.md#insn-004965cc) · [`00496604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496564.md#insn-00496604) · [`004966b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496564.md#insn-004966b4)

~~~diff
- 004962ac ["INT_ADD", "register:40f0:8", ["const:4962ac:8", "const:4:8"]]
- 004962ac ["CALL", null, ["callee:00c58fe0:8"]]
+ 004965cc ["INT_ADD", "register:40f0:8", ["const:4965cc:8", "const:4:8"]]
+ 004965cc ["CALL", null, ["callee:00c58fe0:8"]]
- 004962ac bytes 59071f94
+ 004965cc bytes 850a1f94
- 004962e4 ["INT_ADD", "register:40f0:8", ["const:4962e4:8", "const:4:8"]]
- 004962e4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00496604 ["INT_ADD", "register:40f0:8", ["const:496604:8", "const:4:8"]]
+ 00496604 ["CALL", null, ["callee:00c58f30:8"]]
- 004962e4 bytes 1f071f94
+ 00496604 bytes 4b0a1f94
- 00496394 ["INT_ADD", "register:40f0:8", ["const:496394:8", "const:4:8"]]
- 00496394 ["CALL", null, ["callee:00c58f50:8"]]
+ 004966b4 ["INT_ADD", "register:40f0:8", ["const:4966b4:8", "const:4:8"]]
+ 004966b4 ["CALL", null, ["callee:00c58f50:8"]]
- 00496394 bytes fb061f94
+ 004966b4 bytes 270a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91628550512227edbd3376dcb62a5a6d"></a>

### [`004963cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md) → [`004966ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004966ec.md) FUN_004966ec

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`004960a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049643c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-0049643c) · [`00496474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-00496474) · [`00496524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004963cc.md#insn-00496524)
- 新版 [`0049675c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004966ec.md#insn-0049675c) · [`00496794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004966ec.md#insn-00496794) · [`00496844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004966ec.md#insn-00496844)

~~~diff
- 0049643c ["INT_ADD", "register:40f0:8", ["const:49643c:8", "const:4:8"]]
- 0049643c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049675c ["INT_ADD", "register:40f0:8", ["const:49675c:8", "const:4:8"]]
+ 0049675c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049643c bytes f5061f94
+ 0049675c bytes 210a1f94
- 00496474 ["INT_ADD", "register:40f0:8", ["const:496474:8", "const:4:8"]]
- 00496474 ["CALL", null, ["callee:00c58f30:8"]]
+ 00496794 ["INT_ADD", "register:40f0:8", ["const:496794:8", "const:4:8"]]
+ 00496794 ["CALL", null, ["callee:00c58f30:8"]]
- 00496474 bytes bb061f94
+ 00496794 bytes e7091f94
- 00496524 ["INT_ADD", "register:40f0:8", ["const:496524:8", "const:4:8"]]
- 00496524 ["CALL", null, ["callee:00c58f50:8"]]
+ 00496844 ["INT_ADD", "register:40f0:8", ["const:496844:8", "const:4:8"]]
+ 00496844 ["CALL", null, ["callee:00c58f50:8"]]
- 00496524 bytes 97061f94
+ 00496844 bytes c3091f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb3a794504462f8480839600dc5f643"></a>

### [`00496558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md) → [`00496878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496878.md) FUN_00496878

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`004960a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004965c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-004965c8) · [`00496600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-00496600) · [`004966b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496558.md#insn-004966b0)
- 新版 [`004968e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496878.md#insn-004968e8) · [`00496920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496878.md#insn-00496920) · [`004969d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496878.md#insn-004969d0)

~~~diff
- 004965c8 ["INT_ADD", "register:40f0:8", ["const:4965c8:8", "const:4:8"]]
- 004965c8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004968e8 ["INT_ADD", "register:40f0:8", ["const:4968e8:8", "const:4:8"]]
+ 004968e8 ["CALL", null, ["callee:00c58fe0:8"]]
- 004965c8 bytes 92061f94
+ 004968e8 bytes be091f94
- 00496600 ["INT_ADD", "register:40f0:8", ["const:496600:8", "const:4:8"]]
- 00496600 ["CALL", null, ["callee:00c58f30:8"]]
+ 00496920 ["INT_ADD", "register:40f0:8", ["const:496920:8", "const:4:8"]]
+ 00496920 ["CALL", null, ["callee:00c58f30:8"]]
- 00496600 bytes 58061f94
+ 00496920 bytes 84091f94
- 004966b0 ["INT_ADD", "register:40f0:8", ["const:4966b0:8", "const:4:8"]]
- 004966b0 ["CALL", null, ["callee:00c58f50:8"]]
+ 004969d0 ["INT_ADD", "register:40f0:8", ["const:4969d0:8", "const:4:8"]]
+ 004969d0 ["CALL", null, ["callee:00c58f50:8"]]
- 004966b0 bytes 34061f94
+ 004969d0 bytes 60091f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab3185af82e088e46392982ce32bb75e"></a>

### [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) → [`004971d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004971d4.md) FUN_004971d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md) [`0049763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497858.md) [`0049795c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049795c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md#insn-00496ec8)
- 新版 [`004971e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004971d4.md#insn-004971e8)

~~~diff
- 00496ec8 ["INT_ADD", "register:40f0:8", ["const:496ec8:8", "const:4:8"]]
- 00496ec8 ["CALL", null, ["callee:00497858:8"]]
+ 004971e8 ["INT_ADD", "register:40f0:8", ["const:4971e8:8", "const:4:8"]]
+ 004971e8 ["CALL", null, ["callee:00497858:8"]]
- 00496ec8 bytes 9c010094
+ 004971e8 bytes 9c010094
~~~


<a id="compare-080eda41e75b30068cd9beaa6c1ce772"></a>

### [`00496ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496ef8.md) → [`00497218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497218.md) FUN_00497218

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496ef8.md#insn-00496f0c)
- 新版 [`0049722c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497218.md#insn-0049722c)

~~~diff
- 00496f0c ["INT_ADD", "register:40f0:8", ["const:496f0c:8", "const:4:8"]]
- 00496f0c ["CALL", null, ["callee:004413ec:8"]]
+ 0049722c ["INT_ADD", "register:40f0:8", ["const:49722c:8", "const:4:8"]]
+ 0049722c ["CALL", null, ["callee:004413ec:8"]]
- 00496f0c bytes 70a8fe97
+ 0049722c bytes 70a8fe97
~~~


<a id="compare-ce64774713e2351667c7799648f48c7d"></a>

### [`00496f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f44.md) → [`00497264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497264.md) FUN_00497264

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f44.md#insn-00496f58)
- 新版 [`00497278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497264.md#insn-00497278)

~~~diff
- 00496f58 ["INT_ADD", "register:40f0:8", ["const:496f58:8", "const:4:8"]]
- 00496f58 ["CALL", null, ["callee:004413ec:8"]]
+ 00497278 ["INT_ADD", "register:40f0:8", ["const:497278:8", "const:4:8"]]
+ 00497278 ["CALL", null, ["callee:004413ec:8"]]
- 00496f58 bytes 5da8fe97
+ 00497278 bytes 5da8fe97
~~~


<a id="compare-e9f96068ebbb71c27d8936e247a36288"></a>

### [`00496f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f90.md) → [`004972b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004972b0.md) FUN_004972b0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496f90.md#insn-00496fa4)
- 新版 [`004972c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004972b0.md#insn-004972c4)

~~~diff
- 00496fa4 ["INT_ADD", "register:40f0:8", ["const:496fa4:8", "const:4:8"]]
- 00496fa4 ["CALL", null, ["callee:004413ec:8"]]
+ 004972c4 ["INT_ADD", "register:40f0:8", ["const:4972c4:8", "const:4:8"]]
+ 004972c4 ["CALL", null, ["callee:004413ec:8"]]
- 00496fa4 bytes 4aa8fe97
+ 004972c4 bytes 4aa8fe97
~~~


<a id="compare-43f97426fe7fbf84d834c0dc2d7dd0d2"></a>

### [`00496fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md) → [`004972fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004972fc.md) FUN_004972fc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md#insn-00496ff0) · [`0049700c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496fdc.md#insn-0049700c)
- 新版 [`00497310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004972fc.md#insn-00497310) · [`0049732c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004972fc.md#insn-0049732c)

~~~diff
- 00496ff0 ["INT_ADD", "register:40f0:8", ["const:496ff0:8", "const:4:8"]]
- 00496ff0 ["CALL", null, ["callee:004413ec:8"]]
+ 00497310 ["INT_ADD", "register:40f0:8", ["const:497310:8", "const:4:8"]]
+ 00497310 ["CALL", null, ["callee:004413ec:8"]]
- 00496ff0 bytes 37a8fe97
+ 00497310 bytes 37a8fe97
- 0049700c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049700c ["INT_ADD", "register:40f0:8", ["const:49700c:8", "const:4:8"]]
- 0049700c ["CALLIND", null, ["register:0:8"]]
+ 0049732c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049732c ["INT_ADD", "register:40f0:8", ["const:49732c:8", "const:4:8"]]
+ 0049732c ["CALLIND", null, ["register:0:8"]]
- 0049700c bytes 00013fd6
+ 0049732c bytes 00013fd6
~~~


<a id="compare-fb9e2f48745d399d7b63f6bd31398b4a"></a>

### [`00497024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497024.md) → [`00497344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497344.md) FUN_00497344

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049703c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497024.md#insn-0049703c)
- 新版 [`0049735c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497344.md#insn-0049735c)

~~~diff
- 0049703c ["INT_ADD", "register:40f0:8", ["const:49703c:8", "const:4:8"]]
- 0049703c ["CALL", null, ["callee:004413ec:8"]]
+ 0049735c ["INT_ADD", "register:40f0:8", ["const:49735c:8", "const:4:8"]]
+ 0049735c ["CALL", null, ["callee:004413ec:8"]]
- 0049703c bytes 24a8fe97
+ 0049735c bytes 24a8fe97
~~~


<a id="compare-807da625324dacecd0dc21eee46d2ac0"></a>

### [`00497538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md) → [`00497858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497858.md) FUN_00497858

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`004971d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004971d4.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004975a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md#insn-004975a4) · [`00497600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497538.md#insn-00497600)
- 新版 [`004978c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497858.md#insn-004978c4) · [`00497920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497858.md#insn-00497920)

~~~diff
- 004975a4 ["INT_ADD", "register:40f0:8", ["const:4975a4:8", "const:4:8"]]
- 004975a4 ["CALL", null, ["callee:00c590f0:8"]]
+ 004978c4 ["INT_ADD", "register:40f0:8", ["const:4978c4:8", "const:4:8"]]
+ 004978c4 ["CALL", null, ["callee:00c590f0:8"]]
- 004975a4 bytes df021f94
+ 004978c4 bytes 0b061f94
- 00497600 ["INT_ADD", "register:40f0:8", ["const:497600:8", "const:4:8"]]
- 00497600 ["CALL", null, ["callee:00c590f0:8"]]
+ 00497920 ["INT_ADD", "register:40f0:8", ["const:497920:8", "const:4:8"]]
+ 00497920 ["CALL", null, ["callee:00c590f0:8"]]
- 00497600 bytes c8021f94
+ 00497920 bytes f4051f94
~~~


<a id="compare-27a23feb61b81ae31fdba7caab0c5c05"></a>

### [`0049763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md) → [`0049795c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049795c.md) FUN_0049795c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00496eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496eb4.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004971d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/004971d4.md) · 呼出先 2件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004976a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976a0) · [`004976b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976b8) · [`004976c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049763c.md#insn-004976c8)
- 新版 [`004979c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049795c.md#insn-004979c0) · [`004979d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049795c.md#insn-004979d8) · [`004979e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049795c.md#insn-004979e8)

~~~diff
- 004976a0 ["INT_ADD", "register:40f0:8", ["const:4976a0:8", "const:4:8"]]
- 004976a0 ["CALL", null, ["callee:00494970:8"]]
+ 004979c0 ["INT_ADD", "register:40f0:8", ["const:4979c0:8", "const:4:8"]]
+ 004979c0 ["CALL", null, ["callee:00494970:8"]]
- 004976a0 bytes ecf3ff97
+ 004979c0 bytes ecf3ff97
- 004976b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004976b8 ["INT_ADD", "register:40f0:8", ["const:4976b8:8", "const:4:8"]]
- 004976b8 ["CALLIND", null, ["register:0:8"]]
+ 004979d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004979d8 ["INT_ADD", "register:40f0:8", ["const:4979d8:8", "const:4:8"]]
+ 004979d8 ["CALLIND", null, ["register:0:8"]]
- 004976b8 bytes 00013fd6
+ 004979d8 bytes 00013fd6
- 004976c8 ["INT_ADD", "register:40f0:8", ["const:4976c8:8", "const:4:8"]]
- 004976c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 004979e8 ["INT_ADD", "register:40f0:8", ["const:4979e8:8", "const:4:8"]]
+ 004979e8 ["CALL", null, ["callee:00c58f50:8"]]
- 004976c8 bytes 2e021f94
+ 004979e8 bytes 5a051f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d97c7bf8aa3f0c21aaadb800ab1c3d"></a>

### [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) → [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) FUN_00497b94

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 135件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00578950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md) [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) [`0057f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 135件 [`00497a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md) [`00578c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578c70.md) [`0057e83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md) [`0057eb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md) [`0057f98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f98c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004978e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md#insn-004978e8) · [`0049790c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md#insn-0049790c)
- 新版 [`00497c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md#insn-00497c08) · [`00497c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md#insn-00497c2c)

~~~diff
- 004978e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004978e8 ["INT_ADD", "register:40f0:8", ["const:4978e8:8", "const:4:8"]]
- 004978e8 ["CALLIND", null, ["register:0:8"]]
+ 00497c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497c08 ["INT_ADD", "register:40f0:8", ["const:497c08:8", "const:4:8"]]
+ 00497c08 ["CALLIND", null, ["register:0:8"]]
- 004978e8 bytes 00013fd6
+ 00497c08 bytes 00013fd6
- 0049790c ["INT_ADD", "register:40f0:8", ["const:49790c:8", "const:4:8"]]
- 0049790c ["CALL", null, ["callee:00c58f80:8"]]
+ 00497c2c ["INT_ADD", "register:40f0:8", ["const:497c2c:8", "const:4:8"]]
+ 00497c2c ["CALL", null, ["callee:00c58f80:8"]]
- 0049790c bytes a9011f94
+ 00497c2c bytes d5041f94
~~~


<a id="compare-b39d86f73ad42bd2167b00421bf5d65d"></a>

### [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) → [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) FUN_00497da8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 46件 [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) [`00572a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 46件 [`00497c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md) [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md) [`00571ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571ccc.md) [`00572d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572d44.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md#insn-00497afc) · [`00497b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md#insn-00497b20)
- 新版 [`00497e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md#insn-00497e1c) · [`00497e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md#insn-00497e40)

~~~diff
- 00497afc ["COPY", "register:0:8", ["register:4040:8"]]
- 00497afc ["INT_ADD", "register:40f0:8", ["const:497afc:8", "const:4:8"]]
- 00497afc ["CALLIND", null, ["register:0:8"]]
+ 00497e1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497e1c ["INT_ADD", "register:40f0:8", ["const:497e1c:8", "const:4:8"]]
+ 00497e1c ["CALLIND", null, ["register:0:8"]]
- 00497afc bytes 00013fd6
+ 00497e1c bytes 00013fd6
- 00497b20 ["INT_ADD", "register:40f0:8", ["const:497b20:8", "const:4:8"]]
- 00497b20 ["CALL", null, ["callee:00c58f80:8"]]
+ 00497e40 ["INT_ADD", "register:40f0:8", ["const:497e40:8", "const:4:8"]]
+ 00497e40 ["CALL", null, ["callee:00c58f80:8"]]
- 00497b20 bytes 24011f94
+ 00497e40 bytes 50041f94
~~~


<a id="compare-93a8ff3a1defaae0feb7cdd241433b04"></a>

### [`00497c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md) → [`00497f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f3c.md) FUN_00497f3c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md#insn-00497c38) · [`00497c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c1c.md#insn-00497c58)
- 新版 [`00497f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f3c.md#insn-00497f58) · [`00497f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f3c.md#insn-00497f78)

~~~diff
- 00497c38 ["INT_ADD", "register:40f0:8", ["const:497c38:8", "const:4:8"]]
- 00497c38 ["CALL", null, ["callee:00c54d90:8"]]
+ 00497f58 ["INT_ADD", "register:40f0:8", ["const:497f58:8", "const:4:8"]]
+ 00497f58 ["CALL", null, ["callee:00c54d90:8"]]
- 00497c38 bytes 5af01e94
+ 00497f58 bytes 8ef31e94
- 00497c58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497c58 ["INT_ADD", "register:40f0:8", ["const:497c58:8", "const:4:8"]]
- 00497c58 ["CALLIND", null, ["register:0:8"]]
+ 00497f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497f78 ["INT_ADD", "register:40f0:8", ["const:497f78:8", "const:4:8"]]
+ 00497f78 ["CALLIND", null, ["register:0:8"]]
- 00497c58 bytes 00013fd6
+ 00497f78 bytes 00013fd6
~~~


<a id="compare-6f54dbf5224243017ba4ee89cc301f29"></a>

### [`00497c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md) → [`00497f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f8c.md) FUN_00497f8c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md#insn-00497c88) · [`00497ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497c6c.md#insn-00497ca8)
- 新版 [`00497fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f8c.md#insn-00497fa8) · [`00497fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497f8c.md#insn-00497fc8)

~~~diff
- 00497c88 ["INT_ADD", "register:40f0:8", ["const:497c88:8", "const:4:8"]]
- 00497c88 ["CALL", null, ["callee:00c54d90:8"]]
+ 00497fa8 ["INT_ADD", "register:40f0:8", ["const:497fa8:8", "const:4:8"]]
+ 00497fa8 ["CALL", null, ["callee:00c54d90:8"]]
- 00497c88 bytes 46f01e94
+ 00497fa8 bytes 7af31e94
- 00497ca8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00497ca8 ["INT_ADD", "register:40f0:8", ["const:497ca8:8", "const:4:8"]]
- 00497ca8 ["CALLIND", null, ["register:0:8"]]
+ 00497fc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00497fc8 ["INT_ADD", "register:40f0:8", ["const:497fc8:8", "const:4:8"]]
+ 00497fc8 ["CALLIND", null, ["register:0:8"]]
- 00497ca8 bytes 00013fd6
+ 00497fc8 bytes 00013fd6
~~~


<a id="compare-72ecca76fd2c7cf76605b7885c833e7c"></a>

### [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) → [`00498434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md) FUN_00498434

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00497cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md) [`00497e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md) [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) · 呼出先 4件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 3件 [`00497fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497fdc.md) [`00498154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md) [`004986a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md) · 呼出先 4件 [`00499afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-00498130) · [`00498168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-00498168) · [`004981b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md#insn-004981b4)
- 新版 [`00498450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md#insn-00498450) · [`00498488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md#insn-00498488) · [`004984d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md#insn-004984d4)

~~~diff
- 00498130 ["INT_ADD", "register:40f0:8", ["const:498130:8", "const:4:8"]]
- 00498130 ["CALL", null, ["callee:00c59180:8"]]
+ 00498450 ["INT_ADD", "register:40f0:8", ["const:498450:8", "const:4:8"]]
+ 00498450 ["CALL", null, ["callee:00c59180:8"]]
- 00498130 bytes 20001f94
+ 00498450 bytes 4c031f94
- 00498168 ["INT_ADD", "register:40f0:8", ["const:498168:8", "const:4:8"]]
- 00498168 ["CALL", null, ["callee:00499afc:8"]]
+ 00498488 ["INT_ADD", "register:40f0:8", ["const:498488:8", "const:4:8"]]
+ 00498488 ["CALL", null, ["callee:00499afc:8"]]
- 00498168 bytes 9d050094
+ 00498488 bytes 9d050094
- 004981b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004981b4 ["INT_ADD", "register:40f0:8", ["const:4981b4:8", "const:4:8"]]
- 004981b4 ["CALLIND", null, ["register:0:8"]]
+ 004984d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004984d4 ["INT_ADD", "register:40f0:8", ["const:4984d4:8", "const:4:8"]]
+ 004984d4 ["CALLIND", null, ["register:0:8"]]
- 004981b4 bytes 00013fd6
+ 004984d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333caefb0e2e13eef6384b729b72d56f"></a>

### [`00498620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md) → [`00498940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md) FUN_00498940

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) · 呼出先 4件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`004986a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md) · 呼出先 4件 [`0049a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049863c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-0049863c) · [`00498674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-00498674) · [`004986c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md#insn-004986c4)
- 新版 [`0049895c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md#insn-0049895c) · [`00498994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md#insn-00498994) · [`004989e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md#insn-004989e4)

~~~diff
- 0049863c ["INT_ADD", "register:40f0:8", ["const:49863c:8", "const:4:8"]]
- 0049863c ["CALL", null, ["callee:00c59180:8"]]
+ 0049895c ["INT_ADD", "register:40f0:8", ["const:49895c:8", "const:4:8"]]
+ 0049895c ["CALL", null, ["callee:00c59180:8"]]
- 0049863c bytes ddfe1e94
+ 0049895c bytes 09021f94
- 00498674 ["INT_ADD", "register:40f0:8", ["const:498674:8", "const:4:8"]]
- 00498674 ["CALL", null, ["callee:0049a604:8"]]
+ 00498994 ["INT_ADD", "register:40f0:8", ["const:498994:8", "const:4:8"]]
+ 00498994 ["CALL", null, ["callee:0049a604:8"]]
- 00498674 bytes 1c070094
+ 00498994 bytes 1c070094
- 004986c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004986c4 ["INT_ADD", "register:40f0:8", ["const:4986c4:8", "const:4:8"]]
- 004986c4 ["CALLIND", null, ["register:0:8"]]
+ 004989e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004989e4 ["INT_ADD", "register:40f0:8", ["const:4989e4:8", "const:4:8"]]
+ 004989e4 ["CALLIND", null, ["register:0:8"]]
- 004986c4 bytes 00013fd6
+ 004989e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f56eb9cb34ebba17b8a706f323ece245"></a>

### [`00498844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md) → [`00498b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498b64.md) FUN_00498b64

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 22件 [`0067fdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067f/0067fdec.md) [`00680e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00680/00680e48.md) [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) [`006b545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b5/006b545c.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 2件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)
- 新版 呼出元 22件 [`0068019c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00680/0068019c.md) [`006811f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00681/006811f8.md) [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) [`006b580c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b5/006b580c.md) [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 2件 [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-00498870) · [`0049887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-0049887c) · [`00498894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md#insn-00498894)
- 新版 [`00498b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498b64.md#insn-00498b90) · [`00498b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498b64.md#insn-00498b9c) · [`00498bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498b64.md#insn-00498bb4)

~~~diff
- 00498870 ["INT_ADD", "register:40f0:8", ["const:498870:8", "const:4:8"]]
- 00498870 ["CALL", null, ["callee:00c59180:8"]]
+ 00498b90 ["INT_ADD", "register:40f0:8", ["const:498b90:8", "const:4:8"]]
+ 00498b90 ["CALL", null, ["callee:00c59180:8"]]
- 00498870 bytes 50fe1e94
+ 00498b90 bytes 7c011f94
- 0049887c ["INT_ADD", "register:40f0:8", ["const:49887c:8", "const:4:8"]]
- 0049887c ["CALL", null, ["callee:00c59190:8"]]
+ 00498b9c ["INT_ADD", "register:40f0:8", ["const:498b9c:8", "const:4:8"]]
+ 00498b9c ["CALL", null, ["callee:00c59190:8"]]
- 0049887c bytes 51fe1e94
+ 00498b9c bytes 7d011f94
- 00498894 ["INT_ADD", "register:40f0:8", ["const:498894:8", "const:4:8"]]
- 00498894 ["CALL", null, ["callee:00c59180:8"]]
+ 00498bb4 ["INT_ADD", "register:40f0:8", ["const:498bb4:8", "const:4:8"]]
+ 00498bb4 ["CALL", null, ["callee:00c59180:8"]]
- 00498894 bytes 47fe1e94
+ 00498bb4 bytes 73011f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e0d43eb97d3ff074fdd449305f0087"></a>

### [`004988bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md) → [`00498bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498bdc.md) FUN_00498bdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086b3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b3ac.md) [`0086b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b5c4.md) · 呼出先 2件 [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)
- 新版 呼出元 2件 [`0086c358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c358.md) [`0086c570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c570.md) · 呼出先 2件 [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md) [`00c59190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59190.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004988dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988dc) · [`004988e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988e8) · [`004988f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md#insn-004988f8)
- 新版 [`00498bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498bdc.md#insn-00498bfc) · [`00498c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498bdc.md#insn-00498c08) · [`00498c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498bdc.md#insn-00498c18)

~~~diff
- 004988dc ["INT_ADD", "register:40f0:8", ["const:4988dc:8", "const:4:8"]]
- 004988dc ["CALL", null, ["callee:00c59180:8"]]
+ 00498bfc ["INT_ADD", "register:40f0:8", ["const:498bfc:8", "const:4:8"]]
+ 00498bfc ["CALL", null, ["callee:00c59180:8"]]
- 004988dc bytes 35fe1e94
+ 00498bfc bytes 61011f94
- 004988e8 ["INT_ADD", "register:40f0:8", ["const:4988e8:8", "const:4:8"]]
- 004988e8 ["CALL", null, ["callee:00c59190:8"]]
+ 00498c08 ["INT_ADD", "register:40f0:8", ["const:498c08:8", "const:4:8"]]
+ 00498c08 ["CALL", null, ["callee:00c59190:8"]]
- 004988e8 bytes 36fe1e94
+ 00498c08 bytes 62011f94
- 004988f8 ["INT_ADD", "register:40f0:8", ["const:4988f8:8", "const:4:8"]]
- 004988f8 ["CALL", null, ["callee:00c59180:8"]]
+ 00498c18 ["INT_ADD", "register:40f0:8", ["const:498c18:8", "const:4:8"]]
+ 00498c18 ["CALL", null, ["callee:00c59180:8"]]
- 004988f8 bytes 2efe1e94
+ 00498c18 bytes 5a011f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec220a0a5a447f0f5e963777a7af4efb"></a>

### [`0049895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md) → [`00498c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c7c.md) FUN_00498c7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498cb0.md) [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md#insn-00498970) · [`00498978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md#insn-00498978)
- 新版 [`00498c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c7c.md#insn-00498c90) · [`00498c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c7c.md#insn-00498c98)

~~~diff
- 00498970 ["INT_ADD", "register:40f0:8", ["const:498970:8", "const:4:8"]]
- 00498970 ["CALL", null, ["callee:00c59170:8"]]
+ 00498c90 ["INT_ADD", "register:40f0:8", ["const:498c90:8", "const:4:8"]]
+ 00498c90 ["CALL", null, ["callee:00c59170:8"]]
- 00498970 bytes 0cfe1e94
+ 00498c90 bytes 38011f94
- 00498978 ["INT_ADD", "register:40f0:8", ["const:498978:8", "const:4:8"]]
- 00498978 ["CALL", null, ["callee:00c58f00:8"]]
+ 00498c98 ["INT_ADD", "register:40f0:8", ["const:498c98:8", "const:4:8"]]
+ 00498c98 ["CALL", null, ["callee:00c58f00:8"]]
- 00498978 bytes 6efd1e94
+ 00498c98 bytes 9a001f94
~~~


<a id="compare-d3545aa982aeb62c61e445f54425c7ed"></a>

### [`00498990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md) → [`00498cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498cb0.md) FUN_00498cb0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049895c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00498c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c7c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498a30) · [`00498a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498a7c) · [`00498ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498990.md#insn-00498ac8)
- 新版 [`00498d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498cb0.md#insn-00498d50) · [`00498d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498cb0.md#insn-00498d9c) · [`00498de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498cb0.md#insn-00498de8)

~~~diff
- 00498a30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498a30 ["INT_ADD", "register:40f0:8", ["const:498a30:8", "const:4:8"]]
- 00498a30 ["CALLIND", null, ["register:0:8"]]
+ 00498d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498d50 ["INT_ADD", "register:40f0:8", ["const:498d50:8", "const:4:8"]]
+ 00498d50 ["CALLIND", null, ["register:0:8"]]
- 00498a30 bytes 00013fd6
+ 00498d50 bytes 00013fd6
- 00498a7c ["INT_ADD", "register:40f0:8", ["const:498a7c:8", "const:4:8"]]
- 00498a7c ["CALL", null, ["callee:00c58f50:8"]]
+ 00498d9c ["INT_ADD", "register:40f0:8", ["const:498d9c:8", "const:4:8"]]
+ 00498d9c ["CALL", null, ["callee:00c58f50:8"]]
- 00498a7c bytes 41fd1e94
+ 00498d9c bytes 6d001f94
- 00498ac8 ["INT_ADD", "register:40f0:8", ["const:498ac8:8", "const:4:8"]]
- 00498ac8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00498de8 ["INT_ADD", "register:40f0:8", ["const:498de8:8", "const:4:8"]]
+ 00498de8 ["CALL", null, ["callee:00c58f50:8"]]
- 00498ac8 bytes 2efd1e94
+ 00498de8 bytes 5a001f94
~~~


<a id="compare-d61033c33a495c6417e77deeac93b9dd"></a>

### [`00498b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md) → [`00498e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e8c.md) FUN_00498e8c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00498ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00498ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498ec0.md) [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md#insn-00498b80) · [`00498b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md#insn-00498b88)
- 新版 [`00498ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e8c.md#insn-00498ea0) · [`00498ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e8c.md#insn-00498ea8)

~~~diff
- 00498b80 ["INT_ADD", "register:40f0:8", ["const:498b80:8", "const:4:8"]]
- 00498b80 ["CALL", null, ["callee:00c59170:8"]]
+ 00498ea0 ["INT_ADD", "register:40f0:8", ["const:498ea0:8", "const:4:8"]]
+ 00498ea0 ["CALL", null, ["callee:00c59170:8"]]
- 00498b80 bytes 88fd1e94
+ 00498ea0 bytes b4001f94
- 00498b88 ["INT_ADD", "register:40f0:8", ["const:498b88:8", "const:4:8"]]
- 00498b88 ["CALL", null, ["callee:00c58f00:8"]]
+ 00498ea8 ["INT_ADD", "register:40f0:8", ["const:498ea8:8", "const:4:8"]]
+ 00498ea8 ["CALL", null, ["callee:00c58f00:8"]]
- 00498b88 bytes eafc1e94
+ 00498ea8 bytes 16001f94
~~~


<a id="compare-dfe7f1a6e6afb7c76e22ae6de195e9e9"></a>

### [`00498ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md) → [`00498ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498ec0.md) FUN_00498ec0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b6c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00498e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e8c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00498c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498c40) · [`00498c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498c8c) · [`00498cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498ba0.md#insn-00498cd8)
- 新版 [`00498f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498ec0.md#insn-00498f60) · [`00498fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498ec0.md#insn-00498fac) · [`00498ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498ec0.md#insn-00498ff8)

~~~diff
- 00498c40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498c40 ["INT_ADD", "register:40f0:8", ["const:498c40:8", "const:4:8"]]
- 00498c40 ["CALLIND", null, ["register:0:8"]]
+ 00498f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498f60 ["INT_ADD", "register:40f0:8", ["const:498f60:8", "const:4:8"]]
+ 00498f60 ["CALLIND", null, ["register:0:8"]]
- 00498c40 bytes 00013fd6
+ 00498f60 bytes 00013fd6
- 00498c8c ["INT_ADD", "register:40f0:8", ["const:498c8c:8", "const:4:8"]]
- 00498c8c ["CALL", null, ["callee:00c58f50:8"]]
+ 00498fac ["INT_ADD", "register:40f0:8", ["const:498fac:8", "const:4:8"]]
+ 00498fac ["CALL", null, ["callee:00c58f50:8"]]
- 00498c8c bytes bdfc1e94
+ 00498fac bytes e9ff1e94
- 00498cd8 ["INT_ADD", "register:40f0:8", ["const:498cd8:8", "const:4:8"]]
- 00498cd8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00498ff8 ["INT_ADD", "register:40f0:8", ["const:498ff8:8", "const:4:8"]]
+ 00498ff8 ["CALL", null, ["callee:00c58f50:8"]]
- 00498cd8 bytes aafc1e94
+ 00498ff8 bytes d6ff1e94
~~~


<a id="compare-86a31285576a4c2fe454ff90882250b4"></a>

### [`00499254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md) → [`00499574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499574.md) FUN_00499574

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004992a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992a4) · [`004992b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992b8) · [`004992c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499254.md#insn-004992c0)
- 新版 [`004995c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499574.md#insn-004995c4) · [`004995d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499574.md#insn-004995d8) · [`004995e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499574.md#insn-004995e0)

~~~diff
- 004992a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004992a4 ["INT_ADD", "register:40f0:8", ["const:4992a4:8", "const:4:8"]]
- 004992a4 ["CALLIND", null, ["register:0:8"]]
+ 004995c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004995c4 ["INT_ADD", "register:40f0:8", ["const:4995c4:8", "const:4:8"]]
+ 004995c4 ["CALLIND", null, ["register:0:8"]]
- 004992a4 bytes 00013fd6
+ 004995c4 bytes 00013fd6
- 004992b8 ["INT_ADD", "register:40f0:8", ["const:4992b8:8", "const:4:8"]]
- 004992b8 ["CALL", null, ["callee:00c591f0:8"]]
+ 004995d8 ["INT_ADD", "register:40f0:8", ["const:4995d8:8", "const:4:8"]]
+ 004995d8 ["CALL", null, ["callee:00c591f0:8"]]
- 004992b8 bytes dafb1e94
+ 004995d8 bytes 06ff1e94
- 004992c0 ["INT_ADD", "register:40f0:8", ["const:4992c0:8", "const:4:8"]]
- 004992c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 004995e0 ["INT_ADD", "register:40f0:8", ["const:4995e0:8", "const:4:8"]]
+ 004995e0 ["CALL", null, ["callee:00c58f50:8"]]
- 004992c0 bytes 30fb1e94
+ 004995e0 bytes 5cfe1e94
~~~


<a id="compare-c6557b6a786f916f291673aeda841e25"></a>

### [`004992d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004992d4.md) → [`004995f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004995f4.md) FUN_004995f4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c591f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004992f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004992d4.md#insn-004992f0)
- 新版 [`00499610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004995f4.md#insn-00499610)

~~~diff
- 004992f0 ["INT_ADD", "register:40f0:8", ["const:4992f0:8", "const:4:8"]]
- 004992f0 ["CALL", null, ["callee:00c591f0:8"]]
+ 00499610 ["INT_ADD", "register:40f0:8", ["const:499610:8", "const:4:8"]]
+ 00499610 ["CALL", null, ["callee:00c591f0:8"]]
- 004992f0 bytes ccfb1e94
+ 00499610 bytes f8fe1e94
~~~


<a id="compare-53d24961fdde86f755547d9e209e35d8"></a>

### [`00499310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md) → [`00499630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md) FUN_00499630

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) · 呼出先 4件 [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`0049905c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md) · 呼出先 4件 [`004997d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-00499384) · [`004993ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-004993ac) · [`004993bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md#insn-004993bc)
- 新版 [`004996a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md#insn-004996a4) · [`004996cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md#insn-004996cc) · [`004996dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md#insn-004996dc)

~~~diff
- 00499384 ["COPY", "register:0:8", ["register:4048:8"]]
- 00499384 ["INT_ADD", "register:40f0:8", ["const:499384:8", "const:4:8"]]
- 00499384 ["CALLIND", null, ["register:0:8"]]
+ 004996a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004996a4 ["INT_ADD", "register:40f0:8", ["const:4996a4:8", "const:4:8"]]
+ 004996a4 ["CALLIND", null, ["register:0:8"]]
- 00499384 bytes 20013fd6
+ 004996a4 bytes 20013fd6
- 004993ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004993ac ["INT_ADD", "register:40f0:8", ["const:4993ac:8", "const:4:8"]]
- 004993ac ["CALLIND", null, ["register:0:8"]]
+ 004996cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004996cc ["INT_ADD", "register:40f0:8", ["const:4996cc:8", "const:4:8"]]
+ 004996cc ["CALLIND", null, ["register:0:8"]]
- 004993ac bytes 00013fd6
+ 004996cc bytes 00013fd6
- 004993bc ["INT_ADD", "register:40f0:8", ["const:4993bc:8", "const:4:8"]]
- 004993bc ["CALL", null, ["callee:004997d0:8"]]
+ 004996dc ["INT_ADD", "register:40f0:8", ["const:4996dc:8", "const:4:8"]]
+ 004996dc ["CALL", null, ["callee:004997d0:8"]]
- 004993bc bytes 3d000094
+ 004996dc bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d0c4a912b8931bd1f8a9dead92fbf9"></a>

### [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) → [`004997d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md) FUN_004997d0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) [`00499310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md) [`0049a13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0049905c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md) [`00499630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md) [`0049a45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a45c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049951c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049951c) · [`0049952c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049952c) · [`0049954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md#insn-0049954c)
- 新版 [`0049983c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md#insn-0049983c) · [`0049984c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md#insn-0049984c) · [`0049986c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md#insn-0049986c)

~~~diff
- 0049951c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049951c ["INT_ADD", "register:40f0:8", ["const:49951c:8", "const:4:8"]]
- 0049951c ["CALLIND", null, ["register:0:8"]]
+ 0049983c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049983c ["INT_ADD", "register:40f0:8", ["const:49983c:8", "const:4:8"]]
+ 0049983c ["CALLIND", null, ["register:0:8"]]
- 0049951c bytes 00013fd6
+ 0049983c bytes 00013fd6
- 0049952c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049952c ["INT_ADD", "register:40f0:8", ["const:49952c:8", "const:4:8"]]
- 0049952c ["CALLIND", null, ["register:0:8"]]
+ 0049984c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049984c ["INT_ADD", "register:40f0:8", ["const:49984c:8", "const:4:8"]]
+ 0049984c ["CALLIND", null, ["register:0:8"]]
- 0049952c bytes 00013fd6
+ 0049984c bytes 00013fd6
- 0049954c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049954c ["INT_ADD", "register:40f0:8", ["const:49954c:8", "const:4:8"]]
- 0049954c ["CALLIND", null, ["register:0:8"]]
+ 0049986c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049986c ["INT_ADD", "register:40f0:8", ["const:49986c:8", "const:4:8"]]
+ 0049986c ["CALLIND", null, ["register:0:8"]]
- 0049954c bytes 00013fd6
+ 0049986c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bd0467b832ba8a2d9411266feed83b5"></a>

### [`00499684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md) → [`004999a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004999a4.md) FUN_004999a4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004996c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-004996c8) · [`004996fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-004996fc) · [`00499700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499684.md#insn-00499700)
- 新版 [`004999e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004999a4.md#insn-004999e8) · [`00499a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004999a4.md#insn-00499a1c) · [`00499a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004999a4.md#insn-00499a20)

~~~diff
- 004996c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004996c8 ["INT_ADD", "register:40f0:8", ["const:4996c8:8", "const:4:8"]]
- 004996c8 ["CALLIND", null, ["register:0:8"]]
+ 004999e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004999e8 ["INT_ADD", "register:40f0:8", ["const:4999e8:8", "const:4:8"]]
+ 004999e8 ["CALLIND", null, ["register:0:8"]]
- 004996c8 bytes 00013fd6
+ 004999e8 bytes 00013fd6
- 004996fc ["INT_ADD", "register:40f0:8", ["const:4996fc:8", "const:4:8"]]
- 004996fc ["CALL", null, ["callee:0045a0d4:8"]]
+ 00499a1c ["INT_ADD", "register:40f0:8", ["const:499a1c:8", "const:4:8"]]
+ 00499a1c ["CALL", null, ["callee:0045a0d4:8"]]
- 004996fc bytes ae01ff97
+ 00499a1c bytes ae01ff97
- 00499700 ["INT_ADD", "register:40f0:8", ["const:499700:8", "const:4:8"]]
- 00499700 ["CALL", null, ["callee:00c58f80:8"]]
+ 00499a20 ["INT_ADD", "register:40f0:8", ["const:499a20:8", "const:4:8"]]
+ 00499a20 ["CALL", null, ["callee:00c58f80:8"]]
- 00499700 bytes 2cfa1e94
+ 00499a20 bytes 58fd1e94
~~~


<a id="compare-e4a2f84fe89e2b81ac540a346f157b56"></a>

### [`00499788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499788.md) → [`00499aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499aa8.md) FUN_00499aa8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004997b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499788.md#insn-004997b0)
- 新版 [`00499ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499aa8.md#insn-00499ad0)

~~~diff
- 004997b0 ["INT_ADD", "register:40f0:8", ["const:4997b0:8", "const:4:8"]]
- 004997b0 ["CALL", null, ["callee:0045a0d4:8"]]
+ 00499ad0 ["INT_ADD", "register:40f0:8", ["const:499ad0:8", "const:4:8"]]
+ 00499ad0 ["CALL", null, ["callee:0045a0d4:8"]]
- 004997b0 bytes 8101ff97
+ 00499ad0 bytes 8101ff97
~~~


<a id="compare-08593efde4a7f6fd12aa85439e28a0c5"></a>

### [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) → [`00499afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md) FUN_00499afc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00499c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md) [`00499e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md) [`00499fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00498434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00499fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499fbc.md) [`0049a144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a144.md) [`0049a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a2d0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-00499874) · [`004998b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-004998b8) · [`004998c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md#insn-004998c8)
- 新版 [`00499b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md#insn-00499b94) · [`00499bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md#insn-00499bd8) · [`00499be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md#insn-00499be8)

~~~diff
- 00499874 ["INT_ADD", "register:40f0:8", ["const:499874:8", "const:4:8"]]
- 00499874 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00499b94 ["INT_ADD", "register:40f0:8", ["const:499b94:8", "const:4:8"]]
+ 00499b94 ["CALL", null, ["callee:00c58fe0:8"]]
- 00499874 bytes e7f91e94
+ 00499b94 bytes 13fd1e94
- 004998b8 ["INT_ADD", "register:40f0:8", ["const:4998b8:8", "const:4:8"]]
- 004998b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00499bd8 ["INT_ADD", "register:40f0:8", ["const:499bd8:8", "const:4:8"]]
+ 00499bd8 ["CALL", null, ["callee:00c58f30:8"]]
- 004998b8 bytes aaf91e94
+ 00499bd8 bytes d6fc1e94
- 004998c8 ["INT_ADD", "register:40f0:8", ["const:4998c8:8", "const:4:8"]]
- 004998c8 ["CALL", null, ["callee:00499fbc:8"]]
+ 00499be8 ["INT_ADD", "register:40f0:8", ["const:499be8:8", "const:4:8"]]
+ 00499be8 ["CALL", null, ["callee:00499fbc:8"]]
- 004998c8 bytes f5000094
+ 00499be8 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf60c283a60982483d31042d47b213ee"></a>

### [`00499c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md) → [`00499fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499fbc.md) FUN_00499fbc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00499afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499d04) · [`00499d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499d3c) · [`00499dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499c9c.md#insn-00499dec)
- 新版 [`0049a024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499fbc.md#insn-0049a024) · [`0049a05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499fbc.md#insn-0049a05c) · [`0049a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499fbc.md#insn-0049a10c)

~~~diff
- 00499d04 ["INT_ADD", "register:40f0:8", ["const:499d04:8", "const:4:8"]]
- 00499d04 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049a024 ["INT_ADD", "register:40f0:8", ["const:49a024:8", "const:4:8"]]
+ 0049a024 ["CALL", null, ["callee:00c58fe0:8"]]
- 00499d04 bytes c3f81e94
+ 0049a024 bytes effb1e94
- 00499d3c ["INT_ADD", "register:40f0:8", ["const:499d3c:8", "const:4:8"]]
- 00499d3c ["CALL", null, ["callee:00c58f30:8"]]
+ 0049a05c ["INT_ADD", "register:40f0:8", ["const:49a05c:8", "const:4:8"]]
+ 0049a05c ["CALL", null, ["callee:00c58f30:8"]]
- 00499d3c bytes 89f81e94
+ 0049a05c bytes b5fb1e94
- 00499dec ["INT_ADD", "register:40f0:8", ["const:499dec:8", "const:4:8"]]
- 00499dec ["CALL", null, ["callee:00c58f50:8"]]
+ 0049a10c ["INT_ADD", "register:40f0:8", ["const:49a10c:8", "const:4:8"]]
+ 0049a10c ["CALL", null, ["callee:00c58f50:8"]]
- 00499dec bytes 65f81e94
+ 0049a10c bytes 91fb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee90a4cd4ed1681a1beb7d75a505b5c"></a>

### [`00499e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md) → [`0049a144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a144.md) FUN_0049a144

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00499afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499e94) · [`00499ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499ecc) · [`00499f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499e24.md#insn-00499f7c)
- 新版 [`0049a1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a144.md#insn-0049a1b4) · [`0049a1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a144.md#insn-0049a1ec) · [`0049a29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a144.md#insn-0049a29c)

~~~diff
- 00499e94 ["INT_ADD", "register:40f0:8", ["const:499e94:8", "const:4:8"]]
- 00499e94 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049a1b4 ["INT_ADD", "register:40f0:8", ["const:49a1b4:8", "const:4:8"]]
+ 0049a1b4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00499e94 bytes 5ff81e94
+ 0049a1b4 bytes 8bfb1e94
- 00499ecc ["INT_ADD", "register:40f0:8", ["const:499ecc:8", "const:4:8"]]
- 00499ecc ["CALL", null, ["callee:00c58f30:8"]]
+ 0049a1ec ["INT_ADD", "register:40f0:8", ["const:49a1ec:8", "const:4:8"]]
+ 0049a1ec ["CALL", null, ["callee:00c58f30:8"]]
- 00499ecc bytes 25f81e94
+ 0049a1ec bytes 51fb1e94
- 00499f7c ["INT_ADD", "register:40f0:8", ["const:499f7c:8", "const:4:8"]]
- 00499f7c ["CALL", null, ["callee:00c58f50:8"]]
+ 0049a29c ["INT_ADD", "register:40f0:8", ["const:49a29c:8", "const:4:8"]]
+ 0049a29c ["CALL", null, ["callee:00c58f50:8"]]
- 00499f7c bytes 01f81e94
+ 0049a29c bytes 2dfb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3212f04084c57a85f6b78f9576eb417"></a>

### [`00499fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md) → [`0049a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a2d0.md) FUN_0049a2d0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004997dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004997dc.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00499afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499afc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a020) · [`0049a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a058) · [`0049a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499fb0.md#insn-0049a108)
- 新版 [`0049a340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a2d0.md#insn-0049a340) · [`0049a378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a2d0.md#insn-0049a378) · [`0049a428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a2d0.md#insn-0049a428)

~~~diff
- 0049a020 ["INT_ADD", "register:40f0:8", ["const:49a020:8", "const:4:8"]]
- 0049a020 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049a340 ["INT_ADD", "register:40f0:8", ["const:49a340:8", "const:4:8"]]
+ 0049a340 ["CALL", null, ["callee:00c58fe0:8"]]
- 0049a020 bytes fcf71e94
+ 0049a340 bytes 28fb1e94
- 0049a058 ["INT_ADD", "register:40f0:8", ["const:49a058:8", "const:4:8"]]
- 0049a058 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049a378 ["INT_ADD", "register:40f0:8", ["const:49a378:8", "const:4:8"]]
+ 0049a378 ["CALL", null, ["callee:00c58f30:8"]]
- 0049a058 bytes c2f71e94
+ 0049a378 bytes eefa1e94
- 0049a108 ["INT_ADD", "register:40f0:8", ["const:49a108:8", "const:4:8"]]
- 0049a108 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049a428 ["INT_ADD", "register:40f0:8", ["const:49a428:8", "const:4:8"]]
+ 0049a428 ["CALL", null, ["callee:00c58f50:8"]]
- 0049a108 bytes 9ef71e94
+ 0049a428 bytes cafa1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19f0fc331741f225e33f7e160456eb0c"></a>

### [`0049a13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md) → [`0049a45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a45c.md) FUN_0049a45c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) · 呼出先 4件 [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58450.md)
- 新版 呼出元 1件 [`00498530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498530.md) · 呼出先 4件 [`004997d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59420.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1b8) · [`0049a1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1e0) · [`0049a1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a13c.md#insn-0049a1f0)
- 新版 [`0049a4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a45c.md#insn-0049a4d8) · [`0049a500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a45c.md#insn-0049a500) · [`0049a510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a45c.md#insn-0049a510)

~~~diff
- 0049a1b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049a1b8 ["INT_ADD", "register:40f0:8", ["const:49a1b8:8", "const:4:8"]]
- 0049a1b8 ["CALLIND", null, ["register:0:8"]]
+ 0049a4d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0049a4d8 ["INT_ADD", "register:40f0:8", ["const:49a4d8:8", "const:4:8"]]
+ 0049a4d8 ["CALLIND", null, ["register:0:8"]]
- 0049a1b8 bytes 20013fd6
+ 0049a4d8 bytes 20013fd6
- 0049a1e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049a1e0 ["INT_ADD", "register:40f0:8", ["const:49a1e0:8", "const:4:8"]]
- 0049a1e0 ["CALLIND", null, ["register:0:8"]]
+ 0049a500 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049a500 ["INT_ADD", "register:40f0:8", ["const:49a500:8", "const:4:8"]]
+ 0049a500 ["CALLIND", null, ["register:0:8"]]
- 0049a1e0 bytes 00013fd6
+ 0049a500 bytes 00013fd6
- 0049a1f0 ["INT_ADD", "register:40f0:8", ["const:49a1f0:8", "const:4:8"]]
- 0049a1f0 ["CALL", null, ["callee:004997d0:8"]]
+ 0049a510 ["INT_ADD", "register:40f0:8", ["const:49a510:8", "const:4:8"]]
+ 0049a510 ["CALL", null, ["callee:004997d0:8"]]
- 0049a1f0 bytes b0fcff97
+ 0049a510 bytes b0fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f01d728cf2a8c6816b3f8c96319c54a"></a>

### [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) → [`0049a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md) FUN_0049a604

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00498620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0049a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md) [`0049a92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md) [`0049aab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00498940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0049aac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049aac4.md) [`0049ac4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049ac4c.md) [`0049add8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049add8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a37c) · [`0049a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a3c0) · [`0049a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md#insn-0049a3d0)
- 新版 [`0049a69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md#insn-0049a69c) · [`0049a6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md#insn-0049a6e0) · [`0049a6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md#insn-0049a6f0)

~~~diff
- 0049a37c ["INT_ADD", "register:40f0:8", ["const:49a37c:8", "const:4:8"]]
- 0049a37c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049a69c ["INT_ADD", "register:40f0:8", ["const:49a69c:8", "const:4:8"]]
+ 0049a69c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049a37c bytes 25f71e94
+ 0049a69c bytes 51fa1e94
- 0049a3c0 ["INT_ADD", "register:40f0:8", ["const:49a3c0:8", "const:4:8"]]
- 0049a3c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049a6e0 ["INT_ADD", "register:40f0:8", ["const:49a6e0:8", "const:4:8"]]
+ 0049a6e0 ["CALL", null, ["callee:00c58f30:8"]]
- 0049a3c0 bytes e8f61e94
+ 0049a6e0 bytes 14fa1e94
- 0049a3d0 ["INT_ADD", "register:40f0:8", ["const:49a3d0:8", "const:4:8"]]
- 0049a3d0 ["CALL", null, ["callee:0049aac4:8"]]
+ 0049a6f0 ["INT_ADD", "register:40f0:8", ["const:49a6f0:8", "const:4:8"]]
+ 0049a6f0 ["CALL", null, ["callee:0049aac4:8"]]
- 0049a3d0 bytes f5000094
+ 0049a6f0 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e168f94917ec4f0f256e2e291e787545"></a>

### [`0049a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md) → [`0049aac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049aac4.md) FUN_0049aac4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`0049a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a80c) · [`0049a844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a844) · [`0049a8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a7a4.md#insn-0049a8f4)
- 新版 [`0049ab2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049aac4.md#insn-0049ab2c) · [`0049ab64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049aac4.md#insn-0049ab64) · [`0049ac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049aac4.md#insn-0049ac14)

~~~diff
- 0049a80c ["INT_ADD", "register:40f0:8", ["const:49a80c:8", "const:4:8"]]
- 0049a80c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049ab2c ["INT_ADD", "register:40f0:8", ["const:49ab2c:8", "const:4:8"]]
+ 0049ab2c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049a80c bytes 01f61e94
+ 0049ab2c bytes 2df91e94
- 0049a844 ["INT_ADD", "register:40f0:8", ["const:49a844:8", "const:4:8"]]
- 0049a844 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049ab64 ["INT_ADD", "register:40f0:8", ["const:49ab64:8", "const:4:8"]]
+ 0049ab64 ["CALL", null, ["callee:00c58f30:8"]]
- 0049a844 bytes c7f51e94
+ 0049ab64 bytes f3f81e94
- 0049a8f4 ["INT_ADD", "register:40f0:8", ["const:49a8f4:8", "const:4:8"]]
- 0049a8f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049ac14 ["INT_ADD", "register:40f0:8", ["const:49ac14:8", "const:4:8"]]
+ 0049ac14 ["CALL", null, ["callee:00c58f50:8"]]
- 0049a8f4 bytes a3f51e94
+ 0049ac14 bytes cff81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa35dc6fc075fc2b08560662eb40cde"></a>

### [`0049a92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md) → [`0049ac4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049ac4c.md) FUN_0049ac4c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`0049a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049a99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049a99c) · [`0049a9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049a9d4) · [`0049aa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a92c.md#insn-0049aa84)
- 新版 [`0049acbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049ac4c.md#insn-0049acbc) · [`0049acf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049ac4c.md#insn-0049acf4) · [`0049ada4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049ac4c.md#insn-0049ada4)

~~~diff
- 0049a99c ["INT_ADD", "register:40f0:8", ["const:49a99c:8", "const:4:8"]]
- 0049a99c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049acbc ["INT_ADD", "register:40f0:8", ["const:49acbc:8", "const:4:8"]]
+ 0049acbc ["CALL", null, ["callee:00c58fe0:8"]]
- 0049a99c bytes 9df51e94
+ 0049acbc bytes c9f81e94
- 0049a9d4 ["INT_ADD", "register:40f0:8", ["const:49a9d4:8", "const:4:8"]]
- 0049a9d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049acf4 ["INT_ADD", "register:40f0:8", ["const:49acf4:8", "const:4:8"]]
+ 0049acf4 ["CALL", null, ["callee:00c58f30:8"]]
- 0049a9d4 bytes 63f51e94
+ 0049acf4 bytes 8ff81e94
- 0049aa84 ["INT_ADD", "register:40f0:8", ["const:49aa84:8", "const:4:8"]]
- 0049aa84 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049ada4 ["INT_ADD", "register:40f0:8", ["const:49ada4:8", "const:4:8"]]
+ 0049ada4 ["CALL", null, ["callee:00c58f50:8"]]
- 0049aa84 bytes 3ff51e94
+ 0049ada4 bytes 6bf81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c8087fcb005882b4aa378bdfbe929bc"></a>

### [`0049aab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md) → [`0049add8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049add8.md) FUN_0049add8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049a2e4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`0049a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049a604.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ab28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ab28) · [`0049ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ab60) · [`0049ac10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aab8.md#insn-0049ac10)
- 新版 [`0049ae48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049add8.md#insn-0049ae48) · [`0049ae80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049add8.md#insn-0049ae80) · [`0049af30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049add8.md#insn-0049af30)

~~~diff
- 0049ab28 ["INT_ADD", "register:40f0:8", ["const:49ab28:8", "const:4:8"]]
- 0049ab28 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049ae48 ["INT_ADD", "register:40f0:8", ["const:49ae48:8", "const:4:8"]]
+ 0049ae48 ["CALL", null, ["callee:00c58fe0:8"]]
- 0049ab28 bytes 3af51e94
+ 0049ae48 bytes 66f81e94
- 0049ab60 ["INT_ADD", "register:40f0:8", ["const:49ab60:8", "const:4:8"]]
- 0049ab60 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049ae80 ["INT_ADD", "register:40f0:8", ["const:49ae80:8", "const:4:8"]]
+ 0049ae80 ["CALL", null, ["callee:00c58f30:8"]]
- 0049ab60 bytes 00f51e94
+ 0049ae80 bytes 2cf81e94
- 0049ac10 ["INT_ADD", "register:40f0:8", ["const:49ac10:8", "const:4:8"]]
- 0049ac10 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049af30 ["INT_ADD", "register:40f0:8", ["const:49af30:8", "const:4:8"]]
+ 0049af30 ["CALL", null, ["callee:00c58f50:8"]]
- 0049ac10 bytes dcf41e94
+ 0049af30 bytes 08f81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1808e26699b610fab0700ccf4bd9fc7"></a>

### [`0049ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad34.md) → [`0049b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b054.md) FUN_0049b054

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00498a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md) · 呼出先 2件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad34.md#insn-0049ad50)
- 新版 [`0049b070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b054.md#insn-0049b070)

~~~diff
- 0049ad50 ["INT_ADD", "register:40f0:8", ["const:49ad50:8", "const:4:8"]]
- 0049ad50 ["CALL", null, ["callee:00c58f20:8"]]
+ 0049b070 ["INT_ADD", "register:40f0:8", ["const:49b070:8", "const:4:8"]]
+ 0049b070 ["CALL", null, ["callee:00c58f20:8"]]
- 0049ad50 bytes 80f41e94
+ 0049b070 bytes acf71e94
~~~


<a id="compare-33cd40469d2bed243d77d7c084e8c100"></a>

### [`0049ad64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md) → [`0049b084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b084.md) FUN_0049b084

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c585c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00489808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489808.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ad90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049ad90) · [`0049adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049adac) · [`0049adb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad64.md#insn-0049adb8)
- 新版 [`0049b0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b084.md#insn-0049b0b0) · [`0049b0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b084.md#insn-0049b0cc) · [`0049b0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b084.md#insn-0049b0d8)

~~~diff
- 0049ad90 ["INT_ADD", "register:40f0:8", ["const:49ad90:8", "const:4:8"]]
- 0049ad90 ["CALL", null, ["callee:00c59590:8"]]
+ 0049b0b0 ["INT_ADD", "register:40f0:8", ["const:49b0b0:8", "const:4:8"]]
+ 0049b0b0 ["CALL", null, ["callee:00c59590:8"]]
- 0049ad90 bytes 0cf61e94
+ 0049b0b0 bytes 38f91e94
- 0049adac ["INT_ADD", "register:40f0:8", ["const:49adac:8", "const:4:8"]]
- 0049adac ["CALL", null, ["callee:00489808:8"]]
+ 0049b0cc ["INT_ADD", "register:40f0:8", ["const:49b0cc:8", "const:4:8"]]
+ 0049b0cc ["CALL", null, ["callee:00489808:8"]]
- 0049adac bytes cfb9ff97
+ 0049b0cc bytes cfb9ff97
- 0049adb8 ["INT_ADD", "register:40f0:8", ["const:49adb8:8", "const:4:8"]]
- 0049adb8 ["CALL", null, ["callee:00c54d90:8"]]
+ 0049b0d8 ["INT_ADD", "register:40f0:8", ["const:49b0d8:8", "const:4:8"]]
+ 0049b0d8 ["CALL", null, ["callee:00c54d90:8"]]
- 0049adb8 bytes fae31e94
+ 0049b0d8 bytes 2ee71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65925a425655b1a6fd9d8b3348c957a5"></a>

### [`0049b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md) → [`0049b734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b734.md) FUN_0049b734

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md#insn-0049b450) · [`0049b46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md#insn-0049b46c)
- 新版 [`0049b770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b734.md#insn-0049b770) · [`0049b78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b734.md#insn-0049b78c)

~~~diff
- 0049b450 ["INT_ADD", "register:40f0:8", ["const:49b450:8", "const:4:8"]]
- 0049b450 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049b770 ["INT_ADD", "register:40f0:8", ["const:49b770:8", "const:4:8"]]
+ 0049b770 ["CALL", null, ["callee:00c58f30:8"]]
- 0049b450 bytes c4f21e94
+ 0049b770 bytes f0f51e94
- 0049b46c ["INT_ADD", "register:40f0:8", ["const:49b46c:8", "const:4:8"]]
- 0049b46c ["CALL", null, ["callee:00c59130:8"]]
+ 0049b78c ["INT_ADD", "register:40f0:8", ["const:49b78c:8", "const:4:8"]]
+ 0049b78c ["CALL", null, ["callee:00c59130:8"]]
- 0049b46c bytes 3df31e94
+ 0049b78c bytes 69f61e94
~~~


<a id="compare-1ee0e3c78228275509b60b5fc0d2433c"></a>

### [`0049b5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md) → [`0049b90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b90c.md) FUN_0049b90c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a99514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a99/00a99514.md) · 呼出先 4件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a9a508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a9a/00a9a508.md) · 呼出先 4件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) [`004a02b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a02b0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049b618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b618) · [`0049b638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b638) · [`0049b66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md#insn-0049b66c)
- 新版 [`0049b938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b90c.md#insn-0049b938) · [`0049b958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b90c.md#insn-0049b958) · [`0049b98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b90c.md#insn-0049b98c)

~~~diff
- 0049b618 ["INT_ADD", "register:40f0:8", ["const:49b618:8", "const:4:8"]]
- 0049b618 ["CALL", null, ["callee:004a02b0:8"]]
+ 0049b938 ["INT_ADD", "register:40f0:8", ["const:49b938:8", "const:4:8"]]
+ 0049b938 ["CALL", null, ["callee:004a02b0:8"]]
- 0049b618 bytes 5e120094
+ 0049b938 bytes 5e120094
- 0049b638 ["INT_ADD", "register:40f0:8", ["const:49b638:8", "const:4:8"]]
- 0049b638 ["CALL", null, ["callee:0049b9ec:8"]]
+ 0049b958 ["INT_ADD", "register:40f0:8", ["const:49b958:8", "const:4:8"]]
+ 0049b958 ["CALL", null, ["callee:0049b9ec:8"]]
- 0049b638 bytes 25000094
+ 0049b958 bytes 25000094
- 0049b66c ["INT_ADD", "register:40f0:8", ["const:49b66c:8", "const:4:8"]]
- 0049b66c ["CALL", null, ["callee:00c58f50:8"]]
+ 0049b98c ["INT_ADD", "register:40f0:8", ["const:49b98c:8", "const:4:8"]]
+ 0049b98c ["CALL", null, ["callee:00c58f50:8"]]
- 0049b66c bytes 45f21e94
+ 0049b98c bytes 71f51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4364f348a8586e78e358a6217ae08430"></a>

### [`0049bc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc28.md) → [`0049bf48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bf48.md) FUN_0049bf48

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049bc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc28.md#insn-0049bc6c)
- 新版 [`0049bf8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bf48.md#insn-0049bf8c)

~~~diff
- 0049bc6c ["INT_ADD", "register:40f0:8", ["const:49bc6c:8", "const:4:8"]]
- 0049bc6c ["CALL", null, ["callee:00c58f50:8"]]
+ 0049bf8c ["INT_ADD", "register:40f0:8", ["const:49bf8c:8", "const:4:8"]]
+ 0049bf8c ["CALL", null, ["callee:00c58f50:8"]]
- 0049bc6c bytes c5f01e94
+ 0049bf8c bytes f1f31e94
~~~


<a id="compare-bcc1876dac8c32a50cc087d1f87baf30"></a>

### [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) → [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) FUN_0049c384

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 8件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) [`0049d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 8件 [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) [`0049d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md) [`0049d758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md) [`0049d824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md) [`0049dc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049c0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c0b8) · [`0049c0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c0cc) · [`0049c158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md#insn-0049c158)
- 新版 [`0049c3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md#insn-0049c3d8) · [`0049c3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md#insn-0049c3ec) · [`0049c478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md#insn-0049c478)

~~~diff
- 0049c0b8 ["INT_ADD", "register:40f0:8", ["const:49c0b8:8", "const:4:8"]]
- 0049c0b8 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049c3d8 ["INT_ADD", "register:40f0:8", ["const:49c3d8:8", "const:4:8"]]
+ 0049c3d8 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049c0b8 bytes 48040094
+ 0049c3d8 bytes 48040094
- 0049c0cc ["INT_ADD", "register:40f0:8", ["const:49c0cc:8", "const:4:8"]]
- 0049c0cc ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049c3ec ["INT_ADD", "register:40f0:8", ["const:49c3ec:8", "const:4:8"]]
+ 0049c3ec ["CALL", null, ["callee:0049d4f8:8"]]
- 0049c0cc bytes 43040094
+ 0049c3ec bytes 43040094
- 0049c158 ["INT_ADD", "register:40f0:8", ["const:49c158:8", "const:4:8"]]
- 0049c158 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049c478 ["INT_ADD", "register:40f0:8", ["const:49c478:8", "const:4:8"]]
+ 0049c478 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049c158 bytes 20040094
+ 0049c478 bytes 20040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a975f7566d15b9d94b9cf643bfa2e05a"></a>

### [`0049d0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d0c8.md) → [`0049d3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d3e8.md) FUN_0049d3e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d0c8.md#insn-0049d108)
- 新版 [`0049d428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d3e8.md#insn-0049d428)

~~~diff
- 0049d108 ["INT_ADD", "register:40f0:8", ["const:49d108:8", "const:4:8"]]
- 0049d108 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049d428 ["INT_ADD", "register:40f0:8", ["const:49d428:8", "const:4:8"]]
+ 0049d428 ["CALL", null, ["callee:00c58f50:8"]]
- 0049d108 bytes 9eeb1e94
+ 0049d428 bytes caee1e94
~~~


<a id="compare-0fe702b22371fbc76f2e4bb0abefc153"></a>

### [`0049d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md) → [`0049d460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d460.md) FUN_0049d460

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a99514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a99/00a99514.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)
- 新版 呼出元 1件 [`00a9a508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a9a/00a9a508.md) · 呼出先 2件 [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md#insn-0049d1d0) · [`0049d1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md#insn-0049d1d4)
- 新版 [`0049d4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d460.md#insn-0049d4f0) · [`0049d4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d460.md#insn-0049d4f4)

~~~diff
- 0049d1d0 ["INT_ADD", "register:40f0:8", ["const:49d1d0:8", "const:4:8"]]
- 0049d1d0 ["CALL", null, ["callee:0049f764:8"]]
+ 0049d4f0 ["INT_ADD", "register:40f0:8", ["const:49d4f0:8", "const:4:8"]]
+ 0049d4f0 ["CALL", null, ["callee:0049f764:8"]]
- 0049d1d0 bytes 9d080094
+ 0049d4f0 bytes 9d080094
- 0049d1d4 ["INT_ADD", "register:40f0:8", ["const:49d1d4:8", "const:4:8"]]
- 0049d1d4 ["CALL", null, ["callee:0049f778:8"]]
+ 0049d4f4 ["INT_ADD", "register:40f0:8", ["const:49d4f4:8", "const:4:8"]]
+ 0049d4f4 ["CALL", null, ["callee:0049f778:8"]]
- 0049d1d4 bytes a1080094
+ 0049d4f4 bytes a1080094
~~~


<a id="compare-9ae1a739e77d7a7eebb492002688035f"></a>

### [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) → [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) FUN_0049d4f8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) [`0049d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)
- 新版 呼出元 4件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) [`0049d758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md) [`0049d824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md) [`0049dc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md) · 呼出先 2件 [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2a0) · [`0049d2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2a8) · [`0049d2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md#insn-0049d2ac)
- 新版 [`0049d5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md#insn-0049d5c0) · [`0049d5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md#insn-0049d5c8) · [`0049d5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md#insn-0049d5cc)

~~~diff
- 0049d2a0 ["INT_ADD", "register:40f0:8", ["const:49d2a0:8", "const:4:8"]]
- 0049d2a0 ["CALL", null, ["callee:0049f764:8"]]
+ 0049d5c0 ["INT_ADD", "register:40f0:8", ["const:49d5c0:8", "const:4:8"]]
+ 0049d5c0 ["CALL", null, ["callee:0049f764:8"]]
- 0049d2a0 bytes 69080094
+ 0049d5c0 bytes 69080094
- 0049d2a8 ["INT_ADD", "register:40f0:8", ["const:49d2a8:8", "const:4:8"]]
- 0049d2a8 ["CALL", null, ["callee:0049f778:8"]]
+ 0049d5c8 ["INT_ADD", "register:40f0:8", ["const:49d5c8:8", "const:4:8"]]
+ 0049d5c8 ["CALL", null, ["callee:0049f778:8"]]
- 0049d2a8 bytes 6c080094
+ 0049d5c8 bytes 6c080094
- 0049d2ac ["INT_ADD", "register:40f0:8", ["const:49d2ac:8", "const:4:8"]]
- 0049d2ac ["CALL", null, ["callee:0049f764:8"]]
+ 0049d5cc ["INT_ADD", "register:40f0:8", ["const:49d5cc:8", "const:4:8"]]
+ 0049d5cc ["CALL", null, ["callee:0049f764:8"]]
- 0049d2ac bytes 66080094
+ 0049d5cc bytes 66080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d2091ba021b4dbe7fef960cf2e4e772"></a>

### [`0049d438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md) → [`0049d758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md) FUN_0049d758

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) · 呼出先 1件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md)
- 新版 呼出元 1件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) · 呼出先 1件 [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d480) · [`0049d4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d4a0) · [`0049d4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d438.md#insn-0049d4b4)
- 新版 [`0049d7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md#insn-0049d7a0) · [`0049d7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md#insn-0049d7c0) · [`0049d7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d758.md#insn-0049d7d4)

~~~diff
- 0049d480 ["INT_ADD", "register:40f0:8", ["const:49d480:8", "const:4:8"]]
- 0049d480 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049d7a0 ["INT_ADD", "register:40f0:8", ["const:49d7a0:8", "const:4:8"]]
+ 0049d7a0 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049d480 bytes 56ffff97
+ 0049d7a0 bytes 56ffff97
- 0049d4a0 ["INT_ADD", "register:40f0:8", ["const:49d4a0:8", "const:4:8"]]
- 0049d4a0 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049d7c0 ["INT_ADD", "register:40f0:8", ["const:49d7c0:8", "const:4:8"]]
+ 0049d7c0 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049d4a0 bytes 4effff97
+ 0049d7c0 bytes 4effff97
- 0049d4b4 ["INT_ADD", "register:40f0:8", ["const:49d4b4:8", "const:4:8"]]
- 0049d4b4 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049d7d4 ["INT_ADD", "register:40f0:8", ["const:49d7d4:8", "const:4:8"]]
+ 0049d7d4 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049d4b4 bytes 49ffff97
+ 0049d7d4 bytes 49ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc684beeda6ef6a4183e6e2cbc310a3c"></a>

### [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) → [`0049dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md) FUN_0049dd80

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 8件 [`0049eaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) · 呼出先 8件 [`0049ee0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0049fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049daa8) · [`0049dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049dac4) · [`0049db1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md#insn-0049db1c)
- 新版 [`0049ddc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md#insn-0049ddc8) · [`0049dde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md#insn-0049dde4) · [`0049de3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md#insn-0049de3c)

~~~diff
- 0049daa8 ["INT_ADD", "register:40f0:8", ["const:49daa8:8", "const:4:8"]]
- 0049daa8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049ddc8 ["INT_ADD", "register:40f0:8", ["const:49ddc8:8", "const:4:8"]]
+ 0049ddc8 ["CALL", null, ["callee:00c58f30:8"]]
- 0049daa8 bytes 2ee91e94
+ 0049ddc8 bytes 5aec1e94
- 0049dac4 ["INT_ADD", "register:40f0:8", ["const:49dac4:8", "const:4:8"]]
- 0049dac4 ["CALL", null, ["callee:00c59130:8"]]
+ 0049dde4 ["INT_ADD", "register:40f0:8", ["const:49dde4:8", "const:4:8"]]
+ 0049dde4 ["CALL", null, ["callee:00c59130:8"]]
- 0049dac4 bytes a7e91e94
+ 0049dde4 bytes d3ec1e94
- 0049db1c ["INT_ADD", "register:40f0:8", ["const:49db1c:8", "const:4:8"]]
- 0049db1c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049de3c ["INT_ADD", "register:40f0:8", ["const:49de3c:8", "const:4:8"]]
+ 0049de3c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049db1c bytes 3de91e94
+ 0049de3c bytes 69ec1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7a766c1f55c5bac6e9053d4f3317fb0"></a>

### [`0049dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dc98.md) → [`0049dfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dfb8.md) FUN_0049dfb8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049dce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dc98.md#insn-0049dce4)
- 新版 [`0049e004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dfb8.md#insn-0049e004)

~~~diff
- 0049dce4 ["INT_ADD", "register:40f0:8", ["const:49dce4:8", "const:4:8"]]
- 0049dce4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049e004 ["INT_ADD", "register:40f0:8", ["const:49e004:8", "const:4:8"]]
+ 0049e004 ["CALL", null, ["callee:00c58f50:8"]]
- 0049dce4 bytes a7e81e94
+ 0049e004 bytes d3eb1e94
~~~


<a id="compare-49a372c793d7be0bed24369c2e46484f"></a>

### [`0049df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md) → [`0049e2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md) FUN_0049e2a0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md) · 呼出先 2件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md)
- 新版 呼出元 1件 [`0049d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md) · 呼出先 2件 [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e2a8) · [`0049e4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e4d4) · [`0049e4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md#insn-0049e4dc)
- 新版 [`0049e5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md#insn-0049e5c8) · [`0049e7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md#insn-0049e7f4) · [`0049e7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md#insn-0049e7fc)

~~~diff
- 0049e2a8 ["INT_ADD", "register:40f0:8", ["const:49e2a8:8", "const:4:8"]]
- 0049e2a8 ["CALL", null, ["callee:0049f778:8"]]
+ 0049e5c8 ["INT_ADD", "register:40f0:8", ["const:49e5c8:8", "const:4:8"]]
+ 0049e5c8 ["CALL", null, ["callee:0049f778:8"]]
- 0049e2a8 bytes 6c040094
+ 0049e5c8 bytes 6c040094
- 0049e4d4 ["INT_ADD", "register:40f0:8", ["const:49e4d4:8", "const:4:8"]]
- 0049e4d4 ["CALL", null, ["callee:0049f778:8"]]
+ 0049e7f4 ["INT_ADD", "register:40f0:8", ["const:49e7f4:8", "const:4:8"]]
+ 0049e7f4 ["CALL", null, ["callee:0049f778:8"]]
- 0049e4d4 bytes e1030094
+ 0049e7f4 bytes e1030094
- 0049e4dc ["INT_ADD", "register:40f0:8", ["const:49e4dc:8", "const:4:8"]]
- 0049e4dc ["CALL", null, ["callee:0049f764:8"]]
+ 0049e7fc ["INT_ADD", "register:40f0:8", ["const:49e7fc:8", "const:4:8"]]
+ 0049e7fc ["CALL", null, ["callee:0049f764:8"]]
- 0049e4dc bytes da030094
+ 0049e7fc bytes da030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df691c49031edb1324571253fe673042"></a>

### [`0049e504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md) → [`0049e824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e824.md) FUN_0049e824

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008c7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c7/008c7b94.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 4件 [`0049d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md) [`0073cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073c/0073cd40.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`008c8b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c8/008c8b40.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e5a8) · [`0049e61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e61c) · [`0049e658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md#insn-0049e658)
- 新版 [`0049e8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e824.md#insn-0049e8c8) · [`0049e93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e824.md#insn-0049e93c) · [`0049e978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e824.md#insn-0049e978)

~~~diff
- 0049e5a8 ["INT_ADD", "register:40f0:8", ["const:49e5a8:8", "const:4:8"]]
- 0049e5a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049e8c8 ["INT_ADD", "register:40f0:8", ["const:49e8c8:8", "const:4:8"]]
+ 0049e8c8 ["CALL", null, ["callee:00c58f30:8"]]
- 0049e5a8 bytes 6ee61e94
+ 0049e8c8 bytes 9ae91e94
- 0049e61c ["INT_ADD", "register:40f0:8", ["const:49e61c:8", "const:4:8"]]
- 0049e61c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049e93c ["INT_ADD", "register:40f0:8", ["const:49e93c:8", "const:4:8"]]
+ 0049e93c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049e61c bytes 7de61e94
+ 0049e93c bytes a9e91e94
- 0049e658 ["INT_ADD", "register:40f0:8", ["const:49e658:8", "const:4:8"]]
- 0049e658 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049e978 ["INT_ADD", "register:40f0:8", ["const:49e978:8", "const:4:8"]]
+ 0049e978 ["CALL", null, ["callee:00c58f30:8"]]
- 0049e658 bytes 42e61e94
+ 0049e978 bytes 6ee91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca001cc0028ac09160b3ad78c546015"></a>

### [`0049e714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md) → [`0049ea34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md) FUN_0049ea34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0049f934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0049d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md) [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0049fc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc54.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e7cc) · [`0049e80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e80c) · [`0049e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md#insn-0049e820)
- 新版 [`0049eaec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md#insn-0049eaec) · [`0049eb2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md#insn-0049eb2c) · [`0049eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md#insn-0049eb40)

~~~diff
- 0049e7cc ["INT_ADD", "register:40f0:8", ["const:49e7cc:8", "const:4:8"]]
- 0049e7cc ["CALL", null, ["callee:00c58f30:8"]]
+ 0049eaec ["INT_ADD", "register:40f0:8", ["const:49eaec:8", "const:4:8"]]
+ 0049eaec ["CALL", null, ["callee:00c58f30:8"]]
- 0049e7cc bytes e5e51e94
+ 0049eaec bytes 11e91e94
- 0049e80c ["INT_ADD", "register:40f0:8", ["const:49e80c:8", "const:4:8"]]
- 0049e80c ["CALL", null, ["callee:0049fc54:8"]]
+ 0049eb2c ["INT_ADD", "register:40f0:8", ["const:49eb2c:8", "const:4:8"]]
+ 0049eb2c ["CALL", null, ["callee:0049fc54:8"]]
- 0049e80c bytes 4a040094
+ 0049eb2c bytes 4a040094
- 0049e820 ["INT_ADD", "register:40f0:8", ["const:49e820:8", "const:4:8"]]
- 0049e820 ["CALL", null, ["callee:00c590a0:8"]]
+ 0049eb40 ["INT_ADD", "register:40f0:8", ["const:49eb40:8", "const:4:8"]]
+ 0049eb40 ["CALL", null, ["callee:00c590a0:8"]]
- 0049e820 bytes 2ce61e94
+ 0049eb40 bytes 58e91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12c4d3cfdbc8eff2974e4674e8d1b7d"></a>

### [`0049ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md) → [`0049ef00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ef00.md) FUN_0049ef00

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 2件 [`0047da18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047da18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ec1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md#insn-0049ec1c) · [`0049ece0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md#insn-0049ece0)
- 新版 [`0049ef3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ef00.md#insn-0049ef3c) · [`0049f000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ef00.md#insn-0049f000)

~~~diff
- 0049ec1c ["INT_ADD", "register:40f0:8", ["const:49ec1c:8", "const:4:8"]]
- 0049ec1c ["CALL", null, ["callee:00c58f30:8"]]
+ 0049ef3c ["INT_ADD", "register:40f0:8", ["const:49ef3c:8", "const:4:8"]]
+ 0049ef3c ["CALL", null, ["callee:00c58f30:8"]]
- 0049ec1c bytes d1e41e94
+ 0049ef3c bytes fde71e94
- 0049ece0 ["INT_ADD", "register:40f0:8", ["const:49ece0:8", "const:4:8"]]
- 0049ece0 ["CALL", null, ["callee:0047da18:8"]]
+ 0049f000 ["INT_ADD", "register:40f0:8", ["const:49f000:8", "const:4:8"]]
+ 0049f000 ["CALL", null, ["callee:0047da18:8"]]
- 0049ece0 bytes 867aff97
+ 0049f000 bytes 867aff97
~~~


<a id="compare-4dce3fefc5208d0efeb6fffb698d083e"></a>

### [`0049ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md) → [`0049f004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f004.md) FUN_0049f004

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 7件 [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`0049f1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f1bc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) · 呼出先 7件 [`0047d914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d914.md) [`0047da18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047da18.md) [`0049f4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f4dc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049ee4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049ee4c) · [`0049eea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049eea4) · [`0049eebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md#insn-0049eebc)
- 新版 [`0049f16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f004.md#insn-0049f16c) · [`0049f1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f004.md#insn-0049f1c4) · [`0049f1dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f004.md#insn-0049f1dc)

~~~diff
- 0049ee4c ["INT_ADD", "register:40f0:8", ["const:49ee4c:8", "const:4:8"]]
- 0049ee4c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049f16c ["INT_ADD", "register:40f0:8", ["const:49f16c:8", "const:4:8"]]
+ 0049f16c ["CALL", null, ["callee:00c58fe0:8"]]
- 0049ee4c bytes 71e41e94
+ 0049f16c bytes 9de71e94
- 0049eea4 ["INT_ADD", "register:40f0:8", ["const:49eea4:8", "const:4:8"]]
- 0049eea4 ["CALL", null, ["callee:0049f4dc:8"]]
+ 0049f1c4 ["INT_ADD", "register:40f0:8", ["const:49f1c4:8", "const:4:8"]]
+ 0049f1c4 ["CALL", null, ["callee:0049f4dc:8"]]
- 0049eea4 bytes c6000094
+ 0049f1c4 bytes c6000094
- 0049eebc ["INT_ADD", "register:40f0:8", ["const:49eebc:8", "const:4:8"]]
- 0049eebc ["CALL", null, ["callee:0047d914:8"]]
+ 0049f1dc ["INT_ADD", "register:40f0:8", ["const:49f1dc:8", "const:4:8"]]
+ 0049f1dc ["CALL", null, ["callee:0047d914:8"]]
- 0049eebc bytes ce79ff97
+ 0049f1dc bytes ce79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ecfb5f5c6ed0932a55a7120c567a6a"></a>

### [`0049f3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f3b0.md) → [`0049f6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f6d0.md) FUN_0049f6d0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f3b0.md#insn-0049f40c)
- 新版 [`0049f72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f6d0.md#insn-0049f72c)

~~~diff
- 0049f40c ["INT_ADD", "register:40f0:8", ["const:49f40c:8", "const:4:8"]]
- 0049f40c ["CALL", null, ["callee:00c58f50:8"]]
+ 0049f72c ["INT_ADD", "register:40f0:8", ["const:49f72c:8", "const:4:8"]]
+ 0049f72c ["CALL", null, ["callee:00c58f50:8"]]
- 0049f40c bytes dde21e94
+ 0049f72c bytes 09e61e94
~~~


<a id="compare-efbfa10aff5c88d8644660da284e6905"></a>

### [`0049f480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md) → [`0049f7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md) FUN_0049f7a0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) · 呼出先 5件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f500) · [`0049f534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f534) · [`0049f644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md#insn-0049f644)
- 新版 [`0049f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md#insn-0049f820) · [`0049f854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md#insn-0049f854) · [`0049f964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md#insn-0049f964)

~~~diff
- 0049f500 ["INT_ADD", "register:40f0:8", ["const:49f500:8", "const:4:8"]]
- 0049f500 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049f820 ["INT_ADD", "register:40f0:8", ["const:49f820:8", "const:4:8"]]
+ 0049f820 ["CALL", null, ["callee:00c58f30:8"]]
- 0049f500 bytes 98e21e94
+ 0049f820 bytes c4e51e94
- 0049f534 ["INT_ADD", "register:40f0:8", ["const:49f534:8", "const:4:8"]]
- 0049f534 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049f854 ["INT_ADD", "register:40f0:8", ["const:49f854:8", "const:4:8"]]
+ 0049f854 ["CALL", null, ["callee:00c58fe0:8"]]
- 0049f534 bytes b7e21e94
+ 0049f854 bytes e3e51e94
- 0049f644 ["INT_ADD", "register:40f0:8", ["const:49f644:8", "const:4:8"]]
- 0049f644 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049f964 ["INT_ADD", "register:40f0:8", ["const:49f964:8", "const:4:8"]]
+ 0049f964 ["CALL", null, ["callee:00c58fe0:8"]]
- 0049f644 bytes 73e21e94
+ 0049f964 bytes 9fe51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9fa46d77bf2ec60b8aeee36afaad7e"></a>

### [`0049f76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md) → [`0049fa8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md) FUN_0049fa8c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0049f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0049fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f7f8) · [`0049f8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f8b0) · [`0049f8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md#insn-0049f8cc)
- 新版 [`0049fb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md#insn-0049fb18) · [`0049fbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md#insn-0049fbd0) · [`0049fbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md#insn-0049fbec)

~~~diff
- 0049f7f8 ["INT_ADD", "register:40f0:8", ["const:49f7f8:8", "const:4:8"]]
- 0049f7f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049fb18 ["INT_ADD", "register:40f0:8", ["const:49fb18:8", "const:4:8"]]
+ 0049fb18 ["CALL", null, ["callee:00c58f30:8"]]
- 0049f7f8 bytes dae11e94
+ 0049fb18 bytes 06e51e94
- 0049f8b0 ["INT_ADD", "register:40f0:8", ["const:49f8b0:8", "const:4:8"]]
- 0049f8b0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049fbd0 ["INT_ADD", "register:40f0:8", ["const:49fbd0:8", "const:4:8"]]
+ 0049fbd0 ["CALL", null, ["callee:00c58f50:8"]]
- 0049f8b0 bytes b4e11e94
+ 0049fbd0 bytes e0e41e94
- 0049f8cc ["INT_ADD", "register:40f0:8", ["const:49f8cc:8", "const:4:8"]]
- 0049f8cc ["CALL", null, ["callee:00c58f50:8"]]
+ 0049fbec ["INT_ADD", "register:40f0:8", ["const:49fbec:8", "const:4:8"]]
+ 0049fbec ["CALL", null, ["callee:00c58f50:8"]]
- 0049f8cc bytes ade11e94
+ 0049fbec bytes d9e41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b57507b6b68bc72ccf137a280c935b62"></a>

### [`0049f934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md) → [`0049fc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc54.md) FUN_0049fc54

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049e714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`0049ea34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049f99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049f99c) · [`0049f9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049f9d4) · [`0049fa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f934.md#insn-0049fa84)
- 新版 [`0049fcbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc54.md#insn-0049fcbc) · [`0049fcf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc54.md#insn-0049fcf4) · [`0049fda4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc54.md#insn-0049fda4)

~~~diff
- 0049f99c ["INT_ADD", "register:40f0:8", ["const:49f99c:8", "const:4:8"]]
- 0049f99c ["CALL", null, ["callee:00c58fe0:8"]]
+ 0049fcbc ["INT_ADD", "register:40f0:8", ["const:49fcbc:8", "const:4:8"]]
+ 0049fcbc ["CALL", null, ["callee:00c58fe0:8"]]
- 0049f99c bytes 9de11e94
+ 0049fcbc bytes c9e41e94
- 0049f9d4 ["INT_ADD", "register:40f0:8", ["const:49f9d4:8", "const:4:8"]]
- 0049f9d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049fcf4 ["INT_ADD", "register:40f0:8", ["const:49fcf4:8", "const:4:8"]]
+ 0049fcf4 ["CALL", null, ["callee:00c58f30:8"]]
- 0049f9d4 bytes 63e11e94
+ 0049fcf4 bytes 8fe41e94
- 0049fa84 ["INT_ADD", "register:40f0:8", ["const:49fa84:8", "const:4:8"]]
- 0049fa84 ["CALL", null, ["callee:00c58f50:8"]]
+ 0049fda4 ["INT_ADD", "register:40f0:8", ["const:49fda4:8", "const:4:8"]]
+ 0049fda4 ["CALL", null, ["callee:00c58f50:8"]]
- 0049fa84 bytes 3fe11e94
+ 0049fda4 bytes 6be41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754c5d9121b1e400a1995ec682609043"></a>

### [`004a03a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md) → [`004a06c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a06c8.md) FUN_004a06c8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004a0528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0528.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004a02b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a02b0.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004a0848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a0848.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a0430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a0430) · [`004a04e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a04e4) · [`004a0500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md#insn-004a0500)
- 新版 [`004a0750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a06c8.md#insn-004a0750) · [`004a0804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a06c8.md#insn-004a0804) · [`004a0820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a06c8.md#insn-004a0820)

~~~diff
- 004a0430 ["INT_ADD", "register:40f0:8", ["const:4a0430:8", "const:4:8"]]
- 004a0430 ["CALL", null, ["callee:00c58f30:8"]]
+ 004a0750 ["INT_ADD", "register:40f0:8", ["const:4a0750:8", "const:4:8"]]
+ 004a0750 ["CALL", null, ["callee:00c58f30:8"]]
- 004a0430 bytes ccde1e94
+ 004a0750 bytes f8e11e94
- 004a04e4 ["INT_ADD", "register:40f0:8", ["const:4a04e4:8", "const:4:8"]]
- 004a04e4 ["CALL", null, ["callee:00c58f50:8"]]
+ 004a0804 ["INT_ADD", "register:40f0:8", ["const:4a0804:8", "const:4:8"]]
+ 004a0804 ["CALL", null, ["callee:00c58f50:8"]]
- 004a04e4 bytes a7de1e94
+ 004a0804 bytes d3e11e94
- 004a0500 ["INT_ADD", "register:40f0:8", ["const:4a0500:8", "const:4:8"]]
- 004a0500 ["CALL", null, ["callee:00c58f50:8"]]
+ 004a0820 ["INT_ADD", "register:40f0:8", ["const:4a0820:8", "const:4:8"]]
+ 004a0820 ["CALL", null, ["callee:00c58f50:8"]]
- 004a0500 bytes a0de1e94
+ 004a0820 bytes cce11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c2bcbb779bf726bdd3bde4d375a881"></a>

### [`004a1af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md) → [`004a1e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md) _ZN5Botan7AES_1285clearEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md) [`00540ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b18) · [`004a1b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b28) · [`004a1b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md#insn-004a1b40)
- 新版 [`004a1e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md#insn-004a1e38) · [`004a1e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md#insn-004a1e48) · [`004a1e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md#insn-004a1e60)

~~~diff
- 004a1b18 ["INT_ADD", "register:40f0:8", ["const:4a1b18:8", "const:4:8"]]
- 004a1b18 ["CALL", null, ["callee:00c59130:8"]]
+ 004a1e38 ["INT_ADD", "register:40f0:8", ["const:4a1e38:8", "const:4:8"]]
+ 004a1e38 ["CALL", null, ["callee:00c59130:8"]]
- 004a1b18 bytes 92d91e94
+ 004a1e38 bytes bedc1e94
- 004a1b28 ["INT_ADD", "register:40f0:8", ["const:4a1b28:8", "const:4:8"]]
- 004a1b28 ["CALL", null, ["callee:00540de8:8"]]
+ 004a1e48 ["INT_ADD", "register:40f0:8", ["const:4a1e48:8", "const:4:8"]]
+ 004a1e48 ["CALL", null, ["callee:00540de8:8"]]
- 004a1b28 bytes e87b0294
+ 004a1e48 bytes e87b0294
- 004a1b40 ["INT_ADD", "register:40f0:8", ["const:4a1b40:8", "const:4:8"]]
- 004a1b40 ["CALL", null, ["callee:00c59130:8"]]
+ 004a1e60 ["INT_ADD", "register:40f0:8", ["const:4a1e60:8", "const:4:8"]]
+ 004a1e60 ["CALL", null, ["callee:00c59130:8"]]
- 004a1b40 bytes 88d91e94
+ 004a1e60 bytes b4dc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecf37932de6dad57c8d25c1bc280db20"></a>

### [`004a1e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md) → [`004a2130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md) _ZN5Botan7AES_1925clearEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md) [`00540ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e34) · [`004a1e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e44) · [`004a1e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md#insn-004a1e5c)
- 新版 [`004a2154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md#insn-004a2154) · [`004a2164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md#insn-004a2164) · [`004a217c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md#insn-004a217c)

~~~diff
- 004a1e34 ["INT_ADD", "register:40f0:8", ["const:4a1e34:8", "const:4:8"]]
- 004a1e34 ["CALL", null, ["callee:00c59130:8"]]
+ 004a2154 ["INT_ADD", "register:40f0:8", ["const:4a2154:8", "const:4:8"]]
+ 004a2154 ["CALL", null, ["callee:00c59130:8"]]
- 004a1e34 bytes cbd81e94
+ 004a2154 bytes f7db1e94
- 004a1e44 ["INT_ADD", "register:40f0:8", ["const:4a1e44:8", "const:4:8"]]
- 004a1e44 ["CALL", null, ["callee:00540de8:8"]]
+ 004a2164 ["INT_ADD", "register:40f0:8", ["const:4a2164:8", "const:4:8"]]
+ 004a2164 ["CALL", null, ["callee:00540de8:8"]]
- 004a1e44 bytes 217b0294
+ 004a2164 bytes 217b0294
- 004a1e5c ["INT_ADD", "register:40f0:8", ["const:4a1e5c:8", "const:4:8"]]
- 004a1e5c ["CALL", null, ["callee:00c59130:8"]]
+ 004a217c ["INT_ADD", "register:40f0:8", ["const:4a217c:8", "const:4:8"]]
+ 004a217c ["CALL", null, ["callee:00c59130:8"]]
- 004a1e5c bytes c1d81e94
+ 004a217c bytes eddb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48440e756f0f14020cc12d7aa1f3801"></a>

### [`004a212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md) → [`004a244c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md) _ZN5Botan7AES_2565clearEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md) [`00540ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a2150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2150) · [`004a2160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2160) · [`004a2178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md#insn-004a2178)
- 新版 [`004a2470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md#insn-004a2470) · [`004a2480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md#insn-004a2480) · [`004a2498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md#insn-004a2498)

~~~diff
- 004a2150 ["INT_ADD", "register:40f0:8", ["const:4a2150:8", "const:4:8"]]
- 004a2150 ["CALL", null, ["callee:00c59130:8"]]
+ 004a2470 ["INT_ADD", "register:40f0:8", ["const:4a2470:8", "const:4:8"]]
+ 004a2470 ["CALL", null, ["callee:00c59130:8"]]
- 004a2150 bytes 04d81e94
+ 004a2470 bytes 30db1e94
- 004a2160 ["INT_ADD", "register:40f0:8", ["const:4a2160:8", "const:4:8"]]
- 004a2160 ["CALL", null, ["callee:00540de8:8"]]
+ 004a2480 ["INT_ADD", "register:40f0:8", ["const:4a2480:8", "const:4:8"]]
+ 004a2480 ["CALL", null, ["callee:00540de8:8"]]
- 004a2160 bytes 5a7a0294
+ 004a2480 bytes 5a7a0294
- 004a2178 ["INT_ADD", "register:40f0:8", ["const:4a2178:8", "const:4:8"]]
- 004a2178 ["CALL", null, ["callee:00c59130:8"]]
+ 004a2498 ["INT_ADD", "register:40f0:8", ["const:4a2498:8", "const:4:8"]]
+ 004a2498 ["CALL", null, ["callee:00c59130:8"]]
- 004a2178 bytes fad71e94
+ 004a2498 bytes 26db1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61136d45d2ec373984a6ae18e59842b8"></a>

### [`004a51d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a51d8.md) → [`004a54f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a54f8.md) _ZN5BotaneqERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c59740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59740.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a52a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a51d8.md#insn-004a52a8)
- 新版 [`004a55c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a54f8.md#insn-004a55c8)

~~~diff
- 004a52a8 ["INT_ADD", "register:40f0:8", ["const:4a52a8:8", "const:4:8"]]
- 004a52a8 ["CALL", null, ["callee:00c590f0:8"]]
+ 004a55c8 ["INT_ADD", "register:40f0:8", ["const:4a55c8:8", "const:4:8"]]
+ 004a55c8 ["CALL", null, ["callee:00c590f0:8"]]
- 004a52a8 bytes 9ecb1e94
+ 004a55c8 bytes cace1e94
~~~


<a id="compare-9063709e476d51af23259cb30594a83c"></a>

### [`004a532c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a532c.md) → [`004a564c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a564c.md) _ZN5BotanneERKNS_19AlgorithmIdentifierES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58770.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a532c.md#insn-004a5334)
- 新版 [`004a5654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a564c.md#insn-004a5654)

~~~diff
- 004a5334 ["INT_ADD", "register:40f0:8", ["const:4a5334:8", "const:4:8"]]
- 004a5334 ["CALL", null, ["callee:00c59740:8"]]
+ 004a5654 ["INT_ADD", "register:40f0:8", ["const:4a5654:8", "const:4:8"]]
+ 004a5654 ["CALL", null, ["callee:00c59740:8"]]
- 004a5334 bytes 0fcd1e94
+ 004a5654 bytes 3bd01e94
~~~


<a id="compare-98bd27eea020547a4a75098b03b7bd56"></a>

### [`004a5348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md) → [`004a5668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5668.md) _ZNK5Botan19AlgorithmIdentifier11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59750.md) [`00c59760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59760.md) [`00c59770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a5370) · [`004a5384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a5384) · [`004a53a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md#insn-004a53a0)
- 新版 [`004a5690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5668.md#insn-004a5690) · [`004a56a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5668.md#insn-004a56a4) · [`004a56c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5668.md#insn-004a56c0)

~~~diff
- 004a5370 ["INT_ADD", "register:40f0:8", ["const:4a5370:8", "const:4:8"]]
- 004a5370 ["CALL", null, ["callee:00c59750:8"]]
+ 004a5690 ["INT_ADD", "register:40f0:8", ["const:4a5690:8", "const:4:8"]]
+ 004a5690 ["CALL", null, ["callee:00c59750:8"]]
- 004a5370 bytes 04cd1e94
+ 004a5690 bytes 30d01e94
- 004a5384 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5384 ["INT_ADD", "register:40f0:8", ["const:4a5384:8", "const:4:8"]]
- 004a5384 ["CALLIND", null, ["register:0:8"]]
+ 004a56a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a56a4 ["INT_ADD", "register:40f0:8", ["const:4a56a4:8", "const:4:8"]]
+ 004a56a4 ["CALLIND", null, ["register:0:8"]]
- 004a5384 bytes 00013fd6
+ 004a56a4 bytes 00013fd6
- 004a53a0 ["INT_ADD", "register:40f0:8", ["const:4a53a0:8", "const:4:8"]]
- 004a53a0 ["CALL", null, ["callee:00c59760:8"]]
+ 004a56c0 ["INT_ADD", "register:40f0:8", ["const:4a56c0:8", "const:4:8"]]
+ 004a56c0 ["CALL", null, ["callee:00c59760:8"]]
- 004a53a0 bytes fccc1e94
+ 004a56c0 bytes 28d01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-923aee4ba7a1abf9c9fcf4fb83c83785"></a>

### [`004a55a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55a8.md) → [`004a58c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a58c8.md) _ZN5Botan11DER_Encoder6encodeERKNS_11ASN1_ObjectE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a55c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55a8.md#insn-004a55c8)
- 新版 [`004a58e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a58c8.md#insn-004a58e8)

~~~diff
- 004a55c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a55c8 ["INT_ADD", "register:40f0:8", ["const:4a55c8:8", "const:4:8"]]
- 004a55c8 ["CALLIND", null, ["register:0:8"]]
+ 004a58e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a58e8 ["INT_ADD", "register:40f0:8", ["const:4a58e8:8", "const:4:8"]]
+ 004a58e8 ["CALLIND", null, ["register:0:8"]]
- 004a55c8 bytes 00013fd6
+ 004a58e8 bytes 00013fd6
~~~


<a id="compare-edfe5e596776ec58bd7a79c3591ef12c"></a>

### [`004a598c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a598c.md) → [`004a5cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5cac.md) _ZN5Botan11BER_Decoder6decodeERNS_11ASN1_ObjectENS_8ASN1_TagES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a59ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a598c.md#insn-004a59ac)
- 新版 [`004a5ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5cac.md#insn-004a5ccc)

~~~diff
- 004a59ac ["COPY", "register:0:8", ["register:4040:8"]]
- 004a59ac ["INT_ADD", "register:40f0:8", ["const:4a59ac:8", "const:4:8"]]
- 004a59ac ["CALLIND", null, ["register:0:8"]]
+ 004a5ccc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5ccc ["INT_ADD", "register:40f0:8", ["const:4a5ccc:8", "const:4:8"]]
+ 004a5ccc ["CALLIND", null, ["register:0:8"]]
- 004a59ac bytes 00013fd6
+ 004a5ccc bytes 00013fd6
~~~


<a id="compare-3a8df0f12349be79a75a99af6bde4ee9"></a>

### [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) → [`004a5ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md) FUN_004a5ce0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a5fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md) [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) [`0051f234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`004a5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5adc.md) [`004a6300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6300.md) [`005072f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md) [`00509f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md) [`0051f554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f554.md) · 呼出先 5件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a10) · [`004a5a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a44) · [`004a5a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md#insn-004a5a88)
- 新版 [`004a5d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md#insn-004a5d30) · [`004a5d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md#insn-004a5d64) · [`004a5da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md#insn-004a5da8)

~~~diff
- 004a5a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5a10 ["INT_ADD", "register:40f0:8", ["const:4a5a10:8", "const:4:8"]]
- 004a5a10 ["CALLIND", null, ["register:0:8"]]
+ 004a5d30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5d30 ["INT_ADD", "register:40f0:8", ["const:4a5d30:8", "const:4:8"]]
+ 004a5d30 ["CALLIND", null, ["register:0:8"]]
- 004a5a10 bytes 00013fd6
+ 004a5d30 bytes 00013fd6
- 004a5a44 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5a44 ["INT_ADD", "register:40f0:8", ["const:4a5a44:8", "const:4:8"]]
- 004a5a44 ["CALLIND", null, ["register:0:8"]]
+ 004a5d64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a5d64 ["INT_ADD", "register:40f0:8", ["const:4a5d64:8", "const:4:8"]]
+ 004a5d64 ["CALLIND", null, ["register:0:8"]]
- 004a5a44 bytes 00013fd6
+ 004a5d64 bytes 00013fd6
- 004a5a88 ["INT_ADD", "register:40f0:8", ["const:4a5a88:8", "const:4:8"]]
- 004a5a88 ["CALL", null, ["callee:00c58f30:8"]]
+ 004a5da8 ["INT_ADD", "register:40f0:8", ["const:4a5da8:8", "const:4:8"]]
+ 004a5da8 ["CALL", null, ["callee:00c58f30:8"]]
- 004a5a88 bytes 36c91e94
+ 004a5da8 bytes 62cc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89ec9752413debcfdba54291c4aa1879"></a>

### [`004a5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md) → [`004a621c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a621c.md) _ZNK5Botan9Attribute11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) [`00c58790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58790.md) [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59750.md) [`00c59760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59760.md) [`00c59770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f24) · [`004a5f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f38) · [`004a5f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md#insn-004a5f48)
- 新版 [`004a6244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a621c.md#insn-004a6244) · [`004a6258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a621c.md#insn-004a6258) · [`004a6268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a621c.md#insn-004a6268)

~~~diff
- 004a5f24 ["INT_ADD", "register:40f0:8", ["const:4a5f24:8", "const:4:8"]]
- 004a5f24 ["CALL", null, ["callee:00c59750:8"]]
+ 004a6244 ["INT_ADD", "register:40f0:8", ["const:4a6244:8", "const:4:8"]]
+ 004a6244 ["CALL", null, ["callee:00c59750:8"]]
- 004a5f24 bytes 17ca1e94
+ 004a6244 bytes 43cd1e94
- 004a5f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a5f38 ["INT_ADD", "register:40f0:8", ["const:4a5f38:8", "const:4:8"]]
- 004a5f38 ["CALLIND", null, ["register:0:8"]]
+ 004a6258 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004a6258 ["INT_ADD", "register:40f0:8", ["const:4a6258:8", "const:4:8"]]
+ 004a6258 ["CALLIND", null, ["register:0:8"]]
- 004a5f38 bytes 00013fd6
+ 004a6258 bytes 00013fd6
- 004a5f48 ["INT_ADD", "register:40f0:8", ["const:4a5f48:8", "const:4:8"]]
- 004a5f48 ["CALL", null, ["callee:00c59750:8"]]
+ 004a6268 ["INT_ADD", "register:40f0:8", ["const:4a6268:8", "const:4:8"]]
+ 004a6268 ["CALL", null, ["callee:00c59750:8"]]
- 004a5f48 bytes 0eca1e94
+ 004a6268 bytes 3acd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f00118095e0addc8d84f451b773b5e"></a>

### [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) → [`004a6bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md) FUN_004a6bac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`004af4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4c4.md) [`004bc3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md) [`004bef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md) [`004d7f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7f1c.md) [`004e8e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e8/004e8e40.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 12件 [`004af7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af7e4.md) [`004bc718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc718.md) [`004bf28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf28c.md) [`004d823c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d8/004d823c.md) [`004e9160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e9/004e9160.md) · 呼出先 1件 [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md#insn-004a68b4)
- 新版 [`004a6bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md#insn-004a6bd4)

~~~diff
- 004a68b4 ["INT_ADD", "register:40f0:8", ["const:4a68b4:8", "const:4:8"]]
- 004a68b4 ["CALL", null, ["callee:00c59020:8"]]
+ 004a6bd4 ["INT_ADD", "register:40f0:8", ["const:4a6bd4:8", "const:4:8"]]
+ 004a6bd4 ["CALL", null, ["callee:00c59020:8"]]
- 004a68b4 bytes e7c51e94
+ 004a6bd4 bytes 13c91e94
~~~


<a id="compare-2a95f646e0c21b5084c7ad8eeb7fd5eb"></a>

### [`004a7c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md) → [`004a7f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7f68.md) _ZN5Botan3OIDpLEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c588e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588e0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c598b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598b0.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a7cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7cc4) · [`004a7cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7cf0) · [`004a7d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md#insn-004a7d04)
- 新版 [`004a7fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7f68.md#insn-004a7fe4) · [`004a8010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7f68.md#insn-004a8010) · [`004a8024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7f68.md#insn-004a8024)

~~~diff
- 004a7cc4 ["INT_ADD", "register:40f0:8", ["const:4a7cc4:8", "const:4:8"]]
- 004a7cc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004a7fe4 ["INT_ADD", "register:40f0:8", ["const:4a7fe4:8", "const:4:8"]]
+ 004a7fe4 ["CALL", null, ["callee:00c58f30:8"]]
- 004a7cc4 bytes a7c01e94
+ 004a7fe4 bytes d3c31e94
- 004a7cf0 ["INT_ADD", "register:40f0:8", ["const:4a7cf0:8", "const:4:8"]]
- 004a7cf0 ["CALL", null, ["callee:00c590a0:8"]]
+ 004a8010 ["INT_ADD", "register:40f0:8", ["const:4a8010:8", "const:4:8"]]
+ 004a8010 ["CALL", null, ["callee:00c590a0:8"]]
- 004a7cf0 bytes f8c01e94
+ 004a8010 bytes 24c41e94
- 004a7d04 ["INT_ADD", "register:40f0:8", ["const:4a7d04:8", "const:4:8"]]
- 004a7d04 ["CALL", null, ["callee:00c58f50:8"]]
+ 004a8024 ["INT_ADD", "register:40f0:8", ["const:4a8024:8", "const:4:8"]]
+ 004a8024 ["CALL", null, ["callee:00c58f50:8"]]
- 004a7d04 bytes 9fc01e94
+ 004a8024 bytes cbc31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70b90b792d0ee4961658ef7b41355fc0"></a>

### [`004ac068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md) → [`004ac388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac388.md) _ZN5Botan6BigInt6encodeERKS0_NS0_4BaseE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c589a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589a0.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) [`00c58a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md)
- 新版 呼出元 1件 [`00c59970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59970.md) · 呼出先 5件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c599e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599e0.md) [`00c599f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac088) · [`004ac0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac0a4) · [`004ac0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac068.md#insn-004ac0c0)
- 新版 [`004ac3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac388.md#insn-004ac3a8) · [`004ac3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac388.md#insn-004ac3c4) · [`004ac3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac388.md#insn-004ac3e0)

~~~diff
- 004ac088 ["INT_ADD", "register:40f0:8", ["const:4ac088:8", "const:4:8"]]
- 004ac088 ["CALL", null, ["callee:00c599e0:8"]]
+ 004ac3a8 ["INT_ADD", "register:40f0:8", ["const:4ac3a8:8", "const:4:8"]]
+ 004ac3a8 ["CALL", null, ["callee:00c599e0:8"]]
- 004ac088 bytes 62b21e94
+ 004ac3a8 bytes 8eb51e94
- 004ac0a4 ["INT_ADD", "register:40f0:8", ["const:4ac0a4:8", "const:4:8"]]
- 004ac0a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004ac3c4 ["INT_ADD", "register:40f0:8", ["const:4ac3c4:8", "const:4:8"]]
+ 004ac3c4 ["CALL", null, ["callee:00c58f30:8"]]
- 004ac0a4 bytes afaf1e94
+ 004ac3c4 bytes dbb21e94
- 004ac0c0 ["INT_ADD", "register:40f0:8", ["const:4ac0c0:8", "const:4:8"]]
- 004ac0c0 ["CALL", null, ["callee:00c59130:8"]]
+ 004ac3e0 ["INT_ADD", "register:40f0:8", ["const:4ac3e0:8", "const:4:8"]]
+ 004ac3e0 ["CALL", null, ["callee:00c59130:8"]]
- 004ac0c0 bytes 28b01e94
+ 004ac3e0 bytes 54b31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053804f06f943e947aa37d77b419d70d"></a>

### [`004ac1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac1e0.md) → [`004ac500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac500.md) FUN_004ac500

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac1e0.md#insn-004ac1fc)
- 新版 [`004ac51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac500.md#insn-004ac51c)

~~~diff
- 004ac1fc ["INT_ADD", "register:40f0:8", ["const:4ac1fc:8", "const:4:8"]]
- 004ac1fc ["CALL", null, ["callee:00c58f50:8"]]
+ 004ac51c ["INT_ADD", "register:40f0:8", ["const:4ac51c:8", "const:4:8"]]
+ 004ac51c ["CALL", null, ["callee:00c58f50:8"]]
- 004ac1fc bytes 61af1e94
+ 004ac51c bytes 8db21e94
~~~


<a id="compare-01fc531a9af21cbff8a8a39d3b3415dc"></a>

### [`004acc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md) → [`004acf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004acf84.md) FUN_004acf84

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`005203b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md) [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) · 呼出先 3件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004acc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004acc7c) · [`004accb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004accb8) · [`004accdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md#insn-004accdc)
- 新版 [`004acf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004acf84.md#insn-004acf9c) · [`004acfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004acf84.md#insn-004acfd8) · [`004acffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004acf84.md#insn-004acffc)

~~~diff
- 004acc7c ["INT_ADD", "register:40f0:8", ["const:4acc7c:8", "const:4:8"]]
- 004acc7c ["CALL", null, ["callee:00c59080:8"]]
+ 004acf9c ["INT_ADD", "register:40f0:8", ["const:4acf9c:8", "const:4:8"]]
+ 004acf9c ["CALL", null, ["callee:00c59080:8"]]
- 004acc7c bytes 0dad1e94
+ 004acf9c bytes 39b01e94
- 004accb8 ["INT_ADD", "register:40f0:8", ["const:4accb8:8", "const:4:8"]]
- 004accb8 ["CALL", null, ["callee:00c590f0:8"]]
+ 004acfd8 ["INT_ADD", "register:40f0:8", ["const:4acfd8:8", "const:4:8"]]
+ 004acfd8 ["CALL", null, ["callee:00c590f0:8"]]
- 004accb8 bytes 1aad1e94
+ 004acfd8 bytes 46b01e94
- 004accdc ["INT_ADD", "register:40f0:8", ["const:4accdc:8", "const:4:8"]]
- 004accdc ["CALL", null, ["callee:00442c7c:8"]]
+ 004acffc ["INT_ADD", "register:40f0:8", ["const:4acffc:8", "const:4:8"]]
+ 004acffc ["CALL", null, ["callee:00442c7c:8"]]
- 004accdc bytes 2057fe97
+ 004acffc bytes 2057fe97
~~~


<a id="compare-75e4e6344c6f86881a2416714abcb66c"></a>

### [`004af1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md) → [`004af4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af4c0.md) _ZNK5Botan9X509_Time16to_std_timepointEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ad0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md#insn-004af1d0) · [`004af1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1a0.md#insn-004af1f4)
- 新版 [`004af4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af4c0.md#insn-004af4f0) · [`004af514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af4c0.md#insn-004af514)

~~~diff
- 004af1d0 ["INT_ADD", "register:40f0:8", ["const:4af1d0:8", "const:4:8"]]
- 004af1d0 ["CALL", null, ["callee:00c59aa0:8"]]
+ 004af4f0 ["INT_ADD", "register:40f0:8", ["const:4af4f0:8", "const:4:8"]]
+ 004af4f0 ["CALL", null, ["callee:00c59aa0:8"]]
- 004af1d0 bytes 40a61e94
+ 004af4f0 bytes 6ca91e94
- 004af1f4 ["INT_ADD", "register:40f0:8", ["const:4af1f4:8", "const:4:8"]]
- 004af1f4 ["CALL", null, ["callee:00c58f80:8"]]
+ 004af514 ["INT_ADD", "register:40f0:8", ["const:4af514:8", "const:4:8"]]
+ 004af514 ["CALL", null, ["callee:00c58f80:8"]]
- 004af1f4 bytes 6fa31e94
+ 004af514 bytes 9ba61e94
~~~


<a id="compare-95e21388263f5b97cb88622f997fc8a6"></a>

### [`004af420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af420.md) → [`004af740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af740.md) _ZN5BotaneqERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af420.md#insn-004af428)
- 新版 [`004af748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af740.md#insn-004af748)

~~~diff
- 004af428 ["INT_ADD", "register:40f0:8", ["const:4af428:8", "const:4:8"]]
- 004af428 ["CALL", null, ["callee:00c59a80:8"]]
+ 004af748 ["INT_ADD", "register:40f0:8", ["const:4af748:8", "const:4:8"]]
+ 004af748 ["CALL", null, ["callee:00c59a80:8"]]
- 004af428 bytes a2a51e94
+ 004af748 bytes cea81e94
~~~


<a id="compare-f4e8c029d764633a2e71e4deb65fc774"></a>

### [`004af43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af43c.md) → [`004af75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af75c.md) _ZN5BotanneERKNS_9X509_TimeES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004af444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af43c.md#insn-004af444)
- 新版 [`004af764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004af75c.md#insn-004af764)

~~~diff
- 004af444 ["INT_ADD", "register:40f0:8", ["const:4af444:8", "const:4:8"]]
- 004af444 ["CALL", null, ["callee:00c59a80:8"]]
+ 004af764 ["INT_ADD", "register:40f0:8", ["const:4af764:8", "const:4:8"]]
+ 004af764 ["CALL", null, ["callee:00c59a80:8"]]
- 004af444 bytes 9ba51e94
+ 004af764 bytes c7a81e94
~~~


