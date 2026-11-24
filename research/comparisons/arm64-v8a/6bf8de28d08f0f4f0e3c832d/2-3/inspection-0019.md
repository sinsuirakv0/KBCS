# v16.0.2 → v16.0.3 · 要調査の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-26a30178cc420bde9d8f848e913149c4"></a>

### [`0073edc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073edc4.md) → [`0073f174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f174.md) FUN_0073f174

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0073d7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073d/0073d7fc.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`0073dbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073d/0073dbac.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0073ede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073edc4.md#insn-0073ede8) · [`0073ee30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073edc4.md#insn-0073ee30) · [`0073ee50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073edc4.md#insn-0073ee50)
- 新版 [`0073f198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f174.md#insn-0073f198) · [`0073f1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f174.md#insn-0073f1e0) · [`0073f200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f174.md#insn-0073f200)

~~~diff
- 0073ede8 ["INT_ADD", "register:40f0:8", ["const:73ede8:8", "const:4:8"]]
- 0073ede8 ["CALL", null, ["callee:00c59080:8"]]
+ 0073f198 ["INT_ADD", "register:40f0:8", ["const:73f198:8", "const:4:8"]]
+ 0073f198 ["CALL", null, ["callee:00c59080:8"]]
- 0073ede8 bytes b2641494
+ 0073f198 bytes ba671494
- 0073ee30 ["INT_ADD", "register:40f0:8", ["const:73ee30:8", "const:4:8"]]
- 0073ee30 ["CALL", null, ["callee:00c58f30:8"]]
+ 0073f1e0 ["INT_ADD", "register:40f0:8", ["const:73f1e0:8", "const:4:8"]]
+ 0073f1e0 ["CALL", null, ["callee:00c58f30:8"]]
- 0073ee30 bytes 4c641494
+ 0073f1e0 bytes 54671494
- 0073ee50 ["INT_ADD", "register:40f0:8", ["const:73ee50:8", "const:4:8"]]
- 0073ee50 ["CALL", null, ["callee:00c58fe0:8"]]
+ 0073f200 ["INT_ADD", "register:40f0:8", ["const:73f200:8", "const:4:8"]]
+ 0073f200 ["CALL", null, ["callee:00c58fe0:8"]]
- 0073ee50 bytes 70641494
+ 0073f200 bytes 78671494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba1a91cbbbf23b3256bb51d2c1615f57"></a>

### [`00741058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741058.md) → [`00741408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741408.md) FUN_00741408

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00740ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00740/00740ec0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00741270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741270.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00741068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741058.md#insn-00741068)
- 新版 [`00741418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741408.md#insn-00741418)

~~~diff
- 00741068 ["INT_ADD", "register:40f0:8", ["const:741068:8", "const:4:8"]]
- 00741068 ["CALL", null, ["callee:00741270:8"]]
+ 00741418 ["INT_ADD", "register:40f0:8", ["const:741418:8", "const:4:8"]]
+ 00741418 ["CALL", null, ["callee:00741270:8"]]
- 00741068 bytes 96ffff97
+ 00741418 bytes 96ffff97
~~~


<a id="compare-c11d77352758b9e1020b864dc932a2af"></a>

### [`0074107c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/0074107c.md) → [`0074142c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/0074142c.md) FUN_0074142c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`0073d7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073d/0073d7fc.md) [`0073ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073ee8c.md) [`00741628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741628.md) [`00742090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742090.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 8件 [`0073cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073c/0073cd40.md) [`0073dbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073d/0073dbac.md) [`0073f23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f23c.md) [`007419d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/007419d8.md) [`00742440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742440.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005e8588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e8/005e8588.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007410fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/0074107c.md#insn-007410fc) · [`00741130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/0074107c.md#insn-00741130) · [`0074113c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/0074107c.md#insn-0074113c)
- 新版 [`007414ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/0074142c.md#insn-007414ac) · [`007414e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/0074142c.md#insn-007414e0) · [`007414ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/0074142c.md#insn-007414ec)

~~~diff
- 007410fc ["INT_ADD", "register:40f0:8", ["const:7410fc:8", "const:4:8"]]
- 007410fc ["CALL", null, ["callee:00c58f30:8"]]
+ 007414ac ["INT_ADD", "register:40f0:8", ["const:7414ac:8", "const:4:8"]]
+ 007414ac ["CALL", null, ["callee:00c58f30:8"]]
- 007410fc bytes 995b1494
+ 007414ac bytes a15e1494
- 00741130 ["INT_ADD", "register:40f0:8", ["const:741130:8", "const:4:8"]]
- 00741130 ["CALL", null, ["callee:005e8588:8"]]
+ 007414e0 ["INT_ADD", "register:40f0:8", ["const:7414e0:8", "const:4:8"]]
+ 007414e0 ["CALL", null, ["callee:005e8588:8"]]
- 00741130 bytes 2a9cfa97
+ 007414e0 bytes 2a9cfa97
- 0074113c ["INT_ADD", "register:40f0:8", ["const:74113c:8", "const:4:8"]]
- 0074113c ["CALL", null, ["callee:005e8588:8"]]
+ 007414ec ["INT_ADD", "register:40f0:8", ["const:7414ec:8", "const:4:8"]]
+ 007414ec ["CALL", null, ["callee:005e8588:8"]]
- 0074113c bytes 279cfa97
+ 007414ec bytes 279cfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce3d259f025522d67db2a0a0f2fbfdf"></a>

### [`007411e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007411e8.md) → [`00741598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741598.md) FUN_00741598

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00741220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007411e8.md#insn-00741220)
- 新版 [`007415d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741598.md#insn-007415d0)

~~~diff
- 00741220 ["INT_ADD", "register:40f0:8", ["const:741220:8", "const:4:8"]]
- 00741220 ["CALL", null, ["callee:00c58f50:8"]]
+ 007415d0 ["INT_ADD", "register:40f0:8", ["const:7415d0:8", "const:4:8"]]
+ 007415d0 ["CALL", null, ["callee:00c58f50:8"]]
- 00741220 bytes 585b1494
+ 007415d0 bytes 605e1494
~~~


<a id="compare-38fcfd93ea73f6cb1efab965e14b104c"></a>

### [`007412d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007412d0.md) → [`00741680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741680.md) FUN_00741680

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0063678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00636/0063678c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0073cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073c/0073cd40.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00636b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00636/00636b3c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007412d0.md#insn-0074133c) · [`007413ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007412d0.md#insn-007413ac) · [`007413c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/007412d0.md#insn-007413c0)
- 新版 [`007416ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741680.md#insn-007416ec) · [`0074175c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741680.md#insn-0074175c) · [`00741770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00741/00741680.md#insn-00741770)

~~~diff
- 0074133c ["INT_ADD", "register:40f0:8", ["const:74133c:8", "const:4:8"]]
- 0074133c ["CALL", null, ["callee:00c58f30:8"]]
+ 007416ec ["INT_ADD", "register:40f0:8", ["const:7416ec:8", "const:4:8"]]
+ 007416ec ["CALL", null, ["callee:00c58f30:8"]]
- 0074133c bytes 095b1494
+ 007416ec bytes 115e1494
- 007413ac ["INT_ADD", "register:40f0:8", ["const:7413ac:8", "const:4:8"]]
- 007413ac ["CALL", null, ["callee:00c54d90:8"]]
+ 0074175c ["INT_ADD", "register:40f0:8", ["const:74175c:8", "const:4:8"]]
+ 0074175c ["CALL", null, ["callee:00c54d90:8"]]
- 007413ac bytes 7d4a1494
+ 0074175c bytes 8d4d1494
- 007413c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007413c0 ["INT_ADD", "register:40f0:8", ["const:7413c0:8", "const:4:8"]]
- 007413c0 ["CALLIND", null, ["register:0:8"]]
+ 00741770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00741770 ["INT_ADD", "register:40f0:8", ["const:741770:8", "const:4:8"]]
+ 00741770 ["CALLIND", null, ["register:0:8"]]
- 007413c0 bytes 00013fd6
+ 00741770 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d84792598660f1f94a21f1b13274fb98"></a>

### [`00742a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742a38.md) → [`00742de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742de8.md) FUN_00742de8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00742808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742808.md) [`007fa1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa1a0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00742bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742bb8.md) [`007fb104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fb104.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00742adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742a38.md#insn-00742adc) · [`00742b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742a38.md#insn-00742b14) · [`00742b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742a38.md#insn-00742b74)
- 新版 [`00742e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742de8.md#insn-00742e8c) · [`00742ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742de8.md#insn-00742ec4) · [`00742f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742de8.md#insn-00742f24)

~~~diff
- 00742adc ["INT_ADD", "register:40f0:8", ["const:742adc:8", "const:4:8"]]
- 00742adc ["CALL", null, ["callee:00c58f30:8"]]
+ 00742e8c ["INT_ADD", "register:40f0:8", ["const:742e8c:8", "const:4:8"]]
+ 00742e8c ["CALL", null, ["callee:00c58f30:8"]]
- 00742adc bytes 21551494
+ 00742e8c bytes 29581494
- 00742b14 ["INT_ADD", "register:40f0:8", ["const:742b14:8", "const:4:8"]]
- 00742b14 ["CALL", null, ["callee:0043bf04:8"]]
+ 00742ec4 ["INT_ADD", "register:40f0:8", ["const:742ec4:8", "const:4:8"]]
+ 00742ec4 ["CALL", null, ["callee:0043bf04:8"]]
- 00742b14 bytes 34e4f397
+ 00742ec4 bytes 10e4f397
- 00742b74 ["INT_ADD", "register:40f0:8", ["const:742b74:8", "const:4:8"]]
- 00742b74 ["CALL", null, ["callee:00c58f30:8"]]
+ 00742f24 ["INT_ADD", "register:40f0:8", ["const:742f24:8", "const:4:8"]]
+ 00742f24 ["CALL", null, ["callee:00c58f30:8"]]
- 00742b74 bytes fb541494
+ 00742f24 bytes 03581494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8a8832bec875eb1a849874b63498ec"></a>

### [`00743de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md) → [`00744198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744198.md) FUN_00744198

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`007fa1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa1a0.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 14件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c127c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md) [`007599e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00759/007599e4.md) [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) [`007fb104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fb104.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md#insn-00743e4c) · [`00743e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md#insn-00743e84)
- 新版 [`007441fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744198.md#insn-007441fc) · [`00744234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744198.md#insn-00744234)

~~~diff
- 00743e4c ["INT_ADD", "register:40f0:8", ["const:743e4c:8", "const:4:8"]]
- 00743e4c ["CALL", null, ["callee:00c58f30:8"]]
+ 007441fc ["INT_ADD", "register:40f0:8", ["const:7441fc:8", "const:4:8"]]
+ 007441fc ["CALL", null, ["callee:00c58f30:8"]]
- 00743e4c bytes 45501494
+ 007441fc bytes 4d531494
- 00743e84 ["INT_ADD", "register:40f0:8", ["const:743e84:8", "const:4:8"]]
- 00743e84 ["CALL", null, ["callee:0043bf04:8"]]
+ 00744234 ["INT_ADD", "register:40f0:8", ["const:744234:8", "const:4:8"]]
+ 00744234 ["CALL", null, ["callee:0043bf04:8"]]
- 00743e84 bytes 58dff397
+ 00744234 bytes 34dff397
~~~


<a id="compare-725ae4e7370bfdcba569aef3150478dc"></a>

### [`00743eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743eb4.md) → [`00744264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744264.md) FUN_00744264

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) [`007fbe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fbe60.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`007fb94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fb94c.md) [`007fcdc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fc/007fcdc4.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743eb4.md#insn-00743f1c) · [`00743f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743eb4.md#insn-00743f54)
- 新版 [`007442cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744264.md#insn-007442cc) · [`00744304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744264.md#insn-00744304)

~~~diff
- 00743f1c ["INT_ADD", "register:40f0:8", ["const:743f1c:8", "const:4:8"]]
- 00743f1c ["CALL", null, ["callee:00c58f30:8"]]
+ 007442cc ["INT_ADD", "register:40f0:8", ["const:7442cc:8", "const:4:8"]]
+ 007442cc ["CALL", null, ["callee:00c58f30:8"]]
- 00743f1c bytes 11501494
+ 007442cc bytes 19531494
- 00743f54 ["INT_ADD", "register:40f0:8", ["const:743f54:8", "const:4:8"]]
- 00743f54 ["CALL", null, ["callee:0043bf04:8"]]
+ 00744304 ["INT_ADD", "register:40f0:8", ["const:744304:8", "const:4:8"]]
+ 00744304 ["CALL", null, ["callee:0043bf04:8"]]
- 00743f54 bytes 24dff397
+ 00744304 bytes 00dff397
~~~


<a id="compare-3ad040292a9d15bf331a75b1f3dc418d"></a>

### [`00743f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743f84.md) → [`00744334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744334.md) FUN_00744334

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) [`00adf100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf100.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 8件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c127c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md) [`00ad7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7aec.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) [`00ae00f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae0/00ae00f4.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00743fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743f84.md#insn-00743fe8) · [`00744020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743f84.md#insn-00744020)
- 新版 [`00744398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744334.md#insn-00744398) · [`007443d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744334.md#insn-007443d0)

~~~diff
- 00743fe8 ["INT_ADD", "register:40f0:8", ["const:743fe8:8", "const:4:8"]]
- 00743fe8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00744398 ["INT_ADD", "register:40f0:8", ["const:744398:8", "const:4:8"]]
+ 00744398 ["CALL", null, ["callee:00c58f30:8"]]
- 00743fe8 bytes de4f1494
+ 00744398 bytes e6521494
- 00744020 ["INT_ADD", "register:40f0:8", ["const:744020:8", "const:4:8"]]
- 00744020 ["CALL", null, ["callee:0043bf04:8"]]
+ 007443d0 ["INT_ADD", "register:40f0:8", ["const:7443d0:8", "const:4:8"]]
+ 007443d0 ["CALL", null, ["callee:0043bf04:8"]]
- 00744020 bytes f1def397
+ 007443d0 bytes cddef397
~~~


<a id="compare-c38875d9f785492ae424bcc2b6671a09"></a>

### [`00744048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744048.md) → [`007443f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007443f8.md) FUN_007443f8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) [`00aea3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea3f0.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00ad19bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad19bc.md) [`00aeb3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb3e4.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744048.md#insn-00744074) · [`00744110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744048.md#insn-00744110) · [`00744148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744048.md#insn-00744148)
- 新版 [`00744424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007443f8.md#insn-00744424) · [`007444c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007443f8.md#insn-007444c0) · [`007444f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007443f8.md#insn-007444f8)

~~~diff
- 00744074 ["INT_ADD", "register:40f0:8", ["const:744074:8", "const:4:8"]]
- 00744074 ["CALL", null, ["callee:008524fc:8"]]
+ 00744424 ["INT_ADD", "register:40f0:8", ["const:744424:8", "const:4:8"]]
+ 00744424 ["CALL", null, ["callee:008524fc:8"]]
- 00744074 bytes 37350494
+ 00744424 bytes 36380494
- 00744110 ["INT_ADD", "register:40f0:8", ["const:744110:8", "const:4:8"]]
- 00744110 ["CALL", null, ["callee:00c58f30:8"]]
+ 007444c0 ["INT_ADD", "register:40f0:8", ["const:7444c0:8", "const:4:8"]]
+ 007444c0 ["CALL", null, ["callee:00c58f30:8"]]
- 00744110 bytes 944f1494
+ 007444c0 bytes 9c521494
- 00744148 ["INT_ADD", "register:40f0:8", ["const:744148:8", "const:4:8"]]
- 00744148 ["CALL", null, ["callee:0043bf04:8"]]
+ 007444f8 ["INT_ADD", "register:40f0:8", ["const:7444f8:8", "const:4:8"]]
+ 007444f8 ["CALL", null, ["callee:0043bf04:8"]]
- 00744148 bytes a7def397
+ 007444f8 bytes 83def397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b60b8bd42cc3b2be0b3615b9672f2c7"></a>

### [`007441f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/007441f0.md) → [`007445a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007445a0.md) FUN_007445a0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) [`007faf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007faf94.md) [`007fb288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb288.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 8件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007fb94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fb94c.md) [`007fbef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fbef8.md) [`007fc1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fc/007fc1ec.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/007441f0.md#insn-00744200)
- 新版 [`007445b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007445a0.md#insn-007445b0)

~~~diff
- 00744200 ["INT_ADD", "register:40f0:8", ["const:744200:8", "const:4:8"]]
- 00744200 ["CALL", null, ["callee:008524fc:8"]]
+ 007445b0 ["INT_ADD", "register:40f0:8", ["const:7445b0:8", "const:4:8"]]
+ 007445b0 ["CALL", null, ["callee:008524fc:8"]]
- 00744200 bytes d4340494
+ 007445b0 bytes d3370494
~~~


<a id="compare-f92cb99e70854cc9ba5a01544bd558cd"></a>

### [`00744260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md) → [`00744610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md) FUN_00744610

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 60件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0ecc.md) [`005e4720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4720.md) [`005e4824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4824.md) [`005e4888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4888.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 60件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c127c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c127c.md) [`005e4ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e4ad0.md) [`005e4bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e4bd4.md) [`005e4c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e4c38.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md#insn-00744270)
- 新版 [`00744620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md#insn-00744620)

~~~diff
- 00744270 ["INT_ADD", "register:40f0:8", ["const:744270:8", "const:4:8"]]
- 00744270 ["CALL", null, ["callee:008524fc:8"]]
+ 00744620 ["INT_ADD", "register:40f0:8", ["const:744620:8", "const:4:8"]]
+ 00744620 ["CALL", null, ["callee:008524fc:8"]]
- 00744270 bytes b8340494
+ 00744620 bytes b7370494
~~~


<a id="compare-8fdcaa25696d60afe6adc66eddb5a678"></a>

### [`00744db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744db4.md) → [`00745164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745164.md) FUN_00745164

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00744dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744db4.md#insn-00744dec) · [`00744e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744db4.md#insn-00744e0c) · [`00744ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744db4.md#insn-00744ea4)
- 新版 [`0074519c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745164.md#insn-0074519c) · [`007451bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745164.md#insn-007451bc) · [`00745254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745164.md#insn-00745254)

~~~diff
- 00744dec ["INT_ADD", "register:40f0:8", ["const:744dec:8", "const:4:8"]]
- 00744dec ["CALL", null, ["callee:0043bf04:8"]]
+ 0074519c ["INT_ADD", "register:40f0:8", ["const:74519c:8", "const:4:8"]]
+ 0074519c ["CALL", null, ["callee:0043bf04:8"]]
- 00744dec bytes 7edbf397
+ 0074519c bytes 5adbf397
- 00744e0c ["INT_ADD", "register:40f0:8", ["const:744e0c:8", "const:4:8"]]
- 00744e0c ["CALL", null, ["callee:008524fc:8"]]
+ 007451bc ["INT_ADD", "register:40f0:8", ["const:7451bc:8", "const:4:8"]]
+ 007451bc ["CALL", null, ["callee:008524fc:8"]]
- 00744e0c bytes d1310494
+ 007451bc bytes d0340494
- 00744ea4 ["INT_ADD", "register:40f0:8", ["const:744ea4:8", "const:4:8"]]
- 00744ea4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00745254 ["INT_ADD", "register:40f0:8", ["const:745254:8", "const:4:8"]]
+ 00745254 ["CALL", null, ["callee:00c58f30:8"]]
- 00744ea4 bytes 2f4c1494
+ 00745254 bytes 374f1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69002751ff0d8cde6209738d8af04281"></a>

### [`00744fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fe4.md) → [`00745394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745394.md) FUN_00745394

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00480478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480478.md) [`004804d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/004804d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074500c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fe4.md#insn-0074500c) · [`00745018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fe4.md#insn-00745018) · [`00745028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744fe4.md#insn-00745028)
- 新版 [`007453bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745394.md#insn-007453bc) · [`007453c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745394.md#insn-007453c8) · [`007453d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745394.md#insn-007453d8)

~~~diff
- 0074500c ["INT_ADD", "register:40f0:8", ["const:74500c:8", "const:4:8"]]
- 0074500c ["CALL", null, ["callee:00480538:8"]]
+ 007453bc ["INT_ADD", "register:40f0:8", ["const:7453bc:8", "const:4:8"]]
+ 007453bc ["CALL", null, ["callee:00480538:8"]]
- 0074500c bytes 83ecf497
+ 007453bc bytes 5fecf497
- 00745018 ["INT_ADD", "register:40f0:8", ["const:745018:8", "const:4:8"]]
- 00745018 ["CALL", null, ["callee:004804d8:8"]]
+ 007453c8 ["INT_ADD", "register:40f0:8", ["const:7453c8:8", "const:4:8"]]
+ 007453c8 ["CALL", null, ["callee:004804d8:8"]]
- 00745018 bytes 68ecf497
+ 007453c8 bytes 44ecf497
- 00745028 ["INT_ADD", "register:40f0:8", ["const:745028:8", "const:4:8"]]
- 00745028 ["CALL", null, ["callee:00480478:8"]]
+ 007453d8 ["INT_ADD", "register:40f0:8", ["const:7453d8:8", "const:4:8"]]
+ 007453d8 ["CALL", null, ["callee:00480478:8"]]
- 00745028 bytes 4cecf497
+ 007453d8 bytes 28ecf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0bc2a9afa19699c24b81c93a97dc37"></a>

### [`0074548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md) → [`0074583c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/0074583c.md) FUN_0074583c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 4件 [`00480e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480e98.md) [`00480ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`00480f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480f48.md) [`004810a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007454b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md#insn-007454b0) · [`007454bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md#insn-007454bc) · [`007454c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/0074548c.md#insn-007454c8)
- 新版 [`00745860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/0074583c.md#insn-00745860) · [`0074586c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/0074583c.md#insn-0074586c) · [`00745878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/0074583c.md#insn-00745878)

~~~diff
- 007454b0 ["INT_ADD", "register:40f0:8", ["const:7454b0:8", "const:4:8"]]
- 007454b0 ["CALL", null, ["callee:00480f48:8"]]
+ 00745860 ["INT_ADD", "register:40f0:8", ["const:745860:8", "const:4:8"]]
+ 00745860 ["CALL", null, ["callee:00480f48:8"]]
- 007454b0 bytes deedf497
+ 00745860 bytes baedf497
- 007454bc ["INT_ADD", "register:40f0:8", ["const:7454bc:8", "const:4:8"]]
- 007454bc ["CALL", null, ["callee:00480ef0:8"]]
+ 0074586c ["INT_ADD", "register:40f0:8", ["const:74586c:8", "const:4:8"]]
+ 0074586c ["CALL", null, ["callee:00480ef0:8"]]
- 007454bc bytes c5edf497
+ 0074586c bytes a1edf497
- 007454c8 ["INT_ADD", "register:40f0:8", ["const:7454c8:8", "const:4:8"]]
- 007454c8 ["CALL", null, ["callee:00480e98:8"]]
+ 00745878 ["INT_ADD", "register:40f0:8", ["const:745878:8", "const:4:8"]]
+ 00745878 ["CALL", null, ["callee:00480e98:8"]]
- 007454c8 bytes acedf497
+ 00745878 bytes 88edf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085a180359efb84a27759f94e7923913"></a>

### [`00745988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md) → [`00745d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745d38.md) FUN_00745d38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00745824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745824.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 2件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00a33c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33c70.md)
- 新版 呼出元 2件 [`00745bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745bd4.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 2件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00a34c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a34/00a34c64.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074599c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md#insn-0074599c) · [`007459a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md#insn-007459a8) · [`007459b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745988.md#insn-007459b4)
- 新版 [`00745d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745d38.md#insn-00745d4c) · [`00745d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745d38.md#insn-00745d58) · [`00745d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745d38.md#insn-00745d64)

~~~diff
- 0074599c ["INT_ADD", "register:40f0:8", ["const:74599c:8", "const:4:8"]]
- 0074599c ["CALL", null, ["callee:0048d1e4:8"]]
+ 00745d4c ["INT_ADD", "register:40f0:8", ["const:745d4c:8", "const:4:8"]]
+ 00745d4c ["CALL", null, ["callee:0048d1e4:8"]]
- 0074599c bytes 4a1df597
+ 00745d4c bytes 261df597
- 007459a8 ["INT_ADD", "register:40f0:8", ["const:7459a8:8", "const:4:8"]]
- 007459a8 ["CALL", null, ["callee:00a34c64:8"]]
+ 00745d58 ["INT_ADD", "register:40f0:8", ["const:745d58:8", "const:4:8"]]
+ 00745d58 ["CALL", null, ["callee:00a34c64:8"]]
- 007459a8 bytes b2b80b94
+ 00745d58 bytes c3bb0b94
- 007459b4 ["INT_ADD", "register:40f0:8", ["const:7459b4:8", "const:4:8"]]
- 007459b4 ["CALL", null, ["callee:0048d1e4:8"]]
+ 00745d64 ["INT_ADD", "register:40f0:8", ["const:745d64:8", "const:4:8"]]
+ 00745d64 ["CALL", null, ["callee:0048d1e4:8"]]
- 007459b4 bytes 441df597
+ 00745d64 bytes 201df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1099ba0061b1f94578899cb7c0f22956"></a>

### [`00746944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746944.md) → [`00746cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/00746cf4.md) FUN_00746cf4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 4件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00664bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664bb0.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007469a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746944.md#insn-007469a0) · [`007469c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746944.md#insn-007469c0) · [`00746a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746944.md#insn-00746a18)
- 新版 [`00746d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/00746cf4.md#insn-00746d50) · [`00746d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/00746cf4.md#insn-00746d70) · [`00746dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/00746cf4.md#insn-00746dc8)

~~~diff
- 007469a0 ["INT_ADD", "register:40f0:8", ["const:7469a0:8", "const:4:8"]]
- 007469a0 ["CALL", null, ["callee:0043bf04:8"]]
+ 00746d50 ["INT_ADD", "register:40f0:8", ["const:746d50:8", "const:4:8"]]
+ 00746d50 ["CALL", null, ["callee:0043bf04:8"]]
- 007469a0 bytes 91d4f397
+ 00746d50 bytes 6dd4f397
- 007469c0 ["INT_ADD", "register:40f0:8", ["const:7469c0:8", "const:4:8"]]
- 007469c0 ["CALL", null, ["callee:008524fc:8"]]
+ 00746d70 ["INT_ADD", "register:40f0:8", ["const:746d70:8", "const:4:8"]]
+ 00746d70 ["CALL", null, ["callee:008524fc:8"]]
- 007469c0 bytes e42a0494
+ 00746d70 bytes e32d0494
- 00746a18 ["INT_ADD", "register:40f0:8", ["const:746a18:8", "const:4:8"]]
- 00746a18 ["CALL", null, ["callee:008524fc:8"]]
+ 00746dc8 ["INT_ADD", "register:40f0:8", ["const:746dc8:8", "const:4:8"]]
+ 00746dc8 ["CALL", null, ["callee:008524fc:8"]]
- 00746a18 bytes ce2a0494
+ 00746dc8 bytes cd2d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a8d07ba3ac296c94f3fe8df0c18ad3"></a>

### [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) → [`00747664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md) FUN_00747664

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 6件 [`00748fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md) [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 6件 [`00749350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md) [`0074aa5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aa5c.md) [`0074aadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md#insn-00747338) · [`0074735c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md#insn-0074735c) · [`007473a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md#insn-007473a4)
- 新版 [`007476e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md#insn-007476e8) · [`0074770c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md#insn-0074770c) · [`00747754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md#insn-00747754)

~~~diff
- 00747338 ["INT_ADD", "register:40f0:8", ["const:747338:8", "const:4:8"]]
- 00747338 ["CALL", null, ["callee:00c58f30:8"]]
+ 007476e8 ["INT_ADD", "register:40f0:8", ["const:7476e8:8", "const:4:8"]]
+ 007476e8 ["CALL", null, ["callee:00c58f30:8"]]
- 00747338 bytes 0a431494
+ 007476e8 bytes 12461494
- 0074735c ["INT_ADD", "register:40f0:8", ["const:74735c:8", "const:4:8"]]
- 0074735c ["CALL", null, ["callee:0074aadc:8"]]
+ 0074770c ["INT_ADD", "register:40f0:8", ["const:74770c:8", "const:4:8"]]
+ 0074770c ["CALL", null, ["callee:0074aadc:8"]]
- 0074735c bytes f40c0094
+ 0074770c bytes f40c0094
- 007473a4 ["INT_ADD", "register:40f0:8", ["const:7473a4:8", "const:4:8"]]
- 007473a4 ["CALL", null, ["callee:00749350:8"]]
+ 00747754 ["INT_ADD", "register:40f0:8", ["const:747754:8", "const:4:8"]]
+ 00747754 ["CALL", null, ["callee:00749350:8"]]
- 007473a4 bytes ff060094
+ 00747754 bytes ff060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0ac8ff62cf1bd0f96c85ec17d89c9b"></a>

### [`00747648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747648.md) → [`007479f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007479f8.md) FUN_007479f8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0060eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060eb90.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 9件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468f8c.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md)
- 新版 呼出元 2件 [`0060ef40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060e/0060ef40.md) [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) · 呼出先 9件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692ac.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md) [`0046ddbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046ddbc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747648.md#insn-00747694) · [`007476ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747648.md#insn-007476ac) · [`007476bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747648.md#insn-007476bc)
- 新版 [`00747a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007479f8.md#insn-00747a44) · [`00747a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007479f8.md#insn-00747a5c) · [`00747a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007479f8.md#insn-00747a6c)

~~~diff
- 00747694 ["INT_ADD", "register:40f0:8", ["const:747694:8", "const:4:8"]]
- 00747694 ["CALL", null, ["callee:00467bc0:8"]]
+ 00747a44 ["INT_ADD", "register:40f0:8", ["const:747a44:8", "const:4:8"]]
+ 00747a44 ["CALL", null, ["callee:00467bc0:8"]]
- 00747694 bytes 8380f497
+ 00747a44 bytes 5f80f497
- 007476ac ["INT_ADD", "register:40f0:8", ["const:7476ac:8", "const:4:8"]]
- 007476ac ["CALL", null, ["callee:004692e8:8"]]
+ 00747a5c ["INT_ADD", "register:40f0:8", ["const:747a5c:8", "const:4:8"]]
+ 00747a5c ["CALL", null, ["callee:004692e8:8"]]
- 007476ac bytes 4786f497
+ 00747a5c bytes 2386f497
- 007476bc ["INT_ADD", "register:40f0:8", ["const:7476bc:8", "const:4:8"]]
- 007476bc ["CALL", null, ["callee:008015e8:8"]]
+ 00747a6c ["INT_ADD", "register:40f0:8", ["const:747a6c:8", "const:4:8"]]
+ 00747a6c ["CALL", null, ["callee:008015e8:8"]]
- 007476bc bytes f2e30294
+ 00747a6c bytes dfe60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2121158e83e5a865a71c7aff9be0898f"></a>

### [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) → [`00747c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md) FUN_00747c0c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00742c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00742/00742c10.md) [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008493c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008493c8.md) · 呼出先 2件 [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`00742fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00742/00742fc0.md) [`00747c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084a374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084a374.md) · 呼出先 2件 [`00747c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md#insn-00747878) · [`00747884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md#insn-00747884) · [`00747894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md#insn-00747894)
- 新版 [`00747c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md#insn-00747c28) · [`00747c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md#insn-00747c34) · [`00747c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747c0c.md#insn-00747c44)

~~~diff
- 00747878 ["INT_ADD", "register:40f0:8", ["const:747878:8", "const:4:8"]]
- 00747878 ["CALL", null, ["local:b0:8"]]
+ 00747c28 ["INT_ADD", "register:40f0:8", ["const:747c28:8", "const:4:8"]]
+ 00747c28 ["CALL", null, ["local:b0:8"]]
- 00747878 bytes f9ffff97
+ 00747c28 bytes f9ffff97
- 00747884 ["INT_ADD", "register:40f0:8", ["const:747884:8", "const:4:8"]]
- 00747884 ["CALL", null, ["local:b0:8"]]
+ 00747c34 ["INT_ADD", "register:40f0:8", ["const:747c34:8", "const:4:8"]]
+ 00747c34 ["CALL", null, ["local:b0:8"]]
- 00747884 bytes f6ffff97
+ 00747c34 bytes f6ffff97
- 00747894 ["INT_ADD", "register:40f0:8", ["const:747894:8", "const:4:8"]]
- 00747894 ["CALL", null, ["callee:00c58f50:8"]]
+ 00747c44 ["INT_ADD", "register:40f0:8", ["const:747c44:8", "const:4:8"]]
+ 00747c44 ["CALL", null, ["callee:00c58f50:8"]]
- 00747894 bytes bb411494
+ 00747c44 bytes c3441494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151efb45c25fb31b18e465b368e982a6"></a>

### [`00747ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747ab8.md) → [`00747e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747e68.md) FUN_00747e68

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745a7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00745e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745e2c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747ab8.md#insn-00747af4)
- 新版 [`00747ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747e68.md#insn-00747ea4)

~~~diff
- 00747af4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00747af4 ["INT_ADD", "register:40f0:8", ["const:747af4:8", "const:4:8"]]
- 00747af4 ["CALLIND", null, ["register:0:8"]]
+ 00747ea4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00747ea4 ["INT_ADD", "register:40f0:8", ["const:747ea4:8", "const:4:8"]]
+ 00747ea4 ["CALLIND", null, ["register:0:8"]]
- 00747af4 bytes 00013fd6
+ 00747ea4 bytes 00013fd6
~~~


<a id="compare-538a525f71cb85f7b5b22d5c72b4db18"></a>

### [`00747f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f34.md) → [`007482e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007482e4.md) FUN_007482e4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00745a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745a7c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00745e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745e2c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f34.md#insn-00747f70)
- 新版 [`00748320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007482e4.md#insn-00748320)

~~~diff
- 00747f70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00747f70 ["INT_ADD", "register:40f0:8", ["const:747f70:8", "const:4:8"]]
- 00747f70 ["CALLIND", null, ["register:0:8"]]
+ 00748320 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748320 ["INT_ADD", "register:40f0:8", ["const:748320:8", "const:4:8"]]
+ 00748320 ["CALLIND", null, ["register:0:8"]]
- 00747f70 bytes 00013fd6
+ 00748320 bytes 00013fd6
~~~


<a id="compare-8d2a7f3bae31de72182b2f8f2bf391ac"></a>

### [`00747f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f84.md) → [`00748334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748334.md) FUN_00748334

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00747fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f84.md#insn-00747fbc) · [`00747ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f84.md#insn-00747ff0) · [`00747ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747f84.md#insn-00747ff4)
- 新版 [`0074836c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748334.md#insn-0074836c) · [`007483a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748334.md#insn-007483a0) · [`007483a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748334.md#insn-007483a4)

~~~diff
- 00747fbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00747fbc ["INT_ADD", "register:40f0:8", ["const:747fbc:8", "const:4:8"]]
- 00747fbc ["CALLIND", null, ["register:0:8"]]
+ 0074836c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074836c ["INT_ADD", "register:40f0:8", ["const:74836c:8", "const:4:8"]]
+ 0074836c ["CALLIND", null, ["register:0:8"]]
- 00747fbc bytes 00013fd6
+ 0074836c bytes 00013fd6
- 00747ff0 ["INT_ADD", "register:40f0:8", ["const:747ff0:8", "const:4:8"]]
- 00747ff0 ["CALL", null, ["callee:0045a0d4:8"]]
+ 007483a0 ["INT_ADD", "register:40f0:8", ["const:7483a0:8", "const:4:8"]]
+ 007483a0 ["CALL", null, ["callee:0045a0d4:8"]]
- 00747ff0 bytes 7147f497
+ 007483a0 bytes 4d47f497
- 00747ff4 ["INT_ADD", "register:40f0:8", ["const:747ff4:8", "const:4:8"]]
- 00747ff4 ["CALL", null, ["callee:00c58f80:8"]]
+ 007483a4 ["INT_ADD", "register:40f0:8", ["const:7483a4:8", "const:4:8"]]
+ 007483a4 ["CALL", null, ["callee:00c58f80:8"]]
- 00747ff4 bytes ef3f1494
+ 007483a4 bytes f7421494
~~~


<a id="compare-2cc580999973ab2b3e3599b9e8e88472"></a>

### [`00748214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748214.md) → [`007485c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007485c4.md) FUN_007485c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0074600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074600c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007463bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/007463bc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748214.md#insn-00748250)
- 新版 [`00748600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/007485c4.md#insn-00748600)

~~~diff
- 00748250 ["COPY", "register:0:8", ["register:4040:8"]]
- 00748250 ["INT_ADD", "register:40f0:8", ["const:748250:8", "const:4:8"]]
- 00748250 ["CALLIND", null, ["register:0:8"]]
+ 00748600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748600 ["INT_ADD", "register:40f0:8", ["const:748600:8", "const:4:8"]]
+ 00748600 ["CALLIND", null, ["register:0:8"]]
- 00748250 bytes 00013fd6
+ 00748600 bytes 00013fd6
~~~


<a id="compare-d8d130b822fdb31d1f1b7a468fe25761"></a>

### [`007486d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007486d0.md) → [`00748a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748a80.md) FUN_00748a80

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0074600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074600c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007463bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/007463bc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/007486d0.md#insn-0074870c)
- 新版 [`00748abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748a80.md#insn-00748abc)

~~~diff
- 0074870c ["COPY", "register:0:8", ["register:4040:8"]]
- 0074870c ["INT_ADD", "register:40f0:8", ["const:74870c:8", "const:4:8"]]
- 0074870c ["CALLIND", null, ["register:0:8"]]
+ 00748abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748abc ["INT_ADD", "register:40f0:8", ["const:748abc:8", "const:4:8"]]
+ 00748abc ["CALLIND", null, ["register:0:8"]]
- 0074870c bytes 00013fd6
+ 00748abc bytes 00013fd6
~~~


<a id="compare-3e66506db1f9d6a55dc5480069cf10e8"></a>

### [`00748720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748720.md) → [`00748ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ad0.md) FUN_00748ad0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748720.md#insn-00748760) · [`00748794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748720.md#insn-00748794) · [`00748798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748720.md#insn-00748798)
- 新版 [`00748b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ad0.md#insn-00748b10) · [`00748b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ad0.md#insn-00748b44) · [`00748b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748ad0.md#insn-00748b48)

~~~diff
- 00748760 ["COPY", "register:0:8", ["register:4040:8"]]
- 00748760 ["INT_ADD", "register:40f0:8", ["const:748760:8", "const:4:8"]]
- 00748760 ["CALLIND", null, ["register:0:8"]]
+ 00748b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00748b10 ["INT_ADD", "register:40f0:8", ["const:748b10:8", "const:4:8"]]
+ 00748b10 ["CALLIND", null, ["register:0:8"]]
- 00748760 bytes 00013fd6
+ 00748b10 bytes 00013fd6
- 00748794 ["INT_ADD", "register:40f0:8", ["const:748794:8", "const:4:8"]]
- 00748794 ["CALL", null, ["callee:0045a0d4:8"]]
+ 00748b44 ["INT_ADD", "register:40f0:8", ["const:748b44:8", "const:4:8"]]
+ 00748b44 ["CALL", null, ["callee:0045a0d4:8"]]
- 00748794 bytes 8845f497
+ 00748b44 bytes 6445f497
- 00748798 ["INT_ADD", "register:40f0:8", ["const:748798:8", "const:4:8"]]
- 00748798 ["CALL", null, ["callee:00c58f80:8"]]
+ 00748b48 ["INT_ADD", "register:40f0:8", ["const:748b48:8", "const:4:8"]]
+ 00748b48 ["CALL", null, ["callee:00c58f80:8"]]
- 00748798 bytes 063e1494
+ 00748b48 bytes 0e411494
~~~


<a id="compare-80bb4920dac2a8921c765be7f5027d94"></a>

### [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) → [`00748f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md) FUN_00748f38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) [`00748d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md) [`00748fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fb4.md) [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 7件 [`007470f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007470f4.md) [`0074912c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md) [`00749364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749364.md) [`0074aa5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aa5c.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md#insn-00748ba8) · [`00748be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md#insn-00748be4) · [`00748bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md#insn-00748bf4)
- 新版 [`00748f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md#insn-00748f58) · [`00748f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md#insn-00748f94) · [`00748fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md#insn-00748fa4)

~~~diff
- 00748ba8 ["INT_ADD", "register:40f0:8", ["const:748ba8:8", "const:4:8"]]
- 00748ba8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00748f58 ["INT_ADD", "register:40f0:8", ["const:748f58:8", "const:4:8"]]
+ 00748f58 ["CALL", null, ["callee:00c58f50:8"]]
- 00748ba8 bytes f63c1494
+ 00748f58 bytes fe3f1494
- 00748be4 ["INT_ADD", "register:40f0:8", ["const:748be4:8", "const:4:8"]]
- 00748be4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00748f94 ["INT_ADD", "register:40f0:8", ["const:748f94:8", "const:4:8"]]
+ 00748f94 ["CALL", null, ["callee:00c58f50:8"]]
- 00748be4 bytes e73c1494
+ 00748f94 bytes ef3f1494
- 00748bf4 ["INT_ADD", "register:40f0:8", ["const:748bf4:8", "const:4:8"]]
- 00748bf4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00748fa4 ["INT_ADD", "register:40f0:8", ["const:748fa4:8", "const:4:8"]]
+ 00748fa4 ["CALL", null, ["callee:00c58f50:8"]]
- 00748bf4 bytes e33c1494
+ 00748fa4 bytes eb3f1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18ede36b353e26c834229e9b452b24f4"></a>

### [`00748c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748c34.md) → [`00748fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748fe4.md) FUN_00748fe4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748c34.md#insn-00748c54) · [`00748c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748c34.md#insn-00748c90) · [`00748ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748c34.md#insn-00748ca0)
- 新版 [`00749004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748fe4.md#insn-00749004) · [`00749040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748fe4.md#insn-00749040) · [`00749050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748fe4.md#insn-00749050)

~~~diff
- 00748c54 ["INT_ADD", "register:40f0:8", ["const:748c54:8", "const:4:8"]]
- 00748c54 ["CALL", null, ["callee:00c58f50:8"]]
+ 00749004 ["INT_ADD", "register:40f0:8", ["const:749004:8", "const:4:8"]]
+ 00749004 ["CALL", null, ["callee:00c58f50:8"]]
- 00748c54 bytes cb3c1494
+ 00749004 bytes d33f1494
- 00748c90 ["INT_ADD", "register:40f0:8", ["const:748c90:8", "const:4:8"]]
- 00748c90 ["CALL", null, ["callee:00c58f50:8"]]
+ 00749040 ["INT_ADD", "register:40f0:8", ["const:749040:8", "const:4:8"]]
+ 00749040 ["CALL", null, ["callee:00c58f50:8"]]
- 00748c90 bytes bc3c1494
+ 00749040 bytes c43f1494
- 00748ca0 ["INT_ADD", "register:40f0:8", ["const:748ca0:8", "const:4:8"]]
- 00748ca0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00749050 ["INT_ADD", "register:40f0:8", ["const:749050:8", "const:4:8"]]
+ 00749050 ["CALL", null, ["callee:00c58f50:8"]]
- 00748ca0 bytes b83c1494
+ 00749050 bytes c03f1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9241b1de2eb4d3dbe2be8dd7f4cfcb"></a>

### [`00748ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748ce0.md) → [`00749090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749090.md) FUN_00749090

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`009ab624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748ce0.md#insn-00748d2c) · [`00748d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748ce0.md#insn-00748d3c) · [`00748d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748ce0.md#insn-00748d4c)
- 新版 [`007490dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749090.md#insn-007490dc) · [`007490ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749090.md#insn-007490ec) · [`007490fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749090.md#insn-007490fc)

~~~diff
- 00748d2c ["INT_ADD", "register:40f0:8", ["const:748d2c:8", "const:4:8"]]
- 00748d2c ["CALL", null, ["callee:00c58f50:8"]]
+ 007490dc ["INT_ADD", "register:40f0:8", ["const:7490dc:8", "const:4:8"]]
+ 007490dc ["CALL", null, ["callee:00c58f50:8"]]
- 00748d2c bytes 953c1494
+ 007490dc bytes 9d3f1494
- 00748d3c ["INT_ADD", "register:40f0:8", ["const:748d3c:8", "const:4:8"]]
- 00748d3c ["CALL", null, ["callee:00c58f50:8"]]
+ 007490ec ["INT_ADD", "register:40f0:8", ["const:7490ec:8", "const:4:8"]]
+ 007490ec ["CALL", null, ["callee:00c58f50:8"]]
- 00748d3c bytes 913c1494
+ 007490ec bytes 993f1494
- 00748d4c ["INT_ADD", "register:40f0:8", ["const:748d4c:8", "const:4:8"]]
- 00748d4c ["CALL", null, ["callee:00c58f50:8"]]
+ 007490fc ["INT_ADD", "register:40f0:8", ["const:7490fc:8", "const:4:8"]]
+ 007490fc ["CALL", null, ["callee:00c58f50:8"]]
- 00748d4c bytes 8d3c1494
+ 007490fc bytes 953f1494
~~~


<a id="compare-e670b2d08aba9a4e55165e965a04912f"></a>

### [`00748d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md) → [`0074912c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md) FUN_0074912c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00749a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749a2c.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00748fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fa0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00749ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749ddc.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00748f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md) [`00749350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md#insn-00748e1c) · [`00748f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md#insn-00748f54) · [`00748f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748d7c.md#insn-00748f78)
- 新版 [`007491cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md#insn-007491cc) · [`00749304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md#insn-00749304) · [`00749328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/0074912c.md#insn-00749328)

~~~diff
- 00748e1c ["INT_ADD", "register:40f0:8", ["const:748e1c:8", "const:4:8"]]
- 00748e1c ["CALL", null, ["callee:00c58f30:8"]]
+ 007491cc ["INT_ADD", "register:40f0:8", ["const:7491cc:8", "const:4:8"]]
+ 007491cc ["CALL", null, ["callee:00c58f30:8"]]
- 00748e1c bytes 513c1494
+ 007491cc bytes 593f1494
- 00748f54 ["INT_ADD", "register:40f0:8", ["const:748f54:8", "const:4:8"]]
- 00748f54 ["CALL", null, ["callee:00748f38:8"]]
+ 00749304 ["INT_ADD", "register:40f0:8", ["const:749304:8", "const:4:8"]]
+ 00749304 ["CALL", null, ["callee:00748f38:8"]]
- 00748f54 bytes 0dffff97
+ 00749304 bytes 0dffff97
- 00748f78 ["INT_ADD", "register:40f0:8", ["const:748f78:8", "const:4:8"]]
- 00748f78 ["CALL", null, ["callee:00c58f50:8"]]
+ 00749328 ["INT_ADD", "register:40f0:8", ["const:749328:8", "const:4:8"]]
+ 00749328 ["CALL", null, ["callee:00c58f50:8"]]
- 00748f78 bytes 023c1494
+ 00749328 bytes 0a3f1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edee447b518bcd2aefc24253db6dd9fe"></a>

### [`00748fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fb4.md) → [`00749364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749364.md) FUN_00749364

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00748f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00748ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748fb4.md#insn-00748ff4)
- 新版 [`007493a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749364.md#insn-007493a4)

~~~diff
- 00748ff4 ["INT_ADD", "register:40f0:8", ["const:748ff4:8", "const:4:8"]]
- 00748ff4 ["CALL", null, ["callee:00748f38:8"]]
+ 007493a4 ["INT_ADD", "register:40f0:8", ["const:7493a4:8", "const:4:8"]]
+ 007493a4 ["CALL", null, ["callee:00748f38:8"]]
- 00748ff4 bytes e5feff97
+ 007493a4 bytes e5feff97
~~~


<a id="compare-7a42cbf2e37e9900f4089443fbab748b"></a>

### [`007499dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/007499dc.md) → [`00749d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749d8c.md) FUN_00749d8c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007470f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007470f4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00749a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/007499dc.md#insn-00749a18)
- 新版 [`00749dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/00749d8c.md#insn-00749dc8)

~~~diff
- 00749a18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00749a18 ["INT_ADD", "register:40f0:8", ["const:749a18:8", "const:4:8"]]
- 00749a18 ["CALLIND", null, ["register:0:8"]]
+ 00749dc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00749dc8 ["INT_ADD", "register:40f0:8", ["const:749dc8:8", "const:4:8"]]
+ 00749dc8 ["CALLIND", null, ["register:0:8"]]
- 00749a18 bytes 00013fd6
+ 00749dc8 bytes 00013fd6
~~~


<a id="compare-bd6820978cc013e80b595cc3ff46e2ec"></a>

### [`0074a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a370.md) → [`0074a720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a720.md) FUN_0074a720

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`009ab624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a370.md#insn-0074a3a4) · [`0074a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a370.md#insn-0074a3c0) · [`0074a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a370.md#insn-0074a3d0)
- 新版 [`0074a754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a720.md#insn-0074a754) · [`0074a770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a720.md#insn-0074a770) · [`0074a780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a720.md#insn-0074a780)

~~~diff
- 0074a3a4 ["INT_ADD", "register:40f0:8", ["const:74a3a4:8", "const:4:8"]]
- 0074a3a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0074a754 ["INT_ADD", "register:40f0:8", ["const:74a754:8", "const:4:8"]]
+ 0074a754 ["CALL", null, ["callee:00c58f50:8"]]
- 0074a3a4 bytes f7361494
+ 0074a754 bytes ff391494
- 0074a3c0 ["INT_ADD", "register:40f0:8", ["const:74a3c0:8", "const:4:8"]]
- 0074a3c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0074a770 ["INT_ADD", "register:40f0:8", ["const:74a770:8", "const:4:8"]]
+ 0074a770 ["CALL", null, ["callee:00c58f50:8"]]
- 0074a3c0 bytes f0361494
+ 0074a770 bytes f8391494
- 0074a3d0 ["INT_ADD", "register:40f0:8", ["const:74a3d0:8", "const:4:8"]]
- 0074a3d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0074a780 ["INT_ADD", "register:40f0:8", ["const:74a780:8", "const:4:8"]]
+ 0074a780 ["CALL", null, ["callee:00c58f50:8"]]
- 0074a3d0 bytes ec361494
+ 0074a780 bytes f4391494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e162a117ed11165fc7e19d292254ae20"></a>

### [`0074a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a5d4.md) → [`0074a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a984.md) FUN_0074a984

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007470f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007470f4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a5d4.md#insn-0074a610)
- 新版 [`0074a9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a984.md#insn-0074a9c0)

~~~diff
- 0074a610 ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a610 ["INT_ADD", "register:40f0:8", ["const:74a610:8", "const:4:8"]]
- 0074a610 ["CALLIND", null, ["register:0:8"]]
+ 0074a9c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074a9c0 ["INT_ADD", "register:40f0:8", ["const:74a9c0:8", "const:4:8"]]
+ 0074a9c0 ["CALLIND", null, ["register:0:8"]]
- 0074a610 bytes 00013fd6
+ 0074a9c0 bytes 00013fd6
~~~


<a id="compare-bfeaca5428b4209c9cf4415081763530"></a>

### [`0074a624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a624.md) → [`0074a9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a9d4.md) FUN_0074a9d4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a624.md#insn-0074a65c) · [`0074a680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a624.md#insn-0074a680)
- 新版 [`0074aa0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a9d4.md#insn-0074aa0c) · [`0074aa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074a9d4.md#insn-0074aa30)

~~~diff
- 0074a65c ["COPY", "register:0:8", ["register:4040:8"]]
- 0074a65c ["INT_ADD", "register:40f0:8", ["const:74a65c:8", "const:4:8"]]
- 0074a65c ["CALLIND", null, ["register:0:8"]]
+ 0074aa0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0074aa0c ["INT_ADD", "register:40f0:8", ["const:74aa0c:8", "const:4:8"]]
+ 0074aa0c ["CALLIND", null, ["register:0:8"]]
- 0074a65c bytes 00013fd6
+ 0074aa0c bytes 00013fd6
- 0074a680 ["INT_ADD", "register:40f0:8", ["const:74a680:8", "const:4:8"]]
- 0074a680 ["CALL", null, ["callee:00c58f80:8"]]
+ 0074aa30 ["INT_ADD", "register:40f0:8", ["const:74aa30:8", "const:4:8"]]
+ 0074aa30 ["CALL", null, ["callee:00c58f80:8"]]
- 0074a680 bytes 4c361494
+ 0074aa30 bytes 54391494
~~~


<a id="compare-19e3e3c554953c3afc1958781d7c1076"></a>

### [`0074a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md) → [`0074aa5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aa5c.md) FUN_0074aa5c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) · 呼出先 2件 [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00747664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md) · 呼出先 2件 [`00748f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00748/00748f38.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a6ac.md#insn-0074a700)
- 新版 [`0074aab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aa5c.md#insn-0074aab0)

~~~diff
- 0074a700 ["INT_ADD", "register:40f0:8", ["const:74a700:8", "const:4:8"]]
- 0074a700 ["CALL", null, ["callee:00748f38:8"]]
+ 0074aab0 ["INT_ADD", "register:40f0:8", ["const:74aab0:8", "const:4:8"]]
+ 0074aab0 ["CALL", null, ["callee:00748f38:8"]]
- 0074a700 bytes 22f9ff97
+ 0074aab0 bytes 22f9ff97
~~~


<a id="compare-136b116fa8d9bd70d1030b1c834aa62d"></a>

### [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) → [`0074aadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md) FUN_0074aadc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007472b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/007472b4.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0074a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00747664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/00747664.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0074abdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md#insn-0074a7ac) · [`0074a7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md#insn-0074a7c4) · [`0074a828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md#insn-0074a828)
- 新版 [`0074ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md#insn-0074ab5c) · [`0074ab74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md#insn-0074ab74) · [`0074abd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md#insn-0074abd8)

~~~diff
- 0074a7ac ["INT_ADD", "register:40f0:8", ["const:74a7ac:8", "const:4:8"]]
- 0074a7ac ["CALL", null, ["callee:0074abdc:8"]]
+ 0074ab5c ["INT_ADD", "register:40f0:8", ["const:74ab5c:8", "const:4:8"]]
+ 0074ab5c ["CALL", null, ["callee:0074abdc:8"]]
- 0074a7ac bytes 20000094
+ 0074ab5c bytes 20000094
- 0074a7c4 ["INT_ADD", "register:40f0:8", ["const:74a7c4:8", "const:4:8"]]
- 0074a7c4 ["CALL", null, ["callee:0043be80:8"]]
+ 0074ab74 ["INT_ADD", "register:40f0:8", ["const:74ab74:8", "const:4:8"]]
+ 0074ab74 ["CALL", null, ["callee:0043be80:8"]]
- 0074a7c4 bytes e7c4f397
+ 0074ab74 bytes c3c4f397
- 0074a828 ["INT_ADD", "register:40f0:8", ["const:74a828:8", "const:4:8"]]
- 0074a828 ["CALL", null, ["callee:00c58f80:8"]]
+ 0074abd8 ["INT_ADD", "register:40f0:8", ["const:74abd8:8", "const:4:8"]]
+ 0074abd8 ["CALL", null, ["callee:00c58f80:8"]]
- 0074a828 bytes e2351494
+ 0074abd8 bytes ea381494
~~~


<a id="compare-bbdb5195730c8a64fbe9c8c14db1aaa8"></a>

### [`0074a82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md) → [`0074abdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md) FUN_0074abdc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0074a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a72c.md) [`008a3cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3cf0.md) [`009aae54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aae54.md) [`009ac30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac30c.md) [`009afefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`0074aadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074aadc.md) [`008a4c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4c9c.md) [`009abe00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abe00.md) [`009ad2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad2b8.md) [`009b0ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md#insn-0074a880) · [`0074a8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md#insn-0074a8ac) · [`0074a8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074a82c.md#insn-0074a8c4)
- 新版 [`0074ac30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md#insn-0074ac30) · [`0074ac5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md#insn-0074ac5c) · [`0074ac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074a/0074abdc.md#insn-0074ac74)

~~~diff
- 0074a880 ["INT_ADD", "register:40f0:8", ["const:74a880:8", "const:4:8"]]
- 0074a880 ["CALL", null, ["callee:0043be80:8"]]
+ 0074ac30 ["INT_ADD", "register:40f0:8", ["const:74ac30:8", "const:4:8"]]
+ 0074ac30 ["CALL", null, ["callee:0043be80:8"]]
- 0074a880 bytes b8c4f397
+ 0074ac30 bytes 94c4f397
- 0074a8ac ["INT_ADD", "register:40f0:8", ["const:74a8ac:8", "const:4:8"]]
- 0074a8ac ["CALL", null, ["callee:00c58f30:8"]]
+ 0074ac5c ["INT_ADD", "register:40f0:8", ["const:74ac5c:8", "const:4:8"]]
+ 0074ac5c ["CALL", null, ["callee:00c58f30:8"]]
- 0074a8ac bytes ad351494
+ 0074ac5c bytes b5381494
- 0074a8c4 ["INT_ADD", "register:40f0:8", ["const:74a8c4:8", "const:4:8"]]
- 0074a8c4 ["CALL", null, ["callee:00c590a0:8"]]
+ 0074ac74 ["INT_ADD", "register:40f0:8", ["const:74ac74:8", "const:4:8"]]
+ 0074ac74 ["CALL", null, ["callee:00c590a0:8"]]
- 0074a8c4 bytes 03361494
+ 0074ac74 bytes 0b391494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f2501223947db39da0e3d03e47ecd6a"></a>

### [`0074adf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074adf0.md) → [`0074b1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b1a0.md) FUN_0074b1a0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006f8a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006f8e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md) · 呼出先 4件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074ae04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074adf0.md#insn-0074ae04) · [`0074ae0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074adf0.md#insn-0074ae0c) · [`0074ae24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074a/0074adf0.md#insn-0074ae24)
- 新版 [`0074b1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b1a0.md#insn-0074b1b4) · [`0074b1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b1a0.md#insn-0074b1bc) · [`0074b1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074b1a0.md#insn-0074b1d4)

~~~diff
- 0074ae04 ["INT_ADD", "register:40f0:8", ["const:74ae04:8", "const:4:8"]]
- 0074ae04 ["CALL", null, ["callee:008524fc:8"]]
+ 0074b1b4 ["INT_ADD", "register:40f0:8", ["const:74b1b4:8", "const:4:8"]]
+ 0074b1b4 ["CALL", null, ["callee:008524fc:8"]]
- 0074ae04 bytes d3190494
+ 0074b1b4 bytes d21c0494
- 0074ae0c ["INT_ADD", "register:40f0:8", ["const:74ae0c:8", "const:4:8"]]
- 0074ae0c ["CALL", null, ["callee:00467bc0:8"]]
+ 0074b1bc ["INT_ADD", "register:40f0:8", ["const:74b1bc:8", "const:4:8"]]
+ 0074b1bc ["CALL", null, ["callee:00467bc0:8"]]
- 0074ae0c bytes a572f497
+ 0074b1bc bytes 8172f497
- 0074ae24 ["INT_ADD", "register:40f0:8", ["const:74ae24:8", "const:4:8"]]
- 0074ae24 ["CALL", null, ["callee:008524fc:8"]]
+ 0074b1d4 ["INT_ADD", "register:40f0:8", ["const:74b1d4:8", "const:4:8"]]
+ 0074b1d4 ["CALL", null, ["callee:008524fc:8"]]
- 0074ae24 bytes cb190494
+ 0074b1d4 bytes ca1c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e8fe82b19fb505004fcb98ea90606e"></a>

### [`0074bba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074bba4.md) → [`0074bf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074bf54.md) FUN_0074bf54

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00651ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`00651e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md) · 呼出先 4件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074bbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074bba4.md#insn-0074bbc0) · [`0074bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074bba4.md#insn-0074bbd0) · [`0074bbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074b/0074bba4.md#insn-0074bbd4)
- 新版 [`0074bf70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074bf54.md#insn-0074bf70) · [`0074bf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074bf54.md#insn-0074bf80) · [`0074bf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074b/0074bf54.md#insn-0074bf84)

~~~diff
- 0074bbc0 ["INT_ADD", "register:40f0:8", ["const:74bbc0:8", "const:4:8"]]
- 0074bbc0 ["CALL", null, ["callee:00467bc0:8"]]
+ 0074bf70 ["INT_ADD", "register:40f0:8", ["const:74bf70:8", "const:4:8"]]
+ 0074bf70 ["CALL", null, ["callee:00467bc0:8"]]
- 0074bbc0 bytes 386ff497
+ 0074bf70 bytes 146ff497
- 0074bbd0 ["INT_ADD", "register:40f0:8", ["const:74bbd0:8", "const:4:8"]]
- 0074bbd0 ["CALL", null, ["callee:008524fc:8"]]
+ 0074bf80 ["INT_ADD", "register:40f0:8", ["const:74bf80:8", "const:4:8"]]
+ 0074bf80 ["CALL", null, ["callee:008524fc:8"]]
- 0074bbd0 bytes 60160494
+ 0074bf80 bytes 5f190494
- 0074bbd4 ["INT_ADD", "register:40f0:8", ["const:74bbd4:8", "const:4:8"]]
- 0074bbd4 ["CALL", null, ["callee:0046cd24:8"]]
+ 0074bf84 ["INT_ADD", "register:40f0:8", ["const:74bf84:8", "const:4:8"]]
+ 0074bf84 ["CALL", null, ["callee:0046cd24:8"]]
- 0074bbd4 bytes 8c83f497
+ 0074bf84 bytes 6883f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be9cf84190745e67740ccd72bff9c13b"></a>

### [`0074e008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e008.md) → [`0074e3b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e3b8.md) FUN_0074e3b8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0091abcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091abcc.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`0091bb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0091b/0091bb78.md) · 呼出先 4件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0074e054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e008.md#insn-0074e054) · [`0074e05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e008.md#insn-0074e05c) · [`0074e060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074e/0074e008.md#insn-0074e060)
- 新版 [`0074e404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e3b8.md#insn-0074e404) · [`0074e40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e3b8.md#insn-0074e40c) · [`0074e410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074e/0074e3b8.md#insn-0074e410)

~~~diff
- 0074e054 ["INT_ADD", "register:40f0:8", ["const:74e054:8", "const:4:8"]]
- 0074e054 ["CALL", null, ["callee:00467bc0:8"]]
+ 0074e404 ["INT_ADD", "register:40f0:8", ["const:74e404:8", "const:4:8"]]
+ 0074e404 ["CALL", null, ["callee:00467bc0:8"]]
- 0074e054 bytes 1366f497
+ 0074e404 bytes ef65f497
- 0074e05c ["INT_ADD", "register:40f0:8", ["const:74e05c:8", "const:4:8"]]
- 0074e05c ["CALL", null, ["callee:008524fc:8"]]
+ 0074e40c ["INT_ADD", "register:40f0:8", ["const:74e40c:8", "const:4:8"]]
+ 0074e40c ["CALL", null, ["callee:008524fc:8"]]
- 0074e05c bytes 3d0d0494
+ 0074e40c bytes 3c100494
- 0074e060 ["INT_ADD", "register:40f0:8", ["const:74e060:8", "const:4:8"]]
- 0074e060 ["CALL", null, ["callee:0046cd24:8"]]
+ 0074e410 ["INT_ADD", "register:40f0:8", ["const:74e410:8", "const:4:8"]]
+ 0074e410 ["CALL", null, ["callee:0046cd24:8"]]
- 0074e060 bytes 697af497
+ 0074e410 bytes 457af497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5346f58b16f7946508ccf1bbc88c2861"></a>

### [`00755bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bb8.md) → [`00755f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f68.md) FUN_00755f68

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00755ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00755e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755e70.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00755bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00755/00755bb8.md#insn-00755bc8)
- 新版 [`00755f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00755/00755f68.md#insn-00755f78)

~~~diff
- 00755bc8 ["INT_ADD", "register:40f0:8", ["const:755bc8:8", "const:4:8"]]
- 00755bc8 ["CALL", null, ["callee:00755e70:8"]]
+ 00755f78 ["INT_ADD", "register:40f0:8", ["const:755f78:8", "const:4:8"]]
+ 00755f78 ["CALL", null, ["callee:00755e70:8"]]
- 00755bc8 bytes beffff97
+ 00755f78 bytes beffff97
~~~


<a id="compare-835935d8e4631502c40f887c989ad568"></a>

### [`0075843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/0075843c.md) → [`007587ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007587ec.md) FUN_007587ec

採用 · 移動量 `+0x3b0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`007bcdd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007bc/007bcdd8.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007584a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/0075843c.md#insn-007584a4) · [`00758528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/0075843c.md#insn-00758528)
- 新版 [`00758854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007587ec.md#insn-00758854) · [`007588d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007587ec.md#insn-007588d8)

~~~diff
- 007584a4 ["INT_ADD", "register:40f0:8", ["const:7584a4:8", "const:4:8"]]
- 007584a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00758854 ["INT_ADD", "register:40f0:8", ["const:758854:8", "const:4:8"]]
+ 00758854 ["CALL", null, ["callee:00c58f30:8"]]
- 007584a4 bytes affe1394
+ 00758854 bytes b7011494
- 00758528 ["INT_ADD", "register:40f0:8", ["const:758528:8", "const:4:8"]]
- 00758528 ["CALL", null, ["callee:0043bf04:8"]]
+ 007588d8 ["INT_ADD", "register:40f0:8", ["const:7588d8:8", "const:4:8"]]
+ 007588d8 ["CALL", null, ["callee:0043bf04:8"]]
- 00758528 bytes af8df397
+ 007588d8 bytes 8b8df397
~~~


<a id="compare-dfd2bfe512f75b6159aae9b8c84526b8"></a>

### [`00758550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758550.md) → [`00758900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758900.md) FUN_00758900

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0077bc18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077bc18.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`0077bff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077bff4.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00758570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758550.md#insn-00758570) · [`00758584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758550.md#insn-00758584) · [`0075858c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758550.md#insn-0075858c)
- 新版 [`00758920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758900.md#insn-00758920) · [`00758934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758900.md#insn-00758934) · [`0075893c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/00758900.md#insn-0075893c)

~~~diff
- 00758570 ["INT_ADD", "register:40f0:8", ["const:758570:8", "const:4:8"]]
- 00758570 ["CALL", null, ["callee:00c54d90:8"]]
+ 00758920 ["INT_ADD", "register:40f0:8", ["const:758920:8", "const:4:8"]]
+ 00758920 ["CALL", null, ["callee:00c54d90:8"]]
- 00758570 bytes 0cee1394
+ 00758920 bytes 1cf11394
- 00758584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00758584 ["INT_ADD", "register:40f0:8", ["const:758584:8", "const:4:8"]]
- 00758584 ["CALLIND", null, ["register:0:8"]]
+ 00758934 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00758934 ["INT_ADD", "register:40f0:8", ["const:758934:8", "const:4:8"]]
+ 00758934 ["CALLIND", null, ["register:0:8"]]
- 00758584 bytes 00013fd6
+ 00758934 bytes 00013fd6
- 0075858c ["INT_ADD", "register:40f0:8", ["const:75858c:8", "const:4:8"]]
- 0075858c ["CALL", null, ["callee:00c58f20:8"]]
+ 0075893c ["INT_ADD", "register:40f0:8", ["const:75893c:8", "const:4:8"]]
+ 0075893c ["CALL", null, ["callee:00c58f20:8"]]
- 0075858c bytes 71fe1394
+ 0075893c bytes 79011494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73eac63dacfaaf89a3b24a305d6c0dc2"></a>

### [`0075b928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b928.md) → [`0075bcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bcd8.md) FUN_0075bcd8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075b944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b928.md#insn-0075b944) · [`0075b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b928.md#insn-0075b954)
- 新版 [`0075bcf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bcd8.md#insn-0075bcf4) · [`0075bd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bcd8.md#insn-0075bd04)

~~~diff
- 0075b944 ["INT_ADD", "register:40f0:8", ["const:75b944:8", "const:4:8"]]
- 0075b944 ["CALL", null, ["callee:00c58f50:8"]]
+ 0075bcf4 ["INT_ADD", "register:40f0:8", ["const:75bcf4:8", "const:4:8"]]
+ 0075bcf4 ["CALL", null, ["callee:00c58f50:8"]]
- 0075b944 bytes 8ff11394
+ 0075bcf4 bytes 97f41394
- 0075b954 ["INT_ADD", "register:40f0:8", ["const:75b954:8", "const:4:8"]]
- 0075b954 ["CALL", null, ["callee:00c58f50:8"]]
+ 0075bd04 ["INT_ADD", "register:40f0:8", ["const:75bd04:8", "const:4:8"]]
+ 0075bd04 ["CALL", null, ["callee:00c58f50:8"]]
- 0075b954 bytes 8bf11394
+ 0075bd04 bytes 93f41394
~~~


<a id="compare-df6a2d80839017a5b88ea63ef69e9ecc"></a>

### [`0075d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d5e0.md) → [`0075d990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075d990.md) FUN_0075d990

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 12件 [`00664b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664b00.md) [`00664b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664b9c.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00665078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665078.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 12件 [`00664eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664eb0.md) [`00664f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664f4c.md) [`00664fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664fbc.md) [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00665428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665428.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075d630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d5e0.md#insn-0075d630) · [`0075d63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d5e0.md#insn-0075d63c) · [`0075d64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d5e0.md#insn-0075d64c)
- 新版 [`0075d9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075d990.md#insn-0075d9e0) · [`0075d9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075d990.md#insn-0075d9ec) · [`0075d9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075d990.md#insn-0075d9fc)

~~~diff
- 0075d630 ["INT_ADD", "register:40f0:8", ["const:75d630:8", "const:4:8"]]
- 0075d630 ["CALL", null, ["callee:00b30910:8"]]
+ 0075d9e0 ["INT_ADD", "register:40f0:8", ["const:75d9e0:8", "const:4:8"]]
+ 0075d9e0 ["CALL", null, ["callee:00b30910:8"]]
- 0075d630 bytes bb480f94
+ 0075d9e0 bytes cc4b0f94
- 0075d63c ["INT_ADD", "register:40f0:8", ["const:75d63c:8", "const:4:8"]]
- 0075d63c ["CALL", null, ["callee:00664eb0:8"]]
+ 0075d9ec ["INT_ADD", "register:40f0:8", ["const:75d9ec:8", "const:4:8"]]
+ 0075d9ec ["CALL", null, ["callee:00664eb0:8"]]
- 0075d63c bytes 311dfc97
+ 0075d9ec bytes 311dfc97
- 0075d64c ["INT_ADD", "register:40f0:8", ["const:75d64c:8", "const:4:8"]]
- 0075d64c ["CALL", null, ["callee:00664eb0:8"]]
+ 0075d9fc ["INT_ADD", "register:40f0:8", ["const:75d9fc:8", "const:4:8"]]
+ 0075d9fc ["CALL", null, ["callee:00664eb0:8"]]
- 0075d64c bytes 2d1dfc97
+ 0075d9fc bytes 2d1dfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514f3a4b1d7397df20c39e34c3c16554"></a>

### [`0075e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e91c.md) → [`0075eccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075eccc.md) FUN_0075eccc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e5e0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0077c968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c968.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0075e990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075e990.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0077cd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cd44.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0075e994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e91c.md#insn-0075e994) · [`0075e9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e91c.md#insn-0075e9a8) · [`0075ea00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075e91c.md#insn-0075ea00)
- 新版 [`0075ed44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075eccc.md#insn-0075ed44) · [`0075ed58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075eccc.md#insn-0075ed58) · [`0075edb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075eccc.md#insn-0075edb0)

~~~diff
- 0075e994 ["INT_ADD", "register:40f0:8", ["const:75e994:8", "const:4:8"]]
- 0075e994 ["CALL", null, ["callee:0043be80:8"]]
+ 0075ed44 ["INT_ADD", "register:40f0:8", ["const:75ed44:8", "const:4:8"]]
+ 0075ed44 ["CALL", null, ["callee:0043be80:8"]]
- 0075e994 bytes 7374f397
+ 0075ed44 bytes 4f74f397
- 0075e9a8 ["INT_ADD", "register:40f0:8", ["const:75e9a8:8", "const:4:8"]]
- 0075e9a8 ["CALL", null, ["callee:0043be80:8"]]
+ 0075ed58 ["INT_ADD", "register:40f0:8", ["const:75ed58:8", "const:4:8"]]
+ 0075ed58 ["CALL", null, ["callee:0043be80:8"]]
- 0075e9a8 bytes 6e74f397
+ 0075ed58 bytes 4a74f397
- 0075ea00 ["INT_ADD", "register:40f0:8", ["const:75ea00:8", "const:4:8"]]
- 0075ea00 ["CALL", null, ["callee:0077cd44:8"]]
+ 0075edb0 ["INT_ADD", "register:40f0:8", ["const:75edb0:8", "const:4:8"]]
+ 0075edb0 ["CALL", null, ["callee:0077cd44:8"]]
- 0075ea00 bytes da770094
+ 0075edb0 bytes e5770094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7780ee5d1b14e63253898219296da99e"></a>

### [`00763ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md) → [`007640c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007640c4.md) FUN_007640c4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) · 呼出先 5件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0066d0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d0d4.md) [`00b35884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b35/00b35884.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`00a8f618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8f/00a8f618.md) · 呼出先 5件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0066d484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d484.md) [`00b36878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b36/00b36878.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00763d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d0c) · [`00763d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d20) · [`00763d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763ce8.md#insn-00763d30)
- 新版 [`007640e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007640c4.md#insn-007640e8) · [`007640fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007640c4.md#insn-007640fc) · [`0076410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007640c4.md#insn-0076410c)

~~~diff
- 00763d0c ["INT_ADD", "register:40f0:8", ["const:763d0c:8", "const:4:8"]]
- 00763d0c ["CALL", null, ["callee:0066d484:8"]]
+ 007640e8 ["INT_ADD", "register:40f0:8", ["const:7640e8:8", "const:4:8"]]
+ 007640e8 ["CALL", null, ["callee:0066d484:8"]]
- 00763d0c bytes f224fc97
+ 007640e8 bytes e724fc97
- 00763d20 ["INT_ADD", "register:40f0:8", ["const:763d20:8", "const:4:8"]]
- 00763d20 ["CALL", null, ["callee:00448254:8"]]
+ 007640fc ["INT_ADD", "register:40f0:8", ["const:7640fc:8", "const:4:8"]]
+ 007640fc ["CALL", null, ["callee:00448254:8"]]
- 00763d20 bytes 8590f397
+ 007640fc bytes 5690f397
- 00763d30 ["INT_ADD", "register:40f0:8", ["const:763d30:8", "const:4:8"]]
- 00763d30 ["CALL", null, ["callee:00c58f50:8"]]
+ 0076410c ["INT_ADD", "register:40f0:8", ["const:76410c:8", "const:4:8"]]
+ 0076410c ["CALL", null, ["callee:00c58f50:8"]]
- 00763d30 bytes 94d01394
+ 0076410c bytes 91d31394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b13be3d3b0d9255aacaf14ea84754aa"></a>

### [`0077b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md) → [`0077b68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b68c.md) FUN_0077b68c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077b2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md#insn-0077b2e8) · [`0077b2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077b/0077b2b0.md#insn-0077b2f4)
- 新版 [`0077b6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b68c.md#insn-0077b6c4) · [`0077b6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077b/0077b68c.md#insn-0077b6d0)

~~~diff
- 0077b2e8 ["INT_ADD", "register:40f0:8", ["const:77b2e8:8", "const:4:8"]]
- 0077b2e8 ["CALL", null, ["callee:005c1b8c:8"]]
+ 0077b6c4 ["INT_ADD", "register:40f0:8", ["const:77b6c4:8", "const:4:8"]]
+ 0077b6c4 ["CALL", null, ["callee:005c1b8c:8"]]
- 0077b2e8 bytes 3d19f997
+ 0077b6c4 bytes 3219f997
- 0077b2f4 ["INT_ADD", "register:40f0:8", ["const:77b2f4:8", "const:4:8"]]
- 0077b2f4 ["CALL", null, ["callee:005c1b8c:8"]]
+ 0077b6d0 ["INT_ADD", "register:40f0:8", ["const:77b6d0:8", "const:4:8"]]
+ 0077b6d0 ["CALL", null, ["callee:005c1b8c:8"]]
- 0077b2f4 bytes 3a19f997
+ 0077b6d0 bytes 2f19f997
~~~


<a id="compare-427f2e341838709a5a8a08b38a900492"></a>

### [`0077c5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md) → [`0077c990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c990.md) FUN_0077c990

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0077c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c1e8.md) · 呼出先 5件 [`007262b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007262b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0077c5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c5c4.md) · 呼出先 5件 [`00726668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00726/00726668.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c608) · [`0077c66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c66c) · [`0077c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c5b4.md#insn-0077c694)
- 新版 [`0077c9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c990.md#insn-0077c9e4) · [`0077ca48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c990.md#insn-0077ca48) · [`0077ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c990.md#insn-0077ca70)

~~~diff
- 0077c608 ["INT_ADD", "register:40f0:8", ["const:77c608:8", "const:4:8"]]
- 0077c608 ["CALL", null, ["callee:00c58f50:8"]]
+ 0077c9e4 ["INT_ADD", "register:40f0:8", ["const:77c9e4:8", "const:4:8"]]
+ 0077c9e4 ["CALL", null, ["callee:00c58f50:8"]]
- 0077c608 bytes 5e6e1394
+ 0077c9e4 bytes 5b711394
- 0077c66c ["INT_ADD", "register:40f0:8", ["const:77c66c:8", "const:4:8"]]
- 0077c66c ["CALL", null, ["callee:00c58f30:8"]]
+ 0077ca48 ["INT_ADD", "register:40f0:8", ["const:77ca48:8", "const:4:8"]]
+ 0077ca48 ["CALL", null, ["callee:00c58f30:8"]]
- 0077c66c bytes 3d6e1394
+ 0077ca48 bytes 3a711394
- 0077c694 ["INT_ADD", "register:40f0:8", ["const:77c694:8", "const:4:8"]]
- 0077c694 ["CALL", null, ["callee:00c590a0:8"]]
+ 0077ca70 ["INT_ADD", "register:40f0:8", ["const:77ca70:8", "const:4:8"]]
+ 0077ca70 ["CALL", null, ["callee:00c590a0:8"]]
- 0077c694 bytes 8f6e1394
+ 0077ca70 bytes 8c711394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80bf211fe7dce16c866a1473e070dd6f"></a>

### [`0077c718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md) → [`0077caf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077caf4.md) FUN_0077caf4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00768c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768c40.md) · 呼出先 5件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0076901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/0076901c.md) · 呼出先 5件 [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c75c) · [`0077c794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c794) · [`0077c7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c718.md#insn-0077c7bc)
- 新版 [`0077cb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077caf4.md#insn-0077cb38) · [`0077cb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077caf4.md#insn-0077cb70) · [`0077cb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077caf4.md#insn-0077cb98)

~~~diff
- 0077c75c ["INT_ADD", "register:40f0:8", ["const:77c75c:8", "const:4:8"]]
- 0077c75c ["CALL", null, ["callee:00c58f50:8"]]
+ 0077cb38 ["INT_ADD", "register:40f0:8", ["const:77cb38:8", "const:4:8"]]
+ 0077cb38 ["CALL", null, ["callee:00c58f50:8"]]
- 0077c75c bytes 096e1394
+ 0077cb38 bytes 06711394
- 0077c794 ["INT_ADD", "register:40f0:8", ["const:77c794:8", "const:4:8"]]
- 0077c794 ["CALL", null, ["callee:00c58f30:8"]]
+ 0077cb70 ["INT_ADD", "register:40f0:8", ["const:77cb70:8", "const:4:8"]]
+ 0077cb70 ["CALL", null, ["callee:00c58f30:8"]]
- 0077c794 bytes f36d1394
+ 0077cb70 bytes f0701394
- 0077c7bc ["INT_ADD", "register:40f0:8", ["const:77c7bc:8", "const:4:8"]]
- 0077c7bc ["CALL", null, ["callee:00c590a0:8"]]
+ 0077cb98 ["INT_ADD", "register:40f0:8", ["const:77cb98:8", "const:4:8"]]
+ 0077cb98 ["CALL", null, ["callee:00c590a0:8"]]
- 0077c7bc bytes 456e1394
+ 0077cb98 bytes 42711394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6888c1bf4afdd05e6fed2ac6b8c7c7"></a>

### [`0077c8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md) → [`0077cc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc94.md) FUN_0077cc94

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075b97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b97c.md) · 呼出先 2件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0075bd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bd2c.md) · 呼出先 2件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0077c91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c91c) · [`0077c92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c92c) · [`0077c93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c8b8.md#insn-0077c93c)
- 新版 [`0077ccf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc94.md#insn-0077ccf8) · [`0077cd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc94.md#insn-0077cd08) · [`0077cd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc94.md#insn-0077cd18)

~~~diff
- 0077c91c ["INT_ADD", "register:40f0:8", ["const:77c91c:8", "const:4:8"]]
- 0077c91c ["CALL", null, ["callee:00494970:8"]]
+ 0077ccf8 ["INT_ADD", "register:40f0:8", ["const:77ccf8:8", "const:4:8"]]
+ 0077ccf8 ["CALL", null, ["callee:00494970:8"]]
- 0077c91c bytes 4d5ff497
+ 0077ccf8 bytes 1e5ff497
- 0077c92c ["INT_ADD", "register:40f0:8", ["const:77c92c:8", "const:4:8"]]
- 0077c92c ["CALL", null, ["callee:00c58f50:8"]]
+ 0077cd08 ["INT_ADD", "register:40f0:8", ["const:77cd08:8", "const:4:8"]]
+ 0077cd08 ["CALL", null, ["callee:00c58f50:8"]]
- 0077c92c bytes 956d1394
+ 0077cd08 bytes 92701394
- 0077c93c ["INT_ADD", "register:40f0:8", ["const:77c93c:8", "const:4:8"]]
- 0077c93c ["CALL", null, ["callee:00c58f50:8"]]
+ 0077cd18 ["INT_ADD", "register:40f0:8", ["const:77cd18:8", "const:4:8"]]
+ 0077cd18 ["CALL", null, ["callee:00c58f50:8"]]
- 0077c93c bytes 916d1394
+ 0077cd18 bytes 8e701394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b52b81303dbb5caa04feade651028dd"></a>

### [`00782b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md) → [`00782f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782f54.md) FUN_00782f54

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00782b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md#insn-00782b94) · [`00782bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b78.md#insn-00782bb4)
- 新版 [`00782f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782f54.md#insn-00782f70) · [`00782f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782f54.md#insn-00782f90)

~~~diff
- 00782b94 ["INT_ADD", "register:40f0:8", ["const:782b94:8", "const:4:8"]]
- 00782b94 ["CALL", null, ["callee:00c54d90:8"]]
+ 00782f70 ["INT_ADD", "register:40f0:8", ["const:782f70:8", "const:4:8"]]
+ 00782f70 ["CALL", null, ["callee:00c54d90:8"]]
- 00782b94 bytes 83441394
+ 00782f70 bytes 88471394
- 00782bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00782bb4 ["INT_ADD", "register:40f0:8", ["const:782bb4:8", "const:4:8"]]
- 00782bb4 ["CALLIND", null, ["register:0:8"]]
+ 00782f90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00782f90 ["INT_ADD", "register:40f0:8", ["const:782f90:8", "const:4:8"]]
+ 00782f90 ["CALLIND", null, ["register:0:8"]]
- 00782bb4 bytes 00013fd6
+ 00782f90 bytes 00013fd6
~~~


<a id="compare-b23e71d2780b5830685d05931c8b0340"></a>

### [`00787e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md) → [`007881e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/007881e8.md) FUN_007881e8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00787c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787c58.md) · 呼出先 6件 [`00468ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) [`00729afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/00729afc.md)
- 新版 呼出元 1件 [`00788034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788034.md) · 呼出先 6件 [`00468fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468fc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046ac48.md) [`00729eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/00729eac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00787e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md#insn-00787e4c) · [`00787e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md#insn-00787e6c) · [`00787ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md#insn-00787ea8)
- 新版 [`00788228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/007881e8.md#insn-00788228) · [`00788248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/007881e8.md#insn-00788248) · [`00788284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/007881e8.md#insn-00788284)

~~~diff
- 00787e4c ["INT_ADD", "register:40f0:8", ["const:787e4c:8", "const:4:8"]]
- 00787e4c ["CALL", null, ["callee:00729eac:8"]]
+ 00788228 ["INT_ADD", "register:40f0:8", ["const:788228:8", "const:4:8"]]
+ 00788228 ["CALL", null, ["callee:00729eac:8"]]
- 00787e4c bytes 2c87fe97
+ 00788228 bytes 2187fe97
- 00787e6c ["INT_ADD", "register:40f0:8", ["const:787e6c:8", "const:4:8"]]
- 00787e6c ["CALL", null, ["callee:0046ac48:8"]]
+ 00788248 ["INT_ADD", "register:40f0:8", ["const:788248:8", "const:4:8"]]
+ 00788248 ["CALL", null, ["callee:0046ac48:8"]]
- 00787e6c bytes af8af397
+ 00788248 bytes 808af397
- 00787ea8 ["INT_ADD", "register:40f0:8", ["const:787ea8:8", "const:4:8"]]
- 00787ea8 ["CALL", null, ["callee:00469f64:8"]]
+ 00788284 ["INT_ADD", "register:40f0:8", ["const:788284:8", "const:4:8"]]
+ 00788284 ["CALL", null, ["callee:00469f64:8"]]
- 00787ea8 bytes 6787f397
+ 00788284 bytes 3887f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a2809f7b9a4d91287da1991222fd73"></a>

### [`0078e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e640.md) → [`0078ea1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ea1c.md) FUN_0078ea1c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0049f750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078e67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e640.md#insn-0078e67c)
- 新版 [`0078ea58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ea1c.md#insn-0078ea58)

~~~diff
- 0078e67c ["INT_ADD", "register:40f0:8", ["const:78e67c:8", "const:4:8"]]
- 0078e67c ["CALL", null, ["callee:0049f750:8"]]
+ 0078ea58 ["INT_ADD", "register:40f0:8", ["const:78ea58:8", "const:4:8"]]
+ 0078ea58 ["CALL", null, ["callee:0049f750:8"]]
- 0078e67c bytes 6d43f497
+ 0078ea58 bytes 3e43f497
~~~


<a id="compare-fb182f1e28dbd87e0f80f3e7886a6249"></a>

### [`007918a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md) → [`00791c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791c84.md) FUN_00791c84

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007918e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md#insn-007918e8) · [`00791930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/007918a8.md#insn-00791930)
- 新版 [`00791cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791c84.md#insn-00791cc4) · [`00791d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791c84.md#insn-00791d0c)

~~~diff
- 007918e8 ["INT_ADD", "register:40f0:8", ["const:7918e8:8", "const:4:8"]]
- 007918e8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00791cc4 ["INT_ADD", "register:40f0:8", ["const:791cc4:8", "const:4:8"]]
+ 00791cc4 ["CALL", null, ["callee:00c58f50:8"]]
- 007918e8 bytes a6191394
+ 00791cc4 bytes a31c1394
- 00791930 ["INT_ADD", "register:40f0:8", ["const:791930:8", "const:4:8"]]
- 00791930 ["CALL", null, ["callee:00c58f50:8"]]
+ 00791d0c ["INT_ADD", "register:40f0:8", ["const:791d0c:8", "const:4:8"]]
+ 00791d0c ["CALL", null, ["callee:00c58f50:8"]]
- 00791930 bytes 94191394
+ 00791d0c bytes 911c1394
~~~


<a id="compare-021b929e57ab5ccb1c769aa5466e405b"></a>

### [`00791968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md) → [`00791d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md) FUN_00791d44

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0072b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072b/0072b19c.md) [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md)
- 新版 呼出元 1件 [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) · 呼出先 10件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0072b54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072b/0072b54c.md) [`00794608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794608.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007919e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-007919e8) · [`00791a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-00791a00) · [`00791a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md#insn-00791a1c)
- 新版 [`00791dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md#insn-00791dc4) · [`00791ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md#insn-00791ddc) · [`00791df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md#insn-00791df8)

~~~diff
- 007919e8 ["INT_ADD", "register:40f0:8", ["const:7919e8:8", "const:4:8"]]
- 007919e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00791dc4 ["INT_ADD", "register:40f0:8", ["const:791dc4:8", "const:4:8"]]
+ 00791dc4 ["CALL", null, ["callee:00c58f30:8"]]
- 007919e8 bytes 5e191394
+ 00791dc4 bytes 5b1c1394
- 00791a00 ["INT_ADD", "register:40f0:8", ["const:791a00:8", "const:4:8"]]
- 00791a00 ["CALL", null, ["callee:00c590a0:8"]]
+ 00791ddc ["INT_ADD", "register:40f0:8", ["const:791ddc:8", "const:4:8"]]
+ 00791ddc ["CALL", null, ["callee:00c590a0:8"]]
- 00791a00 bytes b4191394
+ 00791ddc bytes b11c1394
- 00791a1c ["INT_ADD", "register:40f0:8", ["const:791a1c:8", "const:4:8"]]
- 00791a1c ["CALL", null, ["callee:0072b54c:8"]]
+ 00791df8 ["INT_ADD", "register:40f0:8", ["const:791df8:8", "const:4:8"]]
+ 00791df8 ["CALL", null, ["callee:0072b54c:8"]]
- 00791a1c bytes e065fe97
+ 00791df8 bytes d565fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64edbcf58773775c6b1d4a5ce681255a"></a>

### [`007924dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md) → [`007928b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md) FUN_007928b8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0072ae38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072a/0072ae38.md) [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md)
- 新版 呼出元 1件 [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) · 呼出先 10件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0072b1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072b/0072b1e8.md) [`00794608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794608.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00792558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792558) · [`00792570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792570) · [`00792584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md#insn-00792584)
- 新版 [`00792934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md#insn-00792934) · [`0079294c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md#insn-0079294c) · [`00792960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md#insn-00792960)

~~~diff
- 00792558 ["INT_ADD", "register:40f0:8", ["const:792558:8", "const:4:8"]]
- 00792558 ["CALL", null, ["callee:00c58f30:8"]]
+ 00792934 ["INT_ADD", "register:40f0:8", ["const:792934:8", "const:4:8"]]
+ 00792934 ["CALL", null, ["callee:00c58f30:8"]]
- 00792558 bytes 82161394
+ 00792934 bytes 7f191394
- 00792570 ["INT_ADD", "register:40f0:8", ["const:792570:8", "const:4:8"]]
- 00792570 ["CALL", null, ["callee:00c590a0:8"]]
+ 0079294c ["INT_ADD", "register:40f0:8", ["const:79294c:8", "const:4:8"]]
+ 0079294c ["CALL", null, ["callee:00c590a0:8"]]
- 00792570 bytes d8161394
+ 0079294c bytes d5191394
- 00792584 ["INT_ADD", "register:40f0:8", ["const:792584:8", "const:4:8"]]
- 00792584 ["CALL", null, ["callee:0072b1e8:8"]]
+ 00792960 ["INT_ADD", "register:40f0:8", ["const:792960:8", "const:4:8"]]
+ 00792960 ["CALL", null, ["callee:0072b1e8:8"]]
- 00792584 bytes 2d62fe97
+ 00792960 bytes 2262fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2170142bf2e322ab2e45c94ca2a30d43"></a>

### [`00792a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md) → [`00792dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792dfc.md) FUN_00792dfc

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00794c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009ad9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad9d4.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) [`0079505c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079505c.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009ae980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00792a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md#insn-00792a80) · [`00792a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md#insn-00792a8c) · [`00792aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md#insn-00792aa0)
- 新版 [`00792e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792dfc.md#insn-00792e5c) · [`00792e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792dfc.md#insn-00792e68) · [`00792e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792dfc.md#insn-00792e7c)

~~~diff
- 00792a80 ["INT_ADD", "register:40f0:8", ["const:792a80:8", "const:4:8"]]
- 00792a80 ["CALL", null, ["callee:0079505c:8"]]
+ 00792e5c ["INT_ADD", "register:40f0:8", ["const:792e5c:8", "const:4:8"]]
+ 00792e5c ["CALL", null, ["callee:0079505c:8"]]
- 00792a80 bytes 80080094
+ 00792e5c bytes 80080094
- 00792a8c ["INT_ADD", "register:40f0:8", ["const:792a8c:8", "const:4:8"]]
- 00792a8c ["CALL", null, ["callee:005c1fe0:8"]]
+ 00792e68 ["INT_ADD", "register:40f0:8", ["const:792e68:8", "const:4:8"]]
+ 00792e68 ["CALL", null, ["callee:005c1fe0:8"]]
- 00792a8c bytes 69bcf897
+ 00792e68 bytes 5ebcf897
- 00792aa0 ["INT_ADD", "register:40f0:8", ["const:792aa0:8", "const:4:8"]]
- 00792aa0 ["CALL", null, ["callee:009ae980:8"]]
+ 00792e7c ["INT_ADD", "register:40f0:8", ["const:792e7c:8", "const:4:8"]]
+ 00792e7c ["CALL", null, ["callee:009ae980:8"]]
- 00792aa0 bytes cd6b0894
+ 00792e7c bytes c16e0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38bc62781da7943a9aa62c80b13d7d9e"></a>

### [`00792d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md) → [`00793108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793108.md) FUN_00793108

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 3件 [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 3件 [`008b7f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f14.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00792d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d54) · [`00792d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d64) · [`00792d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792d2c.md#insn-00792d70)
- 新版 [`00793130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793108.md#insn-00793130) · [`00793140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793108.md#insn-00793140) · [`0079314c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793108.md#insn-0079314c)

~~~diff
- 00792d54 ["INT_ADD", "register:40f0:8", ["const:792d54:8", "const:4:8"]]
- 00792d54 ["CALL", null, ["callee:008b89cc:8"]]
+ 00793130 ["INT_ADD", "register:40f0:8", ["const:793130:8", "const:4:8"]]
+ 00793130 ["CALL", null, ["callee:008b89cc:8"]]
- 00792d54 bytes 33930494
+ 00793130 bytes 27960494
- 00792d64 ["INT_ADD", "register:40f0:8", ["const:792d64:8", "const:4:8"]]
- 00792d64 ["CALL", null, ["callee:008b7f14:8"]]
+ 00793140 ["INT_ADD", "register:40f0:8", ["const:793140:8", "const:4:8"]]
+ 00793140 ["CALL", null, ["callee:008b7f14:8"]]
- 00792d64 bytes 81900494
+ 00793140 bytes 75930494
- 00792d70 ["INT_ADD", "register:40f0:8", ["const:792d70:8", "const:4:8"]]
- 00792d70 ["CALL", null, ["callee:008b7f1c:8"]]
+ 0079314c ["INT_ADD", "register:40f0:8", ["const:79314c:8", "const:4:8"]]
+ 0079314c ["CALL", null, ["callee:008b7f1c:8"]]
- 00792d70 bytes 80900494
+ 0079314c bytes 74930494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-430a7545d96cf02a740755154b70a93e"></a>

### [`00794760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md) → [`00794b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794b3c.md) FUN_00794b3c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007947ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947ac) · [`007947c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947c0) · [`007947c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794760.md#insn-007947c8)
- 新版 [`00794b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794b3c.md#insn-00794b88) · [`00794b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794b3c.md#insn-00794b9c) · [`00794ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794b3c.md#insn-00794ba4)

~~~diff
- 007947ac ["INT_ADD", "register:40f0:8", ["const:7947ac:8", "const:4:8"]]
- 007947ac ["CALL", null, ["callee:00c54d90:8"]]
+ 00794b88 ["INT_ADD", "register:40f0:8", ["const:794b88:8", "const:4:8"]]
+ 00794b88 ["CALL", null, ["callee:00c54d90:8"]]
- 007947ac bytes 7dfd1294
+ 00794b88 bytes 82001394
- 007947c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007947c0 ["INT_ADD", "register:40f0:8", ["const:7947c0:8", "const:4:8"]]
- 007947c0 ["CALLIND", null, ["register:0:8"]]
+ 00794b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00794b9c ["INT_ADD", "register:40f0:8", ["const:794b9c:8", "const:4:8"]]
+ 00794b9c ["CALLIND", null, ["register:0:8"]]
- 007947c0 bytes 00013fd6
+ 00794b9c bytes 00013fd6
- 007947c8 ["INT_ADD", "register:40f0:8", ["const:7947c8:8", "const:4:8"]]
- 007947c8 ["CALL", null, ["callee:00c58f20:8"]]
+ 00794ba4 ["INT_ADD", "register:40f0:8", ["const:794ba4:8", "const:4:8"]]
+ 00794ba4 ["CALL", null, ["callee:00c58f20:8"]]
- 007947c8 bytes e20d1394
+ 00794ba4 bytes df101394
~~~


<a id="compare-97035d39358df565755ee4278dbbdf68"></a>

### [`007947f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md) → [`00794bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794bd4.md) FUN_00794bd4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009294ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/009294ec.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009291e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00929/009291e0.md)
- 新版 呼出元 1件 [`0092a498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0092a/0092a498.md) · 呼出先 2件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0092a18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0092a/0092a18c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md#insn-00794808) · [`00794814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007947f8.md#insn-00794814)
- 新版 [`00794be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794bd4.md#insn-00794be4) · [`00794bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794bd4.md#insn-00794bf0)

~~~diff
- 00794808 ["INT_ADD", "register:40f0:8", ["const:794808:8", "const:4:8"]]
- 00794808 ["CALL", null, ["callee:008524fc:8"]]
+ 00794be4 ["INT_ADD", "register:40f0:8", ["const:794be4:8", "const:4:8"]]
+ 00794be4 ["CALL", null, ["callee:008524fc:8"]]
- 00794808 bytes 52f30294
+ 00794be4 bytes 46f60294
- 00794814 ["INT_ADD", "register:40f0:8", ["const:794814:8", "const:4:8"]]
- 00794814 ["CALL", null, ["callee:0092a18c:8"]]
+ 00794bf0 ["INT_ADD", "register:40f0:8", ["const:794bf0:8", "const:4:8"]]
+ 00794bf0 ["CALL", null, ["callee:0092a18c:8"]]
- 00794814 bytes 73520694
+ 00794bf0 bytes 67550694
~~~


<a id="compare-e4ca68ce8b1b318a19fa12ddc92cd4d7"></a>

### [`00794994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md) → [`00794d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md) FUN_00794d70

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md) [`00791968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md) [`00791eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md) [`007924dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md) · 呼出先 6件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00794ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md) [`00794bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 5件 [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) [`00791658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md) [`00791d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md) [`00792294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792294.md) [`007928b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md) · 呼出先 6件 [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`00794ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794ec4.md) [`00794fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fa0.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007949f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-007949f0) · [`00794a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-00794a4c) · [`00794aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md#insn-00794aa8)
- 新版 [`00794dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md#insn-00794dcc) · [`00794e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md#insn-00794e28) · [`00794e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md#insn-00794e84)

~~~diff
- 007949f0 ["INT_ADD", "register:40f0:8", ["const:7949f0:8", "const:4:8"]]
- 007949f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00794dcc ["INT_ADD", "register:40f0:8", ["const:794dcc:8", "const:4:8"]]
+ 00794dcc ["CALL", null, ["callee:00c58f30:8"]]
- 007949f0 bytes 5c0d1394
+ 00794dcc bytes 59101394
- 00794a4c ["INT_ADD", "register:40f0:8", ["const:794a4c:8", "const:4:8"]]
- 00794a4c ["CALL", null, ["callee:00540abc:8"]]
+ 00794e28 ["INT_ADD", "register:40f0:8", ["const:794e28:8", "const:4:8"]]
+ 00794e28 ["CALL", null, ["callee:00540abc:8"]]
- 00794a4c bytes 54aff697
+ 00794e28 bytes 25aff697
- 00794aa8 ["INT_ADD", "register:40f0:8", ["const:794aa8:8", "const:4:8"]]
- 00794aa8 ["CALL", null, ["callee:00794fa0:8"]]
+ 00794e84 ["INT_ADD", "register:40f0:8", ["const:794e84:8", "const:4:8"]]
+ 00794e84 ["CALL", null, ["callee:00794fa0:8"]]
- 00794aa8 bytes 47000094
+ 00794e84 bytes 47000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad896ce30c22bc8cf6391c62e2cd6b9"></a>

### [`00794ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md) → [`00794ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794ec4.md) FUN_00794ec4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00794994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00794d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md#insn-00794b50) · [`00794b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794ae8.md#insn-00794b98)
- 新版 [`00794f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794ec4.md#insn-00794f2c) · [`00794f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794ec4.md#insn-00794f74)

~~~diff
- 00794b50 ["INT_ADD", "register:40f0:8", ["const:794b50:8", "const:4:8"]]
- 00794b50 ["CALL", null, ["callee:00c58f50:8"]]
+ 00794f2c ["INT_ADD", "register:40f0:8", ["const:794f2c:8", "const:4:8"]]
+ 00794f2c ["CALL", null, ["callee:00c58f50:8"]]
- 00794b50 bytes 0c0d1394
+ 00794f2c bytes 09101394
- 00794b98 ["INT_ADD", "register:40f0:8", ["const:794b98:8", "const:4:8"]]
- 00794b98 ["CALL", null, ["callee:00c58f50:8"]]
+ 00794f74 ["INT_ADD", "register:40f0:8", ["const:794f74:8", "const:4:8"]]
+ 00794f74 ["CALL", null, ["callee:00c58f50:8"]]
- 00794b98 bytes fa0c1394
+ 00794f74 bytes f70f1394
~~~


<a id="compare-e71a7dde154fdc195bf7fd29c563075d"></a>

### [`00794bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md) → [`00794fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fb4.md) FUN_00794fb4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md#insn-00794c1c) · [`00794c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bd8.md#insn-00794c64)
- 新版 [`00794ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fb4.md#insn-00794ff8) · [`00795040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fb4.md#insn-00795040)

~~~diff
- 00794c1c ["INT_ADD", "register:40f0:8", ["const:794c1c:8", "const:4:8"]]
- 00794c1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00794ff8 ["INT_ADD", "register:40f0:8", ["const:794ff8:8", "const:4:8"]]
+ 00794ff8 ["CALL", null, ["callee:00c58f50:8"]]
- 00794c1c bytes d90c1394
+ 00794ff8 bytes d60f1394
- 00794c64 ["INT_ADD", "register:40f0:8", ["const:794c64:8", "const:4:8"]]
- 00794c64 ["CALL", null, ["callee:00c58f50:8"]]
+ 00795040 ["INT_ADD", "register:40f0:8", ["const:795040:8", "const:4:8"]]
+ 00795040 ["CALL", null, ["callee:00c58f50:8"]]
- 00794c64 bytes c70c1394
+ 00795040 bytes c40f1394
~~~


<a id="compare-3a521a3c7312358d8286c816eeadff3a"></a>

### [`00794f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md) → [`00795328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795328.md) FUN_00795328

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00792f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007932e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/007932e8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00794fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fbc) · [`00794fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fd0) · [`00794fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md#insn-00794fd8)
- 新版 [`00795398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795328.md#insn-00795398) · [`007953ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795328.md#insn-007953ac) · [`007953b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795328.md#insn-007953b4)

~~~diff
- 00794fbc ["INT_ADD", "register:40f0:8", ["const:794fbc:8", "const:4:8"]]
- 00794fbc ["CALL", null, ["callee:00c54d90:8"]]
+ 00795398 ["INT_ADD", "register:40f0:8", ["const:795398:8", "const:4:8"]]
+ 00795398 ["CALL", null, ["callee:00c54d90:8"]]
- 00794fbc bytes 79fb1294
+ 00795398 bytes 7efe1294
- 00794fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00794fd0 ["INT_ADD", "register:40f0:8", ["const:794fd0:8", "const:4:8"]]
- 00794fd0 ["CALLIND", null, ["register:0:8"]]
+ 007953ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 007953ac ["INT_ADD", "register:40f0:8", ["const:7953ac:8", "const:4:8"]]
+ 007953ac ["CALLIND", null, ["register:0:8"]]
- 00794fd0 bytes 00013fd6
+ 007953ac bytes 00013fd6
- 00794fd8 ["INT_ADD", "register:40f0:8", ["const:794fd8:8", "const:4:8"]]
- 00794fd8 ["CALL", null, ["callee:00c58f20:8"]]
+ 007953b4 ["INT_ADD", "register:40f0:8", ["const:7953b4:8", "const:4:8"]]
+ 007953b4 ["CALL", null, ["callee:00c58f20:8"]]
- 00794fd8 bytes de0b1394
+ 007953b4 bytes db0e1394
~~~


<a id="compare-3778a832aba8a78e740df5a9b2f6e6ce"></a>

### [`007955ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md) → [`007959c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007959c8.md) FUN_007959c8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00795660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-00795660) · [`00795674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-00795674) · [`0079567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007955ec.md#insn-0079567c)
- 新版 [`00795a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007959c8.md#insn-00795a3c) · [`00795a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007959c8.md#insn-00795a50) · [`00795a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007959c8.md#insn-00795a58)

~~~diff
- 00795660 ["INT_ADD", "register:40f0:8", ["const:795660:8", "const:4:8"]]
- 00795660 ["CALL", null, ["callee:00c54d90:8"]]
+ 00795a3c ["INT_ADD", "register:40f0:8", ["const:795a3c:8", "const:4:8"]]
+ 00795a3c ["CALL", null, ["callee:00c54d90:8"]]
- 00795660 bytes d0f91294
+ 00795a3c bytes d5fc1294
- 00795674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00795674 ["INT_ADD", "register:40f0:8", ["const:795674:8", "const:4:8"]]
- 00795674 ["CALLIND", null, ["register:0:8"]]
+ 00795a50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795a50 ["INT_ADD", "register:40f0:8", ["const:795a50:8", "const:4:8"]]
+ 00795a50 ["CALLIND", null, ["register:0:8"]]
- 00795674 bytes 00013fd6
+ 00795a50 bytes 00013fd6
- 0079567c ["INT_ADD", "register:40f0:8", ["const:79567c:8", "const:4:8"]]
- 0079567c ["CALL", null, ["callee:00c58f20:8"]]
+ 00795a58 ["INT_ADD", "register:40f0:8", ["const:795a58:8", "const:4:8"]]
+ 00795a58 ["CALL", null, ["callee:00c58f20:8"]]
- 0079567c bytes 350a1394
+ 00795a58 bytes 320d1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2941442a40bbdffdea9a347ca82ffbe5"></a>

### [`0079665c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md) → [`00796a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a38.md) FUN_00796a38

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 2件 [`0079668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md) [`00796b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md)
- 新版 呼出元 1件 [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md) · 呼出先 2件 [`00796a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a68.md) [`00796f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796f2c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00796674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md#insn-00796674)
- 新版 [`00796a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a38.md#insn-00796a50)

~~~diff
- 00796674 ["INT_ADD", "register:40f0:8", ["const:796674:8", "const:4:8"]]
- 00796674 ["CALL", null, ["callee:00796a68:8"]]
+ 00796a50 ["INT_ADD", "register:40f0:8", ["const:796a50:8", "const:4:8"]]
+ 00796a50 ["CALL", null, ["callee:00796a68:8"]]
- 00796674 bytes 06000094
+ 00796a50 bytes 06000094
~~~


<a id="compare-2de974983d35fbcdc878c3d09d0eeca2"></a>

### [`00798e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e2c.md) → [`00799208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799208.md) FUN_00799208

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008517dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00851/008517dc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00798e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e2c.md#insn-00798e60)
- 新版 [`0079923c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799208.md#insn-0079923c)

~~~diff
- 00798e60 ["INT_ADD", "register:40f0:8", ["const:798e60:8", "const:4:8"]]
- 00798e60 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079923c ["INT_ADD", "register:40f0:8", ["const:79923c:8", "const:4:8"]]
+ 0079923c ["CALL", null, ["callee:00c58f50:8"]]
- 00798e60 bytes 48fc1294
+ 0079923c bytes 45ff1294
~~~


<a id="compare-1bb3213753aab3da493b4bf7a787865f"></a>

### [`00798e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md) → [`00799258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799258.md) FUN_00799258

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) · 呼出先 4件 [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) [`0079fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fe88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008517dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00851/008517dc.md) · 呼出先 4件 [`0079d50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md) [`007a0264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0264.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00798ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ea0) · [`00798ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ea8) · [`00798ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md#insn-00798ebc)
- 新版 [`0079927c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799258.md#insn-0079927c) · [`00799284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799258.md#insn-00799284) · [`00799298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799258.md#insn-00799298)

~~~diff
- 00798ea0 ["INT_ADD", "register:40f0:8", ["const:798ea0:8", "const:4:8"]]
- 00798ea0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079927c ["INT_ADD", "register:40f0:8", ["const:79927c:8", "const:4:8"]]
+ 0079927c ["CALL", null, ["callee:00c58f30:8"]]
- 00798ea0 bytes 30fc1294
+ 0079927c bytes 2dff1294
- 00798ea8 ["INT_ADD", "register:40f0:8", ["const:798ea8:8", "const:4:8"]]
- 00798ea8 ["CALL", null, ["callee:007a0264:8"]]
+ 00799284 ["INT_ADD", "register:40f0:8", ["const:799284:8", "const:4:8"]]
+ 00799284 ["CALL", null, ["callee:007a0264:8"]]
- 00798ea8 bytes f81b0094
+ 00799284 bytes f81b0094
- 00798ebc ["INT_ADD", "register:40f0:8", ["const:798ebc:8", "const:4:8"]]
- 00798ebc ["CALL", null, ["callee:0079d50c:8"]]
+ 00799298 ["INT_ADD", "register:40f0:8", ["const:799298:8", "const:4:8"]]
+ 00799298 ["CALL", null, ["callee:0079d50c:8"]]
- 00798ebc bytes 9d100094
+ 00799298 bytes 9d100094
~~~


<a id="compare-6e420854b31e35cb7fe323d7a256c3ad"></a>

### [`00799c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md) → [`0079a040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a040.md) FUN_0079a040

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00799cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md#insn-00799cac) · [`00799cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799c64.md#insn-00799cbc)
- 新版 [`0079a088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a040.md#insn-0079a088) · [`0079a098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a040.md#insn-0079a098)

~~~diff
- 00799cac ["INT_ADD", "register:40f0:8", ["const:799cac:8", "const:4:8"]]
- 00799cac ["CALL", null, ["callee:00c58f50:8"]]
+ 0079a088 ["INT_ADD", "register:40f0:8", ["const:79a088:8", "const:4:8"]]
+ 0079a088 ["CALL", null, ["callee:00c58f50:8"]]
- 00799cac bytes b5f81294
+ 0079a088 bytes b2fb1294
- 00799cbc ["INT_ADD", "register:40f0:8", ["const:799cbc:8", "const:4:8"]]
- 00799cbc ["CALL", null, ["callee:00c58f50:8"]]
+ 0079a098 ["INT_ADD", "register:40f0:8", ["const:79a098:8", "const:4:8"]]
+ 0079a098 ["CALL", null, ["callee:00c58f50:8"]]
- 00799cbc bytes b1f81294
+ 0079a098 bytes aefb1294
~~~


<a id="compare-12130c7ed544a9ea33b83c6e604d4572"></a>

### [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md) → [`0079d3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md) FUN_0079d3a8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) · 呼出先 5件 [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`0079d044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d044.md) [`007a13d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md) · 呼出先 5件 [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d020) · [`0079d084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d084) · [`0079d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md#insn-0079d0ac)
- 新版 [`0079d3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md#insn-0079d3fc) · [`0079d460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md#insn-0079d460) · [`0079d488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md#insn-0079d488)

~~~diff
- 0079d020 ["INT_ADD", "register:40f0:8", ["const:79d020:8", "const:4:8"]]
- 0079d020 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d3fc ["INT_ADD", "register:40f0:8", ["const:79d3fc:8", "const:4:8"]]
+ 0079d3fc ["CALL", null, ["callee:00c58f50:8"]]
- 0079d020 bytes d8eb1294
+ 0079d3fc bytes d5ee1294
- 0079d084 ["INT_ADD", "register:40f0:8", ["const:79d084:8", "const:4:8"]]
- 0079d084 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079d460 ["INT_ADD", "register:40f0:8", ["const:79d460:8", "const:4:8"]]
+ 0079d460 ["CALL", null, ["callee:00c58f30:8"]]
- 0079d084 bytes b7eb1294
+ 0079d460 bytes b4ee1294
- 0079d0ac ["INT_ADD", "register:40f0:8", ["const:79d0ac:8", "const:4:8"]]
- 0079d0ac ["CALL", null, ["callee:00c590a0:8"]]
+ 0079d488 ["INT_ADD", "register:40f0:8", ["const:79d488:8", "const:4:8"]]
+ 0079d488 ["CALL", null, ["callee:00c590a0:8"]]
- 0079d0ac bytes 09ec1294
+ 0079d488 bytes 06ef1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1848faba0aeb9cc838ac13045af1fd0"></a>

### [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) → [`0079d50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md) FUN_0079d50c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`00798e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798e7c.md) · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00797f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md) [`00799258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/00799258.md) · 呼出先 2件 [`005a4868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4868.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d178) · [`0079d188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d188) · [`0079d198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md#insn-0079d198)
- 新版 [`0079d554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md#insn-0079d554) · [`0079d564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md#insn-0079d564) · [`0079d574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md#insn-0079d574)

~~~diff
- 0079d178 ["INT_ADD", "register:40f0:8", ["const:79d178:8", "const:4:8"]]
- 0079d178 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d554 ["INT_ADD", "register:40f0:8", ["const:79d554:8", "const:4:8"]]
+ 0079d554 ["CALL", null, ["callee:00c58f50:8"]]
- 0079d178 bytes 82eb1294
+ 0079d554 bytes 7fee1294
- 0079d188 ["INT_ADD", "register:40f0:8", ["const:79d188:8", "const:4:8"]]
- 0079d188 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d564 ["INT_ADD", "register:40f0:8", ["const:79d564:8", "const:4:8"]]
+ 0079d564 ["CALL", null, ["callee:00c58f50:8"]]
- 0079d188 bytes 7eeb1294
+ 0079d564 bytes 7bee1294
- 0079d198 ["INT_ADD", "register:40f0:8", ["const:79d198:8", "const:4:8"]]
- 0079d198 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d574 ["INT_ADD", "register:40f0:8", ["const:79d574:8", "const:4:8"]]
+ 0079d574 ["CALL", null, ["callee:00c58f50:8"]]
- 0079d198 bytes 7aeb1294
+ 0079d574 bytes 77ee1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c9afb56735ab4b4b1343828eaa4799"></a>

### [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) → [`0079d5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md) FUN_0079d5ac

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) · 呼出先 2件 [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00797f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md) [`0079d5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md) · 呼出先 2件 [`0079d5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d1ec) · [`0079d1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d1f8) · [`0079d22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md#insn-0079d22c)
- 新版 [`0079d5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md#insn-0079d5c8) · [`0079d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md#insn-0079d5d4) · [`0079d608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md#insn-0079d608)

~~~diff
- 0079d1ec ["INT_ADD", "register:40f0:8", ["const:79d1ec:8", "const:4:8"]]
- 0079d1ec ["CALL", null, ["local:b0:8"]]
+ 0079d5c8 ["INT_ADD", "register:40f0:8", ["const:79d5c8:8", "const:4:8"]]
+ 0079d5c8 ["CALL", null, ["local:b0:8"]]
- 0079d1ec bytes f9ffff97
+ 0079d5c8 bytes f9ffff97
- 0079d1f8 ["INT_ADD", "register:40f0:8", ["const:79d1f8:8", "const:4:8"]]
- 0079d1f8 ["CALL", null, ["local:b0:8"]]
+ 0079d5d4 ["INT_ADD", "register:40f0:8", ["const:79d5d4:8", "const:4:8"]]
+ 0079d5d4 ["CALL", null, ["local:b0:8"]]
- 0079d1f8 bytes f6ffff97
+ 0079d5d4 bytes f6ffff97
- 0079d22c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d22c ["INT_ADD", "register:40f0:8", ["const:79d22c:8", "const:4:8"]]
- 0079d22c ["CALLIND", null, ["register:0:8"]]
+ 0079d608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d608 ["INT_ADD", "register:40f0:8", ["const:79d608:8", "const:4:8"]]
+ 0079d608 ["CALLIND", null, ["register:0:8"]]
- 0079d22c bytes 00013fd6
+ 0079d608 bytes 00013fd6
~~~


<a id="compare-2bc9ea1dca153c8a026d1ff5b346ff10"></a>

### [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) → [`0079d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md) FUN_0079d61c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) · 呼出先 2件 [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00797f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md) [`0079d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md) · 呼出先 2件 [`0079d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d25c) · [`0079d268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d268) · [`0079d29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md#insn-0079d29c)
- 新版 [`0079d638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md#insn-0079d638) · [`0079d644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md#insn-0079d644) · [`0079d678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md#insn-0079d678)

~~~diff
- 0079d25c ["INT_ADD", "register:40f0:8", ["const:79d25c:8", "const:4:8"]]
- 0079d25c ["CALL", null, ["local:b0:8"]]
+ 0079d638 ["INT_ADD", "register:40f0:8", ["const:79d638:8", "const:4:8"]]
+ 0079d638 ["CALL", null, ["local:b0:8"]]
- 0079d25c bytes f9ffff97
+ 0079d638 bytes f9ffff97
- 0079d268 ["INT_ADD", "register:40f0:8", ["const:79d268:8", "const:4:8"]]
- 0079d268 ["CALL", null, ["local:b0:8"]]
+ 0079d644 ["INT_ADD", "register:40f0:8", ["const:79d644:8", "const:4:8"]]
+ 0079d644 ["CALL", null, ["local:b0:8"]]
- 0079d268 bytes f6ffff97
+ 0079d644 bytes f6ffff97
- 0079d29c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d29c ["INT_ADD", "register:40f0:8", ["const:79d29c:8", "const:4:8"]]
- 0079d29c ["CALLIND", null, ["register:0:8"]]
+ 0079d678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d678 ["INT_ADD", "register:40f0:8", ["const:79d678:8", "const:4:8"]]
+ 0079d678 ["CALLIND", null, ["register:0:8"]]
- 0079d29c bytes 00013fd6
+ 0079d678 bytes 00013fd6
~~~


<a id="compare-f1b028292c9d4197e18488f3b31967a3"></a>

### [`0079d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md) → [`0079d68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d68c.md) FUN_0079d68c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00797bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00797fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797fb8.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d31c) · [`0079d32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d32c) · [`0079d34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md#insn-0079d34c)
- 新版 [`0079d6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d68c.md#insn-0079d6f8) · [`0079d708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d68c.md#insn-0079d708) · [`0079d728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d68c.md#insn-0079d728)

~~~diff
- 0079d31c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d31c ["INT_ADD", "register:40f0:8", ["const:79d31c:8", "const:4:8"]]
- 0079d31c ["CALLIND", null, ["register:0:8"]]
+ 0079d6f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d6f8 ["INT_ADD", "register:40f0:8", ["const:79d6f8:8", "const:4:8"]]
+ 0079d6f8 ["CALLIND", null, ["register:0:8"]]
- 0079d31c bytes 00013fd6
+ 0079d6f8 bytes 00013fd6
- 0079d32c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d32c ["INT_ADD", "register:40f0:8", ["const:79d32c:8", "const:4:8"]]
- 0079d32c ["CALLIND", null, ["register:0:8"]]
+ 0079d708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d708 ["INT_ADD", "register:40f0:8", ["const:79d708:8", "const:4:8"]]
+ 0079d708 ["CALLIND", null, ["register:0:8"]]
- 0079d32c bytes 00013fd6
+ 0079d708 bytes 00013fd6
- 0079d34c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079d34c ["INT_ADD", "register:40f0:8", ["const:79d34c:8", "const:4:8"]]
- 0079d34c ["CALLIND", null, ["register:0:8"]]
+ 0079d728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079d728 ["INT_ADD", "register:40f0:8", ["const:79d728:8", "const:4:8"]]
+ 0079d728 ["CALLIND", null, ["register:0:8"]]
- 0079d34c bytes 00013fd6
+ 0079d728 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b0ebacfc6f124311ab1a920bd60854"></a>

### [`0079d4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md) → [`0079d8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d8a4.md) FUN_0079d8a4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0079d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079a0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a0c8.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0079d9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d9ec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d530) · [`0079d5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d5cc) · [`0079d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md#insn-0079d5e8)
- 新版 [`0079d90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d8a4.md#insn-0079d90c) · [`0079d9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d8a4.md#insn-0079d9a8) · [`0079d9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d8a4.md#insn-0079d9c4)

~~~diff
- 0079d530 ["INT_ADD", "register:40f0:8", ["const:79d530:8", "const:4:8"]]
- 0079d530 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079d90c ["INT_ADD", "register:40f0:8", ["const:79d90c:8", "const:4:8"]]
+ 0079d90c ["CALL", null, ["callee:00c58f30:8"]]
- 0079d530 bytes 8cea1294
+ 0079d90c bytes 89ed1294
- 0079d5cc ["INT_ADD", "register:40f0:8", ["const:79d5cc:8", "const:4:8"]]
- 0079d5cc ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d9a8 ["INT_ADD", "register:40f0:8", ["const:79d9a8:8", "const:4:8"]]
+ 0079d9a8 ["CALL", null, ["callee:00c58f50:8"]]
- 0079d5cc bytes 6dea1294
+ 0079d9a8 bytes 6aed1294
- 0079d5e8 ["INT_ADD", "register:40f0:8", ["const:79d5e8:8", "const:4:8"]]
- 0079d5e8 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d9c4 ["INT_ADD", "register:40f0:8", ["const:79d9c4:8", "const:4:8"]]
+ 0079d9c4 ["CALL", null, ["callee:00c58f50:8"]]
- 0079d5e8 bytes 66ea1294
+ 0079d9c4 bytes 63ed1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae0943a2b60c2703b0e3c58a125696a5"></a>

### [`0079dd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd6c.md) → [`0079e148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e148.md) FUN_0079e148

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd6c.md#insn-0079dde0)
- 新版 [`0079e1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e148.md#insn-0079e1bc)

~~~diff
- 0079dde0 ["INT_ADD", "register:40f0:8", ["const:79dde0:8", "const:4:8"]]
- 0079dde0 ["CALL", null, ["callee:0045a0d4:8"]]
+ 0079e1bc ["INT_ADD", "register:40f0:8", ["const:79e1bc:8", "const:4:8"]]
+ 0079e1bc ["CALL", null, ["callee:0045a0d4:8"]]
- 0079dde0 bytes f5eff297
+ 0079e1bc bytes c6eff297
~~~


<a id="compare-49cc153a9c1ae2b3306e3b7e39654ec3"></a>

### [`0079e770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e770.md) → [`0079eb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079eb4c.md) FUN_0079eb4c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079e78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e770.md#insn-0079e78c)
- 新版 [`0079eb68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079eb4c.md#insn-0079eb68)

~~~diff
- 0079e78c ["INT_ADD", "register:40f0:8", ["const:79e78c:8", "const:4:8"]]
- 0079e78c ["CALL", null, ["callee:0045a0d4:8"]]
+ 0079eb68 ["INT_ADD", "register:40f0:8", ["const:79eb68:8", "const:4:8"]]
+ 0079eb68 ["CALL", null, ["callee:0045a0d4:8"]]
- 0079e78c bytes 8aedf297
+ 0079eb68 bytes 5bedf297
~~~


<a id="compare-fae24d030c8f8eaa3afaf45ba1edbbca"></a>

### [`0079f104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f104.md) → [`0079f4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f4e0.md) FUN_0079f4e0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079f120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f104.md#insn-0079f120)
- 新版 [`0079f4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f4e0.md#insn-0079f4fc)

~~~diff
- 0079f120 ["INT_ADD", "register:40f0:8", ["const:79f120:8", "const:4:8"]]
- 0079f120 ["CALL", null, ["callee:0045a0d4:8"]]
+ 0079f4fc ["INT_ADD", "register:40f0:8", ["const:79f4fc:8", "const:4:8"]]
+ 0079f4fc ["CALL", null, ["callee:0045a0d4:8"]]
- 0079f120 bytes 25ebf297
+ 0079f4fc bytes f6eaf297
~~~


<a id="compare-863a66bd176e1a483d7dfe39b594fc6f"></a>

### [`007a0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md) → [`007a0b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0b3c.md) FUN_007a0b3c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) [`007a3760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a3/007a3760.md) [`007a4234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a4/007a4234.md) [`007a5298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5298.md) [`007a6180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a6/007a6180.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 9件 [`007a2438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2438.md) [`007a3b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a3/007a3b3c.md) [`007a4610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a4/007a4610.md) [`007a5674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a5/007a5674.md) [`007a655c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a6/007a655c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a077c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0760.md#insn-007a077c)
- 新版 [`007a0b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0b3c.md#insn-007a0b58)

~~~diff
- 007a077c ["INT_ADD", "register:40f0:8", ["const:7a077c:8", "const:4:8"]]
- 007a077c ["CALL", null, ["callee:00c58f50:8"]]
+ 007a0b58 ["INT_ADD", "register:40f0:8", ["const:7a0b58:8", "const:4:8"]]
+ 007a0b58 ["CALL", null, ["callee:00c58f50:8"]]
- 007a077c bytes 01de1294
+ 007a0b58 bytes fee01294
~~~


<a id="compare-e43926d65636ab3d382e8c633c019895"></a>

### [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md) → [`007a0bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md) FUN_007a0bb8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007980b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md) [`0079826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md) · 呼出先 10件 [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b0dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 2件 [`00798494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798494.md) [`00798648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798648.md) · 呼出先 10件 [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`007a0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b0ef94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0e/00b0ef94.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a08a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08a0) · [`007a08bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08bc) · [`007a08dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md#insn-007a08dc)
- 新版 [`007a0c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md#insn-007a0c7c) · [`007a0c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md#insn-007a0c98) · [`007a0cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md#insn-007a0cb8)

~~~diff
- 007a08a0 ["INT_ADD", "register:40f0:8", ["const:7a08a0:8", "const:4:8"]]
- 007a08a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 007a0c7c ["INT_ADD", "register:40f0:8", ["const:7a0c7c:8", "const:4:8"]]
+ 007a0c7c ["CALL", null, ["callee:00c58f30:8"]]
- 007a08a0 bytes b0dd1294
+ 007a0c7c bytes ade01294
- 007a08bc ["INT_ADD", "register:40f0:8", ["const:7a08bc:8", "const:4:8"]]
- 007a08bc ["CALL", null, ["callee:00c590a0:8"]]
+ 007a0c98 ["INT_ADD", "register:40f0:8", ["const:7a0c98:8", "const:4:8"]]
+ 007a0c98 ["CALL", null, ["callee:00c590a0:8"]]
- 007a08bc bytes 05de1294
+ 007a0c98 bytes 02e11294
- 007a08dc ["INT_ADD", "register:40f0:8", ["const:7a08dc:8", "const:4:8"]]
- 007a08dc ["CALL", null, ["callee:007a0ee4:8"]]
+ 007a0cb8 ["INT_ADD", "register:40f0:8", ["const:7a0cb8:8", "const:4:8"]]
+ 007a0cb8 ["CALL", null, ["callee:007a0ee4:8"]]
- 007a08dc bytes 8b000094
+ 007a0cb8 bytes 8b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c3280f475c8a9976a5c2fbe3c4916d0"></a>

### [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) → [`007a0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md) FUN_007a0ee4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00737ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00737/00737ccc.md) [`007a0b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`007a0bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md) [`007a0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`0073807c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00738/0073807c.md) [`007a0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a0bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0bac) · [`007a0c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0c78) · [`007a0cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0b08.md#insn-007a0cac)
- 新版 [`007a0f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md#insn-007a0f88) · [`007a1054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md#insn-007a1054) · [`007a1088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0ee4.md#insn-007a1088)

~~~diff
- 007a0bac ["INT_ADD", "register:40f0:8", ["const:7a0bac:8", "const:4:8"]]
- 007a0bac ["CALL", null, ["callee:0073807c:8"]]
+ 007a0f88 ["INT_ADD", "register:40f0:8", ["const:7a0f88:8", "const:4:8"]]
+ 007a0f88 ["CALL", null, ["callee:0073807c:8"]]
- 007a0bac bytes 485cfe97
+ 007a0f88 bytes 3d5cfe97
- 007a0c78 ["INT_ADD", "register:40f0:8", ["const:7a0c78:8", "const:4:8"]]
- 007a0c78 ["CALL", null, ["callee:00c58f30:8"]]
+ 007a1054 ["INT_ADD", "register:40f0:8", ["const:7a1054:8", "const:4:8"]]
+ 007a1054 ["CALL", null, ["callee:00c58f30:8"]]
- 007a0c78 bytes badc1294
+ 007a1054 bytes b7df1294
- 007a0cac ["INT_ADD", "register:40f0:8", ["const:7a0cac:8", "const:4:8"]]
- 007a0cac ["CALL", null, ["callee:00c590a0:8"]]
+ 007a1088 ["INT_ADD", "register:40f0:8", ["const:7a1088:8", "const:4:8"]]
+ 007a1088 ["CALL", null, ["callee:00c590a0:8"]]
- 007a0cac bytes 09dd1294
+ 007a1088 bytes 06e01294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d2b7bcf280c0c4a016a345b2975536"></a>

### [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) → [`007a13d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md) FUN_007a13d4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 8件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md) [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md)
- 新版 呼出元 1件 [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md) · 呼出先 8件 [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md) [`005981a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/005981a8.md) [`0079d3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md) [`007a2078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md) [`007a22a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1034) · [`007a1054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1054) · [`007a1078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md#insn-007a1078)
- 新版 [`007a1410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md#insn-007a1410) · [`007a1430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md#insn-007a1430) · [`007a1454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md#insn-007a1454)

~~~diff
- 007a1034 ["INT_ADD", "register:40f0:8", ["const:7a1034:8", "const:4:8"]]
- 007a1034 ["CALL", null, ["callee:005979bc:8"]]
+ 007a1410 ["INT_ADD", "register:40f0:8", ["const:7a1410:8", "const:4:8"]]
+ 007a1410 ["CALL", null, ["callee:005979bc:8"]]
- 007a1034 bytes 9ad9f797
+ 007a1410 bytes 6bd9f797
- 007a1054 ["INT_ADD", "register:40f0:8", ["const:7a1054:8", "const:4:8"]]
- 007a1054 ["CALL", null, ["callee:005981a8:8"]]
+ 007a1430 ["INT_ADD", "register:40f0:8", ["const:7a1430:8", "const:4:8"]]
+ 007a1430 ["CALL", null, ["callee:005981a8:8"]]
- 007a1054 bytes 8ddbf797
+ 007a1430 bytes 5edbf797
- 007a1078 ["INT_ADD", "register:40f0:8", ["const:7a1078:8", "const:4:8"]]
- 007a1078 ["CALL", null, ["callee:00c594d0:8"]]
+ 007a1454 ["INT_ADD", "register:40f0:8", ["const:7a1454:8", "const:4:8"]]
+ 007a1454 ["CALL", null, ["callee:00c594d0:8"]]
- 007a1078 bytes 22dd1294
+ 007a1454 bytes 1fe01294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea3bd962d9e9b1e1b1df5a5a527fc6f"></a>

### [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) → [`007a1544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md) FUN_007a1544

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`007a1668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md)
- 新版 呼出元 1件 [`007992d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/007992d4.md) · 呼出先 13件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00597dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597dec.md) [`005981a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/005981a8.md) [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`007a1a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1a44.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a11a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a11a4) · [`007a11dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a11dc) · [`007a1264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md#insn-007a1264)
- 新版 [`007a1580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md#insn-007a1580) · [`007a15b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md#insn-007a15b8) · [`007a1640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md#insn-007a1640)

~~~diff
- 007a11a4 ["INT_ADD", "register:40f0:8", ["const:7a11a4:8", "const:4:8"]]
- 007a11a4 ["CALL", null, ["callee:005981a8:8"]]
+ 007a1580 ["INT_ADD", "register:40f0:8", ["const:7a1580:8", "const:4:8"]]
+ 007a1580 ["CALL", null, ["callee:005981a8:8"]]
- 007a11a4 bytes 39dbf797
+ 007a1580 bytes 0adbf797
- 007a11dc ["INT_ADD", "register:40f0:8", ["const:7a11dc:8", "const:4:8"]]
- 007a11dc ["CALL", null, ["callee:007a2438:8"]]
+ 007a15b8 ["INT_ADD", "register:40f0:8", ["const:7a15b8:8", "const:4:8"]]
+ 007a15b8 ["CALL", null, ["callee:007a2438:8"]]
- 007a11dc bytes a0030094
+ 007a15b8 bytes a0030094
- 007a1264 ["INT_ADD", "register:40f0:8", ["const:7a1264:8", "const:4:8"]]
- 007a1264 ["CALL", null, ["callee:0043be80:8"]]
+ 007a1640 ["INT_ADD", "register:40f0:8", ["const:7a1640:8", "const:4:8"]]
+ 007a1640 ["CALL", null, ["callee:0043be80:8"]]
- 007a1264 bytes 3f6af297
+ 007a1640 bytes 106af297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b195693a1eaf0e380db667ef18b8e84"></a>

### [`007a1668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md) → [`007a1a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1a44.md) FUN_007a1a44

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007a1544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1728) · [`007a1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1754) · [`007a1790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1668.md#insn-007a1790)
- 新版 [`007a1b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1a44.md#insn-007a1b04) · [`007a1b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1a44.md#insn-007a1b30) · [`007a1b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1a44.md#insn-007a1b6c)

~~~diff
- 007a1728 ["INT_ADD", "register:40f0:8", ["const:7a1728:8", "const:4:8"]]
- 007a1728 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1b04 ["INT_ADD", "register:40f0:8", ["const:7a1b04:8", "const:4:8"]]
+ 007a1b04 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1728 bytes 16da1294
+ 007a1b04 bytes 13dd1294
- 007a1754 ["INT_ADD", "register:40f0:8", ["const:7a1754:8", "const:4:8"]]
- 007a1754 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1b30 ["INT_ADD", "register:40f0:8", ["const:7a1b30:8", "const:4:8"]]
+ 007a1b30 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1754 bytes 0bda1294
+ 007a1b30 bytes 08dd1294
- 007a1790 ["INT_ADD", "register:40f0:8", ["const:7a1790:8", "const:4:8"]]
- 007a1790 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1b6c ["INT_ADD", "register:40f0:8", ["const:7a1b6c:8", "const:4:8"]]
+ 007a1b6c ["CALL", null, ["callee:00c58f50:8"]]
- 007a1790 bytes fcd91294
+ 007a1b6c bytes f9dc1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f609ee49b97ae87a5b9f8d28a830ecc3"></a>

### [`007a17cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md) → [`007a1ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ba8.md) FUN_007a1ba8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007a1544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md) · 呼出先 3件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a182c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a182c) · [`007a18bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a18bc) · [`007a18cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a17cc.md#insn-007a18cc)
- 新版 [`007a1c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ba8.md#insn-007a1c08) · [`007a1c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ba8.md#insn-007a1c98) · [`007a1ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ba8.md#insn-007a1ca8)

~~~diff
- 007a182c ["INT_ADD", "register:40f0:8", ["const:7a182c:8", "const:4:8"]]
- 007a182c ["CALL", null, ["callee:00c58f30:8"]]
+ 007a1c08 ["INT_ADD", "register:40f0:8", ["const:7a1c08:8", "const:4:8"]]
+ 007a1c08 ["CALL", null, ["callee:00c58f30:8"]]
- 007a182c bytes cdd91294
+ 007a1c08 bytes cadc1294
- 007a18bc ["INT_ADD", "register:40f0:8", ["const:7a18bc:8", "const:4:8"]]
- 007a18bc ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1c98 ["INT_ADD", "register:40f0:8", ["const:7a1c98:8", "const:4:8"]]
+ 007a1c98 ["CALL", null, ["callee:00c58f50:8"]]
- 007a18bc bytes b1d91294
+ 007a1c98 bytes aedc1294
- 007a18cc ["INT_ADD", "register:40f0:8", ["const:7a18cc:8", "const:4:8"]]
- 007a18cc ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1ca8 ["INT_ADD", "register:40f0:8", ["const:7a1ca8:8", "const:4:8"]]
+ 007a1ca8 ["CALL", null, ["callee:00c58f50:8"]]
- 007a18cc bytes add91294
+ 007a1ca8 bytes aadc1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf84d927d5b52c4edea758ae165844b"></a>

### [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) → [`007a1d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md) FUN_007a1d04

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1168.md) · 呼出先 6件 [`007a1a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md) [`007a1b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md) [`007a1b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`007a1544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1544.md) · 呼出先 6件 [`007a1e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1e4c.md) [`007a1ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ee4.md) [`007a1f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1f5c.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a1984) · [`007a19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a19cc) · [`007a1a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md#insn-007a1a30)
- 新版 [`007a1d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md#insn-007a1d60) · [`007a1da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md#insn-007a1da8) · [`007a1e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md#insn-007a1e0c)

~~~diff
- 007a1984 ["INT_ADD", "register:40f0:8", ["const:7a1984:8", "const:4:8"]]
- 007a1984 ["CALL", null, ["callee:00c58f30:8"]]
+ 007a1d60 ["INT_ADD", "register:40f0:8", ["const:7a1d60:8", "const:4:8"]]
+ 007a1d60 ["CALL", null, ["callee:00c58f30:8"]]
- 007a1984 bytes 77d91294
+ 007a1d60 bytes 74dc1294
- 007a19cc ["INT_ADD", "register:40f0:8", ["const:7a19cc:8", "const:4:8"]]
- 007a19cc ["CALL", null, ["callee:007a1f5c:8"]]
+ 007a1da8 ["INT_ADD", "register:40f0:8", ["const:7a1da8:8", "const:4:8"]]
+ 007a1da8 ["CALL", null, ["callee:007a1f5c:8"]]
- 007a19cc bytes 6d000094
+ 007a1da8 bytes 6d000094
- 007a1a30 ["INT_ADD", "register:40f0:8", ["const:7a1a30:8", "const:4:8"]]
- 007a1a30 ["CALL", null, ["callee:007a1ee4:8"]]
+ 007a1e0c ["INT_ADD", "register:40f0:8", ["const:7a1e0c:8", "const:4:8"]]
+ 007a1e0c ["CALL", null, ["callee:007a1ee4:8"]]
- 007a1a30 bytes 36000094
+ 007a1e0c bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f600ec2d0976702ebcf3627b0d59701"></a>

### [`007a1a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md) → [`007a1e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1e4c.md) FUN_007a1e4c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007a1d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md#insn-007a1ad4) · [`007a1ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1a70.md#insn-007a1ae4)
- 新版 [`007a1eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1e4c.md#insn-007a1eb0) · [`007a1ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1e4c.md#insn-007a1ec0)

~~~diff
- 007a1ad4 ["INT_ADD", "register:40f0:8", ["const:7a1ad4:8", "const:4:8"]]
- 007a1ad4 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1eb0 ["INT_ADD", "register:40f0:8", ["const:7a1eb0:8", "const:4:8"]]
+ 007a1eb0 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1ad4 bytes 2bd91294
+ 007a1eb0 bytes 28dc1294
- 007a1ae4 ["INT_ADD", "register:40f0:8", ["const:7a1ae4:8", "const:4:8"]]
- 007a1ae4 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1ec0 ["INT_ADD", "register:40f0:8", ["const:7a1ec0:8", "const:4:8"]]
+ 007a1ec0 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1ae4 bytes 27d91294
+ 007a1ec0 bytes 24dc1294
~~~


<a id="compare-de1fa5f5c4b05c457d76f6ed08065bd2"></a>

### [`007a1b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md) → [`007a1ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ef8.md) FUN_007a1ef8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md#insn-007a1b5c) · [`007a1b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b1c.md#insn-007a1b6c)
- 新版 [`007a1f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ef8.md#insn-007a1f38) · [`007a1f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ef8.md#insn-007a1f48)

~~~diff
- 007a1b5c ["INT_ADD", "register:40f0:8", ["const:7a1b5c:8", "const:4:8"]]
- 007a1b5c ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1f38 ["INT_ADD", "register:40f0:8", ["const:7a1f38:8", "const:4:8"]]
+ 007a1f38 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1b5c bytes 09d91294
+ 007a1f38 bytes 06dc1294
- 007a1b6c ["INT_ADD", "register:40f0:8", ["const:7a1b6c:8", "const:4:8"]]
- 007a1b6c ["CALL", null, ["callee:00c58f50:8"]]
+ 007a1f48 ["INT_ADD", "register:40f0:8", ["const:7a1f48:8", "const:4:8"]]
+ 007a1f48 ["CALL", null, ["callee:00c58f50:8"]]
- 007a1b6c bytes 05d91294
+ 007a1f48 bytes 02dc1294
~~~


<a id="compare-083067b5e08f2c97e4ba88e0903a15dd"></a>

### [`007a1b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md) → [`007a1f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1f5c.md) FUN_007a1f5c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007a1d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1d04.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1be0) · [`007a1c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1c24) · [`007a1c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b80.md#insn-007a1c3c)
- 新版 [`007a1fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1f5c.md#insn-007a1fbc) · [`007a2000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1f5c.md#insn-007a2000) · [`007a2018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1f5c.md#insn-007a2018)

~~~diff
- 007a1be0 ["INT_ADD", "register:40f0:8", ["const:7a1be0:8", "const:4:8"]]
- 007a1be0 ["CALL", null, ["callee:0043be80:8"]]
+ 007a1fbc ["INT_ADD", "register:40f0:8", ["const:7a1fbc:8", "const:4:8"]]
+ 007a1fbc ["CALL", null, ["callee:0043be80:8"]]
- 007a1be0 bytes e067f297
+ 007a1fbc bytes b167f297
- 007a1c24 ["INT_ADD", "register:40f0:8", ["const:7a1c24:8", "const:4:8"]]
- 007a1c24 ["CALL", null, ["callee:00c58f30:8"]]
+ 007a2000 ["INT_ADD", "register:40f0:8", ["const:7a2000:8", "const:4:8"]]
+ 007a2000 ["CALL", null, ["callee:00c58f30:8"]]
- 007a1c24 bytes cfd81294
+ 007a2000 bytes ccdb1294
- 007a1c3c ["INT_ADD", "register:40f0:8", ["const:7a1c3c:8", "const:4:8"]]
- 007a1c3c ["CALL", null, ["callee:00c590a0:8"]]
+ 007a2018 ["INT_ADD", "register:40f0:8", ["const:7a2018:8", "const:4:8"]]
+ 007a2018 ["CALL", null, ["callee:00c590a0:8"]]
- 007a1c3c bytes 25d91294
+ 007a2018 bytes 22dc1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fd460cf5f95ac5644e42a73c3d6e571"></a>

### [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) → [`007a2078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md) FUN_007a2078

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007a1b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md) [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`007a0468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0468.md) [`007a13d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`007a1ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a1ee4.md) [`007a22a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md#insn-007a1d3c) · [`007a1d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md#insn-007a1d64) · [`007a1e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md#insn-007a1e10)
- 新版 [`007a2118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md#insn-007a2118) · [`007a2140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md#insn-007a2140) · [`007a21ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md#insn-007a21ec)

~~~diff
- 007a1d3c ["INT_ADD", "register:40f0:8", ["const:7a1d3c:8", "const:4:8"]]
- 007a1d3c ["CALL", null, ["callee:00c58f30:8"]]
+ 007a2118 ["INT_ADD", "register:40f0:8", ["const:7a2118:8", "const:4:8"]]
+ 007a2118 ["CALL", null, ["callee:00c58f30:8"]]
- 007a1d3c bytes 89d81294
+ 007a2118 bytes 86db1294
- 007a1d64 ["INT_ADD", "register:40f0:8", ["const:7a1d64:8", "const:4:8"]]
- 007a1d64 ["CALL", null, ["callee:007a22a0:8"]]
+ 007a2140 ["INT_ADD", "register:40f0:8", ["const:7a2140:8", "const:4:8"]]
+ 007a2140 ["CALL", null, ["callee:007a22a0:8"]]
- 007a1d64 bytes 58000094
+ 007a2140 bytes 58000094
- 007a1e10 ["INT_ADD", "register:40f0:8", ["const:7a1e10:8", "const:4:8"]]
- 007a1e10 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a21ec ["INT_ADD", "register:40f0:8", ["const:7a21ec:8", "const:4:8"]]
+ 007a21ec ["CALL", null, ["callee:00c58f50:8"]]
- 007a1e10 bytes 5cd81294
+ 007a21ec bytes 59db1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88d1dbdff0a59b4cef0d1cb91097580a"></a>

### [`007a1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md) → [`007a22a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md) FUN_007a22a0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) [`007a0ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a0ff8.md) [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`007a0468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0468.md) [`007a13d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a1/007a13d4.md) [`007a2078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2078.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a1f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md#insn-007a1f24) · [`007a1f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md#insn-007a1f68) · [`007a1f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1ec4.md#insn-007a1f80)
- 新版 [`007a2300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md#insn-007a2300) · [`007a2344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md#insn-007a2344) · [`007a235c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a22a0.md#insn-007a235c)

~~~diff
- 007a1f24 ["INT_ADD", "register:40f0:8", ["const:7a1f24:8", "const:4:8"]]
- 007a1f24 ["CALL", null, ["callee:0043be80:8"]]
+ 007a2300 ["INT_ADD", "register:40f0:8", ["const:7a2300:8", "const:4:8"]]
+ 007a2300 ["CALL", null, ["callee:0043be80:8"]]
- 007a1f24 bytes 0f67f297
+ 007a2300 bytes e066f297
- 007a1f68 ["INT_ADD", "register:40f0:8", ["const:7a1f68:8", "const:4:8"]]
- 007a1f68 ["CALL", null, ["callee:00c58f30:8"]]
+ 007a2344 ["INT_ADD", "register:40f0:8", ["const:7a2344:8", "const:4:8"]]
+ 007a2344 ["CALL", null, ["callee:00c58f30:8"]]
- 007a1f68 bytes fed71294
+ 007a2344 bytes fbda1294
- 007a1f80 ["INT_ADD", "register:40f0:8", ["const:7a1f80:8", "const:4:8"]]
- 007a1f80 ["CALL", null, ["callee:00c590a0:8"]]
+ 007a235c ["INT_ADD", "register:40f0:8", ["const:7a235c:8", "const:4:8"]]
+ 007a235c ["CALL", null, ["callee:00c590a0:8"]]
- 007a1f80 bytes 54d81294
+ 007a235c bytes 51db1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fae2bb0b15cb35b4d82e07c43e5e745"></a>

### [`007a1fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1fe0.md) → [`007a23bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a23bc.md) FUN_007a23bc

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a201c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1fe0.md#insn-007a201c) · [`007a202c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1fe0.md#insn-007a202c)
- 新版 [`007a23f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a23bc.md#insn-007a23f8) · [`007a2408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a23bc.md#insn-007a2408)

~~~diff
- 007a201c ["INT_ADD", "register:40f0:8", ["const:7a201c:8", "const:4:8"]]
- 007a201c ["CALL", null, ["callee:00c58f50:8"]]
+ 007a23f8 ["INT_ADD", "register:40f0:8", ["const:7a23f8:8", "const:4:8"]]
+ 007a23f8 ["CALL", null, ["callee:00c58f50:8"]]
- 007a201c bytes d9d71294
+ 007a23f8 bytes d6da1294
- 007a202c ["INT_ADD", "register:40f0:8", ["const:7a202c:8", "const:4:8"]]
- 007a202c ["CALL", null, ["callee:00c58f50:8"]]
+ 007a2408 ["INT_ADD", "register:40f0:8", ["const:7a2408:8", "const:4:8"]]
+ 007a2408 ["CALL", null, ["callee:00c58f50:8"]]
- 007a202c bytes d5d71294
+ 007a2408 bytes d2da1294
~~~


<a id="compare-0d5646f9d7b6bccc04ce62816cb6afed"></a>

### [`007a5ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5ff0.md) → [`007a63cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a6/007a63cc.md) FUN_007a63cc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007a205c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a2/007a205c.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`007a2438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a2/007a2438.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007a60b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5ff0.md#insn-007a60b4) · [`007a6118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5ff0.md#insn-007a6118) · [`007a6140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a5/007a5ff0.md#insn-007a6140)
- 新版 [`007a6490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a6/007a63cc.md#insn-007a6490) · [`007a64f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a6/007a63cc.md#insn-007a64f4) · [`007a651c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a6/007a63cc.md#insn-007a651c)

~~~diff
- 007a60b4 ["INT_ADD", "register:40f0:8", ["const:7a60b4:8", "const:4:8"]]
- 007a60b4 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a6490 ["INT_ADD", "register:40f0:8", ["const:7a6490:8", "const:4:8"]]
+ 007a6490 ["CALL", null, ["callee:00c58f50:8"]]
- 007a60b4 bytes b3c71294
+ 007a6490 bytes b0ca1294
- 007a6118 ["INT_ADD", "register:40f0:8", ["const:7a6118:8", "const:4:8"]]
- 007a6118 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a64f4 ["INT_ADD", "register:40f0:8", ["const:7a64f4:8", "const:4:8"]]
+ 007a64f4 ["CALL", null, ["callee:00c58f50:8"]]
- 007a6118 bytes 9ac71294
+ 007a64f4 bytes 97ca1294
- 007a6140 ["INT_ADD", "register:40f0:8", ["const:7a6140:8", "const:4:8"]]
- 007a6140 ["CALL", null, ["callee:00c58f50:8"]]
+ 007a651c ["INT_ADD", "register:40f0:8", ["const:7a651c:8", "const:4:8"]]
+ 007a651c ["CALL", null, ["callee:00c58f50:8"]]
- 007a6140 bytes 90c71294
+ 007a651c bytes 8dca1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37151cc8ba3612d87369606030903f8a"></a>

### [`007aa7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md) → [`007aabac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007aa/007aabac.md) FUN_007aabac

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) · 呼出先 3件 [`00aa34d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa34d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`007ac08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac08c.md) · 呼出先 3件 [`00aa44c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa4/00aa44c4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aa7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md#insn-007aa7fc) · [`007aa80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md#insn-007aa80c) · [`007aa85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md#insn-007aa85c)
- 新版 [`007aabd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007aa/007aabac.md#insn-007aabd8) · [`007aabe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007aa/007aabac.md#insn-007aabe8) · [`007aac38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007aa/007aabac.md#insn-007aac38)

~~~diff
- 007aa7fc ["INT_ADD", "register:40f0:8", ["const:7aa7fc:8", "const:4:8"]]
- 007aa7fc ["CALL", null, ["callee:00aa44c4:8"]]
+ 007aabd8 ["INT_ADD", "register:40f0:8", ["const:7aabd8:8", "const:4:8"]]
+ 007aabd8 ["CALL", null, ["callee:00aa44c4:8"]]
- 007aa7fc bytes 35e30b94
+ 007aabd8 bytes 3be60b94
- 007aa80c ["INT_ADD", "register:40f0:8", ["const:7aa80c:8", "const:4:8"]]
- 007aa80c ["CALL", null, ["callee:00c58f50:8"]]
+ 007aabe8 ["INT_ADD", "register:40f0:8", ["const:7aabe8:8", "const:4:8"]]
+ 007aabe8 ["CALL", null, ["callee:00c58f50:8"]]
- 007aa80c bytes ddb51294
+ 007aabe8 bytes dab81294
- 007aa85c ["INT_ADD", "register:40f0:8", ["const:7aa85c:8", "const:4:8"]]
- 007aa85c ["CALL", null, ["callee:00c58f80:8"]]
+ 007aac38 ["INT_ADD", "register:40f0:8", ["const:7aac38:8", "const:4:8"]]
+ 007aac38 ["CALL", null, ["callee:00c58f80:8"]]
- 007aa85c bytes d5b51294
+ 007aac38 bytes d2b81294
~~~


<a id="compare-ec5167b713ec96f00a469d27c3962fbe"></a>

### [`007ae7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae7cc.md) → [`007aefb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ae/007aefb0.md) FUN_007aefb0

採用 · 移動量 `+0x7e4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007ab86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ab/007ab86c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007ae808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae7cc.md#insn-007ae808)
- 新版 [`007aefec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ae/007aefb0.md#insn-007aefec)

~~~diff
- 007ae808 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae808 ["INT_ADD", "register:40f0:8", ["const:7ae808:8", "const:4:8"]]
- 007ae808 ["CALLIND", null, ["register:0:8"]]
+ 007aefec ["COPY", "register:0:8", ["register:4040:8"]]
+ 007aefec ["INT_ADD", "register:40f0:8", ["const:7aefec:8", "const:4:8"]]
+ 007aefec ["CALLIND", null, ["register:0:8"]]
- 007ae808 bytes 00013fd6
+ 007aefec bytes 00013fd6
~~~


<a id="compare-ce96dac65bba3668d783c38399d89582"></a>

### [`007aef74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef74.md) → [`007af758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af758.md) FUN_007af758

採用 · 移動量 `+0x7e4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007ad9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007ade00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ad/007ade00.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007aef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef74.md#insn-007aef94)
- 新版 [`007af778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af758.md#insn-007af778)

~~~diff
- 007aef94 ["INT_ADD", "register:40f0:8", ["const:7aef94:8", "const:4:8"]]
- 007aef94 ["CALL", null, ["callee:00c58f50:8"]]
+ 007af778 ["INT_ADD", "register:40f0:8", ["const:7af778:8", "const:4:8"]]
+ 007af778 ["CALL", null, ["callee:00c58f50:8"]]
- 007aef94 bytes fba31294
+ 007af778 bytes f6a51294
~~~


<a id="compare-d3b6d3a01ad05f4e78630fd15847aeae"></a>

### [`007af4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af4d4.md) → [`007afef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007afef8.md) FUN_007afef8

採用 · 移動量 `+0xa24` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`007abbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ab/007abbbc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af4d4.md#insn-007af510)
- 新版 [`007aff34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007afef8.md#insn-007aff34)

~~~diff
- 007af510 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af510 ["INT_ADD", "register:40f0:8", ["const:7af510:8", "const:4:8"]]
- 007af510 ["CALLIND", null, ["register:0:8"]]
+ 007aff34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007aff34 ["INT_ADD", "register:40f0:8", ["const:7aff34:8", "const:4:8"]]
+ 007aff34 ["CALLIND", null, ["register:0:8"]]
- 007af510 bytes 00013fd6
+ 007aff34 bytes 00013fd6
~~~


<a id="compare-ba00c4c4760026f84a2c145230de9306"></a>

### [`007af524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af524.md) → [`007aff48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007aff48.md) FUN_007aff48

採用 · 移動量 `+0xa24` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`007af55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af524.md#insn-007af55c) · [`007af57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af524.md#insn-007af57c) · [`007af58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af524.md#insn-007af58c)
- 新版 [`007aff80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007aff48.md#insn-007aff80) · [`007affa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007aff48.md#insn-007affa0) · [`007affb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007aff48.md#insn-007affb0)

~~~diff
- 007af55c ["INT_ADD", "register:40f0:8", ["const:7af55c:8", "const:4:8"]]
- 007af55c ["CALL", null, ["callee:00c54d60:8"]]
+ 007aff80 ["INT_ADD", "register:40f0:8", ["const:7aff80:8", "const:4:8"]]
+ 007aff80 ["CALL", null, ["callee:00c54d60:8"]]
- 007af55c bytes 05921294
+ 007aff80 bytes 78931294
- 007af57c ["COPY", "register:0:8", ["register:4040:8"]]
- 007af57c ["INT_ADD", "register:40f0:8", ["const:7af57c:8", "const:4:8"]]
- 007af57c ["CALLIND", null, ["register:0:8"]]
+ 007affa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007affa0 ["INT_ADD", "register:40f0:8", ["const:7affa0:8", "const:4:8"]]
+ 007affa0 ["CALLIND", null, ["register:0:8"]]
- 007af57c bytes 00013fd6
+ 007affa0 bytes 00013fd6
- 007af58c ["INT_ADD", "register:40f0:8", ["const:7af58c:8", "const:4:8"]]
- 007af58c ["CALL", null, ["callee:00c54d90:8"]]
+ 007affb0 ["INT_ADD", "register:40f0:8", ["const:7affb0:8", "const:4:8"]]
+ 007affb0 ["CALL", null, ["callee:00c54d90:8"]]
- 007af58c bytes 05921294
+ 007affb0 bytes 78931294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

