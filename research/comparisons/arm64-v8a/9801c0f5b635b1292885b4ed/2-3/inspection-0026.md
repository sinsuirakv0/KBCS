# v16.0.1 → v16.0.2 · 要調査の変更候補 (26)

[一覧の目次](README.md)

<a id="compare-6c6e4862cf7c418045041db2bdc5fc06"></a>

### [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) → [`0084932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md) FUN_0084932c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a3e0.md) [`0086bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bec4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008492ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md#insn-008492ec)
- 新版 `00849344`（命令位置の公開資料なし）

~~~diff
- 008492ec ["INT_ADD", "register:40f0:8", ["const:8492ec:8", "const:4:8"]]
- 008492ec ["CALL", null, ["callee:0086bec4:8"]]
+ 00849344 ["INT_ADD", "register:40f0:8", ["const:849344:8", "const:4:8"]]
+ 00849344 ["CALL", null, ["callee:0086bec4:8"]]
- 008492ec bytes e08a0094
+ 00849344 bytes e08a0094
~~~


<a id="compare-ec8f2086d4d321400ddcf966b02280cb"></a>

### [`00849304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849304.md) → [`0084935c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084935c.md) FUN_0084935c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084931c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849304.md#insn-0084931c)
- 新版 `00849374`（命令位置の公開資料なし）

~~~diff
- 0084931c ["INT_ADD", "register:40f0:8", ["const:84931c:8", "const:4:8"]]
- 0084931c ["CALL", null, ["callee:005c17dc:8"]]
+ 00849374 ["INT_ADD", "register:40f0:8", ["const:849374:8", "const:4:8"]]
+ 00849374 ["CALL", null, ["callee:005c17dc:8"]]
- 0084931c bytes 20e1f597
+ 00849374 bytes 1ae1f597
~~~


<a id="compare-5870aef74d31afeae665ff2d0f9bb3c1"></a>

### [`00849334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849334.md) → [`0084938c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084938c.md) FUN_0084938c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009b3b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009b3b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3b5c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849334.md#insn-00849350)
- 新版 `008493a8`（命令位置の公開資料なし）

~~~diff
- 00849350 ["INT_ADD", "register:40f0:8", ["const:849350:8", "const:4:8"]]
- 00849350 ["CALL", null, ["callee:009b3b5c:8"]]
+ 008493a8 ["INT_ADD", "register:40f0:8", ["const:8493a8:8", "const:4:8"]]
+ 008493a8 ["CALL", null, ["callee:009b3b5c:8"]]
- 00849350 bytes eea90594
+ 008493a8 bytes eda90594
~~~


<a id="compare-3f819c67d942dc4dc403e6585ee4425b"></a>

### [`00849370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md) → [`008493c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008493c8.md) FUN_008493c8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00747804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747804.md) [`00748b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/00748b30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0074785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/0074785c.md) [`00748b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748b88.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008493a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md#insn-008493a8) · [`008493bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md#insn-008493bc) · [`008493c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849370.md#insn-008493c8)
- 新版 `00849400`（命令位置の公開資料なし） · `00849414`（命令位置の公開資料なし） · `00849420`（命令位置の公開資料なし）

~~~diff
- 008493a8 ["INT_ADD", "register:40f0:8", ["const:8493a8:8", "const:4:8"]]
- 008493a8 ["CALL", null, ["callee:00748b88:8"]]
+ 00849400 ["INT_ADD", "register:40f0:8", ["const:849400:8", "const:4:8"]]
+ 00849400 ["CALL", null, ["callee:00748b88:8"]]
- 008493a8 bytes e2fdfb97
+ 00849400 bytes e2fdfb97
- 008493bc ["INT_ADD", "register:40f0:8", ["const:8493bc:8", "const:4:8"]]
- 008493bc ["CALL", null, ["callee:00c57f80:8"]]
+ 00849414 ["INT_ADD", "register:40f0:8", ["const:849414:8", "const:4:8"]]
+ 00849414 ["CALL", null, ["callee:00c57f80:8"]]
- 008493bc bytes bd3a1094
+ 00849414 bytes db3a1094
- 008493c8 ["INT_ADD", "register:40f0:8", ["const:8493c8:8", "const:4:8"]]
- 008493c8 ["CALL", null, ["callee:00676aa0:8"]]
+ 00849420 ["INT_ADD", "register:40f0:8", ["const:849420:8", "const:4:8"]]
+ 00849420 ["CALL", null, ["callee:00676aa0:8"]]
- 008493c8 bytes a6b5f897
+ 00849420 bytes a0b5f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1243a04119e8e77773e5299aa79ca62"></a>

