# v16.0.2 → v16.0.3 · 要調査の変更候補 (31)

[一覧の目次](README.md)

<a id="compare-987ea05f2fa1d2d37c5f5298abe5c74c"></a>

### [`00b2d534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d534.md) → [`00b2e528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e528.md) FUN_00b2e528

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d534.md#insn-00b2d53c)
- 新版 [`00b2e530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e528.md#insn-00b2e530)

~~~diff
- 00b2d53c ["INT_ADD", "register:40f0:8", ["const:b2d53c:8", "const:4:8"]]
- 00b2d53c ["CALL", null, ["callee:008524fc:8"]]
+ 00b2e530 ["INT_ADD", "register:40f0:8", ["const:b2e530:8", "const:4:8"]]
+ 00b2e530 ["CALL", null, ["callee:008524fc:8"]]
- 00b2d53c bytes 0590f497
+ 00b2e530 bytes f38ff497
~~~


<a id="compare-794801be93f3f4b00cc654c2c87568e2"></a>

### [`00b2d8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d8c0.md) → [`00b2e8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e8b4.md) FUN_00b2e8b4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00b2d4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d4e0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d8c0.md#insn-00b2d8e0)
- 新版 [`00b2e8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e8b4.md#insn-00b2e8d4)

~~~diff
- 00b2d8e0 ["INT_ADD", "register:40f0:8", ["const:b2d8e0:8", "const:4:8"]]
- 00b2d8e0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b2e8d4 ["INT_ADD", "register:40f0:8", ["const:b2e8d4:8", "const:4:8"]]
+ 00b2e8d4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b2d8e0 bytes a8a90494
+ 00b2e8d4 bytes 9fa90494
~~~


<a id="compare-e01185930f6aabac818edcc28f672dba"></a>

### [`00b2f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f88c.md) → [`00b30880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30880.md) FUN_00b30880

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`00664b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664b70.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00664d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664d5c.md) [`0070d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md) · 呼出先 1件 [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 18件 [`0060ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060a/0060ac90.md) [`00664f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664f20.md) [`00664fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664fbc.md) [`0066510c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/0066510c.md) [`0070d7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md) · 呼出先 1件 [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f88c.md#insn-00b2f894)
- 新版 [`00b30888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30880.md#insn-00b30888)

~~~diff
- 00b2f894 ["INT_ADD", "register:40f0:8", ["const:b2f894:8", "const:4:8"]]
- 00b2f894 ["CALL", null, ["callee:00b3cf24:8"]]
+ 00b30888 ["INT_ADD", "register:40f0:8", ["const:b30888:8", "const:4:8"]]
+ 00b30888 ["CALL", null, ["callee:00b3cf24:8"]]
- 00b2f894 bytes a7310094
+ 00b30888 bytes a7310094
~~~


<a id="compare-6c966c99f902d2ad49604377d0dcc815"></a>

### [`00b2f91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f91c.md) → [`00b30910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30910.md) FUN_00b30910

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`00664acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664acc.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00664c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c68.md) [`00665150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665150.md) · 呼出先 1件 [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 19件 [`0060ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060a/0060ac90.md) [`00664e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664e7c.md) [`00664fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664fbc.md) [`00665018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665018.md) [`00665500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665500.md) · 呼出先 1件 [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2f924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2f91c.md#insn-00b2f924)
- 新版 [`00b30918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30910.md#insn-00b30918)

~~~diff
- 00b2f924 ["INT_ADD", "register:40f0:8", ["const:b2f924:8", "const:4:8"]]
- 00b2f924 ["CALL", null, ["callee:00b3cf24:8"]]
+ 00b30918 ["INT_ADD", "register:40f0:8", ["const:b30918:8", "const:4:8"]]
+ 00b30918 ["CALL", null, ["callee:00b3cf24:8"]]
- 00b2f924 bytes 83310094
+ 00b30918 bytes 83310094
~~~


<a id="compare-859896ec2ffe620600f619ddd383c591"></a>

### [`00b2fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md) → [`00b30a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30a48.md) FUN_00b30a48

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 32件 [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`005fdc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fd/005fdc98.md) [`0063d954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md) [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 1件 [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 32件 [`005b0068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0068.md) [`005fe048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe048.md) [`0063dd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063dd04.md) [`0064a920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md) [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) · 呼出先 1件 [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2fa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md#insn-00b2fa68) · [`00b2fa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md#insn-00b2fa84)
- 新版 [`00b30a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30a48.md#insn-00b30a5c) · [`00b30a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30a48.md#insn-00b30a78)

~~~diff
- 00b2fa68 ["INT_ADD", "register:40f0:8", ["const:b2fa68:8", "const:4:8"]]
- 00b2fa68 ["CALL", null, ["callee:00b3cf24:8"]]
+ 00b30a5c ["INT_ADD", "register:40f0:8", ["const:b30a5c:8", "const:4:8"]]
+ 00b30a5c ["CALL", null, ["callee:00b3cf24:8"]]
- 00b2fa68 bytes 32310094
+ 00b30a5c bytes 32310094
- 00b2fa84 ["INT_ADD", "register:40f0:8", ["const:b2fa84:8", "const:4:8"]]
- 00b2fa84 ["CALL", null, ["callee:00b3cf24:8"]]
+ 00b30a78 ["INT_ADD", "register:40f0:8", ["const:b30a78:8", "const:4:8"]]
+ 00b30a78 ["CALL", null, ["callee:00b3cf24:8"]]
- 00b2fa84 bytes 2b310094
+ 00b30a78 bytes 2b310094
~~~


<a id="compare-2fdf88ab2ebb09ce1b4d7b83e6182977"></a>

### [`00b2fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fddc.md) → [`00b30dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30dd0.md) FUN_00b30dd0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2faa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2faa8.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00b308b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b308b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b30a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30a9c.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00b318a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b318a8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2fe38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fddc.md#insn-00b2fe38) · [`00b2fe4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fddc.md#insn-00b2fe4c) · [`00b2fe80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fddc.md#insn-00b2fe80)
- 新版 [`00b30e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30dd0.md#insn-00b30e2c) · [`00b30e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30dd0.md#insn-00b30e40) · [`00b30e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30dd0.md#insn-00b30e74)

~~~diff
- 00b2fe38 ["INT_ADD", "register:40f0:8", ["const:b2fe38:8", "const:4:8"]]
- 00b2fe38 ["CALL", null, ["callee:0043be80:8"]]
+ 00b30e2c ["INT_ADD", "register:40f0:8", ["const:b30e2c:8", "const:4:8"]]
+ 00b30e2c ["CALL", null, ["callee:0043be80:8"]]
- 00b2fe38 bytes 4a2fe497
+ 00b30e2c bytes 152ce497
- 00b2fe4c ["INT_ADD", "register:40f0:8", ["const:b2fe4c:8", "const:4:8"]]
- 00b2fe4c ["CALL", null, ["callee:0043be80:8"]]
+ 00b30e40 ["INT_ADD", "register:40f0:8", ["const:b30e40:8", "const:4:8"]]
+ 00b30e40 ["CALL", null, ["callee:0043be80:8"]]
- 00b2fe4c bytes 452fe497
+ 00b30e40 bytes 102ce497
- 00b2fe80 ["INT_ADD", "register:40f0:8", ["const:b2fe80:8", "const:4:8"]]
- 00b2fe80 ["CALL", null, ["callee:00b318a8:8"]]
+ 00b30e74 ["INT_ADD", "register:40f0:8", ["const:b30e74:8", "const:4:8"]]
+ 00b30e74 ["CALL", null, ["callee:00b318a8:8"]]
- 00b2fe80 bytes 8d020094
+ 00b30e74 bytes 8d020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053c43cc7aa7212b1bf2cec50d868bb4"></a>

### [`00b30678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b30678.md) → [`00b3166c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b3166c.md) FUN_00b3166c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b2ff14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2ff14.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00b319b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b319b4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b30f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30f08.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00b329a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b329a8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b306e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b30678.md#insn-00b306e0) · [`00b30708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b30678.md#insn-00b30708) · [`00b30734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b30678.md#insn-00b30734)
- 新版 [`00b316d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b3166c.md#insn-00b316d4) · [`00b316fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b3166c.md#insn-00b316fc) · [`00b31728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b3166c.md#insn-00b31728)

~~~diff
- 00b306e0 ["INT_ADD", "register:40f0:8", ["const:b306e0:8", "const:4:8"]]
- 00b306e0 ["CALL", null, ["callee:0043be80:8"]]
+ 00b316d4 ["INT_ADD", "register:40f0:8", ["const:b316d4:8", "const:4:8"]]
+ 00b316d4 ["CALL", null, ["callee:0043be80:8"]]
- 00b306e0 bytes 202de497
+ 00b316d4 bytes eb29e497
- 00b30708 ["INT_ADD", "register:40f0:8", ["const:b30708:8", "const:4:8"]]
- 00b30708 ["CALL", null, ["callee:0043be80:8"]]
+ 00b316fc ["INT_ADD", "register:40f0:8", ["const:b316fc:8", "const:4:8"]]
+ 00b316fc ["CALL", null, ["callee:0043be80:8"]]
- 00b30708 bytes 162de497
+ 00b316fc bytes e129e497
- 00b30734 ["INT_ADD", "register:40f0:8", ["const:b30734:8", "const:4:8"]]
- 00b30734 ["CALL", null, ["callee:0043be80:8"]]
+ 00b31728 ["INT_ADD", "register:40f0:8", ["const:b31728:8", "const:4:8"]]
+ 00b31728 ["CALL", null, ["callee:0043be80:8"]]
- 00b30734 bytes 0b2de497
+ 00b31728 bytes d629e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a006ddfa3bc8850e49a428f0a98152c"></a>

### [`00b319b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b319b4.md) → [`00b329a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b329a8.md) FUN_00b329a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b30678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b30/00b30678.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00b31bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b31bf4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b3166c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b31/00b3166c.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00b32be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b32be8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b31a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b319b4.md#insn-00b31a1c) · [`00b31a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b319b4.md#insn-00b31a44) · [`00b31a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b319b4.md#insn-00b31a70)
- 新版 [`00b32a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b329a8.md#insn-00b32a10) · [`00b32a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b329a8.md#insn-00b32a38) · [`00b32a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b32/00b329a8.md#insn-00b32a64)

~~~diff
- 00b31a1c ["INT_ADD", "register:40f0:8", ["const:b31a1c:8", "const:4:8"]]
- 00b31a1c ["CALL", null, ["callee:0043be80:8"]]
+ 00b32a10 ["INT_ADD", "register:40f0:8", ["const:b32a10:8", "const:4:8"]]
+ 00b32a10 ["CALL", null, ["callee:0043be80:8"]]
- 00b31a1c bytes 5128e497
+ 00b32a10 bytes 1c25e497
- 00b31a44 ["INT_ADD", "register:40f0:8", ["const:b31a44:8", "const:4:8"]]
- 00b31a44 ["CALL", null, ["callee:0043be80:8"]]
+ 00b32a38 ["INT_ADD", "register:40f0:8", ["const:b32a38:8", "const:4:8"]]
+ 00b32a38 ["CALL", null, ["callee:0043be80:8"]]
- 00b31a44 bytes 4728e497
+ 00b32a38 bytes 1225e497
- 00b31a70 ["INT_ADD", "register:40f0:8", ["const:b31a70:8", "const:4:8"]]
- 00b31a70 ["CALL", null, ["callee:0043be80:8"]]
+ 00b32a64 ["INT_ADD", "register:40f0:8", ["const:b32a64:8", "const:4:8"]]
+ 00b32a64 ["CALL", null, ["callee:0043be80:8"]]
- 00b31a70 bytes 3c28e497
+ 00b32a64 bytes 0725e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3097dd30715f12749c33b64e79a2672"></a>

### [`00b3479c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3479c.md) → [`00b35790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35790.md) FUN_00b35790

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b347b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3479c.md#insn-00b347b8) · [`00b347f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3479c.md#insn-00b347f4) · [`00b34804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3479c.md#insn-00b34804)
- 新版 [`00b357ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35790.md#insn-00b357ac) · [`00b357e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35790.md#insn-00b357e8) · [`00b357f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35790.md#insn-00b357f8)

~~~diff
- 00b347b8 ["INT_ADD", "register:40f0:8", ["const:b347b8:8", "const:4:8"]]
- 00b347b8 ["CALL", null, ["callee:0046d7f0:8"]]
+ 00b357ac ["INT_ADD", "register:40f0:8", ["const:b357ac:8", "const:4:8"]]
+ 00b357ac ["CALL", null, ["callee:0046d7f0:8"]]
- 00b347b8 bytes 46e3e497
+ 00b357ac bytes 11e0e497
- 00b347f4 ["INT_ADD", "register:40f0:8", ["const:b347f4:8", "const:4:8"]]
- 00b347f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b357e8 ["INT_ADD", "register:40f0:8", ["const:b357e8:8", "const:4:8"]]
+ 00b357e8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b347f4 bytes e38d0494
+ 00b357e8 bytes da8d0494
- 00b34804 ["INT_ADD", "register:40f0:8", ["const:b34804:8", "const:4:8"]]
- 00b34804 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b357f8 ["INT_ADD", "register:40f0:8", ["const:b357f8:8", "const:4:8"]]
+ 00b357f8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b34804 bytes df8d0494
+ 00b357f8 bytes d68d0494
~~~


<a id="compare-58ca9de5082318b3d4da6d7bcf818149"></a>

### [`00b34834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34834.md) → [`00b35828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35828.md) FUN_00b35828

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b3431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3431c.md) [`00b36a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36a90.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00b35310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35310.md) [`00b37a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b37/00b37a84.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b348a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34834.md#insn-00b348a0) · [`00b348b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34834.md#insn-00b348b0) · [`00b348d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34834.md#insn-00b348d0)
- 新版 [`00b35894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35828.md#insn-00b35894) · [`00b358a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35828.md#insn-00b358a4) · [`00b358c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35828.md#insn-00b358c4)

~~~diff
- 00b348a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b348a0 ["INT_ADD", "register:40f0:8", ["const:b348a0:8", "const:4:8"]]
- 00b348a0 ["CALLIND", null, ["register:0:8"]]
+ 00b35894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35894 ["INT_ADD", "register:40f0:8", ["const:b35894:8", "const:4:8"]]
+ 00b35894 ["CALLIND", null, ["register:0:8"]]
- 00b348a0 bytes 00013fd6
+ 00b35894 bytes 00013fd6
- 00b348b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b348b0 ["INT_ADD", "register:40f0:8", ["const:b348b0:8", "const:4:8"]]
- 00b348b0 ["CALLIND", null, ["register:0:8"]]
+ 00b358a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b358a4 ["INT_ADD", "register:40f0:8", ["const:b358a4:8", "const:4:8"]]
+ 00b358a4 ["CALLIND", null, ["register:0:8"]]
- 00b348b0 bytes 00013fd6
+ 00b358a4 bytes 00013fd6
- 00b348d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b348d0 ["INT_ADD", "register:40f0:8", ["const:b348d0:8", "const:4:8"]]
- 00b348d0 ["CALLIND", null, ["register:0:8"]]
+ 00b358c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b358c4 ["INT_ADD", "register:40f0:8", ["const:b358c4:8", "const:4:8"]]
+ 00b358c4 ["CALLIND", null, ["register:0:8"]]
- 00b348d0 bytes 00013fd6
+ 00b358c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b974f51ef8e7720108a6380eb1af5a6e"></a>

### [`00b3499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3499c.md) → [`00b35990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35990.md) FUN_00b35990

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b343e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b343e4.md) [`00b36b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36b58.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00b353d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b353d8.md) [`00b37b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b37/00b37b4c.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3499c.md#insn-00b34a08) · [`00b34a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3499c.md#insn-00b34a18) · [`00b34a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b3499c.md#insn-00b34a38)
- 新版 [`00b359fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35990.md#insn-00b359fc) · [`00b35a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35990.md#insn-00b35a0c) · [`00b35a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35990.md#insn-00b35a2c)

~~~diff
- 00b34a08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34a08 ["INT_ADD", "register:40f0:8", ["const:b34a08:8", "const:4:8"]]
- 00b34a08 ["CALLIND", null, ["register:0:8"]]
+ 00b359fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b359fc ["INT_ADD", "register:40f0:8", ["const:b359fc:8", "const:4:8"]]
+ 00b359fc ["CALLIND", null, ["register:0:8"]]
- 00b34a08 bytes 00013fd6
+ 00b359fc bytes 00013fd6
- 00b34a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34a18 ["INT_ADD", "register:40f0:8", ["const:b34a18:8", "const:4:8"]]
- 00b34a18 ["CALLIND", null, ["register:0:8"]]
+ 00b35a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35a0c ["INT_ADD", "register:40f0:8", ["const:b35a0c:8", "const:4:8"]]
+ 00b35a0c ["CALLIND", null, ["register:0:8"]]
- 00b34a18 bytes 00013fd6
+ 00b35a0c bytes 00013fd6
- 00b34a38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b34a38 ["INT_ADD", "register:40f0:8", ["const:b34a38:8", "const:4:8"]]
- 00b34a38 ["CALLIND", null, ["register:0:8"]]
+ 00b35a2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b35a2c ["INT_ADD", "register:40f0:8", ["const:b35a2c:8", "const:4:8"]]
+ 00b35a2c ["CALLIND", null, ["register:0:8"]]
- 00b34a38 bytes 00013fd6
+ 00b35a2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48829d77841ebcfa4070b85684354ee4"></a>

### [`00b34b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34b04.md) → [`00b35af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35af8.md) FUN_00b35af8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00b354a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b354a0.md) · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34b04.md#insn-00b34ba4) · [`00b34bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34b04.md#insn-00b34bc8) · [`00b34c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34b04.md#insn-00b34c0c)
- 新版 [`00b35b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35af8.md#insn-00b35b98) · [`00b35bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35af8.md#insn-00b35bbc) · [`00b35c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35af8.md#insn-00b35c00)

~~~diff
- 00b34ba4 ["INT_ADD", "register:40f0:8", ["const:b34ba4:8", "const:4:8"]]
- 00b34ba4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b35b98 ["INT_ADD", "register:40f0:8", ["const:b35b98:8", "const:4:8"]]
+ 00b35b98 ["CALL", null, ["callee:00c58f30:8"]]
- 00b34ba4 bytes ef8c0494
+ 00b35b98 bytes e68c0494
- 00b34bc8 ["INT_ADD", "register:40f0:8", ["const:b34bc8:8", "const:4:8"]]
- 00b34bc8 ["CALL", null, ["callee:00c59080:8"]]
+ 00b35bbc ["INT_ADD", "register:40f0:8", ["const:b35bbc:8", "const:4:8"]]
+ 00b35bbc ["CALL", null, ["callee:00c59080:8"]]
- 00b34bc8 bytes 3a8d0494
+ 00b35bbc bytes 318d0494
- 00b34c0c ["INT_ADD", "register:40f0:8", ["const:b34c0c:8", "const:4:8"]]
- 00b34c0c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b35c00 ["INT_ADD", "register:40f0:8", ["const:b35c00:8", "const:4:8"]]
+ 00b35c00 ["CALL", null, ["callee:00c58f30:8"]]
- 00b34c0c bytes d58c0494
+ 00b35c00 bytes cc8c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b56a749ea1b46bd9fcde3da5cabbd2c"></a>

### [`00b34d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34d00.md) → [`00b35cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35cf4.md) FUN_00b35cf4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00b354a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b354a0.md) · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b34da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34d00.md#insn-00b34da0) · [`00b34dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34d00.md#insn-00b34dc4) · [`00b34e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34d00.md#insn-00b34e08)
- 新版 [`00b35d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35cf4.md#insn-00b35d94) · [`00b35db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35cf4.md#insn-00b35db8) · [`00b35dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35cf4.md#insn-00b35dfc)

~~~diff
- 00b34da0 ["INT_ADD", "register:40f0:8", ["const:b34da0:8", "const:4:8"]]
- 00b34da0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b35d94 ["INT_ADD", "register:40f0:8", ["const:b35d94:8", "const:4:8"]]
+ 00b35d94 ["CALL", null, ["callee:00c58f30:8"]]
- 00b34da0 bytes 708c0494
+ 00b35d94 bytes 678c0494
- 00b34dc4 ["INT_ADD", "register:40f0:8", ["const:b34dc4:8", "const:4:8"]]
- 00b34dc4 ["CALL", null, ["callee:00c59080:8"]]
+ 00b35db8 ["INT_ADD", "register:40f0:8", ["const:b35db8:8", "const:4:8"]]
+ 00b35db8 ["CALL", null, ["callee:00c59080:8"]]
- 00b34dc4 bytes bb8c0494
+ 00b35db8 bytes b28c0494
- 00b34e08 ["INT_ADD", "register:40f0:8", ["const:b34e08:8", "const:4:8"]]
- 00b34e08 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b35dfc ["INT_ADD", "register:40f0:8", ["const:b35dfc:8", "const:4:8"]]
+ 00b35dfc ["CALL", null, ["callee:00c58f30:8"]]
- 00b34e08 bytes 568c0494
+ 00b35dfc bytes 4d8c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e9d761c8f27ecca4396f2543486355"></a>

### [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) → [`00b36f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md) FUN_00b36f08

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b35da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35da0.md) [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) · 呼出先 2件 [`00b35f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00b36d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36d94.md) [`00b36f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md) · 呼出先 2件 [`00b36f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b35f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md#insn-00b35f30) · [`00b35f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md#insn-00b35f3c) · [`00b35f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f14.md#insn-00b35f70)
- 新版 [`00b36f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md#insn-00b36f24) · [`00b36f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md#insn-00b36f30) · [`00b36f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f08.md#insn-00b36f64)

~~~diff
- 00b35f30 ["INT_ADD", "register:40f0:8", ["const:b35f30:8", "const:4:8"]]
- 00b35f30 ["CALL", null, ["local:b0:8"]]
+ 00b36f24 ["INT_ADD", "register:40f0:8", ["const:b36f24:8", "const:4:8"]]
+ 00b36f24 ["CALL", null, ["local:b0:8"]]
- 00b35f30 bytes f9ffff97
+ 00b36f24 bytes f9ffff97
- 00b35f3c ["INT_ADD", "register:40f0:8", ["const:b35f3c:8", "const:4:8"]]
- 00b35f3c ["CALL", null, ["local:b0:8"]]
+ 00b36f30 ["INT_ADD", "register:40f0:8", ["const:b36f30:8", "const:4:8"]]
+ 00b36f30 ["CALL", null, ["local:b0:8"]]
- 00b35f3c bytes f6ffff97
+ 00b36f30 bytes f6ffff97
- 00b35f70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b35f70 ["INT_ADD", "register:40f0:8", ["const:b35f70:8", "const:4:8"]]
- 00b35f70 ["CALLIND", null, ["register:0:8"]]
+ 00b36f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b36f64 ["INT_ADD", "register:40f0:8", ["const:b36f64:8", "const:4:8"]]
+ 00b36f64 ["CALLIND", null, ["register:0:8"]]
- 00b35f70 bytes 00013fd6
+ 00b36f64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a947b611ab2ac09cb043677baa416b4c"></a>

### [`00b35f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f94.md) → [`00b36f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f88.md) FUN_00b36f88

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b35da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35da8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00b36d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36d9c.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b36018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f94.md#insn-00b36018) · [`00b36044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35f94.md#insn-00b36044)
- 新版 [`00b3700c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f88.md#insn-00b3700c) · [`00b37038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36f88.md#insn-00b37038)

~~~diff
- 00b36018 ["INT_ADD", "register:40f0:8", ["const:b36018:8", "const:4:8"]]
- 00b36018 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3700c ["INT_ADD", "register:40f0:8", ["const:b3700c:8", "const:4:8"]]
+ 00b3700c ["CALL", null, ["callee:00c590f0:8"]]
- 00b36018 bytes 42880494
+ 00b3700c bytes 39880494
- 00b36044 ["INT_ADD", "register:40f0:8", ["const:b36044:8", "const:4:8"]]
- 00b36044 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b37038 ["INT_ADD", "register:40f0:8", ["const:b37038:8", "const:4:8"]]
+ 00b37038 ["CALL", null, ["callee:00c590f0:8"]]
- 00b36044 bytes 37880494
+ 00b37038 bytes 2e880494
~~~


<a id="compare-2dda2c396eb297779fac80d60505cb32"></a>

### [`00b37394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37394.md) → [`00b38388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38388.md) FUN_00b38388

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b38f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38f24.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b39f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b39f18.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b373d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37394.md#insn-00b373d0) · [`00b37400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37394.md#insn-00b37400) · [`00b37430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37394.md#insn-00b37430)
- 新版 [`00b383c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38388.md#insn-00b383c4) · [`00b383f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38388.md#insn-00b383f4) · [`00b38424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38388.md#insn-00b38424)

~~~diff
- 00b373d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b373d0 ["INT_ADD", "register:40f0:8", ["const:b373d0:8", "const:4:8"]]
- 00b373d0 ["CALLIND", null, ["register:0:8"]]
+ 00b383c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b383c4 ["INT_ADD", "register:40f0:8", ["const:b383c4:8", "const:4:8"]]
+ 00b383c4 ["CALLIND", null, ["register:0:8"]]
- 00b373d0 bytes 00013fd6
+ 00b383c4 bytes 00013fd6
- 00b37400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37400 ["INT_ADD", "register:40f0:8", ["const:b37400:8", "const:4:8"]]
- 00b37400 ["CALLIND", null, ["register:0:8"]]
+ 00b383f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b383f4 ["INT_ADD", "register:40f0:8", ["const:b383f4:8", "const:4:8"]]
+ 00b383f4 ["CALLIND", null, ["register:0:8"]]
- 00b37400 bytes 00013fd6
+ 00b383f4 bytes 00013fd6
- 00b37430 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b37430 ["INT_ADD", "register:40f0:8", ["const:b37430:8", "const:4:8"]]
- 00b37430 ["CALLIND", null, ["register:0:8"]]
+ 00b38424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b38424 ["INT_ADD", "register:40f0:8", ["const:b38424:8", "const:4:8"]]
+ 00b38424 ["CALLIND", null, ["register:0:8"]]
- 00b37430 bytes 00013fd6
+ 00b38424 bytes 00013fd6
~~~


<a id="compare-6a44280eae4458efbdde24463a996d9e"></a>

### [`00b38338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38338.md) → [`00b3932c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b3932c.md) FUN_00b3932c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b37e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37e64.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b38e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38e58.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b38380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38338.md#insn-00b38380) · [`00b383c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38338.md#insn-00b383c0) · [`00b383f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38338.md#insn-00b383f8)
- 新版 [`00b39374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b3932c.md#insn-00b39374) · [`00b393b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b3932c.md#insn-00b393b4) · [`00b393ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b3932c.md#insn-00b393ec)

~~~diff
- 00b38380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b38380 ["INT_ADD", "register:40f0:8", ["const:b38380:8", "const:4:8"]]
- 00b38380 ["CALLIND", null, ["register:0:8"]]
+ 00b39374 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b39374 ["INT_ADD", "register:40f0:8", ["const:b39374:8", "const:4:8"]]
+ 00b39374 ["CALLIND", null, ["register:0:8"]]
- 00b38380 bytes 00013fd6
+ 00b39374 bytes 00013fd6
- 00b383c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b383c0 ["INT_ADD", "register:40f0:8", ["const:b383c0:8", "const:4:8"]]
- 00b383c0 ["CALLIND", null, ["register:0:8"]]
+ 00b393b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b393b4 ["INT_ADD", "register:40f0:8", ["const:b393b4:8", "const:4:8"]]
+ 00b393b4 ["CALLIND", null, ["register:0:8"]]
- 00b383c0 bytes 00013fd6
+ 00b393b4 bytes 00013fd6
- 00b383f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b383f8 ["INT_ADD", "register:40f0:8", ["const:b383f8:8", "const:4:8"]]
- 00b383f8 ["CALLIND", null, ["register:0:8"]]
+ 00b393ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b393ec ["INT_ADD", "register:40f0:8", ["const:b393ec:8", "const:4:8"]]
+ 00b393ec ["CALLIND", null, ["register:0:8"]]
- 00b383f8 bytes 00013fd6
+ 00b393ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-299a9290f67cc6e76af41d3d8058057f"></a>

### [`00b39d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39d98.md) → [`00b3ad8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3ad8c.md) FUN_00b3ad8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b39a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39a00.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b3a9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3a9f4.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b39de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39d98.md#insn-00b39de0) · [`00b39e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39d98.md#insn-00b39e20) · [`00b39e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39d98.md#insn-00b39e58)
- 新版 [`00b3add4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3ad8c.md#insn-00b3add4) · [`00b3ae14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3ad8c.md#insn-00b3ae14) · [`00b3ae4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3ad8c.md#insn-00b3ae4c)

~~~diff
- 00b39de0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39de0 ["INT_ADD", "register:40f0:8", ["const:b39de0:8", "const:4:8"]]
- 00b39de0 ["CALLIND", null, ["register:0:8"]]
+ 00b3add4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3add4 ["INT_ADD", "register:40f0:8", ["const:b3add4:8", "const:4:8"]]
+ 00b3add4 ["CALLIND", null, ["register:0:8"]]
- 00b39de0 bytes 00013fd6
+ 00b3add4 bytes 00013fd6
- 00b39e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39e20 ["INT_ADD", "register:40f0:8", ["const:b39e20:8", "const:4:8"]]
- 00b39e20 ["CALLIND", null, ["register:0:8"]]
+ 00b3ae14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3ae14 ["INT_ADD", "register:40f0:8", ["const:b3ae14:8", "const:4:8"]]
+ 00b3ae14 ["CALLIND", null, ["register:0:8"]]
- 00b39e20 bytes 00013fd6
+ 00b3ae14 bytes 00013fd6
- 00b39e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b39e58 ["INT_ADD", "register:40f0:8", ["const:b39e58:8", "const:4:8"]]
- 00b39e58 ["CALLIND", null, ["register:0:8"]]
+ 00b3ae4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3ae4c ["INT_ADD", "register:40f0:8", ["const:b3ae4c:8", "const:4:8"]]
+ 00b3ae4c ["CALLIND", null, ["register:0:8"]]
- 00b39e58 bytes 00013fd6
+ 00b3ae4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7010d0416728bcaae5b52ca5e6c7dd4"></a>

### [`00b3afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md) → [`00b3bfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md) FUN_00b3bfac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b38fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38fa4.md) [`00b3afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md) · 呼出先 2件 [`00b3afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00b39f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b39f98.md) [`00b3bfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md) · 呼出先 2件 [`00b3bfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3afd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md#insn-00b3afd4) · [`00b3afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md#insn-00b3afe0) · [`00b3b014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md#insn-00b3b014)
- 新版 [`00b3bfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md#insn-00b3bfc8) · [`00b3bfd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md#insn-00b3bfd4) · [`00b3c008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bfac.md#insn-00b3c008)

~~~diff
- 00b3afd4 ["INT_ADD", "register:40f0:8", ["const:b3afd4:8", "const:4:8"]]
- 00b3afd4 ["CALL", null, ["local:b0:8"]]
+ 00b3bfc8 ["INT_ADD", "register:40f0:8", ["const:b3bfc8:8", "const:4:8"]]
+ 00b3bfc8 ["CALL", null, ["local:b0:8"]]
- 00b3afd4 bytes f9ffff97
+ 00b3bfc8 bytes f9ffff97
- 00b3afe0 ["INT_ADD", "register:40f0:8", ["const:b3afe0:8", "const:4:8"]]
- 00b3afe0 ["CALL", null, ["local:b0:8"]]
+ 00b3bfd4 ["INT_ADD", "register:40f0:8", ["const:b3bfd4:8", "const:4:8"]]
+ 00b3bfd4 ["CALL", null, ["local:b0:8"]]
- 00b3afe0 bytes f6ffff97
+ 00b3bfd4 bytes f6ffff97
- 00b3b014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b014 ["INT_ADD", "register:40f0:8", ["const:b3b014:8", "const:4:8"]]
- 00b3b014 ["CALLIND", null, ["register:0:8"]]
+ 00b3c008 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c008 ["INT_ADD", "register:40f0:8", ["const:b3c008:8", "const:4:8"]]
+ 00b3c008 ["CALLIND", null, ["register:0:8"]]
- 00b3b014 bytes 00013fd6
+ 00b3c008 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61557a05b5504e0cfb0961d346762b45"></a>

### [`00b3b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md) → [`00b3c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md) FUN_00b3c08c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b38fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b38/00b38fac.md) [`00b3b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md) · 呼出先 2件 [`00b3b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00b39fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b39/00b39fa0.md) [`00b3c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md) · 呼出先 2件 [`00b3c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md#insn-00b3b0b4) · [`00b3b0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md#insn-00b3b0c0) · [`00b3b0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b098.md#insn-00b3b0f8)
- 新版 [`00b3c0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md#insn-00b3c0a8) · [`00b3c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md#insn-00b3c0b4) · [`00b3c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c08c.md#insn-00b3c0ec)

~~~diff
- 00b3b0b4 ["INT_ADD", "register:40f0:8", ["const:b3b0b4:8", "const:4:8"]]
- 00b3b0b4 ["CALL", null, ["local:b0:8"]]
+ 00b3c0a8 ["INT_ADD", "register:40f0:8", ["const:b3c0a8:8", "const:4:8"]]
+ 00b3c0a8 ["CALL", null, ["local:b0:8"]]
- 00b3b0b4 bytes f9ffff97
+ 00b3c0a8 bytes f9ffff97
- 00b3b0c0 ["INT_ADD", "register:40f0:8", ["const:b3b0c0:8", "const:4:8"]]
- 00b3b0c0 ["CALL", null, ["local:b0:8"]]
+ 00b3c0b4 ["INT_ADD", "register:40f0:8", ["const:b3c0b4:8", "const:4:8"]]
+ 00b3c0b4 ["CALL", null, ["local:b0:8"]]
- 00b3b0c0 bytes f6ffff97
+ 00b3c0b4 bytes f6ffff97
- 00b3b0f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b0f8 ["INT_ADD", "register:40f0:8", ["const:b3b0f8:8", "const:4:8"]]
- 00b3b0f8 ["CALLIND", null, ["register:0:8"]]
+ 00b3c0ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c0ec ["INT_ADD", "register:40f0:8", ["const:b3c0ec:8", "const:4:8"]]
+ 00b3c0ec ["CALLIND", null, ["register:0:8"]]
- 00b3b0f8 bytes 00013fd6
+ 00b3c0ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5616283b01aa71a9c4403e1cb9f9f3e8"></a>

### [`00b3b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b148.md) → [`00b3c13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c13c.md) FUN_00b3c13c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b39a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39a00.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00b3b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b28c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b3a9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3a9f4.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00b3c280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c280.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b148.md#insn-00b3b17c) · [`00b3b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b148.md#insn-00b3b19c) · [`00b3b1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b148.md#insn-00b3b1d8)
- 新版 [`00b3c170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c13c.md#insn-00b3c170) · [`00b3c190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c13c.md#insn-00b3c190) · [`00b3c1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c13c.md#insn-00b3c1cc)

~~~diff
- 00b3b17c ["INT_ADD", "register:40f0:8", ["const:b3b17c:8", "const:4:8"]]
- 00b3b17c ["CALL", null, ["callee:00b3c280:8"]]
+ 00b3c170 ["INT_ADD", "register:40f0:8", ["const:b3c170:8", "const:4:8"]]
+ 00b3c170 ["CALL", null, ["callee:00b3c280:8"]]
- 00b3b17c bytes 44000094
+ 00b3c170 bytes 44000094
- 00b3b19c ["INT_ADD", "register:40f0:8", ["const:b3b19c:8", "const:4:8"]]
- 00b3b19c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3c190 ["INT_ADD", "register:40f0:8", ["const:b3c190:8", "const:4:8"]]
+ 00b3c190 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3b19c bytes 71730494
+ 00b3c190 bytes 68730494
- 00b3b1d8 ["INT_ADD", "register:40f0:8", ["const:b3b1d8:8", "const:4:8"]]
- 00b3b1d8 ["CALL", null, ["callee:0043be80:8"]]
+ 00b3c1cc ["INT_ADD", "register:40f0:8", ["const:b3c1cc:8", "const:4:8"]]
+ 00b3c1cc ["CALL", null, ["callee:0043be80:8"]]
- 00b3b1d8 bytes 6202e497
+ 00b3c1cc bytes 2dffe397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870106cec313e201cc852d26246217fe"></a>

### [`00b3b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b28c.md) → [`00b3c280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c280.md) FUN_00b3c280

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b148.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00b3c13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c13c.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b28c.md#insn-00b3b310) · [`00b3b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b28c.md#insn-00b3b33c)
- 新版 [`00b3c304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c280.md#insn-00b3c304) · [`00b3c330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c280.md#insn-00b3c330)

~~~diff
- 00b3b310 ["INT_ADD", "register:40f0:8", ["const:b3b310:8", "const:4:8"]]
- 00b3b310 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c304 ["INT_ADD", "register:40f0:8", ["const:b3c304:8", "const:4:8"]]
+ 00b3c304 ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b310 bytes 84730494
+ 00b3c304 bytes 7b730494
- 00b3b33c ["INT_ADD", "register:40f0:8", ["const:b3b33c:8", "const:4:8"]]
- 00b3b33c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c330 ["INT_ADD", "register:40f0:8", ["const:b3c330:8", "const:4:8"]]
+ 00b3c330 ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b33c bytes 79730494
+ 00b3c330 bytes 70730494
~~~


<a id="compare-c5476bcceade8f53da87ebfa4973e885"></a>

### [`00b3b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b390.md) → [`00b3c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c384.md) FUN_00b3c384

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b390.md#insn-00b3b3e8) · [`00b3b41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b390.md#insn-00b3b41c) · [`00b3b448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b390.md#insn-00b3b448)
- 新版 [`00b3c3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c384.md#insn-00b3c3dc) · [`00b3c410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c384.md#insn-00b3c410) · [`00b3c43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c384.md#insn-00b3c43c)

~~~diff
- 00b3b3e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b3e8 ["INT_ADD", "register:40f0:8", ["const:b3b3e8:8", "const:4:8"]]
- 00b3b3e8 ["CALLIND", null, ["register:0:8"]]
+ 00b3c3dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c3dc ["INT_ADD", "register:40f0:8", ["const:b3c3dc:8", "const:4:8"]]
+ 00b3c3dc ["CALLIND", null, ["register:0:8"]]
- 00b3b3e8 bytes 00013fd6
+ 00b3c3dc bytes 00013fd6
- 00b3b41c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b41c ["INT_ADD", "register:40f0:8", ["const:b3b41c:8", "const:4:8"]]
- 00b3b41c ["CALLIND", null, ["register:0:8"]]
+ 00b3c410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c410 ["INT_ADD", "register:40f0:8", ["const:b3c410:8", "const:4:8"]]
+ 00b3c410 ["CALLIND", null, ["register:0:8"]]
- 00b3b41c bytes 00013fd6
+ 00b3c410 bytes 00013fd6
- 00b3b448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b448 ["INT_ADD", "register:40f0:8", ["const:b3b448:8", "const:4:8"]]
- 00b3b448 ["CALLIND", null, ["register:0:8"]]
+ 00b3c43c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c43c ["INT_ADD", "register:40f0:8", ["const:b3c43c:8", "const:4:8"]]
+ 00b3c43c ["CALLIND", null, ["register:0:8"]]
- 00b3b448 bytes 00013fd6
+ 00b3c43c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-009bdef99ba843cedea9c11f6a536641"></a>

### [`00b3b46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md) → [`00b3c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c460.md) FUN_00b3c460

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b39ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b39ff0.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00b3b5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b5a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b3afe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3afe4.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00b3c598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c598.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md#insn-00b3b4a0) · [`00b3b4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md#insn-00b3b4c0) · [`00b3b4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md#insn-00b3b4fc)
- 新版 [`00b3c494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c460.md#insn-00b3c494) · [`00b3c4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c460.md#insn-00b3c4b4) · [`00b3c4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c460.md#insn-00b3c4f0)

~~~diff
- 00b3b4a0 ["INT_ADD", "register:40f0:8", ["const:b3b4a0:8", "const:4:8"]]
- 00b3b4a0 ["CALL", null, ["callee:00b3c598:8"]]
+ 00b3c494 ["INT_ADD", "register:40f0:8", ["const:b3c494:8", "const:4:8"]]
+ 00b3c494 ["CALL", null, ["callee:00b3c598:8"]]
- 00b3b4a0 bytes 41000094
+ 00b3c494 bytes 41000094
- 00b3b4c0 ["INT_ADD", "register:40f0:8", ["const:b3b4c0:8", "const:4:8"]]
- 00b3b4c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3c4b4 ["INT_ADD", "register:40f0:8", ["const:b3c4b4:8", "const:4:8"]]
+ 00b3c4b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3b4c0 bytes a8720494
+ 00b3c4b4 bytes 9f720494
- 00b3b4fc ["INT_ADD", "register:40f0:8", ["const:b3b4fc:8", "const:4:8"]]
- 00b3b4fc ["CALL", null, ["callee:0043be80:8"]]
+ 00b3c4f0 ["INT_ADD", "register:40f0:8", ["const:b3c4f0:8", "const:4:8"]]
+ 00b3c4f0 ["CALL", null, ["callee:0043be80:8"]]
- 00b3b4fc bytes 9901e497
+ 00b3c4f0 bytes 64fee397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0600896aaf1244737be3ee79cd4fb789"></a>

### [`00b3b5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b5a4.md) → [`00b3c598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c598.md) FUN_00b3c598

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3b46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b46c.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00b3c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c460.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b5a4.md#insn-00b3b628) · [`00b3b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b5a4.md#insn-00b3b654)
- 新版 [`00b3c61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c598.md#insn-00b3c61c) · [`00b3c648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c598.md#insn-00b3c648)

~~~diff
- 00b3b628 ["INT_ADD", "register:40f0:8", ["const:b3b628:8", "const:4:8"]]
- 00b3b628 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c61c ["INT_ADD", "register:40f0:8", ["const:b3c61c:8", "const:4:8"]]
+ 00b3c61c ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b628 bytes be720494
+ 00b3c61c bytes b5720494
- 00b3b654 ["INT_ADD", "register:40f0:8", ["const:b3b654:8", "const:4:8"]]
- 00b3b654 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c648 ["INT_ADD", "register:40f0:8", ["const:b3c648:8", "const:4:8"]]
+ 00b3c648 ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b654 bytes b3720494
+ 00b3c648 bytes aa720494
~~~


<a id="compare-b993494212dd6bda1181dfb5f919b2e5"></a>

### [`00b3b6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b6a8.md) → [`00b3c69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c69c.md) FUN_00b3c69c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b6a8.md#insn-00b3b704) · [`00b3b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b6a8.md#insn-00b3b730) · [`00b3b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b6a8.md#insn-00b3b740)
- 新版 [`00b3c6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c69c.md#insn-00b3c6f8) · [`00b3c724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c69c.md#insn-00b3c724) · [`00b3c734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c69c.md#insn-00b3c734)

~~~diff
- 00b3b704 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b704 ["INT_ADD", "register:40f0:8", ["const:b3b704:8", "const:4:8"]]
- 00b3b704 ["CALLIND", null, ["register:0:8"]]
+ 00b3c6f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c6f8 ["INT_ADD", "register:40f0:8", ["const:b3c6f8:8", "const:4:8"]]
+ 00b3c6f8 ["CALLIND", null, ["register:0:8"]]
- 00b3b704 bytes 00013fd6
+ 00b3c6f8 bytes 00013fd6
- 00b3b730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b730 ["INT_ADD", "register:40f0:8", ["const:b3b730:8", "const:4:8"]]
- 00b3b730 ["CALLIND", null, ["register:0:8"]]
+ 00b3c724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c724 ["INT_ADD", "register:40f0:8", ["const:b3c724:8", "const:4:8"]]
+ 00b3c724 ["CALLIND", null, ["register:0:8"]]
- 00b3b730 bytes 00013fd6
+ 00b3c724 bytes 00013fd6
- 00b3b740 ["INT_ADD", "register:40f0:8", ["const:b3b740:8", "const:4:8"]]
- 00b3b740 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b3c734 ["INT_ADD", "register:40f0:8", ["const:b3c734:8", "const:4:8"]]
+ 00b3c734 ["CALL", null, ["callee:00c58f50:8"]]
- 00b3b740 bytes 10720494
+ 00b3c734 bytes 07720494
~~~


<a id="compare-bf0466b7457393249dd4cdad1f38f9e1"></a>

### [`00b3b754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b754.md) → [`00b3c748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c748.md) FUN_00b3c748

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b3a48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3a48c.md) [`00b3a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3a654.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00b3b480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3b480.md) [`00b3b648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3b648.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b754.md#insn-00b3b7c0) · [`00b3b7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b754.md#insn-00b3b7d0) · [`00b3b7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b754.md#insn-00b3b7f0)
- 新版 [`00b3c7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c748.md#insn-00b3c7b4) · [`00b3c7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c748.md#insn-00b3c7c4) · [`00b3c7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c748.md#insn-00b3c7e4)

~~~diff
- 00b3b7c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b7c0 ["INT_ADD", "register:40f0:8", ["const:b3b7c0:8", "const:4:8"]]
- 00b3b7c0 ["CALLIND", null, ["register:0:8"]]
+ 00b3c7b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c7b4 ["INT_ADD", "register:40f0:8", ["const:b3c7b4:8", "const:4:8"]]
+ 00b3c7b4 ["CALLIND", null, ["register:0:8"]]
- 00b3b7c0 bytes 00013fd6
+ 00b3c7b4 bytes 00013fd6
- 00b3b7d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b7d0 ["INT_ADD", "register:40f0:8", ["const:b3b7d0:8", "const:4:8"]]
- 00b3b7d0 ["CALLIND", null, ["register:0:8"]]
+ 00b3c7c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c7c4 ["INT_ADD", "register:40f0:8", ["const:b3c7c4:8", "const:4:8"]]
+ 00b3c7c4 ["CALLIND", null, ["register:0:8"]]
- 00b3b7d0 bytes 00013fd6
+ 00b3c7c4 bytes 00013fd6
- 00b3b7f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b7f0 ["INT_ADD", "register:40f0:8", ["const:b3b7f0:8", "const:4:8"]]
- 00b3b7f0 ["CALLIND", null, ["register:0:8"]]
+ 00b3c7e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b3c7e4 ["INT_ADD", "register:40f0:8", ["const:b3c7e4:8", "const:4:8"]]
+ 00b3c7e4 ["CALLIND", null, ["register:0:8"]]
- 00b3b7f0 bytes 00013fd6
+ 00b3c7e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a0643429722b1d8ad1d706eed18b19"></a>

### [`00b3b8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b8bc.md) → [`00b3c8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c8b0.md) FUN_00b3c8b0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b3aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3aba8.md) [`00b3ac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3ac68.md) [`00b3ad74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3ad74.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00b3bb9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bb9c.md) [`00b3bc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bc5c.md) [`00b3bd68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bd68.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3b928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b8bc.md#insn-00b3b928) · [`00b3b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b8bc.md#insn-00b3b984)
- 新版 [`00b3c91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c8b0.md#insn-00b3c91c) · [`00b3c978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c8b0.md#insn-00b3c978)

~~~diff
- 00b3b928 ["INT_ADD", "register:40f0:8", ["const:b3b928:8", "const:4:8"]]
- 00b3b928 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c91c ["INT_ADD", "register:40f0:8", ["const:b3c91c:8", "const:4:8"]]
+ 00b3c91c ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b928 bytes fe710494
+ 00b3c91c bytes f5710494
- 00b3b984 ["INT_ADD", "register:40f0:8", ["const:b3b984:8", "const:4:8"]]
- 00b3b984 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3c978 ["INT_ADD", "register:40f0:8", ["const:b3c978:8", "const:4:8"]]
+ 00b3c978 ["CALL", null, ["callee:00c590f0:8"]]
- 00b3b984 bytes e7710494
+ 00b3c978 bytes de710494
~~~


<a id="compare-d4df1bdaa88345056becdecd28b06af8"></a>

### [`00b3b9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b9c0.md) → [`00b3c9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c9b4.md) FUN_00b3c9b4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b3ae34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3ae34.md) [`00b3aef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3aef4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00b3be28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3be28.md) [`00b3bee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3bee8.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ba2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b9c0.md#insn-00b3ba2c) · [`00b3ba88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3b9c0.md#insn-00b3ba88)
- 新版 [`00b3ca20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c9b4.md#insn-00b3ca20) · [`00b3ca7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3c9b4.md#insn-00b3ca7c)

~~~diff
- 00b3ba2c ["INT_ADD", "register:40f0:8", ["const:b3ba2c:8", "const:4:8"]]
- 00b3ba2c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3ca20 ["INT_ADD", "register:40f0:8", ["const:b3ca20:8", "const:4:8"]]
+ 00b3ca20 ["CALL", null, ["callee:00c590f0:8"]]
- 00b3ba2c bytes bd710494
+ 00b3ca20 bytes b4710494
- 00b3ba88 ["INT_ADD", "register:40f0:8", ["const:b3ba88:8", "const:4:8"]]
- 00b3ba88 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b3ca7c ["INT_ADD", "register:40f0:8", ["const:b3ca7c:8", "const:4:8"]]
+ 00b3ca7c ["CALL", null, ["callee:00c590f0:8"]]
- 00b3ba88 bytes a6710494
+ 00b3ca7c bytes 9d710494
~~~


<a id="compare-430fa269e9b0981959647967eecacdd2"></a>

### [`00b3bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf04.md) → [`00b3cef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef8.md) FUN_00b3cef8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) [`00846560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846560.md) · 呼出先 1件 [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md)
- 新版 呼出元 2件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) [`0084750c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/0084750c.md) · 呼出先 1件 [`005e8588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e8/005e8588.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3bf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf04.md#insn-00b3bf18)
- 新版 [`00b3cf0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef8.md#insn-00b3cf0c)

~~~diff
- 00b3bf18 ["INT_ADD", "register:40f0:8", ["const:b3bf18:8", "const:4:8"]]
- 00b3bf18 ["CALL", null, ["callee:005e8588:8"]]
+ 00b3cf0c ["INT_ADD", "register:40f0:8", ["const:b3cf0c:8", "const:4:8"]]
+ 00b3cf0c ["CALL", null, ["callee:005e8588:8"]]
- 00b3bf18 bytes b0b0ea97
+ 00b3cf0c bytes 9fadea97
~~~


<a id="compare-07102c6c78af55d5607d42ae40b17414"></a>

### [`00b3c3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c3a8.md) → [`00b3d39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d39c.md) FUN_00b3d39c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00767fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767fec.md) [`007685fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/007685fc.md) [`00768848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768848.md) [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) · 呼出先 5件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00b3c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c504.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 10件 [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`007683c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007683c8.md) [`007689d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007689d8.md) [`00768c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768c24.md) [`0076901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/0076901c.md) · 呼出先 5件 [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`00b3d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d4f8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3c3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c3a8.md#insn-00b3c3ec) · [`00b3c408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c3a8.md#insn-00b3c408) · [`00b3c444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c3a8.md#insn-00b3c444)
- 新版 [`00b3d3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d39c.md#insn-00b3d3e0) · [`00b3d3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d39c.md#insn-00b3d3fc) · [`00b3d438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d39c.md#insn-00b3d438)

~~~diff
- 00b3c3ec ["INT_ADD", "register:40f0:8", ["const:b3c3ec:8", "const:4:8"]]
- 00b3c3ec ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3d3e0 ["INT_ADD", "register:40f0:8", ["const:b3d3e0:8", "const:4:8"]]
+ 00b3d3e0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3c3ec bytes dd6e0494
+ 00b3d3e0 bytes d46e0494
- 00b3c408 ["INT_ADD", "register:40f0:8", ["const:b3c408:8", "const:4:8"]]
- 00b3c408 ["CALL", null, ["callee:00c59130:8"]]
+ 00b3d3fc ["INT_ADD", "register:40f0:8", ["const:b3d3fc:8", "const:4:8"]]
+ 00b3d3fc ["CALL", null, ["callee:00c59130:8"]]
- 00b3c408 bytes 566f0494
+ 00b3d3fc bytes 4d6f0494
- 00b3c444 ["INT_ADD", "register:40f0:8", ["const:b3c444:8", "const:4:8"]]
- 00b3c444 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3d438 ["INT_ADD", "register:40f0:8", ["const:b3d438:8", "const:4:8"]]
+ 00b3d438 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3c444 bytes c76e0494
+ 00b3d438 bytes be6e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e849e4f7008e1754475f6f53b03546b4"></a>

### [`00b3c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md) → [`00b3d754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d754.md) FUN_00b3d754

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00878310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md) · 呼出先 7件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00b3c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c504.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`008792bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008792bc.md) · 呼出先 7件 [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`00b3d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d4f8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3c7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md#insn-00b3c7d0) · [`00b3c82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md#insn-00b3c82c) · [`00b3c848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md#insn-00b3c848)
- 新版 [`00b3d7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d754.md#insn-00b3d7c4) · [`00b3d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d754.md#insn-00b3d820) · [`00b3d83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d754.md#insn-00b3d83c)

~~~diff
- 00b3c7d0 ["INT_ADD", "register:40f0:8", ["const:b3c7d0:8", "const:4:8"]]
- 00b3c7d0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b3d7c4 ["INT_ADD", "register:40f0:8", ["const:b3d7c4:8", "const:4:8"]]
+ 00b3d7c4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00b3c7d0 bytes 106e0494
+ 00b3d7c4 bytes 076e0494
- 00b3c82c ["INT_ADD", "register:40f0:8", ["const:b3c82c:8", "const:4:8"]]
- 00b3c82c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3d820 ["INT_ADD", "register:40f0:8", ["const:b3d820:8", "const:4:8"]]
+ 00b3d820 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3c82c bytes cd6d0494
+ 00b3d820 bytes c46d0494
- 00b3c848 ["INT_ADD", "register:40f0:8", ["const:b3c848:8", "const:4:8"]]
- 00b3c848 ["CALL", null, ["callee:00c59130:8"]]
+ 00b3d83c ["INT_ADD", "register:40f0:8", ["const:b3d83c:8", "const:4:8"]]
+ 00b3d83c ["CALL", null, ["callee:00c59130:8"]]
- 00b3c848 bytes 466e0494
+ 00b3d83c bytes 3d6e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ed059c98a5409616edc46e1ea94511"></a>

### [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md) → [`00b3d96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md) FUN_00b3d96c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`0048d95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d95c.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 20件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00476eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00476/00476eb0.md) [`0048dc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048dc7c.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 3件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3c9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md#insn-00b3c9e0) · [`00b3ca00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md#insn-00b3ca00) · [`00b3cb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md#insn-00b3cb5c)
- 新版 [`00b3d9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md#insn-00b3d9d4) · [`00b3d9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md#insn-00b3d9f4) · [`00b3db50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md#insn-00b3db50)

~~~diff
- 00b3c9e0 ["INT_ADD", "register:40f0:8", ["const:b3c9e0:8", "const:4:8"]]
- 00b3c9e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b3d9d4 ["INT_ADD", "register:40f0:8", ["const:b3d9d4:8", "const:4:8"]]
+ 00b3d9d4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3c9e0 bytes 606d0494
+ 00b3d9d4 bytes 576d0494
- 00b3ca00 ["INT_ADD", "register:40f0:8", ["const:b3ca00:8", "const:4:8"]]
- 00b3ca00 ["CALL", null, ["callee:00c59130:8"]]
+ 00b3d9f4 ["INT_ADD", "register:40f0:8", ["const:b3d9f4:8", "const:4:8"]]
+ 00b3d9f4 ["CALL", null, ["callee:00c59130:8"]]
- 00b3ca00 bytes d86d0494
+ 00b3d9f4 bytes cf6d0494
- 00b3cb5c ["INT_ADD", "register:40f0:8", ["const:b3cb5c:8", "const:4:8"]]
- 00b3cb5c ["CALL", null, ["callee:0043bac4:8"]]
+ 00b3db50 ["INT_ADD", "register:40f0:8", ["const:b3db50:8", "const:4:8"]]
+ 00b3db50 ["CALL", null, ["callee:0043bac4:8"]]
- 00b3cb5c bytes 12fbe397
+ 00b3db50 bytes ddf7e397
~~~


<a id="compare-90581d704553a1c945c56eb4ab1ccb0a"></a>

### [`00b3d554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d554.md) → [`00b3e548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e548.md) FUN_00b3e548

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b3e5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e5d8.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`00b3f5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f5cc.md) · 呼出先 1件 [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3d570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d554.md#insn-00b3d570) · [`00b3d580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d554.md#insn-00b3d580) · [`00b3d598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d554.md#insn-00b3d598)
- 新版 [`00b3e564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e548.md#insn-00b3e564) · [`00b3e574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e548.md#insn-00b3e574) · [`00b3e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e548.md#insn-00b3e58c)

~~~diff
- 00b3d570 ["INT_ADD", "register:40f0:8", ["const:b3d570:8", "const:4:8"]]
- 00b3d570 ["CALL", null, ["callee:00487c9c:8"]]
+ 00b3e564 ["INT_ADD", "register:40f0:8", ["const:b3e564:8", "const:4:8"]]
+ 00b3e564 ["CALL", null, ["callee:00487c9c:8"]]
- 00b3d570 bytes 0329e597
+ 00b3e564 bytes ce25e597
- 00b3d580 ["INT_ADD", "register:40f0:8", ["const:b3d580:8", "const:4:8"]]
- 00b3d580 ["CALL", null, ["callee:00487c9c:8"]]
+ 00b3e574 ["INT_ADD", "register:40f0:8", ["const:b3e574:8", "const:4:8"]]
+ 00b3e574 ["CALL", null, ["callee:00487c9c:8"]]
- 00b3d580 bytes ff28e597
+ 00b3e574 bytes ca25e597
- 00b3d598 ["INT_ADD", "register:40f0:8", ["const:b3d598:8", "const:4:8"]]
- 00b3d598 ["CALL", null, ["callee:00487c9c:8"]]
+ 00b3e58c ["INT_ADD", "register:40f0:8", ["const:b3e58c:8", "const:4:8"]]
+ 00b3e58c ["CALL", null, ["callee:00487c9c:8"]]
- 00b3d598 bytes f928e597
+ 00b3e58c bytes c425e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d44a649ad39cc257fa89a296bc53bbd6"></a>

### [`00b3e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md) → [`00b3f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md) FUN_00b3f4a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 40件 [`005cc724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md) [`00606514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606514.md) [`0067676c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067676c.md) [`00679574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00679/00679574.md) [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 40件 [`005ccad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccad4.md) [`006068c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/006068c4.md) [`00676b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676b1c.md) [`00679924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00679/00679924.md) [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3e4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md#insn-00b3e4c4) · [`00b3e508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md#insn-00b3e508) · [`00b3e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md#insn-00b3e51c)
- 新版 [`00b3f4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md#insn-00b3f4b8) · [`00b3f4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md#insn-00b3f4fc) · [`00b3f510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md#insn-00b3f510)

~~~diff
- 00b3e4c4 ["INT_ADD", "register:40f0:8", ["const:b3e4c4:8", "const:4:8"]]
- 00b3e4c4 ["CALL", null, ["callee:008524fc:8"]]
+ 00b3f4b8 ["INT_ADD", "register:40f0:8", ["const:b3f4b8:8", "const:4:8"]]
+ 00b3f4b8 ["CALL", null, ["callee:008524fc:8"]]
- 00b3e4c4 bytes 234cf497
+ 00b3f4b8 bytes 114cf497
- 00b3e508 ["INT_ADD", "register:40f0:8", ["const:b3e508:8", "const:4:8"]]
- 00b3e508 ["CALL", null, ["callee:008524fc:8"]]
+ 00b3f4fc ["INT_ADD", "register:40f0:8", ["const:b3f4fc:8", "const:4:8"]]
+ 00b3f4fc ["CALL", null, ["callee:008524fc:8"]]
- 00b3e508 bytes 124cf497
+ 00b3f4fc bytes 004cf497
- 00b3e51c ["INT_ADD", "register:40f0:8", ["const:b3e51c:8", "const:4:8"]]
- 00b3e51c ["CALL", null, ["callee:008524fc:8"]]
+ 00b3f510 ["INT_ADD", "register:40f0:8", ["const:b3f510:8", "const:4:8"]]
+ 00b3f510 ["CALL", null, ["callee:008524fc:8"]]
- 00b3e51c bytes 0d4cf497
+ 00b3f510 bytes fb4bf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882e1c47e4b04254e22c5f3e3d15e22f"></a>

### [`00b3f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f580.md) → [`00b40574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40574.md) FUN_00b40574

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b3e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e1d4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a07d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a07d9c.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b3f1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f1c8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f580.md#insn-00b3f600) · [`00b3f660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f580.md#insn-00b3f660) · [`00b3f694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f580.md#insn-00b3f694)
- 新版 [`00b405f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40574.md#insn-00b405f4) · [`00b40654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40574.md#insn-00b40654) · [`00b40688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40574.md#insn-00b40688)

~~~diff
- 00b3f600 ["INT_ADD", "register:40f0:8", ["const:b3f600:8", "const:4:8"]]
- 00b3f600 ["CALL", null, ["callee:00b3f1c8:8"]]
+ 00b405f4 ["INT_ADD", "register:40f0:8", ["const:b405f4:8", "const:4:8"]]
+ 00b405f4 ["CALL", null, ["callee:00b3f1c8:8"]]
- 00b3f600 bytes f5faff97
+ 00b405f4 bytes f5faff97
- 00b3f660 ["INT_ADD", "register:40f0:8", ["const:b3f660:8", "const:4:8"]]
- 00b3f660 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b40654 ["INT_ADD", "register:40f0:8", ["const:b40654:8", "const:4:8"]]
+ 00b40654 ["CALL", null, ["callee:00c58f30:8"]]
- 00b3f660 bytes 40620494
+ 00b40654 bytes 37620494
- 00b3f694 ["INT_ADD", "register:40f0:8", ["const:b3f694:8", "const:4:8"]]
- 00b3f694 ["CALL", null, ["callee:0043bf04:8"]]
+ 00b40688 ["INT_ADD", "register:40f0:8", ["const:b40688:8", "const:4:8"]]
+ 00b40688 ["CALL", null, ["callee:0043bf04:8"]]
- 00b3f694 bytes 54f1e397
+ 00b40688 bytes 1feee397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1b8995fc9d2f54a6f4695f694ea9b9"></a>

### [`00b3f7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f7c0.md) → [`00b407b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b407b4.md) FUN_00b407b4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006d8d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d58.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`009852e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/009852e8.md) [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 1件 [`00b3e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md)
- 新版 呼出元 6件 [`006d9108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9108.md) [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) [`00986294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986294.md) [`00986418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986418.md) [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) · 呼出先 1件 [`00b3f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3f/00b3f4a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f7c0.md#insn-00b3f7e0) · [`00b3f844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3f7c0.md#insn-00b3f844)
- 新版 [`00b407d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b407b4.md#insn-00b407d4) · [`00b40838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b407b4.md#insn-00b40838)

~~~diff
- 00b3f7e0 ["INT_ADD", "register:40f0:8", ["const:b3f7e0:8", "const:4:8"]]
- 00b3f7e0 ["CALL", null, ["callee:00b3f4a0:8"]]
+ 00b407d4 ["INT_ADD", "register:40f0:8", ["const:b407d4:8", "const:4:8"]]
+ 00b407d4 ["CALL", null, ["callee:00b3f4a0:8"]]
- 00b3f7e0 bytes 33fbff97
+ 00b407d4 bytes 33fbff97
- 00b3f844 ["INT_ADD", "register:40f0:8", ["const:b3f844:8", "const:4:8"]]
- 00b3f844 ["CALL", null, ["callee:00b3f4a0:8"]]
+ 00b40838 ["INT_ADD", "register:40f0:8", ["const:b40838:8", "const:4:8"]]
+ 00b40838 ["CALL", null, ["callee:00b3f4a0:8"]]
- 00b3f844 bytes 1afbff97
+ 00b40838 bytes 1afbff97
~~~


<a id="compare-ee3ff0f49d9b5893f9335c2ec3439355"></a>

### [`00b3ff0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff0c.md) → [`00b40f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40f00.md) FUN_00b40f00

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b40448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40448.md) · 呼出先 2件 [`00c5aa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa30.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00b4143c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b4143c.md) · 呼出先 2件 [`00c5ba00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba00.md) [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ff1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff0c.md#insn-00b3ff1c) · [`00b3ff2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff0c.md#insn-00b3ff2c)
- 新版 [`00b40f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40f00.md#insn-00b40f10) · [`00b40f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40f00.md#insn-00b40f20)

~~~diff
- 00b3ff1c ["INT_ADD", "register:40f0:8", ["const:b3ff1c:8", "const:4:8"]]
- 00b3ff1c ["CALL", null, ["callee:00c5bd00:8"]]
+ 00b40f10 ["INT_ADD", "register:40f0:8", ["const:b40f10:8", "const:4:8"]]
+ 00b40f10 ["CALL", null, ["callee:00c5bd00:8"]]
- 00b3ff1c bytes 856b0494
+ 00b40f10 bytes 7c6b0494
- 00b3ff2c ["INT_ADD", "register:40f0:8", ["const:b3ff2c:8", "const:4:8"]]
- 00b3ff2c ["CALL", null, ["callee:00c5ba00:8"]]
+ 00b40f20 ["INT_ADD", "register:40f0:8", ["const:b40f20:8", "const:4:8"]]
+ 00b40f20 ["CALL", null, ["callee:00c5ba00:8"]]
- 00b3ff2c bytes c16a0494
+ 00b40f20 bytes b86a0494
~~~


<a id="compare-e4add7ec87375826acccf267985fb8dc"></a>

### [`00b3ff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff40.md) → [`00b40f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40f34.md) FUN_00b40f34

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b40448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40448.md) · 呼出先 2件 [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00b4143c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b4143c.md) · 呼出先 2件 [`00c5b9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9e0.md) [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3ff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ff40.md#insn-00b3ff50)
- 新版 [`00b40f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b40/00b40f34.md#insn-00b40f44)

~~~diff
- 00b3ff50 ["INT_ADD", "register:40f0:8", ["const:b3ff50:8", "const:4:8"]]
- 00b3ff50 ["CALL", null, ["callee:00c5bd00:8"]]
+ 00b40f44 ["INT_ADD", "register:40f0:8", ["const:b40f44:8", "const:4:8"]]
+ 00b40f44 ["CALL", null, ["callee:00c5bd00:8"]]
- 00b3ff50 bytes 786b0494
+ 00b40f44 bytes 6f6b0494
~~~


<a id="compare-c04ae10017d99d12f436dba9ec7f4e28"></a>

### [`00b4018c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md) → [`00b41180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41180.md) _ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae10.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)
- 新版 呼出元 1件 [`00c5bde0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bde0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b401c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b401c0) · [`00b401e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b401e4) · [`00b401f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b401f8)
- 新版 [`00b411b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41180.md#insn-00b411b4) · [`00b411d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41180.md#insn-00b411d8) · [`00b411ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41180.md#insn-00b411ec)

~~~diff
- 00b401c0 ["INT_ADD", "register:40f0:8", ["const:b401c0:8", "const:4:8"]]
- 00b401c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b411b4 ["INT_ADD", "register:40f0:8", ["const:b411b4:8", "const:4:8"]]
+ 00b411b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b401c0 bytes 685f0494
+ 00b411b4 bytes 5f5f0494
- 00b401e4 ["INT_ADD", "register:40f0:8", ["const:b401e4:8", "const:4:8"]]
- 00b401e4 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00b411d8 ["INT_ADD", "register:40f0:8", ["const:b411d8:8", "const:4:8"]]
+ 00b411d8 ["CALL", null, ["callee:00c5bd10:8"]]
- 00b401e4 bytes d76a0494
+ 00b411d8 bytes ce6a0494
- 00b401f8 ["INT_ADD", "register:40f0:8", ["const:b401f8:8", "const:4:8"]]
- 00b401f8 ["CALL", null, ["callee:00c5bc80:8"]]
+ 00b411ec ["INT_ADD", "register:40f0:8", ["const:b411ec:8", "const:4:8"]]
+ 00b411ec ["CALL", null, ["callee:00c5bc80:8"]]
- 00b401f8 bytes ae6a0494
+ 00b411ec bytes a56a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1286c83d245d7971784ac5e708df1572"></a>

### [`00b4025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4025c.md) → [`00b41250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41250.md) _ZNSt6__ndk113__vector_baseIN8firebase10FutureBaseENS_9allocatorIS2_EEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4028c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4025c.md#insn-00b4028c) · [`00b402a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4025c.md#insn-00b402a4) · [`00b402b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4025c.md#insn-00b402b8)
- 新版 [`00b41280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41250.md#insn-00b41280) · [`00b41298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41250.md#insn-00b41298) · [`00b412ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41250.md#insn-00b412ac)

~~~diff
- 00b4028c ["INT_ADD", "register:40f0:8", ["const:b4028c:8", "const:4:8"]]
- 00b4028c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b41280 ["INT_ADD", "register:40f0:8", ["const:b41280:8", "const:4:8"]]
+ 00b41280 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b4028c bytes 116a0494
+ 00b41280 bytes 086a0494
- 00b402a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b402a4 ["INT_ADD", "register:40f0:8", ["const:b402a4:8", "const:4:8"]]
- 00b402a4 ["CALLIND", null, ["register:0:8"]]
+ 00b41298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41298 ["INT_ADD", "register:40f0:8", ["const:b41298:8", "const:4:8"]]
+ 00b41298 ["CALLIND", null, ["register:0:8"]]
- 00b402a4 bytes 00013fd6
+ 00b41298 bytes 00013fd6
- 00b402b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b402b8 ["INT_ADD", "register:40f0:8", ["const:b402b8:8", "const:4:8"]]
- 00b402b8 ["CALLIND", null, ["register:0:8"]]
+ 00b412ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b412ac ["INT_ADD", "register:40f0:8", ["const:b412ac:8", "const:4:8"]]
+ 00b412ac ["CALLIND", null, ["register:0:8"]]
- 00b402b8 bytes 00013fd6
+ 00b412ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d0e57885ae2104428615a91c4ec1b6"></a>

### [`00b403dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md) → [`00b413d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b413d0.md) _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae00.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5bdd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdd0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bdd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b403f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md#insn-00b403f8) · [`00b40404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md#insn-00b40404)
- 新版 [`00b413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b413d0.md#insn-00b413ec) · [`00b413f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b413d0.md#insn-00b413f8)

~~~diff
- 00b403f8 ["INT_ADD", "register:40f0:8", ["const:b403f8:8", "const:4:8"]]
- 00b403f8 ["CALL", null, ["callee:00c5bdd0:8"]]
+ 00b413ec ["INT_ADD", "register:40f0:8", ["const:b413ec:8", "const:4:8"]]
+ 00b413ec ["CALL", null, ["callee:00c5bdd0:8"]]
- 00b403f8 bytes 826a0494
+ 00b413ec bytes 796a0494
- 00b40404 ["INT_ADD", "register:40f0:8", ["const:b40404:8", "const:4:8"]]
- 00b40404 ["CALL", null, ["callee:00c5bdd0:8"]]
+ 00b413f8 ["INT_ADD", "register:40f0:8", ["const:b413f8:8", "const:4:8"]]
+ 00b413f8 ["CALL", null, ["callee:00c5bdd0:8"]]
- 00b40404 bytes 7f6a0494
+ 00b413f8 bytes 766a0494
~~~


<a id="compare-cd008229127528c9b519d30c6e760627"></a>

### [`00b41144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41144.md) → [`00b42138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42138.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b411b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41144.md#insn-00b411b8) · [`00b411dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41144.md#insn-00b411dc)
- 新版 [`00b421ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42138.md#insn-00b421ac) · [`00b421d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42138.md#insn-00b421d0)

~~~diff
- 00b411b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b411b8 ["INT_ADD", "register:40f0:8", ["const:b411b8:8", "const:4:8"]]
- 00b411b8 ["CALLIND", null, ["register:0:8"]]
+ 00b421ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b421ac ["INT_ADD", "register:40f0:8", ["const:b421ac:8", "const:4:8"]]
+ 00b421ac ["CALLIND", null, ["register:0:8"]]
- 00b411b8 bytes 00013fd6
+ 00b421ac bytes 00013fd6
- 00b411dc ["INT_ADD", "register:40f0:8", ["const:b411dc:8", "const:4:8"]]
- 00b411dc ["CALL", null, ["callee:00c58f80:8"]]
+ 00b421d0 ["INT_ADD", "register:40f0:8", ["const:b421d0:8", "const:4:8"]]
+ 00b421d0 ["CALL", null, ["callee:00c58f80:8"]]
- 00b411dc bytes 755b0494
+ 00b421d0 bytes 6c5b0494
~~~


<a id="compare-3692a6b9c4157e2de7b58cc3a61a2ab6"></a>

### [`00b41770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41770.md) → [`00b42764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42764.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcS6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b41798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41770.md#insn-00b41798) · [`00b417b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41770.md#insn-00b417b0) · [`00b417bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41770.md#insn-00b417bc)
- 新版 [`00b4278c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42764.md#insn-00b4278c) · [`00b427a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42764.md#insn-00b427a4) · [`00b427b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42764.md#insn-00b427b0)

~~~diff
- 00b41798 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41798 ["INT_ADD", "register:40f0:8", ["const:b41798:8", "const:4:8"]]
- 00b41798 ["CALLIND", null, ["register:0:8"]]
+ 00b4278c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4278c ["INT_ADD", "register:40f0:8", ["const:b4278c:8", "const:4:8"]]
+ 00b4278c ["CALLIND", null, ["register:0:8"]]
- 00b41798 bytes 00013fd6
+ 00b4278c bytes 00013fd6
- 00b417b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b417b0 ["INT_ADD", "register:40f0:8", ["const:b417b0:8", "const:4:8"]]
- 00b417b0 ["CALLIND", null, ["register:0:8"]]
+ 00b427a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b427a4 ["INT_ADD", "register:40f0:8", ["const:b427a4:8", "const:4:8"]]
+ 00b427a4 ["CALLIND", null, ["register:0:8"]]
- 00b417b0 bytes 00013fd6
+ 00b427a4 bytes 00013fd6
- 00b417bc ["INT_ADD", "register:40f0:8", ["const:b417bc:8", "const:4:8"]]
- 00b417bc ["CALL", null, ["callee:00c5c030:8"]]
+ 00b427b0 ["INT_ADD", "register:40f0:8", ["const:b427b0:8", "const:4:8"]]
+ 00b427b0 ["CALL", null, ["callee:00c5c030:8"]]
- 00b417bc bytes 29660494
+ 00b427b0 bytes 20660494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca7b94929fca38c79d8149905ea4c1bc"></a>

### [`00b41814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md) → [`00b42808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42808.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcd

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b41840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md#insn-00b41840) · [`00b4184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md#insn-00b4184c) · [`00b41864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md#insn-00b41864)
- 新版 [`00b42834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42808.md#insn-00b42834) · [`00b42840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42808.md#insn-00b42840) · [`00b42858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42808.md#insn-00b42858)

~~~diff
- 00b41840 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41840 ["INT_ADD", "register:40f0:8", ["const:b41840:8", "const:4:8"]]
- 00b41840 ["CALLIND", null, ["register:0:8"]]
+ 00b42834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b42834 ["INT_ADD", "register:40f0:8", ["const:b42834:8", "const:4:8"]]
+ 00b42834 ["CALLIND", null, ["register:0:8"]]
- 00b41840 bytes 00013fd6
+ 00b42834 bytes 00013fd6
- 00b4184c ["INT_ADD", "register:40f0:8", ["const:b4184c:8", "const:4:8"]]
- 00b4184c ["CALL", null, ["callee:00c5c030:8"]]
+ 00b42840 ["INT_ADD", "register:40f0:8", ["const:b42840:8", "const:4:8"]]
+ 00b42840 ["CALL", null, ["callee:00c5c030:8"]]
- 00b4184c bytes 05660494
+ 00b42840 bytes fc650494
- 00b41864 ["INT_ADD", "register:40f0:8", ["const:b41864:8", "const:4:8"]]
- 00b41864 ["CALL", null, ["callee:0057504c:8"]]
+ 00b42858 ["INT_ADD", "register:40f0:8", ["const:b42858:8", "const:4:8"]]
+ 00b42858 ["CALL", null, ["callee:0057504c:8"]]
- 00b41864 bytes 32cde897
+ 00b42858 bytes fdc9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98eab83a6c65898baecb765c0b096145"></a>

### [`00b41894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41894.md) → [`00b42888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42888.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b418bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41894.md#insn-00b418bc) · [`00b418c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41894.md#insn-00b418c8) · [`00b418e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41894.md#insn-00b418e0)
- 新版 [`00b428b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42888.md#insn-00b428b0) · [`00b428bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42888.md#insn-00b428bc) · [`00b428d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42888.md#insn-00b428d4)

~~~diff
- 00b418bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b418bc ["INT_ADD", "register:40f0:8", ["const:b418bc:8", "const:4:8"]]
- 00b418bc ["CALLIND", null, ["register:0:8"]]
+ 00b428b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b428b0 ["INT_ADD", "register:40f0:8", ["const:b428b0:8", "const:4:8"]]
+ 00b428b0 ["CALLIND", null, ["register:0:8"]]
- 00b418bc bytes 00013fd6
+ 00b428b0 bytes 00013fd6
- 00b418c8 ["INT_ADD", "register:40f0:8", ["const:b418c8:8", "const:4:8"]]
- 00b418c8 ["CALL", null, ["callee:00c5c030:8"]]
+ 00b428bc ["INT_ADD", "register:40f0:8", ["const:b428bc:8", "const:4:8"]]
+ 00b428bc ["CALL", null, ["callee:00c5c030:8"]]
- 00b418c8 bytes e6650494
+ 00b428bc bytes dd650494
- 00b418e0 ["INT_ADD", "register:40f0:8", ["const:b418e0:8", "const:4:8"]]
- 00b418e0 ["CALL", null, ["callee:0057504c:8"]]
+ 00b428d4 ["INT_ADD", "register:40f0:8", ["const:b428d4:8", "const:4:8"]]
+ 00b428d4 ["CALL", null, ["callee:0057504c:8"]]
- 00b418e0 bytes 13cde897
+ 00b428d4 bytes dec9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd5a513f837d900f3120501e2441d6a9"></a>

### [`00b4190c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4190c.md) → [`00b42900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42900.md) _ZN8firebase9analytics20AddArrayListToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b41934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4190c.md#insn-00b41934) · [`00b41940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4190c.md#insn-00b41940) · [`00b41958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4190c.md#insn-00b41958)
- 新版 [`00b42928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42900.md#insn-00b42928) · [`00b42934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42900.md#insn-00b42934) · [`00b4294c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42900.md#insn-00b4294c)

~~~diff
- 00b41934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41934 ["INT_ADD", "register:40f0:8", ["const:b41934:8", "const:4:8"]]
- 00b41934 ["CALLIND", null, ["register:0:8"]]
+ 00b42928 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b42928 ["INT_ADD", "register:40f0:8", ["const:b42928:8", "const:4:8"]]
+ 00b42928 ["CALLIND", null, ["register:0:8"]]
- 00b41934 bytes 00013fd6
+ 00b42928 bytes 00013fd6
- 00b41940 ["INT_ADD", "register:40f0:8", ["const:b41940:8", "const:4:8"]]
- 00b41940 ["CALL", null, ["callee:00c5c030:8"]]
+ 00b42934 ["INT_ADD", "register:40f0:8", ["const:b42934:8", "const:4:8"]]
+ 00b42934 ["CALL", null, ["callee:00c5c030:8"]]
- 00b41940 bytes c8650494
+ 00b42934 bytes bf650494
- 00b41958 ["INT_ADD", "register:40f0:8", ["const:b41958:8", "const:4:8"]]
- 00b41958 ["CALL", null, ["callee:0057504c:8"]]
+ 00b4294c ["INT_ADD", "register:40f0:8", ["const:b4294c:8", "const:4:8"]]
+ 00b4294c ["CALL", null, ["callee:0057504c:8"]]
- 00b41958 bytes f5cce897
+ 00b4294c bytes c0c9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c14f292686f87ecd144dc7f5effb79"></a>

### [`00b41984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41984.md) → [`00b42978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42978.md) _ZN8firebase9analytics17AddBundleToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b419ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41984.md#insn-00b419ac) · [`00b419b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41984.md#insn-00b419b8) · [`00b419d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41984.md#insn-00b419d0)
- 新版 [`00b429a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42978.md#insn-00b429a0) · [`00b429ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42978.md#insn-00b429ac) · [`00b429c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b42/00b42978.md#insn-00b429c4)

~~~diff
- 00b419ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b419ac ["INT_ADD", "register:40f0:8", ["const:b419ac:8", "const:4:8"]]
- 00b419ac ["CALLIND", null, ["register:0:8"]]
+ 00b429a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b429a0 ["INT_ADD", "register:40f0:8", ["const:b429a0:8", "const:4:8"]]
+ 00b429a0 ["CALLIND", null, ["register:0:8"]]
- 00b419ac bytes 00013fd6
+ 00b429a0 bytes 00013fd6
- 00b419b8 ["INT_ADD", "register:40f0:8", ["const:b419b8:8", "const:4:8"]]
- 00b419b8 ["CALL", null, ["callee:00c5c030:8"]]
+ 00b429ac ["INT_ADD", "register:40f0:8", ["const:b429ac:8", "const:4:8"]]
+ 00b429ac ["CALL", null, ["callee:00c5c030:8"]]
- 00b419b8 bytes aa650494
+ 00b429ac bytes a1650494
- 00b419d0 ["INT_ADD", "register:40f0:8", ["const:b419d0:8", "const:4:8"]]
- 00b419d0 ["CALL", null, ["callee:0057504c:8"]]
+ 00b429c4 ["INT_ADD", "register:40f0:8", ["const:b429c4:8", "const:4:8"]]
+ 00b429c4 ["CALL", null, ["callee:0057504c:8"]]
- 00b419d0 bytes d7cce897
+ 00b429c4 bytes a2c9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12a9890ee01f40b44019bd41ce3a6b5"></a>

### [`00b426e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md) → [`00b436d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b436d4.md) _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aea0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be70.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42700) · [`00b42714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42714) · [`00b42728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42728)
- 新版 [`00b436f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b436d4.md#insn-00b436f4) · [`00b43708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b436d4.md#insn-00b43708) · [`00b4371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b436d4.md#insn-00b4371c)

~~~diff
- 00b42700 ["INT_ADD", "register:40f0:8", ["const:b42700:8", "const:4:8"]]
- 00b42700 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00b436f4 ["INT_ADD", "register:40f0:8", ["const:b436f4:8", "const:4:8"]]
+ 00b436f4 ["CALL", null, ["callee:00c5bd10:8"]]
- 00b42700 bytes 90610494
+ 00b436f4 bytes 87610494
- 00b42714 ["INT_ADD", "register:40f0:8", ["const:b42714:8", "const:4:8"]]
- 00b42714 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00b43708 ["INT_ADD", "register:40f0:8", ["const:b43708:8", "const:4:8"]]
+ 00b43708 ["CALL", null, ["callee:00c5bea0:8"]]
- 00b42714 bytes ef610494
+ 00b43708 bytes e6610494
- 00b42728 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b42728 ["INT_ADD", "register:40f0:8", ["const:b42728:8", "const:4:8"]]
- 00b42728 ["CALLIND", null, ["register:0:8"]]
+ 00b4371c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4371c ["INT_ADD", "register:40f0:8", ["const:b4371c:8", "const:4:8"]]
+ 00b4371c ["CALLIND", null, ["register:0:8"]]
- 00b42728 bytes 00013fd6
+ 00b4371c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ea02ef24551e69efae56789b25fe8c"></a>

### [`00b42780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md) → [`00b43774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43774.md) _ZN8firebase9analytics29LogAppleTransactionLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b42794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b42794) · [`00b4279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b4279c) · [`00b427b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b427b0)
- 新版 [`00b43788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43774.md#insn-00b43788) · [`00b43790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43774.md#insn-00b43790) · [`00b437a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43774.md#insn-00b437a4)

~~~diff
- 00b42794 ["INT_ADD", "register:40f0:8", ["const:b42794:8", "const:4:8"]]
- 00b42794 ["CALL", null, ["callee:00c5bd50:8"]]
+ 00b43788 ["INT_ADD", "register:40f0:8", ["const:b43788:8", "const:4:8"]]
+ 00b43788 ["CALL", null, ["callee:00c5bd50:8"]]
- 00b42794 bytes 7b610494
+ 00b43788 bytes 72610494
- 00b4279c ["INT_ADD", "register:40f0:8", ["const:b4279c:8", "const:4:8"]]
- 00b4279c ["CALL", null, ["callee:00c5bd50:8"]]
+ 00b43790 ["INT_ADD", "register:40f0:8", ["const:b43790:8", "const:4:8"]]
+ 00b43790 ["CALL", null, ["callee:00c5bd50:8"]]
- 00b4279c bytes 79610494
+ 00b43790 bytes 70610494
- 00b427b0 ["INT_ADD", "register:40f0:8", ["const:b427b0:8", "const:4:8"]]
- 00b427b0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b437a4 ["INT_ADD", "register:40f0:8", ["const:b437a4:8", "const:4:8"]]
+ 00b437a4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b427b0 bytes c8600494
+ 00b437a4 bytes bf600494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e172145923446dc0495c52341a791ec3"></a>

### [`00b43074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43074.md) → [`00b44068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44068.md) _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHand

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae80.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5be50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be50.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43074.md#insn-00b43094) · [`00b430a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43074.md#insn-00b430a8) · [`00b430bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43074.md#insn-00b430bc)
- 新版 [`00b44088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44068.md#insn-00b44088) · [`00b4409c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44068.md#insn-00b4409c) · [`00b440b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44068.md#insn-00b440b0)

~~~diff
- 00b43094 ["INT_ADD", "register:40f0:8", ["const:b43094:8", "const:4:8"]]
- 00b43094 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00b44088 ["INT_ADD", "register:40f0:8", ["const:b44088:8", "const:4:8"]]
+ 00b44088 ["CALL", null, ["callee:00c5bd10:8"]]
- 00b43094 bytes 2b5f0494
+ 00b44088 bytes 225f0494
- 00b430a8 ["INT_ADD", "register:40f0:8", ["const:b430a8:8", "const:4:8"]]
- 00b430a8 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00b4409c ["INT_ADD", "register:40f0:8", ["const:b4409c:8", "const:4:8"]]
+ 00b4409c ["CALL", null, ["callee:00c5bea0:8"]]
- 00b430a8 bytes 8a5f0494
+ 00b4409c bytes 815f0494
- 00b430bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b430bc ["INT_ADD", "register:40f0:8", ["const:b430bc:8", "const:4:8"]]
- 00b430bc ["CALLIND", null, ["register:0:8"]]
+ 00b440b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b440b0 ["INT_ADD", "register:40f0:8", ["const:b440b0:8", "const:4:8"]]
+ 00b440b0 ["CALLIND", null, ["register:0:8"]]
- 00b430bc bytes 00013fd6
+ 00b440b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32bc9469c643d75e087e5cad67093d7f"></a>

### [`00b4333c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4333c.md) → [`00b44330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44330.md) _ZN8firebase6FutureIlEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae90.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00c5be60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be60.md) · 呼出先 3件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4335c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4333c.md#insn-00b4335c) · [`00b43370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4333c.md#insn-00b43370) · [`00b43384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4333c.md#insn-00b43384)
- 新版 [`00b44350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44330.md#insn-00b44350) · [`00b44364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44330.md#insn-00b44364) · [`00b44378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44330.md#insn-00b44378)

~~~diff
- 00b4335c ["INT_ADD", "register:40f0:8", ["const:b4335c:8", "const:4:8"]]
- 00b4335c ["CALL", null, ["callee:00c5bd10:8"]]
+ 00b44350 ["INT_ADD", "register:40f0:8", ["const:b44350:8", "const:4:8"]]
+ 00b44350 ["CALL", null, ["callee:00c5bd10:8"]]
- 00b4335c bytes 795e0494
+ 00b44350 bytes 705e0494
- 00b43370 ["INT_ADD", "register:40f0:8", ["const:b43370:8", "const:4:8"]]
- 00b43370 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00b44364 ["INT_ADD", "register:40f0:8", ["const:b44364:8", "const:4:8"]]
+ 00b44364 ["CALL", null, ["callee:00c5bea0:8"]]
- 00b43370 bytes d85e0494
+ 00b44364 bytes cf5e0494
- 00b43384 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43384 ["INT_ADD", "register:40f0:8", ["const:b43384:8", "const:4:8"]]
- 00b43384 ["CALLIND", null, ["register:0:8"]]
+ 00b44378 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44378 ["INT_ADD", "register:40f0:8", ["const:b44378:8", "const:4:8"]]
+ 00b44378 ["CALLIND", null, ["register:0:8"]]
- 00b43384 bytes 00013fd6
+ 00b44378 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2cdbffa16559b505b5ce88c0339fbe"></a>

### [`00b434b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b434b4.md) → [`00b444a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b444a8.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 1件 [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) · 呼出先 6件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b434dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b434b4.md#insn-00b434dc) · [`00b434f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b434b4.md#insn-00b434f4) · [`00b43508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b434b4.md#insn-00b43508)
- 新版 [`00b444d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b444a8.md#insn-00b444d0) · [`00b444e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b444a8.md#insn-00b444e8) · [`00b444fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b444a8.md#insn-00b444fc)

~~~diff
- 00b434dc ["INT_ADD", "register:40f0:8", ["const:b434dc:8", "const:4:8"]]
- 00b434dc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b444d0 ["INT_ADD", "register:40f0:8", ["const:b444d0:8", "const:4:8"]]
+ 00b444d0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b434dc bytes 7d5d0494
+ 00b444d0 bytes 745d0494
- 00b434f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b434f4 ["INT_ADD", "register:40f0:8", ["const:b434f4:8", "const:4:8"]]
- 00b434f4 ["CALLIND", null, ["register:0:8"]]
+ 00b444e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b444e8 ["INT_ADD", "register:40f0:8", ["const:b444e8:8", "const:4:8"]]
+ 00b444e8 ["CALLIND", null, ["register:0:8"]]
- 00b434f4 bytes 00013fd6
+ 00b444e8 bytes 00013fd6
- 00b43508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43508 ["INT_ADD", "register:40f0:8", ["const:b43508:8", "const:4:8"]]
- 00b43508 ["CALLIND", null, ["register:0:8"]]
+ 00b444fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b444fc ["INT_ADD", "register:40f0:8", ["const:b444fc:8", "const:4:8"]]
+ 00b444fc ["CALLIND", null, ["register:0:8"]]
- 00b43508 bytes 00013fd6
+ 00b444fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca572f7b3754615559f2c5d0cc7eccc"></a>

### [`00b4398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4398c.md) → [`00b44980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44980.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)
- 新版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4398c.md#insn-00b43a00) · [`00b43a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4398c.md#insn-00b43a34)
- 新版 [`00b449f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44980.md#insn-00b449f4) · [`00b44a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44980.md#insn-00b44a28)

~~~diff
- 00b43a00 ["INT_ADD", "register:40f0:8", ["const:b43a00:8", "const:4:8"]]
- 00b43a00 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b449f4 ["INT_ADD", "register:40f0:8", ["const:b449f4:8", "const:4:8"]]
+ 00b449f4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00b43a00 bytes 84510494
+ 00b449f4 bytes 7b510494
- 00b43a34 ["INT_ADD", "register:40f0:8", ["const:b43a34:8", "const:4:8"]]
- 00b43a34 ["CALL", null, ["callee:00c5c140:8"]]
+ 00b44a28 ["INT_ADD", "register:40f0:8", ["const:b44a28:8", "const:4:8"]]
+ 00b44a28 ["CALL", null, ["callee:00c5c140:8"]]
- 00b43a34 bytes cf5d0494
+ 00b44a28 bytes c65d0494
~~~


<a id="compare-f917d6db7666e8bdf9d2aa2e67c0ae19"></a>

### [`00b43a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md) → [`00b44a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44a48.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b160.md)
- 新版 呼出元 1件 [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43af4) · [`00b43b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43b0c) · [`00b43b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43b20)
- 新版 [`00b44ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44a48.md#insn-00b44ae8) · [`00b44b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44a48.md#insn-00b44b00) · [`00b44b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b44/00b44a48.md#insn-00b44b14)

~~~diff
- 00b43af4 ["INT_ADD", "register:40f0:8", ["const:b43af4:8", "const:4:8"]]
- 00b43af4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b44ae8 ["INT_ADD", "register:40f0:8", ["const:b44ae8:8", "const:4:8"]]
+ 00b44ae8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b43af4 bytes 1b510494
+ 00b44ae8 bytes 12510494
- 00b43b0c ["INT_ADD", "register:40f0:8", ["const:b43b0c:8", "const:4:8"]]
- 00b43b0c ["CALL", null, ["callee:00c590a0:8"]]
+ 00b44b00 ["INT_ADD", "register:40f0:8", ["const:b44b00:8", "const:4:8"]]
+ 00b44b00 ["CALL", null, ["callee:00c590a0:8"]]
- 00b43b0c bytes 71510494
+ 00b44b00 bytes 68510494
- 00b43b20 ["INT_ADD", "register:40f0:8", ["const:b43b20:8", "const:4:8"]]
- 00b43b20 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b44b14 ["INT_ADD", "register:40f0:8", ["const:b44b14:8", "const:4:8"]]
+ 00b44b14 ["CALL", null, ["callee:00c590a0:8"]]
- 00b43b20 bytes 6c510494
+ 00b44b14 bytes 63510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8318d0284cb0d2efd83be9d998caa89"></a>

### [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) → [`00b45048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45048.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b42d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md) [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`00b43d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b43/00b43d40.md) [`00bbd868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md) [`00bdf8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf8a8.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md#insn-00b44074)
- 新版 [`00b45068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45048.md#insn-00b45068)

~~~diff
- 00b44074 ["INT_ADD", "register:40f0:8", ["const:b44074:8", "const:4:8"]]
- 00b44074 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b45068 ["INT_ADD", "register:40f0:8", ["const:b45068:8", "const:4:8"]]
+ 00b45068 ["CALL", null, ["callee:00c58f50:8"]]
- 00b44074 bytes c34f0494
+ 00b45068 bytes ba4f0494
~~~


<a id="compare-bae928b1c6983ede16ef1d09615f069b"></a>

### [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) → [`00b451b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451b0.md) FUN_00b451b0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00b441ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md) [`00b446e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b446e8.md) [`00b44714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md) · 呼出先 2件 [`00b4475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4475c.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 3件 [`00b451e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451e0.md) [`00b456dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b456dc.md) [`00b45708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45708.md) · 呼出先 2件 [`00b45750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45750.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b441d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md#insn-00b441d0) · [`00b441e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md#insn-00b441e8)
- 新版 [`00b451c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451b0.md#insn-00b451c4) · [`00b451dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b451b0.md#insn-00b451dc)

~~~diff
- 00b441d0 ["INT_ADD", "register:40f0:8", ["const:b441d0:8", "const:4:8"]]
- 00b441d0 ["CALL", null, ["callee:00b45750:8"]]
+ 00b451c4 ["INT_ADD", "register:40f0:8", ["const:b451c4:8", "const:4:8"]]
+ 00b451c4 ["CALL", null, ["callee:00b45750:8"]]
- 00b441d0 bytes 63010094
+ 00b451c4 bytes 63010094
- 00b441e8 ["INT_ADD", "register:40f0:8", ["const:b441e8:8", "const:4:8"]]
- 00b441e8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b451dc ["INT_ADD", "register:40f0:8", ["const:b451dc:8", "const:4:8"]]
+ 00b451dc ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b441e8 bytes 0a5c0494
+ 00b451dc bytes 015c0494
~~~


<a id="compare-9319646e22b9033318db4472b08af058"></a>

### [`00b44320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44320.md) → [`00b45314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45314.md) _ZN8firebase8LogDebugEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4439c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44320.md#insn-00b4439c) · [`00b443c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44320.md#insn-00b443c0)
- 新版 [`00b45390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45314.md#insn-00b45390) · [`00b453b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45314.md#insn-00b453b4)

~~~diff
- 00b4439c ["INT_ADD", "register:40f0:8", ["const:b4439c:8", "const:4:8"]]
- 00b4439c ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b45390 ["INT_ADD", "register:40f0:8", ["const:b45390:8", "const:4:8"]]
+ 00b45390 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b4439c bytes 955b0494
+ 00b45390 bytes 8c5b0494
- 00b443c0 ["INT_ADD", "register:40f0:8", ["const:b443c0:8", "const:4:8"]]
- 00b443c0 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b453b4 ["INT_ADD", "register:40f0:8", ["const:b453b4:8", "const:4:8"]]
+ 00b453b4 ["CALL", null, ["callee:00c58f80:8"]]
- 00b443c0 bytes fc4e0494
+ 00b453b4 bytes f34e0494
~~~


<a id="compare-cd60dff18a4565853576d65fdc1d2a7a"></a>

### [`00b443c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b443c4.md) → [`00b453b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b453b8.md) _ZN8firebase7LogInfoEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0b0.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c080.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b443c4.md#insn-00b44440) · [`00b44464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b443c4.md#insn-00b44464)
- 新版 [`00b45434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b453b8.md#insn-00b45434) · [`00b45458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b453b8.md#insn-00b45458)

~~~diff
- 00b44440 ["INT_ADD", "register:40f0:8", ["const:b44440:8", "const:4:8"]]
- 00b44440 ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b45434 ["INT_ADD", "register:40f0:8", ["const:b45434:8", "const:4:8"]]
+ 00b45434 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b44440 bytes 6c5b0494
+ 00b45434 bytes 635b0494
- 00b44464 ["INT_ADD", "register:40f0:8", ["const:b44464:8", "const:4:8"]]
- 00b44464 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b45458 ["INT_ADD", "register:40f0:8", ["const:b45458:8", "const:4:8"]]
+ 00b45458 ["CALL", null, ["callee:00c58f80:8"]]
- 00b44464 bytes d34e0494
+ 00b45458 bytes ca4e0494
~~~


<a id="compare-c22d56470c38c72680e32c3ee5231203"></a>

### [`00b44468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44468.md) → [`00b4545c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4545c.md) _ZN8firebase10LogWarningEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b444e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44468.md#insn-00b444e4) · [`00b44508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44468.md#insn-00b44508)
- 新版 [`00b454d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4545c.md#insn-00b454d8) · [`00b454fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b4545c.md#insn-00b454fc)

~~~diff
- 00b444e4 ["INT_ADD", "register:40f0:8", ["const:b444e4:8", "const:4:8"]]
- 00b444e4 ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b454d8 ["INT_ADD", "register:40f0:8", ["const:b454d8:8", "const:4:8"]]
+ 00b454d8 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b444e4 bytes 435b0494
+ 00b454d8 bytes 3a5b0494
- 00b44508 ["INT_ADD", "register:40f0:8", ["const:b44508:8", "const:4:8"]]
- 00b44508 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b454fc ["INT_ADD", "register:40f0:8", ["const:b454fc:8", "const:4:8"]]
+ 00b454fc ["CALL", null, ["callee:00c58f80:8"]]
- 00b44508 bytes aa4e0494
+ 00b454fc bytes a14e0494
~~~


<a id="compare-2076791d036443f3ee4206f5ecf355e0"></a>

### [`00b4450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md) → [`00b45500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45500.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md#insn-00b44588) · [`00b445ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md#insn-00b445ac)
- 新版 [`00b4557c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45500.md#insn-00b4557c) · [`00b455a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45500.md#insn-00b455a0)

~~~diff
- 00b44588 ["INT_ADD", "register:40f0:8", ["const:b44588:8", "const:4:8"]]
- 00b44588 ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b4557c ["INT_ADD", "register:40f0:8", ["const:b4557c:8", "const:4:8"]]
+ 00b4557c ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b44588 bytes 1a5b0494
+ 00b4557c bytes 115b0494
- 00b445ac ["INT_ADD", "register:40f0:8", ["const:b445ac:8", "const:4:8"]]
- 00b445ac ["CALL", null, ["callee:00c58f80:8"]]
+ 00b455a0 ["INT_ADD", "register:40f0:8", ["const:b455a0:8", "const:4:8"]]
+ 00b455a0 ["CALL", null, ["callee:00c58f80:8"]]
- 00b445ac bytes 814e0494
+ 00b455a0 bytes 784e0494
~~~


<a id="compare-2c3fc1fc54af8bb15342ac724de53b3e"></a>

### [`00b445b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b445b0.md) → [`00b455a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b455a4.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4462c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b445b0.md#insn-00b4462c) · [`00b44650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b445b0.md#insn-00b44650)
- 新版 [`00b45620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b455a4.md#insn-00b45620) · [`00b45644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b455a4.md#insn-00b45644)

~~~diff
- 00b4462c ["INT_ADD", "register:40f0:8", ["const:b4462c:8", "const:4:8"]]
- 00b4462c ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b45620 ["INT_ADD", "register:40f0:8", ["const:b45620:8", "const:4:8"]]
+ 00b45620 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b4462c bytes f15a0494
+ 00b45620 bytes e85a0494
- 00b44650 ["INT_ADD", "register:40f0:8", ["const:b44650:8", "const:4:8"]]
- 00b44650 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b45644 ["INT_ADD", "register:40f0:8", ["const:b45644:8", "const:4:8"]]
+ 00b45644 ["CALL", null, ["callee:00c58f80:8"]]
- 00b44650 bytes 584e0494
+ 00b45644 bytes 4f4e0494
~~~


<a id="compare-a06f00ec100e332a95b6ad30b32ebdd3"></a>

### [`00b44654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44654.md) → [`00b45648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45648.md) _ZN8firebase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b190.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 1件 [`00c5c160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c160.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44654.md#insn-00b446c0) · [`00b446e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44654.md#insn-00b446e4)
- 新版 [`00b456b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45648.md#insn-00b456b4) · [`00b456d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45648.md#insn-00b456d8)

~~~diff
- 00b446c0 ["INT_ADD", "register:40f0:8", ["const:b446c0:8", "const:4:8"]]
- 00b446c0 ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b456b4 ["INT_ADD", "register:40f0:8", ["const:b456b4:8", "const:4:8"]]
+ 00b456b4 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b446c0 bytes cc5a0494
+ 00b456b4 bytes c35a0494
- 00b446e4 ["INT_ADD", "register:40f0:8", ["const:b446e4:8", "const:4:8"]]
- 00b446e4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b456d8 ["INT_ADD", "register:40f0:8", ["const:b456d8:8", "const:4:8"]]
+ 00b456d8 ["CALL", null, ["callee:00c58f80:8"]]
- 00b446e4 bytes 334e0494
+ 00b456d8 bytes 2a4e0494
~~~


<a id="compare-0cb2d489db9c5269ba29c5203cc65590"></a>

### [`00b4483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4483c.md) → [`00b45830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45830.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c290.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4483c.md#insn-00b44864) · [`00b44888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4483c.md#insn-00b44888)
- 新版 [`00b45858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45830.md#insn-00b45858) · [`00b4587c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45830.md#insn-00b4587c)

~~~diff
- 00b44864 ["INT_ADD", "register:40f0:8", ["const:b44864:8", "const:4:8"]]
- 00b44864 ["CALL", null, ["callee:00c5c290:8"]]
+ 00b45858 ["INT_ADD", "register:40f0:8", ["const:b45858:8", "const:4:8"]]
+ 00b45858 ["CALL", null, ["callee:00c5c290:8"]]
- 00b44864 bytes 975a0494
+ 00b45858 bytes 8e5a0494
- 00b44888 ["INT_ADD", "register:40f0:8", ["const:b44888:8", "const:4:8"]]
- 00b44888 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b4587c ["INT_ADD", "register:40f0:8", ["const:b4587c:8", "const:4:8"]]
+ 00b4587c ["CALL", null, ["callee:00c58f80:8"]]
- 00b44888 bytes ca4d0494
+ 00b4587c bytes c14d0494
~~~


<a id="compare-17ef7d004a80df96528ff727d961fb35"></a>

### [`00b44c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44c74.md) → [`00b45c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45c68.md) _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b44c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44c74.md#insn-00b44c8c) · [`00b44ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44c74.md#insn-00b44ca4) · [`00b44cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44c74.md#insn-00b44cb4)
- 新版 [`00b45c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45c68.md#insn-00b45c80) · [`00b45c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45c68.md#insn-00b45c98) · [`00b45ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45c68.md#insn-00b45ca8)

~~~diff
- 00b44c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44c8c ["INT_ADD", "register:40f0:8", ["const:b44c8c:8", "const:4:8"]]
- 00b44c8c ["CALLIND", null, ["register:0:8"]]
+ 00b45c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45c80 ["INT_ADD", "register:40f0:8", ["const:b45c80:8", "const:4:8"]]
+ 00b45c80 ["CALLIND", null, ["register:0:8"]]
- 00b44c8c bytes 00013fd6
+ 00b45c80 bytes 00013fd6
- 00b44ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44ca4 ["INT_ADD", "register:40f0:8", ["const:b44ca4:8", "const:4:8"]]
- 00b44ca4 ["CALLIND", null, ["register:0:8"]]
+ 00b45c98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45c98 ["INT_ADD", "register:40f0:8", ["const:b45c98:8", "const:4:8"]]
+ 00b45c98 ["CALLIND", null, ["register:0:8"]]
- 00b44ca4 bytes 00013fd6
+ 00b45c98 bytes 00013fd6
- 00b44cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44cb4 ["INT_ADD", "register:40f0:8", ["const:b44cb4:8", "const:4:8"]]
- 00b44cb4 ["CALLIND", null, ["register:0:8"]]
+ 00b45ca8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45ca8 ["INT_ADD", "register:40f0:8", ["const:b45ca8:8", "const:4:8"]]
+ 00b45ca8 ["CALLIND", null, ["register:0:8"]]
- 00b44cb4 bytes 00013fd6
+ 00b45ca8 bytes 00013fd6
~~~


<a id="compare-274fc0aaabfcfd0ccfce760dea678ed9"></a>

### [`00b517a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b517a0.md) → [`00b52794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52794.md) _ZN7_JNIEnv20CallStaticVoidMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b310.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2e0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b51814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b517a0.md#insn-00b51814) · [`00b51838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b517a0.md#insn-00b51838)
- 新版 [`00b52808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52794.md#insn-00b52808) · [`00b5282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52794.md#insn-00b5282c)

~~~diff
- 00b51814 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b51814 ["INT_ADD", "register:40f0:8", ["const:b51814:8", "const:4:8"]]
- 00b51814 ["CALLIND", null, ["register:0:8"]]
+ 00b52808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52808 ["INT_ADD", "register:40f0:8", ["const:b52808:8", "const:4:8"]]
+ 00b52808 ["CALLIND", null, ["register:0:8"]]
- 00b51814 bytes 00013fd6
+ 00b52808 bytes 00013fd6
- 00b51838 ["INT_ADD", "register:40f0:8", ["const:b51838:8", "const:4:8"]]
- 00b51838 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5282c ["INT_ADD", "register:40f0:8", ["const:b5282c:8", "const:4:8"]]
+ 00b5282c ["CALL", null, ["callee:00c58f80:8"]]
- 00b51838 bytes de190494
+ 00b5282c bytes d5190494
~~~


<a id="compare-f8541b1ff19b1c819b978cd72a0facee"></a>

### [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) → [`00b52830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52830.md) FUN_00b52830

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00b44de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md) [`00b450f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md)
- 新版 呼出元 2件 [`00b45dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45dd4.md) [`00b460ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b46/00b460ec.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b518ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md#insn-00b518ac) · [`00b518d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md#insn-00b518d0)
- 新版 [`00b528a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52830.md#insn-00b528a0) · [`00b528c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b52/00b52830.md#insn-00b528c4)

~~~diff
- 00b518ac ["INT_ADD", "register:40f0:8", ["const:b518ac:8", "const:4:8"]]
- 00b518ac ["CALL", null, ["callee:00c5c1f0:8"]]
+ 00b528a0 ["INT_ADD", "register:40f0:8", ["const:b528a0:8", "const:4:8"]]
+ 00b528a0 ["CALL", null, ["callee:00c5c1f0:8"]]
- 00b518ac bytes 5d260494
+ 00b528a0 bytes 54260494
- 00b518d0 ["INT_ADD", "register:40f0:8", ["const:b518d0:8", "const:4:8"]]
- 00b518d0 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b528c4 ["INT_ADD", "register:40f0:8", ["const:b528c4:8", "const:4:8"]]
+ 00b528c4 ["CALL", null, ["callee:00c58f80:8"]]
- 00b518d0 bytes b8190494
+ 00b528c4 bytes af190494
~~~


<a id="compare-38767bd72cff0519c37256028042e53d"></a>

### [`00b533e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b533e8.md) → [`00b543dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b543dc.md) _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md) · 呼出先 1件 [`00c5aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aff0.md)
- 新版 呼出元 1件 [`00c5c430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md) · 呼出先 1件 [`00c5bfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b533fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b533e8.md#insn-00b533fc)
- 新版 [`00b543f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b543dc.md#insn-00b543f0)

~~~diff
- 00b533fc ["INT_ADD", "register:40f0:8", ["const:b533fc:8", "const:4:8"]]
- 00b533fc ["CALL", null, ["callee:00c5bfc0:8"]]
+ 00b543f0 ["INT_ADD", "register:40f0:8", ["const:b543f0:8", "const:4:8"]]
+ 00b543f0 ["CALL", null, ["callee:00c5bfc0:8"]]
- 00b533fc bytes fd1e0494
+ 00b543f0 bytes f41e0494
~~~


<a id="compare-2727f7be2c1860e25b1c9f7c65eaf61d"></a>

### [`00b536dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b536dc.md) → [`00b546d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b546d0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ac80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac80.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5bc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc50.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b53738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b536dc.md#insn-00b53738) · [`00b537b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b536dc.md#insn-00b537b0) · [`00b537e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b536dc.md#insn-00b537e8)
- 新版 [`00b5472c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b546d0.md#insn-00b5472c) · [`00b547a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b546d0.md#insn-00b547a4) · [`00b547dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b546d0.md#insn-00b547dc)

~~~diff
- 00b53738 ["INT_ADD", "register:40f0:8", ["const:b53738:8", "const:4:8"]]
- 00b53738 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5472c ["INT_ADD", "register:40f0:8", ["const:b5472c:8", "const:4:8"]]
+ 00b5472c ["CALL", null, ["callee:00c58f30:8"]]
- 00b53738 bytes 0a120494
+ 00b5472c bytes 01120494
- 00b537b0 ["INT_ADD", "register:40f0:8", ["const:b537b0:8", "const:4:8"]]
- 00b537b0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b547a4 ["INT_ADD", "register:40f0:8", ["const:b547a4:8", "const:4:8"]]
+ 00b547a4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b537b0 bytes f4110494
+ 00b547a4 bytes eb110494
- 00b537e8 ["INT_ADD", "register:40f0:8", ["const:b537e8:8", "const:4:8"]]
- 00b537e8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b547dc ["INT_ADD", "register:40f0:8", ["const:b547dc:8", "const:4:8"]]
+ 00b547dc ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b537e8 bytes 8a1e0494
+ 00b547dc bytes 811e0494
~~~


<a id="compare-b64fddb7ead69c92d1afa97140fcd861"></a>

### [`00b53cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md) → [`00b54ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54ca0.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b700.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6d0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b53d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md#insn-00b53d0c) · [`00b53d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md#insn-00b53d4c) · [`00b53d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53cac.md#insn-00b53d88)
- 新版 [`00b54d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54ca0.md#insn-00b54d00) · [`00b54d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54ca0.md#insn-00b54d40) · [`00b54d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54ca0.md#insn-00b54d7c)

~~~diff
- 00b53d0c ["INT_ADD", "register:40f0:8", ["const:b53d0c:8", "const:4:8"]]
- 00b53d0c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b54d00 ["INT_ADD", "register:40f0:8", ["const:b54d00:8", "const:4:8"]]
+ 00b54d00 ["CALL", null, ["callee:00c58f30:8"]]
- 00b53d0c bytes 95100494
+ 00b54d00 bytes 8c100494
- 00b53d4c ["INT_ADD", "register:40f0:8", ["const:b53d4c:8", "const:4:8"]]
- 00b53d4c ["CALL", null, ["callee:00c5b8e0:8"]]
+ 00b54d40 ["INT_ADD", "register:40f0:8", ["const:b54d40:8", "const:4:8"]]
+ 00b54d40 ["CALL", null, ["callee:00c5b8e0:8"]]
- 00b53d4c bytes f11a0494
+ 00b54d40 bytes e81a0494
- 00b53d88 ["INT_ADD", "register:40f0:8", ["const:b53d88:8", "const:4:8"]]
- 00b53d88 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b54d7c ["INT_ADD", "register:40f0:8", ["const:b54d7c:8", "const:4:8"]]
+ 00b54d7c ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b53d88 bytes de1a0494
+ 00b54d7c bytes d51a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a75ee92ebd063b1414cb17335bd1f434"></a>

### [`00b53dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53dc8.md) → [`00b54dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54dbc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c660.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b53dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53dc8.md#insn-00b53dec) · [`00b53e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53dc8.md#insn-00b53e20) · [`00b53e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b53/00b53dc8.md#insn-00b53e40)
- 新版 [`00b54de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54dbc.md#insn-00b54de0) · [`00b54e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54dbc.md#insn-00b54e14) · [`00b54e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b54/00b54dbc.md#insn-00b54e34)

~~~diff
- 00b53dec ["INT_ADD", "register:40f0:8", ["const:b53dec:8", "const:4:8"]]
- 00b53dec ["CALL", null, ["callee:00c59080:8"]]
+ 00b54de0 ["INT_ADD", "register:40f0:8", ["const:b54de0:8", "const:4:8"]]
+ 00b54de0 ["CALL", null, ["callee:00c59080:8"]]
- 00b53dec bytes b1100494
+ 00b54de0 bytes a8100494
- 00b53e20 ["INT_ADD", "register:40f0:8", ["const:b53e20:8", "const:4:8"]]
- 00b53e20 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b54e14 ["INT_ADD", "register:40f0:8", ["const:b54e14:8", "const:4:8"]]
+ 00b54e14 ["CALL", null, ["callee:00c58f30:8"]]
- 00b53e20 bytes 50100494
+ 00b54e14 bytes 47100494
- 00b53e40 ["INT_ADD", "register:40f0:8", ["const:b53e40:8", "const:4:8"]]
- 00b53e40 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b54e34 ["INT_ADD", "register:40f0:8", ["const:b54e34:8", "const:4:8"]]
+ 00b54e34 ["CALL", null, ["callee:00c590a0:8"]]
- 00b53e40 bytes a4100494
+ 00b54e34 bytes 9b100494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4cfb9a54a328890569a89bdc6c5ee32"></a>

### [`00b54078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54078.md) → [`00b5506c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5506c.md) _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2d0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2a0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b540ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54078.md#insn-00b540ec) · [`00b54110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54078.md#insn-00b54110)
- 新版 [`00b550e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5506c.md#insn-00b550e0) · [`00b55104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5506c.md#insn-00b55104)

~~~diff
- 00b540ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b540ec ["INT_ADD", "register:40f0:8", ["const:b540ec:8", "const:4:8"]]
- 00b540ec ["CALLIND", null, ["register:0:8"]]
+ 00b550e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b550e0 ["INT_ADD", "register:40f0:8", ["const:b550e0:8", "const:4:8"]]
+ 00b550e0 ["CALLIND", null, ["register:0:8"]]
- 00b540ec bytes 00013fd6
+ 00b550e0 bytes 00013fd6
- 00b54110 ["INT_ADD", "register:40f0:8", ["const:b54110:8", "const:4:8"]]
- 00b54110 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b55104 ["INT_ADD", "register:40f0:8", ["const:b55104:8", "const:4:8"]]
+ 00b55104 ["CALL", null, ["callee:00c58f80:8"]]
- 00b54110 bytes a80f0494
+ 00b55104 bytes 9f0f0494
~~~


<a id="compare-9746c0716f13b896205aed9cd991367f"></a>

### [`00b5417c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b5417c.md) → [`00b55170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55170.md) _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2e0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2b0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b541f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b5417c.md#insn-00b541f0) · [`00b54214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b5417c.md#insn-00b54214)
- 新版 [`00b551e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55170.md#insn-00b551e4) · [`00b55208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55170.md#insn-00b55208)

~~~diff
- 00b541f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b541f0 ["INT_ADD", "register:40f0:8", ["const:b541f0:8", "const:4:8"]]
- 00b541f0 ["CALLIND", null, ["register:0:8"]]
+ 00b551e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b551e4 ["INT_ADD", "register:40f0:8", ["const:b551e4:8", "const:4:8"]]
+ 00b551e4 ["CALLIND", null, ["register:0:8"]]
- 00b541f0 bytes 00013fd6
+ 00b551e4 bytes 00013fd6
- 00b54214 ["INT_ADD", "register:40f0:8", ["const:b54214:8", "const:4:8"]]
- 00b54214 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b55208 ["INT_ADD", "register:40f0:8", ["const:b55208:8", "const:4:8"]]
+ 00b55208 ["CALL", null, ["callee:00c58f80:8"]]
- 00b54214 bytes 670f0494
+ 00b55208 bytes 5e0f0494
~~~


<a id="compare-81e2e8959b21e2d69df37214754fe71f"></a>

### [`00b54280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54280.md) → [`00b55274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55274.md) _ZN7_JNIEnv15CallShortMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2f0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2c0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b542f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54280.md#insn-00b542f4) · [`00b54318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54280.md#insn-00b54318)
- 新版 [`00b552e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55274.md#insn-00b552e8) · [`00b5530c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55274.md#insn-00b5530c)

~~~diff
- 00b542f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b542f4 ["INT_ADD", "register:40f0:8", ["const:b542f4:8", "const:4:8"]]
- 00b542f4 ["CALLIND", null, ["register:0:8"]]
+ 00b552e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b552e8 ["INT_ADD", "register:40f0:8", ["const:b552e8:8", "const:4:8"]]
+ 00b552e8 ["CALLIND", null, ["register:0:8"]]
- 00b542f4 bytes 00013fd6
+ 00b552e8 bytes 00013fd6
- 00b54318 ["INT_ADD", "register:40f0:8", ["const:b54318:8", "const:4:8"]]
- 00b54318 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5530c ["INT_ADD", "register:40f0:8", ["const:b5530c:8", "const:4:8"]]
+ 00b5530c ["CALL", null, ["callee:00c58f80:8"]]
- 00b54318 bytes 260f0494
+ 00b5530c bytes 1d0f0494
~~~


<a id="compare-cbce167b58b47f89402882e8073744a0"></a>

### [`00b544cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b544cc.md) → [`00b554c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b554c0.md) _ZN7_JNIEnv16CallDoubleMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b300.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2d0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b544cc.md#insn-00b54540) · [`00b54564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b544cc.md#insn-00b54564)
- 新版 [`00b55534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b554c0.md#insn-00b55534) · [`00b55558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b554c0.md#insn-00b55558)

~~~diff
- 00b54540 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54540 ["INT_ADD", "register:40f0:8", ["const:b54540:8", "const:4:8"]]
- 00b54540 ["CALLIND", null, ["register:0:8"]]
+ 00b55534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55534 ["INT_ADD", "register:40f0:8", ["const:b55534:8", "const:4:8"]]
+ 00b55534 ["CALLIND", null, ["register:0:8"]]
- 00b54540 bytes 00013fd6
+ 00b55534 bytes 00013fd6
- 00b54564 ["INT_ADD", "register:40f0:8", ["const:b54564:8", "const:4:8"]]
- 00b54564 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b55558 ["INT_ADD", "register:40f0:8", ["const:b55558:8", "const:4:8"]]
+ 00b55558 ["CALL", null, ["callee:00c58f80:8"]]
- 00b54564 bytes 930e0494
+ 00b55558 bytes 8a0e0494
~~~


<a id="compare-b116fa7145d1c588b673b602a9163328"></a>

### [`00b54928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54928.md) → [`00b5591c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5591c.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b580.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c550.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54928.md#insn-00b54968) · [`00b54984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54928.md#insn-00b54984) · [`00b54990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54928.md#insn-00b54990)
- 新版 [`00b5595c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5591c.md#insn-00b5595c) · [`00b55978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5591c.md#insn-00b55978) · [`00b55984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b5591c.md#insn-00b55984)

~~~diff
- 00b54968 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b54968 ["INT_ADD", "register:40f0:8", ["const:b54968:8", "const:4:8"]]
- 00b54968 ["CALLIND", null, ["register:0:8"]]
+ 00b5595c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b5595c ["INT_ADD", "register:40f0:8", ["const:b5595c:8", "const:4:8"]]
+ 00b5595c ["CALLIND", null, ["register:0:8"]]
- 00b54968 bytes 20013fd6
+ 00b5595c bytes 20013fd6
- 00b54984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54984 ["INT_ADD", "register:40f0:8", ["const:b54984:8", "const:4:8"]]
- 00b54984 ["CALLIND", null, ["register:0:8"]]
+ 00b55978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55978 ["INT_ADD", "register:40f0:8", ["const:b55978:8", "const:4:8"]]
+ 00b55978 ["CALLIND", null, ["register:0:8"]]
- 00b54984 bytes 00013fd6
+ 00b55978 bytes 00013fd6
- 00b54990 ["INT_ADD", "register:40f0:8", ["const:b54990:8", "const:4:8"]]
- 00b54990 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b55984 ["INT_ADD", "register:40f0:8", ["const:b55984:8", "const:4:8"]]
+ 00b55984 ["CALL", null, ["callee:00c58f30:8"]]
- 00b54990 bytes 740d0494
+ 00b55984 bytes 6b0d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9245ff676a30dd5f1a0695fa96d1f09b"></a>

### [`00b54aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54aac.md) → [`00b55aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55aa0.md) _ZN8firebase4util19JByteArrayToVariantEP7_JNIEnvP11_jbyteArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4a0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c470.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54aac.md#insn-00b54aec) · [`00b54b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54aac.md#insn-00b54b08) · [`00b54b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54aac.md#insn-00b54b14)
- 新版 [`00b55ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55aa0.md#insn-00b55ae0) · [`00b55afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55aa0.md#insn-00b55afc) · [`00b55b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55aa0.md#insn-00b55b08)

~~~diff
- 00b54aec ["COPY", "register:0:8", ["register:4048:8"]]
- 00b54aec ["INT_ADD", "register:40f0:8", ["const:b54aec:8", "const:4:8"]]
- 00b54aec ["CALLIND", null, ["register:0:8"]]
+ 00b55ae0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b55ae0 ["INT_ADD", "register:40f0:8", ["const:b55ae0:8", "const:4:8"]]
+ 00b55ae0 ["CALLIND", null, ["register:0:8"]]
- 00b54aec bytes 20013fd6
+ 00b55ae0 bytes 20013fd6
- 00b54b08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54b08 ["INT_ADD", "register:40f0:8", ["const:b54b08:8", "const:4:8"]]
- 00b54b08 ["CALLIND", null, ["register:0:8"]]
+ 00b55afc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55afc ["INT_ADD", "register:40f0:8", ["const:b55afc:8", "const:4:8"]]
+ 00b55afc ["CALLIND", null, ["register:0:8"]]
- 00b54b08 bytes 00013fd6
+ 00b55afc bytes 00013fd6
- 00b54b14 ["INT_ADD", "register:40f0:8", ["const:b54b14:8", "const:4:8"]]
- 00b54b14 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b55b08 ["INT_ADD", "register:40f0:8", ["const:b55b08:8", "const:4:8"]]
+ 00b55b08 ["CALL", null, ["callee:00c58f30:8"]]
- 00b54b14 bytes 130d0494
+ 00b55b08 bytes 0a0d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ccabbb5447f52b9bf6744f3dc59ff1"></a>

### [`00b54c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54c28.md) → [`00b55c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55c1c.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4b0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c480.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54c28.md#insn-00b54c68) · [`00b54c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54c28.md#insn-00b54c84) · [`00b54c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54c28.md#insn-00b54c90)
- 新版 [`00b55c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55c1c.md#insn-00b55c5c) · [`00b55c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55c1c.md#insn-00b55c78) · [`00b55c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55c1c.md#insn-00b55c84)

~~~diff
- 00b54c68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b54c68 ["INT_ADD", "register:40f0:8", ["const:b54c68:8", "const:4:8"]]
- 00b54c68 ["CALLIND", null, ["register:0:8"]]
+ 00b55c5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b55c5c ["INT_ADD", "register:40f0:8", ["const:b55c5c:8", "const:4:8"]]
+ 00b55c5c ["CALLIND", null, ["register:0:8"]]
- 00b54c68 bytes 20013fd6
+ 00b55c5c bytes 20013fd6
- 00b54c84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54c84 ["INT_ADD", "register:40f0:8", ["const:b54c84:8", "const:4:8"]]
- 00b54c84 ["CALLIND", null, ["register:0:8"]]
+ 00b55c78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55c78 ["INT_ADD", "register:40f0:8", ["const:b55c78:8", "const:4:8"]]
+ 00b55c78 ["CALLIND", null, ["register:0:8"]]
- 00b54c84 bytes 00013fd6
+ 00b55c78 bytes 00013fd6
- 00b54c90 ["INT_ADD", "register:40f0:8", ["const:b54c90:8", "const:4:8"]]
- 00b54c90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b55c84 ["INT_ADD", "register:40f0:8", ["const:b55c84:8", "const:4:8"]]
+ 00b55c84 ["CALL", null, ["callee:00c58f30:8"]]
- 00b54c90 bytes b40c0494
+ 00b55c84 bytes ab0c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b66c8e2df202ee4b6badf782be45b85"></a>

### [`00b54da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54da8.md) → [`00b55d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55d9c.md) _ZN8firebase4util20JShortArrayToVariantEP7_JNIEnvP12_jshortArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b530.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c500.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54da8.md#insn-00b54de8) · [`00b54e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54da8.md#insn-00b54e04) · [`00b54e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54da8.md#insn-00b54e10)
- 新版 [`00b55ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55d9c.md#insn-00b55ddc) · [`00b55df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55d9c.md#insn-00b55df8) · [`00b55e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55d9c.md#insn-00b55e04)

~~~diff
- 00b54de8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b54de8 ["INT_ADD", "register:40f0:8", ["const:b54de8:8", "const:4:8"]]
- 00b54de8 ["CALLIND", null, ["register:0:8"]]
+ 00b55ddc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b55ddc ["INT_ADD", "register:40f0:8", ["const:b55ddc:8", "const:4:8"]]
+ 00b55ddc ["CALLIND", null, ["register:0:8"]]
- 00b54de8 bytes 20013fd6
+ 00b55ddc bytes 20013fd6
- 00b54e04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54e04 ["INT_ADD", "register:40f0:8", ["const:b54e04:8", "const:4:8"]]
- 00b54e04 ["CALLIND", null, ["register:0:8"]]
+ 00b55df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55df8 ["INT_ADD", "register:40f0:8", ["const:b55df8:8", "const:4:8"]]
+ 00b55df8 ["CALLIND", null, ["register:0:8"]]
- 00b54e04 bytes 00013fd6
+ 00b55df8 bytes 00013fd6
- 00b54e10 ["INT_ADD", "register:40f0:8", ["const:b54e10:8", "const:4:8"]]
- 00b54e10 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b55e04 ["INT_ADD", "register:40f0:8", ["const:b55e04:8", "const:4:8"]]
+ 00b55e04 ["CALL", null, ["callee:00c58f30:8"]]
- 00b54e10 bytes 540c0494
+ 00b55e04 bytes 4b0c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cecb224ff077edc7fef109b7454e60"></a>

### [`00b54f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md) → [`00b55f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55f18.md) _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b480.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c450.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b54f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md#insn-00b54f64) · [`00b54f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md#insn-00b54f80) · [`00b54f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b54/00b54f24.md#insn-00b54f8c)
- 新版 [`00b55f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55f18.md#insn-00b55f58) · [`00b55f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55f18.md#insn-00b55f74) · [`00b55f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b55/00b55f18.md#insn-00b55f80)

~~~diff
- 00b54f64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b54f64 ["INT_ADD", "register:40f0:8", ["const:b54f64:8", "const:4:8"]]
- 00b54f64 ["CALLIND", null, ["register:0:8"]]
+ 00b55f58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b55f58 ["INT_ADD", "register:40f0:8", ["const:b55f58:8", "const:4:8"]]
+ 00b55f58 ["CALLIND", null, ["register:0:8"]]
- 00b54f64 bytes 20013fd6
+ 00b55f58 bytes 20013fd6
- 00b54f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54f80 ["INT_ADD", "register:40f0:8", ["const:b54f80:8", "const:4:8"]]
- 00b54f80 ["CALLIND", null, ["register:0:8"]]
+ 00b55f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55f74 ["INT_ADD", "register:40f0:8", ["const:b55f74:8", "const:4:8"]]
+ 00b55f74 ["CALLIND", null, ["register:0:8"]]
- 00b54f80 bytes 00013fd6
+ 00b55f74 bytes 00013fd6
- 00b54f8c ["INT_ADD", "register:40f0:8", ["const:b54f8c:8", "const:4:8"]]
- 00b54f8c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b55f80 ["INT_ADD", "register:40f0:8", ["const:b55f80:8", "const:4:8"]]
+ 00b55f80 ["CALL", null, ["callee:00c58f30:8"]]
- 00b54f8c bytes f50b0494
+ 00b55f80 bytes ec0b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaff01074b3c1045a32af57d95c42353"></a>

### [`00b550a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md) → [`00b56094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56094.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4c0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c490.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b550e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md#insn-00b550e0) · [`00b550fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md#insn-00b550fc) · [`00b55108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b550a0.md#insn-00b55108)
- 新版 [`00b560d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56094.md#insn-00b560d4) · [`00b560f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56094.md#insn-00b560f0) · [`00b560fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56094.md#insn-00b560fc)

~~~diff
- 00b550e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b550e0 ["INT_ADD", "register:40f0:8", ["const:b550e0:8", "const:4:8"]]
- 00b550e0 ["CALLIND", null, ["register:0:8"]]
+ 00b560d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b560d4 ["INT_ADD", "register:40f0:8", ["const:b560d4:8", "const:4:8"]]
+ 00b560d4 ["CALLIND", null, ["register:0:8"]]
- 00b550e0 bytes 20013fd6
+ 00b560d4 bytes 20013fd6
- 00b550fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b550fc ["INT_ADD", "register:40f0:8", ["const:b550fc:8", "const:4:8"]]
- 00b550fc ["CALLIND", null, ["register:0:8"]]
+ 00b560f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b560f0 ["INT_ADD", "register:40f0:8", ["const:b560f0:8", "const:4:8"]]
+ 00b560f0 ["CALLIND", null, ["register:0:8"]]
- 00b550fc bytes 00013fd6
+ 00b560f0 bytes 00013fd6
- 00b55108 ["INT_ADD", "register:40f0:8", ["const:b55108:8", "const:4:8"]]
- 00b55108 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b560fc ["INT_ADD", "register:40f0:8", ["const:b560fc:8", "const:4:8"]]
+ 00b560fc ["CALL", null, ["callee:00c58f30:8"]]
- 00b55108 bytes 960b0494
+ 00b560fc bytes 8d0b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a7044ac18ead26d001214abd6dc9dd"></a>

### [`00b5521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b5521c.md) → [`00b56210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56210.md) _ZN8firebase4util20JFloatArrayToVariantEP7_JNIEnvP12_jfloatArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b520.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c4f0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b5521c.md#insn-00b55260) · [`00b5527c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b5521c.md#insn-00b5527c) · [`00b55288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b5521c.md#insn-00b55288)
- 新版 [`00b56254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56210.md#insn-00b56254) · [`00b56270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56210.md#insn-00b56270) · [`00b5627c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56210.md#insn-00b5627c)

~~~diff
- 00b55260 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b55260 ["INT_ADD", "register:40f0:8", ["const:b55260:8", "const:4:8"]]
- 00b55260 ["CALLIND", null, ["register:0:8"]]
+ 00b56254 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b56254 ["INT_ADD", "register:40f0:8", ["const:b56254:8", "const:4:8"]]
+ 00b56254 ["CALLIND", null, ["register:0:8"]]
- 00b55260 bytes 20013fd6
+ 00b56254 bytes 20013fd6
- 00b5527c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5527c ["INT_ADD", "register:40f0:8", ["const:b5527c:8", "const:4:8"]]
- 00b5527c ["CALLIND", null, ["register:0:8"]]
+ 00b56270 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56270 ["INT_ADD", "register:40f0:8", ["const:b56270:8", "const:4:8"]]
+ 00b56270 ["CALLIND", null, ["register:0:8"]]
- 00b5527c bytes 00013fd6
+ 00b56270 bytes 00013fd6
- 00b55288 ["INT_ADD", "register:40f0:8", ["const:b55288:8", "const:4:8"]]
- 00b55288 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5627c ["INT_ADD", "register:40f0:8", ["const:b5627c:8", "const:4:8"]]
+ 00b5627c ["CALL", null, ["callee:00c58f30:8"]]
- 00b55288 bytes 360b0494
+ 00b5627c bytes 2d0b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9f90cdbe3bd7e3a34717531ba9af95"></a>

### [`00b553a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b553a4.md) → [`00b56398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56398.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b550.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c520.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b553e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b553a4.md#insn-00b553e4) · [`00b55400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b553a4.md#insn-00b55400) · [`00b5540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b553a4.md#insn-00b5540c)
- 新版 [`00b563d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56398.md#insn-00b563d8) · [`00b563f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56398.md#insn-00b563f4) · [`00b56400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56398.md#insn-00b56400)

~~~diff
- 00b553e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b553e4 ["INT_ADD", "register:40f0:8", ["const:b553e4:8", "const:4:8"]]
- 00b553e4 ["CALLIND", null, ["register:0:8"]]
+ 00b563d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b563d8 ["INT_ADD", "register:40f0:8", ["const:b563d8:8", "const:4:8"]]
+ 00b563d8 ["CALLIND", null, ["register:0:8"]]
- 00b553e4 bytes 20013fd6
+ 00b563d8 bytes 20013fd6
- 00b55400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55400 ["INT_ADD", "register:40f0:8", ["const:b55400:8", "const:4:8"]]
- 00b55400 ["CALLIND", null, ["register:0:8"]]
+ 00b563f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b563f4 ["INT_ADD", "register:40f0:8", ["const:b563f4:8", "const:4:8"]]
+ 00b563f4 ["CALLIND", null, ["register:0:8"]]
- 00b55400 bytes 00013fd6
+ 00b563f4 bytes 00013fd6
- 00b5540c ["INT_ADD", "register:40f0:8", ["const:b5540c:8", "const:4:8"]]
- 00b5540c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b56400 ["INT_ADD", "register:40f0:8", ["const:b56400:8", "const:4:8"]]
+ 00b56400 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5540c bytes d50a0494
+ 00b56400 bytes cc0a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121ae0a6c54b15b790715c8f59b392cf"></a>

### [`00b55520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md) → [`00b56514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56514.md) _ZN8firebase4util21JObjectArrayToVariantEP7_JNIEnvP13_jobjectArray

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b560.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b4e0.md)
- 新版 呼出元 1件 [`00c5c530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c530.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c4b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md#insn-00b55560) · [`00b55570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md#insn-00b55570) · [`00b55584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55520.md#insn-00b55584)
- 新版 [`00b56554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56514.md#insn-00b56554) · [`00b56564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56514.md#insn-00b56564) · [`00b56578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56514.md#insn-00b56578)

~~~diff
- 00b55560 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b55560 ["INT_ADD", "register:40f0:8", ["const:b55560:8", "const:4:8"]]
- 00b55560 ["CALLIND", null, ["register:0:8"]]
+ 00b56554 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b56554 ["INT_ADD", "register:40f0:8", ["const:b56554:8", "const:4:8"]]
+ 00b56554 ["CALLIND", null, ["register:0:8"]]
- 00b55560 bytes 20013fd6
+ 00b56554 bytes 20013fd6
- 00b55570 ["INT_ADD", "register:40f0:8", ["const:b55570:8", "const:4:8"]]
- 00b55570 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b56564 ["INT_ADD", "register:40f0:8", ["const:b56564:8", "const:4:8"]]
+ 00b56564 ["CALL", null, ["callee:00c58f30:8"]]
- 00b55570 bytes 7c0a0494
+ 00b56564 bytes 730a0494
- 00b55584 ["INT_ADD", "register:40f0:8", ["const:b55584:8", "const:4:8"]]
- 00b55584 ["CALL", null, ["callee:00c5c6d0:8"]]
+ 00b56578 ["INT_ADD", "register:40f0:8", ["const:b56578:8", "const:4:8"]]
+ 00b56578 ["CALL", null, ["callee:00c5c6d0:8"]]
- 00b55584 bytes 5f180494
+ 00b56578 bytes 56180494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7445ba7586c5f6ff6ee7a673f9ce7180"></a>

### [`00b55aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55aac.md) → [`00b56aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56aa0.md) _ZN8firebase4util25ByteBufferToJavaByteArrayEP7_JNIEnvPKhm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55aac.md#insn-00b55ad4) · [`00b55af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55aac.md#insn-00b55af8)
- 新版 [`00b56ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56aa0.md#insn-00b56ac8) · [`00b56aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56aa0.md#insn-00b56aec)

~~~diff
- 00b55ad4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ad4 ["INT_ADD", "register:40f0:8", ["const:b55ad4:8", "const:4:8"]]
- 00b55ad4 ["CALLIND", null, ["register:0:8"]]
+ 00b56ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56ac8 ["INT_ADD", "register:40f0:8", ["const:b56ac8:8", "const:4:8"]]
+ 00b56ac8 ["CALLIND", null, ["register:0:8"]]
- 00b55ad4 bytes 00013fd6
+ 00b56ac8 bytes 00013fd6
- 00b55af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55af8 ["INT_ADD", "register:40f0:8", ["const:b55af8:8", "const:4:8"]]
- 00b55af8 ["CALLIND", null, ["register:0:8"]]
+ 00b56aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56aec ["INT_ADD", "register:40f0:8", ["const:b56aec:8", "const:4:8"]]
+ 00b56aec ["CALLIND", null, ["register:0:8"]]
- 00b55af8 bytes 00013fd6
+ 00b56aec bytes 00013fd6
~~~


<a id="compare-e8786e9f4c075b01ac4a3b13ad41a138"></a>

### [`00b55e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md) → [`00b56e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56e28.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b540.md) · 呼出先 1件 [`00c5b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b730.md)
- 新版 呼出元 1件 [`00c5c510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c510.md) · 呼出先 1件 [`00c5c700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c700.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md#insn-00b55e60) · [`00b55e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md#insn-00b55e74) · [`00b55e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55e34.md#insn-00b55e94)
- 新版 [`00b56e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56e28.md#insn-00b56e54) · [`00b56e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56e28.md#insn-00b56e68) · [`00b56e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56e28.md#insn-00b56e88)

~~~diff
- 00b55e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55e60 ["INT_ADD", "register:40f0:8", ["const:b55e60:8", "const:4:8"]]
- 00b55e60 ["CALLIND", null, ["register:0:8"]]
+ 00b56e54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56e54 ["INT_ADD", "register:40f0:8", ["const:b56e54:8", "const:4:8"]]
+ 00b56e54 ["CALLIND", null, ["register:0:8"]]
- 00b55e60 bytes 00013fd6
+ 00b56e54 bytes 00013fd6
- 00b55e74 ["INT_ADD", "register:40f0:8", ["const:b55e74:8", "const:4:8"]]
- 00b55e74 ["CALL", null, ["callee:00c5c700:8"]]
+ 00b56e68 ["INT_ADD", "register:40f0:8", ["const:b56e68:8", "const:4:8"]]
+ 00b56e68 ["CALL", null, ["callee:00c5c700:8"]]
- 00b55e74 bytes 2f160494
+ 00b56e68 bytes 26160494
- 00b55e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55e94 ["INT_ADD", "register:40f0:8", ["const:b55e94:8", "const:4:8"]]
- 00b55e94 ["CALLIND", null, ["register:0:8"]]
+ 00b56e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56e88 ["INT_ADD", "register:40f0:8", ["const:b56e88:8", "const:4:8"]]
+ 00b56e88 ["CALLIND", null, ["register:0:8"]]
- 00b55e94 bytes 00013fd6
+ 00b56e88 bytes 00013fd6
~~~


<a id="compare-53a6c8c25edac743e65eb7d2a10d336d"></a>

### [`00b55eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55eb8.md) → [`00b56eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56eac.md) _ZN8firebase4util22LocalToGlobalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55eb8.md#insn-00b55edc) · [`00b55ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55eb8.md#insn-00b55ef4)
- 新版 [`00b56ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56eac.md#insn-00b56ed0) · [`00b56ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56eac.md#insn-00b56ee8)

~~~diff
- 00b55edc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55edc ["INT_ADD", "register:40f0:8", ["const:b55edc:8", "const:4:8"]]
- 00b55edc ["CALLIND", null, ["register:0:8"]]
+ 00b56ed0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56ed0 ["INT_ADD", "register:40f0:8", ["const:b56ed0:8", "const:4:8"]]
+ 00b56ed0 ["CALLIND", null, ["register:0:8"]]
- 00b55edc bytes 00013fd6
+ 00b56ed0 bytes 00013fd6
- 00b55ef4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ef4 ["INT_ADD", "register:40f0:8", ["const:b55ef4:8", "const:4:8"]]
- 00b55ef4 ["CALLIND", null, ["register:0:8"]]
+ 00b56ee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56ee8 ["INT_ADD", "register:40f0:8", ["const:b56ee8:8", "const:4:8"]]
+ 00b56ee8 ["CALLIND", null, ["register:0:8"]]
- 00b55ef4 bytes 00013fd6
+ 00b56ee8 bytes 00013fd6
~~~


<a id="compare-3668115c8b3554018716e766a43bb4f1"></a>

### [`00b55f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f14.md) → [`00b56f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56f08.md) _ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b55f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f14.md#insn-00b55f2c)
- 新版 [`00b56f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b56/00b56f08.md#insn-00b56f20)

~~~diff
- 00b55f2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55f2c ["INT_ADD", "register:40f0:8", ["const:b55f2c:8", "const:4:8"]]
- 00b55f2c ["CALLIND", null, ["register:0:8"]]
+ 00b56f20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56f20 ["INT_ADD", "register:40f0:8", ["const:b56f20:8", "const:4:8"]]
+ 00b56f20 ["CALLIND", null, ["register:0:8"]]
- 00b55f2c bytes 00013fd6
+ 00b56f20 bytes 00013fd6
~~~


<a id="compare-bfb21c49eac71cf75bd1e4b80aaf5af9"></a>

### [`00b57034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57034.md) → [`00b58028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58028.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b740.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c710.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b570a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57034.md#insn-00b570a4) · [`00b570c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57034.md#insn-00b570c4) · [`00b57114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57034.md#insn-00b57114)
- 新版 [`00b58098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58028.md#insn-00b58098) · [`00b580b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58028.md#insn-00b580b8) · [`00b58108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58028.md#insn-00b58108)

~~~diff
- 00b570a4 ["INT_ADD", "register:40f0:8", ["const:b570a4:8", "const:4:8"]]
- 00b570a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b58098 ["INT_ADD", "register:40f0:8", ["const:b58098:8", "const:4:8"]]
+ 00b58098 ["CALL", null, ["callee:00c58f30:8"]]
- 00b570a4 bytes af030494
+ 00b58098 bytes a6030494
- 00b570c4 ["INT_ADD", "register:40f0:8", ["const:b570c4:8", "const:4:8"]]
- 00b570c4 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b580b8 ["INT_ADD", "register:40f0:8", ["const:b580b8:8", "const:4:8"]]
+ 00b580b8 ["CALL", null, ["callee:00c590a0:8"]]
- 00b570c4 bytes 03040494
+ 00b580b8 bytes fa030494
- 00b57114 ["INT_ADD", "register:40f0:8", ["const:b57114:8", "const:4:8"]]
- 00b57114 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b58108 ["INT_ADD", "register:40f0:8", ["const:b58108:8", "const:4:8"]]
+ 00b58108 ["CALL", null, ["callee:00c5b980:8"]]
- 00b57114 bytes 270e0494
+ 00b58108 bytes 1e0e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21c814c73cefd75f8b3adbd3f60de58"></a>

### [`00b57460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57460.md) → [`00b58454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58454.md) _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b040.md) · 呼出先 1件 [`00c5b020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b020.md)
- 新版 呼出元 1件 [`00c5c010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c010.md) · 呼出先 1件 [`00c5bff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57460.md#insn-00b57480) · [`00b57498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57460.md#insn-00b57498) · [`00b574a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57460.md#insn-00b574a8)
- 新版 [`00b58474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58454.md#insn-00b58474) · [`00b5848c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58454.md#insn-00b5848c) · [`00b5849c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58454.md#insn-00b5849c)

~~~diff
- 00b57480 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b57480 ["INT_ADD", "register:40f0:8", ["const:b57480:8", "const:4:8"]]
- 00b57480 ["CALLIND", null, ["register:0:8"]]
+ 00b58474 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b58474 ["INT_ADD", "register:40f0:8", ["const:b58474:8", "const:4:8"]]
+ 00b58474 ["CALLIND", null, ["register:0:8"]]
- 00b57480 bytes 20013fd6
+ 00b58474 bytes 20013fd6
- 00b57498 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b57498 ["INT_ADD", "register:40f0:8", ["const:b57498:8", "const:4:8"]]
- 00b57498 ["CALLIND", null, ["register:0:8"]]
+ 00b5848c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5848c ["INT_ADD", "register:40f0:8", ["const:b5848c:8", "const:4:8"]]
+ 00b5848c ["CALLIND", null, ["register:0:8"]]
- 00b57498 bytes 00013fd6
+ 00b5848c bytes 00013fd6
- 00b574a8 ["INT_ADD", "register:40f0:8", ["const:b574a8:8", "const:4:8"]]
- 00b574a8 ["CALL", null, ["callee:00c5bff0:8"]]
+ 00b5849c ["INT_ADD", "register:40f0:8", ["const:b5849c:8", "const:4:8"]]
+ 00b5849c ["CALL", null, ["callee:00c5bff0:8"]]
- 00b574a8 bytes de0e0494
+ 00b5849c bytes d50e0494
~~~


<a id="compare-2df2d2a4297b08469ddee82ec0e17002"></a>

### [`00b5793c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md) → [`00b58930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58930.md) DetachJVMThreads

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b579b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b579b4.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b589a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b589a8.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md#insn-00b5796c) · [`00b5797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md#insn-00b5797c) · [`00b579a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md#insn-00b579a0)
- 新版 [`00b58960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58930.md#insn-00b58960) · [`00b58970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58930.md#insn-00b58970) · [`00b58994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58930.md#insn-00b58994)

~~~diff
- 00b5796c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5796c ["INT_ADD", "register:40f0:8", ["const:b5796c:8", "const:4:8"]]
- 00b5796c ["CALLIND", null, ["register:0:8"]]
+ 00b58960 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58960 ["INT_ADD", "register:40f0:8", ["const:b58960:8", "const:4:8"]]
+ 00b58960 ["CALLIND", null, ["register:0:8"]]
- 00b5796c bytes 00013fd6
+ 00b58960 bytes 00013fd6
- 00b5797c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5797c ["INT_ADD", "register:40f0:8", ["const:b5797c:8", "const:4:8"]]
- 00b5797c ["CALLIND", null, ["register:0:8"]]
+ 00b58970 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58970 ["INT_ADD", "register:40f0:8", ["const:b58970:8", "const:4:8"]]
+ 00b58970 ["CALLIND", null, ["register:0:8"]]
- 00b5797c bytes 00013fd6
+ 00b58970 bytes 00013fd6
- 00b579a0 ["INT_ADD", "register:40f0:8", ["const:b579a0:8", "const:4:8"]]
- 00b579a0 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b58994 ["INT_ADD", "register:40f0:8", ["const:b58994:8", "const:4:8"]]
+ 00b58994 ["CALL", null, ["callee:00c58f80:8"]]
- 00b579a0 bytes 84010494
+ 00b58994 bytes 7b010494
~~~


<a id="compare-c8272631ee9a014ec2c63f2b2a9a59f5"></a>

### [`00b57a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a58.md) → [`00b58a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a4c.md) _ZN8firebase4util16GetJNIEnvFromAppEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b410.md) · 呼出先 3件 [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b320.md) [`00c5b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 1件 [`00c5c3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c3e0.md) · 呼出先 3件 [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c2f0.md) [`00c5c300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a58.md#insn-00b57a60) · [`00b57a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a58.md#insn-00b57a68)
- 新版 [`00b58a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a4c.md#insn-00b58a54) · [`00b58a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a4c.md#insn-00b58a5c)

~~~diff
- 00b57a60 ["INT_ADD", "register:40f0:8", ["const:b57a60:8", "const:4:8"]]
- 00b57a60 ["CALL", null, ["callee:00c5c2f0:8"]]
+ 00b58a54 ["INT_ADD", "register:40f0:8", ["const:b58a54:8", "const:4:8"]]
+ 00b58a54 ["CALL", null, ["callee:00c5c2f0:8"]]
- 00b57a60 bytes 300e0494
+ 00b58a54 bytes 270e0494
- 00b57a68 ["INT_ADD", "register:40f0:8", ["const:b57a68:8", "const:4:8"]]
- 00b57a68 ["CALL", null, ["callee:00c5c300:8"]]
+ 00b58a5c ["INT_ADD", "register:40f0:8", ["const:b58a5c:8", "const:4:8"]]
+ 00b58a5c ["CALL", null, ["callee:00c5c300:8"]]
- 00b57a68 bytes 320e0494
+ 00b58a5c bytes 290e0494
~~~


<a id="compare-ecc1582879b88934367dbd4890dd52d5"></a>

### [`00b57a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a80.md) → [`00b58a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a74.md) _ZN8firebase7Variant18set_mutable_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b650.md) · 呼出先 3件 [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9d0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5c620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c620.md) · 呼出先 3件 [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9a0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a80.md#insn-00b57abc) · [`00b57ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a80.md#insn-00b57ae0) · [`00b57af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57a80.md#insn-00b57af0)
- 新版 [`00b58ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a74.md#insn-00b58ab0) · [`00b58ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a74.md#insn-00b58ad4) · [`00b58ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58a74.md#insn-00b58ae4)

~~~diff
- 00b57abc ["INT_ADD", "register:40f0:8", ["const:b57abc:8", "const:4:8"]]
- 00b57abc ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b58ab0 ["INT_ADD", "register:40f0:8", ["const:b58ab0:8", "const:4:8"]]
+ 00b58ab0 ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b57abc bytes 910b0494
+ 00b58ab0 bytes 880b0494
- 00b57ae0 ["INT_ADD", "register:40f0:8", ["const:b57ae0:8", "const:4:8"]]
- 00b57ae0 ["CALL", null, ["callee:00c5b9a0:8"]]
+ 00b58ad4 ["INT_ADD", "register:40f0:8", ["const:b58ad4:8", "const:4:8"]]
+ 00b58ad4 ["CALL", null, ["callee:00c5b9a0:8"]]
- 00b57ae0 bytes bc0b0494
+ 00b58ad4 bytes b30b0494
- 00b57af0 ["INT_ADD", "register:40f0:8", ["const:b57af0:8", "const:4:8"]]
- 00b57af0 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b58ae4 ["INT_ADD", "register:40f0:8", ["const:b58ae4:8", "const:4:8"]]
+ 00b58ae4 ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b57af0 bytes 840b0494
+ 00b58ae4 bytes 7b0b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9719e226df47a0334227ae8f7a0984d"></a>

### [`00b57b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57b28.md) → [`00b58b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58b1c.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6e0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6e0.md)
- 新版 呼出元 1件 [`00c5c6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6b0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57b28.md#insn-00b57b48) · [`00b57b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57b28.md#insn-00b57b54) · [`00b57b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57b28.md#insn-00b57b8c)
- 新版 [`00b58b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58b1c.md#insn-00b58b3c) · [`00b58b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58b1c.md#insn-00b58b48) · [`00b58b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58b1c.md#insn-00b58b80)

~~~diff
- 00b57b48 ["INT_ADD", "register:40f0:8", ["const:b57b48:8", "const:4:8"]]
- 00b57b48 ["CALL", null, ["callee:00c5c6b0:8"]]
+ 00b58b3c ["INT_ADD", "register:40f0:8", ["const:b58b3c:8", "const:4:8"]]
+ 00b58b3c ["CALL", null, ["callee:00c5c6b0:8"]]
- 00b57b48 bytes e60e0494
+ 00b58b3c bytes dd0e0494
- 00b57b54 ["INT_ADD", "register:40f0:8", ["const:b57b54:8", "const:4:8"]]
- 00b57b54 ["CALL", null, ["callee:00c5c6b0:8"]]
+ 00b58b48 ["INT_ADD", "register:40f0:8", ["const:b58b48:8", "const:4:8"]]
+ 00b58b48 ["CALL", null, ["callee:00c5c6b0:8"]]
- 00b57b54 bytes e30e0494
+ 00b58b48 bytes da0e0494
- 00b57b8c ["INT_ADD", "register:40f0:8", ["const:b57b8c:8", "const:4:8"]]
- 00b57b8c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b58b80 ["INT_ADD", "register:40f0:8", ["const:b58b80:8", "const:4:8"]]
+ 00b58b80 ["CALL", null, ["callee:00c58f50:8"]]
- 00b57b8c bytes fd000494
+ 00b58b80 bytes f4000494
~~~


<a id="compare-d289c001e9f66bc2894587b3a4a4f24a"></a>

### [`00b57d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md) → [`00b58d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58d48.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md#insn-00b57dc0) · [`00b57de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md#insn-00b57de0) · [`00b57df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md#insn-00b57df8)
- 新版 [`00b58db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58d48.md#insn-00b58db4) · [`00b58dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58d48.md#insn-00b58dd4) · [`00b58dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58d48.md#insn-00b58dec)

~~~diff
- 00b57dc0 ["INT_ADD", "register:40f0:8", ["const:b57dc0:8", "const:4:8"]]
- 00b57dc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b58db4 ["INT_ADD", "register:40f0:8", ["const:b58db4:8", "const:4:8"]]
+ 00b58db4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b57dc0 bytes 68000494
+ 00b58db4 bytes 5f000494
- 00b57de0 ["INT_ADD", "register:40f0:8", ["const:b57de0:8", "const:4:8"]]
- 00b57de0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b58dd4 ["INT_ADD", "register:40f0:8", ["const:b58dd4:8", "const:4:8"]]
+ 00b58dd4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b57de0 bytes bc000494
+ 00b58dd4 bytes b3000494
- 00b57df8 ["INT_ADD", "register:40f0:8", ["const:b57df8:8", "const:4:8"]]
- 00b57df8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b58dec ["INT_ADD", "register:40f0:8", ["const:b58dec:8", "const:4:8"]]
+ 00b58dec ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b57df8 bytes 060d0494
+ 00b58dec bytes fd0c0494
~~~


<a id="compare-19018873199b9c8db6cf8c4556192b1e"></a>

### [`00b57dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57dfc.md) → [`00b58df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58df0.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6c0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c690.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c640.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57dfc.md#insn-00b57e38) · [`00b57e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57dfc.md#insn-00b57e5c) · [`00b57e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57dfc.md#insn-00b57e9c)
- 新版 [`00b58e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58df0.md#insn-00b58e2c) · [`00b58e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58df0.md#insn-00b58e50) · [`00b58e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58df0.md#insn-00b58e90)

~~~diff
- 00b57e38 ["INT_ADD", "register:40f0:8", ["const:b57e38:8", "const:4:8"]]
- 00b57e38 ["CALL", null, ["callee:00c5c640:8"]]
+ 00b58e2c ["INT_ADD", "register:40f0:8", ["const:b58e2c:8", "const:4:8"]]
+ 00b58e2c ["CALL", null, ["callee:00c5c640:8"]]
- 00b57e38 bytes 0e0e0494
+ 00b58e2c bytes 050e0494
- 00b57e5c ["INT_ADD", "register:40f0:8", ["const:b57e5c:8", "const:4:8"]]
- 00b57e5c ["CALL", null, ["callee:00c5c640:8"]]
+ 00b58e50 ["INT_ADD", "register:40f0:8", ["const:b58e50:8", "const:4:8"]]
+ 00b58e50 ["CALL", null, ["callee:00c5c640:8"]]
- 00b57e5c bytes 050e0494
+ 00b58e50 bytes fc0d0494
- 00b57e9c ["INT_ADD", "register:40f0:8", ["const:b57e9c:8", "const:4:8"]]
- 00b57e9c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b58e90 ["INT_ADD", "register:40f0:8", ["const:b58e90:8", "const:4:8"]]
+ 00b58e90 ["CALL", null, ["callee:00c58f30:8"]]
- 00b57e9c bytes 31000494
+ 00b58e90 bytes 28000494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e877eab61435b5ff4f3a1b16103921"></a>

### [`00b57f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57f18.md) → [`00b58f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58f0c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b710.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5c6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6e0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b57f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57f18.md#insn-00b57f98) · [`00b57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57f18.md#insn-00b57fb0) · [`00b5802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57f18.md#insn-00b5802c)
- 新版 [`00b58f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58f0c.md#insn-00b58f8c) · [`00b58fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58f0c.md#insn-00b58fa4) · [`00b59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b58/00b58f0c.md#insn-00b59020)

~~~diff
- 00b57f98 ["INT_ADD", "register:40f0:8", ["const:b57f98:8", "const:4:8"]]
- 00b57f98 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b58f8c ["INT_ADD", "register:40f0:8", ["const:b58f8c:8", "const:4:8"]]
+ 00b58f8c ["CALL", null, ["callee:00c58f30:8"]]
- 00b57f98 bytes f2ff0394
+ 00b58f8c bytes e9ff0394
- 00b57fb0 ["INT_ADD", "register:40f0:8", ["const:b57fb0:8", "const:4:8"]]
- 00b57fb0 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b58fa4 ["INT_ADD", "register:40f0:8", ["const:b58fa4:8", "const:4:8"]]
+ 00b58fa4 ["CALL", null, ["callee:00c5c650:8"]]
- 00b57fb0 bytes b40d0494
+ 00b58fa4 bytes ab0d0494
- 00b5802c ["INT_ADD", "register:40f0:8", ["const:b5802c:8", "const:4:8"]]
- 00b5802c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b59020 ["INT_ADD", "register:40f0:8", ["const:b59020:8", "const:4:8"]]
+ 00b59020 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5802c bytes d5ff0394
+ 00b59020 bytes ccff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11805ceb7b5ba6a37faf7294902eda18"></a>

### [`00b58068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58068.md) → [`00b5905c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b5905c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b720.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6f0.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b580e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58068.md#insn-00b580e8) · [`00b5818c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58068.md#insn-00b5818c) · [`00b581c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58068.md#insn-00b581c4)
- 新版 [`00b590dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b5905c.md#insn-00b590dc) · [`00b59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b5905c.md#insn-00b59180) · [`00b591b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b5905c.md#insn-00b591b8)

~~~diff
- 00b580e8 ["INT_ADD", "register:40f0:8", ["const:b580e8:8", "const:4:8"]]
- 00b580e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b590dc ["INT_ADD", "register:40f0:8", ["const:b590dc:8", "const:4:8"]]
+ 00b590dc ["CALL", null, ["callee:00c58f30:8"]]
- 00b580e8 bytes 9eff0394
+ 00b590dc bytes 95ff0394
- 00b5818c ["INT_ADD", "register:40f0:8", ["const:b5818c:8", "const:4:8"]]
- 00b5818c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b59180 ["INT_ADD", "register:40f0:8", ["const:b59180:8", "const:4:8"]]
+ 00b59180 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5818c bytes 7dff0394
+ 00b59180 bytes 74ff0394
- 00b581c4 ["INT_ADD", "register:40f0:8", ["const:b581c4:8", "const:4:8"]]
- 00b581c4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b591b8 ["INT_ADD", "register:40f0:8", ["const:b591b8:8", "const:4:8"]]
+ 00b591b8 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b581c4 bytes 130c0494
+ 00b591b8 bytes 0a0c0494
~~~


<a id="compare-03cb6c87a0fdcfc6e1e0b88cf5646636"></a>

### [`00b581c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b581c8.md) → [`00b591bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b591bc.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6f0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6c0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b581c8.md#insn-00b58250) · [`00b58274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b581c8.md#insn-00b58274) · [`00b582a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b581c8.md#insn-00b582a0)
- 新版 [`00b59244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b591bc.md#insn-00b59244) · [`00b59268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b591bc.md#insn-00b59268) · [`00b59294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b591bc.md#insn-00b59294)

~~~diff
- 00b58250 ["INT_ADD", "register:40f0:8", ["const:b58250:8", "const:4:8"]]
- 00b58250 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b59244 ["INT_ADD", "register:40f0:8", ["const:b59244:8", "const:4:8"]]
+ 00b59244 ["CALL", null, ["callee:00c58f30:8"]]
- 00b58250 bytes 44ff0394
+ 00b59244 bytes 3bff0394
- 00b58274 ["INT_ADD", "register:40f0:8", ["const:b58274:8", "const:4:8"]]
- 00b58274 ["CALL", null, ["callee:00c5b8e0:8"]]
+ 00b59268 ["INT_ADD", "register:40f0:8", ["const:b59268:8", "const:4:8"]]
+ 00b59268 ["CALL", null, ["callee:00c5b8e0:8"]]
- 00b58274 bytes a7090494
+ 00b59268 bytes 9e090494
- 00b582a0 ["INT_ADD", "register:40f0:8", ["const:b582a0:8", "const:4:8"]]
- 00b582a0 ["CALL", null, ["callee:00c5b8e0:8"]]
+ 00b59294 ["INT_ADD", "register:40f0:8", ["const:b59294:8", "const:4:8"]]
+ 00b59294 ["CALL", null, ["callee:00c5b8e0:8"]]
- 00b582a0 bytes 9c090494
+ 00b59294 bytes 93090494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d19d6aa3909e304cffb4b07ac0ede25f"></a>

### [`00b5832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5832c.md) → [`00b59320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59320.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b730.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c700.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b583a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5832c.md#insn-00b583a8) · [`00b583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5832c.md#insn-00b583c0) · [`00b583dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5832c.md#insn-00b583dc)
- 新版 [`00b5939c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59320.md#insn-00b5939c) · [`00b593b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59320.md#insn-00b593b4) · [`00b593d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59320.md#insn-00b593d0)

~~~diff
- 00b583a8 ["INT_ADD", "register:40f0:8", ["const:b583a8:8", "const:4:8"]]
- 00b583a8 ["CALL", null, ["callee:00c59130:8"]]
+ 00b5939c ["INT_ADD", "register:40f0:8", ["const:b5939c:8", "const:4:8"]]
+ 00b5939c ["CALL", null, ["callee:00c59130:8"]]
- 00b583a8 bytes 6eff0394
+ 00b5939c bytes 65ff0394
- 00b583c0 ["INT_ADD", "register:40f0:8", ["const:b583c0:8", "const:4:8"]]
- 00b583c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b593b4 ["INT_ADD", "register:40f0:8", ["const:b593b4:8", "const:4:8"]]
+ 00b593b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b583c0 bytes e8fe0394
+ 00b593b4 bytes dffe0394
- 00b583dc ["INT_ADD", "register:40f0:8", ["const:b583dc:8", "const:4:8"]]
- 00b583dc ["CALL", null, ["callee:00c59130:8"]]
+ 00b593d0 ["INT_ADD", "register:40f0:8", ["const:b593d0:8", "const:4:8"]]
+ 00b593d0 ["CALL", null, ["callee:00c59130:8"]]
- 00b583dc bytes 61ff0394
+ 00b593d0 bytes 58ff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

