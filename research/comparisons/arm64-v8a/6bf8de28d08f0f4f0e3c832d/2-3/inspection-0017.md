# v16.0.2 → v16.0.3 · 要調査の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-7809d79dfa3230c1e4ebc18311a621c0"></a>

### [`006bf688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md) → [`006bfa38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfa38.md) FUN_006bfa38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)
- 新版 呼出元 6件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`00720498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bf6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md#insn-006bf6c8) · [`006bf6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md#insn-006bf6d8) · [`006bf6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md#insn-006bf6e4)
- 新版 [`006bfa78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfa38.md#insn-006bfa78) · [`006bfa88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfa38.md#insn-006bfa88) · [`006bfa94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfa38.md#insn-006bfa94)

~~~diff
- 006bf6c8 ["INT_ADD", "register:40f0:8", ["const:6bf6c8:8", "const:4:8"]]
- 006bf6c8 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 006bfa78 ["INT_ADD", "register:40f0:8", ["const:6bfa78:8", "const:4:8"]]
+ 006bfa78 ["CALL", null, ["callee:00c5b8d0:8"]]
- 006bf6c8 bytes 8e6c1694
+ 006bfa78 bytes 966f1694
- 006bf6d8 ["INT_ADD", "register:40f0:8", ["const:6bf6d8:8", "const:4:8"]]
- 006bf6d8 ["CALL", null, ["callee:00c5b8e0:8"]]
+ 006bfa88 ["INT_ADD", "register:40f0:8", ["const:6bfa88:8", "const:4:8"]]
+ 006bfa88 ["CALL", null, ["callee:00c5b8e0:8"]]
- 006bf6d8 bytes 8e6c1694
+ 006bfa88 bytes 966f1694
- 006bf6e4 ["INT_ADD", "register:40f0:8", ["const:6bf6e4:8", "const:4:8"]]
- 006bf6e4 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 006bfa94 ["INT_ADD", "register:40f0:8", ["const:6bfa94:8", "const:4:8"]]
+ 006bfa94 ["CALL", null, ["callee:00c5b8d0:8"]]
- 006bf6e4 bytes 876c1694
+ 006bfa94 bytes 8f6f1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13e6c15cf4f77b31389e39fc923f1397"></a>

### [`006bf738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf738.md) → [`006bfae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfae8.md) FUN_006bfae8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`00aa3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa3e94.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)
- 新版 呼出元 5件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`00720498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) [`00aa4e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa4/00aa4e88.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bf778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf738.md#insn-006bf778) · [`006bf78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf738.md#insn-006bf78c) · [`006bf798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf738.md#insn-006bf798)
- 新版 [`006bfb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfae8.md#insn-006bfb28) · [`006bfb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfae8.md#insn-006bfb3c) · [`006bfb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfae8.md#insn-006bfb48)

~~~diff
- 006bf778 ["INT_ADD", "register:40f0:8", ["const:6bf778:8", "const:4:8"]]
- 006bf778 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 006bfb28 ["INT_ADD", "register:40f0:8", ["const:6bfb28:8", "const:4:8"]]
+ 006bfb28 ["CALL", null, ["callee:00c5b8d0:8"]]
- 006bf778 bytes 626c1694
+ 006bfb28 bytes 6a6f1694
- 006bf78c ["INT_ADD", "register:40f0:8", ["const:6bf78c:8", "const:4:8"]]
- 006bf78c ["CALL", null, ["callee:00c5b8e0:8"]]
+ 006bfb3c ["INT_ADD", "register:40f0:8", ["const:6bfb3c:8", "const:4:8"]]
+ 006bfb3c ["CALL", null, ["callee:00c5b8e0:8"]]
- 006bf78c bytes 616c1694
+ 006bfb3c bytes 696f1694
- 006bf798 ["INT_ADD", "register:40f0:8", ["const:6bf798:8", "const:4:8"]]
- 006bf798 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 006bfb48 ["INT_ADD", "register:40f0:8", ["const:6bfb48:8", "const:4:8"]]
+ 006bfb48 ["CALL", null, ["callee:00c5b8d0:8"]]
- 006bf798 bytes 5a6c1694
+ 006bfb48 bytes 626f1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-565beffce9870e831f29280a74fce8b2"></a>

### [`006bf7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf7ec.md) → [`006bfb9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfb9c.md) FUN_006bfb9c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bf820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf7ec.md#insn-006bf820) · [`006bf828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf7ec.md#insn-006bf828)
- 新版 [`006bfbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfb9c.md#insn-006bfbd0) · [`006bfbd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfb9c.md#insn-006bfbd8)

~~~diff
- 006bf820 ["INT_ADD", "register:40f0:8", ["const:6bf820:8", "const:4:8"]]
- 006bf820 ["CALL", null, ["callee:005c1b8c:8"]]
+ 006bfbd0 ["INT_ADD", "register:40f0:8", ["const:6bfbd0:8", "const:4:8"]]
+ 006bfbd0 ["CALL", null, ["callee:005c1b8c:8"]]
- 006bf820 bytes ef07fc97
+ 006bfbd0 bytes ef07fc97
- 006bf828 ["INT_ADD", "register:40f0:8", ["const:6bf828:8", "const:4:8"]]
- 006bf828 ["CALL", null, ["callee:00c58f50:8"]]
+ 006bfbd8 ["INT_ADD", "register:40f0:8", ["const:6bfbd8:8", "const:4:8"]]
+ 006bfbd8 ["CALL", null, ["callee:00c58f50:8"]]
- 006bf828 bytes d6611694
+ 006bfbd8 bytes de641694
~~~


<a id="compare-acfc6c9261e75802eaae35f54095338c"></a>

### [`006bf844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf844.md) → [`006bfbf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfbf4.md) FUN_006bfbf4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bf870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf844.md#insn-006bf870)
- 新版 [`006bfc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfbf4.md#insn-006bfc20)

~~~diff
- 006bf870 ["INT_ADD", "register:40f0:8", ["const:6bf870:8", "const:4:8"]]
- 006bf870 ["CALL", null, ["callee:00c58f50:8"]]
+ 006bfc20 ["INT_ADD", "register:40f0:8", ["const:6bfc20:8", "const:4:8"]]
+ 006bfc20 ["CALL", null, ["callee:00c58f50:8"]]
- 006bf870 bytes c4611694
+ 006bfc20 bytes cc641694
~~~


<a id="compare-c415e8c4157945f19be0f8f2598e0981"></a>

### [`006bf88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf88c.md) → [`006bfc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc3c.md) FUN_006bfc3c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 2件 [`005fe2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe2d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 2件 [`005fe688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe688.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bf8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf88c.md#insn-006bf8c0) · [`006bf8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf88c.md#insn-006bf8c8)
- 新版 [`006bfc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc3c.md#insn-006bfc70) · [`006bfc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc3c.md#insn-006bfc78)

~~~diff
- 006bf8c0 ["INT_ADD", "register:40f0:8", ["const:6bf8c0:8", "const:4:8"]]
- 006bf8c0 ["CALL", null, ["callee:005fe688:8"]]
+ 006bfc70 ["INT_ADD", "register:40f0:8", ["const:6bfc70:8", "const:4:8"]]
+ 006bfc70 ["CALL", null, ["callee:005fe688:8"]]
- 006bf8c0 bytes 86fafc97
+ 006bfc70 bytes 86fafc97
- 006bf8c8 ["INT_ADD", "register:40f0:8", ["const:6bf8c8:8", "const:4:8"]]
- 006bf8c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 006bfc78 ["INT_ADD", "register:40f0:8", ["const:6bfc78:8", "const:4:8"]]
+ 006bfc78 ["CALL", null, ["callee:00c58f50:8"]]
- 006bf8c8 bytes ae611694
+ 006bfc78 bytes b6641694
~~~


<a id="compare-013cba67eb38e5d6e7433e4ad1ce5198"></a>

### [`006c0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md) → [`006c04b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md) FUN_006c04b0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006bea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bea44.md) [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 7件 [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md) [`006c0318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0318.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`006bedf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006be/006bedf4.md) [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) · 呼出先 7件 [`0048ae90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048ae90.md) [`0048ae98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048ae98.md) [`006c06c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c06c8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c0154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md#insn-006c0154) · [`006c0174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md#insn-006c0174) · [`006c017c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md#insn-006c017c)
- 新版 [`006c0504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md#insn-006c0504) · [`006c0524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md#insn-006c0524) · [`006c052c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md#insn-006c052c)

~~~diff
- 006c0154 ["INT_ADD", "register:40f0:8", ["const:6c0154:8", "const:4:8"]]
- 006c0154 ["CALL", null, ["callee:00c59590:8"]]
+ 006c0504 ["INT_ADD", "register:40f0:8", ["const:6c0504:8", "const:4:8"]]
+ 006c0504 ["CALL", null, ["callee:00c59590:8"]]
- 006c0154 bytes 1b611694
+ 006c0504 bytes 23641694
- 006c0174 ["INT_ADD", "register:40f0:8", ["const:6c0174:8", "const:4:8"]]
- 006c0174 ["CALL", null, ["callee:0048ae90:8"]]
+ 006c0524 ["INT_ADD", "register:40f0:8", ["const:6c0524:8", "const:4:8"]]
+ 006c0524 ["CALL", null, ["callee:0048ae90:8"]]
- 006c0174 bytes 7f2af797
+ 006c0524 bytes 5b2af797
- 006c017c ["INT_ADD", "register:40f0:8", ["const:6c017c:8", "const:4:8"]]
- 006c017c ["CALL", null, ["callee:0048ae98:8"]]
+ 006c052c ["INT_ADD", "register:40f0:8", ["const:6c052c:8", "const:4:8"]]
+ 006c052c ["CALL", null, ["callee:0048ae98:8"]]
- 006c017c bytes 7f2af797
+ 006c052c bytes 5b2af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e6f27483f977d442f0e6f63b477757"></a>

### [`006c0318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0318.md) → [`006c06c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c06c8.md) FUN_006c06c8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006c04b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md) · 呼出先 3件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c037c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0318.md#insn-006c037c) · [`006c0388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0318.md#insn-006c0388) · [`006c0398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0318.md#insn-006c0398)
- 新版 [`006c072c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c06c8.md#insn-006c072c) · [`006c0738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c06c8.md#insn-006c0738) · [`006c0748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c06c8.md#insn-006c0748)

~~~diff
- 006c037c ["INT_ADD", "register:40f0:8", ["const:6c037c:8", "const:4:8"]]
- 006c037c ["CALL", null, ["callee:00494970:8"]]
+ 006c072c ["INT_ADD", "register:40f0:8", ["const:6c072c:8", "const:4:8"]]
+ 006c072c ["CALL", null, ["callee:00494970:8"]]
- 006c037c bytes b550f797
+ 006c072c bytes 9150f797
- 006c0388 ["INT_ADD", "register:40f0:8", ["const:6c0388:8", "const:4:8"]]
- 006c0388 ["CALL", null, ["callee:00c58f20:8"]]
+ 006c0738 ["INT_ADD", "register:40f0:8", ["const:6c0738:8", "const:4:8"]]
+ 006c0738 ["CALL", null, ["callee:00c58f20:8"]]
- 006c0388 bytes f25e1694
+ 006c0738 bytes fa611694
- 006c0398 ["INT_ADD", "register:40f0:8", ["const:6c0398:8", "const:4:8"]]
- 006c0398 ["CALL", null, ["callee:00c58f50:8"]]
+ 006c0748 ["INT_ADD", "register:40f0:8", ["const:6c0748:8", "const:4:8"]]
+ 006c0748 ["CALL", null, ["callee:00c58f50:8"]]
- 006c0398 bytes fa5e1694
+ 006c0748 bytes 02621694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7046cb51a1036e93d4d9ee5b2cb5e328"></a>

### [`006c0ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0ef4.md) → [`006c12a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c12a4.md) FUN_006c12a4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00470120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470120.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`00470440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470440.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c0f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0ef4.md#insn-006c0f24) · [`006c0f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0ef4.md#insn-006c0f38)
- 新版 [`006c12d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c12a4.md#insn-006c12d4) · [`006c12e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c12a4.md#insn-006c12e8)

~~~diff
- 006c0f24 ["INT_ADD", "register:40f0:8", ["const:6c0f24:8", "const:4:8"]]
- 006c0f24 ["CALL", null, ["callee:00470440:8"]]
+ 006c12d4 ["INT_ADD", "register:40f0:8", ["const:6c12d4:8", "const:4:8"]]
+ 006c12d4 ["CALL", null, ["callee:00470440:8"]]
- 006c0f24 bytes 7fbcf697
+ 006c12d4 bytes 5bbcf697
- 006c0f38 ["INT_ADD", "register:40f0:8", ["const:6c0f38:8", "const:4:8"]]
- 006c0f38 ["CALL", null, ["callee:00470440:8"]]
+ 006c12e8 ["INT_ADD", "register:40f0:8", ["const:6c12e8:8", "const:4:8"]]
+ 006c12e8 ["CALL", null, ["callee:00470440:8"]]
- 006c0f38 bytes 7abcf697
+ 006c12e8 bytes 56bcf697
~~~


<a id="compare-8fcc81d23d6675ed1357c6d897e723a1"></a>

### [`006c1e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1e6c.md) → [`006c221c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c221c.md) FUN_006c221c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006c2070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c2/006c2070.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006c2420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2420.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c1f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1e6c.md#insn-006c1f14) · [`006c1f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1e6c.md#insn-006c1f4c)
- 新版 [`006c22c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c221c.md#insn-006c22c4) · [`006c22fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c221c.md#insn-006c22fc)

~~~diff
- 006c1f14 ["INT_ADD", "register:40f0:8", ["const:6c1f14:8", "const:4:8"]]
- 006c1f14 ["CALL", null, ["callee:00c58f30:8"]]
+ 006c22c4 ["INT_ADD", "register:40f0:8", ["const:6c22c4:8", "const:4:8"]]
+ 006c22c4 ["CALL", null, ["callee:00c58f30:8"]]
- 006c1f14 bytes 13581694
+ 006c22c4 bytes 1b5b1694
- 006c1f4c ["INT_ADD", "register:40f0:8", ["const:6c1f4c:8", "const:4:8"]]
- 006c1f4c ["CALL", null, ["callee:0043bf04:8"]]
+ 006c22fc ["INT_ADD", "register:40f0:8", ["const:6c22fc:8", "const:4:8"]]
+ 006c22fc ["CALL", null, ["callee:0043bf04:8"]]
- 006c1f4c bytes 26e7f597
+ 006c22fc bytes 02e7f597
~~~


<a id="compare-957bb436b243ccb0c11970921738a36d"></a>

### [`006c3114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3114.md) → [`006c34c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34c4.md) FUN_006c34c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c3138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3114.md#insn-006c3138)
- 新版 [`006c34e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34c4.md#insn-006c34e8)

~~~diff
- 006c3138 ["INT_ADD", "register:40f0:8", ["const:6c3138:8", "const:4:8"]]
- 006c3138 ["CALL", null, ["callee:006c3680:8"]]
+ 006c34e8 ["INT_ADD", "register:40f0:8", ["const:6c34e8:8", "const:4:8"]]
+ 006c34e8 ["CALL", null, ["callee:006c3680:8"]]
- 006c3138 bytes 66000094
+ 006c34e8 bytes 66000094
~~~


<a id="compare-33bcde014c6e5f1517b4b7592d9fb0c7"></a>

### [`006c3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3148.md) → [`006c34f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34f8.md) FUN_006c34f8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`006e93fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e93fc.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 2件 [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) [`006e97ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e97ac.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c3160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3148.md#insn-006c3160)
- 新版 [`006c3510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34f8.md#insn-006c3510)

~~~diff
- 006c3160 ["INT_ADD", "register:40f0:8", ["const:6c3160:8", "const:4:8"]]
- 006c3160 ["CALL", null, ["callee:006c3680:8"]]
+ 006c3510 ["INT_ADD", "register:40f0:8", ["const:6c3510:8", "const:4:8"]]
+ 006c3510 ["CALL", null, ["callee:006c3680:8"]]
- 006c3160 bytes 5c000094
+ 006c3510 bytes 5c000094
~~~


<a id="compare-7f42befb44492e218d054a6d4bf78ebe"></a>

### [`006c320c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c320c.md) → [`006c35bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c35bc.md) FUN_006c35bc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c323c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c320c.md#insn-006c323c)
- 新版 [`006c35ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c35bc.md#insn-006c35ec)

~~~diff
- 006c323c ["INT_ADD", "register:40f0:8", ["const:6c323c:8", "const:4:8"]]
- 006c323c ["CALL", null, ["callee:006c3680:8"]]
+ 006c35ec ["INT_ADD", "register:40f0:8", ["const:6c35ec:8", "const:4:8"]]
+ 006c35ec ["CALL", null, ["callee:006c3680:8"]]
- 006c323c bytes 25000094
+ 006c35ec bytes 25000094
~~~


<a id="compare-5d256ca91050394dc64f285b981423d4"></a>

### [`006c3258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3258.md) → [`006c3608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3608.md) FUN_006c3608

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`008f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39fc.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 3件 [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`008f49a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f49a8.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c3274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3258.md#insn-006c3274)
- 新版 [`006c3624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3608.md#insn-006c3624)

~~~diff
- 006c3274 ["INT_ADD", "register:40f0:8", ["const:6c3274:8", "const:4:8"]]
- 006c3274 ["CALL", null, ["callee:006c3680:8"]]
+ 006c3624 ["INT_ADD", "register:40f0:8", ["const:6c3624:8", "const:4:8"]]
+ 006c3624 ["CALL", null, ["callee:006c3680:8"]]
- 006c3274 bytes 17000094
+ 006c3624 bytes 17000094
~~~


<a id="compare-b78f2921ee0ebab1dd9d59ae0e80cebd"></a>

### [`006c3284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3284.md) → [`006c3634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3634.md) FUN_006c3634

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 1件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c329c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3284.md#insn-006c329c)
- 新版 [`006c364c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3634.md#insn-006c364c)

~~~diff
- 006c329c ["INT_ADD", "register:40f0:8", ["const:6c329c:8", "const:4:8"]]
- 006c329c ["CALL", null, ["callee:006c3680:8"]]
+ 006c364c ["INT_ADD", "register:40f0:8", ["const:6c364c:8", "const:4:8"]]
+ 006c364c ["CALL", null, ["callee:006c3680:8"]]
- 006c329c bytes 0d000094
+ 006c364c bytes 0d000094
~~~


<a id="compare-16def10e86936cb4e9fb550abb818270"></a>

### [`006c32ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32ac.md) → [`006c365c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c365c.md) FUN_006c365c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) [`006e93fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e93fc.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 1件 [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md)
- 新版 呼出元 6件 [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) [`006e97ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e97ac.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 1件 [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c32c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32ac.md#insn-006c32c0)
- 新版 [`006c3670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c365c.md#insn-006c3670)

~~~diff
- 006c32c0 ["INT_ADD", "register:40f0:8", ["const:6c32c0:8", "const:4:8"]]
- 006c32c0 ["CALL", null, ["callee:006c3680:8"]]
+ 006c3670 ["INT_ADD", "register:40f0:8", ["const:6c3670:8", "const:4:8"]]
+ 006c3670 ["CALL", null, ["callee:006c3680:8"]]
- 006c32c0 bytes 04000094
+ 006c3670 bytes 04000094
~~~


<a id="compare-151c86edcd0931af8f8838e750ae4d99"></a>

### [`006c3cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md) → [`006c408c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c408c.md) FUN_006c408c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 2件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 2件 [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c3d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md#insn-006c3d18) · [`006c3d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md#insn-006c3d44) · [`006c3d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3cdc.md#insn-006c3d54)
- 新版 [`006c40c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c408c.md#insn-006c40c8) · [`006c40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c408c.md#insn-006c40f4) · [`006c4104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c408c.md#insn-006c4104)

~~~diff
- 006c3d18 ["COPY", "register:0:8", ["register:4048:8"]]
- 006c3d18 ["INT_ADD", "register:40f0:8", ["const:6c3d18:8", "const:4:8"]]
- 006c3d18 ["CALLIND", null, ["register:0:8"]]
+ 006c40c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 006c40c8 ["INT_ADD", "register:40f0:8", ["const:6c40c8:8", "const:4:8"]]
+ 006c40c8 ["CALLIND", null, ["register:0:8"]]
- 006c3d18 bytes 20013fd6
+ 006c40c8 bytes 20013fd6
- 006c3d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 006c3d44 ["INT_ADD", "register:40f0:8", ["const:6c3d44:8", "const:4:8"]]
- 006c3d44 ["CALLIND", null, ["register:0:8"]]
+ 006c40f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006c40f4 ["INT_ADD", "register:40f0:8", ["const:6c40f4:8", "const:4:8"]]
+ 006c40f4 ["CALLIND", null, ["register:0:8"]]
- 006c3d44 bytes 00013fd6
+ 006c40f4 bytes 00013fd6
- 006c3d54 ["INT_ADD", "register:40f0:8", ["const:6c3d54:8", "const:4:8"]]
- 006c3d54 ["CALL", null, ["callee:0057c208:8"]]
+ 006c4104 ["INT_ADD", "register:40f0:8", ["const:6c4104:8", "const:4:8"]]
+ 006c4104 ["CALL", null, ["callee:0057c208:8"]]
- 006c3d54 bytes 65e0fa97
+ 006c4104 bytes 41e0fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70e9ebd9914f2bd761de907b36745d0c"></a>

### [`006c4218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md) → [`006c45c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md) FUN_006c45c8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0064a9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a9d0.md) [`006c4290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4290.md) [`006e8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 3件 [`0064ad80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064ad80.md) [`006c4640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4640.md) [`006e8f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8f5c.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c425c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md#insn-006c425c) · [`006c4270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md#insn-006c4270) · [`006c4278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md#insn-006c4278)
- 新版 [`006c460c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md#insn-006c460c) · [`006c4620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md#insn-006c4620) · [`006c4628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md#insn-006c4628)

~~~diff
- 006c425c ["INT_ADD", "register:40f0:8", ["const:6c425c:8", "const:4:8"]]
- 006c425c ["CALL", null, ["callee:00c54d90:8"]]
+ 006c460c ["INT_ADD", "register:40f0:8", ["const:6c460c:8", "const:4:8"]]
+ 006c460c ["CALL", null, ["callee:00c54d90:8"]]
- 006c425c bytes d13e1694
+ 006c460c bytes e1411694
- 006c4270 ["COPY", "register:0:8", ["register:4040:8"]]
- 006c4270 ["INT_ADD", "register:40f0:8", ["const:6c4270:8", "const:4:8"]]
- 006c4270 ["CALLIND", null, ["register:0:8"]]
+ 006c4620 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006c4620 ["INT_ADD", "register:40f0:8", ["const:6c4620:8", "const:4:8"]]
+ 006c4620 ["CALLIND", null, ["register:0:8"]]
- 006c4270 bytes 00013fd6
+ 006c4620 bytes 00013fd6
- 006c4278 ["INT_ADD", "register:40f0:8", ["const:6c4278:8", "const:4:8"]]
- 006c4278 ["CALL", null, ["callee:00c58f20:8"]]
+ 006c4628 ["INT_ADD", "register:40f0:8", ["const:6c4628:8", "const:4:8"]]
+ 006c4628 ["CALL", null, ["callee:00c58f20:8"]]
- 006c4278 bytes 364f1694
+ 006c4628 bytes 3e521694
~~~


<a id="compare-e4b3382203f21e4ca21df6330639fbe6"></a>

### [`006c4ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4ec4.md) → [`006c5274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5274.md) FUN_006c5274

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`006d1510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1510.md) [`006d18a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d18a0.md) [`006d3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d3/006d3e94.md) [`006d8440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md) [`006d87c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d87c0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 13件 [`006d18c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d18c0.md) [`006d1c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1c50.md) [`006d4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d4/006d4244.md) [`006d87f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md) [`006d8b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b70.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c4f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4ec4.md#insn-006c4f2c) · [`006c4f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4ec4.md#insn-006c4f98)
- 新版 [`006c52dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5274.md#insn-006c52dc) · [`006c5348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5274.md#insn-006c5348)

~~~diff
- 006c4f2c ["INT_ADD", "register:40f0:8", ["const:6c4f2c:8", "const:4:8"]]
- 006c4f2c ["CALL", null, ["callee:0043bf04:8"]]
+ 006c52dc ["INT_ADD", "register:40f0:8", ["const:6c52dc:8", "const:4:8"]]
+ 006c52dc ["CALL", null, ["callee:0043bf04:8"]]
- 006c4f2c bytes 2edbf597
+ 006c52dc bytes 0adbf597
- 006c4f98 ["INT_ADD", "register:40f0:8", ["const:6c4f98:8", "const:4:8"]]
- 006c4f98 ["CALL", null, ["callee:00c58f30:8"]]
+ 006c5348 ["INT_ADD", "register:40f0:8", ["const:6c5348:8", "const:4:8"]]
+ 006c5348 ["CALL", null, ["callee:00c58f30:8"]]
- 006c4f98 bytes f24b1694
+ 006c5348 bytes fa4e1694
~~~


<a id="compare-953275258115ae4421cf2eaed08ebf6f"></a>

### [`006c64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md) → [`006c688c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c688c.md) FUN_006c688c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006cdce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cd/006cdce0.md) [`008f0a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md) [`009f8d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8d00.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006d5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md)
- 新版 呼出元 3件 [`006ce090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ce/006ce090.md) [`008f19d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f1/008f19d4.md) [`009f9cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f9/009f9cac.md) · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`006d62ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b05d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b05/00b05d0c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006c6528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md#insn-006c6528) · [`006c6538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md#insn-006c6538) · [`006c6548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md#insn-006c6548)
- 新版 [`006c68d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c688c.md#insn-006c68d8) · [`006c68e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c688c.md#insn-006c68e8) · [`006c68f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c688c.md#insn-006c68f8)

~~~diff
- 006c6528 ["INT_ADD", "register:40f0:8", ["const:6c6528:8", "const:4:8"]]
- 006c6528 ["CALL", null, ["callee:00676e50:8"]]
+ 006c68d8 ["INT_ADD", "register:40f0:8", ["const:6c68d8:8", "const:4:8"]]
+ 006c68d8 ["CALL", null, ["callee:00676e50:8"]]
- 006c6528 bytes 5ec1fe97
+ 006c68d8 bytes 5ec1fe97
- 006c6538 ["INT_ADD", "register:40f0:8", ["const:6c6538:8", "const:4:8"]]
- 006c6538 ["CALL", null, ["callee:008524fc:8"]]
+ 006c68e8 ["INT_ADD", "register:40f0:8", ["const:6c68e8:8", "const:4:8"]]
+ 006c68e8 ["CALL", null, ["callee:008524fc:8"]]
- 006c6538 bytes 062c0694
+ 006c68e8 bytes 052f0694
- 006c6548 ["INT_ADD", "register:40f0:8", ["const:6c6548:8", "const:4:8"]]
- 006c6548 ["CALL", null, ["callee:008524fc:8"]]
+ 006c68f8 ["INT_ADD", "register:40f0:8", ["const:6c68f8:8", "const:4:8"]]
+ 006c68f8 ["CALL", null, ["callee:008524fc:8"]]
- 006c6548 bytes 022c0694
+ 006c68f8 bytes 012f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8509607f1bd94fde8de5681421aeb4"></a>

### [`006cb10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb10c.md) → [`006cb4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb4bc.md) FUN_006cb4bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`006c63ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c63ec.md) [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`006cbacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cbacc.md) [`006ccbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cc/006ccbd0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006d61c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d61c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`006c5700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5700.md) [`006c679c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c679c.md) [`006c7218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md) [`006cbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbe7c.md) [`006ccf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cc/006ccf80.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006d6578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6578.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006cb158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb10c.md#insn-006cb158) · [`006cb188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb10c.md#insn-006cb188) · [`006cb19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb10c.md#insn-006cb19c)
- 新版 [`006cb508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb4bc.md#insn-006cb508) · [`006cb538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb4bc.md#insn-006cb538) · [`006cb54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb4bc.md#insn-006cb54c)

~~~diff
- 006cb158 ["INT_ADD", "register:40f0:8", ["const:6cb158:8", "const:4:8"]]
- 006cb158 ["CALL", null, ["callee:0043bf04:8"]]
+ 006cb508 ["INT_ADD", "register:40f0:8", ["const:6cb508:8", "const:4:8"]]
+ 006cb508 ["CALL", null, ["callee:0043bf04:8"]]
- 006cb158 bytes a3c2f597
+ 006cb508 bytes 7fc2f597
- 006cb188 ["INT_ADD", "register:40f0:8", ["const:6cb188:8", "const:4:8"]]
- 006cb188 ["CALL", null, ["callee:006d6578:8"]]
+ 006cb538 ["INT_ADD", "register:40f0:8", ["const:6cb538:8", "const:4:8"]]
+ 006cb538 ["CALL", null, ["callee:006d6578:8"]]
- 006cb188 bytes 102c0094
+ 006cb538 bytes 102c0094
- 006cb19c ["INT_ADD", "register:40f0:8", ["const:6cb19c:8", "const:4:8"]]
- 006cb19c ["CALL", null, ["callee:00c58f30:8"]]
+ 006cb54c ["INT_ADD", "register:40f0:8", ["const:6cb54c:8", "const:4:8"]]
+ 006cb54c ["CALL", null, ["callee:00c58f30:8"]]
- 006cb19c bytes 71331694
+ 006cb54c bytes 79361694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49e79fbad8e29cf1462946f725dc2708"></a>

### [`006cb228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md) → [`006cb5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb5d8.md) FUN_006cb5d8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006cdce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cd/006cdce0.md) [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) [`008f0a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md) [`00adf288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md) · 呼出先 2件 [`00b039ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b039ac.md) [`00b069f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b069f8.md)
- 新版 呼出元 4件 [`006ce090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ce/006ce090.md) [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) [`008f19d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f1/008f19d4.md) [`00ae027c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae0/00ae027c.md) · 呼出先 2件 [`00b049a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b04/00b049a0.md) [`00b079ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b07/00b079ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006cb260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md#insn-006cb260) · [`006cb290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md#insn-006cb290) · [`006cb2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md#insn-006cb2b4)
- 新版 [`006cb610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb5d8.md#insn-006cb610) · [`006cb640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb5d8.md#insn-006cb640) · [`006cb664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb5d8.md#insn-006cb664)

~~~diff
- 006cb260 ["INT_ADD", "register:40f0:8", ["const:6cb260:8", "const:4:8"]]
- 006cb260 ["CALL", null, ["callee:00b079ec:8"]]
+ 006cb610 ["INT_ADD", "register:40f0:8", ["const:6cb610:8", "const:4:8"]]
+ 006cb610 ["CALL", null, ["callee:00b079ec:8"]]
- 006cb260 bytes e6ed1094
+ 006cb610 bytes f7f01094
- 006cb290 ["INT_ADD", "register:40f0:8", ["const:6cb290:8", "const:4:8"]]
- 006cb290 ["CALL", null, ["callee:00b049a0:8"]]
+ 006cb640 ["INT_ADD", "register:40f0:8", ["const:6cb640:8", "const:4:8"]]
+ 006cb640 ["CALL", null, ["callee:00b049a0:8"]]
- 006cb290 bytes c7e11094
+ 006cb640 bytes d8e41094
- 006cb2b4 ["INT_ADD", "register:40f0:8", ["const:6cb2b4:8", "const:4:8"]]
- 006cb2b4 ["CALL", null, ["callee:00b079ec:8"]]
+ 006cb664 ["INT_ADD", "register:40f0:8", ["const:6cb664:8", "const:4:8"]]
+ 006cb664 ["CALL", null, ["callee:00b079ec:8"]]
- 006cb2b4 bytes d1ed1094
+ 006cb664 bytes e2f01094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbad342a7acfbb302ca68f56bb24ed93"></a>

### [`006d02a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02a4.md) → [`006d0654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0654.md) FUN_006d0654

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d02c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02a4.md#insn-006d02c4) · [`006d02d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02a4.md#insn-006d02d4)
- 新版 [`006d0674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0654.md#insn-006d0674) · [`006d0684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0654.md#insn-006d0684)

~~~diff
- 006d02c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 006d02c4 ["INT_ADD", "register:40f0:8", ["const:6d02c4:8", "const:4:8"]]
- 006d02c4 ["CALLIND", null, ["register:0:8"]]
+ 006d0674 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006d0674 ["INT_ADD", "register:40f0:8", ["const:6d0674:8", "const:4:8"]]
+ 006d0674 ["CALLIND", null, ["register:0:8"]]
- 006d02c4 bytes 00013fd6
+ 006d0674 bytes 00013fd6
- 006d02d4 ["INT_ADD", "register:40f0:8", ["const:6d02d4:8", "const:4:8"]]
- 006d02d4 ["CALL", null, ["callee:00c58f50:8"]]
+ 006d0684 ["INT_ADD", "register:40f0:8", ["const:6d0684:8", "const:4:8"]]
+ 006d0684 ["CALL", null, ["callee:00c58f50:8"]]
- 006d02d4 bytes 2b1f1694
+ 006d0684 bytes 33221694
~~~


<a id="compare-1419566c94ea9132165ef0de2fcdf6fd"></a>

### [`006d12b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md) → [`006d1660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md) FUN_006d1660

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006d3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d3/006d3e94.md) [`006d8440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md) · 呼出先 3件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006d5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`006d4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d4/006d4244.md) [`006d87f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md) · 呼出先 3件 [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`006d62ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d12f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md#insn-006d12f0) · [`006d131c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md#insn-006d131c) · [`006d1348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md#insn-006d1348)
- 新版 [`006d16a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md#insn-006d16a0) · [`006d16cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md#insn-006d16cc) · [`006d16f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md#insn-006d16f8)

~~~diff
- 006d12f0 ["INT_ADD", "register:40f0:8", ["const:6d12f0:8", "const:4:8"]]
- 006d12f0 ["CALL", null, ["callee:006d62ac:8"]]
+ 006d16a0 ["INT_ADD", "register:40f0:8", ["const:6d16a0:8", "const:4:8"]]
+ 006d16a0 ["CALL", null, ["callee:006d62ac:8"]]
- 006d12f0 bytes 03130094
+ 006d16a0 bytes 03130094
- 006d131c ["INT_ADD", "register:40f0:8", ["const:6d131c:8", "const:4:8"]]
- 006d131c ["CALL", null, ["callee:006d62ac:8"]]
+ 006d16cc ["INT_ADD", "register:40f0:8", ["const:6d16cc:8", "const:4:8"]]
+ 006d16cc ["CALL", null, ["callee:006d62ac:8"]]
- 006d131c bytes f8120094
+ 006d16cc bytes f8120094
- 006d1348 ["INT_ADD", "register:40f0:8", ["const:6d1348:8", "const:4:8"]]
- 006d1348 ["CALL", null, ["callee:006d62ac:8"]]
+ 006d16f8 ["INT_ADD", "register:40f0:8", ["const:6d16f8:8", "const:4:8"]]
+ 006d16f8 ["CALL", null, ["callee:006d62ac:8"]]
- 006d1348 bytes ed120094
+ 006d16f8 bytes ed120094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4321c8229b2807c3557cc8c6ea61b9dd"></a>

### [`006d1fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1fc4.md) → [`006d2374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d2374.md) FUN_006d2374

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00986418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986418.md) · 呼出先 3件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d1fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1fc4.md#insn-006d1fe8) · [`006d2000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1fc4.md#insn-006d2000) · [`006d2024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1fc4.md#insn-006d2024)
- 新版 [`006d2398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d2374.md#insn-006d2398) · [`006d23b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d2374.md#insn-006d23b0) · [`006d23d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d2374.md#insn-006d23d4)

~~~diff
- 006d1fe8 ["INT_ADD", "register:40f0:8", ["const:6d1fe8:8", "const:4:8"]]
- 006d1fe8 ["CALL", null, ["callee:00c54d60:8"]]
+ 006d2398 ["INT_ADD", "register:40f0:8", ["const:6d2398:8", "const:4:8"]]
+ 006d2398 ["CALL", null, ["callee:00c54d60:8"]]
- 006d1fe8 bytes 62071694
+ 006d2398 bytes 720a1694
- 006d2000 ["INT_ADD", "register:40f0:8", ["const:6d2000:8", "const:4:8"]]
- 006d2000 ["CALL", null, ["callee:00c54d90:8"]]
+ 006d23b0 ["INT_ADD", "register:40f0:8", ["const:6d23b0:8", "const:4:8"]]
+ 006d23b0 ["CALL", null, ["callee:00c54d90:8"]]
- 006d2000 bytes 68071694
+ 006d23b0 bytes 780a1694
- 006d2024 ["COPY", "register:0:8", ["register:4040:8"]]
- 006d2024 ["INT_ADD", "register:40f0:8", ["const:6d2024:8", "const:4:8"]]
- 006d2024 ["CALLIND", null, ["register:0:8"]]
+ 006d23d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006d23d4 ["INT_ADD", "register:40f0:8", ["const:6d23d4:8", "const:4:8"]]
+ 006d23d4 ["CALLIND", null, ["register:0:8"]]
- 006d2024 bytes 00013fd6
+ 006d23d4 bytes 00013fd6
~~~


<a id="compare-69b6b835d063771919ab524138f5698e"></a>

### [`006d5b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5b5c.md) → [`006d5f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d5f0c.md) FUN_006d5f0c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) · 呼出先 2件 [`00664e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e80.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 1件 [`0099803c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00998/0099803c.md) · 呼出先 2件 [`00665230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665230.md) [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d5b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5b5c.md#insn-006d5b9c) · [`006d5bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5b5c.md#insn-006d5bb8)
- 新版 [`006d5f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d5f0c.md#insn-006d5f4c) · [`006d5f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d5f0c.md#insn-006d5f68)

~~~diff
- 006d5b9c ["INT_ADD", "register:40f0:8", ["const:6d5b9c:8", "const:4:8"]]
- 006d5b9c ["CALL", null, ["callee:00665230:8"]]
+ 006d5f4c ["INT_ADD", "register:40f0:8", ["const:6d5f4c:8", "const:4:8"]]
+ 006d5f4c ["CALL", null, ["callee:00665230:8"]]
- 006d5b9c bytes b93cfe97
+ 006d5f4c bytes b93cfe97
- 006d5bb8 ["INT_ADD", "register:40f0:8", ["const:6d5bb8:8", "const:4:8"]]
- 006d5bb8 ["CALL", null, ["callee:00c594f0:8"]]
+ 006d5f68 ["INT_ADD", "register:40f0:8", ["const:6d5f68:8", "const:4:8"]]
+ 006d5f68 ["CALL", null, ["callee:00c594f0:8"]]
- 006d5bb8 bytes 5a0a1694
+ 006d5f68 bytes 620d1694
~~~


<a id="compare-7320f41e4ca803a6d40ccdd51d0ee82a"></a>

### [`006d5e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5e58.md) → [`006d6208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6208.md) FUN_006d6208

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 3件 [`00664e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e80.md) [`006d5950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5950.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 1件 [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) · 呼出先 3件 [`00665230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665230.md) [`006d5d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d5d00.md) [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d5e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5e58.md#insn-006d5e98) · [`006d5eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5e58.md#insn-006d5eb4)
- 新版 [`006d6248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6208.md#insn-006d6248) · [`006d6264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6208.md#insn-006d6264)

~~~diff
- 006d5e98 ["INT_ADD", "register:40f0:8", ["const:6d5e98:8", "const:4:8"]]
- 006d5e98 ["CALL", null, ["callee:00665230:8"]]
+ 006d6248 ["INT_ADD", "register:40f0:8", ["const:6d6248:8", "const:4:8"]]
+ 006d6248 ["CALL", null, ["callee:00665230:8"]]
- 006d5e98 bytes fa3bfe97
+ 006d6248 bytes fa3bfe97
- 006d5eb4 ["INT_ADD", "register:40f0:8", ["const:6d5eb4:8", "const:4:8"]]
- 006d5eb4 ["CALL", null, ["callee:00c594f0:8"]]
+ 006d6264 ["INT_ADD", "register:40f0:8", ["const:6d6264:8", "const:4:8"]]
+ 006d6264 ["CALL", null, ["callee:00c594f0:8"]]
- 006d5eb4 bytes 9b091694
+ 006d6264 bytes a30c1694
~~~


<a id="compare-c7196f2d2dd794771f9885c6c9c1a422"></a>

### [`006d5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md) → [`006d62ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md) FUN_006d62ac

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`006c64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md) [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`006d12b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md) [`006d87c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d87c0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006d6020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6020.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 17件 [`006c5700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5700.md) [`006c688c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c688c.md) [`006c7218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md) [`006d1660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md) [`006d8b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b70.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006d63d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d63d0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d5f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md#insn-006d5f58) · [`006d5f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md#insn-006d5f78) · [`006d5fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md#insn-006d5fb4)
- 新版 [`006d6308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md#insn-006d6308) · [`006d6328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md#insn-006d6328) · [`006d6364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md#insn-006d6364)

~~~diff
- 006d5f58 ["INT_ADD", "register:40f0:8", ["const:6d5f58:8", "const:4:8"]]
- 006d5f58 ["CALL", null, ["callee:006d63d0:8"]]
+ 006d6308 ["INT_ADD", "register:40f0:8", ["const:6d6308:8", "const:4:8"]]
+ 006d6308 ["CALL", null, ["callee:006d63d0:8"]]
- 006d5f58 bytes 32000094
+ 006d6308 bytes 32000094
- 006d5f78 ["INT_ADD", "register:40f0:8", ["const:6d5f78:8", "const:4:8"]]
- 006d5f78 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d6328 ["INT_ADD", "register:40f0:8", ["const:6d6328:8", "const:4:8"]]
+ 006d6328 ["CALL", null, ["callee:00c58f30:8"]]
- 006d5f78 bytes fa071694
+ 006d6328 bytes 020b1694
- 006d5fb4 ["INT_ADD", "register:40f0:8", ["const:6d5fb4:8", "const:4:8"]]
- 006d5fb4 ["CALL", null, ["callee:0043bf04:8"]]
+ 006d6364 ["INT_ADD", "register:40f0:8", ["const:6d6364:8", "const:4:8"]]
+ 006d6364 ["CALL", null, ["callee:0043bf04:8"]]
- 006d5fb4 bytes 0c97f597
+ 006d6364 bytes e896f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23f5252a893748aca9a594226594e614"></a>

### [`006d6370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6370.md) → [`006d6720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6720.md) FUN_006d6720

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`006c63ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c63ec.md) [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`006cbacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cbacc.md) [`006ccbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cc/006ccbd0.md) · 呼出先 2件 [`006d6370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6370.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 6件 [`006c5700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5700.md) [`006c679c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c6/006c679c.md) [`006c7218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md) [`006cbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbe7c.md) [`006ccf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cc/006ccf80.md) · 呼出先 2件 [`006d6720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6720.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6370.md#insn-006d6390) · [`006d639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6370.md#insn-006d639c)
- 新版 [`006d6740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6720.md#insn-006d6740) · [`006d674c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6720.md#insn-006d674c)

~~~diff
- 006d6390 ["INT_ADD", "register:40f0:8", ["const:6d6390:8", "const:4:8"]]
- 006d6390 ["CALL", null, ["local:b0:8"]]
+ 006d6740 ["INT_ADD", "register:40f0:8", ["const:6d6740:8", "const:4:8"]]
+ 006d6740 ["CALL", null, ["local:b0:8"]]
- 006d6390 bytes f8ffff97
+ 006d6740 bytes f8ffff97
- 006d639c ["INT_ADD", "register:40f0:8", ["const:6d639c:8", "const:4:8"]]
- 006d639c ["CALL", null, ["local:b0:8"]]
+ 006d674c ["INT_ADD", "register:40f0:8", ["const:6d674c:8", "const:4:8"]]
+ 006d674c ["CALL", null, ["local:b0:8"]]
- 006d639c bytes f5ffff97
+ 006d674c bytes f5ffff97
~~~


<a id="compare-801f54618bd947e16c86c2cc1591b6f1"></a>

### [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) → [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md) FUN_006d6764

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006cb598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb598.md) [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) [`006d6730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md) · 呼出先 3件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) [`006d6730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md) [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md)
- 新版 呼出元 3件 [`006cb948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb948.md) [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md) [`006d6ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6ae0.md) · 呼出先 3件 [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md) [`006d6ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6ae0.md) [`006d6db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md#insn-006d6458) · [`006d6470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md#insn-006d6470) · [`006d6540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md#insn-006d6540)
- 新版 [`006d6808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md#insn-006d6808) · [`006d6820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md#insn-006d6820) · [`006d68f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md#insn-006d68f0)

~~~diff
- 006d6458 ["INT_ADD", "register:40f0:8", ["const:6d6458:8", "const:4:8"]]
- 006d6458 ["CALL", null, ["local:b0:8"]]
+ 006d6808 ["INT_ADD", "register:40f0:8", ["const:6d6808:8", "const:4:8"]]
+ 006d6808 ["CALL", null, ["local:b0:8"]]
- 006d6458 bytes d7ffff97
+ 006d6808 bytes d7ffff97
- 006d6470 ["INT_ADD", "register:40f0:8", ["const:6d6470:8", "const:4:8"]]
- 006d6470 ["CALL", null, ["local:b0:8"]]
+ 006d6820 ["INT_ADD", "register:40f0:8", ["const:6d6820:8", "const:4:8"]]
+ 006d6820 ["CALL", null, ["local:b0:8"]]
- 006d6470 bytes d1ffff97
+ 006d6820 bytes d1ffff97
- 006d6540 ["INT_ADD", "register:40f0:8", ["const:6d6540:8", "const:4:8"]]
- 006d6540 ["CALL", null, ["callee:006d6ae0:8"]]
+ 006d68f0 ["INT_ADD", "register:40f0:8", ["const:6d68f0:8", "const:4:8"]]
+ 006d68f0 ["CALL", null, ["callee:006d6ae0:8"]]
- 006d6540 bytes 7c000094
+ 006d68f0 bytes 7c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac14776210cdb68bdb7961f6aeb6d5e7"></a>

### [`006d6730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md) → [`006d6ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6ae0.md) FUN_006d6ae0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) · 呼出先 1件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md)
- 新版 呼出元 1件 [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md) · 呼出先 1件 [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md#insn-006d6880) · [`006d6898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md#insn-006d6898)
- 新版 [`006d6c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6ae0.md#insn-006d6c30) · [`006d6c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6ae0.md#insn-006d6c48)

~~~diff
- 006d6880 ["INT_ADD", "register:40f0:8", ["const:6d6880:8", "const:4:8"]]
- 006d6880 ["CALL", null, ["callee:006d6764:8"]]
+ 006d6c30 ["INT_ADD", "register:40f0:8", ["const:6d6c30:8", "const:4:8"]]
+ 006d6c30 ["CALL", null, ["callee:006d6764:8"]]
- 006d6880 bytes cdfeff97
+ 006d6c30 bytes cdfeff97
- 006d6898 ["INT_ADD", "register:40f0:8", ["const:6d6898:8", "const:4:8"]]
- 006d6898 ["CALL", null, ["callee:006d6764:8"]]
+ 006d6c48 ["INT_ADD", "register:40f0:8", ["const:6d6c48:8", "const:4:8"]]
+ 006d6c48 ["CALL", null, ["callee:006d6764:8"]]
- 006d6898 bytes c7feff97
+ 006d6c48 bytes c7feff97
~~~


<a id="compare-970b8f08463208fd1ec928e82a9511c5"></a>

### [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md) → [`006d6db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md) FUN_006d6db8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md) · 呼出先 1件 [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md)
- 新版 呼出元 2件 [`006d6764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6764.md) [`006d6db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md) · 呼出先 1件 [`006d6db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md#insn-006d6cb4) · [`006d6ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md#insn-006d6ce0)
- 新版 [`006d7064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md#insn-006d7064) · [`006d7090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d6db8.md#insn-006d7090)

~~~diff
- 006d6cb4 ["INT_ADD", "register:40f0:8", ["const:6d6cb4:8", "const:4:8"]]
- 006d6cb4 ["CALL", null, ["local:b0:8"]]
+ 006d7064 ["INT_ADD", "register:40f0:8", ["const:6d7064:8", "const:4:8"]]
+ 006d7064 ["CALL", null, ["local:b0:8"]]
- 006d6cb4 bytes 55ffff97
+ 006d7064 bytes 55ffff97
- 006d6ce0 ["INT_ADD", "register:40f0:8", ["const:6d6ce0:8", "const:4:8"]]
- 006d6ce0 ["CALL", null, ["local:b0:8"]]
+ 006d7090 ["INT_ADD", "register:40f0:8", ["const:6d7090:8", "const:4:8"]]
+ 006d7090 ["CALL", null, ["local:b0:8"]]
- 006d6ce0 bytes 4affff97
+ 006d7090 bytes 4affff97
~~~


<a id="compare-2855fd4fd9a7b092212fb82b58127758"></a>

### [`006d7078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md) → [`006d7428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md) FUN_006d7428

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006cb8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb8e4.md) [`006d7078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md) · 呼出先 2件 [`006d7078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`006cbc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbc94.md) [`006d7428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md) · 呼出先 2件 [`006d7428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d7098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md#insn-006d7098) · [`006d70a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md#insn-006d70a4)
- 新版 [`006d7448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md#insn-006d7448) · [`006d7454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md#insn-006d7454)

~~~diff
- 006d7098 ["INT_ADD", "register:40f0:8", ["const:6d7098:8", "const:4:8"]]
- 006d7098 ["CALL", null, ["local:b0:8"]]
+ 006d7448 ["INT_ADD", "register:40f0:8", ["const:6d7448:8", "const:4:8"]]
+ 006d7448 ["CALL", null, ["local:b0:8"]]
- 006d7098 bytes f8ffff97
+ 006d7448 bytes f8ffff97
- 006d70a4 ["INT_ADD", "register:40f0:8", ["const:6d70a4:8", "const:4:8"]]
- 006d70a4 ["CALL", null, ["local:b0:8"]]
+ 006d7454 ["INT_ADD", "register:40f0:8", ["const:6d7454:8", "const:4:8"]]
+ 006d7454 ["CALL", null, ["local:b0:8"]]
- 006d70a4 bytes f5ffff97
+ 006d7454 bytes f5ffff97
~~~


<a id="compare-1c81173c0d54c0bdc88f7c150b451106"></a>

### [`006d70bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70bc.md) → [`006d746c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d746c.md) FUN_006d746c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006cff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cf/006cff44.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md)
- 新版 呼出元 1件 [`006d02f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d02f4.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d70cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70bc.md#insn-006d70cc)
- 新版 [`006d747c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d746c.md#insn-006d747c)

~~~diff
- 006d70cc ["INT_ADD", "register:40f0:8", ["const:6d70cc:8", "const:4:8"]]
- 006d70cc ["CALL", null, ["callee:00c5b920:8"]]
+ 006d747c ["INT_ADD", "register:40f0:8", ["const:6d747c:8", "const:4:8"]]
+ 006d747c ["CALL", null, ["callee:00c5b920:8"]]
- 006d70cc bytes 210e1694
+ 006d747c bytes 29111694
~~~


<a id="compare-6be873b22e12d002805bbcca24f3df80"></a>

### [`006d73e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md) → [`006d7794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md) FUN_006d7794

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006d70e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md) [`007f3ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ee4.md) · 呼出先 8件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`006d7490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md) [`007f4e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f4/007f4e48.md) · 呼出先 8件 [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d74d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md#insn-006d74d4) · [`006d754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md#insn-006d754c) · [`006d7578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md#insn-006d7578)
- 新版 [`006d7884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md#insn-006d7884) · [`006d78fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md#insn-006d78fc) · [`006d7928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md#insn-006d7928)

~~~diff
- 006d74d4 ["INT_ADD", "register:40f0:8", ["const:6d74d4:8", "const:4:8"]]
- 006d74d4 ["CALL", null, ["callee:00c5b940:8"]]
+ 006d7884 ["INT_ADD", "register:40f0:8", ["const:6d7884:8", "const:4:8"]]
+ 006d7884 ["CALL", null, ["callee:00c5b940:8"]]
- 006d74d4 bytes 270d1694
+ 006d7884 bytes 2f101694
- 006d754c ["INT_ADD", "register:40f0:8", ["const:6d754c:8", "const:4:8"]]
- 006d754c ["CALL", null, ["callee:00c58f30:8"]]
+ 006d78fc ["INT_ADD", "register:40f0:8", ["const:6d78fc:8", "const:4:8"]]
+ 006d78fc ["CALL", null, ["callee:00c58f30:8"]]
- 006d754c bytes 85021694
+ 006d78fc bytes 8d051694
- 006d7578 ["INT_ADD", "register:40f0:8", ["const:6d7578:8", "const:4:8"]]
- 006d7578 ["CALL", null, ["callee:00c590a0:8"]]
+ 006d7928 ["INT_ADD", "register:40f0:8", ["const:6d7928:8", "const:4:8"]]
+ 006d7928 ["CALL", null, ["callee:00c590a0:8"]]
- 006d7578 bytes d6021694
+ 006d7928 bytes de051694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fd504b1c0ceb0558670a1d99b5b4f71"></a>

### [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) → [`006d7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md) FUN_006d7aec

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`006d70e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md) [`007f3ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ee4.md) [`00bf2c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2c88.md) [`00bf2d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2d08.md) [`00c1769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c1769c.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 13件 [`006d7490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md) [`007f4e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f4/007f4e48.md) [`00bf3c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3c7c.md) [`00bf3cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3cfc.md) [`00c18690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18690.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d77a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md#insn-006d77a0) · [`006d77cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md#insn-006d77cc) · [`006d77d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md#insn-006d77d0)
- 新版 [`006d7b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md#insn-006d7b50) · [`006d7b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md#insn-006d7b7c) · [`006d7b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md#insn-006d7b80)

~~~diff
- 006d77a0 ["INT_ADD", "register:40f0:8", ["const:6d77a0:8", "const:4:8"]]
- 006d77a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d7b50 ["INT_ADD", "register:40f0:8", ["const:6d7b50:8", "const:4:8"]]
+ 006d7b50 ["CALL", null, ["callee:00c58f30:8"]]
- 006d77a0 bytes f0011694
+ 006d7b50 bytes f8041694
- 006d77cc ["INT_ADD", "register:40f0:8", ["const:6d77cc:8", "const:4:8"]]
- 006d77cc ["CALL", null, ["callee:006d7aa8:8"]]
+ 006d7b7c ["INT_ADD", "register:40f0:8", ["const:6d7b7c:8", "const:4:8"]]
+ 006d7b7c ["CALL", null, ["callee:006d7aa8:8"]]
- 006d77cc bytes cbffff97
+ 006d7b7c bytes cbffff97
- 006d77d0 ["INT_ADD", "register:40f0:8", ["const:6d77d0:8", "const:4:8"]]
- 006d77d0 ["CALL", null, ["callee:00441220:8"]]
+ 006d7b80 ["INT_ADD", "register:40f0:8", ["const:6d7b80:8", "const:4:8"]]
+ 006d7b80 ["CALL", null, ["callee:00441220:8"]]
- 006d77d0 bytes cca5f597
+ 006d7b80 bytes a8a5f597
~~~


<a id="compare-17b93ed7ca52728e198a8b1e95c55ac5"></a>

### [`006d7be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md) → [`006d7f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7f98.md) FUN_006d7f98

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006d77d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md) [`007f41e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f41e8.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`006d7b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md) [`007f514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f5/007f514c.md) · 呼出先 7件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d7ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md#insn-006d7ccc) · [`006d7d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md#insn-006d7d3c) · [`006d7d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md#insn-006d7d5c)
- 新版 [`006d807c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7f98.md#insn-006d807c) · [`006d80ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7f98.md#insn-006d80ec) · [`006d810c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7f98.md#insn-006d810c)

~~~diff
- 006d7ccc ["INT_ADD", "register:40f0:8", ["const:6d7ccc:8", "const:4:8"]]
- 006d7ccc ["CALL", null, ["callee:00c5b980:8"]]
+ 006d807c ["INT_ADD", "register:40f0:8", ["const:6d807c:8", "const:4:8"]]
+ 006d807c ["CALL", null, ["callee:00c5b980:8"]]
- 006d7ccc bytes 390b1694
+ 006d807c bytes 410e1694
- 006d7d3c ["INT_ADD", "register:40f0:8", ["const:6d7d3c:8", "const:4:8"]]
- 006d7d3c ["CALL", null, ["callee:00c58f30:8"]]
+ 006d80ec ["INT_ADD", "register:40f0:8", ["const:6d80ec:8", "const:4:8"]]
+ 006d80ec ["CALL", null, ["callee:00c58f30:8"]]
- 006d7d3c bytes 89001694
+ 006d80ec bytes 91031694
- 006d7d5c ["INT_ADD", "register:40f0:8", ["const:6d7d5c:8", "const:4:8"]]
- 006d7d5c ["CALL", null, ["callee:00c590a0:8"]]
+ 006d810c ["INT_ADD", "register:40f0:8", ["const:6d810c:8", "const:4:8"]]
+ 006d810c ["CALL", null, ["callee:00c590a0:8"]]
- 006d7d5c bytes dd001694
+ 006d810c bytes e5031694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33b9e8f5d410c73d7d2ecc2ead624eac"></a>

### [`006d7f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7f4c.md) → [`006d82fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d82fc.md) FUN_006d82fc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`006d1510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d1510.md) [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) [`006d82b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d82b0.md) [`006d87c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d87c0.md) [`006d8d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d58.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 10件 [`006d18c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d18c0.md) [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) [`006d8660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8660.md) [`006d8b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b70.md) [`006d9108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9108.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d808c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7f4c.md#insn-006d808c) · [`006d8148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7f4c.md#insn-006d8148) · [`006d816c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7f4c.md#insn-006d816c)
- 新版 [`006d843c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d82fc.md#insn-006d843c) · [`006d84f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d82fc.md#insn-006d84f8) · [`006d851c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d82fc.md#insn-006d851c)

~~~diff
- 006d808c ["INT_ADD", "register:40f0:8", ["const:6d808c:8", "const:4:8"]]
- 006d808c ["CALL", null, ["callee:0043bf04:8"]]
+ 006d843c ["INT_ADD", "register:40f0:8", ["const:6d843c:8", "const:4:8"]]
+ 006d843c ["CALL", null, ["callee:0043bf04:8"]]
- 006d808c bytes d68ef597
+ 006d843c bytes b28ef597
- 006d8148 ["INT_ADD", "register:40f0:8", ["const:6d8148:8", "const:4:8"]]
- 006d8148 ["CALL", null, ["callee:00676e50:8"]]
+ 006d84f8 ["INT_ADD", "register:40f0:8", ["const:6d84f8:8", "const:4:8"]]
+ 006d84f8 ["CALL", null, ["callee:00676e50:8"]]
- 006d8148 bytes 567afe97
+ 006d84f8 bytes 567afe97
- 006d816c ["INT_ADD", "register:40f0:8", ["const:6d816c:8", "const:4:8"]]
- 006d816c ["CALL", null, ["callee:00676e50:8"]]
+ 006d851c ["INT_ADD", "register:40f0:8", ["const:6d851c:8", "const:4:8"]]
+ 006d851c ["CALL", null, ["callee:00676e50:8"]]
- 006d816c bytes 4d7afe97
+ 006d851c bytes 4d7afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce31b3a6e2ea93e79a53880c42ec393f"></a>

### [`006dac04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md) → [`006dafb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dafb4.md) FUN_006dafb4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006dadcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dadcc.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`006f9f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f30.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006db17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`006fa2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa2e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dac40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md#insn-006dac40) · [`006dac4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md#insn-006dac4c) · [`006dac5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md#insn-006dac5c)
- 新版 [`006daff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dafb4.md#insn-006daff0) · [`006daffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dafb4.md#insn-006daffc) · [`006db00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dafb4.md#insn-006db00c)

~~~diff
- 006dac40 ["INT_ADD", "register:40f0:8", ["const:6dac40:8", "const:4:8"]]
- 006dac40 ["CALL", null, ["callee:00487c7c:8"]]
+ 006daff0 ["INT_ADD", "register:40f0:8", ["const:6daff0:8", "const:4:8"]]
+ 006daff0 ["CALL", null, ["callee:00487c7c:8"]]
- 006dac40 bytes 47b3f697
+ 006daff0 bytes 23b3f697
- 006dac4c ["INT_ADD", "register:40f0:8", ["const:6dac4c:8", "const:4:8"]]
- 006dac4c ["CALL", null, ["callee:00487c9c:8"]]
+ 006daffc ["INT_ADD", "register:40f0:8", ["const:6daffc:8", "const:4:8"]]
+ 006daffc ["CALL", null, ["callee:00487c9c:8"]]
- 006dac4c bytes 4cb3f697
+ 006daffc bytes 28b3f697
- 006dac5c ["INT_ADD", "register:40f0:8", ["const:6dac5c:8", "const:4:8"]]
- 006dac5c ["CALL", null, ["callee:00487c9c:8"]]
+ 006db00c ["INT_ADD", "register:40f0:8", ["const:6db00c:8", "const:4:8"]]
+ 006db00c ["CALL", null, ["callee:00487c9c:8"]]
- 006dac5c bytes 48b3f697
+ 006db00c bytes 24b3f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-082fb03a3e35e252c70db34280009f9e"></a>

### [`006dafac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dafac.md) → [`006db35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db35c.md) FUN_006db35c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006db020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dafac.md#insn-006db020)
- 新版 [`006db3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db35c.md#insn-006db3d0)

~~~diff
- 006db020 ["INT_ADD", "register:40f0:8", ["const:6db020:8", "const:4:8"]]
- 006db020 ["CALL", null, ["callee:0046db10:8"]]
+ 006db3d0 ["INT_ADD", "register:40f0:8", ["const:6db3d0:8", "const:4:8"]]
+ 006db3d0 ["CALL", null, ["callee:0046db10:8"]]
- 006db020 bytes f449f697
+ 006db3d0 bytes d049f697
~~~


<a id="compare-3681e0f17bda3c2687036a4031d26196"></a>

### [`006db074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md) → [`006db424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db424.md) FUN_006db424

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 4件 [`00480e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480e98.md) [`00480ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`004810a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md) [`004813f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004813f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006db094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md#insn-006db094) · [`006db0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md#insn-006db0a0) · [`006db0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db074.md#insn-006db0ac)
- 新版 [`006db444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db424.md#insn-006db444) · [`006db450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db424.md#insn-006db450) · [`006db45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db424.md#insn-006db45c)

~~~diff
- 006db094 ["INT_ADD", "register:40f0:8", ["const:6db094:8", "const:4:8"]]
- 006db094 ["CALL", null, ["callee:00480ef0:8"]]
+ 006db444 ["INT_ADD", "register:40f0:8", ["const:6db444:8", "const:4:8"]]
+ 006db444 ["CALL", null, ["callee:00480ef0:8"]]
- 006db094 bytes cf96f697
+ 006db444 bytes ab96f697
- 006db0a0 ["INT_ADD", "register:40f0:8", ["const:6db0a0:8", "const:4:8"]]
- 006db0a0 ["CALL", null, ["callee:004813f8:8"]]
+ 006db450 ["INT_ADD", "register:40f0:8", ["const:6db450:8", "const:4:8"]]
+ 006db450 ["CALL", null, ["callee:004813f8:8"]]
- 006db0a0 bytes 0e98f697
+ 006db450 bytes ea97f697
- 006db0ac ["INT_ADD", "register:40f0:8", ["const:6db0ac:8", "const:4:8"]]
- 006db0ac ["CALL", null, ["callee:00480e98:8"]]
+ 006db45c ["INT_ADD", "register:40f0:8", ["const:6db45c:8", "const:4:8"]]
+ 006db45c ["CALL", null, ["callee:00480e98:8"]]
- 006db0ac bytes b396f697
+ 006db45c bytes 8f96f697
~~~


<a id="compare-2fc006f3a33dea0b4c5990a9932f16cc"></a>

### [`006db0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md) → [`006db474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db474.md) FUN_006db474

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 4件 [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 4件 [`00480478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480478.md) [`004804d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/004804d8.md) [`00480658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00480aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006db0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md#insn-006db0dc) · [`006db0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md#insn-006db0ec) · [`006db0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db0c4.md#insn-006db0f8)
- 新版 [`006db48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db474.md#insn-006db48c) · [`006db49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db474.md#insn-006db49c) · [`006db4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db474.md#insn-006db4a8)

~~~diff
- 006db0dc ["INT_ADD", "register:40f0:8", ["const:6db0dc:8", "const:4:8"]]
- 006db0dc ["CALL", null, ["callee:004804d8:8"]]
+ 006db48c ["INT_ADD", "register:40f0:8", ["const:6db48c:8", "const:4:8"]]
+ 006db48c ["CALL", null, ["callee:004804d8:8"]]
- 006db0dc bytes 3794f697
+ 006db48c bytes 1394f697
- 006db0ec ["INT_ADD", "register:40f0:8", ["const:6db0ec:8", "const:4:8"]]
- 006db0ec ["CALL", null, ["callee:00480aa4:8"]]
+ 006db49c ["INT_ADD", "register:40f0:8", ["const:6db49c:8", "const:4:8"]]
+ 006db49c ["CALL", null, ["callee:00480aa4:8"]]
- 006db0ec bytes a695f697
+ 006db49c bytes 8295f697
- 006db0f8 ["INT_ADD", "register:40f0:8", ["const:6db0f8:8", "const:4:8"]]
- 006db0f8 ["CALL", null, ["callee:00480478:8"]]
+ 006db4a8 ["INT_ADD", "register:40f0:8", ["const:6db4a8:8", "const:4:8"]]
+ 006db4a8 ["CALL", null, ["callee:00480478:8"]]
- 006db0f8 bytes 1894f697
+ 006db4a8 bytes f493f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87fa30a705e126a07a9746ff4a2e977d"></a>

### [`006dbbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbbc4.md) → [`006dbf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006dbf74.md) FUN_006dbf74

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006dbe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbe00.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006fa138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa138.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`006dc1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc1b0.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006fa4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dbccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbbc4.md#insn-006dbccc) · [`006dbd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbbc4.md#insn-006dbd08) · [`006dbd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbbc4.md#insn-006dbd1c)
- 新版 [`006dc07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006dbf74.md#insn-006dc07c) · [`006dc0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006dbf74.md#insn-006dc0b8) · [`006dc0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006dbf74.md#insn-006dc0cc)

~~~diff
- 006dbccc ["INT_ADD", "register:40f0:8", ["const:6dbccc:8", "const:4:8"]]
- 006dbccc ["CALL", null, ["callee:00c58f30:8"]]
+ 006dc07c ["INT_ADD", "register:40f0:8", ["const:6dc07c:8", "const:4:8"]]
+ 006dc07c ["CALL", null, ["callee:00c58f30:8"]]
- 006dbccc bytes a5f01594
+ 006dc07c bytes adf31594
- 006dbd08 ["INT_ADD", "register:40f0:8", ["const:6dbd08:8", "const:4:8"]]
- 006dbd08 ["CALL", null, ["callee:00c590a0:8"]]
+ 006dc0b8 ["INT_ADD", "register:40f0:8", ["const:6dc0b8:8", "const:4:8"]]
+ 006dc0b8 ["CALL", null, ["callee:00c590a0:8"]]
- 006dbd08 bytes f2f01594
+ 006dc0b8 bytes faf31594
- 006dbd1c ["INT_ADD", "register:40f0:8", ["const:6dbd1c:8", "const:4:8"]]
- 006dbd1c ["CALL", null, ["callee:00c58f50:8"]]
+ 006dc0cc ["INT_ADD", "register:40f0:8", ["const:6dc0cc:8", "const:4:8"]]
+ 006dc0cc ["CALL", null, ["callee:00c58f50:8"]]
- 006dbd1c bytes 99f01594
+ 006dc0cc bytes a1f31594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-887796f53d4edd65599f1528a7a38750"></a>

### [`006dc6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc6d4.md) → [`006dca84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dca84.md) FUN_006dca84

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)
- 新版 呼出元 1件 [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · 呼出先 1件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dc6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc6d4.md#insn-006dc6ec)
- 新版 [`006dca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dca84.md#insn-006dca9c)

~~~diff
- 006dc6ec ["INT_ADD", "register:40f0:8", ["const:6dc6ec:8", "const:4:8"]]
- 006dc6ec ["CALL", null, ["callee:005c1b8c:8"]]
+ 006dca9c ["INT_ADD", "register:40f0:8", ["const:6dca9c:8", "const:4:8"]]
+ 006dca9c ["CALL", null, ["callee:005c1b8c:8"]]
- 006dc6ec bytes 3c94fb97
+ 006dca9c bytes 3c94fb97
~~~


<a id="compare-0e496de87da138cb157560dfc2419ff7"></a>

### [`006dc704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md) → [`006dcab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcab4.md) FUN_006dcab4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 2件 [`00480f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480f48.md) [`00481188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481188.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dc728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md#insn-006dc728) · [`006dc760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md#insn-006dc760) · [`006dc76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc704.md#insn-006dc76c)
- 新版 [`006dcad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcab4.md#insn-006dcad8) · [`006dcb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcab4.md#insn-006dcb10) · [`006dcb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcab4.md#insn-006dcb1c)

~~~diff
- 006dc728 ["INT_ADD", "register:40f0:8", ["const:6dc728:8", "const:4:8"]]
- 006dc728 ["CALL", null, ["callee:00480f48:8"]]
+ 006dcad8 ["INT_ADD", "register:40f0:8", ["const:6dcad8:8", "const:4:8"]]
+ 006dcad8 ["CALL", null, ["callee:00480f48:8"]]
- 006dc728 bytes 4091f697
+ 006dcad8 bytes 1c91f697
- 006dc760 ["INT_ADD", "register:40f0:8", ["const:6dc760:8", "const:4:8"]]
- 006dc760 ["CALL", null, ["callee:00480f48:8"]]
+ 006dcb10 ["INT_ADD", "register:40f0:8", ["const:6dcb10:8", "const:4:8"]]
+ 006dcb10 ["CALL", null, ["callee:00480f48:8"]]
- 006dc760 bytes 3291f697
+ 006dcb10 bytes 0e91f697
- 006dc76c ["INT_ADD", "register:40f0:8", ["const:6dc76c:8", "const:4:8"]]
- 006dc76c ["CALL", null, ["callee:00481188:8"]]
+ 006dcb1c ["INT_ADD", "register:40f0:8", ["const:6dcb1c:8", "const:4:8"]]
+ 006dcb1c ["CALL", null, ["callee:00481188:8"]]
- 006dc76c bytes bf91f697
+ 006dcb1c bytes 9b91f697
~~~


<a id="compare-02d20ded62fd4c8691598d8bc7829f41"></a>

### [`006dc7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc7a0.md) → [`006dcb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcb50.md) FUN_006dcb50

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00480538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480538.md) [`00480750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480750.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dc7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc7a0.md#insn-006dc7c8) · [`006dc7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc7a0.md#insn-006dc7e8) · [`006dc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc7a0.md#insn-006dc80c)
- 新版 [`006dcb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcb50.md#insn-006dcb78) · [`006dcb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcb50.md#insn-006dcb98) · [`006dcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcb50.md#insn-006dcbbc)

~~~diff
- 006dc7c8 ["INT_ADD", "register:40f0:8", ["const:6dc7c8:8", "const:4:8"]]
- 006dc7c8 ["CALL", null, ["callee:00480538:8"]]
+ 006dcb78 ["INT_ADD", "register:40f0:8", ["const:6dcb78:8", "const:4:8"]]
+ 006dcb78 ["CALL", null, ["callee:00480538:8"]]
- 006dc7c8 bytes 948ef697
+ 006dcb78 bytes 708ef697
- 006dc7e8 ["INT_ADD", "register:40f0:8", ["const:6dc7e8:8", "const:4:8"]]
- 006dc7e8 ["CALL", null, ["callee:0043bf04:8"]]
+ 006dcb98 ["INT_ADD", "register:40f0:8", ["const:6dcb98:8", "const:4:8"]]
+ 006dcb98 ["CALL", null, ["callee:0043bf04:8"]]
- 006dc7e8 bytes ff7cf597
+ 006dcb98 bytes db7cf597
- 006dc80c ["INT_ADD", "register:40f0:8", ["const:6dc80c:8", "const:4:8"]]
- 006dc80c ["CALL", null, ["callee:00480538:8"]]
+ 006dcbbc ["INT_ADD", "register:40f0:8", ["const:6dcbbc:8", "const:4:8"]]
+ 006dcbbc ["CALL", null, ["callee:00480538:8"]]
- 006dc80c bytes 838ef697
+ 006dcbbc bytes 5f8ef697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7c91917194dbb6c75520a9e41f2d5f1"></a>

### [`006dc8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc8dc.md) → [`006dcc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcc8c.md) FUN_006dcc8c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0063acf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063acf4.md) [`0063ae18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063ae18.md) [`0063b3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b3f4.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 4件 [`0063b0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063b0a4.md) [`0063b1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063b1c8.md) [`0063b7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063b7a4.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dc904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc8dc.md#insn-006dc904)
- 新版 [`006dccb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcc8c.md#insn-006dccb4)

~~~diff
- 006dc904 ["INT_ADD", "register:40f0:8", ["const:6dc904:8", "const:4:8"]]
- 006dc904 ["CALL", null, ["callee:008524fc:8"]]
+ 006dccb4 ["INT_ADD", "register:40f0:8", ["const:6dccb4:8", "const:4:8"]]
+ 006dccb4 ["CALL", null, ["callee:008524fc:8"]]
- 006dc904 bytes 13d30594
+ 006dccb4 bytes 12d60594
~~~


<a id="compare-808f3a1ca5ddc633b8ace34ea1195562"></a>

### [`006de76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md) → [`006deb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb1c.md) FUN_006deb1c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 3件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 3件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006de784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md#insn-006de784) · [`006de7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md#insn-006de7a0) · [`006de7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md#insn-006de7a4)
- 新版 [`006deb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb1c.md#insn-006deb34) · [`006deb50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb1c.md#insn-006deb50) · [`006deb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb1c.md#insn-006deb54)

~~~diff
- 006de784 ["INT_ADD", "register:40f0:8", ["const:6de784:8", "const:4:8"]]
- 006de784 ["CALL", null, ["callee:0046db10:8"]]
+ 006deb34 ["INT_ADD", "register:40f0:8", ["const:6deb34:8", "const:4:8"]]
+ 006deb34 ["CALL", null, ["callee:0046db10:8"]]
- 006de784 bytes 1b3cf697
+ 006deb34 bytes f73bf697
- 006de7a0 ["INT_ADD", "register:40f0:8", ["const:6de7a0:8", "const:4:8"]]
- 006de7a0 ["CALL", null, ["callee:008524fc:8"]]
+ 006deb50 ["INT_ADD", "register:40f0:8", ["const:6deb50:8", "const:4:8"]]
+ 006deb50 ["CALL", null, ["callee:008524fc:8"]]
- 006de7a0 bytes 6ccb0594
+ 006deb50 bytes 6bce0594
- 006de7a4 ["INT_ADD", "register:40f0:8", ["const:6de7a4:8", "const:4:8"]]
- 006de7a4 ["CALL", null, ["callee:0046cd24:8"]]
+ 006deb54 ["INT_ADD", "register:40f0:8", ["const:6deb54:8", "const:4:8"]]
+ 006deb54 ["CALL", null, ["callee:0046cd24:8"]]
- 006de7a4 bytes 9838f697
+ 006deb54 bytes 7438f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b895961cdb8f5cf0053cf4232e92452"></a>

### [`006de7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md) → [`006deb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb90.md) FUN_006deb90

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006deaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006deaec.md) [`006e1f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1f00.md) [`006e3378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3378.md) · 呼出先 4件 [`006b2744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2744.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md) [`009dcf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcf20.md)
- 新版 呼出元 3件 [`006dee9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006dee9c.md) [`006e22b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e22b0.md) [`006e3728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e3728.md) · 呼出先 4件 [`006b2af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2af4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2e4.md) [`009ddecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dd/009ddecc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006de7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md#insn-006de7f0) · [`006de7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md#insn-006de7fc) · [`006de804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md#insn-006de804)
- 新版 [`006deba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb90.md#insn-006deba0) · [`006debac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb90.md#insn-006debac) · [`006debb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006de/006deb90.md#insn-006debb4)

~~~diff
- 006de7f0 ["INT_ADD", "register:40f0:8", ["const:6de7f0:8", "const:4:8"]]
- 006de7f0 ["CALL", null, ["callee:008524fc:8"]]
+ 006deba0 ["INT_ADD", "register:40f0:8", ["const:6deba0:8", "const:4:8"]]
+ 006deba0 ["CALL", null, ["callee:008524fc:8"]]
- 006de7f0 bytes 58cb0594
+ 006deba0 bytes 57ce0594
- 006de7fc ["INT_ADD", "register:40f0:8", ["const:6de7fc:8", "const:4:8"]]
- 006de7fc ["CALL", null, ["callee:006b2af4:8"]]
+ 006debac ["INT_ADD", "register:40f0:8", ["const:6debac:8", "const:4:8"]]
+ 006debac ["CALL", null, ["callee:006b2af4:8"]]
- 006de7fc bytes d24fff97
+ 006debac bytes d24fff97
- 006de804 ["INT_ADD", "register:40f0:8", ["const:6de804:8", "const:4:8"]]
- 006de804 ["CALL", null, ["callee:008524fc:8"]]
+ 006debb4 ["INT_ADD", "register:40f0:8", ["const:6debb4:8", "const:4:8"]]
+ 006debb4 ["CALL", null, ["callee:008524fc:8"]]
- 006de804 bytes 53cb0594
+ 006debb4 bytes 52ce0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816db935fa414bbfcb603c83134eca07"></a>

### [`006df76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006df76c.md) → [`006dfb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dfb1c.md) FUN_006dfb1c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f16e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f16e0.md) · 呼出先 11件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md)
- 新版 呼出元 1件 [`006f1a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f1a90.md) · 呼出先 11件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006df828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006df76c.md#insn-006df828) · [`006df860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006df76c.md#insn-006df860) · [`006df880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006df76c.md#insn-006df880)
- 新版 [`006dfbd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dfb1c.md#insn-006dfbd8) · [`006dfc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dfb1c.md#insn-006dfc10) · [`006dfc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dfb1c.md#insn-006dfc30)

~~~diff
- 006df828 ["INT_ADD", "register:40f0:8", ["const:6df828:8", "const:4:8"]]
- 006df828 ["CALL", null, ["callee:00c58f30:8"]]
+ 006dfbd8 ["INT_ADD", "register:40f0:8", ["const:6dfbd8:8", "const:4:8"]]
+ 006dfbd8 ["CALL", null, ["callee:00c58f30:8"]]
- 006df828 bytes cee11594
+ 006dfbd8 bytes d6e41594
- 006df860 ["INT_ADD", "register:40f0:8", ["const:6df860:8", "const:4:8"]]
- 006df860 ["CALL", null, ["callee:0043bf04:8"]]
+ 006dfc10 ["INT_ADD", "register:40f0:8", ["const:6dfc10:8", "const:4:8"]]
+ 006dfc10 ["CALL", null, ["callee:0043bf04:8"]]
- 006df860 bytes e170f597
+ 006dfc10 bytes bd70f597
- 006df880 ["INT_ADD", "register:40f0:8", ["const:6df880:8", "const:4:8"]]
- 006df880 ["CALL", null, ["callee:00801334:8"]]
+ 006dfc30 ["INT_ADD", "register:40f0:8", ["const:6dfc30:8", "const:4:8"]]
+ 006dfc30 ["CALL", null, ["callee:00801334:8"]]
- 006df880 bytes d4820494
+ 006dfc30 bytes c1850494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c47017516163fc437e2069f8cc0ddc"></a>

### [`006dfb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfb94.md) → [`006dff44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dff44.md) FUN_006dff44

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 6件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) [`009d1320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d1/009d1320.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dfc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfb94.md#insn-006dfc14) · [`006dfc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfb94.md#insn-006dfc44) · [`006dfc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfb94.md#insn-006dfc58)
- 新版 [`006dffc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dff44.md#insn-006dffc4) · [`006dfff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dff44.md#insn-006dfff4) · [`006e0008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006dff44.md#insn-006e0008)

~~~diff
- 006dfc14 ["INT_ADD", "register:40f0:8", ["const:6dfc14:8", "const:4:8"]]
- 006dfc14 ["CALL", null, ["callee:00c58f30:8"]]
+ 006dffc4 ["INT_ADD", "register:40f0:8", ["const:6dffc4:8", "const:4:8"]]
+ 006dffc4 ["CALL", null, ["callee:00c58f30:8"]]
- 006dfc14 bytes d3e01594
+ 006dffc4 bytes dbe31594
- 006dfc44 ["INT_ADD", "register:40f0:8", ["const:6dfc44:8", "const:4:8"]]
- 006dfc44 ["CALL", null, ["callee:00c590a0:8"]]
+ 006dfff4 ["INT_ADD", "register:40f0:8", ["const:6dfff4:8", "const:4:8"]]
+ 006dfff4 ["CALL", null, ["callee:00c590a0:8"]]
- 006dfc44 bytes 23e11594
+ 006dfff4 bytes 2be41594
- 006dfc58 ["INT_ADD", "register:40f0:8", ["const:6dfc58:8", "const:4:8"]]
- 006dfc58 ["CALL", null, ["callee:00c58f50:8"]]
+ 006e0008 ["INT_ADD", "register:40f0:8", ["const:6e0008:8", "const:4:8"]]
+ 006e0008 ["CALL", null, ["callee:00c58f50:8"]]
- 006dfc58 bytes cae01594
+ 006e0008 bytes d2e31594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8acd0fb6ca4816ab75592e01eeab0bc0"></a>

### [`006dfc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfc84.md) → [`006e0034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0034.md) FUN_006e0034

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00805d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805d8c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085c1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085c1a4.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`00806cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00806/00806cf0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085d/0085d150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006dfca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfc84.md#insn-006dfca0) · [`006dfcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfc84.md#insn-006dfcbc) · [`006dfcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfc84.md#insn-006dfcd8)
- 新版 [`006e0050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0034.md#insn-006e0050) · [`006e006c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0034.md#insn-006e006c) · [`006e0088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0034.md#insn-006e0088)

~~~diff
- 006dfca0 ["INT_ADD", "register:40f0:8", ["const:6dfca0:8", "const:4:8"]]
- 006dfca0 ["CALL", null, ["callee:008524fc:8"]]
+ 006e0050 ["INT_ADD", "register:40f0:8", ["const:6e0050:8", "const:4:8"]]
+ 006e0050 ["CALL", null, ["callee:008524fc:8"]]
- 006dfca0 bytes 2cc60594
+ 006e0050 bytes 2bc90594
- 006dfcbc ["INT_ADD", "register:40f0:8", ["const:6dfcbc:8", "const:4:8"]]
- 006dfcbc ["CALL", null, ["callee:008524fc:8"]]
+ 006e006c ["INT_ADD", "register:40f0:8", ["const:6e006c:8", "const:4:8"]]
+ 006e006c ["CALL", null, ["callee:008524fc:8"]]
- 006dfcbc bytes 25c60594
+ 006e006c bytes 24c90594
- 006dfcd8 ["INT_ADD", "register:40f0:8", ["const:6dfcd8:8", "const:4:8"]]
- 006dfcd8 ["CALL", null, ["callee:00c594f0:8"]]
+ 006e0088 ["INT_ADD", "register:40f0:8", ["const:6e0088:8", "const:4:8"]]
+ 006e0088 ["CALL", null, ["callee:00c594f0:8"]]
- 006dfcd8 bytes 12e21594
+ 006e0088 bytes 1ae51594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d5274e177be064e3d1e486d5f8c46e7"></a>

### [`006e040c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e040c.md) → [`006e07bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e07bc.md) FUN_006e07bc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e044c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e040c.md#insn-006e044c) · [`006e045c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e040c.md#insn-006e045c) · [`006e046c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e040c.md#insn-006e046c)
- 新版 [`006e07fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e07bc.md#insn-006e07fc) · [`006e080c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e07bc.md#insn-006e080c) · [`006e081c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e07bc.md#insn-006e081c)

~~~diff
- 006e044c ["INT_ADD", "register:40f0:8", ["const:6e044c:8", "const:4:8"]]
- 006e044c ["CALL", null, ["callee:00c58f50:8"]]
+ 006e07fc ["INT_ADD", "register:40f0:8", ["const:6e07fc:8", "const:4:8"]]
+ 006e07fc ["CALL", null, ["callee:00c58f50:8"]]
- 006e044c bytes cdde1594
+ 006e07fc bytes d5e11594
- 006e045c ["INT_ADD", "register:40f0:8", ["const:6e045c:8", "const:4:8"]]
- 006e045c ["CALL", null, ["callee:00c58f50:8"]]
+ 006e080c ["INT_ADD", "register:40f0:8", ["const:6e080c:8", "const:4:8"]]
+ 006e080c ["CALL", null, ["callee:00c58f50:8"]]
- 006e045c bytes c9de1594
+ 006e080c bytes d1e11594
- 006e046c ["INT_ADD", "register:40f0:8", ["const:6e046c:8", "const:4:8"]]
- 006e046c ["CALL", null, ["callee:00c58f50:8"]]
+ 006e081c ["INT_ADD", "register:40f0:8", ["const:6e081c:8", "const:4:8"]]
+ 006e081c ["CALL", null, ["callee:00c58f50:8"]]
- 006e046c bytes c5de1594
+ 006e081c bytes cde11594
~~~


<a id="compare-a9b23aede3b8f2d57128b0d2d11577f3"></a>

### [`006e0488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0488.md) → [`006e0838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0838.md) FUN_006e0838

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e04c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0488.md#insn-006e04c8) · [`006e04d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0488.md#insn-006e04d8) · [`006e04e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0488.md#insn-006e04e8)
- 新版 [`006e0878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0838.md#insn-006e0878) · [`006e0888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0838.md#insn-006e0888) · [`006e0898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0838.md#insn-006e0898)

~~~diff
- 006e04c8 ["INT_ADD", "register:40f0:8", ["const:6e04c8:8", "const:4:8"]]
- 006e04c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 006e0878 ["INT_ADD", "register:40f0:8", ["const:6e0878:8", "const:4:8"]]
+ 006e0878 ["CALL", null, ["callee:00c58f50:8"]]
- 006e04c8 bytes aede1594
+ 006e0878 bytes b6e11594
- 006e04d8 ["INT_ADD", "register:40f0:8", ["const:6e04d8:8", "const:4:8"]]
- 006e04d8 ["CALL", null, ["callee:00c58f50:8"]]
+ 006e0888 ["INT_ADD", "register:40f0:8", ["const:6e0888:8", "const:4:8"]]
+ 006e0888 ["CALL", null, ["callee:00c58f50:8"]]
- 006e04d8 bytes aade1594
+ 006e0888 bytes b2e11594
- 006e04e8 ["INT_ADD", "register:40f0:8", ["const:6e04e8:8", "const:4:8"]]
- 006e04e8 ["CALL", null, ["callee:00c58f50:8"]]
+ 006e0898 ["INT_ADD", "register:40f0:8", ["const:6e0898:8", "const:4:8"]]
+ 006e0898 ["CALL", null, ["callee:00c58f50:8"]]
- 006e04e8 bytes a6de1594
+ 006e0898 bytes aee11594
~~~


<a id="compare-71c7a837bed4f9d060d7209115a7e673"></a>

### [`006e0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0558.md) → [`006e0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0908.md) FUN_006e0908

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0085c1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085c1a4.md) · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0085d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085d/0085d150.md) · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e0588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0558.md#insn-006e0588) · [`006e05a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0558.md#insn-006e05a0) · [`006e05bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0558.md#insn-006e05bc)
- 新版 [`006e0938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0908.md#insn-006e0938) · [`006e0950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0908.md#insn-006e0950) · [`006e096c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0908.md#insn-006e096c)

~~~diff
- 006e0588 ["INT_ADD", "register:40f0:8", ["const:6e0588:8", "const:4:8"]]
- 006e0588 ["CALL", null, ["callee:00c58f30:8"]]
+ 006e0938 ["INT_ADD", "register:40f0:8", ["const:6e0938:8", "const:4:8"]]
+ 006e0938 ["CALL", null, ["callee:00c58f30:8"]]
- 006e0588 bytes 76de1594
+ 006e0938 bytes 7ee11594
- 006e05a0 ["INT_ADD", "register:40f0:8", ["const:6e05a0:8", "const:4:8"]]
- 006e05a0 ["CALL", null, ["callee:00c590a0:8"]]
+ 006e0950 ["INT_ADD", "register:40f0:8", ["const:6e0950:8", "const:4:8"]]
+ 006e0950 ["CALL", null, ["callee:00c590a0:8"]]
- 006e05a0 bytes ccde1594
+ 006e0950 bytes d4e11594
- 006e05bc ["INT_ADD", "register:40f0:8", ["const:6e05bc:8", "const:4:8"]]
- 006e05bc ["CALL", null, ["callee:00470ba0:8"]]
+ 006e096c ["INT_ADD", "register:40f0:8", ["const:6e096c:8", "const:4:8"]]
+ 006e096c ["CALL", null, ["callee:00470ba0:8"]]
- 006e05bc bytes b140f697
+ 006e096c bytes 8d40f697
~~~


<a id="compare-6d4776fac560a6a85086d8f711ac067f"></a>

### [`006e05e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e05e0.md) → [`006e0990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0990.md) FUN_006e0990

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 3件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e0610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e05e0.md#insn-006e0610) · [`006e0628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e05e0.md#insn-006e0628) · [`006e0644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e05e0.md#insn-006e0644)
- 新版 [`006e09c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0990.md#insn-006e09c0) · [`006e09d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0990.md#insn-006e09d8) · [`006e09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e0990.md#insn-006e09f4)

~~~diff
- 006e0610 ["INT_ADD", "register:40f0:8", ["const:6e0610:8", "const:4:8"]]
- 006e0610 ["CALL", null, ["callee:00c58f30:8"]]
+ 006e09c0 ["INT_ADD", "register:40f0:8", ["const:6e09c0:8", "const:4:8"]]
+ 006e09c0 ["CALL", null, ["callee:00c58f30:8"]]
- 006e0610 bytes 54de1594
+ 006e09c0 bytes 5ce11594
- 006e0628 ["INT_ADD", "register:40f0:8", ["const:6e0628:8", "const:4:8"]]
- 006e0628 ["CALL", null, ["callee:00c590a0:8"]]
+ 006e09d8 ["INT_ADD", "register:40f0:8", ["const:6e09d8:8", "const:4:8"]]
+ 006e09d8 ["CALL", null, ["callee:00c590a0:8"]]
- 006e0628 bytes aade1594
+ 006e09d8 bytes b2e11594
- 006e0644 ["INT_ADD", "register:40f0:8", ["const:6e0644:8", "const:4:8"]]
- 006e0644 ["CALL", null, ["callee:00470ba0:8"]]
+ 006e09f4 ["INT_ADD", "register:40f0:8", ["const:6e09f4:8", "const:4:8"]]
+ 006e09f4 ["CALL", null, ["callee:00470ba0:8"]]
- 006e0644 bytes 8f40f697
+ 006e09f4 bytes 6b40f697
~~~


<a id="compare-8aac25be200348305add62195fd733dd"></a>

### [`006e1cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1cd8.md) → [`006e2088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2088.md) FUN_006e2088

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e1638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`006e19e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e1/006e19e8.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e1d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1cd8.md#insn-006e1d24) · [`006e1d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1cd8.md#insn-006e1d50) · [`006e1d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1cd8.md#insn-006e1d7c)
- 新版 [`006e20d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2088.md#insn-006e20d4) · [`006e2100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2088.md#insn-006e2100) · [`006e212c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2088.md#insn-006e212c)

~~~diff
- 006e1d24 ["INT_ADD", "register:40f0:8", ["const:6e1d24:8", "const:4:8"]]
- 006e1d24 ["CALL", null, ["callee:0043be80:8"]]
+ 006e20d4 ["INT_ADD", "register:40f0:8", ["const:6e20d4:8", "const:4:8"]]
+ 006e20d4 ["CALL", null, ["callee:0043be80:8"]]
- 006e1d24 bytes 8f67f597
+ 006e20d4 bytes 6b67f597
- 006e1d50 ["INT_ADD", "register:40f0:8", ["const:6e1d50:8", "const:4:8"]]
- 006e1d50 ["CALL", null, ["callee:0043be80:8"]]
+ 006e2100 ["INT_ADD", "register:40f0:8", ["const:6e2100:8", "const:4:8"]]
+ 006e2100 ["CALL", null, ["callee:0043be80:8"]]
- 006e1d50 bytes 8467f597
+ 006e2100 bytes 6067f597
- 006e1d7c ["INT_ADD", "register:40f0:8", ["const:6e1d7c:8", "const:4:8"]]
- 006e1d7c ["CALL", null, ["callee:0043be80:8"]]
+ 006e212c ["INT_ADD", "register:40f0:8", ["const:6e212c:8", "const:4:8"]]
+ 006e212c ["CALL", null, ["callee:0043be80:8"]]
- 006e1d7c bytes 7967f597
+ 006e212c bytes 5567f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-294f1b43540089bf275482650b21e4b8"></a>

### [`006e2934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2934.md) → [`006e2ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2ce4.md) FUN_006e2ce4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f8720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7e0.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md)
- 新版 呼出元 1件 [`006f8ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb00.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e2960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2934.md#insn-006e2960) · [`006e2998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2934.md#insn-006e2998) · [`006e29b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2934.md#insn-006e29b4)
- 新版 [`006e2d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2ce4.md#insn-006e2d10) · [`006e2d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2ce4.md#insn-006e2d48) · [`006e2d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2ce4.md#insn-006e2d64)

~~~diff
- 006e2960 ["INT_ADD", "register:40f0:8", ["const:6e2960:8", "const:4:8"]]
- 006e2960 ["CALL", null, ["callee:00470440:8"]]
+ 006e2d10 ["INT_ADD", "register:40f0:8", ["const:6e2d10:8", "const:4:8"]]
+ 006e2d10 ["CALL", null, ["callee:00470440:8"]]
- 006e2960 bytes f035f697
+ 006e2d10 bytes cc35f697
- 006e2998 ["INT_ADD", "register:40f0:8", ["const:6e2998:8", "const:4:8"]]
- 006e2998 ["CALL", null, ["callee:0046eb00:8"]]
+ 006e2d48 ["INT_ADD", "register:40f0:8", ["const:6e2d48:8", "const:4:8"]]
+ 006e2d48 ["CALL", null, ["callee:0046eb00:8"]]
- 006e2998 bytes 922ff697
+ 006e2d48 bytes 6e2ff697
- 006e29b4 ["INT_ADD", "register:40f0:8", ["const:6e29b4:8", "const:4:8"]]
- 006e29b4 ["CALL", null, ["callee:00470414:8"]]
+ 006e2d64 ["INT_ADD", "register:40f0:8", ["const:6e2d64:8", "const:4:8"]]
+ 006e2d64 ["CALL", null, ["callee:00470414:8"]]
- 006e29b4 bytes d035f697
+ 006e2d64 bytes ac35f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40aece1e920e0d7f416246cbccbd122c"></a>

### [`006e3d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3d94.md) → [`006e4144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4144.md) FUN_006e4144

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f8720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7e0.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md)
- 新版 呼出元 1件 [`006f8ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb00.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e3dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3d94.md#insn-006e3dc0) · [`006e3df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3d94.md#insn-006e3df8) · [`006e3e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3d94.md#insn-006e3e14)
- 新版 [`006e4170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4144.md#insn-006e4170) · [`006e41a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4144.md#insn-006e41a8) · [`006e41c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4144.md#insn-006e41c4)

~~~diff
- 006e3dc0 ["INT_ADD", "register:40f0:8", ["const:6e3dc0:8", "const:4:8"]]
- 006e3dc0 ["CALL", null, ["callee:00470440:8"]]
+ 006e4170 ["INT_ADD", "register:40f0:8", ["const:6e4170:8", "const:4:8"]]
+ 006e4170 ["CALL", null, ["callee:00470440:8"]]
- 006e3dc0 bytes d830f697
+ 006e4170 bytes b430f697
- 006e3df8 ["INT_ADD", "register:40f0:8", ["const:6e3df8:8", "const:4:8"]]
- 006e3df8 ["CALL", null, ["callee:0046eb00:8"]]
+ 006e41a8 ["INT_ADD", "register:40f0:8", ["const:6e41a8:8", "const:4:8"]]
+ 006e41a8 ["CALL", null, ["callee:0046eb00:8"]]
- 006e3df8 bytes 7a2af697
+ 006e41a8 bytes 562af697
- 006e3e14 ["INT_ADD", "register:40f0:8", ["const:6e3e14:8", "const:4:8"]]
- 006e3e14 ["CALL", null, ["callee:00470414:8"]]
+ 006e41c4 ["INT_ADD", "register:40f0:8", ["const:6e41c4:8", "const:4:8"]]
+ 006e41c4 ["CALL", null, ["callee:00470414:8"]]
- 006e3e14 bytes b830f697
+ 006e41c4 bytes 9430f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dab03a4539f292b2d5df7ae4a695da5a"></a>

### [`006e7290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7290.md) → [`006e7640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7640.md) FUN_006e7640

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e72b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7290.md#insn-006e72b4) · [`006e72fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7290.md#insn-006e72fc) · [`006e731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7290.md#insn-006e731c)
- 新版 [`006e7664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7640.md#insn-006e7664) · [`006e76ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7640.md#insn-006e76ac) · [`006e76cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7640.md#insn-006e76cc)

~~~diff
- 006e72b4 ["INT_ADD", "register:40f0:8", ["const:6e72b4:8", "const:4:8"]]
- 006e72b4 ["CALL", null, ["callee:00c59080:8"]]
+ 006e7664 ["INT_ADD", "register:40f0:8", ["const:6e7664:8", "const:4:8"]]
+ 006e7664 ["CALL", null, ["callee:00c59080:8"]]
- 006e72b4 bytes 7fc31594
+ 006e7664 bytes 87c61594
- 006e72fc ["INT_ADD", "register:40f0:8", ["const:6e72fc:8", "const:4:8"]]
- 006e72fc ["CALL", null, ["callee:00c58f30:8"]]
+ 006e76ac ["INT_ADD", "register:40f0:8", ["const:6e76ac:8", "const:4:8"]]
+ 006e76ac ["CALL", null, ["callee:00c58f30:8"]]
- 006e72fc bytes 19c31594
+ 006e76ac bytes 21c61594
- 006e731c ["INT_ADD", "register:40f0:8", ["const:6e731c:8", "const:4:8"]]
- 006e731c ["CALL", null, ["callee:00c58fe0:8"]]
+ 006e76cc ["INT_ADD", "register:40f0:8", ["const:6e76cc:8", "const:4:8"]]
+ 006e76cc ["CALL", null, ["callee:00c58fe0:8"]]
- 006e731c bytes 3dc31594
+ 006e76cc bytes 45c61594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a04e7ac288326b64879780a30bad92"></a>

### [`006e8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md) → [`006e8f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8f5c.md) FUN_006e8f5c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 3件 [`006c4218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 3件 [`006c45c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e8bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md#insn-006e8bc0) · [`006e8bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md#insn-006e8bc8) · [`006e8bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8bac.md#insn-006e8bd0)
- 新版 [`006e8f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8f5c.md#insn-006e8f70) · [`006e8f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8f5c.md#insn-006e8f78) · [`006e8f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8f5c.md#insn-006e8f80)

~~~diff
- 006e8bc0 ["INT_ADD", "register:40f0:8", ["const:6e8bc0:8", "const:4:8"]]
- 006e8bc0 ["CALL", null, ["callee:006c45c8:8"]]
+ 006e8f70 ["INT_ADD", "register:40f0:8", ["const:6e8f70:8", "const:4:8"]]
+ 006e8f70 ["CALL", null, ["callee:006c45c8:8"]]
- 006e8bc0 bytes 966dff97
+ 006e8f70 bytes 966dff97
- 006e8bc8 ["INT_ADD", "register:40f0:8", ["const:6e8bc8:8", "const:4:8"]]
- 006e8bc8 ["CALL", null, ["callee:006c45c8:8"]]
+ 006e8f78 ["INT_ADD", "register:40f0:8", ["const:6e8f78:8", "const:4:8"]]
+ 006e8f78 ["CALL", null, ["callee:006c45c8:8"]]
- 006e8bc8 bytes 946dff97
+ 006e8f78 bytes 946dff97
- 006e8bd0 ["INT_ADD", "register:40f0:8", ["const:6e8bd0:8", "const:4:8"]]
- 006e8bd0 ["CALL", null, ["callee:006c45c8:8"]]
+ 006e8f80 ["INT_ADD", "register:40f0:8", ["const:6e8f80:8", "const:4:8"]]
+ 006e8f80 ["CALL", null, ["callee:006c45c8:8"]]
- 006e8bd0 bytes 926dff97
+ 006e8f80 bytes 926dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0766ec34c43318949b7815235ad720"></a>

### [`006e9e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e9e64.md) → [`006ea214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea214.md) FUN_006ea214

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`0098cfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098c/0098cfe0.md) · 呼出先 1件 [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)
- 新版 呼出元 4件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) [`0098df8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098d/0098df8c.md) · 呼出先 1件 [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006e9e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e9e64.md#insn-006e9e94)
- 新版 [`006ea244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea214.md#insn-006ea244)

~~~diff
- 006e9e94 ["INT_ADD", "register:40f0:8", ["const:6e9e94:8", "const:4:8"]]
- 006e9e94 ["CALL", null, ["callee:00c5a070:8"]]
+ 006ea244 ["INT_ADD", "register:40f0:8", ["const:6ea244:8", "const:4:8"]]
+ 006ea244 ["CALL", null, ["callee:00c5a070:8"]]
- 006e9e94 bytes 83bc1594
+ 006ea244 bytes 8bbf1594
~~~


<a id="compare-228f4d5b023e26aa3c0a3feb15bd88bf"></a>

### [`006ec724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ec724.md) → [`006ecad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ec/006ecad4.md) FUN_006ecad4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ec74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ec724.md#insn-006ec74c) · [`006ec760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ec724.md#insn-006ec760) · [`006ec768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ec724.md#insn-006ec768)
- 新版 [`006ecafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ec/006ecad4.md#insn-006ecafc) · [`006ecb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ec/006ecad4.md#insn-006ecb10) · [`006ecb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ec/006ecad4.md#insn-006ecb18)

~~~diff
- 006ec74c ["INT_ADD", "register:40f0:8", ["const:6ec74c:8", "const:4:8"]]
- 006ec74c ["CALL", null, ["callee:00c54d90:8"]]
+ 006ecafc ["INT_ADD", "register:40f0:8", ["const:6ecafc:8", "const:4:8"]]
+ 006ecafc ["CALL", null, ["callee:00c54d90:8"]]
- 006ec74c bytes 959d1594
+ 006ecafc bytes a5a01594
- 006ec760 ["COPY", "register:0:8", ["register:4040:8"]]
- 006ec760 ["INT_ADD", "register:40f0:8", ["const:6ec760:8", "const:4:8"]]
- 006ec760 ["CALLIND", null, ["register:0:8"]]
+ 006ecb10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006ecb10 ["INT_ADD", "register:40f0:8", ["const:6ecb10:8", "const:4:8"]]
+ 006ecb10 ["CALLIND", null, ["register:0:8"]]
- 006ec760 bytes 00013fd6
+ 006ecb10 bytes 00013fd6
- 006ec768 ["INT_ADD", "register:40f0:8", ["const:6ec768:8", "const:4:8"]]
- 006ec768 ["CALL", null, ["callee:00c58f20:8"]]
+ 006ecb18 ["INT_ADD", "register:40f0:8", ["const:6ecb18:8", "const:4:8"]]
+ 006ecb18 ["CALL", null, ["callee:00c58f20:8"]]
- 006ec768 bytes faad1594
+ 006ecb18 bytes 02b11594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5833cda9517cad7240c36de3d8f5b4aa"></a>

### [`006f0464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0464.md) → [`006f0814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0814.md) FUN_006f0814

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006ef79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ef/006ef79c.md) [`006fda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`00ab4d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab4/00ab4d70.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 4件 [`006efb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006efb4c.md) [`006fde34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md) [`0093c770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093c/0093c770.md) [`00ab5d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ab5/00ab5d64.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f0488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0464.md#insn-006f0488) · [`006f04d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0464.md#insn-006f04d0) · [`006f04f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0464.md#insn-006f04f0)
- 新版 [`006f0838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0814.md#insn-006f0838) · [`006f0880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0814.md#insn-006f0880) · [`006f08a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0814.md#insn-006f08a0)

~~~diff
- 006f0488 ["INT_ADD", "register:40f0:8", ["const:6f0488:8", "const:4:8"]]
- 006f0488 ["CALL", null, ["callee:00c59080:8"]]
+ 006f0838 ["INT_ADD", "register:40f0:8", ["const:6f0838:8", "const:4:8"]]
+ 006f0838 ["CALL", null, ["callee:00c59080:8"]]
- 006f0488 bytes 0a9f1594
+ 006f0838 bytes 12a21594
- 006f04d0 ["INT_ADD", "register:40f0:8", ["const:6f04d0:8", "const:4:8"]]
- 006f04d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006f0880 ["INT_ADD", "register:40f0:8", ["const:6f0880:8", "const:4:8"]]
+ 006f0880 ["CALL", null, ["callee:00c58f30:8"]]
- 006f04d0 bytes a49e1594
+ 006f0880 bytes aca11594
- 006f04f0 ["INT_ADD", "register:40f0:8", ["const:6f04f0:8", "const:4:8"]]
- 006f04f0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 006f08a0 ["INT_ADD", "register:40f0:8", ["const:6f08a0:8", "const:4:8"]]
+ 006f08a0 ["CALL", null, ["callee:00c58fe0:8"]]
- 006f04f0 bytes c89e1594
+ 006f08a0 bytes d0a11594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c522b0498d0e8dfbebe054c9de9b56c"></a>

### [`006f1618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f1618.md) → [`006f19c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f19c8.md) FUN_006f19c8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 9件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f1680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f1618.md#insn-006f1680) · [`006f16b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f1618.md#insn-006f16b8)
- 新版 [`006f1a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f19c8.md#insn-006f1a30) · [`006f1a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f19c8.md#insn-006f1a68)

~~~diff
- 006f1680 ["INT_ADD", "register:40f0:8", ["const:6f1680:8", "const:4:8"]]
- 006f1680 ["CALL", null, ["callee:00c58f30:8"]]
+ 006f1a30 ["INT_ADD", "register:40f0:8", ["const:6f1a30:8", "const:4:8"]]
+ 006f1a30 ["CALL", null, ["callee:00c58f30:8"]]
- 006f1680 bytes 389a1594
+ 006f1a30 bytes 409d1594
- 006f16b8 ["INT_ADD", "register:40f0:8", ["const:6f16b8:8", "const:4:8"]]
- 006f16b8 ["CALL", null, ["callee:0043bf04:8"]]
+ 006f1a68 ["INT_ADD", "register:40f0:8", ["const:6f1a68:8", "const:4:8"]]
+ 006f1a68 ["CALL", null, ["callee:0043bf04:8"]]
- 006f16b8 bytes 4b29f597
+ 006f1a68 bytes 2729f597
~~~


<a id="compare-4e85be9aca9d801858192e8880be58cc"></a>

### [`006f86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f86ac.md) → [`006f8a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8a5c.md) FUN_006f8a5c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006f86e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f86ac.md#insn-006f86e8) · [`006f86fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f86ac.md#insn-006f86fc)
- 新版 [`006f8a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8a5c.md#insn-006f8a98) · [`006f8aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8a5c.md#insn-006f8aac)

~~~diff
- 006f86e8 ["INT_ADD", "register:40f0:8", ["const:6f86e8:8", "const:4:8"]]
- 006f86e8 ["CALL", null, ["callee:005410dc:8"]]
+ 006f8a98 ["INT_ADD", "register:40f0:8", ["const:6f8a98:8", "const:4:8"]]
+ 006f8a98 ["CALL", null, ["callee:005410dc:8"]]
- 006f86e8 bytes b521f997
+ 006f8a98 bytes 9121f997
- 006f86fc ["INT_ADD", "register:40f0:8", ["const:6f86fc:8", "const:4:8"]]
- 006f86fc ["CALL", null, ["callee:0043be80:8"]]
+ 006f8aac ["INT_ADD", "register:40f0:8", ["const:6f8aac:8", "const:4:8"]]
+ 006f8aac ["CALL", null, ["callee:0043be80:8"]]
- 006f86fc bytes 190df597
+ 006f8aac bytes f50cf597
~~~


<a id="compare-9860370f5a26368cfedb0a4e98ff0f07"></a>

### [`006fa084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa084.md) → [`006fa434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa434.md) FUN_006fa434

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`0046ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046ac48.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba294.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fa0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa084.md#insn-006fa0a0) · [`006fa0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa084.md#insn-006fa0ac) · [`006fa0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa084.md#insn-006fa0b4)
- 新版 [`006fa450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa434.md#insn-006fa450) · [`006fa45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa434.md#insn-006fa45c) · [`006fa464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa434.md#insn-006fa464)

~~~diff
- 006fa0a0 ["INT_ADD", "register:40f0:8", ["const:6fa0a0:8", "const:4:8"]]
- 006fa0a0 ["CALL", null, ["callee:008ba294:8"]]
+ 006fa450 ["INT_ADD", "register:40f0:8", ["const:6fa450:8", "const:4:8"]]
+ 006fa450 ["CALL", null, ["callee:008ba294:8"]]
- 006fa0a0 bytes 92fc0694
+ 006fa450 bytes 91ff0694
- 006fa0ac ["INT_ADD", "register:40f0:8", ["const:6fa0ac:8", "const:4:8"]]
- 006fa0ac ["CALL", null, ["callee:008ba29c:8"]]
+ 006fa45c ["INT_ADD", "register:40f0:8", ["const:6fa45c:8", "const:4:8"]]
+ 006fa45c ["CALL", null, ["callee:008ba29c:8"]]
- 006fa0ac bytes 91fc0694
+ 006fa45c bytes 90ff0694
- 006fa0b4 ["INT_ADD", "register:40f0:8", ["const:6fa0b4:8", "const:4:8"]]
- 006fa0b4 ["CALL", null, ["callee:00467bc0:8"]]
+ 006fa464 ["INT_ADD", "register:40f0:8", ["const:6fa464:8", "const:4:8"]]
+ 006fa464 ["CALL", null, ["callee:00467bc0:8"]]
- 006fa0b4 bytes fbb5f597
+ 006fa464 bytes d7b5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0237d86ad2170162ae6883e3e842808d"></a>

### [`006fa14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md) → [`006fa4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md) FUN_006fa4fc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006dfe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md) [`006fa14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md) [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) · 呼出先 2件 [`006fa14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`006e01d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e01d0.md) [`006fa4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md) [`0086806c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00868/0086806c.md) · 呼出先 2件 [`006fa4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fa168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md#insn-006fa168) · [`006fa174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md#insn-006fa174) · [`006fa19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa14c.md#insn-006fa19c)
- 新版 [`006fa518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md#insn-006fa518) · [`006fa524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md#insn-006fa524) · [`006fa54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4fc.md#insn-006fa54c)

~~~diff
- 006fa168 ["INT_ADD", "register:40f0:8", ["const:6fa168:8", "const:4:8"]]
- 006fa168 ["CALL", null, ["local:b0:8"]]
+ 006fa518 ["INT_ADD", "register:40f0:8", ["const:6fa518:8", "const:4:8"]]
+ 006fa518 ["CALL", null, ["local:b0:8"]]
- 006fa168 bytes f9ffff97
+ 006fa518 bytes f9ffff97
- 006fa174 ["INT_ADD", "register:40f0:8", ["const:6fa174:8", "const:4:8"]]
- 006fa174 ["CALL", null, ["local:b0:8"]]
+ 006fa524 ["INT_ADD", "register:40f0:8", ["const:6fa524:8", "const:4:8"]]
+ 006fa524 ["CALL", null, ["local:b0:8"]]
- 006fa174 bytes f6ffff97
+ 006fa524 bytes f6ffff97
- 006fa19c ["INT_ADD", "register:40f0:8", ["const:6fa19c:8", "const:4:8"]]
- 006fa19c ["CALL", null, ["callee:00c58f50:8"]]
+ 006fa54c ["INT_ADD", "register:40f0:8", ["const:6fa54c:8", "const:4:8"]]
+ 006fa54c ["CALL", null, ["callee:00c58f50:8"]]
- 006fa19c bytes 79771594
+ 006fa54c bytes 817a1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e335da204a3b3d4679c4548341e29ec"></a>

### [`006fa1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa1e8.md) → [`006fa598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa598.md) FUN_006fa598

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006dfe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006e01d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e01d0.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fa258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa1e8.md#insn-006fa258) · [`006fa2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa1e8.md#insn-006fa2f8)
- 新版 [`006fa608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa598.md#insn-006fa608) · [`006fa6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa598.md#insn-006fa6a8)

~~~diff
- 006fa258 ["INT_ADD", "register:40f0:8", ["const:6fa258:8", "const:4:8"]]
- 006fa258 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fa608 ["INT_ADD", "register:40f0:8", ["const:6fa608:8", "const:4:8"]]
+ 006fa608 ["CALL", null, ["callee:00c58f30:8"]]
- 006fa258 bytes 42771594
+ 006fa608 bytes 4a7a1594
- 006fa2f8 ["INT_ADD", "register:40f0:8", ["const:6fa2f8:8", "const:4:8"]]
- 006fa2f8 ["CALL", null, ["callee:0043bf04:8"]]
+ 006fa6a8 ["INT_ADD", "register:40f0:8", ["const:6fa6a8:8", "const:4:8"]]
+ 006fa6a8 ["CALL", null, ["callee:0043bf04:8"]]
- 006fa2f8 bytes 3b06f597
+ 006fa6a8 bytes 1706f597
~~~


<a id="compare-7a0b8818f0f9c07f3aac861ac5bc065d"></a>

### [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) → [`006fb47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md) FUN_006fb47c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`006e4538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) [`006fb968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md) [`006fbd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md) · 呼出先 4件 [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 10件 [`006e48e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e48e8.md) [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) [`006fb47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md) [`006fbd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md) [`006fc0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc0b4.md) · 呼出先 4件 [`006fb47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006fb0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md#insn-006fb0e8) · [`006fb0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md#insn-006fb0f4) · [`006fb108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md#insn-006fb108)
- 新版 [`006fb498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md#insn-006fb498) · [`006fb4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md#insn-006fb4a4) · [`006fb4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb47c.md#insn-006fb4b8)

~~~diff
- 006fb0e8 ["INT_ADD", "register:40f0:8", ["const:6fb0e8:8", "const:4:8"]]
- 006fb0e8 ["CALL", null, ["local:b0:8"]]
+ 006fb498 ["INT_ADD", "register:40f0:8", ["const:6fb498:8", "const:4:8"]]
+ 006fb498 ["CALL", null, ["local:b0:8"]]
- 006fb0e8 bytes f9ffff97
+ 006fb498 bytes f9ffff97
- 006fb0f4 ["INT_ADD", "register:40f0:8", ["const:6fb0f4:8", "const:4:8"]]
- 006fb0f4 ["CALL", null, ["local:b0:8"]]
+ 006fb4a4 ["INT_ADD", "register:40f0:8", ["const:6fb4a4:8", "const:4:8"]]
+ 006fb4a4 ["CALL", null, ["local:b0:8"]]
- 006fb0f4 bytes f6ffff97
+ 006fb4a4 bytes f6ffff97
- 006fb108 ["INT_ADD", "register:40f0:8", ["const:6fb108:8", "const:4:8"]]
- 006fb108 ["CALL", null, ["callee:00c54d90:8"]]
+ 006fb4b8 ["INT_ADD", "register:40f0:8", ["const:6fb4b8:8", "const:4:8"]]
+ 006fb4b8 ["CALL", null, ["callee:00c54d90:8"]]
- 006fb108 bytes 26631594
+ 006fb4b8 bytes 36661594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f89aabacaa959002810a9c4b54b3b5"></a>

### [`006ff120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff120.md) → [`006ff4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff4d0.md) FUN_006ff4d0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ff130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff120.md#insn-006ff130) · [`006ff140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff120.md#insn-006ff140) · [`006ff15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff120.md#insn-006ff15c)
- 新版 [`006ff4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff4d0.md#insn-006ff4e0) · [`006ff4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff4d0.md#insn-006ff4f0) · [`006ff50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff4d0.md#insn-006ff50c)

~~~diff
- 006ff130 ["INT_ADD", "register:40f0:8", ["const:6ff130:8", "const:4:8"]]
- 006ff130 ["CALL", null, ["callee:008524fc:8"]]
+ 006ff4e0 ["INT_ADD", "register:40f0:8", ["const:6ff4e0:8", "const:4:8"]]
+ 006ff4e0 ["CALL", null, ["callee:008524fc:8"]]
- 006ff130 bytes 08490594
+ 006ff4e0 bytes 074c0594
- 006ff140 ["INT_ADD", "register:40f0:8", ["const:6ff140:8", "const:4:8"]]
- 006ff140 ["CALL", null, ["callee:008524fc:8"]]
+ 006ff4f0 ["INT_ADD", "register:40f0:8", ["const:6ff4f0:8", "const:4:8"]]
+ 006ff4f0 ["CALL", null, ["callee:008524fc:8"]]
- 006ff140 bytes 04490594
+ 006ff4f0 bytes 034c0594
- 006ff15c ["INT_ADD", "register:40f0:8", ["const:6ff15c:8", "const:4:8"]]
- 006ff15c ["CALL", null, ["callee:00470414:8"]]
+ 006ff50c ["INT_ADD", "register:40f0:8", ["const:6ff50c:8", "const:4:8"]]
+ 006ff50c ["CALL", null, ["callee:00470414:8"]]
- 006ff15c bytes e6c3f597
+ 006ff50c bytes c2c3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-459cae5e9d33aabd0d1a7c287fb6ad88"></a>

### [`006ff254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff254.md) → [`006ff604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff604.md) FUN_006ff604

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 6件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006ff280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff254.md#insn-006ff280) · [`006ff284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff254.md#insn-006ff284) · [`006ff28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff254.md#insn-006ff28c)
- 新版 [`006ff630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff604.md#insn-006ff630) · [`006ff634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff604.md#insn-006ff634) · [`006ff63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ff604.md#insn-006ff63c)

~~~diff
- 006ff280 ["INT_ADD", "register:40f0:8", ["const:6ff280:8", "const:4:8"]]
- 006ff280 ["CALL", null, ["callee:00470414:8"]]
+ 006ff630 ["INT_ADD", "register:40f0:8", ["const:6ff630:8", "const:4:8"]]
+ 006ff630 ["CALL", null, ["callee:00470414:8"]]
- 006ff280 bytes 9dc3f597
+ 006ff630 bytes 79c3f597
- 006ff284 ["INT_ADD", "register:40f0:8", ["const:6ff284:8", "const:4:8"]]
- 006ff284 ["CALL", null, ["callee:00467bc0:8"]]
+ 006ff634 ["INT_ADD", "register:40f0:8", ["const:6ff634:8", "const:4:8"]]
+ 006ff634 ["CALL", null, ["callee:00467bc0:8"]]
- 006ff284 bytes 87a1f597
+ 006ff634 bytes 63a1f597
- 006ff28c ["INT_ADD", "register:40f0:8", ["const:6ff28c:8", "const:4:8"]]
- 006ff28c ["CALL", null, ["callee:008524fc:8"]]
+ 006ff63c ["INT_ADD", "register:40f0:8", ["const:6ff63c:8", "const:4:8"]]
+ 006ff63c ["CALL", null, ["callee:008524fc:8"]]
- 006ff28c bytes b1480594
+ 006ff63c bytes b04b0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2e58f0cafefc2462d042eeb894ada25"></a>

### [`0070017c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070017c.md) → [`0070052c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070052c.md) FUN_0070052c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070019c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070017c.md#insn-0070019c)
- 新版 [`0070054c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070052c.md#insn-0070054c)

~~~diff
- 0070019c ["INT_ADD", "register:40f0:8", ["const:70019c:8", "const:4:8"]]
- 0070019c ["CALL", null, ["callee:00c58f50:8"]]
+ 0070054c ["INT_ADD", "register:40f0:8", ["const:70054c:8", "const:4:8"]]
+ 0070054c ["CALL", null, ["callee:00c58f50:8"]]
- 0070019c bytes 795f1594
+ 0070054c bytes 81621594
~~~


<a id="compare-d10879769899998c30615a3a2383537b"></a>

### [`00700568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700568.md) → [`00700918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700918.md) FUN_00700918

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00700588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700568.md#insn-00700588)
- 新版 [`00700938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700918.md#insn-00700938)

~~~diff
- 00700588 ["INT_ADD", "register:40f0:8", ["const:700588:8", "const:4:8"]]
- 00700588 ["CALL", null, ["callee:00c58f50:8"]]
+ 00700938 ["INT_ADD", "register:40f0:8", ["const:700938:8", "const:4:8"]]
+ 00700938 ["CALL", null, ["callee:00c58f50:8"]]
- 00700588 bytes 7e5e1594
+ 00700938 bytes 86611594
~~~


<a id="compare-cdbf16f60044c95f07a3f394a9443aa1"></a>

### [`00707984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md) → [`00707d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707d34.md) FUN_00707d34

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 9件 [`005e0918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0918.md) [`005e0960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0960.md) [`00af398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af398c.md) [`00af3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3cb8.md) [`00af3f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3f08.md)
- 新版 呼出元 3件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00715908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md) [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 9件 [`005e0cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e0/005e0cc8.md) [`005e0d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e0/005e0d10.md) [`00af4980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4980.md) [`00af4cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4cac.md) [`00af4efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4efc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007079c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md#insn-007079c4) · [`007079d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md#insn-007079d4) · [`007079ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707984.md#insn-007079ec)
- 新版 [`00707d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707d34.md#insn-00707d74) · [`00707d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707d34.md#insn-00707d84) · [`00707d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707d34.md#insn-00707d9c)

~~~diff
- 007079c4 ["INT_ADD", "register:40f0:8", ["const:7079c4:8", "const:4:8"]]
- 007079c4 ["CALL", null, ["callee:005e0cc8:8"]]
+ 00707d74 ["INT_ADD", "register:40f0:8", ["const:707d74:8", "const:4:8"]]
+ 00707d74 ["CALL", null, ["callee:005e0cc8:8"]]
- 007079c4 bytes d563fb97
+ 00707d74 bytes d563fb97
- 007079d4 ["INT_ADD", "register:40f0:8", ["const:7079d4:8", "const:4:8"]]
- 007079d4 ["CALL", null, ["callee:00af6328:8"]]
+ 00707d84 ["INT_ADD", "register:40f0:8", ["const:707d84:8", "const:4:8"]]
+ 00707d84 ["CALL", null, ["callee:00af6328:8"]]
- 007079d4 bytes 58b60f94
+ 00707d84 bytes 69b90f94
- 007079ec ["INT_ADD", "register:40f0:8", ["const:7079ec:8", "const:4:8"]]
- 007079ec ["CALL", null, ["callee:005e0d10:8"]]
+ 00707d9c ["INT_ADD", "register:40f0:8", ["const:707d9c:8", "const:4:8"]]
+ 00707d9c ["CALL", null, ["callee:005e0d10:8"]]
- 007079ec bytes dd63fb97
+ 00707d9c bytes dd63fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4120e69b02ca7a86588c1cf0e7fdf422"></a>

### [`00707dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707dc8.md) → [`00708178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/00708178.md) FUN_00708178

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005f2da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f2da8.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 2件 [`00afc5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc5a8.md) [`00afc604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc604.md)
- 新版 呼出元 3件 [`005f3158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f3/005f3158.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`007106e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007106e0.md) · 呼出先 2件 [`00afd59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd59c.md) [`00afd5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd5f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707dc8.md#insn-00707df0) · [`00707e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707dc8.md#insn-00707e08) · [`00707e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707dc8.md#insn-00707e20)
- 新版 [`007081a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/00708178.md#insn-007081a0) · [`007081b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/00708178.md#insn-007081b8) · [`007081d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/00708178.md#insn-007081d0)

~~~diff
- 00707df0 ["INT_ADD", "register:40f0:8", ["const:707df0:8", "const:4:8"]]
- 00707df0 ["CALL", null, ["callee:00afd59c:8"]]
+ 007081a0 ["INT_ADD", "register:40f0:8", ["const:7081a0:8", "const:4:8"]]
+ 007081a0 ["CALL", null, ["callee:00afd59c:8"]]
- 00707df0 bytes eed10f94
+ 007081a0 bytes ffd40f94
- 00707e08 ["INT_ADD", "register:40f0:8", ["const:707e08:8", "const:4:8"]]
- 00707e08 ["CALL", null, ["callee:00afd59c:8"]]
+ 007081b8 ["INT_ADD", "register:40f0:8", ["const:7081b8:8", "const:4:8"]]
+ 007081b8 ["CALL", null, ["callee:00afd59c:8"]]
- 00707e08 bytes e8d10f94
+ 007081b8 bytes f9d40f94
- 00707e20 ["INT_ADD", "register:40f0:8", ["const:707e20:8", "const:4:8"]]
- 00707e20 ["CALL", null, ["callee:00afd59c:8"]]
+ 007081d0 ["INT_ADD", "register:40f0:8", ["const:7081d0:8", "const:4:8"]]
+ 007081d0 ["CALL", null, ["callee:00afd59c:8"]]
- 00707e20 bytes e2d10f94
+ 007081d0 bytes f3d40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89aa1b3b2db00f0c5986a573a213d27"></a>

### [`00707f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f08.md) → [`007082b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/007082b8.md) FUN_007082b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00707f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f08.md#insn-00707f20)
- 新版 [`007082d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/007082b8.md#insn-007082d0)

~~~diff
- 00707f20 ["INT_ADD", "register:40f0:8", ["const:707f20:8", "const:4:8"]]
- 00707f20 ["CALL", null, ["callee:00676e50:8"]]
+ 007082d0 ["INT_ADD", "register:40f0:8", ["const:7082d0:8", "const:4:8"]]
+ 007082d0 ["CALL", null, ["callee:00676e50:8"]]
- 00707f20 bytes e0bafd97
+ 007082d0 bytes e0bafd97
~~~


<a id="compare-d05ec42a4a5dae5cfa6d756b132732f4"></a>

### [`0070df48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070df48.md) → [`0070e2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e2f8.md) FUN_0070e2f8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005f2da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f2/005f2da8.md) · 呼出先 2件 [`00afc5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc5a8.md) [`00afc604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afc604.md)
- 新版 呼出元 1件 [`005f3158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f3/005f3158.md) · 呼出先 2件 [`00afd59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd59c.md) [`00afd5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd5f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070df48.md#insn-0070df70) · [`0070df8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070df48.md#insn-0070df8c) · [`0070df9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070df48.md#insn-0070df9c)
- 新版 [`0070e320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e2f8.md#insn-0070e320) · [`0070e33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e2f8.md#insn-0070e33c) · [`0070e34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e2f8.md#insn-0070e34c)

~~~diff
- 0070df70 ["INT_ADD", "register:40f0:8", ["const:70df70:8", "const:4:8"]]
- 0070df70 ["CALL", null, ["callee:00afd59c:8"]]
+ 0070e320 ["INT_ADD", "register:40f0:8", ["const:70e320:8", "const:4:8"]]
+ 0070e320 ["CALL", null, ["callee:00afd59c:8"]]
- 0070df70 bytes 8eb90f94
+ 0070e320 bytes 9fbc0f94
- 0070df8c ["INT_ADD", "register:40f0:8", ["const:70df8c:8", "const:4:8"]]
- 0070df8c ["CALL", null, ["callee:00afd5f8:8"]]
+ 0070e33c ["INT_ADD", "register:40f0:8", ["const:70e33c:8", "const:4:8"]]
+ 0070e33c ["CALL", null, ["callee:00afd5f8:8"]]
- 0070df8c bytes 9eb90f94
+ 0070e33c bytes afbc0f94
- 0070df9c ["INT_ADD", "register:40f0:8", ["const:70df9c:8", "const:4:8"]]
- 0070df9c ["CALL", null, ["callee:00afd59c:8"]]
+ 0070e34c ["INT_ADD", "register:40f0:8", ["const:70e34c:8", "const:4:8"]]
+ 0070e34c ["CALL", null, ["callee:00afd59c:8"]]
- 0070df9c bytes 83b90f94
+ 0070e34c bytes 94bc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc83200cfcdcc559c0f6076291d5a08"></a>

### [`0070e05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e05c.md) → [`0070e40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e40c.md) FUN_0070e40c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00a52ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a52/00a52ea0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`007082e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/007082e8.md) [`00a53e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a53/00a53e94.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046f258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f258.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e05c.md#insn-0070e0dc) · [`0070e0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e05c.md#insn-0070e0fc) · [`0070e128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e05c.md#insn-0070e128)
- 新版 [`0070e48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e40c.md#insn-0070e48c) · [`0070e4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e40c.md#insn-0070e4ac) · [`0070e4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e40c.md#insn-0070e4d8)

~~~diff
- 0070e0dc ["INT_ADD", "register:40f0:8", ["const:70e0dc:8", "const:4:8"]]
- 0070e0dc ["CALL", null, ["callee:00c58f30:8"]]
+ 0070e48c ["INT_ADD", "register:40f0:8", ["const:70e48c:8", "const:4:8"]]
+ 0070e48c ["CALL", null, ["callee:00c58f30:8"]]
- 0070e0dc bytes a1271594
+ 0070e48c bytes a92a1594
- 0070e0fc ["INT_ADD", "register:40f0:8", ["const:70e0fc:8", "const:4:8"]]
- 0070e0fc ["CALL", null, ["callee:0046f258:8"]]
+ 0070e4ac ["INT_ADD", "register:40f0:8", ["const:70e4ac:8", "const:4:8"]]
+ 0070e4ac ["CALL", null, ["callee:0046f258:8"]]
- 0070e0fc bytes 8f83f597
+ 0070e4ac bytes 6b83f597
- 0070e128 ["INT_ADD", "register:40f0:8", ["const:70e128:8", "const:4:8"]]
- 0070e128 ["CALL", null, ["callee:0043bf04:8"]]
+ 0070e4d8 ["INT_ADD", "register:40f0:8", ["const:70e4d8:8", "const:4:8"]]
+ 0070e4d8 ["CALL", null, ["callee:0043bf04:8"]]
- 0070e128 bytes afb6f497
+ 0070e4d8 bytes 8bb6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c531fe1f4e4f7889de7e4cabbdfba2e2"></a>

### [`0070e1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1a0.md) → [`0070e550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e550.md) FUN_0070e550

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046f33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f33c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0070e1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1a0.md#insn-0070e1c4)
- 新版 [`0070e574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070e550.md#insn-0070e574)

~~~diff
- 0070e1c4 ["INT_ADD", "register:40f0:8", ["const:70e1c4:8", "const:4:8"]]
- 0070e1c4 ["CALL", null, ["callee:0046f33c:8"]]
+ 0070e574 ["INT_ADD", "register:40f0:8", ["const:70e574:8", "const:4:8"]]
+ 0070e574 ["CALL", null, ["callee:0046f33c:8"]]
- 0070e1c4 bytes 9683f597
+ 0070e574 bytes 7283f597
~~~


<a id="compare-4ace7bc750d89c21f4fe75615559710e"></a>

### [`00710128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md) → [`007104d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007104d8.md) FUN_007104d8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 15件 [`00ab92ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab9/00ab92ec.md) [`00af644c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af644c.md) [`00af64bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af64bc.md) [`00af652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af652c.md) [`00af659c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af6/00af659c.md)
- 新版 呼出元 2件 [`0070ee64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070e/0070ee64.md) [`00711df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00711/00711df8.md) · 呼出先 15件 [`00aba2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aba/00aba2e0.md) [`00af7440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af7440.md) [`00af74b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af74b0.md) [`00af7520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af7520.md) [`00af7590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af7590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md#insn-0071014c) · [`0071015c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md#insn-0071015c) · [`00710178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710128.md#insn-00710178)
- 新版 [`007104fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007104d8.md#insn-007104fc) · [`0071050c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007104d8.md#insn-0071050c) · [`00710528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00710/007104d8.md#insn-00710528)

~~~diff
- 0071014c ["INT_ADD", "register:40f0:8", ["const:71014c:8", "const:4:8"]]
- 0071014c ["CALL", null, ["callee:00af7440:8"]]
+ 007104fc ["INT_ADD", "register:40f0:8", ["const:7104fc:8", "const:4:8"]]
+ 007104fc ["CALL", null, ["callee:00af7440:8"]]
- 0071014c bytes c0980f94
+ 007104fc bytes d19b0f94
- 0071015c ["INT_ADD", "register:40f0:8", ["const:71015c:8", "const:4:8"]]
- 0071015c ["CALL", null, ["callee:00af74b0:8"]]
+ 0071050c ["INT_ADD", "register:40f0:8", ["const:71050c:8", "const:4:8"]]
+ 0071050c ["CALL", null, ["callee:00af74b0:8"]]
- 0071015c bytes d8980f94
+ 0071050c bytes e99b0f94
- 00710178 ["INT_ADD", "register:40f0:8", ["const:710178:8", "const:4:8"]]
- 00710178 ["CALL", null, ["callee:00aba2e0:8"]]
+ 00710528 ["INT_ADD", "register:40f0:8", ["const:710528:8", "const:4:8"]]
+ 00710528 ["CALL", null, ["callee:00aba2e0:8"]]
- 00710178 bytes 5da40e94
+ 00710528 bytes 6ea70e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7f90e4a7755c2bc4b4cbebb79fafa3"></a>

### [`0071417c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/0071417c.md) → [`0071452c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/0071452c.md) FUN_0071452c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005fe29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe29c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005fe64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe64c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007141fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/0071417c.md#insn-007141fc) · [`00714238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/0071417c.md#insn-00714238) · [`0071424c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/0071417c.md#insn-0071424c)
- 新版 [`007145ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/0071452c.md#insn-007145ac) · [`007145e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/0071452c.md#insn-007145e8) · [`007145fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/0071452c.md#insn-007145fc)

~~~diff
- 007141fc ["INT_ADD", "register:40f0:8", ["const:7141fc:8", "const:4:8"]]
- 007141fc ["CALL", null, ["callee:00c58f30:8"]]
+ 007145ac ["INT_ADD", "register:40f0:8", ["const:7145ac:8", "const:4:8"]]
+ 007145ac ["CALL", null, ["callee:00c58f30:8"]]
- 007141fc bytes 590f1594
+ 007145ac bytes 61121594
- 00714238 ["INT_ADD", "register:40f0:8", ["const:714238:8", "const:4:8"]]
- 00714238 ["CALL", null, ["callee:00c590a0:8"]]
+ 007145e8 ["INT_ADD", "register:40f0:8", ["const:7145e8:8", "const:4:8"]]
+ 007145e8 ["CALL", null, ["callee:00c590a0:8"]]
- 00714238 bytes a60f1594
+ 007145e8 bytes ae121594
- 0071424c ["INT_ADD", "register:40f0:8", ["const:71424c:8", "const:4:8"]]
- 0071424c ["CALL", null, ["callee:00c58f50:8"]]
+ 007145fc ["INT_ADD", "register:40f0:8", ["const:7145fc:8", "const:4:8"]]
+ 007145fc ["CALL", null, ["callee:00c58f50:8"]]
- 0071424c bytes 4d0f1594
+ 007145fc bytes 55121594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2775bb39e4eec2c5efc24d4f0c528aff"></a>

### [`00714274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714274.md) → [`00714624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714624.md) FUN_00714624

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005fe2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe2d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005fe688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fe688.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00714294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00714/00714274.md#insn-00714294)
- 新版 [`00714644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00714/00714624.md#insn-00714644)

~~~diff
- 00714294 ["INT_ADD", "register:40f0:8", ["const:714294:8", "const:4:8"]]
- 00714294 ["CALL", null, ["callee:005fe688:8"]]
+ 00714644 ["INT_ADD", "register:40f0:8", ["const:714644:8", "const:4:8"]]
+ 00714644 ["CALL", null, ["callee:005fe688:8"]]
- 00714294 bytes 11a8fb97
+ 00714644 bytes 11a8fb97
~~~


<a id="compare-ec299e65d280fc54bd038b7bce146f16"></a>

### [`00716ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716ae8.md) → [`00716e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716e98.md) FUN_00716e98

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00715558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00715/00715558.md) [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 6件 [`00af3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3cb8.md) [`00af3cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3cf8.md) [`00af3e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3e60.md) [`00af4210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af4/00af4210.md) [`00af54a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af54a0.md)
- 新版 呼出元 3件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00715908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00715/00715908.md) [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 6件 [`00af4cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4cac.md) [`00af4cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4cec.md) [`00af4e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4e54.md) [`00af5204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af5/00af5204.md) [`00af6494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af6/00af6494.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00716b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716ae8.md#insn-00716b04) · [`00716b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716ae8.md#insn-00716b14) · [`00716b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716ae8.md#insn-00716b28)
- 新版 [`00716eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716e98.md#insn-00716eb4) · [`00716ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716e98.md#insn-00716ec4) · [`00716ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00716/00716e98.md#insn-00716ed8)

~~~diff
- 00716b04 ["INT_ADD", "register:40f0:8", ["const:716b04:8", "const:4:8"]]
- 00716b04 ["CALL", null, ["callee:00af68f4:8"]]
+ 00716eb4 ["INT_ADD", "register:40f0:8", ["const:716eb4:8", "const:4:8"]]
+ 00716eb4 ["CALL", null, ["callee:00af68f4:8"]]
- 00716b04 bytes 7f7b0f94
+ 00716eb4 bytes 907e0f94
- 00716b14 ["INT_ADD", "register:40f0:8", ["const:716b14:8", "const:4:8"]]
- 00716b14 ["CALL", null, ["callee:00af68f4:8"]]
+ 00716ec4 ["INT_ADD", "register:40f0:8", ["const:716ec4:8", "const:4:8"]]
+ 00716ec4 ["CALL", null, ["callee:00af68f4:8"]]
- 00716b14 bytes 7b7b0f94
+ 00716ec4 bytes 8c7e0f94
- 00716b28 ["INT_ADD", "register:40f0:8", ["const:716b28:8", "const:4:8"]]
- 00716b28 ["CALL", null, ["callee:00af4cac:8"]]
+ 00716ed8 ["INT_ADD", "register:40f0:8", ["const:716ed8:8", "const:4:8"]]
+ 00716ed8 ["CALL", null, ["callee:00af4cac:8"]]
- 00716b28 bytes 64740f94
+ 00716ed8 bytes 75770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1e64e5d25f273dcc8dbf8b461b4ad6"></a>

### [`00718610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/00718610.md) → [`007189c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/007189c0.md) FUN_007189c0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00718678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/00718610.md#insn-00718678) · [`007186b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/00718610.md#insn-007186b4)
- 新版 [`00718a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/007189c0.md#insn-00718a28) · [`00718a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/007189c0.md#insn-00718a64)

~~~diff
- 00718678 ["INT_ADD", "register:40f0:8", ["const:718678:8", "const:4:8"]]
- 00718678 ["CALL", null, ["callee:00c58f30:8"]]
+ 00718a28 ["INT_ADD", "register:40f0:8", ["const:718a28:8", "const:4:8"]]
+ 00718a28 ["CALL", null, ["callee:00c58f30:8"]]
- 00718678 bytes 3afe1494
+ 00718a28 bytes 42011594
- 007186b4 ["INT_ADD", "register:40f0:8", ["const:7186b4:8", "const:4:8"]]
- 007186b4 ["CALL", null, ["callee:0043bf04:8"]]
+ 00718a64 ["INT_ADD", "register:40f0:8", ["const:718a64:8", "const:4:8"]]
+ 00718a64 ["CALL", null, ["callee:0043bf04:8"]]
- 007186b4 bytes 4c8df497
+ 00718a64 bytes 288df497
~~~


<a id="compare-db6e259b237304306c9fa1f9e3bab488"></a>

### [`007186dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007186dc.md) → [`00718a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718a8c.md) FUN_00718a8c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071875c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007186dc.md#insn-0071875c) · [`0071878c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007186dc.md#insn-0071878c) · [`007187a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00718/007186dc.md#insn-007187a0)
- 新版 [`00718b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718a8c.md#insn-00718b0c) · [`00718b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718a8c.md#insn-00718b3c) · [`00718b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00718/00718a8c.md#insn-00718b50)

~~~diff
- 0071875c ["INT_ADD", "register:40f0:8", ["const:71875c:8", "const:4:8"]]
- 0071875c ["CALL", null, ["callee:00c58f30:8"]]
+ 00718b0c ["INT_ADD", "register:40f0:8", ["const:718b0c:8", "const:4:8"]]
+ 00718b0c ["CALL", null, ["callee:00c58f30:8"]]
- 0071875c bytes 01fe1494
+ 00718b0c bytes 09011594
- 0071878c ["INT_ADD", "register:40f0:8", ["const:71878c:8", "const:4:8"]]
- 0071878c ["CALL", null, ["callee:00c590a0:8"]]
+ 00718b3c ["INT_ADD", "register:40f0:8", ["const:718b3c:8", "const:4:8"]]
+ 00718b3c ["CALL", null, ["callee:00c590a0:8"]]
- 0071878c bytes 51fe1494
+ 00718b3c bytes 59011594
- 007187a0 ["INT_ADD", "register:40f0:8", ["const:7187a0:8", "const:4:8"]]
- 007187a0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00718b50 ["INT_ADD", "register:40f0:8", ["const:718b50:8", "const:4:8"]]
+ 00718b50 ["CALL", null, ["callee:00c58f50:8"]]
- 007187a0 bytes f8fd1494
+ 00718b50 bytes 00011594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b13c6fed8a5a7fee4de07e6c15e3f2a2"></a>

### [`007193b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/007193b4.md) → [`00719764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719764.md) FUN_00719764

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 19件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`005e0918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0918.md) [`005e0940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0940.md) [`005e0960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0960.md) [`005e0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0da8.md)
- 新版 呼出元 1件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 19件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`005e0cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e0/005e0cc8.md) [`005e0cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e0/005e0cf0.md) [`005e0d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e0/005e0d10.md) [`005e1158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1158.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007193e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/007193b4.md#insn-007193e0) · [`007193f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/007193b4.md#insn-007193f0) · [`00719488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/007193b4.md#insn-00719488)
- 新版 [`00719790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719764.md#insn-00719790) · [`007197a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719764.md#insn-007197a0) · [`00719838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719764.md#insn-00719838)

~~~diff
- 007193e0 ["INT_ADD", "register:40f0:8", ["const:7193e0:8", "const:4:8"]]
- 007193e0 ["CALL", null, ["callee:005e1158:8"]]
+ 00719790 ["INT_ADD", "register:40f0:8", ["const:719790:8", "const:4:8"]]
+ 00719790 ["CALL", null, ["callee:005e1158:8"]]
- 007193e0 bytes 721efb97
+ 00719790 bytes 721efb97
- 007193f0 ["INT_ADD", "register:40f0:8", ["const:7193f0:8", "const:4:8"]]
- 007193f0 ["CALL", null, ["callee:005e7810:8"]]
+ 007197a0 ["INT_ADD", "register:40f0:8", ["const:7197a0:8", "const:4:8"]]
+ 007197a0 ["CALL", null, ["callee:005e7810:8"]]
- 007193f0 bytes 1c38fb97
+ 007197a0 bytes 1c38fb97
- 00719488 ["INT_ADD", "register:40f0:8", ["const:719488:8", "const:4:8"]]
- 00719488 ["CALL", null, ["callee:005e0cc8:8"]]
+ 00719838 ["INT_ADD", "register:40f0:8", ["const:719838:8", "const:4:8"]]
+ 00719838 ["CALL", null, ["callee:005e0cc8:8"]]
- 00719488 bytes 241dfb97
+ 00719838 bytes 241dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be064d205a25680ff266ccd16d96ab38"></a>

### [`00719790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md) → [`00719b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b40.md) FUN_00719b40

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`00716de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00716/00716de8.md) [`009387c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00938/009387c8.md) [`0093b4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b4b4.md) [`00a323f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323f4.md) [`00a324cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a324cc.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 6件 [`00717198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00717/00717198.md) [`00939774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00939/00939774.md) [`0093c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093c/0093c460.md) [`00a333e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a33/00a333e8.md) [`00a334c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a33/00a334c0.md) · 呼出先 2件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00719840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md#insn-00719840) · [`00719850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md#insn-00719850) · [`00719858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md#insn-00719858)
- 新版 [`00719bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b40.md#insn-00719bf0) · [`00719c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b40.md#insn-00719c00) · [`00719c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719b40.md#insn-00719c08)

~~~diff
- 00719840 ["INT_ADD", "register:40f0:8", ["const:719840:8", "const:4:8"]]
- 00719840 ["CALL", null, ["callee:00494970:8"]]
+ 00719bf0 ["INT_ADD", "register:40f0:8", ["const:719bf0:8", "const:4:8"]]
+ 00719bf0 ["CALL", null, ["callee:00494970:8"]]
- 00719840 bytes 84ebf597
+ 00719bf0 bytes 60ebf597
- 00719850 ["INT_ADD", "register:40f0:8", ["const:719850:8", "const:4:8"]]
- 00719850 ["CALL", null, ["callee:00c58f50:8"]]
+ 00719c00 ["INT_ADD", "register:40f0:8", ["const:719c00:8", "const:4:8"]]
+ 00719c00 ["CALL", null, ["callee:00c58f50:8"]]
- 00719850 bytes ccf91494
+ 00719c00 bytes d4fc1494
- 00719858 ["INT_ADD", "register:40f0:8", ["const:719858:8", "const:4:8"]]
- 00719858 ["CALL", null, ["callee:00c58f50:8"]]
+ 00719c08 ["INT_ADD", "register:40f0:8", ["const:719c08:8", "const:4:8"]]
+ 00719c08 ["CALL", null, ["callee:00c58f50:8"]]
- 00719858 bytes caf91494
+ 00719c08 bytes d2fc1494
~~~


<a id="compare-8e46079c81176da519512e80423090f7"></a>

### [`00719bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719bfc.md) → [`00719fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719fac.md) FUN_00719fac

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 1件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md)
- 新版 呼出元 1件 [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) · 呼出先 1件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00719c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719bfc.md#insn-00719c50)
- 新版 [`0071a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00719/00719fac.md#insn-0071a000)

~~~diff
- 00719c50 ["INT_ADD", "register:40f0:8", ["const:719c50:8", "const:4:8"]]
- 00719c50 ["CALL", null, ["callee:0046db10:8"]]
+ 0071a000 ["INT_ADD", "register:40f0:8", ["const:71a000:8", "const:4:8"]]
+ 0071a000 ["CALL", null, ["callee:0046db10:8"]]
- 00719c50 bytes e84ef597
+ 0071a000 bytes c44ef597
~~~


<a id="compare-ec08ae0f4f78ffed6f88d35204806c23"></a>

### [`0071a230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a230.md) → [`0071a5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a5e0.md) FUN_0071a5e0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a230.md#insn-0071a27c) · [`0071a29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a230.md#insn-0071a29c)
- 新版 [`0071a62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a5e0.md#insn-0071a62c) · [`0071a64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a5e0.md#insn-0071a64c)

~~~diff
- 0071a27c ["INT_ADD", "register:40f0:8", ["const:71a27c:8", "const:4:8"]]
- 0071a27c ["CALL", null, ["callee:00c58f50:8"]]
+ 0071a62c ["INT_ADD", "register:40f0:8", ["const:71a62c:8", "const:4:8"]]
+ 0071a62c ["CALL", null, ["callee:00c58f50:8"]]
- 0071a27c bytes 41f71494
+ 0071a62c bytes 49fa1494
- 0071a29c ["INT_ADD", "register:40f0:8", ["const:71a29c:8", "const:4:8"]]
- 0071a29c ["CALL", null, ["callee:00c58f50:8"]]
+ 0071a64c ["INT_ADD", "register:40f0:8", ["const:71a64c:8", "const:4:8"]]
+ 0071a64c ["CALL", null, ["callee:00c58f50:8"]]
- 0071a29c bytes 39f71494
+ 0071a64c bytes 41fa1494
~~~


<a id="compare-ca0e65567c73d4e833c110f959e89973"></a>

### [`0071a328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a328.md) → [`0071a6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a6d8.md) FUN_0071a6d8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00719cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719cc0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0071a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a070.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a328.md#insn-0071a350) · [`0071a358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a328.md#insn-0071a358) · [`0071a3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a328.md#insn-0071a3ac)
- 新版 [`0071a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a6d8.md#insn-0071a700) · [`0071a708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a6d8.md#insn-0071a708) · [`0071a75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071a6d8.md#insn-0071a75c)

~~~diff
- 0071a350 ["INT_ADD", "register:40f0:8", ["const:71a350:8", "const:4:8"]]
- 0071a350 ["CALL", null, ["callee:00c58f50:8"]]
+ 0071a700 ["INT_ADD", "register:40f0:8", ["const:71a700:8", "const:4:8"]]
+ 0071a700 ["CALL", null, ["callee:00c58f50:8"]]
- 0071a350 bytes 0cf71494
+ 0071a700 bytes 14fa1494
- 0071a358 ["INT_ADD", "register:40f0:8", ["const:71a358:8", "const:4:8"]]
- 0071a358 ["CALL", null, ["callee:00c58f50:8"]]
+ 0071a708 ["INT_ADD", "register:40f0:8", ["const:71a708:8", "const:4:8"]]
+ 0071a708 ["CALL", null, ["callee:00c58f50:8"]]
- 0071a358 bytes 0af71494
+ 0071a708 bytes 12fa1494
- 0071a3ac ["INT_ADD", "register:40f0:8", ["const:71a3ac:8", "const:4:8"]]
- 0071a3ac ["CALL", null, ["callee:00c58f50:8"]]
+ 0071a75c ["INT_ADD", "register:40f0:8", ["const:71a75c:8", "const:4:8"]]
+ 0071a75c ["CALL", null, ["callee:00c58f50:8"]]
- 0071a3ac bytes f5f61494
+ 0071a75c bytes fdf91494
~~~


<a id="compare-ece786c49d94421f6b92f9c5d6620f0f"></a>

### [`0071a79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a79c.md) → [`0071ab4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ab4c.md) FUN_0071ab4c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a79c.md#insn-0071a7d4) · [`0071a804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a79c.md#insn-0071a804) · [`0071a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a79c.md#insn-0071a818)
- 新版 [`0071ab84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ab4c.md#insn-0071ab84) · [`0071abb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ab4c.md#insn-0071abb4) · [`0071abc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ab4c.md#insn-0071abc8)

~~~diff
- 0071a7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a7d4 ["INT_ADD", "register:40f0:8", ["const:71a7d4:8", "const:4:8"]]
- 0071a7d4 ["CALLIND", null, ["register:0:8"]]
+ 0071ab84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071ab84 ["INT_ADD", "register:40f0:8", ["const:71ab84:8", "const:4:8"]]
+ 0071ab84 ["CALLIND", null, ["register:0:8"]]
- 0071a7d4 bytes 00013fd6
+ 0071ab84 bytes 00013fd6
- 0071a804 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a804 ["INT_ADD", "register:40f0:8", ["const:71a804:8", "const:4:8"]]
- 0071a804 ["CALLIND", null, ["register:0:8"]]
+ 0071abb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071abb4 ["INT_ADD", "register:40f0:8", ["const:71abb4:8", "const:4:8"]]
+ 0071abb4 ["CALLIND", null, ["register:0:8"]]
- 0071a804 bytes 00013fd6
+ 0071abb4 bytes 00013fd6
- 0071a818 ["INT_ADD", "register:40f0:8", ["const:71a818:8", "const:4:8"]]
- 0071a818 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071abc8 ["INT_ADD", "register:40f0:8", ["const:71abc8:8", "const:4:8"]]
+ 0071abc8 ["CALL", null, ["callee:00487c9c:8"]]
- 0071a818 bytes 59b4f597
+ 0071abc8 bytes 35b4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eefc1ba3c93d31e3d3e50d4c69a8b21b"></a>

### [`0071a8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a8f4.md) → [`0071aca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071aca4.md) FUN_0071aca4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071a930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a8f4.md#insn-0071a930) · [`0071a95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a8f4.md#insn-0071a95c) · [`0071a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071a8f4.md#insn-0071a970)
- 新版 [`0071ace0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071aca4.md#insn-0071ace0) · [`0071ad0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071aca4.md#insn-0071ad0c) · [`0071ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071aca4.md#insn-0071ad20)

~~~diff
- 0071a930 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a930 ["INT_ADD", "register:40f0:8", ["const:71a930:8", "const:4:8"]]
- 0071a930 ["CALLIND", null, ["register:0:8"]]
+ 0071ace0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071ace0 ["INT_ADD", "register:40f0:8", ["const:71ace0:8", "const:4:8"]]
+ 0071ace0 ["CALLIND", null, ["register:0:8"]]
- 0071a930 bytes 00013fd6
+ 0071ace0 bytes 00013fd6
- 0071a95c ["COPY", "register:0:8", ["register:4040:8"]]
- 0071a95c ["INT_ADD", "register:40f0:8", ["const:71a95c:8", "const:4:8"]]
- 0071a95c ["CALLIND", null, ["register:0:8"]]
+ 0071ad0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071ad0c ["INT_ADD", "register:40f0:8", ["const:71ad0c:8", "const:4:8"]]
+ 0071ad0c ["CALLIND", null, ["register:0:8"]]
- 0071a95c bytes 00013fd6
+ 0071ad0c bytes 00013fd6
- 0071a970 ["INT_ADD", "register:40f0:8", ["const:71a970:8", "const:4:8"]]
- 0071a970 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071ad20 ["INT_ADD", "register:40f0:8", ["const:71ad20:8", "const:4:8"]]
+ 0071ad20 ["CALL", null, ["callee:00487c9c:8"]]
- 0071a970 bytes 03b4f597
+ 0071ad20 bytes dfb3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b747bbae987c8fa6bfd6c2c7d86760c9"></a>

### [`0071aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071aa50.md) → [`0071ae00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ae00.md) FUN_0071ae00

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071aa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071aa50.md#insn-0071aa8c) · [`0071aab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071aa50.md#insn-0071aab8) · [`0071aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071aa50.md#insn-0071aacc)
- 新版 [`0071ae3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ae00.md#insn-0071ae3c) · [`0071ae68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ae00.md#insn-0071ae68) · [`0071ae7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071ae00.md#insn-0071ae7c)

~~~diff
- 0071aa8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0071aa8c ["INT_ADD", "register:40f0:8", ["const:71aa8c:8", "const:4:8"]]
- 0071aa8c ["CALLIND", null, ["register:0:8"]]
+ 0071ae3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071ae3c ["INT_ADD", "register:40f0:8", ["const:71ae3c:8", "const:4:8"]]
+ 0071ae3c ["CALLIND", null, ["register:0:8"]]
- 0071aa8c bytes 00013fd6
+ 0071ae3c bytes 00013fd6
- 0071aab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071aab8 ["INT_ADD", "register:40f0:8", ["const:71aab8:8", "const:4:8"]]
- 0071aab8 ["CALLIND", null, ["register:0:8"]]
+ 0071ae68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0071ae68 ["INT_ADD", "register:40f0:8", ["const:71ae68:8", "const:4:8"]]
+ 0071ae68 ["CALLIND", null, ["register:0:8"]]
- 0071aab8 bytes 00013fd6
+ 0071ae68 bytes 00013fd6
- 0071aacc ["INT_ADD", "register:40f0:8", ["const:71aacc:8", "const:4:8"]]
- 0071aacc ["CALL", null, ["callee:00487c9c:8"]]
+ 0071ae7c ["INT_ADD", "register:40f0:8", ["const:71ae7c:8", "const:4:8"]]
+ 0071ae7c ["CALL", null, ["callee:00487c9c:8"]]
- 0071aacc bytes acb3f597
+ 0071ae7c bytes 88b3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b9878711cd7080197deef3c1211f649"></a>

### [`0071abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071abac.md) → [`0071af5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071af5c.md) FUN_0071af5c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0071adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071adbc.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`0071b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b16c.md) · 呼出先 1件 [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071abc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071abac.md#insn-0071abc8) · [`0071abe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071abac.md#insn-0071abe0) · [`0071abf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071abac.md#insn-0071abf0)
- 新版 [`0071af78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071af5c.md#insn-0071af78) · [`0071af90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071af5c.md#insn-0071af90) · [`0071afa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071a/0071af5c.md#insn-0071afa0)

~~~diff
- 0071abc8 ["INT_ADD", "register:40f0:8", ["const:71abc8:8", "const:4:8"]]
- 0071abc8 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071af78 ["INT_ADD", "register:40f0:8", ["const:71af78:8", "const:4:8"]]
+ 0071af78 ["CALL", null, ["callee:00487c9c:8"]]
- 0071abc8 bytes 6db3f597
+ 0071af78 bytes 49b3f597
- 0071abe0 ["INT_ADD", "register:40f0:8", ["const:71abe0:8", "const:4:8"]]
- 0071abe0 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071af90 ["INT_ADD", "register:40f0:8", ["const:71af90:8", "const:4:8"]]
+ 0071af90 ["CALL", null, ["callee:00487c9c:8"]]
- 0071abe0 bytes 67b3f597
+ 0071af90 bytes 43b3f597
- 0071abf0 ["INT_ADD", "register:40f0:8", ["const:71abf0:8", "const:4:8"]]
- 0071abf0 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071afa0 ["INT_ADD", "register:40f0:8", ["const:71afa0:8", "const:4:8"]]
+ 0071afa0 ["CALL", null, ["callee:00487c9c:8"]]
- 0071abf0 bytes 63b3f597
+ 0071afa0 bytes 3fb3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27e56cad955a8a48ed728896a7a48145"></a>

### [`0071c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c478.md) → [`0071c828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c828.md) FUN_0071c828

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 3件 [`0071ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071a/0071ad68.md) [`0071bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bccc.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)
- 新版 呼出元 1件 [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) · 呼出先 3件 [`0071b118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071b/0071b118.md) [`0071c07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c07c.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071c488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c478.md#insn-0071c488) · [`0071c490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c478.md#insn-0071c490) · [`0071c494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c478.md#insn-0071c494)
- 新版 [`0071c838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c828.md#insn-0071c838) · [`0071c840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c828.md#insn-0071c840) · [`0071c844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c828.md#insn-0071c844)

~~~diff
- 0071c488 ["INT_ADD", "register:40f0:8", ["const:71c488:8", "const:4:8"]]
- 0071c488 ["CALL", null, ["callee:0071c07c:8"]]
+ 0071c838 ["INT_ADD", "register:40f0:8", ["const:71c838:8", "const:4:8"]]
+ 0071c838 ["CALL", null, ["callee:0071c07c:8"]]
- 0071c488 bytes 11feff97
+ 0071c838 bytes 11feff97
- 0071c490 ["INT_ADD", "register:40f0:8", ["const:71c490:8", "const:4:8"]]
- 0071c490 ["CALL", null, ["callee:0071c07c:8"]]
+ 0071c840 ["INT_ADD", "register:40f0:8", ["const:71c840:8", "const:4:8"]]
+ 0071c840 ["CALL", null, ["callee:0071c07c:8"]]
- 0071c490 bytes 0ffeff97
+ 0071c840 bytes 0ffeff97
- 0071c494 ["INT_ADD", "register:40f0:8", ["const:71c494:8", "const:4:8"]]
- 0071c494 ["CALL", null, ["callee:0071b118:8"]]
+ 0071c844 ["INT_ADD", "register:40f0:8", ["const:71c844:8", "const:4:8"]]
+ 0071c844 ["CALL", null, ["callee:0071b118:8"]]
- 0071c494 bytes 35faff97
+ 0071c844 bytes 35faff97
~~~


<a id="compare-1f7264c1a963271bb687083d5b80d2f2"></a>

### [`0071e34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e34c.md) → [`0071e6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e6fc.md) FUN_0071e6fc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) · 呼出先 3件 [`00b3befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3befc.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf74.md)
- 新版 呼出元 1件 [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) · 呼出先 3件 [`00b3cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef0.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md) [`00b3cf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e34c.md#insn-0071e38c) · [`0071e394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e34c.md#insn-0071e394) · [`0071e3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e34c.md#insn-0071e3c8)
- 新版 [`0071e73c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e6fc.md#insn-0071e73c) · [`0071e744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e6fc.md#insn-0071e744) · [`0071e778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e6fc.md#insn-0071e778)

~~~diff
- 0071e38c ["INT_ADD", "register:40f0:8", ["const:71e38c:8", "const:4:8"]]
- 0071e38c ["CALL", null, ["callee:00b3cf68:8"]]
+ 0071e73c ["INT_ADD", "register:40f0:8", ["const:71e73c:8", "const:4:8"]]
+ 0071e73c ["CALL", null, ["callee:00b3cf68:8"]]
- 0071e38c bytes fa761094
+ 0071e73c bytes 0b7a1094
- 0071e394 ["INT_ADD", "register:40f0:8", ["const:71e394:8", "const:4:8"]]
- 0071e394 ["CALL", null, ["callee:00b3cf24:8"]]
+ 0071e744 ["INT_ADD", "register:40f0:8", ["const:71e744:8", "const:4:8"]]
+ 0071e744 ["CALL", null, ["callee:00b3cf24:8"]]
- 0071e394 bytes e7761094
+ 0071e744 bytes f8791094
- 0071e3c8 ["INT_ADD", "register:40f0:8", ["const:71e3c8:8", "const:4:8"]]
- 0071e3c8 ["CALL", null, ["callee:00b3cf68:8"]]
+ 0071e778 ["INT_ADD", "register:40f0:8", ["const:71e778:8", "const:4:8"]]
+ 0071e778 ["CALL", null, ["callee:00b3cf68:8"]]
- 0071e3c8 bytes eb761094
+ 0071e778 bytes fc791094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b120572842f7e5a34a4ced4276dcee0"></a>

### [`0071e824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e824.md) → [`0071ebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071ebd4.md) FUN_0071ebd4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) · 呼出先 3件 [`00b3befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3befc.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf74.md)
- 新版 呼出元 1件 [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) · 呼出先 3件 [`00b3cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef0.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md) [`00b3cf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf68.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e824.md#insn-0071e84c) · [`0071e854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e824.md#insn-0071e854)
- 新版 [`0071ebfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071ebd4.md#insn-0071ebfc) · [`0071ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071ebd4.md#insn-0071ec04)

~~~diff
- 0071e84c ["INT_ADD", "register:40f0:8", ["const:71e84c:8", "const:4:8"]]
- 0071e84c ["CALL", null, ["callee:00b3cf68:8"]]
+ 0071ebfc ["INT_ADD", "register:40f0:8", ["const:71ebfc:8", "const:4:8"]]
+ 0071ebfc ["CALL", null, ["callee:00b3cf68:8"]]
- 0071e84c bytes ca751094
+ 0071ebfc bytes db781094
- 0071e854 ["INT_ADD", "register:40f0:8", ["const:71e854:8", "const:4:8"]]
- 0071e854 ["CALL", null, ["callee:00b3cf24:8"]]
+ 0071ec04 ["INT_ADD", "register:40f0:8", ["const:71ec04:8", "const:4:8"]]
+ 0071ec04 ["CALL", null, ["callee:00b3cf24:8"]]
- 0071e854 bytes b7751094
+ 0071ec04 bytes c8781094
~~~


<a id="compare-50797133223fc181d9748a25eb9cb37a"></a>

### [`0071ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md) → [`0071f108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md) FUN_0071f108

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 43件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`0060d664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060d/0060d664.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 43件 [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0060ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060a/0060ac90.md) [`0060da14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060d/0060da14.md) [`0061491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00614/0061491c.md) [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ed70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md#insn-0071ed70) · [`0071ed7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md#insn-0071ed7c)
- 新版 [`0071f120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md#insn-0071f120) · [`0071f12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md#insn-0071f12c)

~~~diff
- 0071ed70 ["INT_ADD", "register:40f0:8", ["const:71ed70:8", "const:4:8"]]
- 0071ed70 ["CALL", null, ["callee:008524fc:8"]]
+ 0071f120 ["INT_ADD", "register:40f0:8", ["const:71f120:8", "const:4:8"]]
+ 0071f120 ["CALL", null, ["callee:008524fc:8"]]
- 0071ed70 bytes f8c90494
+ 0071f120 bytes f7cc0494
- 0071ed7c ["INT_ADD", "register:40f0:8", ["const:71ed7c:8", "const:4:8"]]
- 0071ed7c ["CALL", null, ["callee:008524fc:8"]]
+ 0071f12c ["INT_ADD", "register:40f0:8", ["const:71f12c:8", "const:4:8"]]
+ 0071f12c ["CALL", null, ["callee:008524fc:8"]]
- 0071ed7c bytes f5c90494
+ 0071f12c bytes f4cc0494
~~~


<a id="compare-507d36ec42d533c9dc61c41a05ee87be"></a>

### [`0071edd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071edd0.md) → [`0071f180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f180.md) FUN_0071f180

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 7件 [`005f4a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f4/005f4a9c.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) [`00964fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00964/00964fd8.md) · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071ee10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071edd0.md#insn-0071ee10) · [`0071ee1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071edd0.md#insn-0071ee1c) · [`0071ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071edd0.md#insn-0071ee20)
- 新版 [`0071f1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f180.md#insn-0071f1c0) · [`0071f1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f180.md#insn-0071f1cc) · [`0071f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f180.md#insn-0071f1d0)

~~~diff
- 0071ee10 ["INT_ADD", "register:40f0:8", ["const:71ee10:8", "const:4:8"]]
- 0071ee10 ["CALL", null, ["callee:008524fc:8"]]
+ 0071f1c0 ["INT_ADD", "register:40f0:8", ["const:71f1c0:8", "const:4:8"]]
+ 0071f1c0 ["CALL", null, ["callee:008524fc:8"]]
- 0071ee10 bytes d0c90494
+ 0071f1c0 bytes cfcc0494
- 0071ee1c ["INT_ADD", "register:40f0:8", ["const:71ee1c:8", "const:4:8"]]
- 0071ee1c ["CALL", null, ["callee:008524fc:8"]]
+ 0071f1cc ["INT_ADD", "register:40f0:8", ["const:71f1cc:8", "const:4:8"]]
+ 0071f1cc ["CALL", null, ["callee:008524fc:8"]]
- 0071ee1c bytes cdc90494
+ 0071f1cc bytes cccc0494
- 0071ee20 ["INT_ADD", "register:40f0:8", ["const:71ee20:8", "const:4:8"]]
- 0071ee20 ["CALL", null, ["callee:008524fc:8"]]
+ 0071f1d0 ["INT_ADD", "register:40f0:8", ["const:71f1d0:8", "const:4:8"]]
+ 0071f1d0 ["CALL", null, ["callee:008524fc:8"]]
- 0071ee20 bytes ccc90494
+ 0071f1d0 bytes cbcc0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9fa2ce2971dc4d63c07fa4acee412e"></a>

### [`0071f4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f4b8.md) → [`0071f868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f868.md) FUN_0071f868

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009d906c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d906c.md) · 呼出先 4件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`009da018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009da/009da018.md) · 呼出先 4件 [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`005e8588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e8/005e8588.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071f4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f4b8.md#insn-0071f4e4) · [`0071f4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f4b8.md#insn-0071f4f0) · [`0071f4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071f/0071f4b8.md#insn-0071f4fc)
- 新版 [`0071f894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f868.md#insn-0071f894) · [`0071f8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f868.md#insn-0071f8a0) · [`0071f8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f868.md#insn-0071f8ac)

~~~diff
- 0071f4e4 ["INT_ADD", "register:40f0:8", ["const:71f4e4:8", "const:4:8"]]
- 0071f4e4 ["CALL", null, ["callee:00487c7c:8"]]
+ 0071f894 ["INT_ADD", "register:40f0:8", ["const:71f894:8", "const:4:8"]]
+ 0071f894 ["CALL", null, ["callee:00487c7c:8"]]
- 0071f4e4 bytes 1ea1f597
+ 0071f894 bytes faa0f597
- 0071f4f0 ["INT_ADD", "register:40f0:8", ["const:71f4f0:8", "const:4:8"]]
- 0071f4f0 ["CALL", null, ["callee:00487c9c:8"]]
+ 0071f8a0 ["INT_ADD", "register:40f0:8", ["const:71f8a0:8", "const:4:8"]]
+ 0071f8a0 ["CALL", null, ["callee:00487c9c:8"]]
- 0071f4f0 bytes 23a1f597
+ 0071f8a0 bytes ffa0f597
- 0071f4fc ["INT_ADD", "register:40f0:8", ["const:71f4fc:8", "const:4:8"]]
- 0071f4fc ["CALL", null, ["callee:005e8588:8"]]
+ 0071f8ac ["INT_ADD", "register:40f0:8", ["const:71f8ac:8", "const:4:8"]]
+ 0071f8ac ["CALL", null, ["callee:005e8588:8"]]
- 0071f4fc bytes 3723fb97
+ 0071f8ac bytes 3723fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