### [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) → [`00849458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849458.md) FUN_00849458

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`0086a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`0086a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a508.md) [`0086a54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a54c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md#insn-00849430) · [`0084943c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md#insn-0084943c) · [`00849448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md#insn-00849448)
- 新版 `00849488`（命令位置の公開資料なし） · `00849494`（命令位置の公開資料なし） · `008494a0`（命令位置の公開資料なし）

~~~diff
- 00849430 ["INT_ADD", "register:40f0:8", ["const:849430:8", "const:4:8"]]
- 00849430 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849488 ["INT_ADD", "register:40f0:8", ["const:849488:8", "const:4:8"]]
+ 00849488 ["CALL", null, ["callee:00c57f80:8"]]
- 00849430 bytes a03a1094
+ 00849488 bytes be3a1094
- 0084943c ["INT_ADD", "register:40f0:8", ["const:84943c:8", "const:4:8"]]
- 0084943c ["CALL", null, ["callee:0086a4b8:8"]]
+ 00849494 ["INT_ADD", "register:40f0:8", ["const:849494:8", "const:4:8"]]
+ 00849494 ["CALL", null, ["callee:0086a4b8:8"]]
- 0084943c bytes 09840094
+ 00849494 bytes 09840094
- 00849448 ["INT_ADD", "register:40f0:8", ["const:849448:8", "const:4:8"]]
- 00849448 ["CALL", null, ["callee:0086a508:8"]]
+ 008494a0 ["INT_ADD", "register:40f0:8", ["const:8494a0:8", "const:4:8"]]
+ 008494a0 ["CALL", null, ["callee:0086a508:8"]]
- 00849448 bytes 1a840094
+ 008494a0 bytes 1a840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80cd16d210b61d5583092d6fd97a2b09"></a>

### [`008494d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008494d0.md) → [`00849528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849528.md) FUN_00849528

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008494f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008494d0.md#insn-008494f4) · [`00849504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008494d0.md#insn-00849504) · [`00849510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008494d0.md#insn-00849510)
- 新版 `0084954c`（命令位置の公開資料なし） · `0084955c`（命令位置の公開資料なし） · `00849568`（命令位置の公開資料なし）

~~~diff
- 008494f4 ["INT_ADD", "register:40f0:8", ["const:8494f4:8", "const:4:8"]]
- 008494f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0084954c ["INT_ADD", "register:40f0:8", ["const:84954c:8", "const:4:8"]]
+ 0084954c ["CALL", null, ["callee:00c57f80:8"]]
- 008494f4 bytes 6f3a1094
+ 0084954c bytes 8d3a1094
- 00849504 ["INT_ADD", "register:40f0:8", ["const:849504:8", "const:4:8"]]
- 00849504 ["CALL", null, ["callee:00c57f80:8"]]
+ 0084955c ["INT_ADD", "register:40f0:8", ["const:84955c:8", "const:4:8"]]
+ 0084955c ["CALL", null, ["callee:00c57f80:8"]]
- 00849504 bytes 6b3a1094
+ 0084955c bytes 893a1094
- 00849510 ["INT_ADD", "register:40f0:8", ["const:849510:8", "const:4:8"]]
- 00849510 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849568 ["INT_ADD", "register:40f0:8", ["const:849568:8", "const:4:8"]]
+ 00849568 ["CALL", null, ["callee:00c57f80:8"]]
- 00849510 bytes 683a1094
+ 00849568 bytes 863a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d041f9288cc71b8b0f388628f62db2d5"></a>

### [`00849734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849734.md) → [`0084978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084978c.md) FUN_0084978c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849734.md#insn-00849750)
- 新版 `008497a8`（命令位置の公開資料なし）

~~~diff
- 00849750 ["INT_ADD", "register:40f0:8", ["const:849750:8", "const:4:8"]]
- 00849750 ["CALL", null, ["callee:00c57f80:8"]]
+ 008497a8 ["INT_ADD", "register:40f0:8", ["const:8497a8:8", "const:4:8"]]
+ 008497a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00849750 bytes d8391094
+ 008497a8 bytes f6391094
~~~


<a id="compare-e5bba50480f9fce05620063fcd44c585"></a>

### [`00849778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md) → [`008497d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008497d0.md) FUN_008497d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`0086a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`0086a5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008497a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md#insn-008497a0) · [`008497ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md#insn-008497ac) · [`008497d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md#insn-008497d0)
- 新版 `008497f8`（命令位置の公開資料なし） · `00849804`（命令位置の公開資料なし） · `00849828`（命令位置の公開資料なし）

~~~diff
- 008497a0 ["INT_ADD", "register:40f0:8", ["const:8497a0:8", "const:4:8"]]
- 008497a0 ["CALL", null, ["callee:0073a35c:8"]]
+ 008497f8 ["INT_ADD", "register:40f0:8", ["const:8497f8:8", "const:4:8"]]
+ 008497f8 ["CALL", null, ["callee:0073a35c:8"]]
- 008497a0 bytes d9c2fb97
+ 008497f8 bytes d9c2fb97
- 008497ac ["INT_ADD", "register:40f0:8", ["const:8497ac:8", "const:4:8"]]
- 008497ac ["CALL", null, ["callee:0086a5fc:8"]]
+ 00849804 ["INT_ADD", "register:40f0:8", ["const:849804:8", "const:4:8"]]
+ 00849804 ["CALL", null, ["callee:0086a5fc:8"]]
- 008497ac bytes 7e830094
+ 00849804 bytes 7e830094
- 008497d0 ["INT_ADD", "register:40f0:8", ["const:8497d0:8", "const:4:8"]]
- 008497d0 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00849828 ["INT_ADD", "register:40f0:8", ["const:849828:8", "const:4:8"]]
+ 00849828 ["CALL", null, ["callee:00c57fb0:8"]]
- 008497d0 bytes c4391094
+ 00849828 bytes e2391094
~~~


<a id="compare-b0916f08df13db108ce29b5f9197c17a"></a>

### [`008497d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008497d4.md) → [`0084982c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084982c.md) FUN_0084982c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008497f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008497d4.md#insn-008497f0)
- 新版 `00849848`（命令位置の公開資料なし）

~~~diff
- 008497f0 ["INT_ADD", "register:40f0:8", ["const:8497f0:8", "const:4:8"]]
- 008497f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849848 ["INT_ADD", "register:40f0:8", ["const:849848:8", "const:4:8"]]
+ 00849848 ["CALL", null, ["callee:00c57f80:8"]]
- 008497f0 bytes b0391094
+ 00849848 bytes ce391094
~~~


<a id="compare-4acd72674d6c180e4292922a26423d4c"></a>

### [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) → [`00849870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849870.md) FUN_00849870

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`0086bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbf0.md) [`0086be10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be10.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md#insn-00849838) · [`00849844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md#insn-00849844) · [`00849850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md#insn-00849850)
- 新版 `00849890`（命令位置の公開資料なし） · `0084989c`（命令位置の公開資料なし） · `008498a8`（命令位置の公開資料なし）

~~~diff
- 00849838 ["INT_ADD", "register:40f0:8", ["const:849838:8", "const:4:8"]]
- 00849838 ["CALL", null, ["callee:005c17dc:8"]]
+ 00849890 ["INT_ADD", "register:40f0:8", ["const:849890:8", "const:4:8"]]
+ 00849890 ["CALL", null, ["callee:005c17dc:8"]]
- 00849838 bytes d9dff597
+ 00849890 bytes d3dff597
- 00849844 ["INT_ADD", "register:40f0:8", ["const:849844:8", "const:4:8"]]
- 00849844 ["CALL", null, ["callee:0086bbf0:8"]]
+ 0084989c ["INT_ADD", "register:40f0:8", ["const:84989c:8", "const:4:8"]]
+ 0084989c ["CALL", null, ["callee:0086bbf0:8"]]
- 00849844 bytes d5880094
+ 0084989c bytes d5880094
- 00849850 ["INT_ADD", "register:40f0:8", ["const:849850:8", "const:4:8"]]
- 00849850 ["CALL", null, ["callee:005c3ebc:8"]]
+ 008498a8 ["INT_ADD", "register:40f0:8", ["const:8498a8:8", "const:4:8"]]
+ 008498a8 ["CALL", null, ["callee:005c3ebc:8"]]
- 00849850 bytes 8be9f597
+ 008498a8 bytes 85e9f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceda45803d0c89d990fbc51cbc834585"></a>

### [`0084987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md) → [`008498d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008498d4.md) FUN_008498d4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0066b9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b9dc.md) [`0066baa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066baa4.md) [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0066ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066ba1c.md) [`0066bae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066bae4.md) [`0086a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6ac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md#insn-00849898) · [`008498a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md#insn-008498a4) · [`008498b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md#insn-008498b0)
- 新版 `008498f0`（命令位置の公開資料なし） · `008498fc`（命令位置の公開資料なし） · `00849908`（命令位置の公開資料なし）

~~~diff
- 00849898 ["INT_ADD", "register:40f0:8", ["const:849898:8", "const:4:8"]]
- 00849898 ["CALL", null, ["callee:00c57f80:8"]]
+ 008498f0 ["INT_ADD", "register:40f0:8", ["const:8498f0:8", "const:4:8"]]
+ 008498f0 ["CALL", null, ["callee:00c57f80:8"]]
- 00849898 bytes 86391094
+ 008498f0 bytes a4391094
- 008498a4 ["INT_ADD", "register:40f0:8", ["const:8498a4:8", "const:4:8"]]
- 008498a4 ["CALL", null, ["callee:0086a6ac:8"]]
+ 008498fc ["INT_ADD", "register:40f0:8", ["const:8498fc:8", "const:4:8"]]
+ 008498fc ["CALL", null, ["callee:0086a6ac:8"]]
- 008498a4 bytes 6c830094
+ 008498fc bytes 6c830094
- 008498b0 ["INT_ADD", "register:40f0:8", ["const:8498b0:8", "const:4:8"]]
- 008498b0 ["CALL", null, ["callee:0066bae4:8"]]
+ 00849908 ["INT_ADD", "register:40f0:8", ["const:849908:8", "const:4:8"]]
+ 00849908 ["CALL", null, ["callee:0066bae4:8"]]
- 008498b0 bytes 7d88f897
+ 00849908 bytes 7788f897
~~~


<a id="compare-1a4269bc66509573c0725439b618add5"></a>

### [`008498c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498c8.md) → [`00849920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849920.md) FUN_00849920

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006a60d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a60d8.md) [`006a6128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6128.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006a6130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6130.md) [`006a6180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008498e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498c8.md#insn-008498e0)
- 新版 `00849938`（命令位置の公開資料なし）

~~~diff
- 008498e0 ["INT_ADD", "register:40f0:8", ["const:8498e0:8", "const:4:8"]]
- 008498e0 ["CALL", null, ["callee:006a6130:8"]]
+ 00849938 ["INT_ADD", "register:40f0:8", ["const:849938:8", "const:4:8"]]
+ 00849938 ["CALL", null, ["callee:006a6130:8"]]
- 008498e0 bytes fe71f997
+ 00849938 bytes fe71f997
~~~


<a id="compare-67b2d07e877993180225e7666371f4e9"></a>

### [`008498f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498f8.md) → [`00849950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849950.md) FUN_00849950

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498f8.md#insn-00849940) · [`00849950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498f8.md#insn-00849950) · [`0084995c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008498f8.md#insn-0084995c)
- 新版 `00849998`（命令位置の公開資料なし） · `008499a8`（命令位置の公開資料なし） · `008499b4`（命令位置の公開資料なし）

~~~diff
- 00849940 ["INT_ADD", "register:40f0:8", ["const:849940:8", "const:4:8"]]
- 00849940 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849998 ["INT_ADD", "register:40f0:8", ["const:849998:8", "const:4:8"]]
+ 00849998 ["CALL", null, ["callee:00c57f80:8"]]
- 00849940 bytes 5c391094
+ 00849998 bytes 7a391094
- 00849950 ["INT_ADD", "register:40f0:8", ["const:849950:8", "const:4:8"]]
- 00849950 ["CALL", null, ["callee:00c57f80:8"]]
+ 008499a8 ["INT_ADD", "register:40f0:8", ["const:8499a8:8", "const:4:8"]]
+ 008499a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00849950 bytes 58391094
+ 008499a8 bytes 76391094
- 0084995c ["INT_ADD", "register:40f0:8", ["const:84995c:8", "const:4:8"]]
- 0084995c ["CALL", null, ["callee:005c17dc:8"]]
+ 008499b4 ["INT_ADD", "register:40f0:8", ["const:8499b4:8", "const:4:8"]]
+ 008499b4 ["CALL", null, ["callee:005c17dc:8"]]
- 0084995c bytes 90dff597
+ 008499b4 bytes 8adff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb416875cadb553d00dbe96f3df091f0"></a>

### [`008499e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008499e0.md) → [`00849a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849a38.md) FUN_00849a38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008499f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008499e0.md#insn-008499f8)
- 新版 `00849a50`（命令位置の公開資料なし）

~~~diff
- 008499f8 ["INT_ADD", "register:40f0:8", ["const:8499f8:8", "const:4:8"]]
- 008499f8 ["CALL", null, ["callee:005c3ebc:8"]]
+ 00849a50 ["INT_ADD", "register:40f0:8", ["const:849a50:8", "const:4:8"]]
+ 00849a50 ["CALL", null, ["callee:005c3ebc:8"]]
- 008499f8 bytes 21e9f597
+ 00849a50 bytes 1be9f597
~~~


<a id="compare-961bbde718a833b995ab2dd39399eae3"></a>

### [`00849a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a10.md) → [`00849a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849a68.md) FUN_00849a68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a10.md#insn-00849a30)
- 新版 `00849a88`（命令位置の公開資料なし）

~~~diff
- 00849a30 ["INT_ADD", "register:40f0:8", ["const:849a30:8", "const:4:8"]]
- 00849a30 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849a88 ["INT_ADD", "register:40f0:8", ["const:849a88:8", "const:4:8"]]
+ 00849a88 ["CALL", null, ["callee:00c57f80:8"]]
- 00849a30 bytes 20391094
+ 00849a88 bytes 3e391094
~~~


<a id="compare-b1822da5dfe5fcd519ad16abe25f839a"></a>

### [`00849a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md) → [`00849aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849aa0.md) FUN_00849aa0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c1820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1820.md) [`0086a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md#insn-00849a60) · [`00849a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md#insn-00849a70) · [`00849a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md#insn-00849a80)
- 新版 `00849ab8`（命令位置の公開資料なし） · `00849ac8`（命令位置の公開資料なし） · `00849ad8`（命令位置の公開資料なし）

~~~diff
- 00849a60 ["INT_ADD", "register:40f0:8", ["const:849a60:8", "const:4:8"]]
- 00849a60 ["CALL", null, ["callee:005c17dc:8"]]
+ 00849ab8 ["INT_ADD", "register:40f0:8", ["const:849ab8:8", "const:4:8"]]
+ 00849ab8 ["CALL", null, ["callee:005c17dc:8"]]
- 00849a60 bytes 4fdff597
+ 00849ab8 bytes 49dff597
- 00849a70 ["INT_ADD", "register:40f0:8", ["const:849a70:8", "const:4:8"]]
- 00849a70 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849ac8 ["INT_ADD", "register:40f0:8", ["const:849ac8:8", "const:4:8"]]
+ 00849ac8 ["CALL", null, ["callee:00c57f80:8"]]
- 00849a70 bytes 10391094
+ 00849ac8 bytes 2e391094
- 00849a80 ["INT_ADD", "register:40f0:8", ["const:849a80:8", "const:4:8"]]
- 00849a80 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849ad8 ["INT_ADD", "register:40f0:8", ["const:849ad8:8", "const:4:8"]]
+ 00849ad8 ["CALL", null, ["callee:00c57f80:8"]]
- 00849a80 bytes 0c391094
+ 00849ad8 bytes 2a391094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ca0c612967e267e740eb601f9a0a7a"></a>

### [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) → [`00849afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849afc.md) FUN_00849afc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0086a7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7fc.md) [`0086a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a890.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md#insn-00849ac0) · [`00849acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md#insn-00849acc)
- 新版 `00849b18`（命令位置の公開資料なし） · `00849b24`（命令位置の公開資料なし）

~~~diff
- 00849ac0 ["INT_ADD", "register:40f0:8", ["const:849ac0:8", "const:4:8"]]
- 00849ac0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849b18 ["INT_ADD", "register:40f0:8", ["const:849b18:8", "const:4:8"]]
+ 00849b18 ["CALL", null, ["callee:00c57f80:8"]]
- 00849ac0 bytes fc381094
+ 00849b18 bytes 1a391094
- 00849acc ["INT_ADD", "register:40f0:8", ["const:849acc:8", "const:4:8"]]
- 00849acc ["CALL", null, ["callee:0086a7fc:8"]]
+ 00849b24 ["INT_ADD", "register:40f0:8", ["const:849b24:8", "const:4:8"]]
+ 00849b24 ["CALL", null, ["callee:0086a7fc:8"]]
- 00849acc bytes 36830094
+ 00849b24 bytes 36830094
~~~


<a id="compare-d3aed6710a380ad8a760b4310f3ad17d"></a>

### [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) → [`00849b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849b3c.md) FUN_00849b3c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0086a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a8e0.md) [`0086a930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a930.md) [`0086bbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md#insn-00849afc) · [`00849b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md#insn-00849b08) · [`00849b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md#insn-00849b14)
- 新版 `00849b54`（命令位置の公開資料なし） · `00849b60`（命令位置の公開資料なし） · `00849b6c`（命令位置の公開資料なし）

~~~diff
- 00849afc ["INT_ADD", "register:40f0:8", ["const:849afc:8", "const:4:8"]]
- 00849afc ["CALL", null, ["callee:0086a8e0:8"]]
+ 00849b54 ["INT_ADD", "register:40f0:8", ["const:849b54:8", "const:4:8"]]
+ 00849b54 ["CALL", null, ["callee:0086a8e0:8"]]
- 00849afc bytes 63830094
+ 00849b54 bytes 63830094
- 00849b08 ["INT_ADD", "register:40f0:8", ["const:849b08:8", "const:4:8"]]
- 00849b08 ["CALL", null, ["callee:0086bbac:8"]]
+ 00849b60 ["INT_ADD", "register:40f0:8", ["const:849b60:8", "const:4:8"]]
+ 00849b60 ["CALL", null, ["callee:0086bbac:8"]]
- 00849b08 bytes 13880094
+ 00849b60 bytes 13880094
- 00849b14 ["INT_ADD", "register:40f0:8", ["const:849b14:8", "const:4:8"]]
- 00849b14 ["CALL", null, ["callee:005c17dc:8"]]
+ 00849b6c ["INT_ADD", "register:40f0:8", ["const:849b6c:8", "const:4:8"]]
+ 00849b6c ["CALL", null, ["callee:005c17dc:8"]]
- 00849b14 bytes 22dff597
+ 00849b6c bytes 1cdff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a863ceede006a5c047d02e8d9d285e2"></a>

### [`00849b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md) → [`00849bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849bb0.md) FUN_00849bb0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md#insn-00849b70) · [`00849b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md#insn-00849b80)
- 新版 `00849bc8`（命令位置の公開資料なし） · `00849bd8`（命令位置の公開資料なし）

~~~diff
- 00849b70 ["INT_ADD", "register:40f0:8", ["const:849b70:8", "const:4:8"]]
- 00849b70 ["CALL", null, ["callee:005c3ebc:8"]]
+ 00849bc8 ["INT_ADD", "register:40f0:8", ["const:849bc8:8", "const:4:8"]]
+ 00849bc8 ["CALL", null, ["callee:005c3ebc:8"]]
- 00849b70 bytes c3e8f597
+ 00849bc8 bytes bde8f597
- 00849b80 ["INT_ADD", "register:40f0:8", ["const:849b80:8", "const:4:8"]]
- 00849b80 ["CALL", null, ["callee:00c57f80:8"]]
+ 00849bd8 ["INT_ADD", "register:40f0:8", ["const:849bd8:8", "const:4:8"]]
+ 00849bd8 ["CALL", null, ["callee:00c57f80:8"]]
- 00849b80 bytes cc381094
+ 00849bd8 bytes ea381094
~~~


<a id="compare-d03bfa829b296e0c16a872e4dcf0dadd"></a>

### [`00849b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md) → [`00849bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849bf0.md) FUN_00849bf0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0086aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aa50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md#insn-00849bb0) · [`00849bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md#insn-00849bbc)
- 新版 `00849c08`（命令位置の公開資料なし） · `00849c14`（命令位置の公開資料なし）

~~~diff
- 00849bb0 ["INT_ADD", "register:40f0:8", ["const:849bb0:8", "const:4:8"]]
- 00849bb0 ["CALL", null, ["callee:00676aa0:8"]]
+ 00849c08 ["INT_ADD", "register:40f0:8", ["const:849c08:8", "const:4:8"]]
+ 00849c08 ["CALL", null, ["callee:00676aa0:8"]]
- 00849bb0 bytes acb3f897
+ 00849c08 bytes a6b3f897
- 00849bbc ["INT_ADD", "register:40f0:8", ["const:849bbc:8", "const:4:8"]]
- 00849bbc ["CALL", null, ["callee:005c3ebc:8"]]
+ 00849c14 ["INT_ADD", "register:40f0:8", ["const:849c14:8", "const:4:8"]]
+ 00849c14 ["CALL", null, ["callee:005c3ebc:8"]]
- 00849bbc bytes b0e8f597
+ 00849c14 bytes aae8f597
~~~


<a id="compare-eda03f1d836d75ce261e8977d5bc1f25"></a>

### [`00849bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md) → [`00849c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c2c.md) FUN_00849c2c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00726390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726390.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`007263e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00726/007263e8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md#insn-00849bec) · [`00849bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849bd4.md#insn-00849bf8)
- 新版 `00849c44`（命令位置の公開資料なし） · `00849c50`（命令位置の公開資料なし）

~~~diff
- 00849bec ["INT_ADD", "register:40f0:8", ["const:849bec:8", "const:4:8"]]
- 00849bec ["CALL", null, ["callee:00676aa0:8"]]
+ 00849c44 ["INT_ADD", "register:40f0:8", ["const:849c44:8", "const:4:8"]]
+ 00849c44 ["CALL", null, ["callee:00676aa0:8"]]
- 00849bec bytes 9db3f897
+ 00849c44 bytes 97b3f897
- 00849bf8 ["INT_ADD", "register:40f0:8", ["const:849bf8:8", "const:4:8"]]
- 00849bf8 ["CALL", null, ["callee:005c17dc:8"]]
+ 00849c50 ["INT_ADD", "register:40f0:8", ["const:849c50:8", "const:4:8"]]
+ 00849c50 ["CALL", null, ["callee:005c17dc:8"]]
- 00849bf8 bytes e9def597
+ 00849c50 bytes e3def597
~~~


<a id="compare-30e042ec6df4619cbf7d4ee9919f9448"></a>

### [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) → [`00849c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c68.md) FUN_00849c68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md#insn-00849c30) · [`00849c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md#insn-00849c44) · [`00849c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md#insn-00849c4c)
- 新版 `00849c88`（命令位置の公開資料なし） · `00849c9c`（命令位置の公開資料なし） · `00849ca4`（命令位置の公開資料なし）

~~~diff
- 00849c30 ["INT_ADD", "register:40f0:8", ["const:849c30:8", "const:4:8"]]
- 00849c30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00849c88 ["INT_ADD", "register:40f0:8", ["const:849c88:8", "const:4:8"]]
+ 00849c88 ["CALL", null, ["callee:00c53da0:8"]]
- 00849c30 bytes 34281094
+ 00849c88 bytes 46281094
- 00849c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00849c44 ["INT_ADD", "register:40f0:8", ["const:849c44:8", "const:4:8"]]
- 00849c44 ["CALLIND", null, ["register:0:8"]]
+ 00849c9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00849c9c ["INT_ADD", "register:40f0:8", ["const:849c9c:8", "const:4:8"]]
+ 00849c9c ["CALLIND", null, ["register:0:8"]]
- 00849c44 bytes 00013fd6
+ 00849c9c bytes 00013fd6
- 00849c4c ["INT_ADD", "register:40f0:8", ["const:849c4c:8", "const:4:8"]]
- 00849c4c ["CALL", null, ["callee:00c57f50:8"]]
+ 00849ca4 ["INT_ADD", "register:40f0:8", ["const:849ca4:8", "const:4:8"]]
+ 00849ca4 ["CALL", null, ["callee:00c57f50:8"]]
- 00849c4c bytes 8d381094
+ 00849ca4 bytes ab381094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed78a9ece6cfbf76e1ace8dd3e7f644"></a>

### [`00849c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md) → [`00849cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849cf0.md) FUN_00849cf0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0080e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e740.md) [`0080e8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080e8a0.md) [`0080ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080ea00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0080e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e798.md) [`0080e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080e8f8.md) [`0080ea58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ea58.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00849cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md#insn-00849cb0) · [`00849cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c98.md#insn-00849cbc)
- 新版 `00849d08`（命令位置の公開資料なし） · `00849d14`（命令位置の公開資料なし）

~~~diff
- 00849cb0 ["INT_ADD", "register:40f0:8", ["const:849cb0:8", "const:4:8"]]
- 00849cb0 ["CALL", null, ["callee:0080ea58:8"]]
+ 00849d08 ["INT_ADD", "register:40f0:8", ["const:849d08:8", "const:4:8"]]
+ 00849d08 ["CALL", null, ["callee:0080ea58:8"]]
- 00849cb0 bytes 5413ff97
+ 00849d08 bytes 5413ff97
- 00849cbc ["INT_ADD", "register:40f0:8", ["const:849cbc:8", "const:4:8"]]
- 00849cbc ["CALL", null, ["callee:0080e8f8:8"]]
+ 00849d14 ["INT_ADD", "register:40f0:8", ["const:849d14:8", "const:4:8"]]
+ 00849d14 ["CALL", null, ["callee:0080e8f8:8"]]
- 00849cbc bytes f912ff97
+ 00849d14 bytes f912ff97
~~~


<a id="compare-78682d4c07c1747fe81ded112da448d7"></a>

### [`00856cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856cf0.md) → [`00856d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856d48.md) FUN_00856d48

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00856d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856cf0.md#insn-00856d30) · [`00856d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856cf0.md#insn-00856d98) · [`00856dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856cf0.md#insn-00856dbc)
- 新版 `00856d88`（命令位置の公開資料なし） · `00856df0`（命令位置の公開資料なし） · `00856e14`（命令位置の公開資料なし）

~~~diff
- 00856d30 ["INT_ADD", "register:40f0:8", ["const:856d30:8", "const:4:8"]]
- 00856d30 ["CALL", null, ["callee:00c57f80:8"]]
+ 00856d88 ["INT_ADD", "register:40f0:8", ["const:856d88:8", "const:4:8"]]
+ 00856d88 ["CALL", null, ["callee:00c57f80:8"]]
- 00856d30 bytes 60041094
+ 00856d88 bytes 7e041094
- 00856d98 ["INT_ADD", "register:40f0:8", ["const:856d98:8", "const:4:8"]]
- 00856d98 ["CALL", null, ["callee:00c57f80:8"]]
+ 00856df0 ["INT_ADD", "register:40f0:8", ["const:856df0:8", "const:4:8"]]
+ 00856df0 ["CALL", null, ["callee:00c57f80:8"]]
- 00856d98 bytes 46041094
+ 00856df0 bytes 64041094
- 00856dbc ["INT_ADD", "register:40f0:8", ["const:856dbc:8", "const:4:8"]]
- 00856dbc ["CALL", null, ["callee:00c57f80:8"]]
+ 00856e14 ["INT_ADD", "register:40f0:8", ["const:856e14:8", "const:4:8"]]
+ 00856e14 ["CALL", null, ["callee:00c57f80:8"]]
- 00856dbc bytes 3d041094
+ 00856e14 bytes 5b041094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-368ef7b206bd6dd4b767900656badfaa"></a>

### [`00859af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859af8.md) → [`00859b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859b50.md) FUN_00859b50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00859b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859af8.md#insn-00859b18) · [`00859b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859af8.md#insn-00859b38)
- 新版 `00859b70`（命令位置の公開資料なし） · `00859b90`（命令位置の公開資料なし）

~~~diff
- 00859b18 ["INT_ADD", "register:40f0:8", ["const:859b18:8", "const:4:8"]]
- 00859b18 ["CALL", null, ["callee:00c53da0:8"]]
+ 00859b70 ["INT_ADD", "register:40f0:8", ["const:859b70:8", "const:4:8"]]
+ 00859b70 ["CALL", null, ["callee:00c53da0:8"]]
- 00859b18 bytes 7ae80f94
+ 00859b70 bytes 8ce80f94
- 00859b38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00859b38 ["INT_ADD", "register:40f0:8", ["const:859b38:8", "const:4:8"]]
- 00859b38 ["CALLIND", null, ["register:0:8"]]
+ 00859b90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00859b90 ["INT_ADD", "register:40f0:8", ["const:859b90:8", "const:4:8"]]
+ 00859b90 ["CALLIND", null, ["register:0:8"]]
- 00859b38 bytes 00013fd6
+ 00859b90 bytes 00013fd6
~~~


<a id="compare-c4125ae5a65c13b3ec011944d0b01933"></a>

### [`0085ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ada0.md) → [`0085adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085a/0085adf8.md) FUN_0085adf8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006bf88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf88c.md) · 呼出先 2件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md)
- 新版 呼出元 1件 [`006bf8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md) · 呼出先 2件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085adbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ada0.md#insn-0085adbc)
- 新版 `0085ae14`（命令位置の公開資料なし）

~~~diff
- 0085adbc ["INT_ADD", "register:40f0:8", ["const:85adbc:8", "const:4:8"]]
- 0085adbc ["CALL", null, ["callee:004678a0:8"]]
+ 0085ae14 ["INT_ADD", "register:40f0:8", ["const:85ae14:8", "const:4:8"]]
+ 0085ae14 ["CALL", null, ["callee:004678a0:8"]]
- 0085adbc bytes a932f097
+ 0085ae14 bytes a332f097
~~~


<a id="compare-e62e5fa58ae34006def3d08c82b30db3"></a>

### [`0085b2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md) → [`0085b350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b350.md) FUN_0085b350

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0086dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dea4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0086defc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086defc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085b354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md#insn-0085b354) · [`0085b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md#insn-0085b368) · [`0085b39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2f8.md#insn-0085b39c)
- 新版 `0085b3ac`（命令位置の公開資料なし） · `0085b3c0`（命令位置の公開資料なし） · `0085b3f4`（命令位置の公開資料なし）

~~~diff
- 0085b354 ["INT_ADD", "register:40f0:8", ["const:85b354:8", "const:4:8"]]
- 0085b354 ["CALL", null, ["callee:0043bb60:8"]]
+ 0085b3ac ["INT_ADD", "register:40f0:8", ["const:85b3ac:8", "const:4:8"]]
+ 0085b3ac ["CALL", null, ["callee:0043bb60:8"]]
- 0085b354 bytes f381ef97
+ 0085b3ac bytes ed81ef97
- 0085b368 ["INT_ADD", "register:40f0:8", ["const:85b368:8", "const:4:8"]]
- 0085b368 ["CALL", null, ["callee:0043bb60:8"]]
+ 0085b3c0 ["INT_ADD", "register:40f0:8", ["const:85b3c0:8", "const:4:8"]]
+ 0085b3c0 ["CALL", null, ["callee:0043bb60:8"]]
- 0085b368 bytes ee81ef97
+ 0085b3c0 bytes e881ef97
- 0085b39c ["INT_ADD", "register:40f0:8", ["const:85b39c:8", "const:4:8"]]
- 0085b39c ["CALL", null, ["callee:0086defc:8"]]
+ 0085b3f4 ["INT_ADD", "register:40f0:8", ["const:85b3f4:8", "const:4:8"]]
+ 0085b3f4 ["CALL", null, ["callee:0086defc:8"]]
- 0085b39c bytes c24a0094
+ 0085b3f4 bytes c24a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63ecc20947696a4ea3422ee9336ddc3"></a>

### [`0085bf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md) → [`0085bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bf60.md) FUN_0085bf60

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 3件 [`00ab91b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab91b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 7件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) [`00a95838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a95/00a95838.md) · 呼出先 3件 [`00ab9228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab9/00ab9228.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0085bfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md#insn-0085bfd0) · [`0085bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md#insn-0085bfe0) · [`0085bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md#insn-0085bffc)
- 新版 `0085c028`（命令位置の公開資料なし） · `0085c038`（命令位置の公開資料なし） · `0085c054`（命令位置の公開資料なし）

~~~diff
- 0085bfd0 ["INT_ADD", "register:40f0:8", ["const:85bfd0:8", "const:4:8"]]
- 0085bfd0 ["CALL", null, ["callee:00ab9228:8"]]
+ 0085c028 ["INT_ADD", "register:40f0:8", ["const:85c028:8", "const:4:8"]]
+ 0085c028 ["CALL", null, ["callee:00ab9228:8"]]
- 0085bfd0 bytes 7a740994
+ 0085c028 bytes 80740994
- 0085bfe0 ["INT_ADD", "register:40f0:8", ["const:85bfe0:8", "const:4:8"]]
- 0085bfe0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0085c038 ["INT_ADD", "register:40f0:8", ["const:85c038:8", "const:4:8"]]
+ 0085c038 ["CALL", null, ["callee:00c57f80:8"]]
- 0085bfe0 bytes b4ef0f94
+ 0085c038 bytes d2ef0f94
- 0085bffc ["INT_ADD", "register:40f0:8", ["const:85bffc:8", "const:4:8"]]
- 0085bffc ["CALL", null, ["callee:00ab9228:8"]]
+ 0085c054 ["INT_ADD", "register:40f0:8", ["const:85c054:8", "const:4:8"]]
+ 0085c054 ["CALL", null, ["callee:00ab9228:8"]]
- 0085bffc bytes 6f740994
+ 0085c054 bytes 75740994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dabbc4ec276754582ab4e77db42aa43"></a>

### [`008614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/008614b0.md) → [`00861508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/00861508.md) FUN_00861508

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) [`006706ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00670/006706ec.md) [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`006acf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006acf5c.md) [`006b5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b5/006b5404.md) · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 19件 [`0062a27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062a/0062a27c.md) [`0067072c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00670/0067072c.md) [`00680e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00680/00680e48.md) [`006acfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ac/006acfb4.md) [`006b545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b5/006b545c.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008614d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/008614b0.md#insn-008614d4) · [`008614e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/008614b0.md#insn-008614e0) · [`00861508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/008614b0.md#insn-00861508)
- 新版 `0086152c`（命令位置の公開資料なし） · `00861538`（命令位置の公開資料なし） · `00861560`（命令位置の公開資料なし）

~~~diff
- 008614d4 ["INT_ADD", "register:40f0:8", ["const:8614d4:8", "const:4:8"]]
- 008614d4 ["CALL", null, ["callee:004678a0:8"]]
+ 0086152c ["INT_ADD", "register:40f0:8", ["const:86152c:8", "const:4:8"]]
+ 0086152c ["CALL", null, ["callee:004678a0:8"]]
- 008614d4 bytes e318f097
+ 0086152c bytes dd18f097
- 008614e0 ["INT_ADD", "register:40f0:8", ["const:8614e0:8", "const:4:8"]]
- 008614e0 ["CALL", null, ["callee:0046ca04:8"]]
+ 00861538 ["INT_ADD", "register:40f0:8", ["const:861538:8", "const:4:8"]]
+ 00861538 ["CALL", null, ["callee:0046ca04:8"]]
- 008614e0 bytes 392df097
+ 00861538 bytes 332df097
- 00861508 ["INT_ADD", "register:40f0:8", ["const:861508:8", "const:4:8"]]
- 00861508 ["CALL", null, ["callee:00468fc8:8"]]
+ 00861560 ["INT_ADD", "register:40f0:8", ["const:861560:8", "const:4:8"]]
+ 00861560 ["CALL", null, ["callee:00468fc8:8"]]
- 00861508 bytes a01ef097
+ 00861560 bytes 9a1ef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07a5a08b2c145e6ed20d9fe1b5861491"></a>

### [`00865608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865608.md) → [`00865660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865660.md) FUN_00865660

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865608.md#insn-00865624) · [`00865644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865608.md#insn-00865644)
- 新版 `0086567c`（命令位置の公開資料なし） · `0086569c`（命令位置の公開資料なし）

~~~diff
- 00865624 ["INT_ADD", "register:40f0:8", ["const:865624:8", "const:4:8"]]
- 00865624 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086567c ["INT_ADD", "register:40f0:8", ["const:86567c:8", "const:4:8"]]
+ 0086567c ["CALL", null, ["callee:00c53da0:8"]]
- 00865624 bytes b7b90f94
+ 0086567c bytes c9b90f94
- 00865644 ["COPY", "register:0:8", ["register:4040:8"]]
- 00865644 ["INT_ADD", "register:40f0:8", ["const:865644:8", "const:4:8"]]
- 00865644 ["CALLIND", null, ["register:0:8"]]
+ 0086569c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086569c ["INT_ADD", "register:40f0:8", ["const:86569c:8", "const:4:8"]]
+ 0086569c ["CALLIND", null, ["register:0:8"]]
- 00865644 bytes 00013fd6
+ 0086569c bytes 00013fd6
~~~


<a id="compare-51d9ca4ee5243e873b5a5e3200523c7b"></a>

### [`00865658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865658.md) → [`008656b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/008656b0.md) FUN_008656b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865658.md#insn-00865674) · [`00865694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865658.md#insn-00865694)
- 新版 `008656cc`（命令位置の公開資料なし） · `008656ec`（命令位置の公開資料なし）

~~~diff
- 00865674 ["INT_ADD", "register:40f0:8", ["const:865674:8", "const:4:8"]]
- 00865674 ["CALL", null, ["callee:00c53da0:8"]]
+ 008656cc ["INT_ADD", "register:40f0:8", ["const:8656cc:8", "const:4:8"]]
+ 008656cc ["CALL", null, ["callee:00c53da0:8"]]
- 00865674 bytes a3b90f94
+ 008656cc bytes b5b90f94
- 00865694 ["COPY", "register:0:8", ["register:4040:8"]]
- 00865694 ["INT_ADD", "register:40f0:8", ["const:865694:8", "const:4:8"]]
- 00865694 ["CALLIND", null, ["register:0:8"]]
+ 008656ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 008656ec ["INT_ADD", "register:40f0:8", ["const:8656ec:8", "const:4:8"]]
+ 008656ec ["CALLIND", null, ["register:0:8"]]
- 00865694 bytes 00013fd6
+ 008656ec bytes 00013fd6
~~~


<a id="compare-9bfd63bc3f3437b1a27a5c3a2bddb94d"></a>

### [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) → [`00865adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865adc.md) FUN_00865adc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 2件 [`00865a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00865adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865adc.md) [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) · 呼出先 2件 [`00865adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865adc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md#insn-00865aa0) · [`00865aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md#insn-00865aac) · [`00865abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865a84.md#insn-00865abc)
- 新版 `00865af8`（命令位置の公開資料なし） · `00865b04`（命令位置の公開資料なし） · `00865b14`（命令位置の公開資料なし）

~~~diff
- 00865aa0 ["INT_ADD", "register:40f0:8", ["const:865aa0:8", "const:4:8"]]
- 00865aa0 ["CALL", null, ["local:b0:8"]]
+ 00865af8 ["INT_ADD", "register:40f0:8", ["const:865af8:8", "const:4:8"]]
+ 00865af8 ["CALL", null, ["local:b0:8"]]
- 00865aa0 bytes f9ffff97
+ 00865af8 bytes f9ffff97
- 00865aac ["INT_ADD", "register:40f0:8", ["const:865aac:8", "const:4:8"]]
- 00865aac ["CALL", null, ["local:b0:8"]]
+ 00865b04 ["INT_ADD", "register:40f0:8", ["const:865b04:8", "const:4:8"]]
+ 00865b04 ["CALL", null, ["local:b0:8"]]
- 00865aac bytes f6ffff97
+ 00865b04 bytes f6ffff97
- 00865abc ["INT_ADD", "register:40f0:8", ["const:865abc:8", "const:4:8"]]
- 00865abc ["CALL", null, ["callee:00c57f80:8"]]
+ 00865b14 ["INT_ADD", "register:40f0:8", ["const:865b14:8", "const:4:8"]]
+ 00865b14 ["CALL", null, ["callee:00c57f80:8"]]
- 00865abc bytes fdc80f94
+ 00865b14 bytes 1bc90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e3ea56e12e08406596af7793e3e968f"></a>

### [`00865ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md) → [`00865d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865d00.md) FUN_00865d00

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) · 呼出先 5件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00630ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630ba4.md) [`00652ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652ccc.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md) · 呼出先 5件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00630be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00630/00630be4.md) [`00652d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md#insn-00865cc8) · [`00865cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md#insn-00865cd4) · [`00865d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865ca8.md#insn-00865d10)
- 新版 `00865d20`（命令位置の公開資料なし） · `00865d2c`（命令位置の公開資料なし） · `00865d68`（命令位置の公開資料なし）

~~~diff
- 00865cc8 ["INT_ADD", "register:40f0:8", ["const:865cc8:8", "const:4:8"]]
- 00865cc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00865d20 ["INT_ADD", "register:40f0:8", ["const:865d20:8", "const:4:8"]]
+ 00865d20 ["CALL", null, ["callee:00c57f80:8"]]
- 00865cc8 bytes 7ac80f94
+ 00865d20 bytes 98c80f94
- 00865cd4 ["INT_ADD", "register:40f0:8", ["const:865cd4:8", "const:4:8"]]
- 00865cd4 ["CALL", null, ["callee:00630be4:8"]]
+ 00865d2c ["INT_ADD", "register:40f0:8", ["const:865d2c:8", "const:4:8"]]
+ 00865d2c ["CALL", null, ["callee:00630be4:8"]]
- 00865cd4 bytes b42bf797
+ 00865d2c bytes ae2bf797
- 00865d10 ["INT_ADD", "register:40f0:8", ["const:865d10:8", "const:4:8"]]
- 00865d10 ["CALL", null, ["callee:00c57f80:8"]]
+ 00865d68 ["INT_ADD", "register:40f0:8", ["const:865d68:8", "const:4:8"]]
+ 00865d68 ["CALL", null, ["callee:00c57f80:8"]]
- 00865d10 bytes 68c80f94
+ 00865d68 bytes 86c80f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b0946cfa880941ada6bb319cebaf09"></a>

### [`00865da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865da4.md) → [`00865dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865dfc.md) FUN_00865dfc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865da4.md#insn-00865dec) · [`00865dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865da4.md#insn-00865dfc) · [`00865e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865da4.md#insn-00865e0c)
- 新版 `00865e44`（命令位置の公開資料なし） · `00865e54`（命令位置の公開資料なし） · `00865e64`（命令位置の公開資料なし）

~~~diff
- 00865dec ["INT_ADD", "register:40f0:8", ["const:865dec:8", "const:4:8"]]
- 00865dec ["CALL", null, ["callee:00c57f80:8"]]
+ 00865e44 ["INT_ADD", "register:40f0:8", ["const:865e44:8", "const:4:8"]]
+ 00865e44 ["CALL", null, ["callee:00c57f80:8"]]
- 00865dec bytes 31c80f94
+ 00865e44 bytes 4fc80f94
- 00865dfc ["INT_ADD", "register:40f0:8", ["const:865dfc:8", "const:4:8"]]
- 00865dfc ["CALL", null, ["callee:00c57f80:8"]]
+ 00865e54 ["INT_ADD", "register:40f0:8", ["const:865e54:8", "const:4:8"]]
+ 00865e54 ["CALL", null, ["callee:00c57f80:8"]]
- 00865dfc bytes 2dc80f94
+ 00865e54 bytes 4bc80f94
- 00865e0c ["INT_ADD", "register:40f0:8", ["const:865e0c:8", "const:4:8"]]
- 00865e0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00865e64 ["INT_ADD", "register:40f0:8", ["const:865e64:8", "const:4:8"]]
+ 00865e64 ["CALL", null, ["callee:00c57f80:8"]]
- 00865e0c bytes 29c80f94
+ 00865e64 bytes 47c80f94
~~~


<a id="compare-69b577aecf575266dcc53b7ffd2f5470"></a>

### [`00865e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865e3c.md) → [`00865e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865e94.md) FUN_00865e94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)
- 新版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865e3c.md#insn-00865eb0) · [`00865eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865e3c.md#insn-00865eb8) · [`00865ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865e3c.md#insn-00865ec4)
- 新版 `00865f08`（命令位置の公開資料なし） · `00865f10`（命令位置の公開資料なし） · `00865f1c`（命令位置の公開資料なし）

~~~diff
- 00865eb0 ["INT_ADD", "register:40f0:8", ["const:865eb0:8", "const:4:8"]]
- 00865eb0 ["CALL", null, ["callee:0046ef38:8"]]
+ 00865f08 ["INT_ADD", "register:40f0:8", ["const:865f08:8", "const:4:8"]]
+ 00865f08 ["CALL", null, ["callee:0046ef38:8"]]
- 00865eb0 bytes 1224f097
+ 00865f08 bytes 0c24f097
- 00865eb8 ["INT_ADD", "register:40f0:8", ["const:865eb8:8", "const:4:8"]]
- 00865eb8 ["CALL", null, ["callee:0046e804:8"]]
+ 00865f10 ["INT_ADD", "register:40f0:8", ["const:865f10:8", "const:4:8"]]
+ 00865f10 ["CALL", null, ["callee:0046e804:8"]]
- 00865eb8 bytes 4322f097
+ 00865f10 bytes 3d22f097
- 00865ec4 ["INT_ADD", "register:40f0:8", ["const:865ec4:8", "const:4:8"]]
- 00865ec4 ["CALL", null, ["callee:0046e804:8"]]
+ 00865f1c ["INT_ADD", "register:40f0:8", ["const:865f1c:8", "const:4:8"]]
+ 00865f1c ["CALL", null, ["callee:0046e804:8"]]
- 00865ec4 bytes 4022f097
+ 00865f1c bytes 3a22f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936a6e32e560a424d4fae41359cb4bff"></a>

### [`00865fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865fd4.md) → [`0086602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/0086602c.md) FUN_0086602c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00865fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865fd4.md#insn-00865fe8) · [`00865ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865fd4.md#insn-00865ff0) · [`00865ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865fd4.md#insn-00865ff8)
- 新版 `00866040`（命令位置の公開資料なし） · `00866048`（命令位置の公開資料なし） · `00866050`（命令位置の公開資料なし）

~~~diff
- 00865fe8 ["INT_ADD", "register:40f0:8", ["const:865fe8:8", "const:4:8"]]
- 00865fe8 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00866040 ["INT_ADD", "register:40f0:8", ["const:866040:8", "const:4:8"]]
+ 00866040 ["CALL", null, ["callee:0046e8e4:8"]]
- 00865fe8 bytes 2f22f097
+ 00866040 bytes 2922f097
- 00865ff0 ["INT_ADD", "register:40f0:8", ["const:865ff0:8", "const:4:8"]]
- 00865ff0 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00866048 ["INT_ADD", "register:40f0:8", ["const:866048:8", "const:4:8"]]
+ 00866048 ["CALL", null, ["callee:0046e8e4:8"]]
- 00865ff0 bytes 2d22f097
+ 00866048 bytes 2722f097
- 00865ff8 ["INT_ADD", "register:40f0:8", ["const:865ff8:8", "const:4:8"]]
- 00865ff8 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00866050 ["INT_ADD", "register:40f0:8", ["const:866050:8", "const:4:8"]]
+ 00866050 ["CALL", null, ["callee:0046e8e4:8"]]
- 00865ff8 bytes 2b22f097
+ 00866050 bytes 2522f097
~~~


<a id="compare-bb452418aebe98d9b4237028a1508ade"></a>

### [`0086600c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/0086600c.md) → [`00866064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866064.md) FUN_00866064

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/0086600c.md#insn-0086602c) · [`00866040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/0086600c.md#insn-00866040) · [`00866048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/0086600c.md#insn-00866048)
- 新版 `00866084`（命令位置の公開資料なし） · `00866098`（命令位置の公開資料なし） · `008660a0`（命令位置の公開資料なし）

~~~diff
- 0086602c ["INT_ADD", "register:40f0:8", ["const:86602c:8", "const:4:8"]]
- 0086602c ["CALL", null, ["callee:00c53da0:8"]]
+ 00866084 ["INT_ADD", "register:40f0:8", ["const:866084:8", "const:4:8"]]
+ 00866084 ["CALL", null, ["callee:00c53da0:8"]]
- 0086602c bytes 35b70f94
+ 00866084 bytes 47b70f94
- 00866040 ["COPY", "register:0:8", ["register:4040:8"]]
- 00866040 ["INT_ADD", "register:40f0:8", ["const:866040:8", "const:4:8"]]
- 00866040 ["CALLIND", null, ["register:0:8"]]
+ 00866098 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00866098 ["INT_ADD", "register:40f0:8", ["const:866098:8", "const:4:8"]]
+ 00866098 ["CALLIND", null, ["register:0:8"]]
- 00866040 bytes 00013fd6
+ 00866098 bytes 00013fd6
- 00866048 ["INT_ADD", "register:40f0:8", ["const:866048:8", "const:4:8"]]
- 00866048 ["CALL", null, ["callee:00c57f50:8"]]
+ 008660a0 ["INT_ADD", "register:40f0:8", ["const:8660a0:8", "const:4:8"]]
+ 008660a0 ["CALL", null, ["callee:00c57f50:8"]]
- 00866048 bytes 8ec70f94
+ 008660a0 bytes acc70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-332da808196f374116df118154f20b4d"></a>

### [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) → [`00866154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866154.md) FUN_00866154

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 5件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md) [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md)
- 新版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 5件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`0086776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/0086776c.md) [`00867944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md) [`00867a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867a60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086615c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md#insn-0086615c) · [`00866168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md#insn-00866168) · [`00866174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md#insn-00866174)
- 新版 `008661b4`（命令位置の公開資料なし） · `008661c0`（命令位置の公開資料なし） · `008661cc`（命令位置の公開資料なし）

~~~diff
- 0086615c ["INT_ADD", "register:40f0:8", ["const:86615c:8", "const:4:8"]]
- 0086615c ["CALL", null, ["callee:0046ef38:8"]]
+ 008661b4 ["INT_ADD", "register:40f0:8", ["const:8661b4:8", "const:4:8"]]
+ 008661b4 ["CALL", null, ["callee:0046ef38:8"]]
- 0086615c bytes 6723f097
+ 008661b4 bytes 6123f097
- 00866168 ["INT_ADD", "register:40f0:8", ["const:866168:8", "const:4:8"]]
- 00866168 ["CALL", null, ["callee:0046ef38:8"]]
+ 008661c0 ["INT_ADD", "register:40f0:8", ["const:8661c0:8", "const:4:8"]]
+ 008661c0 ["CALL", null, ["callee:0046ef38:8"]]
- 00866168 bytes 6423f097
+ 008661c0 bytes 5e23f097
- 00866174 ["INT_ADD", "register:40f0:8", ["const:866174:8", "const:4:8"]]
- 00866174 ["CALL", null, ["callee:0046ef38:8"]]
+ 008661cc ["INT_ADD", "register:40f0:8", ["const:8661cc:8", "const:4:8"]]
+ 008661cc ["CALL", null, ["callee:0046ef38:8"]]
- 00866174 bytes 6123f097
+ 008661cc bytes 5b23f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c7ff9dbeefe3bdbad32725dbc4efb18"></a>

### [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) → [`00866ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md) FUN_00866ac4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 4件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) [`00867f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md)
- 新版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 4件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`0086776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/0086776c.md) [`00867fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867fb4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00866aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md#insn-00866aec) · [`00866af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md#insn-00866af4) · [`00866bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md#insn-00866bf4)
- 新版 `00866b44`（命令位置の公開資料なし） · `00866b4c`（命令位置の公開資料なし） · `00866c4c`（命令位置の公開資料なし）

~~~diff
- 00866aec ["INT_ADD", "register:40f0:8", ["const:866aec:8", "const:4:8"]]
- 00866aec ["CALL", null, ["callee:0086776c:8"]]
+ 00866b44 ["INT_ADD", "register:40f0:8", ["const:866b44:8", "const:4:8"]]
+ 00866b44 ["CALL", null, ["callee:0086776c:8"]]
- 00866aec bytes 0a030094
+ 00866b44 bytes 0a030094
- 00866af4 ["INT_ADD", "register:40f0:8", ["const:866af4:8", "const:4:8"]]
- 00866af4 ["CALL", null, ["callee:00867fb4:8"]]
+ 00866b4c ["INT_ADD", "register:40f0:8", ["const:866b4c:8", "const:4:8"]]
+ 00866b4c ["CALL", null, ["callee:00867fb4:8"]]
- 00866af4 bytes 1a050094
+ 00866b4c bytes 1a050094
- 00866bf4 ["INT_ADD", "register:40f0:8", ["const:866bf4:8", "const:4:8"]]
- 00866bf4 ["CALL", null, ["callee:0046ef38:8"]]
+ 00866c4c ["INT_ADD", "register:40f0:8", ["const:866c4c:8", "const:4:8"]]
+ 00866c4c ["CALL", null, ["callee:0046ef38:8"]]
- 00866bf4 bytes c120f097
+ 00866c4c bytes bb20f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e08ab05c44e36bae2d5983828558b9"></a>

### [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) → [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) FUN_00866da0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 17件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005b9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9ee4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)
- 新版 呼出元 1件 [`00846ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md) · 呼出先 17件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`005b9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9f24.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00866d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md#insn-00866d68) · [`00866d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md#insn-00866d7c) · [`00866d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md#insn-00866d90)
- 新版 `00866dc0`（命令位置の公開資料なし） · `00866dd4`（命令位置の公開資料なし） · `00866de8`（命令位置の公開資料なし）

~~~diff
- 00866d68 ["INT_ADD", "register:40f0:8", ["const:866d68:8", "const:4:8"]]
- 00866d68 ["CALL", null, ["callee:005c3ebc:8"]]
+ 00866dc0 ["INT_ADD", "register:40f0:8", ["const:866dc0:8", "const:4:8"]]
+ 00866dc0 ["CALL", null, ["callee:005c3ebc:8"]]
- 00866d68 bytes 4574f597
+ 00866dc0 bytes 3f74f597
- 00866d7c ["INT_ADD", "register:40f0:8", ["const:866d7c:8", "const:4:8"]]
- 00866d7c ["CALL", null, ["callee:00c53da0:8"]]
+ 00866dd4 ["INT_ADD", "register:40f0:8", ["const:866dd4:8", "const:4:8"]]
+ 00866dd4 ["CALL", null, ["callee:00c53da0:8"]]
- 00866d7c bytes e1b30f94
+ 00866dd4 bytes f3b30f94
- 00866d90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00866d90 ["INT_ADD", "register:40f0:8", ["const:866d90:8", "const:4:8"]]
- 00866d90 ["CALLIND", null, ["register:0:8"]]
+ 00866de8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00866de8 ["INT_ADD", "register:40f0:8", ["const:866de8:8", "const:4:8"]]
+ 00866de8 ["CALLIND", null, ["register:0:8"]]
- 00866d90 bytes 00013fd6
+ 00866de8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e82501593ac36f0e1a76081b4b618285"></a>

### [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) → [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) FUN_008670c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 17件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)
- 新版 呼出元 1件 [`00846ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md) · 呼出先 17件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md#insn-00867088) · [`008670a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md#insn-008670a0) · [`008670b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md#insn-008670b4)
- 新版 `008670e0`（命令位置の公開資料なし） · `008670f8`（命令位置の公開資料なし） · `0086710c`（命令位置の公開資料なし）

~~~diff
- 00867088 ["INT_ADD", "register:40f0:8", ["const:867088:8", "const:4:8"]]
- 00867088 ["CALL", null, ["callee:00c57f80:8"]]
+ 008670e0 ["INT_ADD", "register:40f0:8", ["const:8670e0:8", "const:4:8"]]
+ 008670e0 ["CALL", null, ["callee:00c57f80:8"]]
- 00867088 bytes 8ac30f94
+ 008670e0 bytes a8c30f94
- 008670a0 ["INT_ADD", "register:40f0:8", ["const:8670a0:8", "const:4:8"]]
- 008670a0 ["CALL", null, ["callee:00c53da0:8"]]
+ 008670f8 ["INT_ADD", "register:40f0:8", ["const:8670f8:8", "const:4:8"]]
+ 008670f8 ["CALL", null, ["callee:00c53da0:8"]]
- 008670a0 bytes 18b30f94
+ 008670f8 bytes 2ab30f94
- 008670b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008670b4 ["INT_ADD", "register:40f0:8", ["const:8670b4:8", "const:4:8"]]
- 008670b4 ["CALLIND", null, ["register:0:8"]]
+ 0086710c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086710c ["INT_ADD", "register:40f0:8", ["const:86710c:8", "const:4:8"]]
+ 0086710c ["CALLIND", null, ["register:0:8"]]
- 008670b4 bytes 00013fd6
+ 0086710c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f1e4c9250b84573bc7414b426f6535"></a>

### [`00867714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md) → [`0086776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/0086776c.md) FUN_0086776c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)
- 新版 呼出元 2件 [`00866154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866154.md) [`00866ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md#insn-00867740) · [`00867748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md#insn-00867748) · [`00867754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867714.md#insn-00867754)
- 新版 `00867798`（命令位置の公開資料なし） · `008677a0`（命令位置の公開資料なし） · `008677ac`（命令位置の公開資料なし）

~~~diff
- 00867740 ["INT_ADD", "register:40f0:8", ["const:867740:8", "const:4:8"]]
- 00867740 ["CALL", null, ["callee:0046ef38:8"]]
+ 00867798 ["INT_ADD", "register:40f0:8", ["const:867798:8", "const:4:8"]]
+ 00867798 ["CALL", null, ["callee:0046ef38:8"]]
- 00867740 bytes ee1df097
+ 00867798 bytes e81df097
- 00867748 ["INT_ADD", "register:40f0:8", ["const:867748:8", "const:4:8"]]
- 00867748 ["CALL", null, ["callee:0046e804:8"]]
+ 008677a0 ["INT_ADD", "register:40f0:8", ["const:8677a0:8", "const:4:8"]]
+ 008677a0 ["CALL", null, ["callee:0046e804:8"]]
- 00867748 bytes 1f1cf097
+ 008677a0 bytes 191cf097
- 00867754 ["INT_ADD", "register:40f0:8", ["const:867754:8", "const:4:8"]]
- 00867754 ["CALL", null, ["callee:0046e804:8"]]
+ 008677ac ["INT_ADD", "register:40f0:8", ["const:8677ac:8", "const:4:8"]]
+ 008677ac ["CALL", null, ["callee:0046e804:8"]]
- 00867754 bytes 1c1cf097
+ 008677ac bytes 161cf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe805dfe07aabc9eace16cbc5c27bb71"></a>

### [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md) → [`00867944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md) FUN_00867944

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md) · 呼出先 2件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md)
- 新版 呼出元 2件 [`00866154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866154.md) [`00867a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867a60.md) · 呼出先 2件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md#insn-00867918) · [`00867920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md#insn-00867920) · [`0086792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md#insn-0086792c)
- 新版 `00867970`（命令位置の公開資料なし） · `00867978`（命令位置の公開資料なし） · `00867984`（命令位置の公開資料なし）

~~~diff
- 00867918 ["INT_ADD", "register:40f0:8", ["const:867918:8", "const:4:8"]]
- 00867918 ["CALL", null, ["callee:0046ef38:8"]]
+ 00867970 ["INT_ADD", "register:40f0:8", ["const:867970:8", "const:4:8"]]
+ 00867970 ["CALL", null, ["callee:0046ef38:8"]]
- 00867918 bytes 781df097
+ 00867970 bytes 721df097
- 00867920 ["INT_ADD", "register:40f0:8", ["const:867920:8", "const:4:8"]]
- 00867920 ["CALL", null, ["callee:0046e804:8"]]
+ 00867978 ["INT_ADD", "register:40f0:8", ["const:867978:8", "const:4:8"]]
+ 00867978 ["CALL", null, ["callee:0046e804:8"]]
- 00867920 bytes a91bf097
+ 00867978 bytes a31bf097
- 0086792c ["INT_ADD", "register:40f0:8", ["const:86792c:8", "const:4:8"]]
- 0086792c ["CALL", null, ["callee:0046e804:8"]]
+ 00867984 ["INT_ADD", "register:40f0:8", ["const:867984:8", "const:4:8"]]
+ 00867984 ["CALL", null, ["callee:0046e804:8"]]
- 0086792c bytes a61bf097
+ 00867984 bytes a01bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90ed02c6ba3d57447f299ab7cdfca85a"></a>

### [`00867a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md) → [`00867a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867a60.md) FUN_00867a60

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008660fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/008660fc.md) · 呼出先 3件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`008678ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/008678ec.md)
- 新版 呼出元 1件 [`00866154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866154.md) · 呼出先 3件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`00867944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867944.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md#insn-00867a20) · [`00867a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md#insn-00867a38) · [`00867a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867a08.md#insn-00867a40)
- 新版 `00867a78`（命令位置の公開資料なし） · `00867a90`（命令位置の公開資料なし） · `00867a98`（命令位置の公開資料なし）

