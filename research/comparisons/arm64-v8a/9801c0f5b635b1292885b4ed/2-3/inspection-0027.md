# v16.0.1 → v16.0.2 · 要調査の変更候補 (27)

[一覧の目次](README.md)

<a id="compare-130b38a70ddf354258cbb2b823082242"></a>

### [`0086a4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md) → [`0086a54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a54c.md) FUN_0086a54c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849400.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849458.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md#insn-0086a544) · [`0086a554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md#insn-0086a554) · [`0086a568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4f4.md#insn-0086a568)
- 新版 `0086a59c`（命令位置の公開資料なし） · `0086a5ac`（命令位置の公開資料なし） · `0086a5c0`（命令位置の公開資料なし）

~~~diff
- 0086a544 ["INT_ADD", "register:40f0:8", ["const:86a544:8", "const:4:8"]]
- 0086a544 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a59c ["INT_ADD", "register:40f0:8", ["const:86a59c:8", "const:4:8"]]
+ 0086a59c ["CALL", null, ["callee:00c57f80:8"]]
- 0086a544 bytes 5bb60f94
+ 0086a59c bytes 79b60f94
- 0086a554 ["INT_ADD", "register:40f0:8", ["const:86a554:8", "const:4:8"]]
- 0086a554 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a5ac ["INT_ADD", "register:40f0:8", ["const:86a5ac:8", "const:4:8"]]
+ 0086a5ac ["CALL", null, ["callee:00c57f80:8"]]
- 0086a554 bytes 57b60f94
+ 0086a5ac bytes 75b60f94
- 0086a568 ["INT_ADD", "register:40f0:8", ["const:86a568:8", "const:4:8"]]
- 0086a568 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a5c0 ["INT_ADD", "register:40f0:8", ["const:86a5c0:8", "const:4:8"]]
+ 0086a5c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a568 bytes 52b60f94
+ 0086a5c0 bytes 70b60f94
~~~


<a id="compare-b92d4530e3e09708e8eb72fd90225743"></a>

### [`0086a5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md) → [`0086a5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a5fc.md) FUN_0086a5fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849778.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008497d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008497d0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md#insn-0086a5f4) · [`0086a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md#insn-0086a604) · [`0086a618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a5a4.md#insn-0086a618)
- 新版 `0086a64c`（命令位置の公開資料なし） · `0086a65c`（命令位置の公開資料なし） · `0086a670`（命令位置の公開資料なし）

~~~diff
- 0086a5f4 ["INT_ADD", "register:40f0:8", ["const:86a5f4:8", "const:4:8"]]
- 0086a5f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a64c ["INT_ADD", "register:40f0:8", ["const:86a64c:8", "const:4:8"]]
+ 0086a64c ["CALL", null, ["callee:00c57f80:8"]]
- 0086a5f4 bytes 2fb60f94
+ 0086a64c bytes 4db60f94
- 0086a604 ["INT_ADD", "register:40f0:8", ["const:86a604:8", "const:4:8"]]
- 0086a604 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a65c ["INT_ADD", "register:40f0:8", ["const:86a65c:8", "const:4:8"]]
+ 0086a65c ["CALL", null, ["callee:00c57f80:8"]]
- 0086a604 bytes 2bb60f94
+ 0086a65c bytes 49b60f94
- 0086a618 ["INT_ADD", "register:40f0:8", ["const:86a618:8", "const:4:8"]]
- 0086a618 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a670 ["INT_ADD", "register:40f0:8", ["const:86a670:8", "const:4:8"]]
+ 0086a670 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a618 bytes 26b60f94
+ 0086a670 bytes 44b60f94
~~~


<a id="compare-430057e23ad784ae6a3047b6fd7b1dc1"></a>

### [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) → [`0086a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6ac.md) FUN_0086a6ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/0084987c.md) [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) · 呼出先 2件 [`0086a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008498d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/008498d4.md) [`0086a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6ac.md) · 呼出先 2件 [`0086a6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6ac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md#insn-0086a670) · [`0086a67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md#insn-0086a67c) · [`0086a68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a654.md#insn-0086a68c)
- 新版 `0086a6c8`（命令位置の公開資料なし） · `0086a6d4`（命令位置の公開資料なし） · `0086a6e4`（命令位置の公開資料なし）

~~~diff
- 0086a670 ["INT_ADD", "register:40f0:8", ["const:86a670:8", "const:4:8"]]
- 0086a670 ["CALL", null, ["local:b0:8"]]
+ 0086a6c8 ["INT_ADD", "register:40f0:8", ["const:86a6c8:8", "const:4:8"]]
+ 0086a6c8 ["CALL", null, ["local:b0:8"]]
- 0086a670 bytes f9ffff97
+ 0086a6c8 bytes f9ffff97
- 0086a67c ["INT_ADD", "register:40f0:8", ["const:86a67c:8", "const:4:8"]]
- 0086a67c ["CALL", null, ["local:b0:8"]]
+ 0086a6d4 ["INT_ADD", "register:40f0:8", ["const:86a6d4:8", "const:4:8"]]
+ 0086a6d4 ["CALL", null, ["local:b0:8"]]
- 0086a67c bytes f6ffff97
+ 0086a6d4 bytes f6ffff97
- 0086a68c ["INT_ADD", "register:40f0:8", ["const:86a68c:8", "const:4:8"]]
- 0086a68c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a6e4 ["INT_ADD", "register:40f0:8", ["const:86a6e4:8", "const:4:8"]]
+ 0086a6e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a68c bytes 09b60f94
+ 0086a6e4 bytes 27b60f94
~~~


<a id="compare-9578515ba2d3de06f0738131fb4aa704"></a>

### [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) → [`0086a6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6fc.md) FUN_0086a6fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`00a30fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30fe0.md) · 呼出先 3件 [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086a6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6fc.md) [`00a31034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31034.md) · 呼出先 3件 [`0086a6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6fc.md) [`0086a768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a768.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md#insn-0086a6c0) · [`0086a6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md#insn-0086a6cc) · [`0086a6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md#insn-0086a6d8)
- 新版 `0086a718`（命令位置の公開資料なし） · `0086a724`（命令位置の公開資料なし） · `0086a730`（命令位置の公開資料なし）

~~~diff
- 0086a6c0 ["INT_ADD", "register:40f0:8", ["const:86a6c0:8", "const:4:8"]]
- 0086a6c0 ["CALL", null, ["local:b0:8"]]
+ 0086a718 ["INT_ADD", "register:40f0:8", ["const:86a718:8", "const:4:8"]]
+ 0086a718 ["CALL", null, ["local:b0:8"]]
- 0086a6c0 bytes f9ffff97
+ 0086a718 bytes f9ffff97
- 0086a6cc ["INT_ADD", "register:40f0:8", ["const:86a6cc:8", "const:4:8"]]
- 0086a6cc ["CALL", null, ["local:b0:8"]]
+ 0086a724 ["INT_ADD", "register:40f0:8", ["const:86a724:8", "const:4:8"]]
+ 0086a724 ["CALL", null, ["local:b0:8"]]
- 0086a6cc bytes f6ffff97
+ 0086a724 bytes f6ffff97
- 0086a6d8 ["INT_ADD", "register:40f0:8", ["const:86a6d8:8", "const:4:8"]]
- 0086a6d8 ["CALL", null, ["callee:0086a768:8"]]
+ 0086a730 ["INT_ADD", "register:40f0:8", ["const:86a730:8", "const:4:8"]]
+ 0086a730 ["CALL", null, ["callee:0086a768:8"]]
- 0086a6d8 bytes 0e000094
+ 0086a730 bytes 0e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d152d5ddd94ec090f808ac1be2599e"></a>

