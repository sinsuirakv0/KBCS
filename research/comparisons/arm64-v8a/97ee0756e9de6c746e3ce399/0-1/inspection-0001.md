# v15.7.2 → v15.7.3 · 要調査の変更候補 (1)

[一覧の目次](README.md)

<a id="compare-3ab4b9c513da7a988fcfcb0f41178d16"></a>

### [`00aa9ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9ee8.md) → [`00aa9fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md) FUN_00aa9fb0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009ce/009ce1d0.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045dd10.md)
- 新版 呼出元 1件 [`009ce1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009ce/009ce1d0.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045dd10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa9f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9ee8.md#insn-00aa9f14) · [`00aa9f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9ee8.md#insn-00aa9f30) · [`00aa9f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9ee8.md#insn-00aa9f64)
- 新版 [`00aa9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aa9fdc) · [`00aa9ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aa9ff8) · [`00aaa02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9fb0.md#insn-00aaa02c)

~~~diff
- 00aa9f14 ["INT_ADD", "register:40f0:8", ["const:aa9f14:8", "const:4:8"]]
- 00aa9f14 ["CALL", null, ["callee:0045dcb8:8"]]
+ 00aa9fdc ["INT_ADD", "register:40f0:8", ["const:aa9fdc:8", "const:4:8"]]
+ 00aa9fdc ["CALL", null, ["callee:0045dcb8:8"]]
- 00aa9f14 bytes 69cfe697
+ 00aa9fdc bytes 37cfe697
- 00aa9f30 ["INT_ADD", "register:40f0:8", ["const:aa9f30:8", "const:4:8"]]
- 00aa9f30 ["CALL", null, ["callee:0045dcb8:8"]]
+ 00aa9ff8 ["INT_ADD", "register:40f0:8", ["const:aa9ff8:8", "const:4:8"]]
+ 00aa9ff8 ["CALL", null, ["callee:0045dcb8:8"]]
- 00aa9f30 bytes 62cfe697
+ 00aa9ff8 bytes 30cfe697
- 00aa9f64 ["INT_ADD", "register:40f0:8", ["const:aa9f64:8", "const:4:8"]]
- 00aa9f64 ["CALL", null, ["callee:0045dd10:8"]]
+ 00aaa02c ["INT_ADD", "register:40f0:8", ["const:aaa02c:8", "const:4:8"]]
+ 00aaa02c ["CALL", null, ["callee:0045dd10:8"]]
- 00aa9f64 bytes 6bcfe697
+ 00aaa02c bytes 39cfe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe202f37fd9741bb6da5c9f9599e97c7"></a>

### [`00aaa0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa0c4.md) → [`00aaa18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md) FUN_00aaa18c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0071a134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071a/0071a134.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0071a134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a134.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa0c4.md#insn-00aaa100) · [`00aaa108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa0c4.md#insn-00aaa108) · [`00aaa110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa0c4.md#insn-00aaa110)
- 新版 [`00aaa1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1c8) · [`00aaa1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1d0) · [`00aaa1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md#insn-00aaa1d8)

~~~diff
- 00aaa100 ["INT_ADD", "register:40f0:8", ["const:aaa100:8", "const:4:8"]]
- 00aaa100 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa1c8 ["INT_ADD", "register:40f0:8", ["const:aaa1c8:8", "const:4:8"]]
+ 00aaa1c8 ["CALL", null, ["callee:007cf950:8"]]
- 00aaa100 bytes 1496f497
+ 00aaa1c8 bytes e295f497
- 00aaa108 ["INT_ADD", "register:40f0:8", ["const:aaa108:8", "const:4:8"]]
- 00aaa108 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa1d0 ["INT_ADD", "register:40f0:8", ["const:aaa1d0:8", "const:4:8"]]
+ 00aaa1d0 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa108 bytes 6696f497
+ 00aaa1d0 bytes 3496f497
- 00aaa110 ["INT_ADD", "register:40f0:8", ["const:aaa110:8", "const:4:8"]]
- 00aaa110 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa1d8 ["INT_ADD", "register:40f0:8", ["const:aaa1d8:8", "const:4:8"]]
+ 00aaa1d8 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa110 bytes f296f497
+ 00aaa1d8 bytes c096f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1ec3fb5094adb1dcee91e2b2ed5691"></a>

### [`00aaa5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md) → [`00aaa6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md) FUN_00aaa6bc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00aaa0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa0c4.md) [`00aaad94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md) [`00aac290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md)
- 新版 呼出元 3件 [`00aaa18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa18c.md) [`00aaae5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md#insn-00aaa624) · [`00aaa62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md#insn-00aaa62c) · [`00aaa634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md#insn-00aaa634)
- 新版 [`00aaa6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6ec) · [`00aaa6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6f4) · [`00aaa6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md#insn-00aaa6fc)

~~~diff
- 00aaa624 ["INT_ADD", "register:40f0:8", ["const:aaa624:8", "const:4:8"]]
- 00aaa624 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa6ec ["INT_ADD", "register:40f0:8", ["const:aaa6ec:8", "const:4:8"]]
+ 00aaa6ec ["CALL", null, ["callee:007cf950:8"]]
- 00aaa624 bytes cb94f497
+ 00aaa6ec bytes 9994f497
- 00aaa62c ["INT_ADD", "register:40f0:8", ["const:aaa62c:8", "const:4:8"]]
- 00aaa62c ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa6f4 ["INT_ADD", "register:40f0:8", ["const:aaa6f4:8", "const:4:8"]]
+ 00aaa6f4 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa62c bytes 1d95f497
+ 00aaa6f4 bytes eb94f497
- 00aaa634 ["INT_ADD", "register:40f0:8", ["const:aaa634:8", "const:4:8"]]
- 00aaa634 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa6fc ["INT_ADD", "register:40f0:8", ["const:aaa6fc:8", "const:4:8"]]
+ 00aaa6fc ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa634 bytes a995f497
+ 00aaa6fc bytes 7795f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de82e4a0d46e6d62972458a7ce21298"></a>

### [`00aaa830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa830.md) → [`00aaa8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md) FUN_00aaa8f8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00895118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00895/00895118.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) [`00a8df08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8df08.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0063c0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063c/0063c178.md) [`0063c21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063c/0063c21c.md)
- 新版 呼出元 3件 [`00895118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00895/00895118.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) [`00a8df08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8df08.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0063c0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c0d4.md) [`0063c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c178.md) [`0063c21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c21c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaa860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa830.md#insn-00aaa860) · [`00aaa868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa830.md#insn-00aaa868) · [`00aaa86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa830.md#insn-00aaa86c)
- 新版 [`00aaa928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa928) · [`00aaa930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa930) · [`00aaa934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa8f8.md#insn-00aaa934)

~~~diff
- 00aaa860 ["INT_ADD", "register:40f0:8", ["const:aaa860:8", "const:4:8"]]
- 00aaa860 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaa928 ["INT_ADD", "register:40f0:8", ["const:aaa928:8", "const:4:8"]]
+ 00aaa928 ["CALL", null, ["callee:007cf950:8"]]
- 00aaa860 bytes 3c94f497
+ 00aaa928 bytes 0a94f497
- 00aaa868 ["INT_ADD", "register:40f0:8", ["const:aaa868:8", "const:4:8"]]
- 00aaa868 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaa930 ["INT_ADD", "register:40f0:8", ["const:aaa930:8", "const:4:8"]]
+ 00aaa930 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaa868 bytes 8e94f497
+ 00aaa930 bytes 5c94f497
- 00aaa86c ["INT_ADD", "register:40f0:8", ["const:aaa86c:8", "const:4:8"]]
- 00aaa86c ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaa934 ["INT_ADD", "register:40f0:8", ["const:aaa934:8", "const:4:8"]]
+ 00aaa934 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaa86c bytes 1b95f497
+ 00aaa934 bytes e994f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313f85b946fe3d2eb97f84e3810be5ac"></a>

### [`00aaad50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad50.md) → [`00aaae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae18.md) FUN_00aaae18

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0059815c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md) [`00a72648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a72648.md) [`00a783c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a783c8.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) [`00a8052c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a80/00a8052c.md) · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 8件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) [`00a783c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a783c8.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) [`00a8052c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a80/00a8052c.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaad70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad50.md#insn-00aaad70)
- 新版 [`00aaae38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae18.md#insn-00aaae38)

~~~diff
- 00aaad70 ["INT_ADD", "register:40f0:8", ["const:aaad70:8", "const:4:8"]]
- 00aaad70 ["CALL", null, ["callee:00bdb5b0:8"]]
+ 00aaae38 ["INT_ADD", "register:40f0:8", ["const:aaae38:8", "const:4:8"]]
+ 00aaae38 ["CALL", null, ["callee:00bdb5b0:8"]]
- 00aaad70 bytes e4c10494
+ 00aaae38 bytes dec10494
~~~


<a id="compare-d48bc6efc042c3ee0fd168bc0dd52431"></a>

### [`00aaad94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md) → [`00aaae5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md) FUN_00aaae5c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`00a72648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a72648.md) · 呼出先 6件 [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00aaa5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md)
- 新版 呼出元 2件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) · 呼出先 6件 [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aaa6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaa6bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaadb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md#insn-00aaadb4) · [`00aaadbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md#insn-00aaadbc) · [`00aaadc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md#insn-00aaadc4)
- 新版 [`00aaae7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae7c) · [`00aaae84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae84) · [`00aaae8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaae5c.md#insn-00aaae8c)

~~~diff
- 00aaadb4 ["INT_ADD", "register:40f0:8", ["const:aaadb4:8", "const:4:8"]]
- 00aaadb4 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaae7c ["INT_ADD", "register:40f0:8", ["const:aaae7c:8", "const:4:8"]]
+ 00aaae7c ["CALL", null, ["callee:007cf950:8"]]
- 00aaadb4 bytes e792f497
+ 00aaae7c bytes b592f497
- 00aaadbc ["INT_ADD", "register:40f0:8", ["const:aaadbc:8", "const:4:8"]]
- 00aaadbc ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaae84 ["INT_ADD", "register:40f0:8", ["const:aaae84:8", "const:4:8"]]
+ 00aaae84 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaadbc bytes 3993f497
+ 00aaae84 bytes 0793f497
- 00aaadc4 ["INT_ADD", "register:40f0:8", ["const:aaadc4:8", "const:4:8"]]
- 00aaadc4 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaae8c ["INT_ADD", "register:40f0:8", ["const:aaae8c:8", "const:4:8"]]
+ 00aaae8c ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaadc4 bytes c593f497
+ 00aaae8c bytes 9393f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f71ef8828c78c35851f11bd38981c2e"></a>

### [`00aaaedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md) → [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) FUN_00aaafa4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md)
- 新版 呼出元 1件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaaf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md#insn-00aaaf24) · [`00aaaf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md#insn-00aaaf2c) · [`00aaaf34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md#insn-00aaaf34)
- 新版 [`00aaafec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaafec) · [`00aaaff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaaff4) · [`00aaaffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md#insn-00aaaffc)

~~~diff
- 00aaaf24 ["INT_ADD", "register:40f0:8", ["const:aaaf24:8", "const:4:8"]]
- 00aaaf24 ["CALL", null, ["callee:007cf950:8"]]
+ 00aaafec ["INT_ADD", "register:40f0:8", ["const:aaafec:8", "const:4:8"]]
+ 00aaafec ["CALL", null, ["callee:007cf950:8"]]
- 00aaaf24 bytes 8b92f497
+ 00aaafec bytes 5992f497
- 00aaaf2c ["INT_ADD", "register:40f0:8", ["const:aaaf2c:8", "const:4:8"]]
- 00aaaf2c ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aaaff4 ["INT_ADD", "register:40f0:8", ["const:aaaff4:8", "const:4:8"]]
+ 00aaaff4 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aaaf2c bytes dd92f497
+ 00aaaff4 bytes ab92f497
- 00aaaf34 ["INT_ADD", "register:40f0:8", ["const:aaaf34:8", "const:4:8"]]
- 00aaaf34 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aaaffc ["INT_ADD", "register:40f0:8", ["const:aaaffc:8", "const:4:8"]]
+ 00aaaffc ["CALL", null, ["callee:007cfcd8:8"]]
- 00aaaf34 bytes 6993f497
+ 00aaaffc bytes 3793f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11997a3059eed89ee45a0f5cf803e28"></a>

### [`00aab3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md) → [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) FUN_00aab488

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007acf88.md) [`00a72648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a72/00a72648.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 8件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007acf88.md) [`00a72648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a72/00a72648.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aab3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md#insn-00aab3f8) · [`00aab400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md#insn-00aab400) · [`00aab408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md#insn-00aab408)
- 新版 [`00aab4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4c0) · [`00aab4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4c8) · [`00aab4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md#insn-00aab4d0)

~~~diff
- 00aab3f8 ["INT_ADD", "register:40f0:8", ["const:aab3f8:8", "const:4:8"]]
- 00aab3f8 ["CALL", null, ["callee:007cf950:8"]]
+ 00aab4c0 ["INT_ADD", "register:40f0:8", ["const:aab4c0:8", "const:4:8"]]
+ 00aab4c0 ["CALL", null, ["callee:007cf950:8"]]
- 00aab3f8 bytes 5691f497
+ 00aab4c0 bytes 2491f497
- 00aab400 ["INT_ADD", "register:40f0:8", ["const:aab400:8", "const:4:8"]]
- 00aab400 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aab4c8 ["INT_ADD", "register:40f0:8", ["const:aab4c8:8", "const:4:8"]]
+ 00aab4c8 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aab400 bytes a891f497
+ 00aab4c8 bytes 7691f497
- 00aab408 ["INT_ADD", "register:40f0:8", ["const:aab408:8", "const:4:8"]]
- 00aab408 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aab4d0 ["INT_ADD", "register:40f0:8", ["const:aab4d0:8", "const:4:8"]]
+ 00aab4d0 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aab408 bytes 3492f497
+ 00aab4d0 bytes 0292f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4eb32877d975b181074fda48eb6c3e2"></a>

### [`00aab518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab518.md) → [`00aab5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md) FUN_00aab5e0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00aab67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md) [`00aabd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aab554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab518.md#insn-00aab554) · [`00aab55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab518.md#insn-00aab55c) · [`00aab564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab518.md#insn-00aab564)
- 新版 [`00aab61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab61c) · [`00aab624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab624) · [`00aab62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab5e0.md#insn-00aab62c)

~~~diff
- 00aab554 ["INT_ADD", "register:40f0:8", ["const:aab554:8", "const:4:8"]]
- 00aab554 ["CALL", null, ["callee:007cf950:8"]]
+ 00aab61c ["INT_ADD", "register:40f0:8", ["const:aab61c:8", "const:4:8"]]
+ 00aab61c ["CALL", null, ["callee:007cf950:8"]]
- 00aab554 bytes ff90f497
+ 00aab61c bytes cd90f497
- 00aab55c ["INT_ADD", "register:40f0:8", ["const:aab55c:8", "const:4:8"]]
- 00aab55c ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aab624 ["INT_ADD", "register:40f0:8", ["const:aab624:8", "const:4:8"]]
+ 00aab624 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aab55c bytes 5191f497
+ 00aab624 bytes 1f91f497
- 00aab564 ["INT_ADD", "register:40f0:8", ["const:aab564:8", "const:4:8"]]
- 00aab564 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aab62c ["INT_ADD", "register:40f0:8", ["const:aab62c:8", "const:4:8"]]
+ 00aab62c ["CALL", null, ["callee:007cfcd8:8"]]
- 00aab564 bytes dd91f497
+ 00aab62c bytes ab91f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbafb2b3b5b959bc93bcee1ccf8c02d6"></a>

### [`00aac290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md) → [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) FUN_00aac358

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00aad110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad110.md) [`00aad22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad22c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cfcd8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aac2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md#insn-00aac2d0) · [`00aac2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md#insn-00aac2d8) · [`00aac2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md#insn-00aac2e0)
- 新版 [`00aac398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac398) · [`00aac3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac3a0) · [`00aac3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md#insn-00aac3a8)

~~~diff
- 00aac2d0 ["INT_ADD", "register:40f0:8", ["const:aac2d0:8", "const:4:8"]]
- 00aac2d0 ["CALL", null, ["callee:007cf950:8"]]
+ 00aac398 ["INT_ADD", "register:40f0:8", ["const:aac398:8", "const:4:8"]]
+ 00aac398 ["CALL", null, ["callee:007cf950:8"]]
- 00aac2d0 bytes a08df497
+ 00aac398 bytes 6e8df497
- 00aac2d8 ["INT_ADD", "register:40f0:8", ["const:aac2d8:8", "const:4:8"]]
- 00aac2d8 ["CALL", null, ["callee:007cfaa0:8"]]
+ 00aac3a0 ["INT_ADD", "register:40f0:8", ["const:aac3a0:8", "const:4:8"]]
+ 00aac3a0 ["CALL", null, ["callee:007cfaa0:8"]]
- 00aac2d8 bytes f28df497
+ 00aac3a0 bytes c08df497
- 00aac2e0 ["INT_ADD", "register:40f0:8", ["const:aac2e0:8", "const:4:8"]]
- 00aac2e0 ["CALL", null, ["callee:007cfcd8:8"]]
+ 00aac3a8 ["INT_ADD", "register:40f0:8", ["const:aac3a8:8", "const:4:8"]]
+ 00aac3a8 ["CALL", null, ["callee:007cfcd8:8"]]
- 00aac2e0 bytes 7e8ef497
+ 00aac3a8 bytes 4c8ef497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09abda40e0d536ff2f4304926aa6118"></a>

### [`00aac858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac858.md) → [`00aac920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md) FUN_00aac920

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aa980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa980c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aaca64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca64.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aac904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac858.md#insn-00aac904) · [`00aac948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac858.md#insn-00aac948) · [`00aac98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac858.md#insn-00aac98c)
- 新版 [`00aac9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aac9cc) · [`00aaca10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aaca10) · [`00aaca54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md#insn-00aaca54)

~~~diff
- 00aac904 ["INT_ADD", "register:40f0:8", ["const:aac904:8", "const:4:8"]]
- 00aac904 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aac9cc ["INT_ADD", "register:40f0:8", ["const:aac9cc:8", "const:4:8"]]
+ 00aac9cc ["CALL", null, ["callee:00bdaff0:8"]]
- 00aac904 bytes 8fb90494
+ 00aac9cc bytes 89b90494
- 00aac948 ["INT_ADD", "register:40f0:8", ["const:aac948:8", "const:4:8"]]
- 00aac948 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aaca10 ["INT_ADD", "register:40f0:8", ["const:aaca10:8", "const:4:8"]]
+ 00aaca10 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aac948 bytes feb90494
+ 00aaca10 bytes f8b90494
- 00aac98c ["INT_ADD", "register:40f0:8", ["const:aac98c:8", "const:4:8"]]
- 00aac98c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aaca54 ["INT_ADD", "register:40f0:8", ["const:aaca54:8", "const:4:8"]]
+ 00aaca54 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aac98c bytes edb90494
+ 00aaca54 bytes e7b90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89d4f659d5d43ef25b4c6eed9e329ea0"></a>

### [`00aaca8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca8c.md) → [`00aacb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md) FUN_00aacb54

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aaaedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aaca64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca64.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aacb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca8c.md#insn-00aacb18) · [`00aacbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca8c.md#insn-00aacbd0) · [`00aacbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca8c.md#insn-00aacbec)
- 新版 [`00aacbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aacbe0) · [`00aacc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aacc98) · [`00aaccb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md#insn-00aaccb4)

~~~diff
- 00aacb18 ["INT_ADD", "register:40f0:8", ["const:aacb18:8", "const:4:8"]]
- 00aacb18 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aacbe0 ["INT_ADD", "register:40f0:8", ["const:aacbe0:8", "const:4:8"]]
+ 00aacbe0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aacb18 bytes 0ab90494
+ 00aacbe0 bytes 04b90494
- 00aacbd0 ["INT_ADD", "register:40f0:8", ["const:aacbd0:8", "const:4:8"]]
- 00aacbd0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00aacc98 ["INT_ADD", "register:40f0:8", ["const:aacc98:8", "const:4:8"]]
+ 00aacc98 ["CALL", null, ["callee:00bdb010:8"]]
- 00aacbd0 bytes e4b80494
+ 00aacc98 bytes deb80494
- 00aacbec ["INT_ADD", "register:40f0:8", ["const:aacbec:8", "const:4:8"]]
- 00aacbec ["CALL", null, ["callee:00bdb010:8"]]
+ 00aaccb4 ["INT_ADD", "register:40f0:8", ["const:aaccb4:8", "const:4:8"]]
+ 00aaccb4 ["CALL", null, ["callee:00bdb010:8"]]
- 00aacbec bytes ddb80494
+ 00aaccb4 bytes d7b80494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d96e9f0700bcf1b16f371e5b01ff8e9"></a>

### [`00aad110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad110.md) → [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) FUN_00aad1d8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00885/00885f80.md) [`00aab67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md) [`00aac290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad110.md#insn-00aad140) · [`00aad14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad110.md#insn-00aad14c)
- 新版 [`00aad208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md#insn-00aad208) · [`00aad214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md#insn-00aad214)

~~~diff
- 00aad140 ["INT_ADD", "register:40f0:8", ["const:aad140:8", "const:4:8"]]
- 00aad140 ["CALL", null, ["ram:457e1c:8"]]
+ 00aad208 ["INT_ADD", "register:40f0:8", ["const:aad208:8", "const:4:8"]]
+ 00aad208 ["CALL", null, ["ram:457e1c:8"]]
- 00aad140 bytes 37abe697
+ 00aad208 bytes 05abe697
- 00aad14c ["INT_ADD", "register:40f0:8", ["const:aad14c:8", "const:4:8"]]
- 00aad14c ["CALL", null, ["callee:00459efc:8"]]
+ 00aad214 ["INT_ADD", "register:40f0:8", ["const:aad214:8", "const:4:8"]]
+ 00aad214 ["CALL", null, ["callee:00459efc:8"]]
- 00aad14c bytes 6cb3e697
+ 00aad214 bytes 3ab3e697
~~~


<a id="compare-7c4e3931c8291f147de3b3549bca6d3f"></a>

### [`00aad22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad22c.md) → [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) FUN_00aad2f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00885/00885f80.md) [`00aab67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md) [`00aac290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad25c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad22c.md#insn-00aad25c) · [`00aad268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad22c.md#insn-00aad268)
- 新版 [`00aad324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md#insn-00aad324) · [`00aad330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md#insn-00aad330)

~~~diff
- 00aad25c ["INT_ADD", "register:40f0:8", ["const:aad25c:8", "const:4:8"]]
- 00aad25c ["CALL", null, ["ram:457e1c:8"]]
+ 00aad324 ["INT_ADD", "register:40f0:8", ["const:aad324:8", "const:4:8"]]
+ 00aad324 ["CALL", null, ["ram:457e1c:8"]]
- 00aad25c bytes f0aae697
+ 00aad324 bytes beaae697
- 00aad268 ["INT_ADD", "register:40f0:8", ["const:aad268:8", "const:4:8"]]
- 00aad268 ["CALL", null, ["callee:00459efc:8"]]
+ 00aad330 ["INT_ADD", "register:40f0:8", ["const:aad330:8", "const:4:8"]]
+ 00aad330 ["CALL", null, ["callee:00459efc:8"]]
- 00aad268 bytes 25b3e697
+ 00aad330 bytes f3b2e697
~~~


<a id="compare-c5d2a6d2d6d58aeba48881d9b8e93429"></a>

### [`00aad330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad330.md) → [`00aad3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md) FUN_00aad3f8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883878.md) [`008847e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/008847e4.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883878.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad330.md#insn-00aad33c) · [`00aad34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad330.md#insn-00aad34c) · [`00aad354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad330.md#insn-00aad354)
- 新版 [`00aad404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad404) · [`00aad414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad414) · [`00aad41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad3f8.md#insn-00aad41c)

~~~diff
- 00aad33c ["INT_ADD", "register:40f0:8", ["const:aad33c:8", "const:4:8"]]
- 00aad33c ["CALL", null, ["callee:0081f580:8"]]
+ 00aad404 ["INT_ADD", "register:40f0:8", ["const:aad404:8", "const:4:8"]]
+ 00aad404 ["CALL", null, ["callee:0081f580:8"]]
- 00aad33c bytes 91c8f597
+ 00aad404 bytes 5fc8f597
- 00aad34c ["INT_ADD", "register:40f0:8", ["const:aad34c:8", "const:4:8"]]
- 00aad34c ["CALL", null, ["callee:008847e4:8"]]
+ 00aad414 ["INT_ADD", "register:40f0:8", ["const:aad414:8", "const:4:8"]]
+ 00aad414 ["CALL", null, ["callee:008847e4:8"]]
- 00aad34c bytes 265df797
+ 00aad414 bytes f45cf797
- 00aad354 ["INT_ADD", "register:40f0:8", ["const:aad354:8", "const:4:8"]]
- 00aad354 ["CALL", null, ["callee:00883878:8"]]
+ 00aad41c ["INT_ADD", "register:40f0:8", ["const:aad41c:8", "const:4:8"]]
+ 00aad41c ["CALL", null, ["callee:00883878:8"]]
- 00aad354 bytes 4959f797
+ 00aad41c bytes 1759f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed72049bc2bda591424c7e1710732cd"></a>

### [`00aad40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad40c.md) → [`00aad4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md) FUN_00aad4d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 13件 [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad40c.md#insn-00aad438) · [`00aad458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad40c.md#insn-00aad458) · [`00aad464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad40c.md#insn-00aad464)
- 新版 [`00aad500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad500) · [`00aad520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad520) · [`00aad52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad4d4.md#insn-00aad52c)

~~~diff
- 00aad438 ["INT_ADD", "register:40f0:8", ["const:aad438:8", "const:4:8"]]
- 00aad438 ["CALL", null, ["callee:0088600c:8"]]
+ 00aad500 ["INT_ADD", "register:40f0:8", ["const:aad500:8", "const:4:8"]]
+ 00aad500 ["CALL", null, ["callee:0088600c:8"]]
- 00aad438 bytes f562f797
+ 00aad500 bytes c362f797
- 00aad458 ["INT_ADD", "register:40f0:8", ["const:aad458:8", "const:4:8"]]
- 00aad458 ["CALL", null, ["callee:00886014:8"]]
+ 00aad520 ["INT_ADD", "register:40f0:8", ["const:aad520:8", "const:4:8"]]
+ 00aad520 ["CALL", null, ["callee:00886014:8"]]
- 00aad458 bytes ef62f797
+ 00aad520 bytes bd62f797
- 00aad464 ["INT_ADD", "register:40f0:8", ["const:aad464:8", "const:4:8"]]
- 00aad464 ["CALL", null, ["callee:00886014:8"]]
+ 00aad52c ["INT_ADD", "register:40f0:8", ["const:aad52c:8", "const:4:8"]]
+ 00aad52c ["CALL", null, ["callee:00886014:8"]]
- 00aad464 bytes ec62f797
+ 00aad52c bytes ba62f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5f57f557c4af238598e34193f3c33b"></a>

### [`00aad8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad8d8.md) → [`00aad9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md) FUN_00aad9a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00aab3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md) [`00aabd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aad900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad8d8.md#insn-00aad900) · [`00aad90c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad8d8.md#insn-00aad90c) · [`00aad940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad8d8.md#insn-00aad940)
- 新版 [`00aad9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aad9c8) · [`00aad9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aad9d4) · [`00aada08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md#insn-00aada08)

~~~diff
- 00aad900 ["INT_ADD", "register:40f0:8", ["const:aad900:8", "const:4:8"]]
- 00aad900 ["CALL", null, ["ram:457e1c:8"]]
+ 00aad9c8 ["INT_ADD", "register:40f0:8", ["const:aad9c8:8", "const:4:8"]]
+ 00aad9c8 ["CALL", null, ["ram:457e1c:8"]]
- 00aad900 bytes 47a9e697
+ 00aad9c8 bytes 15a9e697
- 00aad90c ["INT_ADD", "register:40f0:8", ["const:aad90c:8", "const:4:8"]]
- 00aad90c ["CALL", null, ["ram:457e1c:8"]]
+ 00aad9d4 ["INT_ADD", "register:40f0:8", ["const:aad9d4:8", "const:4:8"]]
+ 00aad9d4 ["CALL", null, ["ram:457e1c:8"]]
- 00aad90c bytes 44a9e697
+ 00aad9d4 bytes 12a9e697
- 00aad940 ["INT_ADD", "register:40f0:8", ["const:aad940:8", "const:4:8"]]
- 00aad940 ["CALL", null, ["callee:00aab488:8"]]
+ 00aada08 ["INT_ADD", "register:40f0:8", ["const:aada08:8", "const:4:8"]]
+ 00aada08 ["CALL", null, ["callee:00aab488:8"]]
- 00aad940 bytes a0f6ff97
+ 00aada08 bytes a0f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c0f3b3445aec4986efc55c0c2daeffc"></a>

### [`00aada14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md) → [`00aadadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md) FUN_00aadadc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00aab3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab3c0.md) [`00aabd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00aab488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab488.md) [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aada3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md#insn-00aada3c) · [`00aada48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md#insn-00aada48) · [`00aada80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md#insn-00aada80)
- 新版 [`00aadb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb04) · [`00aadb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb10) · [`00aadb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md#insn-00aadb48)

~~~diff
- 00aada3c ["INT_ADD", "register:40f0:8", ["const:aada3c:8", "const:4:8"]]
- 00aada3c ["CALL", null, ["ram:457e1c:8"]]
+ 00aadb04 ["INT_ADD", "register:40f0:8", ["const:aadb04:8", "const:4:8"]]
+ 00aadb04 ["CALL", null, ["ram:457e1c:8"]]
- 00aada3c bytes f8a8e697
+ 00aadb04 bytes c6a8e697
- 00aada48 ["INT_ADD", "register:40f0:8", ["const:aada48:8", "const:4:8"]]
- 00aada48 ["CALL", null, ["ram:457e1c:8"]]
+ 00aadb10 ["INT_ADD", "register:40f0:8", ["const:aadb10:8", "const:4:8"]]
+ 00aadb10 ["CALL", null, ["ram:457e1c:8"]]
- 00aada48 bytes f5a8e697
+ 00aadb10 bytes c3a8e697
- 00aada80 ["INT_ADD", "register:40f0:8", ["const:aada80:8", "const:4:8"]]
- 00aada80 ["CALL", null, ["callee:00aab488:8"]]
+ 00aadb48 ["INT_ADD", "register:40f0:8", ["const:aadb48:8", "const:4:8"]]
+ 00aadb48 ["CALL", null, ["callee:00aab488:8"]]
- 00aada80 bytes 50f6ff97
+ 00aadb48 bytes 50f6ff97
~~~


<a id="compare-887fcd8fc55585724330c43ed19c6195"></a>

### [`00aadadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md) → [`00aadba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md) FUN_00aadba4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aac290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac290.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471738.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00aac358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac358.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aadb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md#insn-00aadb44) · [`00aadb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md#insn-00aadb80) · [`00aadb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aadadc.md#insn-00aadb90)
- 新版 [`00aadc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc0c) · [`00aadc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc48) · [`00aadc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadba4.md#insn-00aadc58)

~~~diff
- 00aadb44 ["INT_ADD", "register:40f0:8", ["const:aadb44:8", "const:4:8"]]
- 00aadb44 ["CALL", null, ["callee:00471738:8"]]
+ 00aadc0c ["INT_ADD", "register:40f0:8", ["const:aadc0c:8", "const:4:8"]]
+ 00aadc0c ["CALL", null, ["callee:00471738:8"]]
- 00aadb44 bytes fd0ee797
+ 00aadc0c bytes cb0ee797
- 00aadb80 ["INT_ADD", "register:40f0:8", ["const:aadb80:8", "const:4:8"]]
- 00aadb80 ["CALL", null, ["callee:00bdb010:8"]]
+ 00aadc48 ["INT_ADD", "register:40f0:8", ["const:aadc48:8", "const:4:8"]]
+ 00aadc48 ["CALL", null, ["callee:00bdb010:8"]]
- 00aadb80 bytes f8b40494
+ 00aadc48 bytes f2b40494
- 00aadb90 ["INT_ADD", "register:40f0:8", ["const:aadb90:8", "const:4:8"]]
- 00aadb90 ["CALL", null, ["callee:00bdb010:8"]]
+ 00aadc58 ["INT_ADD", "register:40f0:8", ["const:aadc58:8", "const:4:8"]]
+ 00aadc58 ["CALL", null, ["callee:00bdb010:8"]]
- 00aadb90 bytes f4b40494
+ 00aadc58 bytes eeb40494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78dc7aba048dd086a81a7cabb1bf89c9"></a>

### [`00aaedf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaedf8.md) → [`00aaeec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md) FUN_00aaeec0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009bd/009bd6b8.md) · 呼出先 2件 [`0045d420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d420.md) [`0045d518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd6b8.md) · 呼出先 2件 [`0045d420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d420.md) [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaee18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaedf8.md#insn-00aaee18) · [`00aaee24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaedf8.md#insn-00aaee24) · [`00aaee30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaedf8.md#insn-00aaee30)
- 新版 [`00aaeee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeee0) · [`00aaeeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeeec) · [`00aaeef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md#insn-00aaeef8)

~~~diff
- 00aaee18 ["INT_ADD", "register:40f0:8", ["const:aaee18:8", "const:4:8"]]
- 00aaee18 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaeee0 ["INT_ADD", "register:40f0:8", ["const:aaeee0:8", "const:4:8"]]
+ 00aaeee0 ["CALL", null, ["callee:0045d518:8"]]
- 00aaee18 bytes c0b9e697
+ 00aaeee0 bytes 8eb9e697
- 00aaee24 ["INT_ADD", "register:40f0:8", ["const:aaee24:8", "const:4:8"]]
- 00aaee24 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaeeec ["INT_ADD", "register:40f0:8", ["const:aaeeec:8", "const:4:8"]]
+ 00aaeeec ["CALL", null, ["callee:0045d518:8"]]
- 00aaee24 bytes bdb9e697
+ 00aaeeec bytes 8bb9e697
- 00aaee30 ["INT_ADD", "register:40f0:8", ["const:aaee30:8", "const:4:8"]]
- 00aaee30 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaeef8 ["INT_ADD", "register:40f0:8", ["const:aaeef8:8", "const:4:8"]]
+ 00aaeef8 ["CALL", null, ["callee:0045d518:8"]]
- 00aaee30 bytes bab9e697
+ 00aaeef8 bytes 88b9e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b45b7e6f1d5c5875fe02a7a3a3d2142c"></a>

### [`00aaef18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaef18.md) → [`00aaefe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md) FUN_00aaefe0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009c5/009c5338.md) · 呼出先 2件 [`0045de70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`009c5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c5/009c5338.md) · 呼出先 2件 [`0045de70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaef38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaef18.md#insn-00aaef38) · [`00aaef44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaef18.md#insn-00aaef44) · [`00aaef50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaef18.md#insn-00aaef50)
- 新版 [`00aaf000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf000) · [`00aaf00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf00c) · [`00aaf018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaefe0.md#insn-00aaf018)

~~~diff
- 00aaef38 ["INT_ADD", "register:40f0:8", ["const:aaef38:8", "const:4:8"]]
- 00aaef38 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf000 ["INT_ADD", "register:40f0:8", ["const:aaf000:8", "const:4:8"]]
+ 00aaf000 ["CALL", null, ["callee:0045df50:8"]]
- 00aaef38 bytes 06bce697
+ 00aaf000 bytes d4bbe697
- 00aaef44 ["INT_ADD", "register:40f0:8", ["const:aaef44:8", "const:4:8"]]
- 00aaef44 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf00c ["INT_ADD", "register:40f0:8", ["const:aaf00c:8", "const:4:8"]]
+ 00aaf00c ["CALL", null, ["callee:0045df50:8"]]
- 00aaef44 bytes 03bce697
+ 00aaf00c bytes d1bbe697
- 00aaef50 ["INT_ADD", "register:40f0:8", ["const:aaef50:8", "const:4:8"]]
- 00aaef50 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf018 ["INT_ADD", "register:40f0:8", ["const:aaf018:8", "const:4:8"]]
+ 00aaf018 ["CALL", null, ["callee:0045df50:8"]]
- 00aaef50 bytes 00bce697
+ 00aaf018 bytes cebbe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d229f861e853d5a6375f36bc54b019e"></a>

### [`00aaefdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaefdc.md) → [`00aaf0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md) FUN_00aaf0a4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009bd/009bd6b8.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`009bd6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd6b8.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaeff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaefdc.md#insn-00aaeff4) · [`00aaf000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaefdc.md#insn-00aaf000)
- 新版 [`00aaf0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md#insn-00aaf0bc) · [`00aaf0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md#insn-00aaf0c8)

~~~diff
- 00aaeff4 ["INT_ADD", "register:40f0:8", ["const:aaeff4:8", "const:4:8"]]
- 00aaeff4 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaf0bc ["INT_ADD", "register:40f0:8", ["const:aaf0bc:8", "const:4:8"]]
+ 00aaf0bc ["CALL", null, ["callee:0045d518:8"]]
- 00aaeff4 bytes 49b9e697
+ 00aaf0bc bytes 17b9e697
- 00aaf000 ["INT_ADD", "register:40f0:8", ["const:aaf000:8", "const:4:8"]]
- 00aaf000 ["CALL", null, ["callee:0045d518:8"]]
+ 00aaf0c8 ["INT_ADD", "register:40f0:8", ["const:aaf0c8:8", "const:4:8"]]
+ 00aaf0c8 ["CALL", null, ["callee:0045d518:8"]]
- 00aaf000 bytes 46b9e697
+ 00aaf0c8 bytes 14b9e697
~~~


<a id="compare-65aa5bd29ec9314c8ab69086e5b86ea6"></a>

### [`00aaf014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf014.md) → [`00aaf0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0dc.md) FUN_00aaf0dc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009c5338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009c5/009c5338.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`009c5338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009c5/009c5338.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045df50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf014.md#insn-00aaf034)
- 新版 [`00aaf0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0dc.md#insn-00aaf0fc)

~~~diff
- 00aaf034 ["INT_ADD", "register:40f0:8", ["const:aaf034:8", "const:4:8"]]
- 00aaf034 ["CALL", null, ["callee:0045df50:8"]]
+ 00aaf0fc ["INT_ADD", "register:40f0:8", ["const:aaf0fc:8", "const:4:8"]]
+ 00aaf0fc ["CALL", null, ["callee:0045df50:8"]]
- 00aaf034 bytes c7bbe697
+ 00aaf0fc bytes 95bbe697
~~~


<a id="compare-ceea01244cca410d93d4d543899c74e2"></a>

### [`00aaf04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf04c.md) → [`00aaf114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md) FUN_00aaf114

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d2/005d2c18.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005d2c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d2/005d2c18.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf04c.md#insn-00aaf05c) · [`00aaf088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf04c.md#insn-00aaf088)
- 新版 [`00aaf124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md#insn-00aaf124) · [`00aaf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf114.md#insn-00aaf150)

~~~diff
- 00aaf05c ["INT_ADD", "register:40f0:8", ["const:aaf05c:8", "const:4:8"]]
- 00aaf05c ["CALL", null, ["callee:0081f580:8"]]
+ 00aaf124 ["INT_ADD", "register:40f0:8", ["const:aaf124:8", "const:4:8"]]
+ 00aaf124 ["CALL", null, ["callee:0081f580:8"]]
- 00aaf05c bytes 49c1f597
+ 00aaf124 bytes 17c1f597
- 00aaf088 ["INT_ADD", "register:40f0:8", ["const:aaf088:8", "const:4:8"]]
- 00aaf088 ["CALL", null, ["callee:0081f580:8"]]
+ 00aaf150 ["INT_ADD", "register:40f0:8", ["const:aaf150:8", "const:4:8"]]
+ 00aaf150 ["CALL", null, ["callee:0081f580:8"]]
- 00aaf088 bytes 3ec1f597
+ 00aaf150 bytes 0cc1f597
~~~


<a id="compare-6b96bbadb0b253859ed358f30964c52b"></a>

### [`00aaf448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf448.md) → [`00aaf510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md) FUN_00aaf510

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aaf630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf630.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00ab0d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab0/00ab0d70.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00aaf6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf6f8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00ab0e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf448.md#insn-00aaf488) · [`00aaf498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf448.md#insn-00aaf498) · [`00aaf4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf448.md#insn-00aaf4c0)
- 新版 [`00aaf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf550) · [`00aaf560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf560) · [`00aaf588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf510.md#insn-00aaf588)

~~~diff
- 00aaf488 ["INT_ADD", "register:40f0:8", ["const:aaf488:8", "const:4:8"]]
- 00aaf488 ["CALL", null, ["callee:00464a64:8"]]
+ 00aaf550 ["INT_ADD", "register:40f0:8", ["const:aaf550:8", "const:4:8"]]
+ 00aaf550 ["CALL", null, ["callee:00464a64:8"]]
- 00aaf488 bytes 77d5e697
+ 00aaf550 bytes 45d5e697
- 00aaf498 ["INT_ADD", "register:40f0:8", ["const:aaf498:8", "const:4:8"]]
- 00aaf498 ["CALL", null, ["callee:00464a64:8"]]
+ 00aaf560 ["INT_ADD", "register:40f0:8", ["const:aaf560:8", "const:4:8"]]
+ 00aaf560 ["CALL", null, ["callee:00464a64:8"]]
- 00aaf498 bytes 73d5e697
+ 00aaf560 bytes 41d5e697
- 00aaf4c0 ["INT_ADD", "register:40f0:8", ["const:aaf4c0:8", "const:4:8"]]
- 00aaf4c0 ["CALL", null, ["callee:00464a44:8"]]
+ 00aaf588 ["INT_ADD", "register:40f0:8", ["const:aaf588:8", "const:4:8"]]
+ 00aaf588 ["CALL", null, ["callee:00464a44:8"]]
- 00aaf4c0 bytes 61d5e697
+ 00aaf588 bytes 2fd5e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4016ac7fc5eb05dd6ea326a227b20217"></a>

### [`00aaf8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf8f0.md) → [`00aaf9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md) FUN_00aaf9b8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00a271c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a27/00a271c8.md) [`00aafa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00ab0d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab0/00ab0d70.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`00a271c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a27/00a271c8.md) [`00aafb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md) · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00ab0e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab0/00ab0e38.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aaf994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf8f0.md#insn-00aaf994) · [`00aaf9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf8f0.md#insn-00aaf9c0) · [`00aaf9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf8f0.md#insn-00aaf9f0)
- 新版 [`00aafa5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafa5c) · [`00aafa88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafa88) · [`00aafab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md#insn-00aafab8)

~~~diff
- 00aaf994 ["INT_ADD", "register:40f0:8", ["const:aaf994:8", "const:4:8"]]
- 00aaf994 ["CALL", null, ["callee:0041fdf0:8"]]
+ 00aafa5c ["INT_ADD", "register:40f0:8", ["const:aafa5c:8", "const:4:8"]]
+ 00aafa5c ["CALL", null, ["callee:0041fdf0:8"]]
- 00aaf994 bytes 17c1e597
+ 00aafa5c bytes e5c0e597
- 00aaf9c0 ["INT_ADD", "register:40f0:8", ["const:aaf9c0:8", "const:4:8"]]
- 00aaf9c0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aafa88 ["INT_ADD", "register:40f0:8", ["const:aafa88:8", "const:4:8"]]
+ 00aafa88 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aaf9c0 bytes 60ad0494
+ 00aafa88 bytes 5aad0494
- 00aaf9f0 ["INT_ADD", "register:40f0:8", ["const:aaf9f0:8", "const:4:8"]]
- 00aaf9f0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aafab8 ["INT_ADD", "register:40f0:8", ["const:aafab8:8", "const:4:8"]]
+ 00aafab8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aaf9f0 bytes 54ad0494
+ 00aafab8 bytes 4ead0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7a301aeb9c2d666e214dcc2ec6429e"></a>

### [`00aafa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md) → [`00aafb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md) FUN_00aafb1c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0082ea34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0082e/0082ea34.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`007ac4fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ac/007ac4fc.md)
- 新版 呼出元 1件 [`0082ea34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082e/0082ea34.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`007ac4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac4fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aafa88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md#insn-00aafa88) · [`00aafaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md#insn-00aafaac) · [`00aafb08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md#insn-00aafb08)
- 新版 [`00aafb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafb50) · [`00aafb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafb74) · [`00aafbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aafb1c.md#insn-00aafbd0)

~~~diff
- 00aafa88 ["INT_ADD", "register:40f0:8", ["const:aafa88:8", "const:4:8"]]
- 00aafa88 ["CALL", null, ["callee:00aaf9b8:8"]]
+ 00aafb50 ["INT_ADD", "register:40f0:8", ["const:aafb50:8", "const:4:8"]]
+ 00aafb50 ["CALL", null, ["callee:00aaf9b8:8"]]
- 00aafa88 bytes 9affff97
+ 00aafb50 bytes 9affff97
- 00aafaac ["INT_ADD", "register:40f0:8", ["const:aafaac:8", "const:4:8"]]
- 00aafaac ["CALL", null, ["callee:0081f580:8"]]
+ 00aafb74 ["INT_ADD", "register:40f0:8", ["const:aafb74:8", "const:4:8"]]
+ 00aafb74 ["CALL", null, ["callee:0081f580:8"]]
- 00aafaac bytes b5bef597
+ 00aafb74 bytes 83bef597
- 00aafb08 ["INT_ADD", "register:40f0:8", ["const:aafb08:8", "const:4:8"]]
- 00aafb08 ["CALL", null, ["callee:0081f580:8"]]
+ 00aafbd0 ["INT_ADD", "register:40f0:8", ["const:aafbd0:8", "const:4:8"]]
+ 00aafbd0 ["CALL", null, ["callee:0081f580:8"]]
- 00aafb08 bytes 9ebef597
+ 00aafbd0 bytes 6cbef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c70b6e8cdda554cf6ca18fb0037f2ae"></a>

### [`00ab1c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1c58.md) → [`00ab1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d20.md) FUN_00ab1d20

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00596128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596128.md) · 呼出先 2件 [`00449ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449ae0.md) [`00449bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bdc.md)
- 新版 呼出元 1件 [`00596128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596128.md) · 呼出先 2件 [`00449ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449ae0.md) [`00449bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bdc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ab1c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1c58.md#insn-00ab1c8c)
- 新版 [`00ab1d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d20.md#insn-00ab1d54)

~~~diff
- 00ab1c8c ["INT_ADD", "register:40f0:8", ["const:ab1c8c:8", "const:4:8"]]
- 00ab1c8c ["CALL", null, ["callee:00449bdc:8"]]
+ 00ab1d54 ["INT_ADD", "register:40f0:8", ["const:ab1d54:8", "const:4:8"]]
+ 00ab1d54 ["CALL", null, ["callee:00449bdc:8"]]
- 00ab1c8c bytes d45fe697
+ 00ab1d54 bytes a25fe697
~~~


<a id="compare-07011a3c84229ed5c16bfdd0e52110b4"></a>

### [`00ac8e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8e44.md) → [`00ac8f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8f0c.md) FUN_00ac8f0c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac8ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8e44.md#insn-00ac8ea0) · [`00ac8ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8e44.md#insn-00ac8ec8)
- 新版 [`00ac8f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8f0c.md#insn-00ac8f68) · [`00ac8f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac8/00ac8f0c.md#insn-00ac8f90)

~~~diff
- 00ac8ea0 ["INT_ADD", "register:40f0:8", ["const:ac8ea0:8", "const:4:8"]]
- 00ac8ea0 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ac8f68 ["INT_ADD", "register:40f0:8", ["const:ac8f68:8", "const:4:8"]]
+ 00ac8f68 ["CALL", null, ["callee:00418fe0:8"]]
- 00ac8ea0 bytes 5040e597
+ 00ac8f68 bytes 1e40e597
- 00ac8ec8 ["INT_ADD", "register:40f0:8", ["const:ac8ec8:8", "const:4:8"]]
- 00ac8ec8 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ac8f90 ["INT_ADD", "register:40f0:8", ["const:ac8f90:8", "const:4:8"]]
+ 00ac8f90 ["CALL", null, ["callee:00418fe0:8"]]
- 00ac8ec8 bytes 4640e597
+ 00ac8f90 bytes 1440e597
~~~


<a id="compare-5d9cd7e52cd478c2bb9822cab57e83b5"></a>

### [`00ac9a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9a24.md) → [`00ac9aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md) FUN_00ac9aec

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00729118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00729/00729118.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00729118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00729/00729118.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9a24.md#insn-00ac9a9c) · [`00ac9ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9a24.md#insn-00ac9ac0) · [`00ac9aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9a24.md#insn-00ac9aec)
- 新版 [`00ac9b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9b64) · [`00ac9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9b88) · [`00ac9bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9aec.md#insn-00ac9bb4)

~~~diff
- 00ac9a9c ["INT_ADD", "register:40f0:8", ["const:ac9a9c:8", "const:4:8"]]
- 00ac9a9c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ac9b64 ["INT_ADD", "register:40f0:8", ["const:ac9b64:8", "const:4:8"]]
+ 00ac9b64 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ac9a9c bytes 29450494
+ 00ac9b64 bytes 23450494
- 00ac9ac0 ["INT_ADD", "register:40f0:8", ["const:ac9ac0:8", "const:4:8"]]
- 00ac9ac0 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9b88 ["INT_ADD", "register:40f0:8", ["const:ac9b88:8", "const:4:8"]]
+ 00ac9b88 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9ac0 bytes a0450494
+ 00ac9b88 bytes 9a450494
- 00ac9aec ["INT_ADD", "register:40f0:8", ["const:ac9aec:8", "const:4:8"]]
- 00ac9aec ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9bb4 ["INT_ADD", "register:40f0:8", ["const:ac9bb4:8", "const:4:8"]]
+ 00ac9bb4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9aec bytes 95450494
+ 00ac9bb4 bytes 8f450494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa84e25c69822e2815c8faedb46e618"></a>

### [`00ac9b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9b50.md) → [`00ac9c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md) FUN_00ac9c18

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00ac9d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d00.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00ac9dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9dc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9b50.md#insn-00ac9c04) · [`00ac9c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9b50.md#insn-00ac9c4c) · [`00ac9ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9b50.md#insn-00ac9ca0)
- 新版 [`00ac9ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9ccc) · [`00ac9d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9d14) · [`00ac9d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9c18.md#insn-00ac9d68)

~~~diff
- 00ac9c04 ["INT_ADD", "register:40f0:8", ["const:ac9c04:8", "const:4:8"]]
- 00ac9c04 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ac9ccc ["INT_ADD", "register:40f0:8", ["const:ac9ccc:8", "const:4:8"]]
+ 00ac9ccc ["CALL", null, ["callee:00bdaff0:8"]]
- 00ac9c04 bytes cf440494
+ 00ac9ccc bytes c9440494
- 00ac9c4c ["INT_ADD", "register:40f0:8", ["const:ac9c4c:8", "const:4:8"]]
- 00ac9c4c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9d14 ["INT_ADD", "register:40f0:8", ["const:ac9d14:8", "const:4:8"]]
+ 00ac9d14 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9c4c bytes 3d450494
+ 00ac9d14 bytes 37450494
- 00ac9ca0 ["INT_ADD", "register:40f0:8", ["const:ac9ca0:8", "const:4:8"]]
- 00ac9ca0 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9d68 ["INT_ADD", "register:40f0:8", ["const:ac9d68:8", "const:4:8"]]
+ 00ac9d68 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9ca0 bytes 28450494
+ 00ac9d68 bytes 22450494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d5fb2fbd097f47883c24c3b981a46a9"></a>

### [`00ac9d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d14.md) → [`00ac9ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md) FUN_00ac9ddc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00ac9ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9ea8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00ac9f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d14.md#insn-00ac9dbc) · [`00ac9dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d14.md#insn-00ac9dfc) · [`00ac9e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9d14.md#insn-00ac9e40)
- 新版 [`00ac9e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9e84) · [`00ac9ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9ec4) · [`00ac9f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9ddc.md#insn-00ac9f08)

~~~diff
- 00ac9dbc ["INT_ADD", "register:40f0:8", ["const:ac9dbc:8", "const:4:8"]]
- 00ac9dbc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ac9e84 ["INT_ADD", "register:40f0:8", ["const:ac9e84:8", "const:4:8"]]
+ 00ac9e84 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ac9dbc bytes 61440494
+ 00ac9e84 bytes 5b440494
- 00ac9dfc ["INT_ADD", "register:40f0:8", ["const:ac9dfc:8", "const:4:8"]]
- 00ac9dfc ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9ec4 ["INT_ADD", "register:40f0:8", ["const:ac9ec4:8", "const:4:8"]]
+ 00ac9ec4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9dfc bytes d1440494
+ 00ac9ec4 bytes cb440494
- 00ac9e40 ["INT_ADD", "register:40f0:8", ["const:ac9e40:8", "const:4:8"]]
- 00ac9e40 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00ac9f08 ["INT_ADD", "register:40f0:8", ["const:ac9f08:8", "const:4:8"]]
+ 00ac9f08 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9e40 bytes c0440494
+ 00ac9f08 bytes ba440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a10a6e6c7799a2a84325173a0f9d15d4"></a>

### [`00ac9ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9ebc.md) → [`00ac9f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md) FUN_00ac9f84

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aca04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca04c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca114.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9ebc.md#insn-00ac9f60) · [`00ac9fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9ebc.md#insn-00ac9fa0) · [`00ac9fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac9/00ac9ebc.md#insn-00ac9fec)
- 新版 [`00aca028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca028) · [`00aca068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca068) · [`00aca0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9f84.md#insn-00aca0b4)

~~~diff
- 00ac9f60 ["INT_ADD", "register:40f0:8", ["const:ac9f60:8", "const:4:8"]]
- 00ac9f60 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca028 ["INT_ADD", "register:40f0:8", ["const:aca028:8", "const:4:8"]]
+ 00aca028 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ac9f60 bytes f8430494
+ 00aca028 bytes f2430494
- 00ac9fa0 ["INT_ADD", "register:40f0:8", ["const:ac9fa0:8", "const:4:8"]]
- 00ac9fa0 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca068 ["INT_ADD", "register:40f0:8", ["const:aca068:8", "const:4:8"]]
+ 00aca068 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9fa0 bytes 68440494
+ 00aca068 bytes 62440494
- 00ac9fec ["INT_ADD", "register:40f0:8", ["const:ac9fec:8", "const:4:8"]]
- 00ac9fec ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca0b4 ["INT_ADD", "register:40f0:8", ["const:aca0b4:8", "const:4:8"]]
+ 00aca0b4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00ac9fec bytes 55440494
+ 00aca0b4 bytes 4f440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a41625d92d3cedd0207f519303fc7a"></a>

### [`00aca060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca060.md) → [`00aca128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md) FUN_00aca128

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aca18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca18c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca254.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca060.md#insn-00aca0d8) · [`00aca0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca060.md#insn-00aca0fc) · [`00aca128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca060.md#insn-00aca128)
- 新版 [`00aca1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1a0) · [`00aca1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1c4) · [`00aca1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca128.md#insn-00aca1f0)

~~~diff
- 00aca0d8 ["INT_ADD", "register:40f0:8", ["const:aca0d8:8", "const:4:8"]]
- 00aca0d8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca1a0 ["INT_ADD", "register:40f0:8", ["const:aca1a0:8", "const:4:8"]]
+ 00aca1a0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aca0d8 bytes 9a430494
+ 00aca1a0 bytes 94430494
- 00aca0fc ["INT_ADD", "register:40f0:8", ["const:aca0fc:8", "const:4:8"]]
- 00aca0fc ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca1c4 ["INT_ADD", "register:40f0:8", ["const:aca1c4:8", "const:4:8"]]
+ 00aca1c4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca0fc bytes 11440494
+ 00aca1c4 bytes 0b440494
- 00aca128 ["INT_ADD", "register:40f0:8", ["const:aca128:8", "const:4:8"]]
- 00aca128 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca1f0 ["INT_ADD", "register:40f0:8", ["const:aca1f0:8", "const:4:8"]]
+ 00aca1f0 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca128 bytes 06440494
+ 00aca1f0 bytes 00440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-114475b9bb8661f40633fd0f1fa61b3a"></a>

### [`00aca1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca1a0.md) → [`00aca268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md) FUN_00aca268

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aca334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca334.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca3fc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca1a0.md#insn-00aca248) · [`00aca288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca1a0.md#insn-00aca288) · [`00aca2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca1a0.md#insn-00aca2cc)
- 新版 [`00aca310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca310) · [`00aca350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca350) · [`00aca394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca268.md#insn-00aca394)

~~~diff
- 00aca248 ["INT_ADD", "register:40f0:8", ["const:aca248:8", "const:4:8"]]
- 00aca248 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca310 ["INT_ADD", "register:40f0:8", ["const:aca310:8", "const:4:8"]]
+ 00aca310 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aca248 bytes 3e430494
+ 00aca310 bytes 38430494
- 00aca288 ["INT_ADD", "register:40f0:8", ["const:aca288:8", "const:4:8"]]
- 00aca288 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca350 ["INT_ADD", "register:40f0:8", ["const:aca350:8", "const:4:8"]]
+ 00aca350 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca288 bytes ae430494
+ 00aca350 bytes a8430494
- 00aca2cc ["INT_ADD", "register:40f0:8", ["const:aca2cc:8", "const:4:8"]]
- 00aca2cc ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca394 ["INT_ADD", "register:40f0:8", ["const:aca394:8", "const:4:8"]]
+ 00aca394 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca2cc bytes 9d430494
+ 00aca394 bytes 97430494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8276d146fc8edaec275a56fb0d758ece"></a>

### [`00aca348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca348.md) → [`00aca410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md) FUN_00aca410

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aca4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca4d8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca3ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca348.md#insn-00aca3ec) · [`00aca42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca348.md#insn-00aca42c) · [`00aca478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca348.md#insn-00aca478)
- 新版 [`00aca4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca4b4) · [`00aca4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca4f4) · [`00aca540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca410.md#insn-00aca540)

~~~diff
- 00aca3ec ["INT_ADD", "register:40f0:8", ["const:aca3ec:8", "const:4:8"]]
- 00aca3ec ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca4b4 ["INT_ADD", "register:40f0:8", ["const:aca4b4:8", "const:4:8"]]
+ 00aca4b4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aca3ec bytes d5420494
+ 00aca4b4 bytes cf420494
- 00aca42c ["INT_ADD", "register:40f0:8", ["const:aca42c:8", "const:4:8"]]
- 00aca42c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca4f4 ["INT_ADD", "register:40f0:8", ["const:aca4f4:8", "const:4:8"]]
+ 00aca4f4 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca42c bytes 45430494
+ 00aca4f4 bytes 3f430494
- 00aca478 ["INT_ADD", "register:40f0:8", ["const:aca478:8", "const:4:8"]]
- 00aca478 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca540 ["INT_ADD", "register:40f0:8", ["const:aca540:8", "const:4:8"]]
+ 00aca540 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca478 bytes 32430494
+ 00aca540 bytes 2c430494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca22f4be79ba5779f69e673d7daf3560"></a>

### [`00aca500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca500.md) → [`00aca5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md) FUN_00aca5c8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ab3338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab3/00ab3338.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00aca62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca62c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ab3400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab3/00ab3400.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00aca6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca6f4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca500.md#insn-00aca578) · [`00aca59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca500.md#insn-00aca59c) · [`00aca5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca500.md#insn-00aca5c8)
- 新版 [`00aca640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca640) · [`00aca664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca664) · [`00aca690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca5c8.md#insn-00aca690)

~~~diff
- 00aca578 ["INT_ADD", "register:40f0:8", ["const:aca578:8", "const:4:8"]]
- 00aca578 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca640 ["INT_ADD", "register:40f0:8", ["const:aca640:8", "const:4:8"]]
+ 00aca640 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aca578 bytes 72420494
+ 00aca640 bytes 6c420494
- 00aca59c ["INT_ADD", "register:40f0:8", ["const:aca59c:8", "const:4:8"]]
- 00aca59c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca664 ["INT_ADD", "register:40f0:8", ["const:aca664:8", "const:4:8"]]
+ 00aca664 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca59c bytes e9420494
+ 00aca664 bytes e3420494
- 00aca5c8 ["INT_ADD", "register:40f0:8", ["const:aca5c8:8", "const:4:8"]]
- 00aca5c8 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00aca690 ["INT_ADD", "register:40f0:8", ["const:aca690:8", "const:4:8"]]
+ 00aca690 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00aca5c8 bytes de420494
+ 00aca690 bytes d8420494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4b27c44d205cd6feb9b7e920513040"></a>

### [`00aca878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca878.md) → [`00aca940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md) FUN_00aca940

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00acaaec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaaec.md) [`00acab00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00acabb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabb4.md) [`00acabc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aca918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca878.md#insn-00aca918) · [`00aca9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca878.md#insn-00aca9a8) · [`00aca9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca878.md#insn-00aca9c4)
- 新版 [`00aca9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00aca9e0) · [`00acaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00acaa70) · [`00acaa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md#insn-00acaa8c)

~~~diff
- 00aca918 ["INT_ADD", "register:40f0:8", ["const:aca918:8", "const:4:8"]]
- 00aca918 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aca9e0 ["INT_ADD", "register:40f0:8", ["const:aca9e0:8", "const:4:8"]]
+ 00aca9e0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aca918 bytes 8a410494
+ 00aca9e0 bytes 84410494
- 00aca9a8 ["INT_ADD", "register:40f0:8", ["const:aca9a8:8", "const:4:8"]]
- 00aca9a8 ["CALL", null, ["callee:00acabc8:8"]]
+ 00acaa70 ["INT_ADD", "register:40f0:8", ["const:acaa70:8", "const:4:8"]]
+ 00acaa70 ["CALL", null, ["callee:00acabc8:8"]]
- 00aca9a8 bytes 56000094
+ 00acaa70 bytes 56000094
- 00aca9c4 ["INT_ADD", "register:40f0:8", ["const:aca9c4:8", "const:4:8"]]
- 00aca9c4 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acaa8c ["INT_ADD", "register:40f0:8", ["const:acaa8c:8", "const:4:8"]]
+ 00acaa8c ["CALL", null, ["callee:00bdb010:8"]]
- 00aca9c4 bytes 67410494
+ 00acaa8c bytes 61410494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d351b1f679615dec29034ccd10dae4ff"></a>

### [`00acaa4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaa4c.md) → [`00acab14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md) FUN_00acab14

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acaa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaa4c.md#insn-00acaa9c) · [`00acaaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaa4c.md#insn-00acaaac) · [`00acaabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaa4c.md#insn-00acaabc)
- 新版 [`00acab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab64) · [`00acab74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab74) · [`00acab84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md#insn-00acab84)

~~~diff
- 00acaa9c ["INT_ADD", "register:40f0:8", ["const:acaa9c:8", "const:4:8"]]
- 00acaa9c ["CALL", null, ["callee:00bdb010:8"]]
+ 00acab64 ["INT_ADD", "register:40f0:8", ["const:acab64:8", "const:4:8"]]
+ 00acab64 ["CALL", null, ["callee:00bdb010:8"]]
- 00acaa9c bytes 31410494
+ 00acab64 bytes 2b410494
- 00acaaac ["INT_ADD", "register:40f0:8", ["const:acaaac:8", "const:4:8"]]
- 00acaaac ["CALL", null, ["callee:00bdb010:8"]]
+ 00acab74 ["INT_ADD", "register:40f0:8", ["const:acab74:8", "const:4:8"]]
+ 00acab74 ["CALL", null, ["callee:00bdb010:8"]]
- 00acaaac bytes 2d410494
+ 00acab74 bytes 27410494
- 00acaabc ["INT_ADD", "register:40f0:8", ["const:acaabc:8", "const:4:8"]]
- 00acaabc ["CALL", null, ["callee:00bdb010:8"]]
+ 00acab84 ["INT_ADD", "register:40f0:8", ["const:acab84:8", "const:4:8"]]
+ 00acab84 ["CALL", null, ["callee:00bdb010:8"]]
- 00acaabc bytes 29410494
+ 00acab84 bytes 23410494
~~~


<a id="compare-98fa0979f91d416e8141256e8e116073"></a>

### [`00acab00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md) → [`00acabc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md) FUN_00acabc8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00aca878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00aca878.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00aca940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00aca940.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acabc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md#insn-00acabc0) · [`00acabd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md#insn-00acabd0) · [`00acabe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acab00.md#insn-00acabe0)
- 新版 [`00acac88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acac88) · [`00acac98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acac98) · [`00acaca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acabc8.md#insn-00acaca8)

~~~diff
- 00acabc0 ["INT_ADD", "register:40f0:8", ["const:acabc0:8", "const:4:8"]]
- 00acabc0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acac88 ["INT_ADD", "register:40f0:8", ["const:acac88:8", "const:4:8"]]
+ 00acac88 ["CALL", null, ["callee:00bdb010:8"]]
- 00acabc0 bytes e8400494
+ 00acac88 bytes e2400494
- 00acabd0 ["INT_ADD", "register:40f0:8", ["const:acabd0:8", "const:4:8"]]
- 00acabd0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acac98 ["INT_ADD", "register:40f0:8", ["const:acac98:8", "const:4:8"]]
+ 00acac98 ["CALL", null, ["callee:00bdb010:8"]]
- 00acabd0 bytes e4400494
+ 00acac98 bytes de400494
- 00acabe0 ["INT_ADD", "register:40f0:8", ["const:acabe0:8", "const:4:8"]]
- 00acabe0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acaca8 ["INT_ADD", "register:40f0:8", ["const:acaca8:8", "const:4:8"]]
+ 00acaca8 ["CALL", null, ["callee:00bdb010:8"]]
- 00acabe0 bytes e0400494
+ 00acaca8 bytes da400494
~~~


<a id="compare-966b9e508915a0cbad5642eb7086c923"></a>

### [`00acae18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acae18.md) → [`00acaee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md) FUN_00acaee0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`005c3468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c3/005c3468.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acae98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acae18.md#insn-00acae98) · [`00acaecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acae18.md#insn-00acaecc) · [`00acaed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acae18.md#insn-00acaed8)
- 新版 [`00acaf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acaf60) · [`00acaf94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acaf94) · [`00acafa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acaee0.md#insn-00acafa0)

~~~diff
- 00acae98 ["INT_ADD", "register:40f0:8", ["const:acae98:8", "const:4:8"]]
- 00acae98 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00acaf60 ["INT_ADD", "register:40f0:8", ["const:acaf60:8", "const:4:8"]]
+ 00acaf60 ["CALL", null, ["callee:00bdaff0:8"]]
- 00acae98 bytes 2a400494
+ 00acaf60 bytes 24400494
- 00acaecc ["INT_ADD", "register:40f0:8", ["const:acaecc:8", "const:4:8"]]
- 00acaecc ["CALL", null, ["callee:005c3468:8"]]
+ 00acaf94 ["INT_ADD", "register:40f0:8", ["const:acaf94:8", "const:4:8"]]
+ 00acaf94 ["CALL", null, ["callee:005c3468:8"]]
- 00acaecc bytes 67e1eb97
+ 00acaf94 bytes 35e1eb97
- 00acaed8 ["INT_ADD", "register:40f0:8", ["const:acaed8:8", "const:4:8"]]
- 00acaed8 ["CALL", null, ["callee:005c3468:8"]]
+ 00acafa0 ["INT_ADD", "register:40f0:8", ["const:acafa0:8", "const:4:8"]]
+ 00acafa0 ["CALL", null, ["callee:005c3468:8"]]
- 00acaed8 bytes 64e1eb97
+ 00acafa0 bytes 32e1eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c47a46eea2df630490c665abc6b2a57a"></a>

### [`00acaf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaf84.md) → [`00acb04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md) FUN_00acb04c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 6件 [`005f064c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062c/0062ca28.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 6件 [`005f064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062ca28.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acaffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaf84.md#insn-00acaffc) · [`00acb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaf84.md#insn-00acb020) · [`00acb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaf84.md#insn-00acb070)
- 新版 [`00acb0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb0c4) · [`00acb0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb0e8) · [`00acb138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb04c.md#insn-00acb138)

~~~diff
- 00acaffc ["INT_ADD", "register:40f0:8", ["const:acaffc:8", "const:4:8"]]
- 00acaffc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00acb0c4 ["INT_ADD", "register:40f0:8", ["const:acb0c4:8", "const:4:8"]]
+ 00acb0c4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00acaffc bytes d13f0494
+ 00acb0c4 bytes cb3f0494
- 00acb020 ["INT_ADD", "register:40f0:8", ["const:acb020:8", "const:4:8"]]
- 00acb020 ["CALL", null, ["callee:0062ca28:8"]]
+ 00acb0e8 ["INT_ADD", "register:40f0:8", ["const:acb0e8:8", "const:4:8"]]
+ 00acb0e8 ["CALL", null, ["callee:0062ca28:8"]]
- 00acb020 bytes 8286ed97
+ 00acb0e8 bytes 5086ed97
- 00acb070 ["INT_ADD", "register:40f0:8", ["const:acb070:8", "const:4:8"]]
- 00acb070 ["CALL", null, ["callee:005f064c:8"]]
+ 00acb138 ["INT_ADD", "register:40f0:8", ["const:acb138:8", "const:4:8"]]
+ 00acb138 ["CALL", null, ["callee:005f064c:8"]]
- 00acb070 bytes 7795ec97
+ 00acb138 bytes 4595ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb8be75ea0565d06de719a2c0bdfebd"></a>

### [`00acb0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md) → [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) FUN_00acb174

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`005f064c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062c/0062ca28.md) [`00acb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb330.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`005f064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f064c.md) [`0062c99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062c99c.md) [`0062ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062ca28.md) [`00acb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md#insn-00acb150) · [`00acb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md#insn-00acb1b0) · [`00acb1d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md#insn-00acb1d4)
- 新版 [`00acb218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb218) · [`00acb278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb278) · [`00acb29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md#insn-00acb29c)

~~~diff
- 00acb150 ["INT_ADD", "register:40f0:8", ["const:acb150:8", "const:4:8"]]
- 00acb150 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00acb218 ["INT_ADD", "register:40f0:8", ["const:acb218:8", "const:4:8"]]
+ 00acb218 ["CALL", null, ["callee:00bdaff0:8"]]
- 00acb150 bytes 7c3f0494
+ 00acb218 bytes 763f0494
- 00acb1b0 ["INT_ADD", "register:40f0:8", ["const:acb1b0:8", "const:4:8"]]
- 00acb1b0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00acb278 ["INT_ADD", "register:40f0:8", ["const:acb278:8", "const:4:8"]]
+ 00acb278 ["CALL", null, ["callee:00bdaff0:8"]]
- 00acb1b0 bytes 643f0494
+ 00acb278 bytes 5e3f0494
- 00acb1d4 ["INT_ADD", "register:40f0:8", ["const:acb1d4:8", "const:4:8"]]
- 00acb1d4 ["CALL", null, ["callee:0062ca28:8"]]
+ 00acb29c ["INT_ADD", "register:40f0:8", ["const:acb29c:8", "const:4:8"]]
+ 00acb29c ["CALL", null, ["callee:0062ca28:8"]]
- 00acb1d4 bytes 1586ed97
+ 00acb29c bytes e385ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9fd48f40727bd6ac3242e247eb97ff"></a>

### [`00acb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb330.md) → [`00acb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md) FUN_00acb3f8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb330.md#insn-00acb3ac) · [`00acb3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb330.md#insn-00acb3f4)
- 新版 [`00acb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md#insn-00acb474) · [`00acb4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb3f8.md#insn-00acb4bc)

~~~diff
- 00acb3ac ["INT_ADD", "register:40f0:8", ["const:acb3ac:8", "const:4:8"]]
- 00acb3ac ["CALL", null, ["callee:00bdb010:8"]]
+ 00acb474 ["INT_ADD", "register:40f0:8", ["const:acb474:8", "const:4:8"]]
+ 00acb474 ["CALL", null, ["callee:00bdb010:8"]]
- 00acb3ac bytes ed3e0494
+ 00acb474 bytes e73e0494
- 00acb3f4 ["INT_ADD", "register:40f0:8", ["const:acb3f4:8", "const:4:8"]]
- 00acb3f4 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acb4bc ["INT_ADD", "register:40f0:8", ["const:acb4bc:8", "const:4:8"]]
+ 00acb4bc ["CALL", null, ["callee:00bdb010:8"]]
- 00acb3f4 bytes db3e0494
+ 00acb4bc bytes d53e0494
~~~


<a id="compare-36334344a298cd0d6043e26cab06f647"></a>

### [`00acb44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb44c.md) → [`00acb514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md) FUN_00acb514

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acb0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb0ac.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00acb174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acb480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb44c.md#insn-00acb480) · [`00acb4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb44c.md#insn-00acb4d0)
- 新版 [`00acb548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md#insn-00acb548) · [`00acb598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb514.md#insn-00acb598)

~~~diff
- 00acb480 ["INT_ADD", "register:40f0:8", ["const:acb480:8", "const:4:8"]]
- 00acb480 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acb548 ["INT_ADD", "register:40f0:8", ["const:acb548:8", "const:4:8"]]
+ 00acb548 ["CALL", null, ["callee:00bdb010:8"]]
- 00acb480 bytes b83e0494
+ 00acb548 bytes b23e0494
- 00acb4d0 ["INT_ADD", "register:40f0:8", ["const:acb4d0:8", "const:4:8"]]
- 00acb4d0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acb598 ["INT_ADD", "register:40f0:8", ["const:acb598:8", "const:4:8"]]
+ 00acb598 ["CALL", null, ["callee:00bdb010:8"]]
- 00acb4d0 bytes a43e0494
+ 00acb598 bytes 9e3e0494
~~~


<a id="compare-97f074ca5982662c546c823a8415ff7f"></a>

### [`00acbc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md) → [`00acbcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md) FUN_00acbcd0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00418a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418a68.md) [`00418b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md) · 呼出先 4件 [`00449bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bcc.md) [`00449be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449be4.md) [`00449bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bf0.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00418a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a68.md) [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 4件 [`00449bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bcc.md) [`00449be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449be4.md) [`00449bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bf0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acbc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md#insn-00acbc18) · [`00acbc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md#insn-00acbc20) · [`00acbc28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md#insn-00acbc28)
- 新版 [`00acbce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbce0) · [`00acbce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbce8) · [`00acbcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md#insn-00acbcf0)

~~~diff
- 00acbc18 ["INT_ADD", "register:40f0:8", ["const:acbc18:8", "const:4:8"]]
- 00acbc18 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbce0 ["INT_ADD", "register:40f0:8", ["const:acbce0:8", "const:4:8"]]
+ 00acbce0 ["CALL", null, ["callee:0081f580:8"]]
- 00acbc18 bytes 5a4ef597
+ 00acbce0 bytes 284ef597
- 00acbc20 ["INT_ADD", "register:40f0:8", ["const:acbc20:8", "const:4:8"]]
- 00acbc20 ["CALL", null, ["callee:00449be4:8"]]
+ 00acbce8 ["INT_ADD", "register:40f0:8", ["const:acbce8:8", "const:4:8"]]
+ 00acbce8 ["CALL", null, ["callee:00449be4:8"]]
- 00acbc20 bytes f1f7e597
+ 00acbce8 bytes bff7e597
- 00acbc28 ["INT_ADD", "register:40f0:8", ["const:acbc28:8", "const:4:8"]]
- 00acbc28 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbcf0 ["INT_ADD", "register:40f0:8", ["const:acbcf0:8", "const:4:8"]]
+ 00acbcf0 ["CALL", null, ["callee:0081f580:8"]]
- 00acbc28 bytes 564ef597
+ 00acbcf0 bytes 244ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a77b6d632f0e26140c4885f1e2e89b9"></a>

### [`00acbc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc70.md) → [`00acbd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd38.md) FUN_00acbd38

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004188e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004188e8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`004188e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004188e8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acbc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc70.md#insn-00acbc80)
- 新版 [`00acbd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd38.md#insn-00acbd48)

~~~diff
- 00acbc80 ["INT_ADD", "register:40f0:8", ["const:acbc80:8", "const:4:8"]]
- 00acbc80 ["CALL", null, ["callee:0081f580:8"]]
+ 00acbd48 ["INT_ADD", "register:40f0:8", ["const:acbd48:8", "const:4:8"]]
+ 00acbd48 ["CALL", null, ["callee:0081f580:8"]]
- 00acbc80 bytes 404ef597
+ 00acbd48 bytes 0e4ef597
~~~


<a id="compare-10769979e3fc2a07a930e5ea0af80c47"></a>

### [`00acc460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md) → [`00acc528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) FUN_00acc528

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md) · 呼出先 5件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c9f4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`004588f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00458/004588f4.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 5件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9f4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`004588f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/004588f4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acc468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md#insn-00acc468) · [`00acc474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md#insn-00acc474) · [`00acc478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md#insn-00acc478)
- 新版 [`00acc530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc530) · [`00acc53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc53c) · [`00acc540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md#insn-00acc540)

~~~diff
- 00acc468 ["INT_ADD", "register:40f0:8", ["const:acc468:8", "const:4:8"]]
- 00acc468 ["CALL", null, ["callee:0081f580:8"]]
+ 00acc530 ["INT_ADD", "register:40f0:8", ["const:acc530:8", "const:4:8"]]
+ 00acc530 ["CALL", null, ["callee:0081f580:8"]]
- 00acc468 bytes 464cf597
+ 00acc530 bytes 144cf597
- 00acc474 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acc474 ["INT_ADD", "register:40f0:8", ["const:acc474:8", "const:4:8"]]
- 00acc474 ["CALLIND", null, ["register:0:8"]]
+ 00acc53c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acc53c ["INT_ADD", "register:40f0:8", ["const:acc53c:8", "const:4:8"]]
+ 00acc53c ["CALLIND", null, ["register:0:8"]]
- 00acc474 bytes 00013fd6
+ 00acc53c bytes 00013fd6
- 00acc478 ["INT_ADD", "register:40f0:8", ["const:acc478:8", "const:4:8"]]
- 00acc478 ["CALL", null, ["ram:457e1c:8"]]
+ 00acc540 ["INT_ADD", "register:40f0:8", ["const:acc540:8", "const:4:8"]]
+ 00acc540 ["CALL", null, ["ram:457e1c:8"]]
- 00acc478 bytes 692ee697
+ 00acc540 bytes 372ee697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce1b2b2f5e63758c32e4210f9afcd18e"></a>

### [`00acd284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd284.md) → [`00acd34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md) FUN_00acd34c

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd284.md#insn-00acd2a0)
- 新版 [`00acd368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md#insn-00acd368)

~~~diff
- 00acd2a0 ["INT_ADD", "register:40f0:8", ["const:acd2a0:8", "const:4:8"]]
- 00acd2a0 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd368 ["INT_ADD", "register:40f0:8", ["const:acd368:8", "const:4:8"]]
+ 00acd368 ["CALL", null, ["callee:0081f580:8"]]
- 00acd2a0 bytes b848f597
+ 00acd368 bytes 8648f597
~~~


<a id="compare-bc0629a036944166d76c728dd0ea991c"></a>

### [`00acd2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd2cc.md) → [`00acd394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md) FUN_00acd394

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd2cc.md#insn-00acd2e8)
- 新版 [`00acd3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md#insn-00acd3b0)

~~~diff
- 00acd2e8 ["INT_ADD", "register:40f0:8", ["const:acd2e8:8", "const:4:8"]]
- 00acd2e8 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd3b0 ["INT_ADD", "register:40f0:8", ["const:acd3b0:8", "const:4:8"]]
+ 00acd3b0 ["CALL", null, ["callee:0081f580:8"]]
- 00acd2e8 bytes a648f597
+ 00acd3b0 bytes 7448f597
~~~


<a id="compare-2280ad98bb776e1586701e6966fd90c8"></a>

### [`00acd314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd314.md) → [`00acd3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md) FUN_00acd3dc

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd314.md#insn-00acd330)
- 新版 [`00acd3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md#insn-00acd3f8)

~~~diff
- 00acd330 ["INT_ADD", "register:40f0:8", ["const:acd330:8", "const:4:8"]]
- 00acd330 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd3f8 ["INT_ADD", "register:40f0:8", ["const:acd3f8:8", "const:4:8"]]
+ 00acd3f8 ["CALL", null, ["callee:0081f580:8"]]
- 00acd330 bytes 9448f597
+ 00acd3f8 bytes 6248f597
~~~


<a id="compare-ec5975b14a4f5f62aabdbd9efc615d85"></a>

### [`00acd360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd360.md) → [`00acd428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md) FUN_00acd428

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00418a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418a54.md) · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`004215a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md) [`00423bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bb8.md)
- 新版 呼出元 1件 [`00418a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a54.md) · 呼出先 8件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`00423bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd360.md#insn-00acd370) · [`00acd374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd360.md#insn-00acd374) · [`00acd380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd360.md#insn-00acd380)
- 新版 [`00acd438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd438) · [`00acd43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd43c) · [`00acd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd428.md#insn-00acd448)

~~~diff
- 00acd370 ["INT_ADD", "register:40f0:8", ["const:acd370:8", "const:4:8"]]
- 00acd370 ["CALL", null, ["callee:00646dc4:8"]]
+ 00acd438 ["INT_ADD", "register:40f0:8", ["const:acd438:8", "const:4:8"]]
+ 00acd438 ["CALL", null, ["callee:00646dc4:8"]]
- 00acd370 bytes 95e6ed97
+ 00acd438 bytes 63e6ed97
- 00acd374 ["INT_ADD", "register:40f0:8", ["const:acd374:8", "const:4:8"]]
- 00acd374 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd43c ["INT_ADD", "register:40f0:8", ["const:acd43c:8", "const:4:8"]]
+ 00acd43c ["CALL", null, ["callee:0081f580:8"]]
- 00acd374 bytes 8348f597
+ 00acd43c bytes 5148f597
- 00acd380 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acd380 ["INT_ADD", "register:40f0:8", ["const:acd380:8", "const:4:8"]]
- 00acd380 ["CALLIND", null, ["register:0:8"]]
+ 00acd448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acd448 ["INT_ADD", "register:40f0:8", ["const:acd448:8", "const:4:8"]]
+ 00acd448 ["CALLIND", null, ["register:0:8"]]
- 00acd380 bytes 00013fd6
+ 00acd448 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4657eddb2108dc27625e794a5a9e350b"></a>

### [`00acd428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd428.md) → [`00acd4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4f0.md) FUN_00acd4f0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd428.md#insn-00acd430)
- 新版 [`00acd4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4f0.md#insn-00acd4f8)

~~~diff
- 00acd430 ["INT_ADD", "register:40f0:8", ["const:acd430:8", "const:4:8"]]
- 00acd430 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd4f8 ["INT_ADD", "register:40f0:8", ["const:acd4f8:8", "const:4:8"]]
+ 00acd4f8 ["CALL", null, ["callee:0081f580:8"]]
- 00acd430 bytes 5448f597
+ 00acd4f8 bytes 2248f597
~~~


<a id="compare-4bc5eca8c93768c7dec68671d9dbabbb"></a>

### [`00acd4ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd4ac.md) → [`00acd574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd574.md) FUN_00acd574

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd4ac.md#insn-00acd4b4)
- 新版 [`00acd57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd574.md#insn-00acd57c)

~~~diff
- 00acd4b4 ["INT_ADD", "register:40f0:8", ["const:acd4b4:8", "const:4:8"]]
- 00acd4b4 ["CALL", null, ["callee:0081f580:8"]]
+ 00acd57c ["INT_ADD", "register:40f0:8", ["const:acd57c:8", "const:4:8"]]
+ 00acd57c ["CALL", null, ["callee:0081f580:8"]]
- 00acd4b4 bytes 3348f597
+ 00acd57c bytes 0148f597
~~~


<a id="compare-7a430d068f4c2b71ae66d4576c50be25"></a>

### [`00acd838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd838.md) → [`00acd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd900.md) FUN_00acd900

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acc48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc48c.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00acc554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc554.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acd858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd838.md#insn-00acd858)
- 新版 [`00acd920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd900.md#insn-00acd920)

~~~diff
- 00acd858 ["INT_ADD", "register:40f0:8", ["const:acd858:8", "const:4:8"]]
- 00acd858 ["CALL", null, ["callee:00bdb010:8"]]
+ 00acd920 ["INT_ADD", "register:40f0:8", ["const:acd920:8", "const:4:8"]]
+ 00acd920 ["CALL", null, ["callee:00bdb010:8"]]
- 00acd858 bytes c2350494
+ 00acd920 bytes bc350494
~~~


<a id="compare-907890f1fdc3ae7f2b059e1727f39bba"></a>

### [`00acf360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf360.md) → [`00acf428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md) FUN_00acf428

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00934148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00934/00934148.md) [`0094847c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md) · 呼出先 2件 [`0066f824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0066f/0066f824.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0094847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md) · 呼出先 2件 [`0066f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf360.md#insn-00acf3a0) · [`00acf3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf360.md#insn-00acf3c8)
- 新版 [`00acf468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md#insn-00acf468) · [`00acf490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf428.md#insn-00acf490)

~~~diff
- 00acf3a0 ["INT_ADD", "register:40f0:8", ["const:acf3a0:8", "const:4:8"]]
- 00acf3a0 ["CALL", null, ["callee:0066f824:8"]]
+ 00acf468 ["INT_ADD", "register:40f0:8", ["const:acf468:8", "const:4:8"]]
+ 00acf468 ["CALL", null, ["callee:0066f824:8"]]
- 00acf3a0 bytes 2181ee97
+ 00acf468 bytes ef80ee97
- 00acf3c8 ["INT_ADD", "register:40f0:8", ["const:acf3c8:8", "const:4:8"]]
- 00acf3c8 ["CALL", null, ["callee:00bdb040:8"]]
+ 00acf490 ["INT_ADD", "register:40f0:8", ["const:acf490:8", "const:4:8"]]
+ 00acf490 ["CALL", null, ["callee:00bdb040:8"]]
- 00acf3c8 bytes f22e0494
+ 00acf490 bytes ec2e0494
~~~


<a id="compare-974abce9a1344e1ced6bd465efebc3fb"></a>

### [`00acf804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf804.md) → [`00acf8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md) FUN_00acf8cc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e5/005e53dc.md) [`0063e818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e818.md) [`0063e8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e8b4.md) [`0063ea04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063ea04.md) [`006e34b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006e3/006e34b0.md) · 呼出先 1件 [`00adbf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf88.md)
- 新版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`0063e818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e818.md) [`0063e8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e8b4.md) [`0063ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063ea04.md) [`006e34b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e3/006e34b0.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf804.md#insn-00acf80c)
- 新版 [`00acf8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md#insn-00acf8d4)

~~~diff
- 00acf80c ["INT_ADD", "register:40f0:8", ["const:acf80c:8", "const:4:8"]]
- 00acf80c ["CALL", null, ["callee:00adc050:8"]]
+ 00acf8d4 ["INT_ADD", "register:40f0:8", ["const:acf8d4:8", "const:4:8"]]
+ 00acf8d4 ["CALL", null, ["callee:00adc050:8"]]
- 00acf80c bytes df310094
+ 00acf8d4 bytes df310094
~~~


<a id="compare-54919a2bd62467cb4e16fe8f04e2788f"></a>

### [`00acf894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf894.md) → [`00acf95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md) FUN_00acf95c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e5/005e53dc.md) [`0063e774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e774.md) [`0063e8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e8b4.md) [`0063e910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e910.md) [`0063edf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063edf8.md) · 呼出先 1件 [`00adbf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf88.md)
- 新版 呼出元 18件 [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`0063e774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e774.md) [`0063e8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e8b4.md) [`0063e910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e910.md) [`0063edf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063edf8.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf894.md#insn-00acf89c)
- 新版 [`00acf964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md#insn-00acf964)

~~~diff
- 00acf89c ["INT_ADD", "register:40f0:8", ["const:acf89c:8", "const:4:8"]]
- 00acf89c ["CALL", null, ["callee:00adc050:8"]]
+ 00acf964 ["INT_ADD", "register:40f0:8", ["const:acf964:8", "const:4:8"]]
+ 00acf964 ["CALL", null, ["callee:00adc050:8"]]
- 00acf89c bytes bb310094
+ 00acf964 bytes bb310094
~~~


<a id="compare-46d4e391faec96e19103e860b38d7b8b"></a>

### [`00acf9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf9cc.md) → [`00acfa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md) FUN_00acfa94

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 33件 [`0058b674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058b/0058b674.md) [`005d8f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d8/005d8f58.md) [`00617dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00617/00617dec.md) [`00624a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00624/00624a0c.md) [`0062da7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062da7c.md) · 呼出先 1件 [`00adbf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf88.md)
- 新版 呼出元 33件 [`0058b674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058b/0058b674.md) [`005d8f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d8/005d8f58.md) [`00617dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00617/00617dec.md) [`00624a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00624/00624a0c.md) [`0062da7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da7c.md) · 呼出先 1件 [`00adc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acf9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf9cc.md#insn-00acf9e0) · [`00acf9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acf9cc.md#insn-00acf9fc)
- 新版 [`00acfaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md#insn-00acfaa8) · [`00acfac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md#insn-00acfac4)

~~~diff
- 00acf9e0 ["INT_ADD", "register:40f0:8", ["const:acf9e0:8", "const:4:8"]]
- 00acf9e0 ["CALL", null, ["callee:00adc050:8"]]
+ 00acfaa8 ["INT_ADD", "register:40f0:8", ["const:acfaa8:8", "const:4:8"]]
+ 00acfaa8 ["CALL", null, ["callee:00adc050:8"]]
- 00acf9e0 bytes 6a310094
+ 00acfaa8 bytes 6a310094
- 00acf9fc ["INT_ADD", "register:40f0:8", ["const:acf9fc:8", "const:4:8"]]
- 00acf9fc ["CALL", null, ["callee:00adc050:8"]]
+ 00acfac4 ["INT_ADD", "register:40f0:8", ["const:acfac4:8", "const:4:8"]]
+ 00acfac4 ["CALL", null, ["callee:00adc050:8"]]
- 00acf9fc bytes 63310094
+ 00acfac4 bytes 63310094
~~~


<a id="compare-08de87e69e43018e25d420b16037dd6c"></a>

### [`00acfd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfd54.md) → [`00acfe1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md) FUN_00acfe1c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acfa20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfa20.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00ad082c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad082c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00acfae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfae8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad08f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad08f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00acfdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfd54.md#insn-00acfdb0) · [`00acfdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfd54.md#insn-00acfdc4) · [`00acfdf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfd54.md#insn-00acfdf8)
- 新版 [`00acfe78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfe78) · [`00acfe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfe8c) · [`00acfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfe1c.md#insn-00acfec0)

~~~diff
- 00acfdb0 ["INT_ADD", "register:40f0:8", ["const:acfdb0:8", "const:4:8"]]
- 00acfdb0 ["CALL", null, ["callee:00418fe0:8"]]
+ 00acfe78 ["INT_ADD", "register:40f0:8", ["const:acfe78:8", "const:4:8"]]
+ 00acfe78 ["CALL", null, ["callee:00418fe0:8"]]
- 00acfdb0 bytes 8c24e597
+ 00acfe78 bytes 5a24e597
- 00acfdc4 ["INT_ADD", "register:40f0:8", ["const:acfdc4:8", "const:4:8"]]
- 00acfdc4 ["CALL", null, ["callee:00418fe0:8"]]
+ 00acfe8c ["INT_ADD", "register:40f0:8", ["const:acfe8c:8", "const:4:8"]]
+ 00acfe8c ["CALL", null, ["callee:00418fe0:8"]]
- 00acfdc4 bytes 8724e597
+ 00acfe8c bytes 5524e597
- 00acfdf8 ["INT_ADD", "register:40f0:8", ["const:acfdf8:8", "const:4:8"]]
- 00acfdf8 ["CALL", null, ["callee:00ad08f4:8"]]
+ 00acfec0 ["INT_ADD", "register:40f0:8", ["const:acfec0:8", "const:4:8"]]
+ 00acfec0 ["CALL", null, ["callee:00ad08f4:8"]]
- 00acfdf8 bytes 8d020094
+ 00acfec0 bytes 8d020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8897b8c0430c76332b3d536e0d9ff002"></a>

### [`00ad192c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad192c.md) → [`00ad19f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md) FUN_00ad19f4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad05f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad0/00ad05f0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00ad1b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad1b6c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00ad06b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad06b8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00ad1c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad1c34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad1994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad192c.md#insn-00ad1994) · [`00ad19bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad192c.md#insn-00ad19bc) · [`00ad19e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad1/00ad192c.md#insn-00ad19e8)
- 新版 [`00ad1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1a5c) · [`00ad1a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1a84) · [`00ad1ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad1/00ad19f4.md#insn-00ad1ab0)

~~~diff
- 00ad1994 ["INT_ADD", "register:40f0:8", ["const:ad1994:8", "const:4:8"]]
- 00ad1994 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1a5c ["INT_ADD", "register:40f0:8", ["const:ad1a5c:8", "const:4:8"]]
+ 00ad1a5c ["CALL", null, ["callee:00418fe0:8"]]
- 00ad1994 bytes 931de597
+ 00ad1a5c bytes 611de597
- 00ad19bc ["INT_ADD", "register:40f0:8", ["const:ad19bc:8", "const:4:8"]]
- 00ad19bc ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1a84 ["INT_ADD", "register:40f0:8", ["const:ad1a84:8", "const:4:8"]]
+ 00ad1a84 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad19bc bytes 891de597
+ 00ad1a84 bytes 571de597
- 00ad19e8 ["INT_ADD", "register:40f0:8", ["const:ad19e8:8", "const:4:8"]]
- 00ad19e8 ["CALL", null, ["callee:00418fe0:8"]]
+ 00ad1ab0 ["INT_ADD", "register:40f0:8", ["const:ad1ab0:8", "const:4:8"]]
+ 00ad1ab0 ["CALL", null, ["callee:00418fe0:8"]]
- 00ad19e8 bytes 7e1de597
+ 00ad1ab0 bytes 4c1de597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de39777c765a8421998ed4d64fb6af2"></a>

### [`00ad4988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4988.md) → [`00ad4a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md) FUN_00ad4a50

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad435c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad435c.md) [`00ad6bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad6bb0.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`00ad4424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4424.md) [`00ad6c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad49f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4988.md#insn-00ad49f4) · [`00ad4a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4988.md#insn-00ad4a04) · [`00ad4a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4988.md#insn-00ad4a24)
- 新版 [`00ad4abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4abc) · [`00ad4acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4acc) · [`00ad4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4a50.md#insn-00ad4aec)

~~~diff
- 00ad49f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad49f4 ["INT_ADD", "register:40f0:8", ["const:ad49f4:8", "const:4:8"]]
- 00ad49f4 ["CALLIND", null, ["register:0:8"]]
+ 00ad4abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4abc ["INT_ADD", "register:40f0:8", ["const:ad4abc:8", "const:4:8"]]
+ 00ad4abc ["CALLIND", null, ["register:0:8"]]
- 00ad49f4 bytes 00013fd6
+ 00ad4abc bytes 00013fd6
- 00ad4a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4a04 ["INT_ADD", "register:40f0:8", ["const:ad4a04:8", "const:4:8"]]
- 00ad4a04 ["CALLIND", null, ["register:0:8"]]
+ 00ad4acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4acc ["INT_ADD", "register:40f0:8", ["const:ad4acc:8", "const:4:8"]]
+ 00ad4acc ["CALLIND", null, ["register:0:8"]]
- 00ad4a04 bytes 00013fd6
+ 00ad4acc bytes 00013fd6
- 00ad4a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad4a24 ["INT_ADD", "register:40f0:8", ["const:ad4a24:8", "const:4:8"]]
- 00ad4a24 ["CALLIND", null, ["register:0:8"]]
+ 00ad4aec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad4aec ["INT_ADD", "register:40f0:8", ["const:ad4aec:8", "const:4:8"]]
+ 00ad4aec ["CALLIND", null, ["register:0:8"]]
- 00ad4a24 bytes 00013fd6
+ 00ad4aec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a3b157b419596d46335554a8710d3dc"></a>

### [`00ad4af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4af0.md) → [`00ad4bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md) FUN_00ad4bb8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad4424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4424.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00ad44ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad44ec.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad4b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4af0.md#insn-00ad4b90) · [`00ad4bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4af0.md#insn-00ad4bb4) · [`00ad4bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad4/00ad4af0.md#insn-00ad4bf8)
- 新版 [`00ad4c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4c58) · [`00ad4c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4c7c) · [`00ad4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md#insn-00ad4cc0)

~~~diff
- 00ad4b90 ["INT_ADD", "register:40f0:8", ["const:ad4b90:8", "const:4:8"]]
- 00ad4b90 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ad4c58 ["INT_ADD", "register:40f0:8", ["const:ad4c58:8", "const:4:8"]]
+ 00ad4c58 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ad4b90 bytes ec180494
+ 00ad4c58 bytes e6180494
- 00ad4bb4 ["INT_ADD", "register:40f0:8", ["const:ad4bb4:8", "const:4:8"]]
- 00ad4bb4 ["CALL", null, ["callee:00bdb140:8"]]
+ 00ad4c7c ["INT_ADD", "register:40f0:8", ["const:ad4c7c:8", "const:4:8"]]
+ 00ad4c7c ["CALL", null, ["callee:00bdb140:8"]]
- 00ad4bb4 bytes 37190494
+ 00ad4c7c bytes 31190494
- 00ad4bf8 ["INT_ADD", "register:40f0:8", ["const:ad4bf8:8", "const:4:8"]]
- 00ad4bf8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ad4cc0 ["INT_ADD", "register:40f0:8", ["const:ad4cc0:8", "const:4:8"]]
+ 00ad4cc0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ad4bf8 bytes d2180494
+ 00ad4cc0 bytes cc180494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f0fa3e631ebd9569abdec0e0318eed6"></a>

### [`00ad5f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md) → [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) FUN_00ad6034

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ad5df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5df8.md) [`00ad5f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md) · 呼出先 2件 [`00ad5f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`00ad5ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec0.md) [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) · 呼出先 2件 [`00ad6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad5f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md#insn-00ad5f88) · [`00ad5f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md#insn-00ad5f94) · [`00ad5fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5f6c.md#insn-00ad5fc8)
- 新版 [`00ad6050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad6050) · [`00ad605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad605c) · [`00ad6090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6034.md#insn-00ad6090)

~~~diff
- 00ad5f88 ["INT_ADD", "register:40f0:8", ["const:ad5f88:8", "const:4:8"]]
- 00ad5f88 ["CALL", null, ["local:b0:8"]]
+ 00ad6050 ["INT_ADD", "register:40f0:8", ["const:ad6050:8", "const:4:8"]]
+ 00ad6050 ["CALL", null, ["local:b0:8"]]
- 00ad5f88 bytes f9ffff97
+ 00ad6050 bytes f9ffff97
- 00ad5f94 ["INT_ADD", "register:40f0:8", ["const:ad5f94:8", "const:4:8"]]
- 00ad5f94 ["CALL", null, ["local:b0:8"]]
+ 00ad605c ["INT_ADD", "register:40f0:8", ["const:ad605c:8", "const:4:8"]]
+ 00ad605c ["CALL", null, ["local:b0:8"]]
- 00ad5f94 bytes f6ffff97
+ 00ad605c bytes f6ffff97
- 00ad5fc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad5fc8 ["INT_ADD", "register:40f0:8", ["const:ad5fc8:8", "const:4:8"]]
- 00ad5fc8 ["CALLIND", null, ["register:0:8"]]
+ 00ad6090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad6090 ["INT_ADD", "register:40f0:8", ["const:ad6090:8", "const:4:8"]]
+ 00ad6090 ["CALLIND", null, ["register:0:8"]]
- 00ad5fc8 bytes 00013fd6
+ 00ad6090 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40db739cb828f53faf30fd3a9ce134aa"></a>

### [`00ad5fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5fec.md) → [`00ad60b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md) FUN_00ad60b4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ad5e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5e00.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00ad5ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad5ec8.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad6070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5fec.md#insn-00ad6070) · [`00ad609c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad5/00ad5fec.md#insn-00ad609c)
- 新版 [`00ad6138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md#insn-00ad6138) · [`00ad6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad60b4.md#insn-00ad6164)

~~~diff
- 00ad6070 ["INT_ADD", "register:40f0:8", ["const:ad6070:8", "const:4:8"]]
- 00ad6070 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ad6138 ["INT_ADD", "register:40f0:8", ["const:ad6138:8", "const:4:8"]]
+ 00ad6138 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ad6070 bytes 24140494
+ 00ad6138 bytes 1e140494
- 00ad609c ["INT_ADD", "register:40f0:8", ["const:ad609c:8", "const:4:8"]]
- 00ad609c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00ad6164 ["INT_ADD", "register:40f0:8", ["const:ad6164:8", "const:4:8"]]
+ 00ad6164 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00ad609c bytes 19140494
+ 00ad6164 bytes 13140494
~~~


<a id="compare-0a04ec533f402f6afaa063621c982874"></a>

### [`00ad611c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad611c.md) → [`00ad61e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md) FUN_00ad61e4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00acc23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc23c.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00acc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad613c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad611c.md#insn-00ad613c) · [`00ad6144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad611c.md#insn-00ad6144) · [`00ad6150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad6/00ad611c.md#insn-00ad6150)
- 新版 [`00ad6204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad6204) · [`00ad620c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad620c) · [`00ad6218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad61e4.md#insn-00ad6218)

~~~diff
- 00ad613c ["INT_ADD", "register:40f0:8", ["const:ad613c:8", "const:4:8"]]
- 00ad613c ["CALL", null, ["callee:00565f94:8"]]
+ 00ad6204 ["INT_ADD", "register:40f0:8", ["const:ad6204:8", "const:4:8"]]
+ 00ad6204 ["CALL", null, ["callee:00565f94:8"]]
- 00ad613c bytes 963fea97
+ 00ad6204 bytes 643fea97
- 00ad6144 ["INT_ADD", "register:40f0:8", ["const:ad6144:8", "const:4:8"]]
- 00ad6144 ["CALL", null, ["callee:00566284:8"]]
+ 00ad620c ["INT_ADD", "register:40f0:8", ["const:ad620c:8", "const:4:8"]]
+ 00ad620c ["CALL", null, ["callee:00566284:8"]]
- 00ad6144 bytes 5040ea97
+ 00ad620c bytes 1e40ea97
- 00ad6150 ["INT_ADD", "register:40f0:8", ["const:ad6150:8", "const:4:8"]]
- 00ad6150 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00ad6218 ["INT_ADD", "register:40f0:8", ["const:ad6218:8", "const:4:8"]]
+ 00ad6218 ["CALL", null, ["callee:00bdaff0:8"]]
- 00ad6150 bytes 7c130494
+ 00ad6218 bytes 76130494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff38baa77501b00934174f2f1ab6936"></a>

### [`00ad73ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad73ec.md) → [`00ad74b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md) FUN_00ad74b4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad8f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8f7c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00ad9044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad9/00ad9044.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad7428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad73ec.md#insn-00ad7428) · [`00ad7458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad73ec.md#insn-00ad7458) · [`00ad7488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad73ec.md#insn-00ad7488)
- 新版 [`00ad74f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad74f0) · [`00ad7520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad7520) · [`00ad7550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad74b4.md#insn-00ad7550)

~~~diff
- 00ad7428 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7428 ["INT_ADD", "register:40f0:8", ["const:ad7428:8", "const:4:8"]]
- 00ad7428 ["CALLIND", null, ["register:0:8"]]
+ 00ad74f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad74f0 ["INT_ADD", "register:40f0:8", ["const:ad74f0:8", "const:4:8"]]
+ 00ad74f0 ["CALLIND", null, ["register:0:8"]]
- 00ad7428 bytes 00013fd6
+ 00ad74f0 bytes 00013fd6
- 00ad7458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7458 ["INT_ADD", "register:40f0:8", ["const:ad7458:8", "const:4:8"]]
- 00ad7458 ["CALLIND", null, ["register:0:8"]]
+ 00ad7520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad7520 ["INT_ADD", "register:40f0:8", ["const:ad7520:8", "const:4:8"]]
+ 00ad7520 ["CALLIND", null, ["register:0:8"]]
- 00ad7458 bytes 00013fd6
+ 00ad7520 bytes 00013fd6
- 00ad7488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad7488 ["INT_ADD", "register:40f0:8", ["const:ad7488:8", "const:4:8"]]
- 00ad7488 ["CALLIND", null, ["register:0:8"]]
+ 00ad7550 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad7550 ["INT_ADD", "register:40f0:8", ["const:ad7550:8", "const:4:8"]]
+ 00ad7550 ["CALLIND", null, ["register:0:8"]]
- 00ad7488 bytes 00013fd6
+ 00ad7550 bytes 00013fd6
~~~


<a id="compare-bd0038f028ea46ba620ffdaf264ed8d5"></a>

### [`00ad78a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad78a8.md) → [`00ad7970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md) FUN_00ad7970

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008547f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008547f8.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`008547f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008547f8.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad78cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad78a8.md#insn-00ad78cc) · [`00ad78d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad78a8.md#insn-00ad78d4) · [`00ad7924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad78a8.md#insn-00ad7924)
- 新版 [`00ad7994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad7994) · [`00ad799c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad799c) · [`00ad79ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7970.md#insn-00ad79ec)

~~~diff
- 00ad78cc ["INT_ADD", "register:40f0:8", ["const:ad78cc:8", "const:4:8"]]
- 00ad78cc ["CALL", null, ["callee:00565f94:8"]]
+ 00ad7994 ["INT_ADD", "register:40f0:8", ["const:ad7994:8", "const:4:8"]]
+ 00ad7994 ["CALL", null, ["callee:00565f94:8"]]
- 00ad78cc bytes b239ea97
+ 00ad7994 bytes 8039ea97
- 00ad78d4 ["INT_ADD", "register:40f0:8", ["const:ad78d4:8", "const:4:8"]]
- 00ad78d4 ["CALL", null, ["callee:00566284:8"]]
+ 00ad799c ["INT_ADD", "register:40f0:8", ["const:ad799c:8", "const:4:8"]]
+ 00ad799c ["CALL", null, ["callee:00566284:8"]]
- 00ad78d4 bytes 6c3aea97
+ 00ad799c bytes 3a3aea97
- 00ad7924 ["INT_ADD", "register:40f0:8", ["const:ad7924:8", "const:4:8"]]
- 00ad7924 ["CALL", null, ["callee:00566448:8"]]
+ 00ad79ec ["INT_ADD", "register:40f0:8", ["const:ad79ec:8", "const:4:8"]]
+ 00ad79ec ["CALL", null, ["callee:00566448:8"]]
- 00ad7924 bytes c93aea97
+ 00ad79ec bytes 973aea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78be830eef0f26937a0baf196485af14"></a>

### [`00ad8390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8390.md) → [`00ad8458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md) FUN_00ad8458

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad7ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad7ebc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00ad7f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ad83d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8390.md#insn-00ad83d8) · [`00ad8418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8390.md#insn-00ad8418) · [`00ad8450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad8390.md#insn-00ad8450)
- 新版 [`00ad84a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad84a0) · [`00ad84e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad84e0) · [`00ad8518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8458.md#insn-00ad8518)

~~~diff
- 00ad83d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad83d8 ["INT_ADD", "register:40f0:8", ["const:ad83d8:8", "const:4:8"]]
- 00ad83d8 ["CALLIND", null, ["register:0:8"]]
+ 00ad84a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad84a0 ["INT_ADD", "register:40f0:8", ["const:ad84a0:8", "const:4:8"]]
+ 00ad84a0 ["CALLIND", null, ["register:0:8"]]
- 00ad83d8 bytes 00013fd6
+ 00ad84a0 bytes 00013fd6
- 00ad8418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad8418 ["INT_ADD", "register:40f0:8", ["const:ad8418:8", "const:4:8"]]
- 00ad8418 ["CALLIND", null, ["register:0:8"]]
+ 00ad84e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad84e0 ["INT_ADD", "register:40f0:8", ["const:ad84e0:8", "const:4:8"]]
+ 00ad84e0 ["CALLIND", null, ["register:0:8"]]
- 00ad8418 bytes 00013fd6
+ 00ad84e0 bytes 00013fd6
- 00ad8450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ad8450 ["INT_ADD", "register:40f0:8", ["const:ad8450:8", "const:4:8"]]
- 00ad8450 ["CALLIND", null, ["register:0:8"]]
+ 00ad8518 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ad8518 ["INT_ADD", "register:40f0:8", ["const:ad8518:8", "const:4:8"]]
+ 00ad8518 ["CALLIND", null, ["register:0:8"]]
- 00ad8450 bytes 00013fd6
+ 00ad8518 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5f8c62e0a3fda31c9fe24e4cb57929"></a>

### [`00adb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb700.md) → [`00adb7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md) FUN_00adb7c8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adb75c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb700.md#insn-00adb75c) · [`00adb788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb700.md#insn-00adb788) · [`00adb798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb700.md#insn-00adb798)
- 新版 [`00adb824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb824) · [`00adb850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb850) · [`00adb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb7c8.md#insn-00adb860)

~~~diff
- 00adb75c ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb75c ["INT_ADD", "register:40f0:8", ["const:adb75c:8", "const:4:8"]]
- 00adb75c ["CALLIND", null, ["register:0:8"]]
+ 00adb824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb824 ["INT_ADD", "register:40f0:8", ["const:adb824:8", "const:4:8"]]
+ 00adb824 ["CALLIND", null, ["register:0:8"]]
- 00adb75c bytes 00013fd6
+ 00adb824 bytes 00013fd6
- 00adb788 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb788 ["INT_ADD", "register:40f0:8", ["const:adb788:8", "const:4:8"]]
- 00adb788 ["CALLIND", null, ["register:0:8"]]
+ 00adb850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00adb850 ["INT_ADD", "register:40f0:8", ["const:adb850:8", "const:4:8"]]
+ 00adb850 ["CALLIND", null, ["register:0:8"]]
- 00adb788 bytes 00013fd6
+ 00adb850 bytes 00013fd6
- 00adb798 ["INT_ADD", "register:40f0:8", ["const:adb798:8", "const:4:8"]]
- 00adb798 ["CALL", null, ["callee:00bdb010:8"]]
+ 00adb860 ["INT_ADD", "register:40f0:8", ["const:adb860:8", "const:4:8"]]
+ 00adb860 ["CALL", null, ["callee:00bdb010:8"]]
- 00adb798 bytes f2fd0394
+ 00adb860 bytes ecfd0394
~~~


<a id="compare-cb026748c717b7d4b7c278bc455b7ff9"></a>

### [`00adba18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adba18.md) → [`00adbae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md) FUN_00adbae0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00adae8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adae8c.md) [`00adaf4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adaf4c.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 2件 [`00adaf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md) [`00adb014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb014.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adba84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adba18.md#insn-00adba84) · [`00adbae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adba18.md#insn-00adbae0)
- 新版 [`00adbb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md#insn-00adbb4c) · [`00adbba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbae0.md#insn-00adbba8)

~~~diff
- 00adba84 ["INT_ADD", "register:40f0:8", ["const:adba84:8", "const:4:8"]]
- 00adba84 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00adbb4c ["INT_ADD", "register:40f0:8", ["const:adbb4c:8", "const:4:8"]]
+ 00adbb4c ["CALL", null, ["callee:00bdb1b0:8"]]
- 00adba84 bytes 9ffd0394
+ 00adbb4c bytes 99fd0394
- 00adbae0 ["INT_ADD", "register:40f0:8", ["const:adbae0:8", "const:4:8"]]
- 00adbae0 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00adbba8 ["INT_ADD", "register:40f0:8", ["const:adbba8:8", "const:4:8"]]
+ 00adbba8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00adbae0 bytes 88fd0394
+ 00adbba8 bytes 82fd0394
~~~


<a id="compare-454b4bfbdcf094d295b171bf0cb99296"></a>

### [`00adbf5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf5c.md) → [`00adc024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc024.md) FUN_00adc024

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) [`00814828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00814/00814828.md) · 呼出先 1件 [`005c3468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c3/005c3468.md)
- 新版 呼出元 2件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`00814828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00814/00814828.md) · 呼出先 1件 [`005c3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c3/005c3468.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adbf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbf5c.md#insn-00adbf70)
- 新版 [`00adc038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc024.md#insn-00adc038)

~~~diff
- 00adbf70 ["INT_ADD", "register:40f0:8", ["const:adbf70:8", "const:4:8"]]
- 00adbf70 ["CALL", null, ["callee:005c3468:8"]]
+ 00adc038 ["INT_ADD", "register:40f0:8", ["const:adc038:8", "const:4:8"]]
+ 00adc038 ["CALL", null, ["callee:005c3468:8"]]
- 00adbf70 bytes 3e9deb97
+ 00adc038 bytes 0c9deb97
~~~


<a id="compare-117d7a2cdd82f4660df2c11e7721be6f"></a>

### [`00adff64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adff64.md) → [`00ae002c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md) FUN_00ae002c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae04a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae04a0.md) · 呼出先 2件 [`00bdda10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda10.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md)
- 新版 呼出元 1件 [`00ae0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md) · 呼出先 2件 [`00bddac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddac0.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adff74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adff64.md#insn-00adff74) · [`00adff84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adff64.md#insn-00adff84)
- 新版 [`00ae003c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md#insn-00ae003c) · [`00ae004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae002c.md#insn-00ae004c)

~~~diff
- 00adff74 ["INT_ADD", "register:40f0:8", ["const:adff74:8", "const:4:8"]]
- 00adff74 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00ae003c ["INT_ADD", "register:40f0:8", ["const:ae003c:8", "const:4:8"]]
+ 00ae003c ["CALL", null, ["callee:00bdddb0:8"]]
- 00adff74 bytes 63f70394
+ 00ae003c bytes 5df70394
- 00adff84 ["INT_ADD", "register:40f0:8", ["const:adff84:8", "const:4:8"]]
- 00adff84 ["CALL", null, ["callee:00bddac0:8"]]
+ 00ae004c ["INT_ADD", "register:40f0:8", ["const:ae004c:8", "const:4:8"]]
+ 00ae004c ["CALL", null, ["callee:00bddac0:8"]]
- 00adff84 bytes a3f60394
+ 00ae004c bytes 9df60394
~~~


<a id="compare-b10c5d50f8a2a795c46b7d24d6887232"></a>

### [`00adff98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adff98.md) → [`00ae0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0060.md) FUN_00ae0060

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00ae04a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae04a0.md) · 呼出先 2件 [`00bdd9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9f0.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md)
- 新版 呼出元 1件 [`00ae0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0568.md) · 呼出先 2件 [`00bddaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adffa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adff98.md#insn-00adffa8)
- 新版 [`00ae0070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0060.md#insn-00ae0070)

~~~diff
- 00adffa8 ["INT_ADD", "register:40f0:8", ["const:adffa8:8", "const:4:8"]]
- 00adffa8 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00ae0070 ["INT_ADD", "register:40f0:8", ["const:ae0070:8", "const:4:8"]]
+ 00ae0070 ["CALL", null, ["callee:00bdddb0:8"]]
- 00adffa8 bytes 56f70394
+ 00ae0070 bytes 50f70394
~~~


<a id="compare-f17094262225e71132feed3c0849c668"></a>

### [`00ae0434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0434.md) → [`00ae04fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md) _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdddd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddd0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdddd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddd0.md)
- 新版 呼出元 1件 [`00bdde80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0434.md#insn-00ae0450) · [`00ae045c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae0434.md#insn-00ae045c)
- 新版 [`00ae0518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md#insn-00ae0518) · [`00ae0524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae04fc.md#insn-00ae0524)

~~~diff
- 00ae0450 ["INT_ADD", "register:40f0:8", ["const:ae0450:8", "const:4:8"]]
- 00ae0450 ["CALL", null, ["callee:00bdde80:8"]]
+ 00ae0518 ["INT_ADD", "register:40f0:8", ["const:ae0518:8", "const:4:8"]]
+ 00ae0518 ["CALL", null, ["callee:00bdde80:8"]]
- 00ae0450 bytes 60f60394
+ 00ae0518 bytes 5af60394
- 00ae045c ["INT_ADD", "register:40f0:8", ["const:ae045c:8", "const:4:8"]]
- 00ae045c ["CALL", null, ["callee:00bdde80:8"]]
+ 00ae0524 ["INT_ADD", "register:40f0:8", ["const:ae0524:8", "const:4:8"]]
+ 00ae0524 ["CALL", null, ["callee:00bdde80:8"]]
- 00ae045c bytes 5df60394
+ 00ae0524 bytes 57f60394
~~~


<a id="compare-d00287655f42c45c546b95acbc5f78a1"></a>

### [`00ae35cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae35cc.md) → [`00ae3694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md)
- 新版 呼出元 1件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) · 呼出先 2件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae35cc.md#insn-00ae3640) · [`00ae3674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae35cc.md#insn-00ae3674)
- 新版 [`00ae3708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md#insn-00ae3708) · [`00ae373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3694.md#insn-00ae373c)

~~~diff
- 00ae3640 ["INT_ADD", "register:40f0:8", ["const:ae3640:8", "const:4:8"]]
- 00ae3640 ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00ae3708 ["INT_ADD", "register:40f0:8", ["const:ae3708:8", "const:4:8"]]
+ 00ae3708 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00ae3640 bytes 6cde0394
+ 00ae3708 bytes 66de0394
- 00ae3674 ["INT_ADD", "register:40f0:8", ["const:ae3674:8", "const:4:8"]]
- 00ae3674 ["CALL", null, ["callee:00bde1d0:8"]]
+ 00ae373c ["INT_ADD", "register:40f0:8", ["const:ae373c:8", "const:4:8"]]
+ 00ae373c ["CALL", null, ["callee:00bde1d0:8"]]
- 00ae3674 bytes abea0394
+ 00ae373c bytes a5ea0394
~~~


<a id="compare-3a7e6e37465503613f0c48681dfa939f"></a>

### [`00ae3d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d00.md) → [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00ae2b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md) [`00b4dd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md) [`00b6ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 3件 [`00ae2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md) [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d00.md#insn-00ae3d20)
- 新版 [`00ae3de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md#insn-00ae3de8)

~~~diff
- 00ae3d20 ["INT_ADD", "register:40f0:8", ["const:ae3d20:8", "const:4:8"]]
- 00ae3d20 ["CALL", null, ["callee:00bdb010:8"]]
+ 00ae3de8 ["INT_ADD", "register:40f0:8", ["const:ae3de8:8", "const:4:8"]]
+ 00ae3de8 ["CALL", null, ["callee:00bdb010:8"]]
- 00ae3d20 bytes 90dc0394
+ 00ae3de8 bytes 8adc0394
~~~


<a id="compare-62106e33ceefb696915ad5412e5edfa1"></a>

### [`00af3094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3094.md) → [`00af315c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af315c.md) _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md) · 呼出先 1件 [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md)
- 新版 呼出元 1件 [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md) · 呼出先 1件 [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af30a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3094.md#insn-00af30a8)
- 新版 [`00af3170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af315c.md#insn-00af3170)

~~~diff
- 00af30a8 ["INT_ADD", "register:40f0:8", ["const:af30a8:8", "const:4:8"]]
- 00af30a8 ["CALL", null, ["callee:00bde050:8"]]
+ 00af3170 ["INT_ADD", "register:40f0:8", ["const:af3170:8", "const:4:8"]]
+ 00af3170 ["CALL", null, ["callee:00bde050:8"]]
- 00af30a8 bytes beab0394
+ 00af3170 bytes b8ab0394
~~~


<a id="compare-26704d73aa74bf097e0ac1aa66e42cfa"></a>

### [`00af3388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3388.md) → [`00af3450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc50.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af33e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3388.md#insn-00af33e4) · [`00af345c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3388.md#insn-00af345c) · [`00af3494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3388.md#insn-00af3494)
- 新版 [`00af34ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af34ac) · [`00af3524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af3524) · [`00af355c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3450.md#insn-00af355c)

~~~diff
- 00af33e4 ["INT_ADD", "register:40f0:8", ["const:af33e4:8", "const:4:8"]]
- 00af33e4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af34ac ["INT_ADD", "register:40f0:8", ["const:af34ac:8", "const:4:8"]]
+ 00af34ac ["CALL", null, ["callee:00bdaff0:8"]]
- 00af33e4 bytes d79e0394
+ 00af34ac bytes d19e0394
- 00af345c ["INT_ADD", "register:40f0:8", ["const:af345c:8", "const:4:8"]]
- 00af345c ["CALL", null, ["callee:00bdb010:8"]]
+ 00af3524 ["INT_ADD", "register:40f0:8", ["const:af3524:8", "const:4:8"]]
+ 00af3524 ["CALL", null, ["callee:00bdb010:8"]]
- 00af345c bytes c19e0394
+ 00af3524 bytes bb9e0394
- 00af3494 ["INT_ADD", "register:40f0:8", ["const:af3494:8", "const:4:8"]]
- 00af3494 ["CALL", null, ["callee:00bde270:8"]]
+ 00af355c ["INT_ADD", "register:40f0:8", ["const:af355c:8", "const:4:8"]]
+ 00af355c ["CALL", null, ["callee:00bde270:8"]]
- 00af3494 bytes 4bab0394
+ 00af355c bytes 45ab0394
~~~


<a id="compare-4412879e02c3288da0ac18ff0971d7d8"></a>

### [`00af3958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3958.md) → [`00af3a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6b0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af39b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3958.md#insn-00af39b8) · [`00af39f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3958.md#insn-00af39f8) · [`00af3a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3958.md#insn-00af3a34)
- 新版 [`00af3a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3a80) · [`00af3ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3ac0) · [`00af3afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md#insn-00af3afc)

~~~diff
- 00af39b8 ["INT_ADD", "register:40f0:8", ["const:af39b8:8", "const:4:8"]]
- 00af39b8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af3a80 ["INT_ADD", "register:40f0:8", ["const:af3a80:8", "const:4:8"]]
+ 00af3a80 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af39b8 bytes 629d0394
+ 00af3a80 bytes 5c9d0394
- 00af39f8 ["INT_ADD", "register:40f0:8", ["const:af39f8:8", "const:4:8"]]
- 00af39f8 ["CALL", null, ["callee:00bdd9a0:8"]]
+ 00af3ac0 ["INT_ADD", "register:40f0:8", ["const:af3ac0:8", "const:4:8"]]
+ 00af3ac0 ["CALL", null, ["callee:00bdd9a0:8"]]
- 00af39f8 bytes bea70394
+ 00af3ac0 bytes b8a70394
- 00af3a34 ["INT_ADD", "register:40f0:8", ["const:af3a34:8", "const:4:8"]]
- 00af3a34 ["CALL", null, ["callee:00bdd990:8"]]
+ 00af3afc ["INT_ADD", "register:40f0:8", ["const:af3afc:8", "const:4:8"]]
+ 00af3afc ["CALL", null, ["callee:00bdd990:8"]]
- 00af3a34 bytes aba70394
+ 00af3afc bytes a5a70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da3c7214c964913c60dad6d19a62ca6"></a>

### [`00af3a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3a74.md) → [`00af3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3a74.md#insn-00af3a98) · [`00af3acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3a74.md#insn-00af3acc) · [`00af3aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3a74.md#insn-00af3aec)
- 新版 [`00af3b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3b60) · [`00af3b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3b94) · [`00af3bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md#insn-00af3bb4)

~~~diff
- 00af3a98 ["INT_ADD", "register:40f0:8", ["const:af3a98:8", "const:4:8"]]
- 00af3a98 ["CALL", null, ["callee:00bdb140:8"]]
+ 00af3b60 ["INT_ADD", "register:40f0:8", ["const:af3b60:8", "const:4:8"]]
+ 00af3b60 ["CALL", null, ["callee:00bdb140:8"]]
- 00af3a98 bytes 7e9d0394
+ 00af3b60 bytes 789d0394
- 00af3acc ["INT_ADD", "register:40f0:8", ["const:af3acc:8", "const:4:8"]]
- 00af3acc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af3b94 ["INT_ADD", "register:40f0:8", ["const:af3b94:8", "const:4:8"]]
+ 00af3b94 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af3acc bytes 1d9d0394
+ 00af3b94 bytes 179d0394
- 00af3aec ["INT_ADD", "register:40f0:8", ["const:af3aec:8", "const:4:8"]]
- 00af3aec ["CALL", null, ["callee:00bdb160:8"]]
+ 00af3bb4 ["INT_ADD", "register:40f0:8", ["const:af3bb4:8", "const:4:8"]]
+ 00af3bb4 ["CALL", null, ["callee:00bdb160:8"]]
- 00af3aec bytes 719d0394
+ 00af3bb4 bytes 6b9d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c23c7a90207cb8f396185786f8cb3d"></a>

### [`00af3d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3d24.md) → [`00af3dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md) _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde280.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde330.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3d24.md#insn-00af3d98) · [`00af3dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3d24.md#insn-00af3dbc)
- 新版 [`00af3e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md#insn-00af3e60) · [`00af3e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3dec.md#insn-00af3e84)

~~~diff
- 00af3d98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3d98 ["INT_ADD", "register:40f0:8", ["const:af3d98:8", "const:4:8"]]
- 00af3d98 ["CALLIND", null, ["register:0:8"]]
+ 00af3e60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af3e60 ["INT_ADD", "register:40f0:8", ["const:af3e60:8", "const:4:8"]]
+ 00af3e60 ["CALLIND", null, ["register:0:8"]]
- 00af3d98 bytes 00013fd6
+ 00af3e60 bytes 00013fd6
- 00af3dbc ["INT_ADD", "register:40f0:8", ["const:af3dbc:8", "const:4:8"]]
- 00af3dbc ["CALL", null, ["callee:00bdb040:8"]]
+ 00af3e84 ["INT_ADD", "register:40f0:8", ["const:af3e84:8", "const:4:8"]]
+ 00af3e84 ["CALL", null, ["callee:00bdb040:8"]]
- 00af3dbc bytes 759c0394
+ 00af3e84 bytes 6f9c0394
~~~


<a id="compare-f5492e98d540afc771dd8b49418e58ce"></a>

### [`00af3e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3e28.md) → [`00af3ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md) _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde290.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde340.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3e28.md#insn-00af3e9c) · [`00af3ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3e28.md#insn-00af3ec0)
- 新版 [`00af3f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md#insn-00af3f64) · [`00af3f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ef0.md#insn-00af3f88)

~~~diff
- 00af3e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3e9c ["INT_ADD", "register:40f0:8", ["const:af3e9c:8", "const:4:8"]]
- 00af3e9c ["CALLIND", null, ["register:0:8"]]
+ 00af3f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af3f64 ["INT_ADD", "register:40f0:8", ["const:af3f64:8", "const:4:8"]]
+ 00af3f64 ["CALLIND", null, ["register:0:8"]]
- 00af3e9c bytes 00013fd6
+ 00af3f64 bytes 00013fd6
- 00af3ec0 ["INT_ADD", "register:40f0:8", ["const:af3ec0:8", "const:4:8"]]
- 00af3ec0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af3f88 ["INT_ADD", "register:40f0:8", ["const:af3f88:8", "const:4:8"]]
+ 00af3f88 ["CALL", null, ["callee:00bdb040:8"]]
- 00af3ec0 bytes 349c0394
+ 00af3f88 bytes 2e9c0394
~~~


<a id="compare-66f500f2d99197ed14bc768b618bb4de"></a>

### [`00af3f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3f2c.md) → [`00af3ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md) _ZN7_JNIEnv15CallShortMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2a0.md) · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde350.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3f2c.md#insn-00af3fa0) · [`00af3fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3f2c.md#insn-00af3fc4)
- 新版 [`00af4068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md#insn-00af4068) · [`00af408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3ff4.md#insn-00af408c)

~~~diff
- 00af3fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af3fa0 ["INT_ADD", "register:40f0:8", ["const:af3fa0:8", "const:4:8"]]
- 00af3fa0 ["CALLIND", null, ["register:0:8"]]
+ 00af4068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4068 ["INT_ADD", "register:40f0:8", ["const:af4068:8", "const:4:8"]]
+ 00af4068 ["CALLIND", null, ["register:0:8"]]
- 00af3fa0 bytes 00013fd6
+ 00af4068 bytes 00013fd6
- 00af3fc4 ["INT_ADD", "register:40f0:8", ["const:af3fc4:8", "const:4:8"]]
- 00af3fc4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00af408c ["INT_ADD", "register:40f0:8", ["const:af408c:8", "const:4:8"]]
+ 00af408c ["CALL", null, ["callee:00bdb040:8"]]
- 00af3fc4 bytes f39b0394
+ 00af408c bytes ed9b0394
~~~


<a id="compare-f35c47e1861e6a519f43de637a0c867c"></a>

### [`00af45d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af45d4.md) → [`00af469c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md) _ZN8firebase4util22JBooleanArrayToVariantEP7_JNIEnvP14_jbooleanArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde530.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5e0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af45d4.md#insn-00af4614) · [`00af4630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af45d4.md#insn-00af4630) · [`00af463c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af45d4.md#insn-00af463c)
- 新版 [`00af46dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af46dc) · [`00af46f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af46f8) · [`00af4704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af469c.md#insn-00af4704)

~~~diff
- 00af4614 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4614 ["INT_ADD", "register:40f0:8", ["const:af4614:8", "const:4:8"]]
- 00af4614 ["CALLIND", null, ["register:0:8"]]
+ 00af46dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af46dc ["INT_ADD", "register:40f0:8", ["const:af46dc:8", "const:4:8"]]
+ 00af46dc ["CALLIND", null, ["register:0:8"]]
- 00af4614 bytes 20013fd6
+ 00af46dc bytes 20013fd6
- 00af4630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4630 ["INT_ADD", "register:40f0:8", ["const:af4630:8", "const:4:8"]]
- 00af4630 ["CALLIND", null, ["register:0:8"]]
+ 00af46f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af46f8 ["INT_ADD", "register:40f0:8", ["const:af46f8:8", "const:4:8"]]
+ 00af46f8 ["CALLIND", null, ["register:0:8"]]
- 00af4630 bytes 00013fd6
+ 00af46f8 bytes 00013fd6
- 00af463c ["INT_ADD", "register:40f0:8", ["const:af463c:8", "const:4:8"]]
- 00af463c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af4704 ["INT_ADD", "register:40f0:8", ["const:af4704:8", "const:4:8"]]
+ 00af4704 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af463c bytes 419a0394
+ 00af4704 bytes 3b9a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca44220ed3619915b52d1b5fb213b3e"></a>

### [`00af4758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4758.md) → [`00af4820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md) _ZN8firebase4util19JByteArrayToVariantEP7_JNIEnvP11_jbyteArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde450.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde500.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4758.md#insn-00af4798) · [`00af47b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4758.md#insn-00af47b4) · [`00af47c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4758.md#insn-00af47c0)
- 新版 [`00af4860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af4860) · [`00af487c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af487c) · [`00af4888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4820.md#insn-00af4888)

~~~diff
- 00af4798 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4798 ["INT_ADD", "register:40f0:8", ["const:af4798:8", "const:4:8"]]
- 00af4798 ["CALLIND", null, ["register:0:8"]]
+ 00af4860 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4860 ["INT_ADD", "register:40f0:8", ["const:af4860:8", "const:4:8"]]
+ 00af4860 ["CALLIND", null, ["register:0:8"]]
- 00af4798 bytes 20013fd6
+ 00af4860 bytes 20013fd6
- 00af47b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af47b4 ["INT_ADD", "register:40f0:8", ["const:af47b4:8", "const:4:8"]]
- 00af47b4 ["CALLIND", null, ["register:0:8"]]
+ 00af487c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af487c ["INT_ADD", "register:40f0:8", ["const:af487c:8", "const:4:8"]]
+ 00af487c ["CALLIND", null, ["register:0:8"]]
- 00af47b4 bytes 00013fd6
+ 00af487c bytes 00013fd6
- 00af47c0 ["INT_ADD", "register:40f0:8", ["const:af47c0:8", "const:4:8"]]
- 00af47c0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af4888 ["INT_ADD", "register:40f0:8", ["const:af4888:8", "const:4:8"]]
+ 00af4888 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af47c0 bytes e0990394
+ 00af4888 bytes da990394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f1fbfbea977d7abeb8c5e81afa41e01"></a>

### [`00af4bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4bd0.md) → [`00af4c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md) _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde430.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4e0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4bd0.md#insn-00af4c10) · [`00af4c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4bd0.md#insn-00af4c2c) · [`00af4c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4bd0.md#insn-00af4c38)
- 新版 [`00af4cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4cd8) · [`00af4cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4cf4) · [`00af4d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md#insn-00af4d00)

~~~diff
- 00af4c10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4c10 ["INT_ADD", "register:40f0:8", ["const:af4c10:8", "const:4:8"]]
- 00af4c10 ["CALLIND", null, ["register:0:8"]]
+ 00af4cd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4cd8 ["INT_ADD", "register:40f0:8", ["const:af4cd8:8", "const:4:8"]]
+ 00af4cd8 ["CALLIND", null, ["register:0:8"]]
- 00af4c10 bytes 20013fd6
+ 00af4cd8 bytes 20013fd6
- 00af4c2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4c2c ["INT_ADD", "register:40f0:8", ["const:af4c2c:8", "const:4:8"]]
- 00af4c2c ["CALLIND", null, ["register:0:8"]]
+ 00af4cf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4cf4 ["INT_ADD", "register:40f0:8", ["const:af4cf4:8", "const:4:8"]]
+ 00af4cf4 ["CALLIND", null, ["register:0:8"]]
- 00af4c2c bytes 00013fd6
+ 00af4cf4 bytes 00013fd6
- 00af4c38 ["INT_ADD", "register:40f0:8", ["const:af4c38:8", "const:4:8"]]
- 00af4c38 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af4d00 ["INT_ADD", "register:40f0:8", ["const:af4d00:8", "const:4:8"]]
+ 00af4d00 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af4c38 bytes c2980394
+ 00af4d00 bytes bc980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08b2838336e06253a9e02e846db2cd60"></a>

### [`00af5050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5050.md) → [`00af5118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md) _ZN8firebase4util21JDoubleArrayToVariantEP7_JNIEnvP13_jdoubleArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde500.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5b0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af5090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5050.md#insn-00af5090) · [`00af50ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5050.md#insn-00af50ac) · [`00af50b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5050.md#insn-00af50b8)
- 新版 [`00af5158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5158) · [`00af5174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5174) · [`00af5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5118.md#insn-00af5180)

~~~diff
- 00af5090 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af5090 ["INT_ADD", "register:40f0:8", ["const:af5090:8", "const:4:8"]]
- 00af5090 ["CALLIND", null, ["register:0:8"]]
+ 00af5158 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af5158 ["INT_ADD", "register:40f0:8", ["const:af5158:8", "const:4:8"]]
+ 00af5158 ["CALLIND", null, ["register:0:8"]]
- 00af5090 bytes 20013fd6
+ 00af5158 bytes 20013fd6
- 00af50ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00af50ac ["INT_ADD", "register:40f0:8", ["const:af50ac:8", "const:4:8"]]
- 00af50ac ["CALLIND", null, ["register:0:8"]]
+ 00af5174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af5174 ["INT_ADD", "register:40f0:8", ["const:af5174:8", "const:4:8"]]
+ 00af5174 ["CALLIND", null, ["register:0:8"]]
- 00af50ac bytes 00013fd6
+ 00af5174 bytes 00013fd6
- 00af50b8 ["INT_ADD", "register:40f0:8", ["const:af50b8:8", "const:4:8"]]
- 00af50b8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af5180 ["INT_ADD", "register:40f0:8", ["const:af5180:8", "const:4:8"]]
+ 00af5180 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af50b8 bytes a2970394
+ 00af5180 bytes 9c970394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cfc427ccf2a346191ec028f271fece7"></a>

### [`00af51cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af51cc.md) → [`00af5294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md) _ZN8firebase4util21JObjectArrayToVariantEP7_JNIEnvP13_jobjectArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde510.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde490.md)
- 新版 呼出元 1件 [`00bde5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5c0.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde540.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af520c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af51cc.md#insn-00af520c) · [`00af521c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af51cc.md#insn-00af521c) · [`00af5230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af51cc.md#insn-00af5230)
- 新版 [`00af52d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52d4) · [`00af52e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52e4) · [`00af52f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md#insn-00af52f8)

~~~diff
- 00af520c ["COPY", "register:0:8", ["register:4048:8"]]
- 00af520c ["INT_ADD", "register:40f0:8", ["const:af520c:8", "const:4:8"]]
- 00af520c ["CALLIND", null, ["register:0:8"]]
+ 00af52d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af52d4 ["INT_ADD", "register:40f0:8", ["const:af52d4:8", "const:4:8"]]
+ 00af52d4 ["CALLIND", null, ["register:0:8"]]
- 00af520c bytes 20013fd6
+ 00af52d4 bytes 20013fd6
- 00af521c ["INT_ADD", "register:40f0:8", ["const:af521c:8", "const:4:8"]]
- 00af521c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af52e4 ["INT_ADD", "register:40f0:8", ["const:af52e4:8", "const:4:8"]]
+ 00af52e4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af521c bytes 49970394
+ 00af52e4 bytes 43970394
- 00af5230 ["INT_ADD", "register:40f0:8", ["const:af5230:8", "const:4:8"]]
- 00af5230 ["CALL", null, ["callee:00bde760:8"]]
+ 00af52f8 ["INT_ADD", "register:40f0:8", ["const:af52f8:8", "const:4:8"]]
+ 00af52f8 ["CALL", null, ["callee:00bde760:8"]]
- 00af5230 bytes 20a50394
+ 00af52f8 bytes 1aa50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb7869afcaecbbedeeb29a24be46218"></a>

### [`00af710c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af710c.md) → [`00af71d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md) _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddff0.md) · 呼出先 1件 [`00bddfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfd0.md)
- 新版 呼出元 1件 [`00bde0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0a0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af712c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af710c.md#insn-00af712c) · [`00af7144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af710c.md#insn-00af7144) · [`00af7154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af710c.md#insn-00af7154)
- 新版 [`00af71f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af71f4) · [`00af720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af720c) · [`00af721c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af71d4.md#insn-00af721c)

~~~diff
- 00af712c ["COPY", "register:0:8", ["register:4048:8"]]
- 00af712c ["INT_ADD", "register:40f0:8", ["const:af712c:8", "const:4:8"]]
- 00af712c ["CALLIND", null, ["register:0:8"]]
+ 00af71f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af71f4 ["INT_ADD", "register:40f0:8", ["const:af71f4:8", "const:4:8"]]
+ 00af71f4 ["CALLIND", null, ["register:0:8"]]
- 00af712c bytes 20013fd6
+ 00af71f4 bytes 20013fd6
- 00af7144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af7144 ["INT_ADD", "register:40f0:8", ["const:af7144:8", "const:4:8"]]
- 00af7144 ["CALLIND", null, ["register:0:8"]]
+ 00af720c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af720c ["INT_ADD", "register:40f0:8", ["const:af720c:8", "const:4:8"]]
+ 00af720c ["CALLIND", null, ["register:0:8"]]
- 00af7144 bytes 00013fd6
+ 00af720c bytes 00013fd6
- 00af7154 ["INT_ADD", "register:40f0:8", ["const:af7154:8", "const:4:8"]]
- 00af7154 ["CALL", null, ["callee:00bde080:8"]]
+ 00af721c ["INT_ADD", "register:40f0:8", ["const:af721c:8", "const:4:8"]]
+ 00af721c ["CALL", null, ["callee:00bde080:8"]]
- 00af7154 bytes 9f9b0394
+ 00af721c bytes 999b0394
~~~


<a id="compare-abe81ff6ca6abefe4998928ccd8638be"></a>

### [`00af772c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af772c.md) → [`00af77f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md) _ZN8firebase7Variant18set_mutable_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde600.md) · 呼出先 3件 [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9b0.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6b0.md) · 呼出先 3件 [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdda60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda60.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af7768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af772c.md#insn-00af7768) · [`00af778c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af772c.md#insn-00af778c) · [`00af779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af772c.md#insn-00af779c)
- 新版 [`00af7830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7830) · [`00af7854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7854) · [`00af7864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af77f4.md#insn-00af7864)

~~~diff
- 00af7768 ["INT_ADD", "register:40f0:8", ["const:af7768:8", "const:4:8"]]
- 00af7768 ["CALL", null, ["callee:00bdd990:8"]]
+ 00af7830 ["INT_ADD", "register:40f0:8", ["const:af7830:8", "const:4:8"]]
+ 00af7830 ["CALL", null, ["callee:00bdd990:8"]]
- 00af7768 bytes 5e980394
+ 00af7830 bytes 58980394
- 00af778c ["INT_ADD", "register:40f0:8", ["const:af778c:8", "const:4:8"]]
- 00af778c ["CALL", null, ["callee:00bdda60:8"]]
+ 00af7854 ["INT_ADD", "register:40f0:8", ["const:af7854:8", "const:4:8"]]
+ 00af7854 ["CALL", null, ["callee:00bdda60:8"]]
- 00af778c bytes 89980394
+ 00af7854 bytes 83980394
- 00af779c ["INT_ADD", "register:40f0:8", ["const:af779c:8", "const:4:8"]]
- 00af779c ["CALL", null, ["callee:00bdd990:8"]]
+ 00af7864 ["INT_ADD", "register:40f0:8", ["const:af7864:8", "const:4:8"]]
+ 00af7864 ["CALL", null, ["callee:00bdd990:8"]]
- 00af779c bytes 51980394
+ 00af7864 bytes 4b980394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abaacba89c7ffc90a4792f9bb2f84353"></a>

### [`00af7fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7fd8.md) → [`00af80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bde6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6e0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af8054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7fd8.md#insn-00af8054) · [`00af806c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7fd8.md#insn-00af806c) · [`00af8088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7fd8.md#insn-00af8088)
- 新版 [`00af811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af811c) · [`00af8134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af8134) · [`00af8150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af80a0.md#insn-00af8150)

~~~diff
- 00af8054 ["INT_ADD", "register:40f0:8", ["const:af8054:8", "const:4:8"]]
- 00af8054 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00af811c ["INT_ADD", "register:40f0:8", ["const:af811c:8", "const:4:8"]]
+ 00af811c ["CALL", null, ["callee:00bdb1f0:8"]]
- 00af8054 bytes 3b8c0394
+ 00af811c bytes 358c0394
- 00af806c ["INT_ADD", "register:40f0:8", ["const:af806c:8", "const:4:8"]]
- 00af806c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af8134 ["INT_ADD", "register:40f0:8", ["const:af8134:8", "const:4:8"]]
+ 00af8134 ["CALL", null, ["callee:00bdaff0:8"]]
- 00af806c bytes b58b0394
+ 00af8134 bytes af8b0394
- 00af8088 ["INT_ADD", "register:40f0:8", ["const:af8088:8", "const:4:8"]]
- 00af8088 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00af8150 ["INT_ADD", "register:40f0:8", ["const:af8150:8", "const:4:8"]]
+ 00af8150 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00af8088 bytes 2e8c0394
+ 00af8150 bytes 288c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe5e7ae60735b9f7063fb0a1f8c2f6c"></a>

### [`00afc700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc700.md) → [`00afc7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md) _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md)
- 新版 呼出元 1件 [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc700.md#insn-00afc720) · [`00afc7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc700.md#insn-00afc7d4) · [`00afc808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc700.md#insn-00afc808)
- 新版 [`00afc7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc7e8) · [`00afc89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc89c) · [`00afc8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc7c8.md#insn-00afc8d0)

~~~diff
- 00afc720 ["INT_ADD", "register:40f0:8", ["const:afc720:8", "const:4:8"]]
- 00afc720 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc7e8 ["INT_ADD", "register:40f0:8", ["const:afc7e8:8", "const:4:8"]]
+ 00afc7e8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc720 bytes 00850394
+ 00afc7e8 bytes fa840394
- 00afc7d4 ["INT_ADD", "register:40f0:8", ["const:afc7d4:8", "const:4:8"]]
- 00afc7d4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afc89c ["INT_ADD", "register:40f0:8", ["const:afc89c:8", "const:4:8"]]
+ 00afc89c ["CALL", null, ["callee:00bdaff0:8"]]
- 00afc7d4 bytes db790394
+ 00afc89c bytes d5790394
- 00afc808 ["INT_ADD", "register:40f0:8", ["const:afc808:8", "const:4:8"]]
- 00afc808 ["CALL", null, ["callee:00bde710:8"]]
+ 00afc8d0 ["INT_ADD", "register:40f0:8", ["const:afc8d0:8", "const:4:8"]]
+ 00afc8d0 ["CALL", null, ["callee:00bde710:8"]]
- 00afc808 bytes 96870394
+ 00afc8d0 bytes 90870394
~~~


<a id="compare-7f22461e76dd65576249a7a3138e0d46"></a>

### [`00afd508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd508.md) → [`00afd5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md) _ZNK8firebase4Path9GetParentEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd508.md#insn-00afd57c) · [`00afd5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd508.md#insn-00afd5b0) · [`00afd5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd508.md#insn-00afd5c0)
- 新版 [`00afd644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd644) · [`00afd678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd678) · [`00afd688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md#insn-00afd688)

~~~diff
- 00afd57c ["INT_ADD", "register:40f0:8", ["const:afd57c:8", "const:4:8"]]
- 00afd57c ["CALL", null, ["callee:00bde920:8"]]
+ 00afd644 ["INT_ADD", "register:40f0:8", ["const:afd644:8", "const:4:8"]]
+ 00afd644 ["CALL", null, ["callee:00bde920:8"]]
- 00afd57c bytes bd840394
+ 00afd644 bytes b7840394
- 00afd5b0 ["INT_ADD", "register:40f0:8", ["const:afd5b0:8", "const:4:8"]]
- 00afd5b0 ["CALL", null, ["callee:00bde1e0:8"]]
+ 00afd678 ["INT_ADD", "register:40f0:8", ["const:afd678:8", "const:4:8"]]
+ 00afd678 ["CALL", null, ["callee:00bde1e0:8"]]
- 00afd5b0 bytes e0820394
+ 00afd678 bytes da820394
- 00afd5c0 ["INT_ADD", "register:40f0:8", ["const:afd5c0:8", "const:4:8"]]
- 00afd5c0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00afd688 ["INT_ADD", "register:40f0:8", ["const:afd688:8", "const:4:8"]]
+ 00afd688 ["CALL", null, ["callee:00bdb010:8"]]
- 00afd5c0 bytes 68760394
+ 00afd688 bytes 62760394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b5cf5093c8dbbefdcc26b45f40f157"></a>

### [`00afd5f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd5f8.md) → [`00afd6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd6c0.md) _ZN8firebase4Path8MakePathERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afd62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd5f8.md#insn-00afd62c)
- 新版 [`00afd6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd6c0.md#insn-00afd6f4)

~~~diff
- 00afd62c ["INT_ADD", "register:40f0:8", ["const:afd62c:8", "const:4:8"]]
- 00afd62c ["CALL", null, ["callee:00bde1e0:8"]]
+ 00afd6f4 ["INT_ADD", "register:40f0:8", ["const:afd6f4:8", "const:4:8"]]
+ 00afd6f4 ["CALL", null, ["callee:00bde1e0:8"]]
- 00afd62c bytes c1820394
+ 00afd6f4 bytes bb820394
~~~


<a id="compare-87b8d5797a6b0323b89c0babc7e00922"></a>

### [`00afdf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdf50.md) → [`00afe018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdec50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec50.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`00bded00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded00.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdf50.md#insn-00afe060) · [`00afe08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdf50.md#insn-00afe08c) · [`00afe0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdf50.md#insn-00afe0dc)
- 新版 [`00afe128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe128) · [`00afe154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe154) · [`00afe1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md#insn-00afe1a4)

~~~diff
- 00afe060 ["INT_ADD", "register:40f0:8", ["const:afe060:8", "const:4:8"]]
- 00afe060 ["CALL", null, ["callee:00bdda40:8"]]
+ 00afe128 ["INT_ADD", "register:40f0:8", ["const:afe128:8", "const:4:8"]]
+ 00afe128 ["CALL", null, ["callee:00bdda40:8"]]
- 00afe060 bytes 4c7e0394
+ 00afe128 bytes 467e0394
- 00afe08c ["INT_ADD", "register:40f0:8", ["const:afe08c:8", "const:4:8"]]
- 00afe08c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afe154 ["INT_ADD", "register:40f0:8", ["const:afe154:8", "const:4:8"]]
+ 00afe154 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afe08c bytes ad730394
+ 00afe154 bytes a7730394
- 00afe0dc ["INT_ADD", "register:40f0:8", ["const:afe0dc:8", "const:4:8"]]
- 00afe0dc ["CALL", null, ["callee:00bdb0a0:8"]]
+ 00afe1a4 ["INT_ADD", "register:40f0:8", ["const:afe1a4:8", "const:4:8"]]
+ 00afe1a4 ["CALL", null, ["callee:00bdb0a0:8"]]
- 00afe0dc bytes c5730394
+ 00afe1a4 bytes bf730394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abb5814f241b9d35f9208e28484d32ad"></a>

### [`00afe270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe270.md) → [`00afe338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdb6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6a0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe270.md#insn-00afe30c) · [`00afe354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe270.md#insn-00afe354) · [`00afe378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe270.md#insn-00afe378)
- 新版 [`00afe3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe3d4) · [`00afe41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe41c) · [`00afe440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe338.md#insn-00afe440)

~~~diff
- 00afe30c ["INT_ADD", "register:40f0:8", ["const:afe30c:8", "const:4:8"]]
- 00afe30c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afe3d4 ["INT_ADD", "register:40f0:8", ["const:afe3d4:8", "const:4:8"]]
+ 00afe3d4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afe30c bytes 0d730394
+ 00afe3d4 bytes 07730394
- 00afe354 ["INT_ADD", "register:40f0:8", ["const:afe354:8", "const:4:8"]]
- 00afe354 ["CALL", null, ["callee:00bdb160:8"]]
+ 00afe41c ["INT_ADD", "register:40f0:8", ["const:afe41c:8", "const:4:8"]]
+ 00afe41c ["CALL", null, ["callee:00bdb160:8"]]
- 00afe354 bytes 57730394
+ 00afe41c bytes 51730394
- 00afe378 ["INT_ADD", "register:40f0:8", ["const:afe378:8", "const:4:8"]]
- 00afe378 ["CALL", null, ["callee:00bdb010:8"]]
+ 00afe440 ["INT_ADD", "register:40f0:8", ["const:afe440:8", "const:4:8"]]
+ 00afe440 ["CALL", null, ["callee:00bdb010:8"]]
- 00afe378 bytes fa720394
+ 00afe440 bytes f4720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d2a84f19d39c2039a6bef758116565"></a>

### [`00afe3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md) → [`00afe46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec60.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`00bded10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded10.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md#insn-00afe4b4) · [`00afe4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md#insn-00afe4e0) · [`00afe570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md#insn-00afe570)
- 新版 [`00afe57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe57c) · [`00afe5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe5a8) · [`00afe638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md#insn-00afe638)

~~~diff
- 00afe4b4 ["INT_ADD", "register:40f0:8", ["const:afe4b4:8", "const:4:8"]]
- 00afe4b4 ["CALL", null, ["callee:00bdda40:8"]]
+ 00afe57c ["INT_ADD", "register:40f0:8", ["const:afe57c:8", "const:4:8"]]
+ 00afe57c ["CALL", null, ["callee:00bdda40:8"]]
- 00afe4b4 bytes 377d0394
+ 00afe57c bytes 317d0394
- 00afe4e0 ["INT_ADD", "register:40f0:8", ["const:afe4e0:8", "const:4:8"]]
- 00afe4e0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afe5a8 ["INT_ADD", "register:40f0:8", ["const:afe5a8:8", "const:4:8"]]
+ 00afe5a8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afe4e0 bytes 98720394
+ 00afe5a8 bytes 92720394
- 00afe570 ["INT_ADD", "register:40f0:8", ["const:afe570:8", "const:4:8"]]
- 00afe570 ["CALL", null, ["callee:00bded10:8"]]
+ 00afe638 ["INT_ADD", "register:40f0:8", ["const:afe638:8", "const:4:8"]]
+ 00afe638 ["CALL", null, ["callee:00bded10:8"]]
- 00afe570 bytes bc810394
+ 00afe638 bytes b6810394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb75bd592037e687f4b910008ac3039c"></a>

### [`00afe91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe91c.md) → [`00afe9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdecc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdecc0.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bded70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded70.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe91c.md#insn-00afe948) · [`00afe964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe91c.md#insn-00afe964) · [`00afe9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe91c.md#insn-00afe9c0)
- 新版 [`00afea10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea10) · [`00afea2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea2c) · [`00afea88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe9e4.md#insn-00afea88)

~~~diff
- 00afe948 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afe948 ["INT_ADD", "register:40f0:8", ["const:afe948:8", "const:4:8"]]
- 00afe948 ["CALLIND", null, ["register:0:8"]]
+ 00afea10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afea10 ["INT_ADD", "register:40f0:8", ["const:afea10:8", "const:4:8"]]
+ 00afea10 ["CALLIND", null, ["register:0:8"]]
- 00afe948 bytes 00013fd6
+ 00afea10 bytes 00013fd6
- 00afe964 ["INT_ADD", "register:40f0:8", ["const:afe964:8", "const:4:8"]]
- 00afe964 ["CALL", null, ["callee:00bdb010:8"]]
+ 00afea2c ["INT_ADD", "register:40f0:8", ["const:afea2c:8", "const:4:8"]]
+ 00afea2c ["CALL", null, ["callee:00bdb010:8"]]
- 00afe964 bytes 7f710394
+ 00afea2c bytes 79710394
- 00afe9c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afe9c0 ["INT_ADD", "register:40f0:8", ["const:afe9c0:8", "const:4:8"]]
- 00afe9c0 ["CALLIND", null, ["register:0:8"]]
+ 00afea88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afea88 ["INT_ADD", "register:40f0:8", ["const:afea88:8", "const:4:8"]]
+ 00afea88 ["CALLIND", null, ["register:0:8"]]
- 00afe9c0 bytes 00013fd6
+ 00afea88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4508c7b83fd4958a817a93cd30ae5662"></a>

### [`00b00e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e2c.md) → [`00b00ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md) _ZN8firebase12FutureHandle6DetachEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) · 呼出先 1件 [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) · 呼出先 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e2c.md#insn-00b00e4c) · [`00b00e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e2c.md#insn-00b00e60)
- 新版 [`00b00f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md#insn-00b00f14) · [`00b00f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00ef4.md#insn-00b00f28)

~~~diff
- 00b00e4c ["INT_ADD", "register:40f0:8", ["const:b00e4c:8", "const:4:8"]]
- 00b00e4c ["CALL", null, ["callee:00bddd60:8"]]
+ 00b00f14 ["INT_ADD", "register:40f0:8", ["const:b00f14:8", "const:4:8"]]
+ 00b00f14 ["CALL", null, ["callee:00bddd60:8"]]
- 00b00e4c bytes 99730394
+ 00b00f14 bytes 93730394
- 00b00e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00e60 ["INT_ADD", "register:40f0:8", ["const:b00e60:8", "const:4:8"]]
- 00b00e60 ["CALLIND", null, ["register:0:8"]]
+ 00b00f28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b00f28 ["INT_ADD", "register:40f0:8", ["const:b00f28:8", "const:4:8"]]
+ 00b00f28 ["CALLIND", null, ["register:0:8"]]
- 00b00e60 bytes 00013fd6
+ 00b00f28 bytes 00013fd6
~~~