~~~diff
- 00867a20 ["INT_ADD", "register:40f0:8", ["const:867a20:8", "const:4:8"]]
- 00867a20 ["CALL", null, ["callee:00867944:8"]]
+ 00867a78 ["INT_ADD", "register:40f0:8", ["const:867a78:8", "const:4:8"]]
+ 00867a78 ["CALL", null, ["callee:00867944:8"]]
- 00867a20 bytes b3ffff97
+ 00867a78 bytes b3ffff97
- 00867a38 ["INT_ADD", "register:40f0:8", ["const:867a38:8", "const:4:8"]]
- 00867a38 ["CALL", null, ["callee:0046ef38:8"]]
+ 00867a90 ["INT_ADD", "register:40f0:8", ["const:867a90:8", "const:4:8"]]
+ 00867a90 ["CALL", null, ["callee:0046ef38:8"]]
- 00867a38 bytes 301df097
+ 00867a90 bytes 2a1df097
- 00867a40 ["INT_ADD", "register:40f0:8", ["const:867a40:8", "const:4:8"]]
- 00867a40 ["CALL", null, ["callee:0046e804:8"]]
+ 00867a98 ["INT_ADD", "register:40f0:8", ["const:867a98:8", "const:4:8"]]
+ 00867a98 ["CALL", null, ["callee:0046e804:8"]]
- 00867a40 bytes 611bf097
+ 00867a98 bytes 5b1bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f35746fd8a50035b17fdd724943c1a"></a>