### [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) → [`0086a768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a768.md) FUN_0086a768

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0086a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a6a4.md) [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) · 呼出先 2件 [`0086a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0086a6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a6fc.md) [`0086a768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a768.md) · 呼出先 2件 [`0086a768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a768.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md#insn-0086a72c) · [`0086a738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md#insn-0086a738) · [`0086a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a710.md#insn-0086a748)
- 新版 `0086a784`（命令位置の公開資料なし） · `0086a790`（命令位置の公開資料なし） · `0086a7a0`（命令位置の公開資料なし）

~~~diff
- 0086a72c ["INT_ADD", "register:40f0:8", ["const:86a72c:8", "const:4:8"]]
- 0086a72c ["CALL", null, ["local:b0:8"]]
+ 0086a784 ["INT_ADD", "register:40f0:8", ["const:86a784:8", "const:4:8"]]
+ 0086a784 ["CALL", null, ["local:b0:8"]]
- 0086a72c bytes f9ffff97
+ 0086a784 bytes f9ffff97
- 0086a738 ["INT_ADD", "register:40f0:8", ["const:86a738:8", "const:4:8"]]
- 0086a738 ["CALL", null, ["local:b0:8"]]
+ 0086a790 ["INT_ADD", "register:40f0:8", ["const:86a790:8", "const:4:8"]]
+ 0086a790 ["CALL", null, ["local:b0:8"]]
- 0086a738 bytes f6ffff97
+ 0086a790 bytes f6ffff97
- 0086a748 ["INT_ADD", "register:40f0:8", ["const:86a748:8", "const:4:8"]]
- 0086a748 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a7a0 ["INT_ADD", "register:40f0:8", ["const:86a7a0:8", "const:4:8"]]
+ 0086a7a0 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a748 bytes dab50f94
+ 0086a7a0 bytes f8b50f94
~~~


<a id="compare-49087f4d90d3642d28a3b59721952866"></a>

### [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) → [`0086a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7b8.md) FUN_0086a7b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849a48.md) [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) · 呼出先 2件 [`0086a760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849aa0.md) [`0086a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7b8.md) · 呼出先 2件 [`0086a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md#insn-0086a780) · [`0086a78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a760.md#insn-0086a78c)
- 新版 `0086a7d8`（命令位置の公開資料なし） · `0086a7e4`（命令位置の公開資料なし）

~~~diff
- 0086a780 ["INT_ADD", "register:40f0:8", ["const:86a780:8", "const:4:8"]]
- 0086a780 ["CALL", null, ["local:b0:8"]]
+ 0086a7d8 ["INT_ADD", "register:40f0:8", ["const:86a7d8:8", "const:4:8"]]
+ 0086a7d8 ["CALL", null, ["local:b0:8"]]
- 0086a780 bytes f8ffff97
+ 0086a7d8 bytes f8ffff97
- 0086a78c ["INT_ADD", "register:40f0:8", ["const:86a78c:8", "const:4:8"]]
- 0086a78c ["CALL", null, ["local:b0:8"]]
+ 0086a7e4 ["INT_ADD", "register:40f0:8", ["const:86a7e4:8", "const:4:8"]]
+ 0086a7e4 ["CALL", null, ["local:b0:8"]]
- 0086a78c bytes f5ffff97
+ 0086a7e4 bytes f5ffff97
~~~


<a id="compare-0925e44a7f32142cbfc9e22c18fa7f22"></a>

### [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) → [`0086a7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7fc.md) FUN_0086a7fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 2件 [`0086a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849afc.md) [`0086a7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7fc.md) [`00b096a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b096a0.md) [`00b097a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b097a4.md) · 呼出先 2件 [`0086a7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a7fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md#insn-0086a7c4) · [`0086a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md#insn-0086a7d0) · [`0086a80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a7a4.md#insn-0086a80c)
- 新版 `0086a81c`（命令位置の公開資料なし） · `0086a828`（命令位置の公開資料なし） · `0086a864`（命令位置の公開資料なし）

~~~diff
- 0086a7c4 ["INT_ADD", "register:40f0:8", ["const:86a7c4:8", "const:4:8"]]
- 0086a7c4 ["CALL", null, ["local:b0:8"]]
+ 0086a81c ["INT_ADD", "register:40f0:8", ["const:86a81c:8", "const:4:8"]]
+ 0086a81c ["CALL", null, ["local:b0:8"]]
- 0086a7c4 bytes f8ffff97
+ 0086a81c bytes f8ffff97
- 0086a7d0 ["INT_ADD", "register:40f0:8", ["const:86a7d0:8", "const:4:8"]]
- 0086a7d0 ["CALL", null, ["local:b0:8"]]
+ 0086a828 ["INT_ADD", "register:40f0:8", ["const:86a828:8", "const:4:8"]]
+ 0086a828 ["CALL", null, ["local:b0:8"]]
- 0086a7d0 bytes f5ffff97
+ 0086a828 bytes f5ffff97
- 0086a80c ["INT_ADD", "register:40f0:8", ["const:86a80c:8", "const:4:8"]]
- 0086a80c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a864 ["INT_ADD", "register:40f0:8", ["const:86a864:8", "const:4:8"]]
+ 0086a864 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a80c bytes a9b50f94
+ 0086a864 bytes c7b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4410dab70ddb77ceb0dc62a6f9c47767"></a>

### [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) → [`0086a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a890.md) FUN_0086a890

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849aa4.md) [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00b09604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09604.md) [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) · 呼出先 2件 [`0086a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849afc.md) [`0086a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a890.md) [`00b096a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b096a0.md) [`00b097a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b097a4.md) · 呼出先 2件 [`0086a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a890.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md#insn-0086a854) · [`0086a860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md#insn-0086a860) · [`0086a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a838.md#insn-0086a870)
- 新版 `0086a8ac`（命令位置の公開資料なし） · `0086a8b8`（命令位置の公開資料なし） · `0086a8c8`（命令位置の公開資料なし）

~~~diff
- 0086a854 ["INT_ADD", "register:40f0:8", ["const:86a854:8", "const:4:8"]]
- 0086a854 ["CALL", null, ["local:b0:8"]]
+ 0086a8ac ["INT_ADD", "register:40f0:8", ["const:86a8ac:8", "const:4:8"]]
+ 0086a8ac ["CALL", null, ["local:b0:8"]]
- 0086a854 bytes f9ffff97
+ 0086a8ac bytes f9ffff97
- 0086a860 ["INT_ADD", "register:40f0:8", ["const:86a860:8", "const:4:8"]]
- 0086a860 ["CALL", null, ["local:b0:8"]]
+ 0086a8b8 ["INT_ADD", "register:40f0:8", ["const:86a8b8:8", "const:4:8"]]
+ 0086a8b8 ["CALL", null, ["local:b0:8"]]
- 0086a860 bytes f6ffff97
+ 0086a8b8 bytes f6ffff97
- 0086a870 ["INT_ADD", "register:40f0:8", ["const:86a870:8", "const:4:8"]]
- 0086a870 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a8c8 ["INT_ADD", "register:40f0:8", ["const:86a8c8:8", "const:4:8"]]
+ 0086a8c8 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a870 bytes 90b50f94
+ 0086a8c8 bytes aeb50f94
~~~


<a id="compare-ea3c0a2ffa8772771cac85c7ec4f2d3c"></a>

### [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) → [`0086a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a8e0.md) FUN_0086a8e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`009c3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3350.md) [`009c7dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7dbc.md) · 呼出先 2件 [`0086a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849b3c.md) [`0086a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a8e0.md) [`009c33a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c3/009c33a4.md) [`009c7e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c7/009c7e10.md) · 呼出先 2件 [`0086a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a8e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md#insn-0086a8a4) · [`0086a8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md#insn-0086a8b0) · [`0086a8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a888.md#insn-0086a8c0)
- 新版 `0086a8fc`（命令位置の公開資料なし） · `0086a908`（命令位置の公開資料なし） · `0086a918`（命令位置の公開資料なし）

~~~diff
- 0086a8a4 ["INT_ADD", "register:40f0:8", ["const:86a8a4:8", "const:4:8"]]
- 0086a8a4 ["CALL", null, ["local:b0:8"]]
+ 0086a8fc ["INT_ADD", "register:40f0:8", ["const:86a8fc:8", "const:4:8"]]
+ 0086a8fc ["CALL", null, ["local:b0:8"]]
- 0086a8a4 bytes f9ffff97
+ 0086a8fc bytes f9ffff97
- 0086a8b0 ["INT_ADD", "register:40f0:8", ["const:86a8b0:8", "const:4:8"]]
- 0086a8b0 ["CALL", null, ["local:b0:8"]]
+ 0086a908 ["INT_ADD", "register:40f0:8", ["const:86a908:8", "const:4:8"]]
+ 0086a908 ["CALL", null, ["local:b0:8"]]
- 0086a8b0 bytes f6ffff97
+ 0086a908 bytes f6ffff97
- 0086a8c0 ["INT_ADD", "register:40f0:8", ["const:86a8c0:8", "const:4:8"]]
- 0086a8c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a918 ["INT_ADD", "register:40f0:8", ["const:86a918:8", "const:4:8"]]
+ 0086a918 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a8c0 bytes 7cb50f94
+ 0086a918 bytes 9ab50f94
~~~


<a id="compare-27cc3dafaf1913999d9d32531112ffc1"></a>

### [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) → [`0086a930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a930.md) FUN_0086a930

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`009c33dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c33dc.md) · 呼出先 2件 [`0086a8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849b3c.md) [`0086a930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a930.md) [`009c3430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c3/009c3430.md) · 呼出先 2件 [`0086a930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a930.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md#insn-0086a8f8) · [`0086a904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a8d8.md#insn-0086a904)
- 新版 `0086a950`（命令位置の公開資料なし） · `0086a95c`（命令位置の公開資料なし）

~~~diff
- 0086a8f8 ["INT_ADD", "register:40f0:8", ["const:86a8f8:8", "const:4:8"]]
- 0086a8f8 ["CALL", null, ["local:b0:8"]]
+ 0086a950 ["INT_ADD", "register:40f0:8", ["const:86a950:8", "const:4:8"]]
+ 0086a950 ["CALL", null, ["local:b0:8"]]
- 0086a8f8 bytes f8ffff97
+ 0086a950 bytes f8ffff97
- 0086a904 ["INT_ADD", "register:40f0:8", ["const:86a904:8", "const:4:8"]]
- 0086a904 ["CALL", null, ["local:b0:8"]]
+ 0086a95c ["INT_ADD", "register:40f0:8", ["const:86a95c:8", "const:4:8"]]
+ 0086a95c ["CALL", null, ["local:b0:8"]]
- 0086a904 bytes f5ffff97
+ 0086a95c bytes f5ffff97
~~~


<a id="compare-cc2f578a958c84386a5d0bd91f9c647b"></a>

### [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) → [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) FUN_0086a974

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b58.md) [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`00936cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/00936cb4.md) · 呼出先 3件 [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) [`0086a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849bb0.md) [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) [`00936d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00936/00936d08.md) · 呼出先 3件 [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) [`0086a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a9c0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md#insn-0086a93c) · [`0086a948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md#insn-0086a948) · [`0086a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md#insn-0086a950)
- 新版 `0086a994`（命令位置の公開資料なし） · `0086a9a0`（命令位置の公開資料なし） · `0086a9a8`（命令位置の公開資料なし）

~~~diff
- 0086a93c ["INT_ADD", "register:40f0:8", ["const:86a93c:8", "const:4:8"]]
- 0086a93c ["CALL", null, ["local:b0:8"]]
+ 0086a994 ["INT_ADD", "register:40f0:8", ["const:86a994:8", "const:4:8"]]
+ 0086a994 ["CALL", null, ["local:b0:8"]]
- 0086a93c bytes f8ffff97
+ 0086a994 bytes f8ffff97
- 0086a948 ["INT_ADD", "register:40f0:8", ["const:86a948:8", "const:4:8"]]
- 0086a948 ["CALL", null, ["local:b0:8"]]
+ 0086a9a0 ["INT_ADD", "register:40f0:8", ["const:86a9a0:8", "const:4:8"]]
+ 0086a9a0 ["CALL", null, ["local:b0:8"]]
- 0086a948 bytes f5ffff97
+ 0086a9a0 bytes f5ffff97
- 0086a950 ["INT_ADD", "register:40f0:8", ["const:86a950:8", "const:4:8"]]
- 0086a950 ["CALL", null, ["callee:0086a9c0:8"]]
+ 0086a9a8 ["INT_ADD", "register:40f0:8", ["const:86a9a8:8", "const:4:8"]]
+ 0086a9a8 ["CALL", null, ["callee:0086a9c0:8"]]
- 0086a950 bytes 06000094
+ 0086a9a8 bytes 06000094
~~~


<a id="compare-82bcacb03fdd1a02cba677fccbfd8124"></a>

### [`0086a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md) → [`0086a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a9c0.md) FUN_0086a9c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086a91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a91c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0086a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086a974.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086a99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md#insn-0086a99c) · [`0086a9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md#insn-0086a9bc) · [`0086a9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a968.md#insn-0086a9cc)
- 新版 `0086a9f4`（命令位置の公開資料なし） · `0086aa14`（命令位置の公開資料なし） · `0086aa24`（命令位置の公開資料なし）

~~~diff
- 0086a99c ["INT_ADD", "register:40f0:8", ["const:86a99c:8", "const:4:8"]]
- 0086a99c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086a9f4 ["INT_ADD", "register:40f0:8", ["const:86a9f4:8", "const:4:8"]]
+ 0086a9f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a99c bytes 45b50f94
+ 0086a9f4 bytes 63b50f94
- 0086a9bc ["INT_ADD", "register:40f0:8", ["const:86a9bc:8", "const:4:8"]]
- 0086a9bc ["CALL", null, ["callee:00c57f80:8"]]
+ 0086aa14 ["INT_ADD", "register:40f0:8", ["const:86aa14:8", "const:4:8"]]
+ 0086aa14 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a9bc bytes 3db50f94
+ 0086aa14 bytes 5bb50f94
- 0086a9cc ["INT_ADD", "register:40f0:8", ["const:86a9cc:8", "const:4:8"]]
- 0086a9cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0086aa24 ["INT_ADD", "register:40f0:8", ["const:86aa24:8", "const:4:8"]]
+ 0086aa24 ["CALL", null, ["callee:00c57f80:8"]]
- 0086a9cc bytes 39b50f94
+ 0086aa24 bytes 57b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46593588d28875baea43d5e64783405f"></a>

### [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) → [`0086aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aa50.md) FUN_0086aa50

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849b98.md) [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) · 呼出先 2件 [`0086a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849bf0.md) [`0086aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aa50.md) [`00939108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00939/00939108.md) · 呼出先 2件 [`0086aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aa50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md#insn-0086aa18) · [`0086aa24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md#insn-0086aa24) · [`0086aa5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a9f8.md#insn-0086aa5c)
- 新版 `0086aa70`（命令位置の公開資料なし） · `0086aa7c`（命令位置の公開資料なし） · `0086aab4`（命令位置の公開資料なし）

~~~diff
- 0086aa18 ["INT_ADD", "register:40f0:8", ["const:86aa18:8", "const:4:8"]]
- 0086aa18 ["CALL", null, ["local:b0:8"]]
+ 0086aa70 ["INT_ADD", "register:40f0:8", ["const:86aa70:8", "const:4:8"]]
+ 0086aa70 ["CALL", null, ["local:b0:8"]]
- 0086aa18 bytes f8ffff97
+ 0086aa70 bytes f8ffff97
- 0086aa24 ["INT_ADD", "register:40f0:8", ["const:86aa24:8", "const:4:8"]]
- 0086aa24 ["CALL", null, ["local:b0:8"]]
+ 0086aa7c ["INT_ADD", "register:40f0:8", ["const:86aa7c:8", "const:4:8"]]
+ 0086aa7c ["CALL", null, ["local:b0:8"]]
- 0086aa24 bytes f5ffff97
+ 0086aa7c bytes f5ffff97
- 0086aa5c ["INT_ADD", "register:40f0:8", ["const:86aa5c:8", "const:4:8"]]
- 0086aa5c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086aab4 ["INT_ADD", "register:40f0:8", ["const:86aab4:8", "const:4:8"]]
+ 0086aab4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086aa5c bytes 15b50f94
+ 0086aab4 bytes 33b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c10b01993e25d62134185e811318535"></a>

### [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) → [`0086aaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aaf0.md) FUN_0086aaf0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) [`00ab9f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab9f1c.md) · 呼出先 2件 [`0086aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086aaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aaf0.md) [`00ab9f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab9/00ab9f8c.md) · 呼出先 2件 [`0086aaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086aaf0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md#insn-0086aab8) · [`0086aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aa98.md#insn-0086aac4)
- 新版 `0086ab10`（命令位置の公開資料なし） · `0086ab1c`（命令位置の公開資料なし）

~~~diff
- 0086aab8 ["INT_ADD", "register:40f0:8", ["const:86aab8:8", "const:4:8"]]
- 0086aab8 ["CALL", null, ["local:b0:8"]]
+ 0086ab10 ["INT_ADD", "register:40f0:8", ["const:86ab10:8", "const:4:8"]]
+ 0086ab10 ["CALL", null, ["local:b0:8"]]
- 0086aab8 bytes f8ffff97
+ 0086ab10 bytes f8ffff97
- 0086aac4 ["INT_ADD", "register:40f0:8", ["const:86aac4:8", "const:4:8"]]
- 0086aac4 ["CALL", null, ["local:b0:8"]]
+ 0086ab1c ["INT_ADD", "register:40f0:8", ["const:86ab1c:8", "const:4:8"]]
+ 0086ab1c ["CALL", null, ["local:b0:8"]]
- 0086aac4 bytes f5ffff97
+ 0086ab1c bytes f5ffff97
~~~


<a id="compare-60814f0128f8f1d5858ebd869fad17e3"></a>

### [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) → [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) FUN_0086ab34

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`009e01d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md) [`009e0d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0d78.md) · 呼出先 3件 [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c68.md) [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`009e0228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md) [`009e0dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0dcc.md) · 呼出先 3件 [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086aaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md#insn-0086aaf8) · [`0086ab04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md#insn-0086ab04) · [`0086ab14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md#insn-0086ab14)
- 新版 `0086ab50`（命令位置の公開資料なし） · `0086ab5c`（命令位置の公開資料なし） · `0086ab6c`（命令位置の公開資料なし）

~~~diff
- 0086aaf8 ["INT_ADD", "register:40f0:8", ["const:86aaf8:8", "const:4:8"]]
- 0086aaf8 ["CALL", null, ["local:b0:8"]]
+ 0086ab50 ["INT_ADD", "register:40f0:8", ["const:86ab50:8", "const:4:8"]]
+ 0086ab50 ["CALL", null, ["local:b0:8"]]
- 0086aaf8 bytes f9ffff97
+ 0086ab50 bytes f9ffff97
- 0086ab04 ["INT_ADD", "register:40f0:8", ["const:86ab04:8", "const:4:8"]]
- 0086ab04 ["CALL", null, ["local:b0:8"]]
+ 0086ab5c ["INT_ADD", "register:40f0:8", ["const:86ab5c:8", "const:4:8"]]
+ 0086ab5c ["CALL", null, ["local:b0:8"]]
- 0086ab04 bytes f6ffff97
+ 0086ab5c bytes f6ffff97
- 0086ab14 ["INT_ADD", "register:40f0:8", ["const:86ab14:8", "const:4:8"]]
- 0086ab14 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ab6c ["INT_ADD", "register:40f0:8", ["const:86ab6c:8", "const:4:8"]]
+ 0086ab6c ["CALL", null, ["callee:00c57f80:8"]]
- 0086ab14 bytes e7b40f94
+ 0086ab6c bytes 05b50f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e21de3d2fb7ca78aaf08dae8681a6a50"></a>

### [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) → [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) FUN_0086ab90

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`009dfe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md) [`009e891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md) · 呼出先 3件 [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`0086abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`009dfe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe60.md) [`009e8970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8970.md) · 呼出先 3件 [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`0086ac08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ab54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md#insn-0086ab54) · [`0086ab60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md#insn-0086ab60) · [`0086ab70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md#insn-0086ab70)
- 新版 `0086abac`（命令位置の公開資料なし） · `0086abb8`（命令位置の公開資料なし） · `0086abc8`（命令位置の公開資料なし）

~~~diff
- 0086ab54 ["INT_ADD", "register:40f0:8", ["const:86ab54:8", "const:4:8"]]
- 0086ab54 ["CALL", null, ["local:b0:8"]]
+ 0086abac ["INT_ADD", "register:40f0:8", ["const:86abac:8", "const:4:8"]]
+ 0086abac ["CALL", null, ["local:b0:8"]]
- 0086ab54 bytes f9ffff97
+ 0086abac bytes f9ffff97
- 0086ab60 ["INT_ADD", "register:40f0:8", ["const:86ab60:8", "const:4:8"]]
- 0086ab60 ["CALL", null, ["local:b0:8"]]
+ 0086abb8 ["INT_ADD", "register:40f0:8", ["const:86abb8:8", "const:4:8"]]
+ 0086abb8 ["CALL", null, ["local:b0:8"]]
- 0086ab60 bytes f6ffff97
+ 0086abb8 bytes f6ffff97
- 0086ab70 ["INT_ADD", "register:40f0:8", ["const:86ab70:8", "const:4:8"]]
- 0086ab70 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086abc8 ["INT_ADD", "register:40f0:8", ["const:86abc8:8", "const:4:8"]]
+ 0086abc8 ["CALL", null, ["callee:00c57f80:8"]]
- 0086ab70 bytes d0b40f94
+ 0086abc8 bytes eeb40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4485c113c20420aed3ad9f5562e29d23"></a>

### [`0086abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md) → [`0086ac08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md) FUN_0086ac08

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`009e238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e238c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e23e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e23e0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ac54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md#insn-0086ac54) · [`0086aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md#insn-0086aca0) · [`0086acec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086abb0.md#insn-0086acec)
- 新版 `0086acac`（命令位置の公開資料なし） · `0086acf8`（命令位置の公開資料なし） · `0086ad44`（命令位置の公開資料なし）

~~~diff
- 0086ac54 ["INT_ADD", "register:40f0:8", ["const:86ac54:8", "const:4:8"]]
- 0086ac54 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086acac ["INT_ADD", "register:40f0:8", ["const:86acac:8", "const:4:8"]]
+ 0086acac ["CALL", null, ["callee:00c57f80:8"]]
- 0086ac54 bytes 97b40f94
+ 0086acac bytes b5b40f94
- 0086aca0 ["INT_ADD", "register:40f0:8", ["const:86aca0:8", "const:4:8"]]
- 0086aca0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086acf8 ["INT_ADD", "register:40f0:8", ["const:86acf8:8", "const:4:8"]]
+ 0086acf8 ["CALL", null, ["callee:00c57f80:8"]]
- 0086aca0 bytes 84b40f94
+ 0086acf8 bytes a2b40f94
- 0086acec ["INT_ADD", "register:40f0:8", ["const:86acec:8", "const:4:8"]]
- 0086acec ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ad44 ["INT_ADD", "register:40f0:8", ["const:86ad44:8", "const:4:8"]]
+ 0086ad44 ["CALL", null, ["callee:00c57f80:8"]]
- 0086acec bytes 71b40f94
+ 0086ad44 bytes 8fb40f94
~~~


<a id="compare-eaa4be114aa6c14c8aafc58f2468073d"></a>

### [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) → [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) FUN_0086ada8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849c10.md) [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`009e037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md) · 呼出先 2件 [`0086ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c68.md) [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) [`009e03d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md) · 呼出先 2件 [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ad70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md#insn-0086ad70) · [`0086ad7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md#insn-0086ad7c) · [`0086adb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ad50.md#insn-0086adb4)
- 新版 `0086adc8`（命令位置の公開資料なし） · `0086add4`（命令位置の公開資料なし） · `0086ae0c`（命令位置の公開資料なし）

~~~diff
- 0086ad70 ["INT_ADD", "register:40f0:8", ["const:86ad70:8", "const:4:8"]]
- 0086ad70 ["CALL", null, ["local:b0:8"]]
+ 0086adc8 ["INT_ADD", "register:40f0:8", ["const:86adc8:8", "const:4:8"]]
+ 0086adc8 ["CALL", null, ["local:b0:8"]]
- 0086ad70 bytes f8ffff97
+ 0086adc8 bytes f8ffff97
- 0086ad7c ["INT_ADD", "register:40f0:8", ["const:86ad7c:8", "const:4:8"]]
- 0086ad7c ["CALL", null, ["local:b0:8"]]
+ 0086add4 ["INT_ADD", "register:40f0:8", ["const:86add4:8", "const:4:8"]]
+ 0086add4 ["CALL", null, ["local:b0:8"]]
- 0086ad7c bytes f5ffff97
+ 0086add4 bytes f5ffff97
- 0086adb4 ["INT_ADD", "register:40f0:8", ["const:86adb4:8", "const:4:8"]]
- 0086adb4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ae0c ["INT_ADD", "register:40f0:8", ["const:86ae0c:8", "const:4:8"]]
+ 0086ae0c ["CALL", null, ["callee:00c57f80:8"]]
- 0086adb4 bytes 3fb40f94
+ 0086ae0c bytes 5db40f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c13c1879773f4b80ee91a3f739d24035"></a>

### [`0086aef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aef4.md) → [`0086af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086af4c.md) FUN_0086af4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008536f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/008536f8.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aef4.md#insn-0086af10)
- 新版 `0086af68`（命令位置の公開資料なし）

~~~diff
- 0086af10 ["INT_ADD", "register:40f0:8", ["const:86af10:8", "const:4:8"]]
- 0086af10 ["CALL", null, ["callee:00c57f50:8"]]
+ 0086af68 ["INT_ADD", "register:40f0:8", ["const:86af68:8", "const:4:8"]]
+ 0086af68 ["CALL", null, ["callee:00c57f50:8"]]
- 0086af10 bytes dcb30f94
+ 0086af68 bytes fab30f94
~~~


<a id="compare-5e0817c8105a9ccb13dc0fa2878ea2bd"></a>

### [`0086b174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b174.md) → [`0086b1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b1cc.md) FUN_0086b1cc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008536f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/008536f8.md) · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b174.md#insn-0086b190)
- 新版 `0086b1e8`（命令位置の公開資料なし）

~~~diff
- 0086b190 ["INT_ADD", "register:40f0:8", ["const:86b190:8", "const:4:8"]]
- 0086b190 ["CALL", null, ["callee:00c57f50:8"]]
+ 0086b1e8 ["INT_ADD", "register:40f0:8", ["const:86b1e8:8", "const:4:8"]]
+ 0086b1e8 ["CALL", null, ["callee:00c57f50:8"]]
- 0086b190 bytes 3cb30f94
+ 0086b1e8 bytes 5ab30f94
~~~


<a id="compare-006f7ecade25f35900ca43c75cd65879"></a>

### [`0086b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md) → [`0086b22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md) FUN_0086b22c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086b1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1a4.md) · 呼出先 7件 [`0048aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md) [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0086b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b1fc.md) · 呼出先 7件 [`0048aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048aa90.md) [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md#insn-0086b208) · [`0086b228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md#insn-0086b228) · [`0086b238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md#insn-0086b238)
- 新版 `0086b260`（命令位置の公開資料なし） · `0086b280`（命令位置の公開資料なし） · `0086b290`（命令位置の公開資料なし）

~~~diff
- 0086b208 ["INT_ADD", "register:40f0:8", ["const:86b208:8", "const:4:8"]]
- 0086b208 ["CALL", null, ["callee:00c585c0:8"]]
+ 0086b260 ["INT_ADD", "register:40f0:8", ["const:86b260:8", "const:4:8"]]
+ 0086b260 ["CALL", null, ["callee:00c585c0:8"]]
- 0086b208 bytes bab40f94
+ 0086b260 bytes d8b40f94
- 0086b228 ["INT_ADD", "register:40f0:8", ["const:86b228:8", "const:4:8"]]
- 0086b228 ["CALL", null, ["callee:0048aa90:8"]]
+ 0086b280 ["INT_ADD", "register:40f0:8", ["const:86b280:8", "const:4:8"]]
+ 0086b280 ["CALL", null, ["callee:0048aa90:8"]]
- 0086b228 bytes 0a7ef097
+ 0086b280 bytes 047ef097
- 0086b238 ["INT_ADD", "register:40f0:8", ["const:86b238:8", "const:4:8"]]
- 0086b238 ["CALL", null, ["callee:00c53d70:8"]]
+ 0086b290 ["INT_ADD", "register:40f0:8", ["const:86b290:8", "const:4:8"]]
+ 0086b290 ["CALL", null, ["callee:00c53d70:8"]]
- 0086b238 bytes a6a20f94
+ 0086b290 bytes b8a20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a2fc59168fb4cb7a7cdb09298ef21d"></a>

### [`0086b56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b56c.md) → [`0086b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b5c4.md) FUN_0086b5c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0049887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/0049887c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004988bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/004988bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b56c.md#insn-0086b580)
- 新版 `0086b5d8`（命令位置の公開資料なし）

~~~diff
- 0086b580 ["INT_ADD", "register:40f0:8", ["const:86b580:8", "const:4:8"]]
- 0086b580 ["CALL", null, ["callee:004988bc:8"]]
+ 0086b5d8 ["INT_ADD", "register:40f0:8", ["const:86b5d8:8", "const:4:8"]]
+ 0086b5d8 ["CALL", null, ["callee:004988bc:8"]]
- 0086b580 bytes bfb4f097
+ 0086b5d8 bytes b9b4f097
~~~


<a id="compare-5355ad288f4e9b379ede74a74c6996b4"></a>

### [`0086b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5a8.md) → [`0086b600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b600.md) FUN_0086b600

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`00498804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498804.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) [`00498844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498844.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5a8.md#insn-0086b5bc)
- 新版 `0086b614`（命令位置の公開資料なし）

~~~diff
- 0086b5bc ["INT_ADD", "register:40f0:8", ["const:86b5bc:8", "const:4:8"]]
- 0086b5bc ["CALL", null, ["callee:00498210:8"]]
+ 0086b614 ["INT_ADD", "register:40f0:8", ["const:86b614:8", "const:4:8"]]
+ 0086b614 ["CALL", null, ["callee:00498210:8"]]
- 0086b5bc bytes 05b3f097
+ 0086b614 bytes ffb2f097
~~~


<a id="compare-47c65fb1ba689e9ecb56c86542468dc5"></a>

### [`0086b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5e0.md) → [`0086b638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b638.md) FUN_0086b638

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0085c14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085c14c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0085c1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085c1a4.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5e0.md#insn-0086b624) · [`0086b648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5e0.md#insn-0086b648) · [`0086b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b5e0.md#insn-0086b660)
- 新版 `0086b67c`（命令位置の公開資料なし） · `0086b6a0`（命令位置の公開資料なし） · `0086b6b8`（命令位置の公開資料なし）

~~~diff
- 0086b624 ["INT_ADD", "register:40f0:8", ["const:86b624:8", "const:4:8"]]
- 0086b624 ["CALL", null, ["callee:0054079c:8"]]
+ 0086b67c ["INT_ADD", "register:40f0:8", ["const:86b67c:8", "const:4:8"]]
+ 0086b67c ["CALL", null, ["callee:0054079c:8"]]
- 0086b624 bytes 4e54f397
+ 0086b67c bytes 4854f397
- 0086b648 ["INT_ADD", "register:40f0:8", ["const:86b648:8", "const:4:8"]]
- 0086b648 ["CALL", null, ["callee:00c57f60:8"]]
+ 0086b6a0 ["INT_ADD", "register:40f0:8", ["const:86b6a0:8", "const:4:8"]]
+ 0086b6a0 ["CALL", null, ["callee:00c57f60:8"]]
- 0086b648 bytes 12b20f94
+ 0086b6a0 bytes 30b20f94
- 0086b660 ["INT_ADD", "register:40f0:8", ["const:86b660:8", "const:4:8"]]
- 0086b660 ["CALL", null, ["callee:00c580d0:8"]]
+ 0086b6b8 ["INT_ADD", "register:40f0:8", ["const:86b6b8:8", "const:4:8"]]
+ 0086b6b8 ["CALL", null, ["callee:00c580d0:8"]]
- 0086b660 bytes 68b20f94
+ 0086b6b8 bytes 86b20f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f34294eaccbba5921a457de1ebd44a73"></a>

### [`0086b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md) → [`0086ba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086ba28.md) FUN_0086ba28

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0085c14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085c14c.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0085c1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085c1a4.md) [`0086c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c098.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md#insn-0086b9f0) · [`0086ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md#insn-0086ba00) · [`0086ba38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md#insn-0086ba38)
- 新版 `0086ba48`（命令位置の公開資料なし） · `0086ba58`（命令位置の公開資料なし） · `0086ba90`（命令位置の公開資料なし）

~~~diff
- 0086b9f0 ["INT_ADD", "register:40f0:8", ["const:86b9f0:8", "const:4:8"]]
- 0086b9f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ba48 ["INT_ADD", "register:40f0:8", ["const:86ba48:8", "const:4:8"]]
+ 0086ba48 ["CALL", null, ["callee:00c57f80:8"]]
- 0086b9f0 bytes 30b10f94
+ 0086ba48 bytes 4eb10f94
- 0086ba00 ["INT_ADD", "register:40f0:8", ["const:86ba00:8", "const:4:8"]]
- 0086ba00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ba58 ["INT_ADD", "register:40f0:8", ["const:86ba58:8", "const:4:8"]]
+ 0086ba58 ["CALL", null, ["callee:00c57f80:8"]]
- 0086ba00 bytes 2cb10f94
+ 0086ba58 bytes 4ab10f94
- 0086ba38 ["INT_ADD", "register:40f0:8", ["const:86ba38:8", "const:4:8"]]
- 0086ba38 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086ba90 ["INT_ADD", "register:40f0:8", ["const:86ba90:8", "const:4:8"]]
+ 0086ba90 ["CALL", null, ["callee:00c57f80:8"]]
- 0086ba38 bytes 1eb10f94
+ 0086ba90 bytes 3cb10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f41f1b75c07477ae3ba307dfecabcd5f"></a>

### [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) → [`0086bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bb60.md) FUN_0086bb60

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bb60.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`0086bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md#insn-0086bb24) · [`0086bb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md#insn-0086bb30) · [`0086bb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb08.md#insn-0086bb3c)
- 新版 `0086bb7c`（命令位置の公開資料なし） · `0086bb88`（命令位置の公開資料なし） · `0086bb94`（命令位置の公開資料なし）

~~~diff
- 0086bb24 ["INT_ADD", "register:40f0:8", ["const:86bb24:8", "const:4:8"]]
- 0086bb24 ["CALL", null, ["local:b0:8"]]
+ 0086bb7c ["INT_ADD", "register:40f0:8", ["const:86bb7c:8", "const:4:8"]]
+ 0086bb7c ["CALL", null, ["local:b0:8"]]
- 0086bb24 bytes f9ffff97
+ 0086bb7c bytes f9ffff97
- 0086bb30 ["INT_ADD", "register:40f0:8", ["const:86bb30:8", "const:4:8"]]
- 0086bb30 ["CALL", null, ["local:b0:8"]]
+ 0086bb88 ["INT_ADD", "register:40f0:8", ["const:86bb88:8", "const:4:8"]]
+ 0086bb88 ["CALL", null, ["local:b0:8"]]
- 0086bb30 bytes f6ffff97
+ 0086bb88 bytes f6ffff97
- 0086bb3c ["INT_ADD", "register:40f0:8", ["const:86bb3c:8", "const:4:8"]]
- 0086bb3c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086bb94 ["INT_ADD", "register:40f0:8", ["const:86bb94:8", "const:4:8"]]
+ 0086bb94 ["CALL", null, ["callee:00c57f80:8"]]
- 0086bb3c bytes ddb00f94
+ 0086bb94 bytes fbb00f94
~~~


<a id="compare-03970be9e2fd2a9c098ac68a781083e7"></a>

### [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) → [`0086bbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbac.md) FUN_0086bbac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849ae4.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`009c3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c3/009c3350.md) · 呼出先 2件 [`0086bb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849b3c.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086bbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbac.md) [`009c33a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c3/009c33a4.md) · 呼出先 2件 [`0086bbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md#insn-0086bb74) · [`0086bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb54.md#insn-0086bb80)
- 新版 `0086bbcc`（命令位置の公開資料なし） · `0086bbd8`（命令位置の公開資料なし）

~~~diff
- 0086bb74 ["INT_ADD", "register:40f0:8", ["const:86bb74:8", "const:4:8"]]
- 0086bb74 ["CALL", null, ["local:b0:8"]]
+ 0086bbcc ["INT_ADD", "register:40f0:8", ["const:86bbcc:8", "const:4:8"]]
+ 0086bbcc ["CALL", null, ["local:b0:8"]]
- 0086bb74 bytes f8ffff97
+ 0086bbcc bytes f8ffff97
- 0086bb80 ["INT_ADD", "register:40f0:8", ["const:86bb80:8", "const:4:8"]]
- 0086bb80 ["CALL", null, ["local:b0:8"]]
+ 0086bbd8 ["INT_ADD", "register:40f0:8", ["const:86bbd8:8", "const:4:8"]]
+ 0086bbd8 ["CALL", null, ["local:b0:8"]]
- 0086bb80 bytes f5ffff97
+ 0086bbd8 bytes f5ffff97
~~~


<a id="compare-e26ef31dea96d6dd3ff8905e1d7b231f"></a>

### [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) → [`0086bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbf0.md) FUN_0086bbf0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) · 呼出先 3件 [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849870.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`0086bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbf0.md) · 呼出先 3件 [`0086bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbf0.md) [`0086bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bc50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md#insn-0086bbb4) · [`0086bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md#insn-0086bbc0) · [`0086bbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md#insn-0086bbd8)
- 新版 `0086bc0c`（命令位置の公開資料なし） · `0086bc18`（命令位置の公開資料なし） · `0086bc30`（命令位置の公開資料なし）

~~~diff
- 0086bbb4 ["INT_ADD", "register:40f0:8", ["const:86bbb4:8", "const:4:8"]]
- 0086bbb4 ["CALL", null, ["local:b0:8"]]
+ 0086bc0c ["INT_ADD", "register:40f0:8", ["const:86bc0c:8", "const:4:8"]]
+ 0086bc0c ["CALL", null, ["local:b0:8"]]
- 0086bbb4 bytes f9ffff97
+ 0086bc0c bytes f9ffff97
- 0086bbc0 ["INT_ADD", "register:40f0:8", ["const:86bbc0:8", "const:4:8"]]
- 0086bbc0 ["CALL", null, ["local:b0:8"]]
+ 0086bc18 ["INT_ADD", "register:40f0:8", ["const:86bc18:8", "const:4:8"]]
+ 0086bc18 ["CALL", null, ["local:b0:8"]]
- 0086bbc0 bytes f6ffff97
+ 0086bc18 bytes f6ffff97
- 0086bbd8 ["INT_ADD", "register:40f0:8", ["const:86bbd8:8", "const:4:8"]]
- 0086bbd8 ["CALL", null, ["callee:0086bc50:8"]]
+ 0086bc30 ["INT_ADD", "register:40f0:8", ["const:86bc30:8", "const:4:8"]]
+ 0086bc30 ["CALL", null, ["callee:0086bc50:8"]]
- 0086bbd8 bytes 08000094
+ 0086bc30 bytes 08000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116f2171e8dddfc8d5a143e91623f871"></a>

### [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) → [`0086bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bc50.md) FUN_0086bc50

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0086bb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bb98.md) [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00a6a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a2a0.md) [`00a6a660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6a660.md) · 呼出先 3件 [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`0086bc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0086bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bbf0.md) [`0086bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bc50.md) [`00a6a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6a/00a6a310.md) [`00a6a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6a/00a6a6d0.md) · 呼出先 3件 [`0086bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bc50.md) [`0086bcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bcac.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md#insn-0086bc14) · [`0086bc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md#insn-0086bc20) · [`0086bc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md#insn-0086bc34)
- 新版 `0086bc6c`（命令位置の公開資料なし） · `0086bc78`（命令位置の公開資料なし） · `0086bc8c`（命令位置の公開資料なし）

~~~diff
- 0086bc14 ["INT_ADD", "register:40f0:8", ["const:86bc14:8", "const:4:8"]]
- 0086bc14 ["CALL", null, ["local:b0:8"]]
+ 0086bc6c ["INT_ADD", "register:40f0:8", ["const:86bc6c:8", "const:4:8"]]
+ 0086bc6c ["CALL", null, ["local:b0:8"]]
- 0086bc14 bytes f9ffff97
+ 0086bc6c bytes f9ffff97
- 0086bc20 ["INT_ADD", "register:40f0:8", ["const:86bc20:8", "const:4:8"]]
- 0086bc20 ["CALL", null, ["local:b0:8"]]
+ 0086bc78 ["INT_ADD", "register:40f0:8", ["const:86bc78:8", "const:4:8"]]
+ 0086bc78 ["CALL", null, ["local:b0:8"]]
- 0086bc20 bytes f6ffff97
+ 0086bc78 bytes f6ffff97
- 0086bc34 ["INT_ADD", "register:40f0:8", ["const:86bc34:8", "const:4:8"]]
- 0086bc34 ["CALL", null, ["callee:0086bcac:8"]]
+ 0086bc8c ["INT_ADD", "register:40f0:8", ["const:86bc8c:8", "const:4:8"]]
+ 0086bc8c ["CALL", null, ["callee:0086bcac:8"]]
- 0086bc34 bytes 08000094
+ 0086bc8c bytes 08000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1248158c70c89a649ca3b1597680c08"></a>

### [`0086bc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md) → [`0086bcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bcac.md) FUN_0086bcac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0086bbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bbf8.md) [`00a6c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c218.md) [`00a6c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6c44c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0086bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bc50.md) [`00a6c288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c288.md) [`00a6c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c4bc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md#insn-0086bc78) · [`0086bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md#insn-0086bc8c) · [`0086bc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bc54.md#insn-0086bc94)
- 新版 `0086bcd0`（命令位置の公開資料なし） · `0086bce4`（命令位置の公開資料なし） · `0086bcec`（命令位置の公開資料なし）

~~~diff
- 0086bc78 ["INT_ADD", "register:40f0:8", ["const:86bc78:8", "const:4:8"]]
- 0086bc78 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086bcd0 ["INT_ADD", "register:40f0:8", ["const:86bcd0:8", "const:4:8"]]
+ 0086bcd0 ["CALL", null, ["callee:00c53da0:8"]]
- 0086bc78 bytes 22a00f94
+ 0086bcd0 bytes 34a00f94
- 0086bc8c ["COPY", "register:0:8", ["register:4040:8"]]
- 0086bc8c ["INT_ADD", "register:40f0:8", ["const:86bc8c:8", "const:4:8"]]
- 0086bc8c ["CALLIND", null, ["register:0:8"]]
+ 0086bce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0086bce4 ["INT_ADD", "register:40f0:8", ["const:86bce4:8", "const:4:8"]]
+ 0086bce4 ["CALLIND", null, ["register:0:8"]]
- 0086bc8c bytes 00013fd6
+ 0086bce4 bytes 00013fd6
- 0086bc94 ["INT_ADD", "register:40f0:8", ["const:86bc94:8", "const:4:8"]]
- 0086bc94 ["CALL", null, ["callee:00c57f50:8"]]
+ 0086bcec ["INT_ADD", "register:40f0:8", ["const:86bcec:8", "const:4:8"]]
+ 0086bcec ["CALL", null, ["callee:00c57f50:8"]]
- 0086bc94 bytes 7bb00f94
+ 0086bcec bytes 99b00f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a99d9593aa611c8ede0b7446ad2344c7"></a>

### [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) → [`0086be10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be10.md) FUN_0086be10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849818.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00a69154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69154.md) · 呼出先 4件 [`0086bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849870.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`0086be10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be10.md) [`00a691c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a691c4.md) · 呼出先 4件 [`0086be10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be10.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md#insn-0086bdd4) · [`0086bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md#insn-0086bde0) · [`0086bdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bdb8.md#insn-0086bdf4)
- 新版 `0086be2c`（命令位置の公開資料なし） · `0086be38`（命令位置の公開資料なし） · `0086be4c`（命令位置の公開資料なし）

~~~diff
- 0086bdd4 ["INT_ADD", "register:40f0:8", ["const:86bdd4:8", "const:4:8"]]
- 0086bdd4 ["CALL", null, ["local:b0:8"]]
+ 0086be2c ["INT_ADD", "register:40f0:8", ["const:86be2c:8", "const:4:8"]]
+ 0086be2c ["CALL", null, ["local:b0:8"]]
- 0086bdd4 bytes f9ffff97
+ 0086be2c bytes f9ffff97
- 0086bde0 ["INT_ADD", "register:40f0:8", ["const:86bde0:8", "const:4:8"]]
- 0086bde0 ["CALL", null, ["local:b0:8"]]
+ 0086be38 ["INT_ADD", "register:40f0:8", ["const:86be38:8", "const:4:8"]]
+ 0086be38 ["CALL", null, ["local:b0:8"]]
- 0086bde0 bytes f6ffff97
+ 0086be38 bytes f6ffff97
- 0086bdf4 ["INT_ADD", "register:40f0:8", ["const:86bdf4:8", "const:4:8"]]
- 0086bdf4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086be4c ["INT_ADD", "register:40f0:8", ["const:86be4c:8", "const:4:8"]]
+ 0086be4c ["CALL", null, ["callee:00c53da0:8"]]
- 0086bdf4 bytes c39f0f94
+ 0086be4c bytes d59f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-938d55966f22382bc7cf448dd157323e"></a>

### [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) → [`0086be80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be80.md) FUN_0086be80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086be28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086be80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be80.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`0086be80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086be80.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086be48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md#insn-0086be48) · [`0086be54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be28.md#insn-0086be54)
- 新版 `0086bea0`（命令位置の公開資料なし） · `0086beac`（命令位置の公開資料なし）

~~~diff
- 0086be48 ["INT_ADD", "register:40f0:8", ["const:86be48:8", "const:4:8"]]
- 0086be48 ["CALL", null, ["local:b0:8"]]
+ 0086bea0 ["INT_ADD", "register:40f0:8", ["const:86bea0:8", "const:4:8"]]
+ 0086bea0 ["CALL", null, ["local:b0:8"]]
- 0086be48 bytes f8ffff97
+ 0086bea0 bytes f8ffff97
- 0086be54 ["INT_ADD", "register:40f0:8", ["const:86be54:8", "const:4:8"]]
- 0086be54 ["CALL", null, ["local:b0:8"]]
+ 0086beac ["INT_ADD", "register:40f0:8", ["const:86beac:8", "const:4:8"]]
+ 0086beac ["CALL", null, ["local:b0:8"]]
- 0086be54 bytes f5ffff97
+ 0086beac bytes f5ffff97
~~~


<a id="compare-17517ceee5f3a009015728e770e4e71e"></a>

### [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) → [`0086bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bec4.md) FUN_0086bec4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008492d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/008492d4.md) [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) [`00aa2a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa2a18.md) · 呼出先 2件 [`0086be6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084932c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/0084932c.md) [`0086bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bec4.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) [`00aa2a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa2/00aa2a88.md) · 呼出先 2件 [`0086bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bec4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086be8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md#insn-0086be8c) · [`0086be98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086be6c.md#insn-0086be98)
- 新版 `0086bee4`（命令位置の公開資料なし） · `0086bef0`（命令位置の公開資料なし）

~~~diff
- 0086be8c ["INT_ADD", "register:40f0:8", ["const:86be8c:8", "const:4:8"]]
- 0086be8c ["CALL", null, ["local:b0:8"]]
+ 0086bee4 ["INT_ADD", "register:40f0:8", ["const:86bee4:8", "const:4:8"]]
+ 0086bee4 ["CALL", null, ["local:b0:8"]]
- 0086be8c bytes f8ffff97
+ 0086bee4 bytes f8ffff97
- 0086be98 ["INT_ADD", "register:40f0:8", ["const:86be98:8", "const:4:8"]]
- 0086be98 ["CALL", null, ["local:b0:8"]]
+ 0086bef0 ["INT_ADD", "register:40f0:8", ["const:86bef0:8", "const:4:8"]]
+ 0086bef0 ["CALL", null, ["local:b0:8"]]
- 0086be98 bytes f5ffff97
+ 0086bef0 bytes f5ffff97
~~~


<a id="compare-69cbdd54e962544324e4b6ebcb55f863"></a>

### [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) → [`0086bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf08.md) FUN_0086bf08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) · 呼出先 2件 [`0086beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf08.md) · 呼出先 2件 [`0086bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf08.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086becc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md#insn-0086becc) · [`0086bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md#insn-0086bed8) · [`0086bee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086beb0.md#insn-0086bee8)
- 新版 `0086bf24`（命令位置の公開資料なし） · `0086bf30`（命令位置の公開資料なし） · `0086bf40`（命令位置の公開資料なし）

~~~diff
- 0086becc ["INT_ADD", "register:40f0:8", ["const:86becc:8", "const:4:8"]]
- 0086becc ["CALL", null, ["local:b0:8"]]
+ 0086bf24 ["INT_ADD", "register:40f0:8", ["const:86bf24:8", "const:4:8"]]
+ 0086bf24 ["CALL", null, ["local:b0:8"]]
- 0086becc bytes f9ffff97
+ 0086bf24 bytes f9ffff97
- 0086bed8 ["INT_ADD", "register:40f0:8", ["const:86bed8:8", "const:4:8"]]
- 0086bed8 ["CALL", null, ["local:b0:8"]]
+ 0086bf30 ["INT_ADD", "register:40f0:8", ["const:86bf30:8", "const:4:8"]]
+ 0086bf30 ["CALL", null, ["local:b0:8"]]
- 0086bed8 bytes f6ffff97
+ 0086bf30 bytes f6ffff97
- 0086bee8 ["INT_ADD", "register:40f0:8", ["const:86bee8:8", "const:4:8"]]
- 0086bee8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086bf40 ["INT_ADD", "register:40f0:8", ["const:86bf40:8", "const:4:8"]]
+ 0086bf40 ["CALL", null, ["callee:00c57f80:8"]]
- 0086bee8 bytes f2af0f94
+ 0086bf40 bytes 10b00f94
~~~


<a id="compare-203db205bfb20a4b0d54c2a61fc06fa2"></a>

### [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) → [`0086bf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf58.md) FUN_0086bf58

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 2件 [`0086bf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086bf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf58.md) [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 2件 [`0086bf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bf58.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md#insn-0086bf1c) · [`0086bf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md#insn-0086bf28) · [`0086bf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf00.md#insn-0086bf38)
- 新版 `0086bf74`（命令位置の公開資料なし） · `0086bf80`（命令位置の公開資料なし） · `0086bf90`（命令位置の公開資料なし）

~~~diff
- 0086bf1c ["INT_ADD", "register:40f0:8", ["const:86bf1c:8", "const:4:8"]]
- 0086bf1c ["CALL", null, ["local:b0:8"]]
+ 0086bf74 ["INT_ADD", "register:40f0:8", ["const:86bf74:8", "const:4:8"]]
+ 0086bf74 ["CALL", null, ["local:b0:8"]]
- 0086bf1c bytes f9ffff97
+ 0086bf74 bytes f9ffff97
- 0086bf28 ["INT_ADD", "register:40f0:8", ["const:86bf28:8", "const:4:8"]]
- 0086bf28 ["CALL", null, ["local:b0:8"]]
+ 0086bf80 ["INT_ADD", "register:40f0:8", ["const:86bf80:8", "const:4:8"]]
+ 0086bf80 ["CALL", null, ["local:b0:8"]]
- 0086bf28 bytes f6ffff97
+ 0086bf80 bytes f6ffff97
- 0086bf38 ["INT_ADD", "register:40f0:8", ["const:86bf38:8", "const:4:8"]]
- 0086bf38 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086bf90 ["INT_ADD", "register:40f0:8", ["const:86bf90:8", "const:4:8"]]
+ 0086bf90 ["CALL", null, ["callee:00c57f80:8"]]
- 0086bf38 bytes deaf0f94
+ 0086bf90 bytes fcaf0f94
~~~


<a id="compare-5eff6454d8258421bbb3204545542802"></a>

### [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) → [`0086bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bfa8.md) FUN_0086bfa8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) · 呼出先 3件 [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) [`0086bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bfa8.md) · 呼出先 3件 [`0086bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bfa8.md) [`0086bff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bff4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md#insn-0086bf70) · [`0086bf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md#insn-0086bf7c) · [`0086bf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md#insn-0086bf84)
- 新版 `0086bfc8`（命令位置の公開資料なし） · `0086bfd4`（命令位置の公開資料なし） · `0086bfdc`（命令位置の公開資料なし）

~~~diff
- 0086bf70 ["INT_ADD", "register:40f0:8", ["const:86bf70:8", "const:4:8"]]
- 0086bf70 ["CALL", null, ["local:b0:8"]]
+ 0086bfc8 ["INT_ADD", "register:40f0:8", ["const:86bfc8:8", "const:4:8"]]
+ 0086bfc8 ["CALL", null, ["local:b0:8"]]
- 0086bf70 bytes f8ffff97
+ 0086bfc8 bytes f8ffff97
- 0086bf7c ["INT_ADD", "register:40f0:8", ["const:86bf7c:8", "const:4:8"]]
- 0086bf7c ["CALL", null, ["local:b0:8"]]
+ 0086bfd4 ["INT_ADD", "register:40f0:8", ["const:86bfd4:8", "const:4:8"]]
+ 0086bfd4 ["CALL", null, ["local:b0:8"]]
- 0086bf7c bytes f5ffff97
+ 0086bfd4 bytes f5ffff97
- 0086bf84 ["INT_ADD", "register:40f0:8", ["const:86bf84:8", "const:4:8"]]
- 0086bf84 ["CALL", null, ["callee:0086bff4:8"]]
+ 0086bfdc ["INT_ADD", "register:40f0:8", ["const:86bfdc:8", "const:4:8"]]
+ 0086bfdc ["CALL", null, ["callee:0086bff4:8"]]
- 0086bf84 bytes 06000094
+ 0086bfdc bytes 06000094
~~~


<a id="compare-8e81f6c79ea146315aea4a6d38c684d9"></a>

### [`0086bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md) → [`0086bff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bff4.md) FUN_0086bff4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf50.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0086bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086bfa8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md#insn-0086bfe8) · [`0086bff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md#insn-0086bff8) · [`0086c004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086bf9c.md#insn-0086c004)
- 新版 `0086c040`（命令位置の公開資料なし） · `0086c050`（命令位置の公開資料なし） · `0086c05c`（命令位置の公開資料なし）

~~~diff
- 0086bfe8 ["INT_ADD", "register:40f0:8", ["const:86bfe8:8", "const:4:8"]]
- 0086bfe8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c040 ["INT_ADD", "register:40f0:8", ["const:86c040:8", "const:4:8"]]
+ 0086c040 ["CALL", null, ["callee:00c57f80:8"]]
- 0086bfe8 bytes b2af0f94
+ 0086c040 bytes d0af0f94
- 0086bff8 ["INT_ADD", "register:40f0:8", ["const:86bff8:8", "const:4:8"]]
- 0086bff8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c050 ["INT_ADD", "register:40f0:8", ["const:86c050:8", "const:4:8"]]
+ 0086c050 ["CALL", null, ["callee:00c57f80:8"]]
- 0086bff8 bytes aeaf0f94
+ 0086c050 bytes ccaf0f94
- 0086c004 ["INT_ADD", "register:40f0:8", ["const:86c004:8", "const:4:8"]]
- 0086c004 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c05c ["INT_ADD", "register:40f0:8", ["const:86c05c:8", "const:4:8"]]
+ 0086c05c ["CALL", null, ["callee:00c57f80:8"]]
- 0086c004 bytes abaf0f94
+ 0086c05c bytes c9af0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09eeaac08e696c956a9198416ebe06ab"></a>

### [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) → [`0086c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c098.md) FUN_0086c098

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 3件 [`0086b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b9d0.md) [`0086c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c098.md) [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 3件 [`0086ba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086ba28.md) [`0086c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c098.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md#insn-0086c060) · [`0086c06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md#insn-0086c06c) · [`0086c074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c040.md#insn-0086c074)
- 新版 `0086c0b8`（命令位置の公開資料なし） · `0086c0c4`（命令位置の公開資料なし） · `0086c0cc`（命令位置の公開資料なし）

~~~diff
- 0086c060 ["INT_ADD", "register:40f0:8", ["const:86c060:8", "const:4:8"]]
- 0086c060 ["CALL", null, ["local:b0:8"]]
+ 0086c0b8 ["INT_ADD", "register:40f0:8", ["const:86c0b8:8", "const:4:8"]]
+ 0086c0b8 ["CALL", null, ["local:b0:8"]]
- 0086c060 bytes f8ffff97
+ 0086c0b8 bytes f8ffff97
- 0086c06c ["INT_ADD", "register:40f0:8", ["const:86c06c:8", "const:4:8"]]
- 0086c06c ["CALL", null, ["local:b0:8"]]
+ 0086c0c4 ["INT_ADD", "register:40f0:8", ["const:86c0c4:8", "const:4:8"]]
+ 0086c0c4 ["CALL", null, ["local:b0:8"]]
- 0086c06c bytes f5ffff97
+ 0086c0c4 bytes f5ffff97
- 0086c074 ["INT_ADD", "register:40f0:8", ["const:86c074:8", "const:4:8"]]
- 0086c074 ["CALL", null, ["callee:0086ba28:8"]]
+ 0086c0cc ["INT_ADD", "register:40f0:8", ["const:86c0cc:8", "const:4:8"]]
+ 0086c0cc ["CALL", null, ["callee:0086ba28:8"]]
- 0086c074 bytes 57feff97
+ 0086c0cc bytes 57feff97
~~~


<a id="compare-5008523d82426acaaa36a304e5c769eb"></a>

### [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) → [`0086c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c0e4.md) FUN_0086c0e4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) · 呼出先 4件 [`0086c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c0e4.md) · 呼出先 4件 [`0086c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c0e4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md#insn-0086c0ac) · [`0086c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md#insn-0086c0b8) · [`0086c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c08c.md#insn-0086c0f4)
- 新版 `0086c104`（命令位置の公開資料なし） · `0086c110`（命令位置の公開資料なし） · `0086c14c`（命令位置の公開資料なし）

~~~diff
- 0086c0ac ["INT_ADD", "register:40f0:8", ["const:86c0ac:8", "const:4:8"]]
- 0086c0ac ["CALL", null, ["local:b0:8"]]
+ 0086c104 ["INT_ADD", "register:40f0:8", ["const:86c104:8", "const:4:8"]]
+ 0086c104 ["CALL", null, ["local:b0:8"]]
- 0086c0ac bytes f8ffff97
+ 0086c104 bytes f8ffff97
- 0086c0b8 ["INT_ADD", "register:40f0:8", ["const:86c0b8:8", "const:4:8"]]
- 0086c0b8 ["CALL", null, ["local:b0:8"]]
+ 0086c110 ["INT_ADD", "register:40f0:8", ["const:86c110:8", "const:4:8"]]
+ 0086c110 ["CALL", null, ["local:b0:8"]]
- 0086c0b8 bytes f5ffff97
+ 0086c110 bytes f5ffff97
- 0086c0f4 ["INT_ADD", "register:40f0:8", ["const:86c0f4:8", "const:4:8"]]
- 0086c0f4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0086c14c ["INT_ADD", "register:40f0:8", ["const:86c14c:8", "const:4:8"]]
+ 0086c14c ["CALL", null, ["callee:00c53da0:8"]]
- 0086c0f4 bytes 039f0f94
+ 0086c14c bytes 159f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad2b54704c5e4c3966c1ebdcc8d6ea04"></a>

### [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) → [`0086c194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c194.md) FUN_0086c194

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) · 呼出先 2件 [`0086c13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086c194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c194.md) · 呼出先 2件 [`0086c194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c194.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md#insn-0086c15c) · [`0086c168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c13c.md#insn-0086c168)
- 新版 `0086c1b4`（命令位置の公開資料なし） · `0086c1c0`（命令位置の公開資料なし）

~~~diff
- 0086c15c ["INT_ADD", "register:40f0:8", ["const:86c15c:8", "const:4:8"]]
- 0086c15c ["CALL", null, ["local:b0:8"]]
+ 0086c1b4 ["INT_ADD", "register:40f0:8", ["const:86c1b4:8", "const:4:8"]]
+ 0086c1b4 ["CALL", null, ["local:b0:8"]]
- 0086c15c bytes f8ffff97
+ 0086c1b4 bytes f8ffff97
- 0086c168 ["INT_ADD", "register:40f0:8", ["const:86c168:8", "const:4:8"]]
- 0086c168 ["CALL", null, ["local:b0:8"]]
+ 0086c1c0 ["INT_ADD", "register:40f0:8", ["const:86c1c0:8", "const:4:8"]]
+ 0086c1c0 ["CALL", null, ["local:b0:8"]]
- 0086c168 bytes f5ffff97
+ 0086c1c0 bytes f5ffff97
~~~


<a id="compare-346819a04e16b11cb77095d5be86611a"></a>

### [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) → [`0086c1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c1d8.md) FUN_0086c1d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) · 呼出先 2件 [`0086c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`0086c1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c1d8.md) · 呼出先 2件 [`0086c1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c1d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md#insn-0086c19c) · [`0086c1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md#insn-0086c1a8) · [`0086c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c180.md#insn-0086c1b8)
- 新版 `0086c1f4`（命令位置の公開資料なし） · `0086c200`（命令位置の公開資料なし） · `0086c210`（命令位置の公開資料なし）

~~~diff
- 0086c19c ["INT_ADD", "register:40f0:8", ["const:86c19c:8", "const:4:8"]]
- 0086c19c ["CALL", null, ["local:b0:8"]]
+ 0086c1f4 ["INT_ADD", "register:40f0:8", ["const:86c1f4:8", "const:4:8"]]
+ 0086c1f4 ["CALL", null, ["local:b0:8"]]
- 0086c19c bytes f9ffff97
+ 0086c1f4 bytes f9ffff97
- 0086c1a8 ["INT_ADD", "register:40f0:8", ["const:86c1a8:8", "const:4:8"]]
- 0086c1a8 ["CALL", null, ["local:b0:8"]]
+ 0086c200 ["INT_ADD", "register:40f0:8", ["const:86c200:8", "const:4:8"]]
+ 0086c200 ["CALL", null, ["local:b0:8"]]
- 0086c1a8 bytes f6ffff97
+ 0086c200 bytes f6ffff97
- 0086c1b8 ["INT_ADD", "register:40f0:8", ["const:86c1b8:8", "const:4:8"]]
- 0086c1b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c210 ["INT_ADD", "register:40f0:8", ["const:86c210:8", "const:4:8"]]
+ 0086c210 ["CALL", null, ["callee:00c57f80:8"]]
- 0086c1b8 bytes 3eaf0f94
+ 0086c210 bytes 5caf0f94
~~~


<a id="compare-4eef1fcd85e6527d9a6520e32c2da4f2"></a>

### [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) → [`0086c228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c228.md) FUN_0086c228

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/0086155c.md) [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) · 呼出先 2件 [`0086c1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`008615b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008615b4.md) [`0086c228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c228.md) · 呼出先 2件 [`0086c228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c228.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md#insn-0086c1f0) · [`0086c1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c1d0.md#insn-0086c1fc)
- 新版 `0086c248`（命令位置の公開資料なし） · `0086c254`（命令位置の公開資料なし）

~~~diff
- 0086c1f0 ["INT_ADD", "register:40f0:8", ["const:86c1f0:8", "const:4:8"]]
- 0086c1f0 ["CALL", null, ["local:b0:8"]]
+ 0086c248 ["INT_ADD", "register:40f0:8", ["const:86c248:8", "const:4:8"]]
+ 0086c248 ["CALL", null, ["local:b0:8"]]
- 0086c1f0 bytes f8ffff97
+ 0086c248 bytes f8ffff97
- 0086c1fc ["INT_ADD", "register:40f0:8", ["const:86c1fc:8", "const:4:8"]]
- 0086c1fc ["CALL", null, ["local:b0:8"]]
+ 0086c254 ["INT_ADD", "register:40f0:8", ["const:86c254:8", "const:4:8"]]
+ 0086c254 ["CALL", null, ["local:b0:8"]]
- 0086c1fc bytes f5ffff97
+ 0086c254 bytes f5ffff97
~~~


<a id="compare-19c646c5f775115dd48f2feae9db13c6"></a>

### [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) → [`0086c26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c26c.md) FUN_0086c26c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 2件 [`0086c214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c26c.md) [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 2件 [`0086c26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c26c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md#insn-0086c230) · [`0086c23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md#insn-0086c23c) · [`0086c24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c214.md#insn-0086c24c)
- 新版 `0086c288`（命令位置の公開資料なし） · `0086c294`（命令位置の公開資料なし） · `0086c2a4`（命令位置の公開資料なし）

~~~diff
- 0086c230 ["INT_ADD", "register:40f0:8", ["const:86c230:8", "const:4:8"]]
- 0086c230 ["CALL", null, ["local:b0:8"]]
+ 0086c288 ["INT_ADD", "register:40f0:8", ["const:86c288:8", "const:4:8"]]
+ 0086c288 ["CALL", null, ["local:b0:8"]]
- 0086c230 bytes f9ffff97
+ 0086c288 bytes f9ffff97
- 0086c23c ["INT_ADD", "register:40f0:8", ["const:86c23c:8", "const:4:8"]]
- 0086c23c ["CALL", null, ["local:b0:8"]]
+ 0086c294 ["INT_ADD", "register:40f0:8", ["const:86c294:8", "const:4:8"]]
+ 0086c294 ["CALL", null, ["local:b0:8"]]
- 0086c23c bytes f6ffff97
+ 0086c294 bytes f6ffff97
- 0086c24c ["INT_ADD", "register:40f0:8", ["const:86c24c:8", "const:4:8"]]
- 0086c24c ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c2a4 ["INT_ADD", "register:40f0:8", ["const:86c2a4:8", "const:4:8"]]
+ 0086c2a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0086c24c bytes 19af0f94
+ 0086c2a4 bytes 37af0f94
~~~


<a id="compare-8a6c015593c4a51a17ed44284a6f18ec"></a>

### [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) → [`0086c2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c2bc.md) FUN_0086c2bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`008609ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/008609ec.md) [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 3件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0086c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`00860a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00860/00860a44.md) [`0086c2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c2bc.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 3件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0086c2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c2bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md#insn-0086c284) · [`0086c290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md#insn-0086c290) · [`0086c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c264.md#insn-0086c29c)
- 新版 `0086c2dc`（命令位置の公開資料なし） · `0086c2e8`（命令位置の公開資料なし） · `0086c2f4`（命令位置の公開資料なし）

~~~diff
- 0086c284 ["INT_ADD", "register:40f0:8", ["const:86c284:8", "const:4:8"]]
- 0086c284 ["CALL", null, ["local:b0:8"]]
+ 0086c2dc ["INT_ADD", "register:40f0:8", ["const:86c2dc:8", "const:4:8"]]
+ 0086c2dc ["CALL", null, ["local:b0:8"]]
- 0086c284 bytes f8ffff97
+ 0086c2dc bytes f8ffff97
- 0086c290 ["INT_ADD", "register:40f0:8", ["const:86c290:8", "const:4:8"]]
- 0086c290 ["CALL", null, ["local:b0:8"]]
+ 0086c2e8 ["INT_ADD", "register:40f0:8", ["const:86c2e8:8", "const:4:8"]]
+ 0086c2e8 ["CALL", null, ["local:b0:8"]]
- 0086c290 bytes f5ffff97
+ 0086c2e8 bytes f5ffff97
- 0086c29c ["INT_ADD", "register:40f0:8", ["const:86c29c:8", "const:4:8"]]
- 0086c29c ["CALL", null, ["callee:00676aa0:8"]]
+ 0086c2f4 ["INT_ADD", "register:40f0:8", ["const:86c2f4:8", "const:4:8"]]
+ 0086c2f4 ["CALL", null, ["callee:00676aa0:8"]]
- 0086c29c bytes f129f897
+ 0086c2f4 bytes eb29f897
~~~


<a id="compare-f97eda9b59aa9799295c99474450fb16"></a>

### [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) → [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) FUN_0086c30c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`0086c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c350.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md#insn-0086c2d4) · [`0086c2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md#insn-0086c2e0)
- 新版 `0086c32c`（命令位置の公開資料なし） · `0086c338`（命令位置の公開資料なし）

~~~diff
- 0086c2d4 ["INT_ADD", "register:40f0:8", ["const:86c2d4:8", "const:4:8"]]
- 0086c2d4 ["CALL", null, ["local:b0:8"]]
+ 0086c32c ["INT_ADD", "register:40f0:8", ["const:86c32c:8", "const:4:8"]]
+ 0086c32c ["CALL", null, ["local:b0:8"]]
- 0086c2d4 bytes f8ffff97
+ 0086c32c bytes f8ffff97
- 0086c2e0 ["INT_ADD", "register:40f0:8", ["const:86c2e0:8", "const:4:8"]]
- 0086c2e0 ["CALL", null, ["local:b0:8"]]
+ 0086c338 ["INT_ADD", "register:40f0:8", ["const:86c338:8", "const:4:8"]]
+ 0086c338 ["CALL", null, ["local:b0:8"]]
- 0086c2e0 bytes f5ffff97
+ 0086c338 bytes f5ffff97
~~~


<a id="compare-558a0791706423078b098e25b4bd692e"></a>

### [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) → [`0086c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c350.md) FUN_0086c350

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008507d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00850/008507d8.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`0086c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00850830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00850/00850830.md) [`0086c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c350.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`0086c350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c350.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md#insn-0086c318) · [`0086c324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md#insn-0086c324) · [`0086c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2f8.md#insn-0086c330)
- 新版 `0086c370`（命令位置の公開資料なし） · `0086c37c`（命令位置の公開資料なし） · `0086c388`（命令位置の公開資料なし）

~~~diff
- 0086c318 ["INT_ADD", "register:40f0:8", ["const:86c318:8", "const:4:8"]]
- 0086c318 ["CALL", null, ["local:b0:8"]]
+ 0086c370 ["INT_ADD", "register:40f0:8", ["const:86c370:8", "const:4:8"]]
+ 0086c370 ["CALL", null, ["local:b0:8"]]
- 0086c318 bytes f8ffff97
+ 0086c370 bytes f8ffff97
- 0086c324 ["INT_ADD", "register:40f0:8", ["const:86c324:8", "const:4:8"]]
- 0086c324 ["CALL", null, ["local:b0:8"]]
+ 0086c37c ["INT_ADD", "register:40f0:8", ["const:86c37c:8", "const:4:8"]]
+ 0086c37c ["CALL", null, ["local:b0:8"]]
- 0086c324 bytes f5ffff97
+ 0086c37c bytes f5ffff97
- 0086c330 ["INT_ADD", "register:40f0:8", ["const:86c330:8", "const:4:8"]]
- 0086c330 ["CALL", null, ["callee:0086c30c:8"]]
+ 0086c388 ["INT_ADD", "register:40f0:8", ["const:86c388:8", "const:4:8"]]
+ 0086c388 ["CALL", null, ["callee:0086c30c:8"]]
- 0086c330 bytes e1ffff97
+ 0086c388 bytes e1ffff97
~~~


<a id="compare-ce6a25f7e83a9189b25789d456dca6a9"></a>

### [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) → [`0086c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3a0.md) FUN_0086c3a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) · 呼出先 2件 [`0086c348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3a0.md) · 呼出先 2件 [`0086c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3a0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md#insn-0086c368) · [`0086c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c348.md#insn-0086c374)
- 新版 `0086c3c0`（命令位置の公開資料なし） · `0086c3cc`（命令位置の公開資料なし）

~~~diff
- 0086c368 ["INT_ADD", "register:40f0:8", ["const:86c368:8", "const:4:8"]]
- 0086c368 ["CALL", null, ["local:b0:8"]]
+ 0086c3c0 ["INT_ADD", "register:40f0:8", ["const:86c3c0:8", "const:4:8"]]
+ 0086c3c0 ["CALL", null, ["local:b0:8"]]
- 0086c368 bytes f8ffff97
+ 0086c3c0 bytes f8ffff97
- 0086c374 ["INT_ADD", "register:40f0:8", ["const:86c374:8", "const:4:8"]]
- 0086c374 ["CALL", null, ["local:b0:8"]]
+ 0086c3cc ["INT_ADD", "register:40f0:8", ["const:86c3cc:8", "const:4:8"]]
+ 0086c3cc ["CALL", null, ["local:b0:8"]]
- 0086c374 bytes f5ffff97
+ 0086c3cc bytes f5ffff97
~~~


<a id="compare-dfe519418dee0c5f3fc59d7189b0eb65"></a>

### [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) → [`0086c3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3e4.md) FUN_0086c3e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) · 呼出先 2件 [`0086c38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3e4.md) · 呼出先 2件 [`0086c3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c3e4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md#insn-0086c3ac) · [`0086c3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c38c.md#insn-0086c3b8)
- 新版 `0086c404`（命令位置の公開資料なし） · `0086c410`（命令位置の公開資料なし）

~~~diff
- 0086c3ac ["INT_ADD", "register:40f0:8", ["const:86c3ac:8", "const:4:8"]]
- 0086c3ac ["CALL", null, ["local:b0:8"]]
+ 0086c404 ["INT_ADD", "register:40f0:8", ["const:86c404:8", "const:4:8"]]
+ 0086c404 ["CALL", null, ["local:b0:8"]]
- 0086c3ac bytes f8ffff97
+ 0086c404 bytes f8ffff97
- 0086c3b8 ["INT_ADD", "register:40f0:8", ["const:86c3b8:8", "const:4:8"]]
- 0086c3b8 ["CALL", null, ["local:b0:8"]]
+ 0086c410 ["INT_ADD", "register:40f0:8", ["const:86c410:8", "const:4:8"]]
+ 0086c410 ["CALL", null, ["local:b0:8"]]
- 0086c3b8 bytes f5ffff97
+ 0086c410 bytes f5ffff97
~~~


<a id="compare-f8d78298032809b43437001c33e9d291"></a>

### [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) → [`0086c428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c428.md) FUN_0086c428

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c428.md) [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0086c428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c428.md) [`0086c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c478.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md#insn-0086c3f0) · [`0086c3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md#insn-0086c3fc) · [`0086c408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md#insn-0086c408)
- 新版 `0086c448`（命令位置の公開資料なし） · `0086c454`（命令位置の公開資料なし） · `0086c460`（命令位置の公開資料なし）

~~~diff
- 0086c3f0 ["INT_ADD", "register:40f0:8", ["const:86c3f0:8", "const:4:8"]]
- 0086c3f0 ["CALL", null, ["local:b0:8"]]
+ 0086c448 ["INT_ADD", "register:40f0:8", ["const:86c448:8", "const:4:8"]]
+ 0086c448 ["CALL", null, ["local:b0:8"]]
- 0086c3f0 bytes f8ffff97
+ 0086c448 bytes f8ffff97
- 0086c3fc ["INT_ADD", "register:40f0:8", ["const:86c3fc:8", "const:4:8"]]
- 0086c3fc ["CALL", null, ["local:b0:8"]]
+ 0086c454 ["INT_ADD", "register:40f0:8", ["const:86c454:8", "const:4:8"]]
+ 0086c454 ["CALL", null, ["local:b0:8"]]
- 0086c3fc bytes f5ffff97
+ 0086c454 bytes f5ffff97
- 0086c408 ["INT_ADD", "register:40f0:8", ["const:86c408:8", "const:4:8"]]
- 0086c408 ["CALL", null, ["callee:0086c478:8"]]
+ 0086c460 ["INT_ADD", "register:40f0:8", ["const:86c460:8", "const:4:8"]]
+ 0086c460 ["CALL", null, ["callee:0086c478:8"]]
- 0086c408 bytes 06000094
+ 0086c460 bytes 06000094
~~~


<a id="compare-b09bfd56b756c42a2fffe108e5019d0d"></a>

### [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) → [`0086c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c478.md) FUN_0086c478

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0086c3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c3d0.md) [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`0086c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0086c428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c428.md) [`0086c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c478.md) [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`0086c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c478.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md#insn-0086c440) · [`0086c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c420.md#insn-0086c44c)
- 新版 `0086c498`（命令位置の公開資料なし） · `0086c4a4`（命令位置の公開資料なし）

~~~diff
- 0086c440 ["INT_ADD", "register:40f0:8", ["const:86c440:8", "const:4:8"]]
- 0086c440 ["CALL", null, ["local:b0:8"]]
+ 0086c498 ["INT_ADD", "register:40f0:8", ["const:86c498:8", "const:4:8"]]
+ 0086c498 ["CALL", null, ["local:b0:8"]]
- 0086c440 bytes f8ffff97
+ 0086c498 bytes f8ffff97
- 0086c44c ["INT_ADD", "register:40f0:8", ["const:86c44c:8", "const:4:8"]]
- 0086c44c ["CALL", null, ["local:b0:8"]]
+ 0086c4a4 ["INT_ADD", "register:40f0:8", ["const:86c4a4:8", "const:4:8"]]
+ 0086c4a4 ["CALL", null, ["local:b0:8"]]
- 0086c44c bytes f5ffff97
+ 0086c4a4 bytes f5ffff97
~~~


<a id="compare-fcc79d465807a1d1432887f4dfa324f2"></a>

### [`0086c464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c464.md) → [`0086c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c4bc.md) FUN_0086c4bc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c464.md#insn-0086c4c4) · [`0086c4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c464.md#insn-0086c4d4) · [`0086c4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c464.md#insn-0086c4e4)
- 新版 `0086c51c`（命令位置の公開資料なし） · `0086c52c`（命令位置の公開資料なし） · `0086c53c`（命令位置の公開資料なし）

~~~diff
- 0086c4c4 ["INT_ADD", "register:40f0:8", ["const:86c4c4:8", "const:4:8"]]
- 0086c4c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c51c ["INT_ADD", "register:40f0:8", ["const:86c51c:8", "const:4:8"]]
+ 0086c51c ["CALL", null, ["callee:00c57f80:8"]]
- 0086c4c4 bytes 7bae0f94
+ 0086c51c bytes 99ae0f94
- 0086c4d4 ["INT_ADD", "register:40f0:8", ["const:86c4d4:8", "const:4:8"]]
- 0086c4d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c52c ["INT_ADD", "register:40f0:8", ["const:86c52c:8", "const:4:8"]]
+ 0086c52c ["CALL", null, ["callee:00c57f80:8"]]
- 0086c4d4 bytes 77ae0f94
+ 0086c52c bytes 95ae0f94
- 0086c4e4 ["INT_ADD", "register:40f0:8", ["const:86c4e4:8", "const:4:8"]]
- 0086c4e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c53c ["INT_ADD", "register:40f0:8", ["const:86c53c:8", "const:4:8"]]
+ 0086c53c ["CALL", null, ["callee:00c57f80:8"]]
- 0086c4e4 bytes 73ae0f94
+ 0086c53c bytes 91ae0f94
~~~


<a id="compare-da54b9845c939c7640906a756961c508"></a>

### [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) → [`0086c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c570.md) FUN_0086c570

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) · 呼出先 2件 [`0086c518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0086c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c570.md) · 呼出先 2件 [`0086c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c570.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086c534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md#insn-0086c534) · [`0086c540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md#insn-0086c540) · [`0086c560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c518.md#insn-0086c560)
- 新版 `0086c58c`（命令位置の公開資料なし） · `0086c598`（命令位置の公開資料なし） · `0086c5b8`（命令位置の公開資料なし）

~~~diff
- 0086c534 ["INT_ADD", "register:40f0:8", ["const:86c534:8", "const:4:8"]]
- 0086c534 ["CALL", null, ["local:b0:8"]]
+ 0086c58c ["INT_ADD", "register:40f0:8", ["const:86c58c:8", "const:4:8"]]
+ 0086c58c ["CALL", null, ["local:b0:8"]]
- 0086c534 bytes f9ffff97
+ 0086c58c bytes f9ffff97
- 0086c540 ["INT_ADD", "register:40f0:8", ["const:86c540:8", "const:4:8"]]
- 0086c540 ["CALL", null, ["local:b0:8"]]
+ 0086c598 ["INT_ADD", "register:40f0:8", ["const:86c598:8", "const:4:8"]]
+ 0086c598 ["CALL", null, ["local:b0:8"]]
- 0086c540 bytes f6ffff97
+ 0086c598 bytes f6ffff97
- 0086c560 ["INT_ADD", "register:40f0:8", ["const:86c560:8", "const:4:8"]]
- 0086c560 ["CALL", null, ["callee:00c57f80:8"]]
+ 0086c5b8 ["INT_ADD", "register:40f0:8", ["const:86c5b8:8", "const:4:8"]]
+ 0086c5b8 ["CALL", null, ["callee:00c57f80:8"]]
- 0086c560 bytes 54ae0f94
+ 0086c5b8 bytes 72ae0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4f99163dd03c009678c504b961e018"></a>

### [`0086ddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086ddd4.md) → [`0086de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086de2c.md) FUN_0086de2c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) · 呼出先 2件 [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0086d774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d774.md) · 呼出先 2件 [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0086ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086ddd4.md#insn-0086ddf0)
- 新版 `0086de48`（命令位置の公開資料なし）

~~~diff
- 0086ddf0 ["INT_ADD", "register:40f0:8", ["const:86ddf0:8", "const:4:8"]]
- 0086ddf0 ["CALL", null, ["callee:004647dc:8"]]
+ 0086de48 ["INT_ADD", "register:40f0:8", ["const:86de48:8", "const:4:8"]]
+ 0086de48 ["CALL", null, ["callee:004647dc:8"]]
- 0086ddf0 bytes 6bdaef97
+ 0086de48 bytes 65daef97
~~~


<a id="compare-f94cf68d160f190338fdcc4d91a22dd4"></a>

### [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) → [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md) FUN_00870d14

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) · 呼出先 4件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0085d54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md) [`00871014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871014.md) · 呼出先 4件 [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md) [`00871014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871014.md) [`008712ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008712ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00870d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md#insn-00870d40) · [`00870dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md#insn-00870dc8) · [`00870e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md#insn-00870e0c)
- 新版 `00870d98`（命令位置の公開資料なし） · `00870e20`（命令位置の公開資料なし） · `00870e64`（命令位置の公開資料なし）

~~~diff
- 00870d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00870d40 ["INT_ADD", "register:40f0:8", ["const:870d40:8", "const:4:8"]]
- 00870d40 ["CALLIND", null, ["register:0:8"]]
+ 00870d98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00870d98 ["INT_ADD", "register:40f0:8", ["const:870d98:8", "const:4:8"]]
+ 00870d98 ["CALLIND", null, ["register:0:8"]]
- 00870d40 bytes 00013fd6
+ 00870d98 bytes 00013fd6
- 00870dc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00870dc8 ["INT_ADD", "register:40f0:8", ["const:870dc8:8", "const:4:8"]]
- 00870dc8 ["CALLIND", null, ["register:0:8"]]
+ 00870e20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00870e20 ["INT_ADD", "register:40f0:8", ["const:870e20:8", "const:4:8"]]
+ 00870e20 ["CALLIND", null, ["register:0:8"]]
- 00870dc8 bytes 20013fd6
+ 00870e20 bytes 20013fd6
- 00870e0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00870e0c ["INT_ADD", "register:40f0:8", ["const:870e0c:8", "const:4:8"]]
- 00870e0c ["CALLIND", null, ["register:0:8"]]
+ 00870e64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00870e64 ["INT_ADD", "register:40f0:8", ["const:870e64:8", "const:4:8"]]
+ 00870e64 ["CALLIND", null, ["register:0:8"]]
- 00870e0c bytes 00013fd6
+ 00870e64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd8a0ac1187676e341acd919356c69c"></a>

### [`00870fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md) → [`00871014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871014.md) FUN_00871014

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) · 呼出先 1件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md)
- 新版 呼出元 1件 [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md) · 呼出先 1件 [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00871020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md#insn-00871020) · [`008710ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md#insn-008710ac) · [`008710ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870fbc.md#insn-008710ec)
- 新版 `00871078`（命令位置の公開資料なし） · `00871104`（命令位置の公開資料なし） · `00871144`（命令位置の公開資料なし）

~~~diff
- 00871020 ["COPY", "register:0:8", ["register:4040:8"]]
- 00871020 ["INT_ADD", "register:40f0:8", ["const:871020:8", "const:4:8"]]
- 00871020 ["CALLIND", null, ["register:0:8"]]
+ 00871078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00871078 ["INT_ADD", "register:40f0:8", ["const:871078:8", "const:4:8"]]
+ 00871078 ["CALLIND", null, ["register:0:8"]]
- 00871020 bytes 00013fd6
+ 00871078 bytes 00013fd6
- 008710ac ["COPY", "register:0:8", ["register:4040:8"]]
- 008710ac ["INT_ADD", "register:40f0:8", ["const:8710ac:8", "const:4:8"]]
- 008710ac ["CALLIND", null, ["register:0:8"]]
+ 00871104 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00871104 ["INT_ADD", "register:40f0:8", ["const:871104:8", "const:4:8"]]
+ 00871104 ["CALLIND", null, ["register:0:8"]]
- 008710ac bytes 00013fd6
+ 00871104 bytes 00013fd6
- 008710ec ["COPY", "register:0:8", ["register:4040:8"]]
- 008710ec ["INT_ADD", "register:40f0:8", ["const:8710ec:8", "const:4:8"]]
- 008710ec ["CALLIND", null, ["register:0:8"]]
+ 00871144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00871144 ["INT_ADD", "register:40f0:8", ["const:871144:8", "const:4:8"]]
+ 00871144 ["CALLIND", null, ["register:0:8"]]
- 008710ec bytes 00013fd6
+ 00871144 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7333e1bc8d41f40c67142af332d6041"></a>

### [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) → [`008712ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008712ac.md) FUN_008712ac

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00870cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870cbc.md) [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) · 呼出先 4件 [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) [`0087170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`00870d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d14.md) [`008712ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008712ac.md) · 呼出先 4件 [`008712ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008712ac.md) [`00871764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871764.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008712d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md#insn-008712d4) · [`00871360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md#insn-00871360) · [`0087140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md#insn-0087140c)
- 新版 `0087132c`（命令位置の公開資料なし） · `008713b8`（命令位置の公開資料なし） · `00871464`（命令位置の公開資料なし）

~~~diff
- 008712d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008712d4 ["INT_ADD", "register:40f0:8", ["const:8712d4:8", "const:4:8"]]
- 008712d4 ["CALLIND", null, ["register:0:8"]]
+ 0087132c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087132c ["INT_ADD", "register:40f0:8", ["const:87132c:8", "const:4:8"]]
+ 0087132c ["CALLIND", null, ["register:0:8"]]
- 008712d4 bytes 00013fd6
+ 0087132c bytes 00013fd6
- 00871360 ["COPY", "register:0:8", ["register:4040:8"]]
- 00871360 ["INT_ADD", "register:40f0:8", ["const:871360:8", "const:4:8"]]
- 00871360 ["CALLIND", null, ["register:0:8"]]
+ 008713b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008713b8 ["INT_ADD", "register:40f0:8", ["const:8713b8:8", "const:4:8"]]
+ 008713b8 ["CALLIND", null, ["register:0:8"]]
- 00871360 bytes 00013fd6
+ 008713b8 bytes 00013fd6
- 0087140c ["COPY", "register:0:8", ["register:40c8:8"]]
- 0087140c ["INT_ADD", "register:40f0:8", ["const:87140c:8", "const:4:8"]]
- 0087140c ["CALLIND", null, ["register:0:8"]]
+ 00871464 ["COPY", "register:0:8", ["register:40c8:8"]]
+ 00871464 ["INT_ADD", "register:40f0:8", ["const:871464:8", "const:4:8"]]
+ 00871464 ["CALLIND", null, ["register:0:8"]]
- 0087140c bytes 20033fd6
+ 00871464 bytes 20033fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b74893643bf130020c60b2fc92eff6"></a>

### [`0087170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md) → [`00871764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871764.md) FUN_00871764

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00871254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871254.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`008712ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008712ac.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008717f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md#insn-008717f0) · [`00871848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md#insn-00871848) · [`0087192c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087170c.md#insn-0087192c)
- 新版 `00871848`（命令位置の公開資料なし） · `008718a0`（命令位置の公開資料なし） · `00871984`（命令位置の公開資料なし）

~~~diff
- 008717f0 ["INT_ADD", "register:40f0:8", ["const:8717f0:8", "const:4:8"]]
- 008717f0 ["CALL", null, ["callee:00c58010:8"]]
+ 00871848 ["INT_ADD", "register:40f0:8", ["const:871848:8", "const:4:8"]]
+ 00871848 ["CALL", null, ["callee:00c58010:8"]]
- 008717f0 bytes d4990f94
+ 00871848 bytes f2990f94
- 00871848 ["INT_ADD", "register:40f0:8", ["const:871848:8", "const:4:8"]]
- 00871848 ["CALL", null, ["callee:00c58010:8"]]
+ 008718a0 ["INT_ADD", "register:40f0:8", ["const:8718a0:8", "const:4:8"]]
+ 008718a0 ["CALL", null, ["callee:00c58010:8"]]
- 00871848 bytes be990f94
+ 008718a0 bytes dc990f94
- 0087192c ["INT_ADD", "register:40f0:8", ["const:87192c:8", "const:4:8"]]
- 0087192c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00871984 ["INT_ADD", "register:40f0:8", ["const:871984:8", "const:4:8"]]
+ 00871984 ["CALL", null, ["callee:00c57fb0:8"]]
- 0087192c bytes 6d990f94
+ 00871984 bytes 8b990f94
~~~


<a id="compare-6fd3199c8bc92cd69e75a88edc478e40"></a>

### [`00871bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871bb8.md) → [`00871c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871c10.md) FUN_00871c10

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0086155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/0086155c.md) [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) [`008fc5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fc/008fc5f0.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a3aac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3aac8.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 5件 [`008615b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008615b4.md) [`008c525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c525c.md) [`008fc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc644.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) [`00a3ab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3ab1c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00871cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871bb8.md#insn-00871cf8) · [`00871db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871bb8.md#insn-00871db4) · [`00871dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871bb8.md#insn-00871dd8)
- 新版 `00871d50`（命令位置の公開資料なし） · `00871e0c`（命令位置の公開資料なし） · `00871e30`（命令位置の公開資料なし）

~~~diff
- 00871cf8 ["INT_ADD", "register:40f0:8", ["const:871cf8:8", "const:4:8"]]
- 00871cf8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00871d50 ["INT_ADD", "register:40f0:8", ["const:871d50:8", "const:4:8"]]
+ 00871d50 ["CALL", null, ["callee:0043bbe4:8"]]
- 00871cf8 bytes ab27ef97
+ 00871d50 bytes a527ef97
- 00871db4 ["INT_ADD", "register:40f0:8", ["const:871db4:8", "const:4:8"]]
- 00871db4 ["CALL", null, ["callee:005c17dc:8"]]
+ 00871e0c ["INT_ADD", "register:40f0:8", ["const:871e0c:8", "const:4:8"]]
+ 00871e0c ["CALL", null, ["callee:005c17dc:8"]]
- 00871db4 bytes 7a3ef597
+ 00871e0c bytes 743ef597
- 00871dd8 ["INT_ADD", "register:40f0:8", ["const:871dd8:8", "const:4:8"]]
- 00871dd8 ["CALL", null, ["callee:005c17dc:8"]]
+ 00871e30 ["INT_ADD", "register:40f0:8", ["const:871e30:8", "const:4:8"]]
+ 00871e30 ["CALL", null, ["callee:005c17dc:8"]]
- 00871dd8 bytes 713ef597
+ 00871e30 bytes 6b3ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6d52af49e06e04bacad49fa788f3a2a"></a>

### [`00871fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871fec.md) → [`00872044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872044.md) FUN_00872044

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087200c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871fec.md#insn-0087200c)
- 新版 `00872064`（命令位置の公開資料なし）

~~~diff
- 0087200c ["INT_ADD", "register:40f0:8", ["const:87200c:8", "const:4:8"]]
- 0087200c ["CALL", null, ["callee:00c57f80:8"]]
+ 00872064 ["INT_ADD", "register:40f0:8", ["const:872064:8", "const:4:8"]]
+ 00872064 ["CALL", null, ["callee:00c57f80:8"]]
- 0087200c bytes a9970f94
+ 00872064 bytes c7970f94
~~~


<a id="compare-54ccabd3875d7eae6167aa9ebdfe0794"></a>

### [`0087221c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/0087221c.md) → [`00872274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872274.md) FUN_00872274

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087223c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/0087221c.md#insn-0087223c)
- 新版 `00872294`（命令位置の公開資料なし）

~~~diff
- 0087223c ["INT_ADD", "register:40f0:8", ["const:87223c:8", "const:4:8"]]
- 0087223c ["CALL", null, ["callee:00c57f80:8"]]
+ 00872294 ["INT_ADD", "register:40f0:8", ["const:872294:8", "const:4:8"]]
+ 00872294 ["CALL", null, ["callee:00c57f80:8"]]
- 0087223c bytes 1d970f94
+ 00872294 bytes 3b970f94
~~~


<a id="compare-62c74bd60df6e7d38306797033769971"></a>

### [`008729ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008729ec.md) → [`00872a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a44.md) FUN_00872a44

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008725f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008729fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008729ec.md#insn-008729fc)
- 新版 `00872a54`（命令位置の公開資料なし）

~~~diff
- 008729fc ["INT_ADD", "register:40f0:8", ["const:8729fc:8", "const:4:8"]]
- 008729fc ["CALL", null, ["callee:008725f8:8"]]
+ 00872a54 ["INT_ADD", "register:40f0:8", ["const:872a54:8", "const:4:8"]]
+ 00872a54 ["CALL", null, ["callee:008725f8:8"]]
- 008729fc bytes e9feff97
+ 00872a54 bytes e9feff97
~~~


<a id="compare-135e9cdde6f2f10ac7ffba5c9bc4eea3"></a>

### [`0087438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087438c.md) → [`008743e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008743e4.md) FUN_008743e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008743a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087438c.md#insn-008743a8) · [`008743c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087438c.md#insn-008743c8)
- 新版 `00874400`（命令位置の公開資料なし） · `00874420`（命令位置の公開資料なし）

~~~diff
- 008743a8 ["INT_ADD", "register:40f0:8", ["const:8743a8:8", "const:4:8"]]
- 008743a8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874400 ["INT_ADD", "register:40f0:8", ["const:874400:8", "const:4:8"]]
+ 00874400 ["CALL", null, ["callee:00c53da0:8"]]
- 008743a8 bytes 567e0f94
+ 00874400 bytes 687e0f94
- 008743c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008743c8 ["INT_ADD", "register:40f0:8", ["const:8743c8:8", "const:4:8"]]
- 008743c8 ["CALLIND", null, ["register:0:8"]]
+ 00874420 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874420 ["INT_ADD", "register:40f0:8", ["const:874420:8", "const:4:8"]]
+ 00874420 ["CALLIND", null, ["register:0:8"]]
- 008743c8 bytes 00013fd6
+ 00874420 bytes 00013fd6
~~~


<a id="compare-2a33729f6c0f651cc073ac9fc257223c"></a>

### [`008743dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008743dc.md) → [`00874434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874434.md) FUN_00874434

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008743f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008743dc.md#insn-008743f8) · [`00874418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008743dc.md#insn-00874418)
- 新版 `00874450`（命令位置の公開資料なし） · `00874470`（命令位置の公開資料なし）

~~~diff
- 008743f8 ["INT_ADD", "register:40f0:8", ["const:8743f8:8", "const:4:8"]]
- 008743f8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874450 ["INT_ADD", "register:40f0:8", ["const:874450:8", "const:4:8"]]
+ 00874450 ["CALL", null, ["callee:00c53da0:8"]]
- 008743f8 bytes 427e0f94
+ 00874450 bytes 547e0f94
- 00874418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874418 ["INT_ADD", "register:40f0:8", ["const:874418:8", "const:4:8"]]
- 00874418 ["CALLIND", null, ["register:0:8"]]
+ 00874470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874470 ["INT_ADD", "register:40f0:8", ["const:874470:8", "const:4:8"]]
+ 00874470 ["CALLIND", null, ["register:0:8"]]
- 00874418 bytes 00013fd6
+ 00874470 bytes 00013fd6
~~~


<a id="compare-b46d94c815720124cf53bac7396bf8fa"></a>

### [`00874578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md) → [`008745d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008745d0.md) FUN_008745d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00873b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md#insn-00874594) · [`008745b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md#insn-008745b4)
- 新版 `008745ec`（命令位置の公開資料なし） · `0087460c`（命令位置の公開資料なし）

~~~diff
- 00874594 ["INT_ADD", "register:40f0:8", ["const:874594:8", "const:4:8"]]
- 00874594 ["CALL", null, ["callee:00c53da0:8"]]
+ 008745ec ["INT_ADD", "register:40f0:8", ["const:8745ec:8", "const:4:8"]]
+ 008745ec ["CALL", null, ["callee:00c53da0:8"]]
- 00874594 bytes db7d0f94
+ 008745ec bytes ed7d0f94
- 008745b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008745b4 ["INT_ADD", "register:40f0:8", ["const:8745b4:8", "const:4:8"]]
- 008745b4 ["CALLIND", null, ["register:0:8"]]
+ 0087460c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087460c ["INT_ADD", "register:40f0:8", ["const:87460c:8", "const:4:8"]]
+ 0087460c ["CALLIND", null, ["register:0:8"]]
- 008745b4 bytes 00013fd6
+ 0087460c bytes 00013fd6
~~~


<a id="compare-c4e47dd51601de215e00e2c6a68b1b08"></a>

### [`008745c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md) → [`00874620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874620.md) FUN_00874620

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00873b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008745e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md#insn-008745e8) · [`008745fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md#insn-008745fc) · [`00874604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md#insn-00874604)
- 新版 `00874640`（命令位置の公開資料なし） · `00874654`（命令位置の公開資料なし） · `0087465c`（命令位置の公開資料なし）

~~~diff
- 008745e8 ["INT_ADD", "register:40f0:8", ["const:8745e8:8", "const:4:8"]]
- 008745e8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874640 ["INT_ADD", "register:40f0:8", ["const:874640:8", "const:4:8"]]
+ 00874640 ["CALL", null, ["callee:00c53da0:8"]]
- 008745e8 bytes c67d0f94
+ 00874640 bytes d87d0f94
- 008745fc ["COPY", "register:0:8", ["register:4040:8"]]
- 008745fc ["INT_ADD", "register:40f0:8", ["const:8745fc:8", "const:4:8"]]
- 008745fc ["CALLIND", null, ["register:0:8"]]
+ 00874654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874654 ["INT_ADD", "register:40f0:8", ["const:874654:8", "const:4:8"]]
+ 00874654 ["CALLIND", null, ["register:0:8"]]
- 008745fc bytes 00013fd6
+ 00874654 bytes 00013fd6
- 00874604 ["INT_ADD", "register:40f0:8", ["const:874604:8", "const:4:8"]]
- 00874604 ["CALL", null, ["callee:00c57f50:8"]]
+ 0087465c ["INT_ADD", "register:40f0:8", ["const:87465c:8", "const:4:8"]]
+ 0087465c ["CALL", null, ["callee:00c57f50:8"]]
- 00874604 bytes 1f8e0f94
+ 0087465c bytes 3d8e0f94
~~~


<a id="compare-ede790dfb23909f3ed23952b8d10e208"></a>

### [`00874618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md) → [`00874670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874670.md) FUN_00874670

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md#insn-0087465c) · [`0087466c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md#insn-0087466c) · [`008746bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md#insn-008746bc)
- 新版 `008746b4`（命令位置の公開資料なし） · `008746c4`（命令位置の公開資料なし） · `00874714`（命令位置の公開資料なし）

~~~diff
- 0087465c ["INT_ADD", "register:40f0:8", ["const:87465c:8", "const:4:8"]]
- 0087465c ["CALL", null, ["callee:00874740:8"]]
+ 008746b4 ["INT_ADD", "register:40f0:8", ["const:8746b4:8", "const:4:8"]]
+ 008746b4 ["CALL", null, ["callee:00874740:8"]]
- 0087465c bytes 23000094
+ 008746b4 bytes 23000094
- 0087466c ["INT_ADD", "register:40f0:8", ["const:87466c:8", "const:4:8"]]
- 0087466c ["CALL", null, ["callee:00c57f80:8"]]
+ 008746c4 ["INT_ADD", "register:40f0:8", ["const:8746c4:8", "const:4:8"]]
+ 008746c4 ["CALL", null, ["callee:00c57f80:8"]]
- 0087466c bytes 118e0f94
+ 008746c4 bytes 2f8e0f94
- 008746bc ["INT_ADD", "register:40f0:8", ["const:8746bc:8", "const:4:8"]]
- 008746bc ["CALL", null, ["callee:00c57fb0:8"]]
+ 00874714 ["INT_ADD", "register:40f0:8", ["const:874714:8", "const:4:8"]]
+ 00874714 ["CALL", null, ["callee:00c57fb0:8"]]
- 008746bc bytes 098e0f94
+ 00874714 bytes 278e0f94
~~~


<a id="compare-0cede8171f74487a6facf83c9453bab4"></a>

### [`00874898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874898.md) → [`008748f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008748f0.md) FUN_008748f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008748b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874898.md#insn-008748b4) · [`008748d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874898.md#insn-008748d4)
- 新版 `0087490c`（命令位置の公開資料なし） · `0087492c`（命令位置の公開資料なし）

~~~diff
- 008748b4 ["INT_ADD", "register:40f0:8", ["const:8748b4:8", "const:4:8"]]
- 008748b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087490c ["INT_ADD", "register:40f0:8", ["const:87490c:8", "const:4:8"]]
+ 0087490c ["CALL", null, ["callee:00c53da0:8"]]
- 008748b4 bytes 137d0f94
+ 0087490c bytes 257d0f94
- 008748d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008748d4 ["INT_ADD", "register:40f0:8", ["const:8748d4:8", "const:4:8"]]
- 008748d4 ["CALLIND", null, ["register:0:8"]]
+ 0087492c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087492c ["INT_ADD", "register:40f0:8", ["const:87492c:8", "const:4:8"]]
+ 0087492c ["CALLIND", null, ["register:0:8"]]
- 008748d4 bytes 00013fd6
+ 0087492c bytes 00013fd6
~~~


<a id="compare-72b9e8667c981e6ba7ecc7d23e130063"></a>

### [`00874a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md) → [`00874a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a8c.md) FUN_00874a8c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md#insn-00874a50) · [`00874a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md#insn-00874a70)
- 新版 `00874aa8`（命令位置の公開資料なし） · `00874ac8`（命令位置の公開資料なし）

~~~diff
- 00874a50 ["INT_ADD", "register:40f0:8", ["const:874a50:8", "const:4:8"]]
- 00874a50 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874aa8 ["INT_ADD", "register:40f0:8", ["const:874aa8:8", "const:4:8"]]
+ 00874aa8 ["CALL", null, ["callee:00c53da0:8"]]
- 00874a50 bytes ac7c0f94
+ 00874aa8 bytes be7c0f94
- 00874a70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874a70 ["INT_ADD", "register:40f0:8", ["const:874a70:8", "const:4:8"]]
- 00874a70 ["CALLIND", null, ["register:0:8"]]
+ 00874ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ac8 ["INT_ADD", "register:40f0:8", ["const:874ac8:8", "const:4:8"]]
+ 00874ac8 ["CALLIND", null, ["register:0:8"]]
- 00874a70 bytes 00013fd6
+ 00874ac8 bytes 00013fd6
~~~


<a id="compare-5c0bdec45ee27121621b08b2dd77268a"></a>

### [`00874a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md) → [`00874adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874adc.md) FUN_00874adc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md#insn-00874aa4) · [`00874ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md#insn-00874ab8) · [`00874ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md#insn-00874ac0)
- 新版 `00874afc`（命令位置の公開資料なし） · `00874b10`（命令位置の公開資料なし） · `00874b18`（命令位置の公開資料なし）

~~~diff
- 00874aa4 ["INT_ADD", "register:40f0:8", ["const:874aa4:8", "const:4:8"]]
- 00874aa4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874afc ["INT_ADD", "register:40f0:8", ["const:874afc:8", "const:4:8"]]
+ 00874afc ["CALL", null, ["callee:00c53da0:8"]]
- 00874aa4 bytes 977c0f94
+ 00874afc bytes a97c0f94
- 00874ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874ab8 ["INT_ADD", "register:40f0:8", ["const:874ab8:8", "const:4:8"]]
- 00874ab8 ["CALLIND", null, ["register:0:8"]]
+ 00874b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874b10 ["INT_ADD", "register:40f0:8", ["const:874b10:8", "const:4:8"]]
+ 00874b10 ["CALLIND", null, ["register:0:8"]]
- 00874ab8 bytes 00013fd6
+ 00874b10 bytes 00013fd6
- 00874ac0 ["INT_ADD", "register:40f0:8", ["const:874ac0:8", "const:4:8"]]
- 00874ac0 ["CALL", null, ["callee:00c57f50:8"]]
+ 00874b18 ["INT_ADD", "register:40f0:8", ["const:874b18:8", "const:4:8"]]
+ 00874b18 ["CALL", null, ["callee:00c57f50:8"]]
- 00874ac0 bytes f08c0f94
+ 00874b18 bytes 0e8d0f94
~~~


<a id="compare-507e5aa4bf0393299c537b79e65e6800"></a>

### [`00874b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b0c.md) → [`00874b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874b64.md) FUN_00874b64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b0c.md#insn-00874b28) · [`00874b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b0c.md#insn-00874b48)
- 新版 `00874b80`（命令位置の公開資料なし） · `00874ba0`（命令位置の公開資料なし）

~~~diff
- 00874b28 ["INT_ADD", "register:40f0:8", ["const:874b28:8", "const:4:8"]]
- 00874b28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874b80 ["INT_ADD", "register:40f0:8", ["const:874b80:8", "const:4:8"]]
+ 00874b80 ["CALL", null, ["callee:00c53da0:8"]]
- 00874b28 bytes 767c0f94
+ 00874b80 bytes 887c0f94
- 00874b48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874b48 ["INT_ADD", "register:40f0:8", ["const:874b48:8", "const:4:8"]]
- 00874b48 ["CALLIND", null, ["register:0:8"]]
+ 00874ba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ba0 ["INT_ADD", "register:40f0:8", ["const:874ba0:8", "const:4:8"]]
+ 00874ba0 ["CALLIND", null, ["register:0:8"]]
- 00874b48 bytes 00013fd6
+ 00874ba0 bytes 00013fd6
~~~


<a id="compare-6f8993bda57093a200bafa71f08c32dd"></a>

### [`00874ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md) → [`00874d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d00.md) FUN_00874d00

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md#insn-00874cc4) · [`00874ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md#insn-00874ce4)
- 新版 `00874d1c`（命令位置の公開資料なし） · `00874d3c`（命令位置の公開資料なし）

~~~diff
- 00874cc4 ["INT_ADD", "register:40f0:8", ["const:874cc4:8", "const:4:8"]]
- 00874cc4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874d1c ["INT_ADD", "register:40f0:8", ["const:874d1c:8", "const:4:8"]]
+ 00874d1c ["CALL", null, ["callee:00c53da0:8"]]
- 00874cc4 bytes 0f7c0f94
+ 00874d1c bytes 217c0f94
- 00874ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874ce4 ["INT_ADD", "register:40f0:8", ["const:874ce4:8", "const:4:8"]]
- 00874ce4 ["CALLIND", null, ["register:0:8"]]
+ 00874d3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874d3c ["INT_ADD", "register:40f0:8", ["const:874d3c:8", "const:4:8"]]
+ 00874d3c ["CALLIND", null, ["register:0:8"]]
- 00874ce4 bytes 00013fd6
+ 00874d3c bytes 00013fd6
~~~


<a id="compare-6afb076b612c7ed8b76808ddbbda72a4"></a>

### [`00874cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md) → [`00874d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md) FUN_00874d50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md#insn-00874d18) · [`00874d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md#insn-00874d2c) · [`00874d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md#insn-00874d34)
- 新版 `00874d70`（命令位置の公開資料なし） · `00874d84`（命令位置の公開資料なし） · `00874d8c`（命令位置の公開資料なし）

~~~diff
- 00874d18 ["INT_ADD", "register:40f0:8", ["const:874d18:8", "const:4:8"]]
- 00874d18 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874d70 ["INT_ADD", "register:40f0:8", ["const:874d70:8", "const:4:8"]]
+ 00874d70 ["CALL", null, ["callee:00c53da0:8"]]
- 00874d18 bytes fa7b0f94
+ 00874d70 bytes 0c7c0f94
- 00874d2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00874d2c ["INT_ADD", "register:40f0:8", ["const:874d2c:8", "const:4:8"]]
- 00874d2c ["CALLIND", null, ["register:0:8"]]
+ 00874d84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874d84 ["INT_ADD", "register:40f0:8", ["const:874d84:8", "const:4:8"]]
+ 00874d84 ["CALLIND", null, ["register:0:8"]]
- 00874d2c bytes 00013fd6
+ 00874d84 bytes 00013fd6
- 00874d34 ["INT_ADD", "register:40f0:8", ["const:874d34:8", "const:4:8"]]
- 00874d34 ["CALL", null, ["callee:00c57f50:8"]]
+ 00874d8c ["INT_ADD", "register:40f0:8", ["const:874d8c:8", "const:4:8"]]
+ 00874d8c ["CALL", null, ["callee:00c57f50:8"]]
- 00874d34 bytes 538c0f94
+ 00874d8c bytes 718c0f94
~~~


<a id="compare-b2d44c3f4e91481857505905ae4decd9"></a>

### [`00874f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f44.md) → [`00874f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874f9c.md) FUN_00874f9c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00874f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f44.md#insn-00874f60) · [`00874f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f44.md#insn-00874f80)
- 新版 `00874fb8`（命令位置の公開資料なし） · `00874fd8`（命令位置の公開資料なし）

~~~diff
- 00874f60 ["INT_ADD", "register:40f0:8", ["const:874f60:8", "const:4:8"]]
- 00874f60 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874fb8 ["INT_ADD", "register:40f0:8", ["const:874fb8:8", "const:4:8"]]
+ 00874fb8 ["CALL", null, ["callee:00c53da0:8"]]
- 00874f60 bytes 687b0f94
+ 00874fb8 bytes 7a7b0f94
- 00874f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874f80 ["INT_ADD", "register:40f0:8", ["const:874f80:8", "const:4:8"]]
- 00874f80 ["CALLIND", null, ["register:0:8"]]
+ 00874fd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874fd8 ["INT_ADD", "register:40f0:8", ["const:874fd8:8", "const:4:8"]]
+ 00874fd8 ["CALLIND", null, ["register:0:8"]]
- 00874f80 bytes 00013fd6
+ 00874fd8 bytes 00013fd6
~~~


<a id="compare-4d64a97522c18c549709def4b5f6d7ec"></a>

### [`008750e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md) → [`00875138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md) FUN_00875138

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008750fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md#insn-008750fc) · [`0087511c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md#insn-0087511c)
- 新版 `00875154`（命令位置の公開資料なし） · `00875174`（命令位置の公開資料なし）

~~~diff
- 008750fc ["INT_ADD", "register:40f0:8", ["const:8750fc:8", "const:4:8"]]
- 008750fc ["CALL", null, ["callee:00c53da0:8"]]
+ 00875154 ["INT_ADD", "register:40f0:8", ["const:875154:8", "const:4:8"]]
+ 00875154 ["CALL", null, ["callee:00c53da0:8"]]
- 008750fc bytes 017b0f94
+ 00875154 bytes 137b0f94
- 0087511c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087511c ["INT_ADD", "register:40f0:8", ["const:87511c:8", "const:4:8"]]
- 0087511c ["CALLIND", null, ["register:0:8"]]
+ 00875174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875174 ["INT_ADD", "register:40f0:8", ["const:875174:8", "const:4:8"]]
+ 00875174 ["CALLIND", null, ["register:0:8"]]
- 0087511c bytes 00013fd6
+ 00875174 bytes 00013fd6
~~~


<a id="compare-e02902d0a2a213c4ba4d9ff45ba7c6a4"></a>

### [`00875130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md) → [`00875188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875188.md) FUN_00875188

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md#insn-00875150) · [`00875164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md#insn-00875164) · [`0087516c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md#insn-0087516c)
- 新版 `008751a8`（命令位置の公開資料なし） · `008751bc`（命令位置の公開資料なし） · `008751c4`（命令位置の公開資料なし）

~~~diff
- 00875150 ["INT_ADD", "register:40f0:8", ["const:875150:8", "const:4:8"]]
- 00875150 ["CALL", null, ["callee:00c53da0:8"]]
+ 008751a8 ["INT_ADD", "register:40f0:8", ["const:8751a8:8", "const:4:8"]]
+ 008751a8 ["CALL", null, ["callee:00c53da0:8"]]
- 00875150 bytes ec7a0f94
+ 008751a8 bytes fe7a0f94
- 00875164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875164 ["INT_ADD", "register:40f0:8", ["const:875164:8", "const:4:8"]]
- 00875164 ["CALLIND", null, ["register:0:8"]]
+ 008751bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008751bc ["INT_ADD", "register:40f0:8", ["const:8751bc:8", "const:4:8"]]
+ 008751bc ["CALLIND", null, ["register:0:8"]]
- 00875164 bytes 00013fd6
+ 008751bc bytes 00013fd6
- 0087516c ["INT_ADD", "register:40f0:8", ["const:87516c:8", "const:4:8"]]
- 0087516c ["CALL", null, ["callee:00c57f50:8"]]
+ 008751c4 ["INT_ADD", "register:40f0:8", ["const:8751c4:8", "const:4:8"]]
+ 008751c4 ["CALL", null, ["callee:00c57f50:8"]]
- 0087516c bytes 458b0f94
+ 008751c4 bytes 638b0f94
~~~


<a id="compare-3148e9b706ab190fb9a18389cdecabda"></a>

### [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md) → [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md) FUN_00875434

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087546c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md#insn-0087546c) · [`008754c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md#insn-008754c8) · [`00875518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md#insn-00875518)
- 新版 `008754c4`（命令位置の公開資料なし） · `00875520`（命令位置の公開資料なし） · `00875570`（命令位置の公開資料なし）

~~~diff
- 0087546c ["INT_ADD", "register:40f0:8", ["const:87546c:8", "const:4:8"]]
- 0087546c ["CALL", null, ["callee:00c58120:8"]]
+ 008754c4 ["INT_ADD", "register:40f0:8", ["const:8754c4:8", "const:4:8"]]
+ 008754c4 ["CALL", null, ["callee:00c58120:8"]]
- 0087546c bytes f98a0f94
+ 008754c4 bytes 178b0f94
- 008754c8 ["INT_ADD", "register:40f0:8", ["const:8754c8:8", "const:4:8"]]
- 008754c8 ["CALL", null, ["callee:00c58120:8"]]
+ 00875520 ["INT_ADD", "register:40f0:8", ["const:875520:8", "const:4:8"]]
+ 00875520 ["CALL", null, ["callee:00c58120:8"]]
- 008754c8 bytes e28a0f94
+ 00875520 bytes 008b0f94
- 00875518 ["INT_ADD", "register:40f0:8", ["const:875518:8", "const:4:8"]]
- 00875518 ["CALL", null, ["callee:00875674:8"]]
+ 00875570 ["INT_ADD", "register:40f0:8", ["const:875570:8", "const:4:8"]]
+ 00875570 ["CALL", null, ["callee:00875674:8"]]
- 00875518 bytes 41000094
+ 00875570 bytes 41000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe598d8b6cd68e0f6f3d1729fb515969"></a>

### [`008755cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008755cc.md) → [`00875624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875624.md) FUN_00875624

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008755e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008755cc.md#insn-008755e8) · [`00875608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008755cc.md#insn-00875608)
- 新版 `00875640`（命令位置の公開資料なし） · `00875660`（命令位置の公開資料なし）

~~~diff
- 008755e8 ["INT_ADD", "register:40f0:8", ["const:8755e8:8", "const:4:8"]]
- 008755e8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875640 ["INT_ADD", "register:40f0:8", ["const:875640:8", "const:4:8"]]
+ 00875640 ["CALL", null, ["callee:00c53da0:8"]]
- 008755e8 bytes c6790f94
+ 00875640 bytes d8790f94
- 00875608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875608 ["INT_ADD", "register:40f0:8", ["const:875608:8", "const:4:8"]]
- 00875608 ["CALLIND", null, ["register:0:8"]]
+ 00875660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875660 ["INT_ADD", "register:40f0:8", ["const:875660:8", "const:4:8"]]
+ 00875660 ["CALLIND", null, ["register:0:8"]]
- 00875608 bytes 00013fd6
+ 00875660 bytes 00013fd6
~~~


<a id="compare-ca1c5d88c0149e1d2cf3bb775789e3e4"></a>

### [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) → [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) FUN_00875674

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md) · 呼出先 2件 [`008758b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md) · 呼出先 2件 [`00875910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008756a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md#insn-008756a4) · [`008756f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md#insn-008756f8) · [`00875794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md#insn-00875794)
- 新版 `008756fc`（命令位置の公開資料なし） · `00875750`（命令位置の公開資料なし） · `008757ec`（命令位置の公開資料なし）

~~~diff
- 008756a4 ["INT_ADD", "register:40f0:8", ["const:8756a4:8", "const:4:8"]]
- 008756a4 ["CALL", null, ["callee:00c58120:8"]]
+ 008756fc ["INT_ADD", "register:40f0:8", ["const:8756fc:8", "const:4:8"]]
+ 008756fc ["CALL", null, ["callee:00c58120:8"]]
- 008756a4 bytes 6b8a0f94
+ 008756fc bytes 898a0f94
- 008756f8 ["INT_ADD", "register:40f0:8", ["const:8756f8:8", "const:4:8"]]
- 008756f8 ["CALL", null, ["callee:00c58120:8"]]
+ 00875750 ["INT_ADD", "register:40f0:8", ["const:875750:8", "const:4:8"]]
+ 00875750 ["CALL", null, ["callee:00c58120:8"]]
- 008756f8 bytes 568a0f94
+ 00875750 bytes 748a0f94
- 00875794 ["INT_ADD", "register:40f0:8", ["const:875794:8", "const:4:8"]]
- 00875794 ["CALL", null, ["callee:00c58120:8"]]
+ 008757ec ["INT_ADD", "register:40f0:8", ["const:8757ec:8", "const:4:8"]]
+ 008757ec ["CALL", null, ["callee:00c58120:8"]]
- 00875794 bytes 2f8a0f94
+ 008757ec bytes 4d8a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a5a16da24ded3632d5c77222e4deca"></a>

### [`008758b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md) → [`00875910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md) FUN_00875910

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0087561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087561c.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md#insn-0087593c) · [`00875968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008758b8.md#insn-00875968)
- 新版 `00875994`（命令位置の公開資料なし） · `008759c0`（命令位置の公開資料なし）

~~~diff
- 0087593c ["INT_ADD", "register:40f0:8", ["const:87593c:8", "const:4:8"]]
- 0087593c ["CALL", null, ["callee:00c58120:8"]]
+ 00875994 ["INT_ADD", "register:40f0:8", ["const:875994:8", "const:4:8"]]
+ 00875994 ["CALL", null, ["callee:00c58120:8"]]
- 0087593c bytes c5890f94
+ 00875994 bytes e3890f94
- 00875968 ["INT_ADD", "register:40f0:8", ["const:875968:8", "const:4:8"]]
- 00875968 ["CALL", null, ["callee:00c58120:8"]]
+ 008759c0 ["INT_ADD", "register:40f0:8", ["const:8759c0:8", "const:4:8"]]
+ 008759c0 ["CALL", null, ["callee:00c58120:8"]]
- 00875968 bytes ba890f94
+ 008759c0 bytes d8890f94
~~~


<a id="compare-356575a96d280b3dfbb0961888f71fa8"></a>

### [`00875ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ba4.md) → [`00875bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bfc.md) FUN_00875bfc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ba4.md#insn-00875bc0) · [`00875be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ba4.md#insn-00875be0)
- 新版 `00875c18`（命令位置の公開資料なし） · `00875c38`（命令位置の公開資料なし）

~~~diff
- 00875bc0 ["INT_ADD", "register:40f0:8", ["const:875bc0:8", "const:4:8"]]
- 00875bc0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875c18 ["INT_ADD", "register:40f0:8", ["const:875c18:8", "const:4:8"]]
+ 00875c18 ["CALL", null, ["callee:00c53da0:8"]]
- 00875bc0 bytes 50780f94
+ 00875c18 bytes 62780f94
- 00875be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875be0 ["INT_ADD", "register:40f0:8", ["const:875be0:8", "const:4:8"]]
- 00875be0 ["CALLIND", null, ["register:0:8"]]
+ 00875c38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875c38 ["INT_ADD", "register:40f0:8", ["const:875c38:8", "const:4:8"]]
+ 00875c38 ["CALLIND", null, ["register:0:8"]]
- 00875be0 bytes 00013fd6
+ 00875c38 bytes 00013fd6
~~~


<a id="compare-15e9b62cf4268ea81caea82e53f46f77"></a>

### [`00875bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875bf4.md) → [`00875c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c4c.md) FUN_00875c4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875bf4.md#insn-00875c14) · [`00875c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875bf4.md#insn-00875c28) · [`00875c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875bf4.md#insn-00875c30)
- 新版 `00875c6c`（命令位置の公開資料なし） · `00875c80`（命令位置の公開資料なし） · `00875c88`（命令位置の公開資料なし）

~~~diff
- 00875c14 ["INT_ADD", "register:40f0:8", ["const:875c14:8", "const:4:8"]]
- 00875c14 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875c6c ["INT_ADD", "register:40f0:8", ["const:875c6c:8", "const:4:8"]]
+ 00875c6c ["CALL", null, ["callee:00c53da0:8"]]
- 00875c14 bytes 3b780f94
+ 00875c6c bytes 4d780f94
- 00875c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875c28 ["INT_ADD", "register:40f0:8", ["const:875c28:8", "const:4:8"]]
- 00875c28 ["CALLIND", null, ["register:0:8"]]
+ 00875c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875c80 ["INT_ADD", "register:40f0:8", ["const:875c80:8", "const:4:8"]]
+ 00875c80 ["CALLIND", null, ["register:0:8"]]
- 00875c28 bytes 00013fd6
+ 00875c80 bytes 00013fd6
- 00875c30 ["INT_ADD", "register:40f0:8", ["const:875c30:8", "const:4:8"]]
- 00875c30 ["CALL", null, ["callee:00c57f50:8"]]
+ 00875c88 ["INT_ADD", "register:40f0:8", ["const:875c88:8", "const:4:8"]]
+ 00875c88 ["CALL", null, ["callee:00c57f50:8"]]
- 00875c30 bytes 94880f94
+ 00875c88 bytes b2880f94
~~~


<a id="compare-6f63ca1fecb317b62ed47c80f9b6d4d9"></a>

### [`00875e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e1c.md) → [`00875e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875e74.md) FUN_00875e74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e1c.md#insn-00875e38) · [`00875e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e1c.md#insn-00875e58)
- 新版 `00875e90`（命令位置の公開資料なし） · `00875eb0`（命令位置の公開資料なし）

~~~diff
- 00875e38 ["INT_ADD", "register:40f0:8", ["const:875e38:8", "const:4:8"]]
- 00875e38 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875e90 ["INT_ADD", "register:40f0:8", ["const:875e90:8", "const:4:8"]]
+ 00875e90 ["CALL", null, ["callee:00c53da0:8"]]
- 00875e38 bytes b2770f94
+ 00875e90 bytes c4770f94
- 00875e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875e58 ["INT_ADD", "register:40f0:8", ["const:875e58:8", "const:4:8"]]
- 00875e58 ["CALLIND", null, ["register:0:8"]]
+ 00875eb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875eb0 ["INT_ADD", "register:40f0:8", ["const:875eb0:8", "const:4:8"]]
+ 00875eb0 ["CALLIND", null, ["register:0:8"]]
- 00875e58 bytes 00013fd6
+ 00875eb0 bytes 00013fd6
~~~


<a id="compare-eb37a19ab0f1bbf2a1423478d3e9f878"></a>

### [`00875fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md) → [`00876010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876010.md) FUN_00876010

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00875cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md#insn-00875fd4) · [`00875ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md#insn-00875ff4)
- 新版 `0087602c`（命令位置の公開資料なし） · `0087604c`（命令位置の公開資料なし）

~~~diff
- 00875fd4 ["INT_ADD", "register:40f0:8", ["const:875fd4:8", "const:4:8"]]
- 00875fd4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087602c ["INT_ADD", "register:40f0:8", ["const:87602c:8", "const:4:8"]]
+ 0087602c ["CALL", null, ["callee:00c53da0:8"]]
- 00875fd4 bytes 4b770f94
+ 0087602c bytes 5d770f94
- 00875ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875ff4 ["INT_ADD", "register:40f0:8", ["const:875ff4:8", "const:4:8"]]
- 00875ff4 ["CALLIND", null, ["register:0:8"]]
+ 0087604c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087604c ["INT_ADD", "register:40f0:8", ["const:87604c:8", "const:4:8"]]
+ 0087604c ["CALLIND", null, ["register:0:8"]]
- 00875ff4 bytes 00013fd6
+ 0087604c bytes 00013fd6
~~~


<a id="compare-55c67c3ae6d419ca8dc32823164620d7"></a>

### [`00876008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md) → [`00876060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md) FUN_00876060

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00875cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00876028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md#insn-00876028) · [`0087603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md#insn-0087603c) · [`00876044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md#insn-00876044)
- 新版 `00876080`（命令位置の公開資料なし） · `00876094`（命令位置の公開資料なし） · `0087609c`（命令位置の公開資料なし）

~~~diff
- 00876028 ["INT_ADD", "register:40f0:8", ["const:876028:8", "const:4:8"]]
- 00876028 ["CALL", null, ["callee:00c53da0:8"]]
+ 00876080 ["INT_ADD", "register:40f0:8", ["const:876080:8", "const:4:8"]]
+ 00876080 ["CALL", null, ["callee:00c53da0:8"]]
- 00876028 bytes 36770f94
+ 00876080 bytes 48770f94
- 0087603c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087603c ["INT_ADD", "register:40f0:8", ["const:87603c:8", "const:4:8"]]
- 0087603c ["CALLIND", null, ["register:0:8"]]
+ 00876094 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00876094 ["INT_ADD", "register:40f0:8", ["const:876094:8", "const:4:8"]]
+ 00876094 ["CALLIND", null, ["register:0:8"]]
- 0087603c bytes 00013fd6
+ 00876094 bytes 00013fd6
- 00876044 ["INT_ADD", "register:40f0:8", ["const:876044:8", "const:4:8"]]
- 00876044 ["CALL", null, ["callee:00c57f50:8"]]
+ 0087609c ["INT_ADD", "register:40f0:8", ["const:87609c:8", "const:4:8"]]
+ 0087609c ["CALL", null, ["callee:00c57f50:8"]]
- 00876044 bytes 8f870f94
+ 0087609c bytes ad870f94
~~~


<a id="compare-807bd99a9ef370108afa37e7c21a01ef"></a>

### [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) → [`008760e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008760e8.md) FUN_008760e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) · 呼出先 2件 [`00876090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) [`008760e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008760e8.md) · 呼出先 2件 [`008760e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008760e8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008760ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md#insn-008760ac) · [`008760b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md#insn-008760b8) · [`008760c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876090.md#insn-008760c8)
- 新版 `00876104`（命令位置の公開資料なし） · `00876110`（命令位置の公開資料なし） · `00876120`（命令位置の公開資料なし）

~~~diff
- 008760ac ["INT_ADD", "register:40f0:8", ["const:8760ac:8", "const:4:8"]]
- 008760ac ["CALL", null, ["local:b0:8"]]
+ 00876104 ["INT_ADD", "register:40f0:8", ["const:876104:8", "const:4:8"]]
+ 00876104 ["CALL", null, ["local:b0:8"]]
- 008760ac bytes f9ffff97
+ 00876104 bytes f9ffff97
- 008760b8 ["INT_ADD", "register:40f0:8", ["const:8760b8:8", "const:4:8"]]
- 008760b8 ["CALL", null, ["local:b0:8"]]
+ 00876110 ["INT_ADD", "register:40f0:8", ["const:876110:8", "const:4:8"]]
+ 00876110 ["CALL", null, ["local:b0:8"]]
- 008760b8 bytes f6ffff97
+ 00876110 bytes f6ffff97
- 008760c8 ["INT_ADD", "register:40f0:8", ["const:8760c8:8", "const:4:8"]]
- 008760c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00876120 ["INT_ADD", "register:40f0:8", ["const:876120:8", "const:4:8"]]
+ 00876120 ["CALL", null, ["callee:00c57f80:8"]]
- 008760c8 bytes 7a870f94
+ 00876120 bytes 98870f94
~~~


<a id="compare-31cbc84d0380624ceea38f09d9191b97"></a>

### [`008778c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md) → [`00877918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md) FUN_00877918

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 5件 [`00877c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 1件 [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 5件 [`00877c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877c78.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008778dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md#insn-008778dc) · [`008778e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md#insn-008778e8) · [`00877904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md#insn-00877904)
- 新版 `00877934`（命令位置の公開資料なし） · `00877940`（命令位置の公開資料なし） · `0087795c`（命令位置の公開資料なし）

~~~diff
- 008778dc ["INT_ADD", "register:40f0:8", ["const:8778dc:8", "const:4:8"]]
- 008778dc ["CALL", null, ["callee:00c58500:8"]]
+ 00877934 ["INT_ADD", "register:40f0:8", ["const:877934:8", "const:4:8"]]
+ 00877934 ["CALL", null, ["callee:00c58500:8"]]
- 008778dc bytes d5820f94
+ 00877934 bytes f3820f94
- 008778e8 ["INT_ADD", "register:40f0:8", ["const:8778e8:8", "const:4:8"]]
- 008778e8 ["CALL", null, ["callee:00c58500:8"]]
+ 00877940 ["INT_ADD", "register:40f0:8", ["const:877940:8", "const:4:8"]]
+ 00877940 ["CALL", null, ["callee:00c58500:8"]]
- 008778e8 bytes d2820f94
+ 00877940 bytes f0820f94
- 00877904 ["INT_ADD", "register:40f0:8", ["const:877904:8", "const:4:8"]]
- 00877904 ["CALL", null, ["callee:00c53d70:8"]]
+ 0087795c ["INT_ADD", "register:40f0:8", ["const:87795c:8", "const:4:8"]]
+ 0087795c ["CALL", null, ["callee:00c53d70:8"]]
- 00877904 bytes f3700f94
+ 0087795c bytes 05710f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38a8746977974b9ec831985d2303211a"></a>

### [`00877a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md) → [`00877a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md) FUN_00877a68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 6件 [`00446a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446a48.md) [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58170.md)
- 新版 呼出元 1件 [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 6件 [`00446a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446a88.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c58240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58240.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md#insn-00877a2c) · [`00877a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md#insn-00877a34) · [`00877a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a10.md#insn-00877a3c)
- 新版 `00877a84`（命令位置の公開資料なし） · `00877a8c`（命令位置の公開資料なし） · `00877a94`（命令位置の公開資料なし）

~~~diff
- 00877a2c ["INT_ADD", "register:40f0:8", ["const:877a2c:8", "const:4:8"]]
- 00877a2c ["CALL", null, ["callee:00446a88:8"]]
+ 00877a84 ["INT_ADD", "register:40f0:8", ["const:877a84:8", "const:4:8"]]
+ 00877a84 ["CALL", null, ["callee:00446a88:8"]]
- 00877a2c bytes 073cef97
+ 00877a84 bytes 013cef97
- 00877a34 ["INT_ADD", "register:40f0:8", ["const:877a34:8", "const:4:8"]]
- 00877a34 ["CALL", null, ["callee:00c58240:8"]]
+ 00877a8c ["INT_ADD", "register:40f0:8", ["const:877a8c:8", "const:4:8"]]
+ 00877a8c ["CALL", null, ["callee:00c58240:8"]]
- 00877a34 bytes cf810f94
+ 00877a8c bytes ed810f94
- 00877a3c ["INT_ADD", "register:40f0:8", ["const:877a3c:8", "const:4:8"]]
- 00877a3c ["CALL", null, ["callee:00c58250:8"]]
+ 00877a94 ["INT_ADD", "register:40f0:8", ["const:877a94:8", "const:4:8"]]
+ 00877a94 ["CALL", null, ["callee:00c58250:8"]]
- 00877a3c bytes d1810f94
+ 00877a94 bytes ef810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93dcd7bcf025f61aa7f1c983ce1189e2"></a>

### [`00877c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md) → [`00877c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877c78.md) FUN_00877c78

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008778c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/008778c0.md) · 呼出先 5件 [`0048b544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00877918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md) · 呼出先 5件 [`0048b584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md#insn-00877c64) · [`00877cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md#insn-00877cac) · [`00877cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md#insn-00877cd4)
- 新版 `00877cbc`（命令位置の公開資料なし） · `00877d04`（命令位置の公開資料なし） · `00877d2c`（命令位置の公開資料なし）

~~~diff
- 00877c64 ["INT_ADD", "register:40f0:8", ["const:877c64:8", "const:4:8"]]
- 00877c64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00877cbc ["INT_ADD", "register:40f0:8", ["const:877cbc:8", "const:4:8"]]
+ 00877cbc ["CALL", null, ["callee:00c57f80:8"]]
- 00877c64 bytes 93800f94
+ 00877cbc bytes b1800f94
- 00877cac ["INT_ADD", "register:40f0:8", ["const:877cac:8", "const:4:8"]]
- 00877cac ["CALL", null, ["callee:00c57f60:8"]]
+ 00877d04 ["INT_ADD", "register:40f0:8", ["const:877d04:8", "const:4:8"]]
+ 00877d04 ["CALL", null, ["callee:00c57f60:8"]]
- 00877cac bytes 79800f94
+ 00877d04 bytes 97800f94
- 00877cd4 ["INT_ADD", "register:40f0:8", ["const:877cd4:8", "const:4:8"]]
- 00877cd4 ["CALL", null, ["callee:00c580d0:8"]]
+ 00877d2c ["INT_ADD", "register:40f0:8", ["const:877d2c:8", "const:4:8"]]
+ 00877d2c ["CALL", null, ["callee:00c580d0:8"]]
- 00877cd4 bytes cb800f94
+ 00877d2c bytes e9800f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c872aaf64ffdf7f0b784b3f8453356c8"></a>

### [`00877d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md) → [`00877da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877da8.md) FUN_00877da8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00877a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md) · 呼出先 9件 [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00877ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md) · 呼出先 9件 [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md#insn-00877d78) · [`00877d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md#insn-00877d88) · [`00877d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md#insn-00877d94)
- 新版 `00877dd0`（命令位置の公開資料なし） · `00877de0`（命令位置の公開資料なし） · `00877dec`（命令位置の公開資料なし）

~~~diff
- 00877d78 ["INT_ADD", "register:40f0:8", ["const:877d78:8", "const:4:8"]]
- 00877d78 ["CALL", null, ["callee:00c58200:8"]]
+ 00877dd0 ["INT_ADD", "register:40f0:8", ["const:877dd0:8", "const:4:8"]]
+ 00877dd0 ["CALL", null, ["callee:00c58200:8"]]
- 00877d78 bytes ee800f94
+ 00877dd0 bytes 0c810f94
- 00877d88 ["INT_ADD", "register:40f0:8", ["const:877d88:8", "const:4:8"]]
- 00877d88 ["CALL", null, ["callee:00c58210:8"]]
+ 00877de0 ["INT_ADD", "register:40f0:8", ["const:877de0:8", "const:4:8"]]
+ 00877de0 ["CALL", null, ["callee:00c58210:8"]]
- 00877d88 bytes ee800f94
+ 00877de0 bytes 0c810f94
- 00877d94 ["INT_ADD", "register:40f0:8", ["const:877d94:8", "const:4:8"]]
- 00877d94 ["CALL", null, ["callee:00597e88:8"]]
+ 00877dec ["INT_ADD", "register:40f0:8", ["const:877dec:8", "const:4:8"]]
+ 00877dec ["CALL", null, ["callee:00597e88:8"]]
- 00877d94 bytes 2d80f497
+ 00877dec bytes 2780f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b3277c5aabb5ae04858c91ff08fc67d"></a>

### [`00877e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e48.md) → [`00877ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ea0.md) FUN_00877ea0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e48.md#insn-00877e70) · [`00877e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e48.md#insn-00877e78)
- 新版 `00877ec8`（命令位置の公開資料なし） · `00877ed0`（命令位置の公開資料なし）

~~~diff
- 00877e70 ["INT_ADD", "register:40f0:8", ["const:877e70:8", "const:4:8"]]
- 00877e70 ["CALL", null, ["callee:00c58220:8"]]
+ 00877ec8 ["INT_ADD", "register:40f0:8", ["const:877ec8:8", "const:4:8"]]
+ 00877ec8 ["CALL", null, ["callee:00c58220:8"]]
- 00877e70 bytes b8800f94
+ 00877ec8 bytes d6800f94
- 00877e78 ["INT_ADD", "register:40f0:8", ["const:877e78:8", "const:4:8"]]
- 00877e78 ["CALL", null, ["callee:00c57f80:8"]]
+ 00877ed0 ["INT_ADD", "register:40f0:8", ["const:877ed0:8", "const:4:8"]]
+ 00877ed0 ["CALL", null, ["callee:00c57f80:8"]]
- 00877e78 bytes 0e800f94
+ 00877ed0 bytes 2c800f94
~~~


<a id="compare-ec005178cd105e53ad55f5003015d9b9"></a>

### [`0087822c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/0087822c.md) → [`00878284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878284.md) FUN_00878284

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`008486d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/008486d8.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md)
- 新版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848730.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087823c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/0087822c.md#insn-0087823c) · [`0087824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/0087822c.md#insn-0087824c)
- 新版 `00878294`（命令位置の公開資料なし） · `008782a4`（命令位置の公開資料なし）

~~~diff
- 0087823c ["INT_ADD", "register:40f0:8", ["const:87823c:8", "const:4:8"]]
- 0087823c ["CALL", null, ["callee:00c5aa10:8"]]
+ 00878294 ["INT_ADD", "register:40f0:8", ["const:878294:8", "const:4:8"]]
+ 00878294 ["CALL", null, ["callee:00c5aa10:8"]]
- 0087823c bytes c1890f94
+ 00878294 bytes df890f94
- 0087824c ["INT_ADD", "register:40f0:8", ["const:87824c:8", "const:4:8"]]
- 0087824c ["CALL", null, ["callee:00c57f80:8"]]
+ 008782a4 ["INT_ADD", "register:40f0:8", ["const:8782a4:8", "const:4:8"]]
+ 008782a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0087824c bytes 197f0f94
+ 008782a4 bytes 377f0f94
~~~


<a id="compare-31d28c024cc0082ef466cf92ffaac2c1"></a>

### [`008782b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md) → [`00878310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md) FUN_00878310

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`007681b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007681b4.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00881d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881d7c.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00b3c6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c6c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0076820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00881dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881dd4.md) · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00b3c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008782e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md#insn-008782e8) · [`00878334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md#insn-00878334) · [`00878354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md#insn-00878354)
- 新版 `00878340`（命令位置の公開資料なし） · `0087838c`（命令位置の公開資料なし） · `008783ac`（命令位置の公開資料なし）

~~~diff
- 008782e8 ["INT_ADD", "register:40f0:8", ["const:8782e8:8", "const:4:8"]]
- 008782e8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00878340 ["INT_ADD", "register:40f0:8", ["const:878340:8", "const:4:8"]]
+ 00878340 ["CALL", null, ["callee:00c580b0:8"]]
- 008782e8 bytes 3e7f0f94
+ 00878340 bytes 5c7f0f94
- 00878334 ["INT_ADD", "register:40f0:8", ["const:878334:8", "const:4:8"]]
- 00878334 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087838c ["INT_ADD", "register:40f0:8", ["const:87838c:8", "const:4:8"]]
+ 0087838c ["CALL", null, ["callee:00c57f60:8"]]
- 00878334 bytes d77e0f94
+ 0087838c bytes f57e0f94
- 00878354 ["INT_ADD", "register:40f0:8", ["const:878354:8", "const:4:8"]]
- 00878354 ["CALL", null, ["callee:00c580d0:8"]]
+ 008783ac ["INT_ADD", "register:40f0:8", ["const:8783ac:8", "const:4:8"]]
+ 008783ac ["CALL", null, ["callee:00c580d0:8"]]
- 00878354 bytes 2b7f0f94
+ 008783ac bytes 497f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abdf09443baf1c10e34033aa6f6bc535"></a>

### [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) → [`00879c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879c10.md) FUN_00879c10

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1338.md) · 呼出先 7件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005b1378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1378.md) · 呼出先 7件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md) [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00879c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md#insn-00879c00) · [`00879c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md#insn-00879c08) · [`00879c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md#insn-00879c0c)
- 新版 `00879c58`（命令位置の公開資料なし） · `00879c60`（命令位置の公開資料なし） · `00879c64`（命令位置の公開資料なし）

~~~diff
- 00879c00 ["INT_ADD", "register:40f0:8", ["const:879c00:8", "const:4:8"]]
- 00879c00 ["CALL", null, ["callee:00588eac:8"]]
+ 00879c58 ["INT_ADD", "register:40f0:8", ["const:879c58:8", "const:4:8"]]
+ 00879c58 ["CALL", null, ["callee:00588eac:8"]]
- 00879c00 bytes 9b3cf497
+ 00879c58 bytes 953cf497
- 00879c08 ["INT_ADD", "register:40f0:8", ["const:879c08:8", "const:4:8"]]
- 00879c08 ["CALL", null, ["callee:0058919c:8"]]
+ 00879c60 ["INT_ADD", "register:40f0:8", ["const:879c60:8", "const:4:8"]]
+ 00879c60 ["CALL", null, ["callee:0058919c:8"]]
- 00879c08 bytes 553df497
+ 00879c60 bytes 4f3df497
- 00879c0c ["INT_ADD", "register:40f0:8", ["const:879c0c:8", "const:4:8"]]
- 00879c0c ["CALL", null, ["callee:00589890:8"]]
+ 00879c64 ["INT_ADD", "register:40f0:8", ["const:879c64:8", "const:4:8"]]
+ 00879c64 ["CALL", null, ["callee:00589890:8"]]
- 00879c0c bytes 113ff497
+ 00879c64 bytes 0b3ff497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09bfd51161e78508984ffa22145a51a"></a>

### [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) → [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) FUN_00879ce0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00879bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879bb8.md) [`0087e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e5d4.md) [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`00879c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879c10.md) [`0087e62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e62c.md) [`00b66c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md) [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00879cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md#insn-00879cf0) · [`00879d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md#insn-00879d00) · [`00879d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md#insn-00879d10)
- 新版 `00879d48`（命令位置の公開資料なし） · `00879d58`（命令位置の公開資料なし） · `00879d68`（命令位置の公開資料なし）

~~~diff
- 00879cf0 ["INT_ADD", "register:40f0:8", ["const:879cf0:8", "const:4:8"]]
- 00879cf0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00879d48 ["INT_ADD", "register:40f0:8", ["const:879d48:8", "const:4:8"]]
+ 00879d48 ["CALL", null, ["callee:00c57f80:8"]]
- 00879cf0 bytes 70780f94
+ 00879d48 bytes 8e780f94
- 00879d00 ["INT_ADD", "register:40f0:8", ["const:879d00:8", "const:4:8"]]
- 00879d00 ["CALL", null, ["callee:00c57f80:8"]]
+ 00879d58 ["INT_ADD", "register:40f0:8", ["const:879d58:8", "const:4:8"]]
+ 00879d58 ["CALL", null, ["callee:00c57f80:8"]]
- 00879d00 bytes 6c780f94
+ 00879d58 bytes 8a780f94
- 00879d10 ["INT_ADD", "register:40f0:8", ["const:879d10:8", "const:4:8"]]
- 00879d10 ["CALL", null, ["callee:00c57f80:8"]]
+ 00879d68 ["INT_ADD", "register:40f0:8", ["const:879d68:8", "const:4:8"]]
+ 00879d68 ["CALL", null, ["callee:00c57f80:8"]]
- 00879d10 bytes 68780f94
+ 00879d68 bytes 86780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8be59e6f03e867f8c3d45e5b208d900"></a>

### [`0087a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a550.md) → [`0087a5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a5a8.md) FUN_0087a5a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087a58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a550.md#insn-0087a58c)
- 新版 `0087a5e4`（命令位置の公開資料なし）

~~~diff
- 0087a58c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087a58c ["INT_ADD", "register:40f0:8", ["const:87a58c:8", "const:4:8"]]
- 0087a58c ["CALLIND", null, ["register:0:8"]]
+ 0087a5e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087a5e4 ["INT_ADD", "register:40f0:8", ["const:87a5e4:8", "const:4:8"]]
+ 0087a5e4 ["CALLIND", null, ["register:0:8"]]
- 0087a58c bytes 00013fd6
+ 0087a5e4 bytes 00013fd6
~~~


<a id="compare-5c7f637861bd9b5de8b6b1ed5dfb6915"></a>

### [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) → [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) FUN_0087b414

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) [`00b34410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34410.md) [`00b34ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34ea4.md) · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md)
- 新版 呼出元 8件 [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md) [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md) [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) [`00b34f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34f40.md) · 呼出先 4件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md#insn-0087b3cc) · [`0087b3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md#insn-0087b3e4) · [`0087b3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md#insn-0087b3f8)
- 新版 `0087b424`（命令位置の公開資料なし） · `0087b43c`（命令位置の公開資料なし） · `0087b450`（命令位置の公開資料なし）

~~~diff
- 0087b3cc ["INT_ADD", "register:40f0:8", ["const:87b3cc:8", "const:4:8"]]
- 0087b3cc ["CALL", null, ["callee:00c5aad0:8"]]
+ 0087b424 ["INT_ADD", "register:40f0:8", ["const:87b424:8", "const:4:8"]]
+ 0087b424 ["CALL", null, ["callee:00c5aad0:8"]]
- 0087b3cc bytes 8d7d0f94
+ 0087b424 bytes ab7d0f94
- 0087b3e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b3e4 ["INT_ADD", "register:40f0:8", ["const:87b3e4:8", "const:4:8"]]
- 0087b3e4 ["CALLIND", null, ["register:0:8"]]
+ 0087b43c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b43c ["INT_ADD", "register:40f0:8", ["const:87b43c:8", "const:4:8"]]
+ 0087b43c ["CALLIND", null, ["register:0:8"]]
- 0087b3e4 bytes 00013fd6
+ 0087b43c bytes 00013fd6
- 0087b3f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b3f8 ["INT_ADD", "register:40f0:8", ["const:87b3f8:8", "const:4:8"]]
- 0087b3f8 ["CALLIND", null, ["register:0:8"]]
+ 0087b450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b450 ["INT_ADD", "register:40f0:8", ["const:87b450:8", "const:4:8"]]
+ 0087b450 ["CALLIND", null, ["register:0:8"]]
- 0087b3f8 bytes 00013fd6
+ 0087b450 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11dd35d5481a0ffe73bdcca2078fbe3d"></a>

### [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) → [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) FUN_0087b4a0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 3件 [`0087a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md) [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) [`0087b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md#insn-0087b470) · [`0087b494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md#insn-0087b494) · [`0087b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md#insn-0087b4b8)
- 新版 `0087b4c8`（命令位置の公開資料なし） · `0087b4ec`（命令位置の公開資料なし） · `0087b510`（命令位置の公開資料なし）

~~~diff
- 0087b470 ["INT_ADD", "register:40f0:8", ["const:87b470:8", "const:4:8"]]
- 0087b470 ["CALL", null, ["callee:00c5aad0:8"]]
+ 0087b4c8 ["INT_ADD", "register:40f0:8", ["const:87b4c8:8", "const:4:8"]]
+ 0087b4c8 ["CALL", null, ["callee:00c5aad0:8"]]
- 0087b470 bytes 647d0f94
+ 0087b4c8 bytes 827d0f94
- 0087b494 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b494 ["INT_ADD", "register:40f0:8", ["const:87b494:8", "const:4:8"]]
- 0087b494 ["CALLIND", null, ["register:0:8"]]
+ 0087b4ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b4ec ["INT_ADD", "register:40f0:8", ["const:87b4ec:8", "const:4:8"]]
+ 0087b4ec ["CALLIND", null, ["register:0:8"]]
- 0087b494 bytes 00013fd6
+ 0087b4ec bytes 00013fd6
- 0087b4b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b4b8 ["INT_ADD", "register:40f0:8", ["const:87b4b8:8", "const:4:8"]]
- 0087b4b8 ["CALLIND", null, ["register:0:8"]]
+ 0087b510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b510 ["INT_ADD", "register:40f0:8", ["const:87b510:8", "const:4:8"]]
+ 0087b510 ["CALLIND", null, ["register:0:8"]]
- 0087b4b8 bytes 00013fd6
+ 0087b510 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011fc2506783a05d14e308aca4ee7cdb"></a>

### [`0087b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b778.md) → [`0087b7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b7d0.md) FUN_0087b7d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0087a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b778.md#insn-0087b7b4)
- 新版 `0087b80c`（命令位置の公開資料なし）

~~~diff
- 0087b7b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b7b4 ["INT_ADD", "register:40f0:8", ["const:87b7b4:8", "const:4:8"]]
- 0087b7b4 ["CALLIND", null, ["register:0:8"]]
+ 0087b80c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b80c ["INT_ADD", "register:40f0:8", ["const:87b80c:8", "const:4:8"]]
+ 0087b80c ["CALLIND", null, ["register:0:8"]]
- 0087b7b4 bytes 00013fd6
+ 0087b80c bytes 00013fd6
~~~


<a id="compare-d5bc5f90b8233db4e414aa7ee43732e4"></a>

### [`0087b7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b7c8.md) → [`0087b820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b820.md) FUN_0087b820

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087b7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b7c8.md#insn-0087b7e4)
- 新版 `0087b83c`（命令位置の公開資料なし）

~~~diff
- 0087b7e4 ["INT_ADD", "register:40f0:8", ["const:87b7e4:8", "const:4:8"]]
- 0087b7e4 ["CALL", null, ["callee:00459db4:8"]]
+ 0087b83c ["INT_ADD", "register:40f0:8", ["const:87b83c:8", "const:4:8"]]
+ 0087b83c ["CALL", null, ["callee:00459db4:8"]]
- 0087b7e4 bytes 6479ef97
+ 0087b83c bytes 5e79ef97
~~~


<a id="compare-76cebc4b3ecf6fa1d668868df365fa34"></a>

### [`0087bb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bb40.md) → [`0087bb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bb98.md) FUN_0087bb98

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bb40.md#insn-0087bb80)
- 新版 `0087bbd8`（命令位置の公開資料なし）

~~~diff
- 0087bb80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bb80 ["INT_ADD", "register:40f0:8", ["const:87bb80:8", "const:4:8"]]
- 0087bb80 ["CALLIND", null, ["register:0:8"]]
+ 0087bbd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bbd8 ["INT_ADD", "register:40f0:8", ["const:87bbd8:8", "const:4:8"]]
+ 0087bbd8 ["CALLIND", null, ["register:0:8"]]
- 0087bb80 bytes 00013fd6
+ 0087bbd8 bytes 00013fd6
~~~