### [`00867b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867b58.md) → [`00867bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867bb0.md) FUN_00867bb0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 3件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) · 呼出先 3件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867b58.md#insn-00867b94) · [`00867b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867b58.md#insn-00867b9c) · [`00867bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867b58.md#insn-00867bcc)
- 新版 `00867bec`（命令位置の公開資料なし） · `00867bf4`（命令位置の公開資料なし） · `00867c24`（命令位置の公開資料なし）

~~~diff
- 00867b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00867b94 ["INT_ADD", "register:40f0:8", ["const:867b94:8", "const:4:8"]]
- 00867b94 ["CALLIND", null, ["register:0:8"]]
+ 00867bec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00867bec ["INT_ADD", "register:40f0:8", ["const:867bec:8", "const:4:8"]]
+ 00867bec ["CALLIND", null, ["register:0:8"]]
- 00867b94 bytes 00013fd6
+ 00867bec bytes 00013fd6
- 00867b9c ["INT_ADD", "register:40f0:8", ["const:867b9c:8", "const:4:8"]]
- 00867b9c ["CALL", null, ["callee:0067e628:8"]]
+ 00867bf4 ["INT_ADD", "register:40f0:8", ["const:867bf4:8", "const:4:8"]]
+ 00867bf4 ["CALL", null, ["callee:0067e628:8"]]
- 00867b9c bytes 935af897
+ 00867bf4 bytes 8d5af897
- 00867bcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00867bcc ["INT_ADD", "register:40f0:8", ["const:867bcc:8", "const:4:8"]]
- 00867bcc ["CALLIND", null, ["register:0:8"]]
+ 00867c24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00867c24 ["INT_ADD", "register:40f0:8", ["const:867c24:8", "const:4:8"]]
+ 00867c24 ["CALLIND", null, ["register:0:8"]]
- 00867bcc bytes 00013fd6
+ 00867c24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7047df9857798755c241aa087429174"></a>

### [`00867c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md) → [`00867ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867ce4.md) FUN_00867ce4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00867df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) · 呼出先 6件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00867e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867e50.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md#insn-00867cc0) · [`00867cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md#insn-00867cc8) · [`00867cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md#insn-00867cd0)
- 新版 `00867d18`（命令位置の公開資料なし） · `00867d20`（命令位置の公開資料なし） · `00867d28`（命令位置の公開資料なし）

~~~diff
- 00867cc0 ["INT_ADD", "register:40f0:8", ["const:867cc0:8", "const:4:8"]]
- 00867cc0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00867d18 ["INT_ADD", "register:40f0:8", ["const:867d18:8", "const:4:8"]]
+ 00867d18 ["CALL", null, ["callee:00c57f80:8"]]
- 00867cc0 bytes 7cc00f94
+ 00867d18 bytes 9ac00f94
- 00867cc8 ["INT_ADD", "register:40f0:8", ["const:867cc8:8", "const:4:8"]]
- 00867cc8 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00867d20 ["INT_ADD", "register:40f0:8", ["const:867d20:8", "const:4:8"]]
+ 00867d20 ["CALL", null, ["callee:0046e8e4:8"]]
- 00867cc8 bytes f71af097
+ 00867d20 bytes f11af097
- 00867cd0 ["INT_ADD", "register:40f0:8", ["const:867cd0:8", "const:4:8"]]
- 00867cd0 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00867d28 ["INT_ADD", "register:40f0:8", ["const:867d28:8", "const:4:8"]]
+ 00867d28 ["CALL", null, ["callee:0046e8e4:8"]]
- 00867cd0 bytes f51af097
+ 00867d28 bytes ef1af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba93508e50444539a11432bdd1277fcc"></a>

### [`00867df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md) → [`00867e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867e50.md) FUN_00867e50

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00867c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867c8c.md) · 呼出先 4件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) [`00867ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867ce4.md) · 呼出先 4件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md#insn-00867e0c) · [`00867e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md#insn-00867e14) · [`00867e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867df8.md#insn-00867e1c)
- 新版 `00867e64`（命令位置の公開資料なし） · `00867e6c`（命令位置の公開資料なし） · `00867e74`（命令位置の公開資料なし）

~~~diff
- 00867e0c ["INT_ADD", "register:40f0:8", ["const:867e0c:8", "const:4:8"]]
- 00867e0c ["CALL", null, ["callee:0046e8e4:8"]]
+ 00867e64 ["INT_ADD", "register:40f0:8", ["const:867e64:8", "const:4:8"]]
+ 00867e64 ["CALL", null, ["callee:0046e8e4:8"]]
- 00867e0c bytes a61af097
+ 00867e64 bytes a01af097
- 00867e14 ["INT_ADD", "register:40f0:8", ["const:867e14:8", "const:4:8"]]
- 00867e14 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00867e6c ["INT_ADD", "register:40f0:8", ["const:867e6c:8", "const:4:8"]]
+ 00867e6c ["CALL", null, ["callee:0046e8e4:8"]]
- 00867e14 bytes a41af097
+ 00867e6c bytes 9e1af097
- 00867e1c ["INT_ADD", "register:40f0:8", ["const:867e1c:8", "const:4:8"]]
- 00867e1c ["CALL", null, ["callee:0046e8e4:8"]]
+ 00867e74 ["INT_ADD", "register:40f0:8", ["const:867e74:8", "const:4:8"]]
+ 00867e74 ["CALL", null, ["callee:0046e8e4:8"]]
- 00867e1c bytes a21af097
+ 00867e74 bytes 9c1af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc518bd1639c1f7f1bc20beb4850ec03"></a>

### [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) → [`00867f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867f70.md) FUN_00867f70

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) [`00b13030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md) · 呼出先 2件 [`00867f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) [`00867f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867f70.md) [`00b130cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b130cc.md) · 呼出先 2件 [`00867f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md#insn-00867f38) · [`00867f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f18.md#insn-00867f44)
- 新版 `00867f90`（命令位置の公開資料なし） · `00867f9c`（命令位置の公開資料なし）

~~~diff
- 00867f38 ["INT_ADD", "register:40f0:8", ["const:867f38:8", "const:4:8"]]
- 00867f38 ["CALL", null, ["local:b0:8"]]
+ 00867f90 ["INT_ADD", "register:40f0:8", ["const:867f90:8", "const:4:8"]]
+ 00867f90 ["CALL", null, ["local:b0:8"]]
- 00867f38 bytes f8ffff97
+ 00867f90 bytes f8ffff97
- 00867f44 ["INT_ADD", "register:40f0:8", ["const:867f44:8", "const:4:8"]]
- 00867f44 ["CALL", null, ["local:b0:8"]]
+ 00867f9c ["INT_ADD", "register:40f0:8", ["const:867f9c:8", "const:4:8"]]
+ 00867f9c ["CALL", null, ["local:b0:8"]]
- 00867f44 bytes f5ffff97
+ 00867f9c bytes f5ffff97
~~~


<a id="compare-6a79a21c7dfcc11d967616205a18cf1a"></a>

### [`00867f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md) → [`00867fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/00867fb4.md) FUN_00867fb4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00866a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866a6c.md) · 呼出先 3件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)
- 新版 呼出元 1件 [`00866ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866ac4.md) · 呼出先 3件 [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00867f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md#insn-00867f84) · [`00867f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md#insn-00867f9c) · [`00867fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867f5c.md#insn-00867fa4)
- 新版 `00867fdc`（命令位置の公開資料なし） · `00867ff4`（命令位置の公開資料なし） · `00867ffc`（命令位置の公開資料なし）

~~~diff
- 00867f84 ["INT_ADD", "register:40f0:8", ["const:867f84:8", "const:4:8"]]
- 00867f84 ["CALL", null, ["callee:005e81d8:8"]]
+ 00867fdc ["INT_ADD", "register:40f0:8", ["const:867fdc:8", "const:4:8"]]
+ 00867fdc ["CALL", null, ["callee:005e81d8:8"]]
- 00867f84 bytes 8500f697
+ 00867fdc bytes 7f00f697
- 00867f9c ["INT_ADD", "register:40f0:8", ["const:867f9c:8", "const:4:8"]]
- 00867f9c ["CALL", null, ["callee:0046ef38:8"]]
+ 00867ff4 ["INT_ADD", "register:40f0:8", ["const:867ff4:8", "const:4:8"]]
+ 00867ff4 ["CALL", null, ["callee:0046ef38:8"]]
- 00867f9c bytes d71bf097
+ 00867ff4 bytes d11bf097
- 00867fa4 ["INT_ADD", "register:40f0:8", ["const:867fa4:8", "const:4:8"]]
- 00867fa4 ["CALL", null, ["callee:0046e804:8"]]
+ 00867ffc ["INT_ADD", "register:40f0:8", ["const:867ffc:8", "const:4:8"]]
+ 00867ffc ["CALL", null, ["callee:0046e804:8"]]
- 00867fa4 bytes 081af097
+ 00867ffc bytes 021af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6edf60b1877df5e1cf188b6ccde97082"></a>

### [`008680c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008680c4.md) → [`0086811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/0086811c.md) FUN_0086811c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 3件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) · 呼出先 3件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008680c4.md#insn-00868100) · [`00868108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008680c4.md#insn-00868108) · [`00868138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008680c4.md#insn-00868138)
- 新版 `00868158`（命令位置の公開資料なし） · `00868160`（命令位置の公開資料なし） · `00868190`（命令位置の公開資料なし）

~~~diff
- 00868100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868100 ["INT_ADD", "register:40f0:8", ["const:868100:8", "const:4:8"]]
- 00868100 ["CALLIND", null, ["register:0:8"]]
+ 00868158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868158 ["INT_ADD", "register:40f0:8", ["const:868158:8", "const:4:8"]]
+ 00868158 ["CALLIND", null, ["register:0:8"]]
- 00868100 bytes 00013fd6
+ 00868158 bytes 00013fd6
- 00868108 ["INT_ADD", "register:40f0:8", ["const:868108:8", "const:4:8"]]
- 00868108 ["CALL", null, ["callee:0067e628:8"]]
+ 00868160 ["INT_ADD", "register:40f0:8", ["const:868160:8", "const:4:8"]]
+ 00868160 ["CALL", null, ["callee:0067e628:8"]]
- 00868108 bytes 3859f897
+ 00868160 bytes 3259f897
- 00868138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868138 ["INT_ADD", "register:40f0:8", ["const:868138:8", "const:4:8"]]
- 00868138 ["CALLIND", null, ["register:0:8"]]
+ 00868190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868190 ["INT_ADD", "register:40f0:8", ["const:868190:8", "const:4:8"]]
+ 00868190 ["CALLIND", null, ["register:0:8"]]
- 00868138 bytes 00013fd6
+ 00868190 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d20ebb872fb84927cf8688c6a574662"></a>

### [`00868234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md) → [`0086828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/0086828c.md) FUN_0086828c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 3件 [`008686d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) · 呼出先 3件 [`00868730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md#insn-00868254) · [`00868268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md#insn-00868268) · [`00868270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md#insn-00868270)
- 新版 `008682ac`（命令位置の公開資料なし） · `008682c0`（命令位置の公開資料なし） · `008682c8`（命令位置の公開資料なし）

~~~diff
- 00868254 ["INT_ADD", "register:40f0:8", ["const:868254:8", "const:4:8"]]
- 00868254 ["CALL", null, ["callee:00c53da0:8"]]
+ 008682ac ["INT_ADD", "register:40f0:8", ["const:8682ac:8", "const:4:8"]]
+ 008682ac ["CALL", null, ["callee:00c53da0:8"]]
- 00868254 bytes abae0f94
+ 008682ac bytes bdae0f94
- 00868268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868268 ["INT_ADD", "register:40f0:8", ["const:868268:8", "const:4:8"]]
- 00868268 ["CALLIND", null, ["register:0:8"]]
+ 008682c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008682c0 ["INT_ADD", "register:40f0:8", ["const:8682c0:8", "const:4:8"]]
+ 008682c0 ["CALLIND", null, ["register:0:8"]]
- 00868268 bytes 00013fd6
+ 008682c0 bytes 00013fd6
- 00868270 ["INT_ADD", "register:40f0:8", ["const:868270:8", "const:4:8"]]
- 00868270 ["CALL", null, ["callee:00c57f50:8"]]
+ 008682c8 ["INT_ADD", "register:40f0:8", ["const:8682c8:8", "const:4:8"]]
+ 008682c8 ["CALL", null, ["callee:00c57f50:8"]]
- 00868270 bytes 04bf0f94
+ 008682c8 bytes 22bf0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6375cfcf976206d6c13df410b4c8ac"></a>

### [`008683bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008683bc.md) → [`00868414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868414.md) FUN_00868414

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) · 呼出先 5件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) · 呼出先 5件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008683d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008683bc.md#insn-008683d0) · [`008683d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008683bc.md#insn-008683d8) · [`008683e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008683bc.md#insn-008683e0)
- 新版 `00868428`（命令位置の公開資料なし） · `00868430`（命令位置の公開資料なし） · `00868438`（命令位置の公開資料なし）

~~~diff
- 008683d0 ["INT_ADD", "register:40f0:8", ["const:8683d0:8", "const:4:8"]]
- 008683d0 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00868428 ["INT_ADD", "register:40f0:8", ["const:868428:8", "const:4:8"]]
+ 00868428 ["CALL", null, ["callee:0046e8e4:8"]]
- 008683d0 bytes 3519f097
+ 00868428 bytes 2f19f097
- 008683d8 ["INT_ADD", "register:40f0:8", ["const:8683d8:8", "const:4:8"]]
- 008683d8 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00868430 ["INT_ADD", "register:40f0:8", ["const:868430:8", "const:4:8"]]
+ 00868430 ["CALL", null, ["callee:0046e8e4:8"]]
- 008683d8 bytes 3319f097
+ 00868430 bytes 2d19f097
- 008683e0 ["INT_ADD", "register:40f0:8", ["const:8683e0:8", "const:4:8"]]
- 008683e0 ["CALL", null, ["callee:0046e8e4:8"]]
+ 00868438 ["INT_ADD", "register:40f0:8", ["const:868438:8", "const:4:8"]]
+ 00868438 ["CALL", null, ["callee:0046e8e4:8"]]
- 008683e0 bytes 3119f097
+ 00868438 bytes 2b19f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f3922003cf0098ab4897db4091db14"></a>

### [`008684f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008684f0.md) → [`00868548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868548.md) FUN_00868548

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) · 呼出先 4件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) · 呼出先 4件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008684f0.md#insn-00868504) · [`0086850c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008684f0.md#insn-0086850c) · [`00868520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008684f0.md#insn-00868520)
- 新版 `0086855c`（命令位置の公開資料なし） · `00868564`（命令位置の公開資料なし） · `00868578`（命令位置の公開資料なし）

~~~diff
- 00868504 ["INT_ADD", "register:40f0:8", ["const:868504:8", "const:4:8"]]
- 00868504 ["CALL", null, ["callee:0046e8e4:8"]]
+ 0086855c ["INT_ADD", "register:40f0:8", ["const:86855c:8", "const:4:8"]]
+ 0086855c ["CALL", null, ["callee:0046e8e4:8"]]
- 00868504 bytes e818f097
+ 0086855c bytes e218f097
- 0086850c ["INT_ADD", "register:40f0:8", ["const:86850c:8", "const:4:8"]]
- 0086850c ["CALL", null, ["callee:0046f01c:8"]]
+ 00868564 ["INT_ADD", "register:40f0:8", ["const:868564:8", "const:4:8"]]
+ 00868564 ["CALL", null, ["callee:0046f01c:8"]]
- 0086850c bytes b41af097
+ 00868564 bytes ae1af097
- 00868520 ["INT_ADD", "register:40f0:8", ["const:868520:8", "const:4:8"]]
- 00868520 ["CALL", null, ["callee:00c53da0:8"]]
+ 00868578 ["INT_ADD", "register:40f0:8", ["const:868578:8", "const:4:8"]]
+ 00868578 ["CALL", null, ["callee:00c53da0:8"]]
- 00868520 bytes f8ad0f94
+ 00868578 bytes 0aae0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed36103a736a788dbf704640d47322d"></a>

### [`00868660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868660.md) → [`008686b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008686b8.md) FUN_008686b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008686a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868660.md#insn-008686a8)
- 新版 `00868700`（命令位置の公開資料なし）

~~~diff
- 008686a8 ["INT_ADD", "register:40f0:8", ["const:8686a8:8", "const:4:8"]]
- 008686a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00868700 ["INT_ADD", "register:40f0:8", ["const:868700:8", "const:4:8"]]
+ 00868700 ["CALL", null, ["callee:00c57f80:8"]]
- 008686a8 bytes 02be0f94
+ 00868700 bytes 20be0f94
~~~


<a id="compare-5da66a3183ec4f6b0f25e82dc0098aa5"></a>

### [`008686d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md) → [`00868730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868730.md) FUN_00868730

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00868234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868234.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0086828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/0086828c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md#insn-00868724) · [`00868738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md#insn-00868738) · [`00868740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008686d8.md#insn-00868740)
- 新版 `0086877c`（命令位置の公開資料なし） · `00868790`（命令位置の公開資料なし） · `00868798`（命令位置の公開資料なし）

~~~diff
- 00868724 ["INT_ADD", "register:40f0:8", ["const:868724:8", "const:4:8"]]
- 00868724 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086877c ["INT_ADD", "register:40f0:8", ["const:86877c:8", "const:4:8"]]
+ 0086877c ["CALL", null, ["callee:00c53da0:8"]]
- 00868724 bytes 77ad0f94
+ 0086877c bytes 89ad0f94
- 00868738 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868738 ["INT_ADD", "register:40f0:8", ["const:868738:8", "const:4:8"]]
- 00868738 ["CALLIND", null, ["register:0:8"]]
+ 00868790 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868790 ["INT_ADD", "register:40f0:8", ["const:868790:8", "const:4:8"]]
+ 00868790 ["CALLIND", null, ["register:0:8"]]
- 00868738 bytes 00013fd6
+ 00868790 bytes 00013fd6
- 00868740 ["INT_ADD", "register:40f0:8", ["const:868740:8", "const:4:8"]]
- 00868740 ["CALL", null, ["callee:00c57f50:8"]]
+ 00868798 ["INT_ADD", "register:40f0:8", ["const:868798:8", "const:4:8"]]
+ 00868798 ["CALL", null, ["callee:00c57f50:8"]]
- 00868740 bytes d0bd0f94
+ 00868798 bytes eebd0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9df677fbbd2070bd812bb3a125e1d67d"></a>

### [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) → [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) FUN_00868898

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00866d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00866/00866d48.md) [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) · 呼出先 2件 [`00868840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) · 呼出先 2件 [`00868898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868898.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md#insn-00868860) · [`0086886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868840.md#insn-0086886c)
- 新版 `008688b8`（命令位置の公開資料なし） · `008688c4`（命令位置の公開資料なし）

~~~diff
- 00868860 ["INT_ADD", "register:40f0:8", ["const:868860:8", "const:4:8"]]
- 00868860 ["CALL", null, ["local:b0:8"]]
+ 008688b8 ["INT_ADD", "register:40f0:8", ["const:8688b8:8", "const:4:8"]]
+ 008688b8 ["CALL", null, ["local:b0:8"]]
- 00868860 bytes f8ffff97
+ 008688b8 bytes f8ffff97
- 0086886c ["INT_ADD", "register:40f0:8", ["const:86886c:8", "const:4:8"]]
- 0086886c ["CALL", null, ["local:b0:8"]]
+ 008688c4 ["INT_ADD", "register:40f0:8", ["const:8688c4:8", "const:4:8"]]
+ 008688c4 ["CALL", null, ["local:b0:8"]]
- 0086886c bytes f5ffff97
+ 008688c4 bytes f5ffff97
~~~


<a id="compare-f1869a5b5527a3cdf3d6d21661b1a691"></a>

### [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) → [`008688dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008688dc.md) FUN_008688dc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00867068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00867/00867068.md) [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) · 呼出先 2件 [`00868884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`008670c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00867/008670c0.md) [`008688dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008688dc.md) · 呼出先 2件 [`008688dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008688dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008688a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md#insn-008688a4) · [`008688b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868884.md#insn-008688b0)
- 新版 `008688fc`（命令位置の公開資料なし） · `00868908`（命令位置の公開資料なし）

~~~diff
- 008688a4 ["INT_ADD", "register:40f0:8", ["const:8688a4:8", "const:4:8"]]
- 008688a4 ["CALL", null, ["local:b0:8"]]
+ 008688fc ["INT_ADD", "register:40f0:8", ["const:8688fc:8", "const:4:8"]]
+ 008688fc ["CALL", null, ["local:b0:8"]]
- 008688a4 bytes f8ffff97
+ 008688fc bytes f8ffff97
- 008688b0 ["INT_ADD", "register:40f0:8", ["const:8688b0:8", "const:4:8"]]
- 008688b0 ["CALL", null, ["local:b0:8"]]
+ 00868908 ["INT_ADD", "register:40f0:8", ["const:868908:8", "const:4:8"]]
+ 00868908 ["CALL", null, ["local:b0:8"]]
- 008688b0 bytes f5ffff97
+ 00868908 bytes f5ffff97
~~~


<a id="compare-72691c02f7ee8263e5f623f553a0a46d"></a>

### [`008688c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008688c8.md) → [`00868920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868920.md) FUN_00868920

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008688c8.md#insn-00868914) · [`00868928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008688c8.md#insn-00868928) · [`00868930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008688c8.md#insn-00868930)
- 新版 `0086896c`（命令位置の公開資料なし） · `00868980`（命令位置の公開資料なし） · `00868988`（命令位置の公開資料なし）

~~~diff
- 00868914 ["INT_ADD", "register:40f0:8", ["const:868914:8", "const:4:8"]]
- 00868914 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086896c ["INT_ADD", "register:40f0:8", ["const:86896c:8", "const:4:8"]]
+ 0086896c ["CALL", null, ["callee:00c53da0:8"]]
- 00868914 bytes fbac0f94
+ 0086896c bytes 0dad0f94
- 00868928 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868928 ["INT_ADD", "register:40f0:8", ["const:868928:8", "const:4:8"]]
- 00868928 ["CALLIND", null, ["register:0:8"]]
+ 00868980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868980 ["INT_ADD", "register:40f0:8", ["const:868980:8", "const:4:8"]]
+ 00868980 ["CALLIND", null, ["register:0:8"]]
- 00868928 bytes 00013fd6
+ 00868980 bytes 00013fd6
- 00868930 ["INT_ADD", "register:40f0:8", ["const:868930:8", "const:4:8"]]
- 00868930 ["CALL", null, ["callee:00c57f50:8"]]
+ 00868988 ["INT_ADD", "register:40f0:8", ["const:868988:8", "const:4:8"]]
+ 00868988 ["CALL", null, ["callee:00c57f50:8"]]
- 00868930 bytes 54bd0f94
+ 00868988 bytes 72bd0f94
~~~


<a id="compare-d6691a1a5d4c56a3c514302b612351a5"></a>

### [`00868960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868960.md) → [`008689b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/008689b8.md) FUN_008689b8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008469a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/008469a4.md) · 呼出先 7件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006fb074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb074.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`008469fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/008469fc.md) · 呼出先 7件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006fb0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb0cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868960.md#insn-0086897c) · [`0086898c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868960.md#insn-0086898c) · [`00868998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868960.md#insn-00868998)
- 新版 `008689d4`（命令位置の公開資料なし） · `008689e4`（命令位置の公開資料なし） · `008689f0`（命令位置の公開資料なし）

~~~diff
- 0086897c ["INT_ADD", "register:40f0:8", ["const:86897c:8", "const:4:8"]]
- 0086897c ["CALL", null, ["callee:00c57f80:8"]]
+ 008689d4 ["INT_ADD", "register:40f0:8", ["const:8689d4:8", "const:4:8"]]
+ 008689d4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086897c bytes 4dbd0f94
+ 008689d4 bytes 6bbd0f94
- 0086898c ["INT_ADD", "register:40f0:8", ["const:86898c:8", "const:4:8"]]
- 0086898c ["CALL", null, ["callee:00c57f80:8"]]
+ 008689e4 ["INT_ADD", "register:40f0:8", ["const:8689e4:8", "const:4:8"]]
+ 008689e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086898c bytes 49bd0f94
+ 008689e4 bytes 67bd0f94
- 00868998 ["INT_ADD", "register:40f0:8", ["const:868998:8", "const:4:8"]]
- 00868998 ["CALL", null, ["callee:006fb0cc:8"]]
+ 008689f0 ["INT_ADD", "register:40f0:8", ["const:8689f0:8", "const:4:8"]]
+ 008689f0 ["CALL", null, ["callee:006fb0cc:8"]]
- 00868998 bytes b749fa97
+ 008689f0 bytes b749fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7549acdd1672114914ea397734539dc9"></a>

### [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) → [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) FUN_00868a50

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) · 呼出先 8件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00868ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md) [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md)
- 新版 呼出元 1件 [`00846ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md) · 呼出先 8件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00868b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md) [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md#insn-00868a14) · [`00868a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md#insn-00868a1c) · [`00868a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md#insn-00868a30)
- 新版 `00868a6c`（命令位置の公開資料なし） · `00868a74`（命令位置の公開資料なし） · `00868a88`（命令位置の公開資料なし）

~~~diff
- 00868a14 ["INT_ADD", "register:40f0:8", ["const:868a14:8", "const:4:8"]]
- 00868a14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00868a6c ["INT_ADD", "register:40f0:8", ["const:868a6c:8", "const:4:8"]]
+ 00868a6c ["CALL", null, ["callee:00c57f80:8"]]
- 00868a14 bytes 27bd0f94
+ 00868a6c bytes 45bd0f94
- 00868a1c ["INT_ADD", "register:40f0:8", ["const:868a1c:8", "const:4:8"]]
- 00868a1c ["CALL", null, ["callee:00868b18:8"]]
+ 00868a74 ["INT_ADD", "register:40f0:8", ["const:868a74:8", "const:4:8"]]
+ 00868a74 ["CALL", null, ["callee:00868b18:8"]]
- 00868a1c bytes 29000094
+ 00868a74 bytes 29000094
- 00868a30 ["INT_ADD", "register:40f0:8", ["const:868a30:8", "const:4:8"]]
- 00868a30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00868a88 ["INT_ADD", "register:40f0:8", ["const:868a88:8", "const:4:8"]]
+ 00868a88 ["CALL", null, ["callee:00c53da0:8"]]
- 00868a30 bytes b4ac0f94
+ 00868a88 bytes c6ac0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aae5991247eaa6a35245f64a1351e9f1"></a>

### [`00868ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md) → [`00868b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868b18.md) FUN_00868b18

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) [`008e3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3d50.md) [`008e95c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e95c0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) [`008e3da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md) [`008e9614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md#insn-00868b08) · [`00868b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md#insn-00868b18) · [`00868b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ac0.md#insn-00868b50)
- 新版 `00868b60`（命令位置の公開資料なし） · `00868b70`（命令位置の公開資料なし） · `00868ba8`（命令位置の公開資料なし）

~~~diff
- 00868b08 ["INT_ADD", "register:40f0:8", ["const:868b08:8", "const:4:8"]]
- 00868b08 ["CALL", null, ["callee:00c57f80:8"]]
+ 00868b60 ["INT_ADD", "register:40f0:8", ["const:868b60:8", "const:4:8"]]
+ 00868b60 ["CALL", null, ["callee:00c57f80:8"]]
- 00868b08 bytes eabc0f94
+ 00868b60 bytes 08bd0f94
- 00868b18 ["INT_ADD", "register:40f0:8", ["const:868b18:8", "const:4:8"]]
- 00868b18 ["CALL", null, ["callee:00c57f80:8"]]
+ 00868b70 ["INT_ADD", "register:40f0:8", ["const:868b70:8", "const:4:8"]]
+ 00868b70 ["CALL", null, ["callee:00c57f80:8"]]
- 00868b18 bytes e6bc0f94
+ 00868b70 bytes 04bd0f94
- 00868b50 ["INT_ADD", "register:40f0:8", ["const:868b50:8", "const:4:8"]]
- 00868b50 ["CALL", null, ["callee:00c57f80:8"]]
+ 00868ba8 ["INT_ADD", "register:40f0:8", ["const:868ba8:8", "const:4:8"]]
+ 00868ba8 ["CALL", null, ["callee:00c57f80:8"]]
- 00868b50 bytes d8bc0f94
+ 00868ba8 bytes f6bc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57a1210f1a916a82483b2035999fe9d9"></a>

### [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) → [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) FUN_00868c78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`008689f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/008689f8.md) [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) [`008e1d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e1/008e1d44.md) [`008e4560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e4/008e4560.md) · 呼出先 2件 [`00868c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00868a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868a50.md) [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) [`008e1d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md) [`008e45b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45b4.md) · 呼出先 2件 [`00868c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868c78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md#insn-00868c40) · [`00868c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c20.md#insn-00868c4c)
- 新版 `00868c98`（命令位置の公開資料なし） · `00868ca4`（命令位置の公開資料なし）

~~~diff
- 00868c40 ["INT_ADD", "register:40f0:8", ["const:868c40:8", "const:4:8"]]
- 00868c40 ["CALL", null, ["local:b0:8"]]
+ 00868c98 ["INT_ADD", "register:40f0:8", ["const:868c98:8", "const:4:8"]]
+ 00868c98 ["CALL", null, ["local:b0:8"]]
- 00868c40 bytes f8ffff97
+ 00868c98 bytes f8ffff97
- 00868c4c ["INT_ADD", "register:40f0:8", ["const:868c4c:8", "const:4:8"]]
- 00868c4c ["CALL", null, ["local:b0:8"]]
+ 00868ca4 ["INT_ADD", "register:40f0:8", ["const:868ca4:8", "const:4:8"]]
+ 00868ca4 ["CALL", null, ["local:b0:8"]]
- 00868c4c bytes f5ffff97
+ 00868ca4 bytes f5ffff97
~~~


<a id="compare-3a32dd9bc438aa537fb571e320387ded"></a>

### [`00868c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md) → [`00868cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868cbc.md) FUN_00868cbc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) · 呼出先 5件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008472f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md) · 呼出先 5件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00869004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869004.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md#insn-00868c88) · [`00868c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md#insn-00868c9c) · [`00868ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md#insn-00868ca4)
- 新版 `00868ce0`（命令位置の公開資料なし） · `00868cf4`（命令位置の公開資料なし） · `00868cfc`（命令位置の公開資料なし）

~~~diff
- 00868c88 ["INT_ADD", "register:40f0:8", ["const:868c88:8", "const:4:8"]]
- 00868c88 ["CALL", null, ["callee:00c53da0:8"]]
+ 00868ce0 ["INT_ADD", "register:40f0:8", ["const:868ce0:8", "const:4:8"]]
+ 00868ce0 ["CALL", null, ["callee:00c53da0:8"]]
- 00868c88 bytes 1eac0f94
+ 00868ce0 bytes 30ac0f94
- 00868c9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00868c9c ["INT_ADD", "register:40f0:8", ["const:868c9c:8", "const:4:8"]]
- 00868c9c ["CALLIND", null, ["register:0:8"]]
+ 00868cf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868cf4 ["INT_ADD", "register:40f0:8", ["const:868cf4:8", "const:4:8"]]
+ 00868cf4 ["CALLIND", null, ["register:0:8"]]
- 00868c9c bytes 00013fd6
+ 00868cf4 bytes 00013fd6
- 00868ca4 ["INT_ADD", "register:40f0:8", ["const:868ca4:8", "const:4:8"]]
- 00868ca4 ["CALL", null, ["callee:00c57f50:8"]]
+ 00868cfc ["INT_ADD", "register:40f0:8", ["const:868cfc:8", "const:4:8"]]
+ 00868cfc ["CALL", null, ["callee:00c57f50:8"]]
- 00868ca4 bytes 77bc0f94
+ 00868cfc bytes 95bc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8661029b211fb78fa1b59b05099d6f1"></a>

### [`00868d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md) → [`00868da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868da4.md) FUN_00868da4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084729c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/0084729c.md) · 呼出先 7件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`008472f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008472f4.md) · 呼出先 7件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00672788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672788.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md#insn-00868d6c) · [`00868d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md#insn-00868d80) · [`00868d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868d4c.md#insn-00868d88)
- 新版 `00868dc4`（命令位置の公開資料なし） · `00868dd8`（命令位置の公開資料なし） · `00868de0`（命令位置の公開資料なし）

~~~diff
- 00868d6c ["INT_ADD", "register:40f0:8", ["const:868d6c:8", "const:4:8"]]
- 00868d6c ["CALL", null, ["callee:00c53da0:8"]]
+ 00868dc4 ["INT_ADD", "register:40f0:8", ["const:868dc4:8", "const:4:8"]]
+ 00868dc4 ["CALL", null, ["callee:00c53da0:8"]]
- 00868d6c bytes e5ab0f94
+ 00868dc4 bytes f7ab0f94
- 00868d80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00868d80 ["INT_ADD", "register:40f0:8", ["const:868d80:8", "const:4:8"]]
- 00868d80 ["CALLIND", null, ["register:0:8"]]
+ 00868dd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00868dd8 ["INT_ADD", "register:40f0:8", ["const:868dd8:8", "const:4:8"]]
+ 00868dd8 ["CALLIND", null, ["register:0:8"]]
- 00868d80 bytes 00013fd6
+ 00868dd8 bytes 00013fd6
- 00868d88 ["INT_ADD", "register:40f0:8", ["const:868d88:8", "const:4:8"]]
- 00868d88 ["CALL", null, ["callee:00c57f50:8"]]
+ 00868de0 ["INT_ADD", "register:40f0:8", ["const:868de0:8", "const:4:8"]]
+ 00868de0 ["CALL", null, ["callee:00c57f50:8"]]
- 00868d88 bytes 3ebc0f94
+ 00868de0 bytes 5cbc0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aac67ef95d1c3ba547169052f4a7a4fc"></a>

### [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) → [`00869004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869004.md) FUN_00869004

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00868c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868c64.md) [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 3件 [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`00868ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00868cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00868/00868cbc.md) [`00869004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869004.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) · 呼出先 3件 [`00869004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869004.md) [`00869050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869050.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00868fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md#insn-00868fcc) · [`00868fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md#insn-00868fd8) · [`00868fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md#insn-00868fe0)
- 新版 `00869024`（命令位置の公開資料なし） · `00869030`（命令位置の公開資料なし） · `00869038`（命令位置の公開資料なし）

~~~diff
- 00868fcc ["INT_ADD", "register:40f0:8", ["const:868fcc:8", "const:4:8"]]
- 00868fcc ["CALL", null, ["local:b0:8"]]
+ 00869024 ["INT_ADD", "register:40f0:8", ["const:869024:8", "const:4:8"]]
+ 00869024 ["CALL", null, ["local:b0:8"]]
- 00868fcc bytes f8ffff97
+ 00869024 bytes f8ffff97
- 00868fd8 ["INT_ADD", "register:40f0:8", ["const:868fd8:8", "const:4:8"]]
- 00868fd8 ["CALL", null, ["local:b0:8"]]
+ 00869030 ["INT_ADD", "register:40f0:8", ["const:869030:8", "const:4:8"]]
+ 00869030 ["CALL", null, ["local:b0:8"]]
- 00868fd8 bytes f5ffff97
+ 00869030 bytes f5ffff97
- 00868fe0 ["INT_ADD", "register:40f0:8", ["const:868fe0:8", "const:4:8"]]
- 00868fe0 ["CALL", null, ["callee:00869050:8"]]
+ 00869038 ["INT_ADD", "register:40f0:8", ["const:869038:8", "const:4:8"]]
+ 00869038 ["CALL", null, ["callee:00869050:8"]]
- 00868fe0 bytes 06000094
+ 00869038 bytes 06000094
~~~


<a id="compare-f1bd45c71ed1a56e6ac6602c5ee09906"></a>

### [`00868ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md) → [`00869050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869050.md) FUN_00869050

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00868fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868fac.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`00869004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869004.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) · 呼出先 3件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md#insn-00869010) · [`0086901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md#insn-0086901c) · [`00869028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00868/00868ff8.md#insn-00869028)
- 新版 `00869068`（命令位置の公開資料なし） · `00869074`（命令位置の公開資料なし） · `00869080`（命令位置の公開資料なし）

~~~diff
- 00869010 ["INT_ADD", "register:40f0:8", ["const:869010:8", "const:4:8"]]
- 00869010 ["CALL", null, ["callee:00676aa0:8"]]
+ 00869068 ["INT_ADD", "register:40f0:8", ["const:869068:8", "const:4:8"]]
+ 00869068 ["CALL", null, ["callee:00676aa0:8"]]
- 00869010 bytes 9436f897
+ 00869068 bytes 8e36f897
- 0086901c ["INT_ADD", "register:40f0:8", ["const:86901c:8", "const:4:8"]]
- 0086901c ["CALL", null, ["callee:00676aa0:8"]]
+ 00869074 ["INT_ADD", "register:40f0:8", ["const:869074:8", "const:4:8"]]
+ 00869074 ["CALL", null, ["callee:00676aa0:8"]]
- 0086901c bytes 9136f897
+ 00869074 bytes 8b36f897
- 00869028 ["INT_ADD", "register:40f0:8", ["const:869028:8", "const:4:8"]]
- 00869028 ["CALL", null, ["callee:00676aa0:8"]]
+ 00869080 ["INT_ADD", "register:40f0:8", ["const:869080:8", "const:4:8"]]
+ 00869080 ["CALL", null, ["callee:00676aa0:8"]]
- 00869028 bytes 8e36f897
+ 00869080 bytes 8836f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9619aa296458027d10cfca343b6245c"></a>

### [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) → [`00869140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869140.md) FUN_00869140

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) · 呼出先 3件 [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00869140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869140.md) [`00a64fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64fa8.md) · 呼出先 3件 [`00869140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869140.md) [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md#insn-00869108) · [`00869114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md#insn-00869114) · [`00869120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md#insn-00869120)
- 新版 `00869160`（命令位置の公開資料なし） · `0086916c`（命令位置の公開資料なし） · `00869178`（命令位置の公開資料なし）

~~~diff
- 00869108 ["INT_ADD", "register:40f0:8", ["const:869108:8", "const:4:8"]]
- 00869108 ["CALL", null, ["local:b0:8"]]
+ 00869160 ["INT_ADD", "register:40f0:8", ["const:869160:8", "const:4:8"]]
+ 00869160 ["CALL", null, ["local:b0:8"]]
- 00869108 bytes f8ffff97
+ 00869160 bytes f8ffff97
- 00869114 ["INT_ADD", "register:40f0:8", ["const:869114:8", "const:4:8"]]
- 00869114 ["CALL", null, ["local:b0:8"]]
+ 0086916c ["INT_ADD", "register:40f0:8", ["const:86916c:8", "const:4:8"]]
+ 0086916c ["CALL", null, ["local:b0:8"]]
- 00869114 bytes f5ffff97
+ 0086916c bytes f5ffff97
- 00869120 ["INT_ADD", "register:40f0:8", ["const:869120:8", "const:4:8"]]
- 00869120 ["CALL", null, ["callee:00869190:8"]]
+ 00869178 ["INT_ADD", "register:40f0:8", ["const:869178:8", "const:4:8"]]
+ 00869178 ["CALL", null, ["callee:00869190:8"]]
- 00869120 bytes 06000094
+ 00869178 bytes 06000094
~~~


<a id="compare-b151c995444e92e49eff93675b04bc6a"></a>

### [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) → [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md) FUN_00869190

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`008690e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008690e8.md) [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00a64f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a64/00a64f38.md) [`00a67c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67c80.md) [`00a68014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68014.md) · 呼出先 2件 [`00869138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`00869140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869140.md) [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md) [`00a64fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a64/00a64fa8.md) [`00a67cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a67cf0.md) [`00a68084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68084.md) · 呼出先 2件 [`00869190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869190.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md#insn-00869154) · [`00869160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md#insn-00869160) · [`00869170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869138.md#insn-00869170)
- 新版 `008691ac`（命令位置の公開資料なし） · `008691b8`（命令位置の公開資料なし） · `008691c8`（命令位置の公開資料なし）

~~~diff
- 00869154 ["INT_ADD", "register:40f0:8", ["const:869154:8", "const:4:8"]]
- 00869154 ["CALL", null, ["local:b0:8"]]
+ 008691ac ["INT_ADD", "register:40f0:8", ["const:8691ac:8", "const:4:8"]]
+ 008691ac ["CALL", null, ["local:b0:8"]]
- 00869154 bytes f9ffff97
+ 008691ac bytes f9ffff97
- 00869160 ["INT_ADD", "register:40f0:8", ["const:869160:8", "const:4:8"]]
- 00869160 ["CALL", null, ["local:b0:8"]]
+ 008691b8 ["INT_ADD", "register:40f0:8", ["const:8691b8:8", "const:4:8"]]
+ 008691b8 ["CALL", null, ["local:b0:8"]]
- 00869160 bytes f6ffff97
+ 008691b8 bytes f6ffff97
- 00869170 ["INT_ADD", "register:40f0:8", ["const:869170:8", "const:4:8"]]
- 00869170 ["CALL", null, ["callee:00c57f80:8"]]
+ 008691c8 ["INT_ADD", "register:40f0:8", ["const:8691c8:8", "const:4:8"]]
+ 008691c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00869170 bytes 50bb0f94
+ 008691c8 bytes 6ebb0f94
~~~


<a id="compare-9d730fa769a0a092922362f4f5d41e54"></a>

### [`00869188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md) → [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) FUN_008691e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a37ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ff8.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00a3a018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a018.md) [`00a3a268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a268.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0084743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md) [`00a3804c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3804c.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) [`00a3a06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md) [`00a3a2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a2bc.md) · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008691a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md#insn-008691a4) · [`008691b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md#insn-008691b0) · [`008691e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869188.md#insn-008691e8)
- 新版 `008691fc`（命令位置の公開資料なし） · `00869208`（命令位置の公開資料なし） · `00869240`（命令位置の公開資料なし）

~~~diff
- 008691a4 ["INT_ADD", "register:40f0:8", ["const:8691a4:8", "const:4:8"]]
- 008691a4 ["CALL", null, ["callee:0046d4d0:8"]]
+ 008691fc ["INT_ADD", "register:40f0:8", ["const:8691fc:8", "const:4:8"]]
+ 008691fc ["CALL", null, ["callee:0046d4d0:8"]]
- 008691a4 bytes bb10f097
+ 008691fc bytes b510f097
- 008691b0 ["INT_ADD", "register:40f0:8", ["const:8691b0:8", "const:4:8"]]
- 008691b0 ["CALL", null, ["callee:0046d4d0:8"]]
+ 00869208 ["INT_ADD", "register:40f0:8", ["const:869208:8", "const:4:8"]]
+ 00869208 ["CALL", null, ["callee:0046d4d0:8"]]
- 008691b0 bytes b810f097
+ 00869208 bytes b210f097
- 008691e8 ["INT_ADD", "register:40f0:8", ["const:8691e8:8", "const:4:8"]]
- 008691e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869240 ["INT_ADD", "register:40f0:8", ["const:869240:8", "const:4:8"]]
+ 00869240 ["CALL", null, ["callee:00c57f80:8"]]
- 008691e8 bytes 32bb0f94
+ 00869240 bytes 50bb0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f628ad70aadf5780921841688a4c22"></a>

### [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) → [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) FUN_00869280

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a38064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) [`00a39dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0084743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md) [`00a380b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) [`00a39e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md) · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md#insn-00869260) · [`0086926c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md#insn-0086926c) · [`00869278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md#insn-00869278)
- 新版 `008692b8`（命令位置の公開資料なし） · `008692c4`（命令位置の公開資料なし） · `008692d0`（命令位置の公開資料なし）

~~~diff
- 00869260 ["INT_ADD", "register:40f0:8", ["const:869260:8", "const:4:8"]]
- 00869260 ["CALL", null, ["callee:0046d4d0:8"]]
+ 008692b8 ["INT_ADD", "register:40f0:8", ["const:8692b8:8", "const:4:8"]]
+ 008692b8 ["CALL", null, ["callee:0046d4d0:8"]]
- 00869260 bytes 8c10f097
+ 008692b8 bytes 8610f097
- 0086926c ["INT_ADD", "register:40f0:8", ["const:86926c:8", "const:4:8"]]
- 0086926c ["CALL", null, ["callee:0046d4d0:8"]]
+ 008692c4 ["INT_ADD", "register:40f0:8", ["const:8692c4:8", "const:4:8"]]
+ 008692c4 ["CALL", null, ["callee:0046d4d0:8"]]
- 0086926c bytes 8910f097
+ 008692c4 bytes 8310f097
- 00869278 ["INT_ADD", "register:40f0:8", ["const:869278:8", "const:4:8"]]
- 00869278 ["CALL", null, ["callee:0046d4d0:8"]]
+ 008692d0 ["INT_ADD", "register:40f0:8", ["const:8692d0:8", "const:4:8"]]
+ 008692d0 ["CALL", null, ["callee:0046d4d0:8"]]
- 00869278 bytes 8610f097
+ 008692d0 bytes 8010f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57a2d330ee44517d50ed873090a464e3"></a>

### [`0086930c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md) → [`00869364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869364.md) FUN_00869364

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`008473e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008473e4.md) [`00a380cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a380cc.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0084743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/0084743c.md) [`00a38120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a38120.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md#insn-00869354) · [`00869370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md#insn-00869370) · [`008693a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/0086930c.md#insn-008693a8)
- 新版 `008693ac`（命令位置の公開資料なし） · `008693c8`（命令位置の公開資料なし） · `00869400`（命令位置の公開資料なし）

~~~diff
- 00869354 ["INT_ADD", "register:40f0:8", ["const:869354:8", "const:4:8"]]
- 00869354 ["CALL", null, ["callee:00c57f80:8"]]
+ 008693ac ["INT_ADD", "register:40f0:8", ["const:8693ac:8", "const:4:8"]]
+ 008693ac ["CALL", null, ["callee:00c57f80:8"]]
- 00869354 bytes d7ba0f94
+ 008693ac bytes f5ba0f94
- 00869370 ["INT_ADD", "register:40f0:8", ["const:869370:8", "const:4:8"]]
- 00869370 ["CALL", null, ["callee:00c57f80:8"]]
+ 008693c8 ["INT_ADD", "register:40f0:8", ["const:8693c8:8", "const:4:8"]]
+ 008693c8 ["CALL", null, ["callee:00c57f80:8"]]
- 00869370 bytes d0ba0f94
+ 008693c8 bytes eeba0f94
- 008693a8 ["INT_ADD", "register:40f0:8", ["const:8693a8:8", "const:4:8"]]
- 008693a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869400 ["INT_ADD", "register:40f0:8", ["const:869400:8", "const:4:8"]]
+ 00869400 ["CALL", null, ["callee:00c57f80:8"]]
- 008693a8 bytes c2ba0f94
+ 00869400 bytes e0ba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619ea4e15c09e92db042e5f2ab632729"></a>

### [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) → [`00869418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869418.md) FUN_00869418

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474b0.md) [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) · 呼出先 2件 [`008693c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847508.md) [`00869418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869418.md) · 呼出先 2件 [`00869418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869418.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008693dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md#insn-008693dc) · [`008693e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md#insn-008693e8) · [`008693f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008693c0.md#insn-008693f8)
- 新版 `00869434`（命令位置の公開資料なし） · `00869440`（命令位置の公開資料なし） · `00869450`（命令位置の公開資料なし）

~~~diff
- 008693dc ["INT_ADD", "register:40f0:8", ["const:8693dc:8", "const:4:8"]]
- 008693dc ["CALL", null, ["local:b0:8"]]
+ 00869434 ["INT_ADD", "register:40f0:8", ["const:869434:8", "const:4:8"]]
+ 00869434 ["CALL", null, ["local:b0:8"]]
- 008693dc bytes f9ffff97
+ 00869434 bytes f9ffff97
- 008693e8 ["INT_ADD", "register:40f0:8", ["const:8693e8:8", "const:4:8"]]
- 008693e8 ["CALL", null, ["local:b0:8"]]
+ 00869440 ["INT_ADD", "register:40f0:8", ["const:869440:8", "const:4:8"]]
+ 00869440 ["CALL", null, ["local:b0:8"]]
- 008693e8 bytes f6ffff97
+ 00869440 bytes f6ffff97
- 008693f8 ["INT_ADD", "register:40f0:8", ["const:8693f8:8", "const:4:8"]]
- 008693f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869450 ["INT_ADD", "register:40f0:8", ["const:869450:8", "const:4:8"]]
+ 00869450 ["CALL", null, ["callee:00c57f80:8"]]
- 008693f8 bytes aeba0f94
+ 00869450 bytes ccba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1d41ce182fb59672abe5c15e3cfaf9"></a>

### [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) → [`00869478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869478.md) FUN_00869478

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008474b0.md) [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) · 呼出先 2件 [`00869420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847508.md) [`00869478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869478.md) · 呼出先 2件 [`00869478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869478.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md#insn-00869440) · [`0086944c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869420.md#insn-0086944c)
- 新版 `00869498`（命令位置の公開資料なし） · `008694a4`（命令位置の公開資料なし）

~~~diff
- 00869440 ["INT_ADD", "register:40f0:8", ["const:869440:8", "const:4:8"]]
- 00869440 ["CALL", null, ["local:b0:8"]]
+ 00869498 ["INT_ADD", "register:40f0:8", ["const:869498:8", "const:4:8"]]
+ 00869498 ["CALL", null, ["local:b0:8"]]
- 00869440 bytes f8ffff97
+ 00869498 bytes f8ffff97
- 0086944c ["INT_ADD", "register:40f0:8", ["const:86944c:8", "const:4:8"]]
- 0086944c ["CALL", null, ["local:b0:8"]]
+ 008694a4 ["INT_ADD", "register:40f0:8", ["const:8694a4:8", "const:4:8"]]
+ 008694a4 ["CALL", null, ["local:b0:8"]]
- 0086944c bytes f5ffff97
+ 008694a4 bytes f5ffff97
~~~


<a id="compare-d4ffd9cff78afeaee5c033513000b52f"></a>

### [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) → [`008694bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008694bc.md) FUN_008694bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) · 呼出先 2件 [`00869464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008694bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008694bc.md) · 呼出先 2件 [`008694bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008694bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md#insn-00869480) · [`0086948c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md#insn-0086948c) · [`0086949c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869464.md#insn-0086949c)
- 新版 `008694d8`（命令位置の公開資料なし） · `008694e4`（命令位置の公開資料なし） · `008694f4`（命令位置の公開資料なし）

~~~diff
- 00869480 ["INT_ADD", "register:40f0:8", ["const:869480:8", "const:4:8"]]
- 00869480 ["CALL", null, ["local:b0:8"]]
+ 008694d8 ["INT_ADD", "register:40f0:8", ["const:8694d8:8", "const:4:8"]]
+ 008694d8 ["CALL", null, ["local:b0:8"]]
- 00869480 bytes f9ffff97
+ 008694d8 bytes f9ffff97
- 0086948c ["INT_ADD", "register:40f0:8", ["const:86948c:8", "const:4:8"]]
- 0086948c ["CALL", null, ["local:b0:8"]]
+ 008694e4 ["INT_ADD", "register:40f0:8", ["const:8694e4:8", "const:4:8"]]
+ 008694e4 ["CALL", null, ["local:b0:8"]]
- 0086948c bytes f6ffff97
+ 008694e4 bytes f6ffff97
- 0086949c ["INT_ADD", "register:40f0:8", ["const:86949c:8", "const:4:8"]]
- 0086949c ["CALL", null, ["callee:00c57f80:8"]]
+ 008694f4 ["INT_ADD", "register:40f0:8", ["const:8694f4:8", "const:4:8"]]
+ 008694f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086949c bytes 85ba0f94
+ 008694f4 bytes a3ba0f94
~~~


<a id="compare-4b51e5ad257233c56d6f9533cb6faafb"></a>

### [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) → [`0086950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086950c.md) FUN_0086950c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008476ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/008476ac.md) [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) [`00aafa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aaf/00aafa34.md) [`00ab09f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab09f4.md) · 呼出先 2件 [`008694b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847704.md) [`0086950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086950c.md) [`00aafaa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aaf/00aafaa4.md) [`00ab0a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab0a64.md) · 呼出先 2件 [`0086950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086950c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008694d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md#insn-008694d0) · [`008694dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md#insn-008694dc) · [`008694ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008694b4.md#insn-008694ec)
- 新版 `00869528`（命令位置の公開資料なし） · `00869534`（命令位置の公開資料なし） · `00869544`（命令位置の公開資料なし）

~~~diff
- 008694d0 ["INT_ADD", "register:40f0:8", ["const:8694d0:8", "const:4:8"]]
- 008694d0 ["CALL", null, ["local:b0:8"]]
+ 00869528 ["INT_ADD", "register:40f0:8", ["const:869528:8", "const:4:8"]]
+ 00869528 ["CALL", null, ["local:b0:8"]]
- 008694d0 bytes f9ffff97
+ 00869528 bytes f9ffff97
- 008694dc ["INT_ADD", "register:40f0:8", ["const:8694dc:8", "const:4:8"]]
- 008694dc ["CALL", null, ["local:b0:8"]]
+ 00869534 ["INT_ADD", "register:40f0:8", ["const:869534:8", "const:4:8"]]
+ 00869534 ["CALL", null, ["local:b0:8"]]
- 008694dc bytes f6ffff97
+ 00869534 bytes f6ffff97
- 008694ec ["INT_ADD", "register:40f0:8", ["const:8694ec:8", "const:4:8"]]
- 008694ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00869544 ["INT_ADD", "register:40f0:8", ["const:869544:8", "const:4:8"]]
+ 00869544 ["CALL", null, ["callee:00c57f80:8"]]
- 008694ec bytes 71ba0f94
+ 00869544 bytes 8fba0f94
~~~


<a id="compare-52ed88cda6ac836a8a4467d7c8d702ab"></a>

### [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) → [`0086955c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086955c.md) FUN_0086955c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00847860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847860.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) · 呼出先 2件 [`00869504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`008478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/008478b8.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086955c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086955c.md) · 呼出先 2件 [`0086955c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/0086955c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md#insn-00869524) · [`00869530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869504.md#insn-00869530)
- 新版 `0086957c`（命令位置の公開資料なし） · `00869588`（命令位置の公開資料なし）

~~~diff
- 00869524 ["INT_ADD", "register:40f0:8", ["const:869524:8", "const:4:8"]]
- 00869524 ["CALL", null, ["local:b0:8"]]
+ 0086957c ["INT_ADD", "register:40f0:8", ["const:86957c:8", "const:4:8"]]
+ 0086957c ["CALL", null, ["local:b0:8"]]
- 00869524 bytes f8ffff97
+ 0086957c bytes f8ffff97
- 00869530 ["INT_ADD", "register:40f0:8", ["const:869530:8", "const:4:8"]]
- 00869530 ["CALL", null, ["local:b0:8"]]
+ 00869588 ["INT_ADD", "register:40f0:8", ["const:869588:8", "const:4:8"]]
+ 00869588 ["CALL", null, ["local:b0:8"]]
- 00869530 bytes f5ffff97
+ 00869588 bytes f5ffff97
~~~


<a id="compare-cad39fc329caaba634019afc18a8fffa"></a>

### [`00869548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md) → [`008695a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008695a0.md) FUN_008695a0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md) · 呼出先 6件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md#insn-00869594) · [`008695a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md#insn-008695a4) · [`008695b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869548.md#insn-008695b4)
- 新版 `008695ec`（命令位置の公開資料なし） · `008695fc`（命令位置の公開資料なし） · `0086960c`（命令位置の公開資料なし）

~~~diff
- 00869594 ["INT_ADD", "register:40f0:8", ["const:869594:8", "const:4:8"]]
- 00869594 ["CALL", null, ["callee:00c57f80:8"]]
+ 008695ec ["INT_ADD", "register:40f0:8", ["const:8695ec:8", "const:4:8"]]
+ 008695ec ["CALL", null, ["callee:00c57f80:8"]]
- 00869594 bytes 47ba0f94
+ 008695ec bytes 65ba0f94
- 008695a4 ["INT_ADD", "register:40f0:8", ["const:8695a4:8", "const:4:8"]]
- 008695a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 008695fc ["INT_ADD", "register:40f0:8", ["const:8695fc:8", "const:4:8"]]
+ 008695fc ["CALL", null, ["callee:00c57f80:8"]]
- 008695a4 bytes 43ba0f94
+ 008695fc bytes 61ba0f94
- 008695b4 ["INT_ADD", "register:40f0:8", ["const:8695b4:8", "const:4:8"]]
- 008695b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086960c ["INT_ADD", "register:40f0:8", ["const:86960c:8", "const:4:8"]]
+ 0086960c ["CALL", null, ["callee:00c57f80:8"]]
- 008695b4 bytes 3fba0f94
+ 0086960c bytes 5dba0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c167031e9b70ebd16c22678466ab7b"></a>

### [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) → [`008697dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008697dc.md) FUN_008697dc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847af8.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) · 呼出先 2件 [`00869784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b50.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`008697dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008697dc.md) · 呼出先 2件 [`008697dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008697dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008697a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md#insn-008697a4) · [`008697b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869784.md#insn-008697b0)
- 新版 `008697fc`（命令位置の公開資料なし） · `00869808`（命令位置の公開資料なし）

~~~diff
- 008697a4 ["INT_ADD", "register:40f0:8", ["const:8697a4:8", "const:4:8"]]
- 008697a4 ["CALL", null, ["local:b0:8"]]
+ 008697fc ["INT_ADD", "register:40f0:8", ["const:8697fc:8", "const:4:8"]]
+ 008697fc ["CALL", null, ["local:b0:8"]]
- 008697a4 bytes f8ffff97
+ 008697fc bytes f8ffff97
- 008697b0 ["INT_ADD", "register:40f0:8", ["const:8697b0:8", "const:4:8"]]
- 008697b0 ["CALL", null, ["local:b0:8"]]
+ 00869808 ["INT_ADD", "register:40f0:8", ["const:869808:8", "const:4:8"]]
+ 00869808 ["CALL", null, ["local:b0:8"]]
- 008697b0 bytes f5ffff97
+ 00869808 bytes f5ffff97
~~~


<a id="compare-277b7eb0f38ed92523fbfa5e48cb2e0c"></a>

### [`008697c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md) → [`00869820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869820.md) FUN_00869820

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00847b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00847/00847b38.md) [`009bdd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdd38.md) [`009c058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c058c.md) [`009c0fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0fe4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847b90.md) [`009bdd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bd/009bdd8c.md) [`009c05e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c0/009c05e0.md) [`009c1038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c1/009c1038.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md#insn-00869810) · [`00869820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md#insn-00869820) · [`0086984c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/008697c8.md#insn-0086984c)
- 新版 `00869868`（命令位置の公開資料なし） · `00869878`（命令位置の公開資料なし） · `008698a4`（命令位置の公開資料なし）

~~~diff
- 00869810 ["INT_ADD", "register:40f0:8", ["const:869810:8", "const:4:8"]]
- 00869810 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869868 ["INT_ADD", "register:40f0:8", ["const:869868:8", "const:4:8"]]
+ 00869868 ["CALL", null, ["callee:00c57f80:8"]]
- 00869810 bytes a8b90f94
+ 00869868 bytes c6b90f94
- 00869820 ["INT_ADD", "register:40f0:8", ["const:869820:8", "const:4:8"]]
- 00869820 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869878 ["INT_ADD", "register:40f0:8", ["const:869878:8", "const:4:8"]]
+ 00869878 ["CALL", null, ["callee:00c57f80:8"]]
- 00869820 bytes a4b90f94
+ 00869878 bytes c2b90f94
- 0086984c ["INT_ADD", "register:40f0:8", ["const:86984c:8", "const:4:8"]]
- 0086984c ["CALL", null, ["callee:00c57f80:8"]]
+ 008698a4 ["INT_ADD", "register:40f0:8", ["const:8698a4:8", "const:4:8"]]
+ 008698a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086984c bytes 99b90f94
+ 008698a4 bytes b7b90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6482b6932fabcc6ae807f15dacd79ed3"></a>

### [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) → [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) FUN_008699e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) [`00a82f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a82/00a82f2c.md) · 呼出先 4件 [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) [`00a82f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a82/00a82f9c.md) · 呼出先 4件 [`008699e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008699e0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008699ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md#insn-008699ac) · [`008699b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md#insn-008699b8) · [`008699e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md#insn-008699e0)
- 新版 `00869a04`（命令位置の公開資料なし） · `00869a10`（命令位置の公開資料なし） · `00869a38`（命令位置の公開資料なし）

~~~diff
- 008699ac ["INT_ADD", "register:40f0:8", ["const:8699ac:8", "const:4:8"]]
- 008699ac ["CALL", null, ["local:b0:8"]]
+ 00869a04 ["INT_ADD", "register:40f0:8", ["const:869a04:8", "const:4:8"]]
+ 00869a04 ["CALL", null, ["local:b0:8"]]
- 008699ac bytes f7ffff97
+ 00869a04 bytes f7ffff97
- 008699b8 ["INT_ADD", "register:40f0:8", ["const:8699b8:8", "const:4:8"]]
- 008699b8 ["CALL", null, ["local:b0:8"]]
+ 00869a10 ["INT_ADD", "register:40f0:8", ["const:869a10:8", "const:4:8"]]
+ 00869a10 ["CALL", null, ["local:b0:8"]]
- 008699b8 bytes f4ffff97
+ 00869a10 bytes f4ffff97
- 008699e0 ["INT_ADD", "register:40f0:8", ["const:8699e0:8", "const:4:8"]]
- 008699e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869a38 ["INT_ADD", "register:40f0:8", ["const:869a38:8", "const:4:8"]]
+ 00869a38 ["CALL", null, ["callee:00c57f80:8"]]
- 008699e0 bytes 34b90f94
+ 00869a38 bytes 52b90f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f657a875d556fa8d6ac75b06cc532967"></a>

### [`00869b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md) → [`00869b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869b94.md) FUN_00869b94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848250.md) [`008bac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bac8c.md) [`008bb53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb53c.md) [`008bba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bba60.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008482a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008482a8.md) [`008bace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bace4.md) [`008bb594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb594.md) [`008bbab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbab8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md#insn-00869b80) · [`00869bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md#insn-00869bb0) · [`00869be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869b3c.md#insn-00869be0)
- 新版 `00869bd8`（命令位置の公開資料なし） · `00869c08`（命令位置の公開資料なし） · `00869c38`（命令位置の公開資料なし）

~~~diff
- 00869b80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869b80 ["INT_ADD", "register:40f0:8", ["const:869b80:8", "const:4:8"]]
- 00869b80 ["CALLIND", null, ["register:0:8"]]
+ 00869bd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869bd8 ["INT_ADD", "register:40f0:8", ["const:869bd8:8", "const:4:8"]]
+ 00869bd8 ["CALLIND", null, ["register:0:8"]]
- 00869b80 bytes 00013fd6
+ 00869bd8 bytes 00013fd6
- 00869bb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869bb0 ["INT_ADD", "register:40f0:8", ["const:869bb0:8", "const:4:8"]]
- 00869bb0 ["CALLIND", null, ["register:0:8"]]
+ 00869c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869c08 ["INT_ADD", "register:40f0:8", ["const:869c08:8", "const:4:8"]]
+ 00869c08 ["CALLIND", null, ["register:0:8"]]
- 00869bb0 bytes 00013fd6
+ 00869c08 bytes 00013fd6
- 00869be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00869be0 ["INT_ADD", "register:40f0:8", ["const:869be0:8", "const:4:8"]]
- 00869be0 ["CALLIND", null, ["register:0:8"]]
+ 00869c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00869c38 ["INT_ADD", "register:40f0:8", ["const:869c38:8", "const:4:8"]]
+ 00869c38 ["CALLIND", null, ["register:0:8"]]
- 00869be0 bytes 00013fd6
+ 00869c38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f598ed38e39498fe9b8267eb9d748ca6"></a>

### [`00869ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ca4.md) → [`00869cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869cfc.md) FUN_00869cfc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ca4.md#insn-00869ce8) · [`00869cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ca4.md#insn-00869cf0) · [`00869d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ca4.md#insn-00869d38)
- 新版 `00869d40`（命令位置の公開資料なし） · `00869d48`（命令位置の公開資料なし） · `00869d90`（命令位置の公開資料なし）

~~~diff
- 00869ce8 ["INT_ADD", "register:40f0:8", ["const:869ce8:8", "const:4:8"]]
- 00869ce8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869d40 ["INT_ADD", "register:40f0:8", ["const:869d40:8", "const:4:8"]]
+ 00869d40 ["CALL", null, ["callee:00c57f80:8"]]
- 00869ce8 bytes 72b80f94
+ 00869d40 bytes 90b80f94
- 00869cf0 ["INT_ADD", "register:40f0:8", ["const:869cf0:8", "const:4:8"]]
- 00869cf0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869d48 ["INT_ADD", "register:40f0:8", ["const:869d48:8", "const:4:8"]]
+ 00869d48 ["CALL", null, ["callee:00c57f80:8"]]
- 00869cf0 bytes 70b80f94
+ 00869d48 bytes 8eb80f94
- 00869d38 ["INT_ADD", "register:40f0:8", ["const:869d38:8", "const:4:8"]]
- 00869d38 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869d90 ["INT_ADD", "register:40f0:8", ["const:869d90:8", "const:4:8"]]
+ 00869d90 ["CALL", null, ["callee:00c57f80:8"]]
- 00869d38 bytes 5eb80f94
+ 00869d90 bytes 7cb80f94
~~~


<a id="compare-4f41072ebda7234f28d0eeaca76f1f5b"></a>

### [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) → [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) FUN_00869dd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008484f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008484f8.md) [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) · 呼出先 2件 [`00869d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848550.md) [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) · 呼出先 2件 [`00869dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869dd4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md#insn-00869d9c) · [`00869da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869d7c.md#insn-00869da8)
- 新版 `00869df4`（命令位置の公開資料なし） · `00869e00`（命令位置の公開資料なし）

~~~diff
- 00869d9c ["INT_ADD", "register:40f0:8", ["const:869d9c:8", "const:4:8"]]
- 00869d9c ["CALL", null, ["local:b0:8"]]
+ 00869df4 ["INT_ADD", "register:40f0:8", ["const:869df4:8", "const:4:8"]]
+ 00869df4 ["CALL", null, ["local:b0:8"]]
- 00869d9c bytes f8ffff97
+ 00869df4 bytes f8ffff97
- 00869da8 ["INT_ADD", "register:40f0:8", ["const:869da8:8", "const:4:8"]]
- 00869da8 ["CALL", null, ["local:b0:8"]]
+ 00869e00 ["INT_ADD", "register:40f0:8", ["const:869e00:8", "const:4:8"]]
+ 00869e00 ["CALL", null, ["local:b0:8"]]
- 00869da8 bytes f5ffff97
+ 00869e00 bytes f5ffff97
~~~


<a id="compare-ea0eb0082327c8a976bfc247b1e7c169"></a>

### [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) → [`00869e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e18.md) FUN_00869e18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) · 呼出先 3件 [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00869e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e18.md) · 呼出先 3件 [`00869e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e18.md) [`00869e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e68.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md#insn-00869de0) · [`00869dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md#insn-00869dec) · [`00869df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md#insn-00869df8)
- 新版 `00869e38`（命令位置の公開資料なし） · `00869e44`（命令位置の公開資料なし） · `00869e50`（命令位置の公開資料なし）

~~~diff
- 00869de0 ["INT_ADD", "register:40f0:8", ["const:869de0:8", "const:4:8"]]
- 00869de0 ["CALL", null, ["local:b0:8"]]
+ 00869e38 ["INT_ADD", "register:40f0:8", ["const:869e38:8", "const:4:8"]]
+ 00869e38 ["CALL", null, ["local:b0:8"]]
- 00869de0 bytes f8ffff97
+ 00869e38 bytes f8ffff97
- 00869dec ["INT_ADD", "register:40f0:8", ["const:869dec:8", "const:4:8"]]
- 00869dec ["CALL", null, ["local:b0:8"]]
+ 00869e44 ["INT_ADD", "register:40f0:8", ["const:869e44:8", "const:4:8"]]
+ 00869e44 ["CALL", null, ["local:b0:8"]]
- 00869dec bytes f5ffff97
+ 00869e44 bytes f5ffff97
- 00869df8 ["INT_ADD", "register:40f0:8", ["const:869df8:8", "const:4:8"]]
- 00869df8 ["CALL", null, ["callee:00869e68:8"]]
+ 00869e50 ["INT_ADD", "register:40f0:8", ["const:869e50:8", "const:4:8"]]
+ 00869e50 ["CALL", null, ["callee:00869e68:8"]]
- 00869df8 bytes 06000094
+ 00869e50 bytes 06000094
~~~


<a id="compare-d739c04dde38530e78c4ea8460a34f6a"></a>

### [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) → [`00869e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e68.md) FUN_00869e68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00869dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869dc0.md) [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) · 呼出先 2件 [`00869e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00869e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e18.md) [`00869e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e68.md) · 呼出先 2件 [`00869e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869e68.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md#insn-00869e30) · [`00869e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e10.md#insn-00869e3c)
- 新版 `00869e88`（命令位置の公開資料なし） · `00869e94`（命令位置の公開資料なし）

~~~diff
- 00869e30 ["INT_ADD", "register:40f0:8", ["const:869e30:8", "const:4:8"]]
- 00869e30 ["CALL", null, ["local:b0:8"]]
+ 00869e88 ["INT_ADD", "register:40f0:8", ["const:869e88:8", "const:4:8"]]
+ 00869e88 ["CALL", null, ["local:b0:8"]]
- 00869e30 bytes f8ffff97
+ 00869e88 bytes f8ffff97
- 00869e3c ["INT_ADD", "register:40f0:8", ["const:869e3c:8", "const:4:8"]]
- 00869e3c ["CALL", null, ["local:b0:8"]]
+ 00869e94 ["INT_ADD", "register:40f0:8", ["const:869e94:8", "const:4:8"]]
+ 00869e94 ["CALL", null, ["local:b0:8"]]
- 00869e3c bytes f5ffff97
+ 00869e94 bytes f5ffff97
~~~


<a id="compare-caa48075121b4f7715ff4317fe58bc4d"></a>

### [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) → [`00869eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869eac.md) FUN_00869eac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) [`00a2f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f62c.md) · 呼出先 2件 [`00869e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00869eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869eac.md) [`00a2f680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2f680.md) · 呼出先 2件 [`00869eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869eac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md#insn-00869e70) · [`00869e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md#insn-00869e7c) · [`00869e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869e54.md#insn-00869e8c)
- 新版 `00869ec8`（命令位置の公開資料なし） · `00869ed4`（命令位置の公開資料なし） · `00869ee4`（命令位置の公開資料なし）

~~~diff
- 00869e70 ["INT_ADD", "register:40f0:8", ["const:869e70:8", "const:4:8"]]
- 00869e70 ["CALL", null, ["local:b0:8"]]
+ 00869ec8 ["INT_ADD", "register:40f0:8", ["const:869ec8:8", "const:4:8"]]
+ 00869ec8 ["CALL", null, ["local:b0:8"]]
- 00869e70 bytes f9ffff97
+ 00869ec8 bytes f9ffff97
- 00869e7c ["INT_ADD", "register:40f0:8", ["const:869e7c:8", "const:4:8"]]
- 00869e7c ["CALL", null, ["local:b0:8"]]
+ 00869ed4 ["INT_ADD", "register:40f0:8", ["const:869ed4:8", "const:4:8"]]
+ 00869ed4 ["CALL", null, ["local:b0:8"]]
- 00869e7c bytes f6ffff97
+ 00869ed4 bytes f6ffff97
- 00869e8c ["INT_ADD", "register:40f0:8", ["const:869e8c:8", "const:4:8"]]
- 00869e8c ["CALL", null, ["callee:00c57f80:8"]]
+ 00869ee4 ["INT_ADD", "register:40f0:8", ["const:869ee4:8", "const:4:8"]]
+ 00869ee4 ["CALL", null, ["callee:00c57f80:8"]]
- 00869e8c bytes 09b80f94
+ 00869ee4 bytes 27b80f94
~~~


<a id="compare-3a921dd5243d6125cbc432261da3f19a"></a>

### [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) → [`00869efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869efc.md) FUN_00869efc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) [`00a62f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a62/00a62f4c.md) · 呼出先 3件 [`005c17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c17e0.md) [`00869ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00869efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869efc.md) [`00a62fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a62/00a62fbc.md) · 呼出先 3件 [`005c1820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1820.md) [`00869efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869efc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md#insn-00869ec4) · [`00869ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md#insn-00869ed0) · [`00869edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ea4.md#insn-00869edc)
- 新版 `00869f1c`（命令位置の公開資料なし） · `00869f28`（命令位置の公開資料なし） · `00869f34`（命令位置の公開資料なし）

~~~diff
- 00869ec4 ["INT_ADD", "register:40f0:8", ["const:869ec4:8", "const:4:8"]]
- 00869ec4 ["CALL", null, ["local:b0:8"]]
+ 00869f1c ["INT_ADD", "register:40f0:8", ["const:869f1c:8", "const:4:8"]]
+ 00869f1c ["CALL", null, ["local:b0:8"]]
- 00869ec4 bytes f8ffff97
+ 00869f1c bytes f8ffff97
- 00869ed0 ["INT_ADD", "register:40f0:8", ["const:869ed0:8", "const:4:8"]]
- 00869ed0 ["CALL", null, ["local:b0:8"]]
+ 00869f28 ["INT_ADD", "register:40f0:8", ["const:869f28:8", "const:4:8"]]
+ 00869f28 ["CALL", null, ["local:b0:8"]]
- 00869ed0 bytes f5ffff97
+ 00869f28 bytes f5ffff97
- 00869edc ["INT_ADD", "register:40f0:8", ["const:869edc:8", "const:4:8"]]
- 00869edc ["CALL", null, ["callee:005c1820:8"]]
+ 00869f34 ["INT_ADD", "register:40f0:8", ["const:869f34:8", "const:4:8"]]
+ 00869f34 ["CALL", null, ["callee:005c1820:8"]]
- 00869edc bytes 415ef597
+ 00869f34 bytes 3b5ef597
~~~


<a id="compare-440d22a87b72ddd195dd93f988f560dd"></a>

### [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) → [`00869f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869f4c.md) FUN_00869f4c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 10件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008487c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008487c8.md) [`009aa61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa61c.md) [`009ac400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac400.md) [`009acc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009acc30.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 10件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848820.md) [`009aa670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa670.md) [`009ac454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac454.md) [`009acc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md#insn-00869f78) · [`00869f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md#insn-00869f88) · [`00869f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md#insn-00869f98)
- 新版 `00869fd0`（命令位置の公開資料なし） · `00869fe0`（命令位置の公開資料なし） · `00869ff0`（命令位置の公開資料なし）

~~~diff
- 00869f78 ["INT_ADD", "register:40f0:8", ["const:869f78:8", "const:4:8"]]
- 00869f78 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869fd0 ["INT_ADD", "register:40f0:8", ["const:869fd0:8", "const:4:8"]]
+ 00869fd0 ["CALL", null, ["callee:00c57f80:8"]]
- 00869f78 bytes ceb70f94
+ 00869fd0 bytes ecb70f94
- 00869f88 ["INT_ADD", "register:40f0:8", ["const:869f88:8", "const:4:8"]]
- 00869f88 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869fe0 ["INT_ADD", "register:40f0:8", ["const:869fe0:8", "const:4:8"]]
+ 00869fe0 ["CALL", null, ["callee:00c57f80:8"]]
- 00869f88 bytes cab70f94
+ 00869fe0 bytes e8b70f94
- 00869f98 ["INT_ADD", "register:40f0:8", ["const:869f98:8", "const:4:8"]]
- 00869f98 ["CALL", null, ["callee:00c57f80:8"]]
+ 00869ff0 ["INT_ADD", "register:40f0:8", ["const:869ff0:8", "const:4:8"]]
+ 00869ff0 ["CALL", null, ["callee:00c57f80:8"]]
- 00869f98 bytes c6b70f94
+ 00869ff0 bytes e4b70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6805e505b3f409895d27b398224bdbac"></a>

### [`00869fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md) → [`0086a008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a008.md) FUN_0086a008

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848818.md) [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) [`008e05f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e05f4.md) [`008e09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e09d8.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848870.md) [`008dd148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dd148.md) [`008e0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md) [`008e0a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a2c.md) · 呼出先 3件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00869fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md#insn-00869fc8) · [`00869fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md#insn-00869fd4) · [`00869fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869fb0.md#insn-00869fe0)
- 新版 `0086a020`（命令位置の公開資料なし） · `0086a02c`（命令位置の公開資料なし） · `0086a038`（命令位置の公開資料なし）

~~~diff
- 00869fc8 ["INT_ADD", "register:40f0:8", ["const:869fc8:8", "const:4:8"]]
- 00869fc8 ["CALL", null, ["callee:00676aa0:8"]]
+ 0086a020 ["INT_ADD", "register:40f0:8", ["const:86a020:8", "const:4:8"]]
+ 0086a020 ["CALL", null, ["callee:00676aa0:8"]]
- 00869fc8 bytes a632f897
+ 0086a020 bytes a032f897
- 00869fd4 ["INT_ADD", "register:40f0:8", ["const:869fd4:8", "const:4:8"]]
- 00869fd4 ["CALL", null, ["callee:00676aa0:8"]]
+ 0086a02c ["INT_ADD", "register:40f0:8", ["const:86a02c:8", "const:4:8"]]
+ 0086a02c ["CALL", null, ["callee:00676aa0:8"]]
- 00869fd4 bytes a332f897
+ 0086a02c bytes 9d32f897
- 00869fe0 ["INT_ADD", "register:40f0:8", ["const:869fe0:8", "const:4:8"]]
- 00869fe0 ["CALL", null, ["callee:00676aa0:8"]]
+ 0086a038 ["INT_ADD", "register:40f0:8", ["const:86a038:8", "const:4:8"]]
+ 0086a038 ["CALL", null, ["callee:00676aa0:8"]]
- 00869fe0 bytes a032f897
+ 0086a038 bytes 9a32f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce834094fd5716eee86fb95b5e843b74"></a>

### [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) → [`0086a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a0bc.md) FUN_0086a0bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008488dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008488dc.md) [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) · 呼出先 2件 [`0086a064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848934.md) [`0086a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a0bc.md) [`008d7248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7248.md) · 呼出先 2件 [`0086a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a0bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md#insn-0086a080) · [`0086a08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md#insn-0086a08c) · [`0086a09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a064.md#insn-0086a09c)
- 新版 `0086a0d8`（命令位置の公開資料なし） · `0086a0e4`（命令位置の公開資料なし） · `0086a0f4`（命令位置の公開資料なし）

~~~diff
- 0086a080 ["INT_ADD", "register:40f0:8", ["const:86a080:8", "const:4:8"]]
- 0086a080 ["CALL", null, ["local:b0:8"]]
+ 0086a0d8 ["INT_ADD", "register:40f0:8", ["const:86a0d8:8", "const:4:8"]]
+ 0086a0d8 ["CALL", null, ["local:b0:8"]]
- 0086a080 bytes f9ffff97
+ 0086a0d8 bytes f9ffff97
- 0086a08c ["INT_ADD", "register:40f0:8", ["const:86a08c:8", "const:4:8"]]
- 0086a08c ["CALL", null, ["local:b0:8"]]
+ 0086a0e4 ["INT_ADD", "register:40f0:8", ["const:86a0e4:8", "const:4:8"]]
+ 0086a0e4 ["CALL", null, ["local:b0:8"]]
- 0086a08c bytes f6ffff97
+ 0086a0e4 bytes f6ffff97
- 0086a09c ["INT_ADD", "register:40f0:8", ["const:86a09c:8", "const:4:8"]]
- 0086a09c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a0f4 ["INT_ADD", "register:40f0:8", ["const:86a0f4:8", "const:4:8"]]
+ 0086a0f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a09c bytes 85b70f94
+ 0086a0f4 bytes a3b70f94
~~~


<a id="compare-d726e0ba5120ea856cee0f8f64a33a37"></a>

### [`0086a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md) → [`0086a10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a10c.md) FUN_0086a10c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00848a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848a2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00848a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848a84.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md#insn-0086a104) · [`0086a114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md#insn-0086a114) · [`0086a128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a0b4.md#insn-0086a128)
- 新版 `0086a15c`（命令位置の公開資料なし） · `0086a16c`（命令位置の公開資料なし） · `0086a180`（命令位置の公開資料なし）

~~~diff
- 0086a104 ["INT_ADD", "register:40f0:8", ["const:86a104:8", "const:4:8"]]
- 0086a104 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a15c ["INT_ADD", "register:40f0:8", ["const:86a15c:8", "const:4:8"]]
+ 0086a15c ["CALL", null, ["callee:00c57f80:8"]]
- 0086a104 bytes 6bb70f94
+ 0086a15c bytes 89b70f94
- 0086a114 ["INT_ADD", "register:40f0:8", ["const:86a114:8", "const:4:8"]]
- 0086a114 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a16c ["INT_ADD", "register:40f0:8", ["const:86a16c:8", "const:4:8"]]
+ 0086a16c ["CALL", null, ["callee:00c57f80:8"]]
- 0086a114 bytes 67b70f94
+ 0086a16c bytes 85b70f94
- 0086a128 ["INT_ADD", "register:40f0:8", ["const:86a128:8", "const:4:8"]]
- 0086a128 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a180 ["INT_ADD", "register:40f0:8", ["const:86a180:8", "const:4:8"]]
+ 0086a180 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a128 bytes 62b70f94
+ 0086a180 bytes 80b70f94
~~~


<a id="compare-f162d226fbddf417b0623db898f4c26a"></a>

### [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) → [`0086a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a1bc.md) FUN_0086a1bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b20.md) [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) [`008fd054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd054.md) · 呼出先 2件 [`0086a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848b78.md) [`0086a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a1bc.md) [`008fc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc644.md) [`008fd0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd0a8.md) · 呼出先 2件 [`0086a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a1bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md#insn-0086a184) · [`0086a190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a164.md#insn-0086a190)
- 新版 `0086a1dc`（命令位置の公開資料なし） · `0086a1e8`（命令位置の公開資料なし）

~~~diff
- 0086a184 ["INT_ADD", "register:40f0:8", ["const:86a184:8", "const:4:8"]]
- 0086a184 ["CALL", null, ["local:b0:8"]]
+ 0086a1dc ["INT_ADD", "register:40f0:8", ["const:86a1dc:8", "const:4:8"]]
+ 0086a1dc ["CALL", null, ["local:b0:8"]]
- 0086a184 bytes f8ffff97
+ 0086a1dc bytes f8ffff97
- 0086a190 ["INT_ADD", "register:40f0:8", ["const:86a190:8", "const:4:8"]]
- 0086a190 ["CALL", null, ["local:b0:8"]]
+ 0086a1e8 ["INT_ADD", "register:40f0:8", ["const:86a1e8:8", "const:4:8"]]
+ 0086a1e8 ["CALL", null, ["local:b0:8"]]
- 0086a190 bytes f5ffff97
+ 0086a1e8 bytes f5ffff97
~~~


<a id="compare-39c436e5afde2ce06f639cede43cfba1"></a>

### [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) → [`0086a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a200.md) FUN_0086a200

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848b98.md) [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) [`00a3b884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3b884.md) · 呼出先 2件 [`0086a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848bf0.md) [`0086a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a200.md) [`00a3ab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3ab1c.md) [`00a3b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b8d8.md) · 呼出先 2件 [`0086a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a200.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md#insn-0086a1c8) · [`0086a1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1a8.md#insn-0086a1d4)
- 新版 `0086a220`（命令位置の公開資料なし） · `0086a22c`（命令位置の公開資料なし）

~~~diff
- 0086a1c8 ["INT_ADD", "register:40f0:8", ["const:86a1c8:8", "const:4:8"]]
- 0086a1c8 ["CALL", null, ["local:b0:8"]]
+ 0086a220 ["INT_ADD", "register:40f0:8", ["const:86a220:8", "const:4:8"]]
+ 0086a220 ["CALL", null, ["local:b0:8"]]
- 0086a1c8 bytes f8ffff97
+ 0086a220 bytes f8ffff97
- 0086a1d4 ["INT_ADD", "register:40f0:8", ["const:86a1d4:8", "const:4:8"]]
- 0086a1d4 ["CALL", null, ["local:b0:8"]]
+ 0086a22c ["INT_ADD", "register:40f0:8", ["const:86a22c:8", "const:4:8"]]
+ 0086a22c ["CALL", null, ["local:b0:8"]]
- 0086a1d4 bytes f5ffff97
+ 0086a22c bytes f5ffff97
~~~


<a id="compare-f1bae8bb10399d35a2de34da76a982c5"></a>

### [`0086a1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md) → [`0086a244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a244.md) FUN_0086a244

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00848c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848c20.md) [`00abd86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd86c.md) [`00abd8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd8ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00848c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848c78.md) [`00abd8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abd/00abd8dc.md) [`00abd95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abd/00abd95c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md#insn-0086a21c) · [`0086a22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md#insn-0086a22c) · [`0086a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md#insn-0086a23c)
- 新版 `0086a274`（命令位置の公開資料なし） · `0086a284`（命令位置の公開資料なし） · `0086a294`（命令位置の公開資料なし）

~~~diff
- 0086a21c ["INT_ADD", "register:40f0:8", ["const:86a21c:8", "const:4:8"]]
- 0086a21c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a274 ["INT_ADD", "register:40f0:8", ["const:86a274:8", "const:4:8"]]
+ 0086a274 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a21c bytes 25b70f94
+ 0086a274 bytes 43b70f94
- 0086a22c ["INT_ADD", "register:40f0:8", ["const:86a22c:8", "const:4:8"]]
- 0086a22c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a284 ["INT_ADD", "register:40f0:8", ["const:86a284:8", "const:4:8"]]
+ 0086a284 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a22c bytes 21b70f94
+ 0086a284 bytes 3fb70f94
- 0086a23c ["INT_ADD", "register:40f0:8", ["const:86a23c:8", "const:4:8"]]
- 0086a23c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a294 ["INT_ADD", "register:40f0:8", ["const:86a294:8", "const:4:8"]]
+ 0086a294 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a23c bytes 1db70f94
+ 0086a294 bytes 3bb70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a82a5cb321af6178faa60aec69dbdb"></a>

### [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) → [`0086a2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a2d0.md) FUN_0086a2d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848cfc.md) [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) [`00928318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00928/00928318.md) · 呼出先 2件 [`0086a278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848d54.md) [`0086a2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a2d0.md) [`0092836c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00928/0092836c.md) · 呼出先 2件 [`0086a2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a2d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md#insn-0086a294) · [`0086a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md#insn-0086a2a0) · [`0086a2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a278.md#insn-0086a2b0)
- 新版 `0086a2ec`（命令位置の公開資料なし） · `0086a2f8`（命令位置の公開資料なし） · `0086a308`（命令位置の公開資料なし）

~~~diff
- 0086a294 ["INT_ADD", "register:40f0:8", ["const:86a294:8", "const:4:8"]]
- 0086a294 ["CALL", null, ["local:b0:8"]]
+ 0086a2ec ["INT_ADD", "register:40f0:8", ["const:86a2ec:8", "const:4:8"]]
+ 0086a2ec ["CALL", null, ["local:b0:8"]]
- 0086a294 bytes f9ffff97
+ 0086a2ec bytes f9ffff97
- 0086a2a0 ["INT_ADD", "register:40f0:8", ["const:86a2a0:8", "const:4:8"]]
- 0086a2a0 ["CALL", null, ["local:b0:8"]]
+ 0086a2f8 ["INT_ADD", "register:40f0:8", ["const:86a2f8:8", "const:4:8"]]
+ 0086a2f8 ["CALL", null, ["local:b0:8"]]
- 0086a2a0 bytes f6ffff97
+ 0086a2f8 bytes f6ffff97
- 0086a2b0 ["INT_ADD", "register:40f0:8", ["const:86a2b0:8", "const:4:8"]]
- 0086a2b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a308 ["INT_ADD", "register:40f0:8", ["const:86a308:8", "const:4:8"]]
+ 0086a308 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a2b0 bytes 00b70f94
+ 0086a308 bytes 1eb70f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750200491033de42ffc6922d50d18405"></a>

### [`0086a2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md) → [`0086a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a330.md) FUN_0086a330

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00848f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848f94.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00848fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848fec.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md#insn-0086a328) · [`0086a338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md#insn-0086a338) · [`0086a34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a2d8.md#insn-0086a34c)
- 新版 `0086a380`（命令位置の公開資料なし） · `0086a390`（命令位置の公開資料なし） · `0086a3a4`（命令位置の公開資料なし）

~~~diff
- 0086a328 ["INT_ADD", "register:40f0:8", ["const:86a328:8", "const:4:8"]]
- 0086a328 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a380 ["INT_ADD", "register:40f0:8", ["const:86a380:8", "const:4:8"]]
+ 0086a380 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a328 bytes e2b60f94
+ 0086a380 bytes 00b70f94
- 0086a338 ["INT_ADD", "register:40f0:8", ["const:86a338:8", "const:4:8"]]
- 0086a338 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a390 ["INT_ADD", "register:40f0:8", ["const:86a390:8", "const:4:8"]]
+ 0086a390 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a338 bytes deb60f94
+ 0086a390 bytes fcb60f94
- 0086a34c ["INT_ADD", "register:40f0:8", ["const:86a34c:8", "const:4:8"]]
- 0086a34c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a3a4 ["INT_ADD", "register:40f0:8", ["const:86a3a4:8", "const:4:8"]]
+ 0086a3a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a34c bytes d9b60f94
+ 0086a3a4 bytes f7b60f94
~~~


<a id="compare-176424e7ca52561b02b10834ecdb1202"></a>

### [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) → [`0086a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a3e0.md) FUN_0086a3e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`00aa25e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa25e8.md) · 呼出先 2件 [`0086a388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md) [`0086a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a3e0.md) [`00aa2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa2/00aa2658.md) · 呼出先 2件 [`0086a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a3e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md#insn-0086a3a4) · [`0086a3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md#insn-0086a3b0) · [`0086a3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a388.md#insn-0086a3cc)
- 新版 `0086a3fc`（命令位置の公開資料なし） · `0086a408`（命令位置の公開資料なし） · `0086a424`（命令位置の公開資料なし）

~~~diff
- 0086a3a4 ["INT_ADD", "register:40f0:8", ["const:86a3a4:8", "const:4:8"]]
- 0086a3a4 ["CALL", null, ["local:b0:8"]]
+ 0086a3fc ["INT_ADD", "register:40f0:8", ["const:86a3fc:8", "const:4:8"]]
+ 0086a3fc ["CALL", null, ["local:b0:8"]]
- 0086a3a4 bytes f9ffff97
+ 0086a3fc bytes f9ffff97
- 0086a3b0 ["INT_ADD", "register:40f0:8", ["const:86a3b0:8", "const:4:8"]]
- 0086a3b0 ["CALL", null, ["local:b0:8"]]
+ 0086a408 ["INT_ADD", "register:40f0:8", ["const:86a408:8", "const:4:8"]]
+ 0086a408 ["CALL", null, ["local:b0:8"]]
- 0086a3b0 bytes f6ffff97
+ 0086a408 bytes f6ffff97
- 0086a3cc ["INT_ADD", "register:40f0:8", ["const:86a3cc:8", "const:4:8"]]
- 0086a3cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a424 ["INT_ADD", "register:40f0:8", ["const:86a424:8", "const:4:8"]]
+ 0086a424 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a3cc bytes b9b60f94
+ 0086a424 bytes d7b60f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-285c18b0cd490b677802c9bb9d9066d8"></a>

### [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) → [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) FUN_0086a444

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849304.md) [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) · 呼出先 2件 [`0086a3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084935c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084935c.md) [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) [`00b07a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md) · 呼出先 2件 [`0086a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a444.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md#insn-0086a408) · [`0086a414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md#insn-0086a414) · [`0086a430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a3ec.md#insn-0086a430)
- 新版 `0086a460`（命令位置の公開資料なし） · `0086a46c`（命令位置の公開資料なし） · `0086a488`（命令位置の公開資料なし）

~~~diff
- 0086a408 ["INT_ADD", "register:40f0:8", ["const:86a408:8", "const:4:8"]]
- 0086a408 ["CALL", null, ["local:b0:8"]]
+ 0086a460 ["INT_ADD", "register:40f0:8", ["const:86a460:8", "const:4:8"]]
+ 0086a460 ["CALL", null, ["local:b0:8"]]
- 0086a408 bytes f9ffff97
+ 0086a460 bytes f9ffff97
- 0086a414 ["INT_ADD", "register:40f0:8", ["const:86a414:8", "const:4:8"]]
- 0086a414 ["CALL", null, ["local:b0:8"]]
+ 0086a46c ["INT_ADD", "register:40f0:8", ["const:86a46c:8", "const:4:8"]]
+ 0086a46c ["CALL", null, ["local:b0:8"]]
- 0086a414 bytes f6ffff97
+ 0086a46c bytes f6ffff97
- 0086a430 ["INT_ADD", "register:40f0:8", ["const:86a430:8", "const:4:8"]]
- 0086a430 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a488 ["INT_ADD", "register:40f0:8", ["const:86a488:8", "const:4:8"]]
+ 0086a488 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a430 bytes a0b60f94
+ 0086a488 bytes beb60f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adab601324a1249f47515c07cdb1e778"></a>

### [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) → [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) FUN_0086a4b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) · 呼出先 2件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 8件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849458.md) [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`0097fb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097fb74.md) [`00981494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981494.md) · 呼出先 2件 [`0086a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a4b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md#insn-0086a47c) · [`0086a488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md#insn-0086a488) · [`0086a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md#insn-0086a498)
- 新版 `0086a4d4`（命令位置の公開資料なし） · `0086a4e0`（命令位置の公開資料なし） · `0086a4f0`（命令位置の公開資料なし）

~~~diff
- 0086a47c ["INT_ADD", "register:40f0:8", ["const:86a47c:8", "const:4:8"]]
- 0086a47c ["CALL", null, ["local:b0:8"]]
+ 0086a4d4 ["INT_ADD", "register:40f0:8", ["const:86a4d4:8", "const:4:8"]]
+ 0086a4d4 ["CALL", null, ["local:b0:8"]]
- 0086a47c bytes f9ffff97
+ 0086a4d4 bytes f9ffff97
- 0086a488 ["INT_ADD", "register:40f0:8", ["const:86a488:8", "const:4:8"]]
- 0086a488 ["CALL", null, ["local:b0:8"]]
+ 0086a4e0 ["INT_ADD", "register:40f0:8", ["const:86a4e0:8", "const:4:8"]]
+ 0086a4e0 ["CALL", null, ["local:b0:8"]]
- 0086a488 bytes f6ffff97
+ 0086a4e0 bytes f6ffff97
- 0086a498 ["INT_ADD", "register:40f0:8", ["const:86a498:8", "const:4:8"]]
- 0086a498 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a4f0 ["INT_ADD", "register:40f0:8", ["const:86a4f0:8", "const:4:8"]]
+ 0086a4f0 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a498 bytes 86b60f94
+ 0086a4f0 bytes a4b60f94
~~~


<a id="compare-aefdb9b5f0f0c3b5632233b6d68e6ae4"></a>

### [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) → [`0086a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a508.md) FUN_0086a508

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`009816cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md) · 呼出先 2件 [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849458.md) [`0086a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a508.md) [`00981720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00981/00981720.md) · 呼出先 2件 [`0086a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a508.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md#insn-0086a4d0) · [`0086a4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md#insn-0086a4dc)
- 新版 `0086a528`（命令位置の公開資料なし） · `0086a534`（命令位置の公開資料なし）

~~~diff
- 0086a4d0 ["INT_ADD", "register:40f0:8", ["const:86a4d0:8", "const:4:8"]]
- 0086a4d0 ["CALL", null, ["local:b0:8"]]
+ 0086a528 ["INT_ADD", "register:40f0:8", ["const:86a528:8", "const:4:8"]]
+ 0086a528 ["CALL", null, ["local:b0:8"]]
- 0086a4d0 bytes f8ffff97
+ 0086a528 bytes f8ffff97
- 0086a4dc ["INT_ADD", "register:40f0:8", ["const:86a4dc:8", "const:4:8"]]
- 0086a4dc ["CALL", null, ["local:b0:8"]]
+ 0086a534 ["INT_ADD", "register:40f0:8", ["const:86a534:8", "const:4:8"]]
+ 0086a534 ["CALL", null, ["local:b0:8"]]
- 0086a4dc bytes f5ffff97
+ 0086a534 bytes f5ffff97
~~~


