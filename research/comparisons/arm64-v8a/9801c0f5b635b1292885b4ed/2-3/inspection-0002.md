# v16.0.1 → v16.0.2 · 要調査の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-1904f95ae189fe37e03c0ad50240a0ff"></a>

### [`0046138c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/0046138c.md) → [`004613cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004613cc.md) FUN_004613cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004613d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/0046138c.md#insn-004613d4) · [`004613e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/0046138c.md#insn-004613e4) · [`00461414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/0046138c.md#insn-00461414)
- 新版 `00461414`（命令位置の公開資料なし） · `00461424`（命令位置の公開資料なし） · `00461454`（命令位置の公開資料なし）

~~~diff
- 004613d4 ["INT_ADD", "register:40f0:8", ["const:4613d4:8", "const:4:8"]]
- 004613d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461414 ["INT_ADD", "register:40f0:8", ["const:461414:8", "const:4:8"]]
+ 00461414 ["CALL", null, ["callee:00c57f80:8"]]
- 004613d4 bytes b7da1f94
+ 00461414 bytes dbda1f94
- 004613e4 ["INT_ADD", "register:40f0:8", ["const:4613e4:8", "const:4:8"]]
- 004613e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461424 ["INT_ADD", "register:40f0:8", ["const:461424:8", "const:4:8"]]
+ 00461424 ["CALL", null, ["callee:00c57f80:8"]]
- 004613e4 bytes b3da1f94
+ 00461424 bytes d7da1f94
- 00461414 ["INT_ADD", "register:40f0:8", ["const:461414:8", "const:4:8"]]
- 00461414 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461454 ["INT_ADD", "register:40f0:8", ["const:461454:8", "const:4:8"]]
+ 00461454 ["CALL", null, ["callee:00c57f80:8"]]
- 00461414 bytes a7da1f94
+ 00461454 bytes cbda1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc11400dfe4b804245151fc3ce080f8f"></a>

### [`00461444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461444.md) → [`00461484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461484.md) FUN_00461484

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046147c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461444.md#insn-0046147c)
- 新版 `004614bc`（命令位置の公開資料なし）

~~~diff
- 0046147c ["INT_ADD", "register:40f0:8", ["const:46147c:8", "const:4:8"]]
- 0046147c ["CALL", null, ["callee:00461ac0:8"]]
+ 004614bc ["INT_ADD", "register:40f0:8", ["const:4614bc:8", "const:4:8"]]
+ 004614bc ["CALL", null, ["callee:00461ac0:8"]]
- 0046147c bytes 81010094
+ 004614bc bytes 81010094
~~~


<a id="compare-ac8303055b6301277a328555dbd95d1a"></a>

### [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) → [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) FUN_004614f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 6件 [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) · 呼出先 6件 [`00461620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461620.md) [`004616a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md) [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004614fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md#insn-004614fc) · [`0046153c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md#insn-0046153c) · [`004615a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md#insn-004615a0)
- 新版 `0046153c`（命令位置の公開資料なし） · `0046157c`（命令位置の公開資料なし） · `004615e0`（命令位置の公開資料なし）

~~~diff
- 004614fc ["INT_ADD", "register:40f0:8", ["const:4614fc:8", "const:4:8"]]
- 004614fc ["CALL", null, ["callee:00c57f60:8"]]
+ 0046153c ["INT_ADD", "register:40f0:8", ["const:46153c:8", "const:4:8"]]
+ 0046153c ["CALL", null, ["callee:00c57f60:8"]]
- 004614fc bytes 65da1f94
+ 0046153c bytes 89da1f94
- 0046153c ["INT_ADD", "register:40f0:8", ["const:46153c:8", "const:4:8"]]
- 0046153c ["CALL", null, ["callee:00461710:8"]]
+ 0046157c ["INT_ADD", "register:40f0:8", ["const:46157c:8", "const:4:8"]]
+ 0046157c ["CALL", null, ["callee:00461710:8"]]
- 0046153c bytes 65000094
+ 0046157c bytes 65000094
- 004615a0 ["INT_ADD", "register:40f0:8", ["const:4615a0:8", "const:4:8"]]
- 004615a0 ["CALL", null, ["callee:004616a0:8"]]
+ 004615e0 ["INT_ADD", "register:40f0:8", ["const:4615e0:8", "const:4:8"]]
+ 004615e0 ["CALL", null, ["callee:004616a0:8"]]
- 004615a0 bytes 30000094
+ 004615e0 bytes 30000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a1c54bb1022f84e265e5cca378ddb0"></a>

### [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) → [`00461620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461620.md) FUN_00461620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) · 呼出先 2件 [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md#insn-00461634)
- 新版 `00461674`（命令位置の公開資料なし）

~~~diff
- 00461634 ["INT_ADD", "register:40f0:8", ["const:461634:8", "const:4:8"]]
- 00461634 ["CALL", null, ["callee:00461ac0:8"]]
+ 00461674 ["INT_ADD", "register:40f0:8", ["const:461674:8", "const:4:8"]]
+ 00461674 ["CALL", null, ["callee:00461ac0:8"]]
- 00461634 bytes 13010094
+ 00461674 bytes 13010094
~~~


<a id="compare-2281501b5f4a4315abec053109a41090"></a>

### [`00461674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461674.md) → [`004616b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616b4.md) FUN_004616b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004616b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461674.md#insn-004616b4)
- 新版 `004616f4`（命令位置の公開資料なし）

~~~diff
- 004616b4 ["INT_ADD", "register:40f0:8", ["const:4616b4:8", "const:4:8"]]
- 004616b4 ["CALL", null, ["callee:00461ac0:8"]]
+ 004616f4 ["INT_ADD", "register:40f0:8", ["const:4616f4:8", "const:4:8"]]
+ 004616f4 ["CALL", null, ["callee:00461ac0:8"]]
- 004616b4 bytes f3000094
+ 004616f4 bytes f3000094
~~~


<a id="compare-88c36c297ce22b51fe2e43e9e3cd7994"></a>

### [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) → [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md) FUN_00461710

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) [`009c0f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0f00.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md)
- 新版 呼出元 4件 [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461e08.md) [`009c0f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009c0/009c0f54.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md#insn-00461708) · [`00461734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md#insn-00461734) · [`00461760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md#insn-00461760)
- 新版 `00461748`（命令位置の公開資料なし） · `00461774`（命令位置の公開資料なし） · `004617a0`（命令位置の公開資料なし）

~~~diff
- 00461708 ["INT_ADD", "register:40f0:8", ["const:461708:8", "const:4:8"]]
- 00461708 ["CALL", null, ["callee:0043bb60:8"]]
+ 00461748 ["INT_ADD", "register:40f0:8", ["const:461748:8", "const:4:8"]]
+ 00461748 ["CALL", null, ["callee:0043bb60:8"]]
- 00461708 bytes 0669ff97
+ 00461748 bytes 0669ff97
- 00461734 ["INT_ADD", "register:40f0:8", ["const:461734:8", "const:4:8"]]
- 00461734 ["CALL", null, ["callee:0043bb60:8"]]
+ 00461774 ["INT_ADD", "register:40f0:8", ["const:461774:8", "const:4:8"]]
+ 00461774 ["CALL", null, ["callee:0043bb60:8"]]
- 00461734 bytes fb68ff97
+ 00461774 bytes fb68ff97
- 00461760 ["INT_ADD", "register:40f0:8", ["const:461760:8", "const:4:8"]]
- 00461760 ["CALL", null, ["callee:0043bb60:8"]]
+ 004617a0 ["INT_ADD", "register:40f0:8", ["const:4617a0:8", "const:4:8"]]
+ 004617a0 ["CALL", null, ["callee:0043bb60:8"]]
- 00461760 bytes f068ff97
+ 004617a0 bytes f068ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c173fc439a86359d886a97b1012c6d5a"></a>

### [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) → [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) FUN_00461858

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00461990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461990.md) [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004619d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004619d0.md) [`00461a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md#insn-00461874) · [`00461900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md#insn-00461900) · [`00461950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md#insn-00461950)
- 新版 `004618b4`（命令位置の公開資料なし） · `00461940`（命令位置の公開資料なし） · `00461990`（命令位置の公開資料なし）

~~~diff
- 00461874 ["INT_ADD", "register:40f0:8", ["const:461874:8", "const:4:8"]]
- 00461874 ["CALL", null, ["callee:00c57f60:8"]]
+ 004618b4 ["INT_ADD", "register:40f0:8", ["const:4618b4:8", "const:4:8"]]
+ 004618b4 ["CALL", null, ["callee:00c57f60:8"]]
- 00461874 bytes 87d91f94
+ 004618b4 bytes abd91f94
- 00461900 ["INT_ADD", "register:40f0:8", ["const:461900:8", "const:4:8"]]
- 00461900 ["CALL", null, ["callee:0043bb60:8"]]
+ 00461940 ["INT_ADD", "register:40f0:8", ["const:461940:8", "const:4:8"]]
+ 00461940 ["CALL", null, ["callee:0043bb60:8"]]
- 00461900 bytes 8868ff97
+ 00461940 bytes 8868ff97
- 00461950 ["INT_ADD", "register:40f0:8", ["const:461950:8", "const:4:8"]]
- 00461950 ["CALL", null, ["callee:00461a58:8"]]
+ 00461990 ["INT_ADD", "register:40f0:8", ["const:461990:8", "const:4:8"]]
+ 00461990 ["CALL", null, ["callee:00461a58:8"]]
- 00461950 bytes 32000094
+ 00461990 bytes 32000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bda521cb55cd1e85397479a3cba658df"></a>

### [`00461990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461990.md) → [`004619d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004619d0.md) FUN_004619d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004619f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461990.md#insn-004619f4)
- 新版 `00461a34`（命令位置の公開資料なし）

~~~diff
- 004619f4 ["INT_ADD", "register:40f0:8", ["const:4619f4:8", "const:4:8"]]
- 004619f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461a34 ["INT_ADD", "register:40f0:8", ["const:461a34:8", "const:4:8"]]
+ 00461a34 ["CALL", null, ["callee:00c57f80:8"]]
- 004619f4 bytes 2fd91f94
+ 00461a34 bytes 53d91f94
~~~


<a id="compare-e31795fee6c7f0a8aaee990be825dc00"></a>

### [`00461a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a2c.md) → [`00461a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a6c.md) FUN_00461a6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009bf268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf268.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a2c.md#insn-00461a6c)
- 新版 `00461aac`（命令位置の公開資料なし）

~~~diff
- 00461a6c ["INT_ADD", "register:40f0:8", ["const:461a6c:8", "const:4:8"]]
- 00461a6c ["CALL", null, ["callee:00c57f80:8"]]
+ 00461aac ["INT_ADD", "register:40f0:8", ["const:461aac:8", "const:4:8"]]
+ 00461aac ["CALL", null, ["callee:00c57f80:8"]]
- 00461a6c bytes 11d91f94
+ 00461aac bytes 35d91f94
~~~


<a id="compare-09f09d774c30c372a4c875a6b2b5d4e0"></a>

### [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) → [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) FUN_00461ac0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) [`00461318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461318.md) [`00461444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461444.md) [`004615e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004615e0.md) [`00461674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461674.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 11件 [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) [`00461358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461358.md) [`00461484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461484.md) [`00461620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461620.md) [`004616b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616b4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md#insn-00461ac8) · [`00461ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md#insn-00461ad8) · [`00461b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md#insn-00461b08)
- 新版 `00461b08`（命令位置の公開資料なし） · `00461b18`（命令位置の公開資料なし） · `00461b48`（命令位置の公開資料なし）

~~~diff
- 00461ac8 ["INT_ADD", "register:40f0:8", ["const:461ac8:8", "const:4:8"]]
- 00461ac8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461b08 ["INT_ADD", "register:40f0:8", ["const:461b08:8", "const:4:8"]]
+ 00461b08 ["CALL", null, ["callee:00c57f80:8"]]
- 00461ac8 bytes fad81f94
+ 00461b08 bytes 1ed91f94
- 00461ad8 ["INT_ADD", "register:40f0:8", ["const:461ad8:8", "const:4:8"]]
- 00461ad8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461b18 ["INT_ADD", "register:40f0:8", ["const:461b18:8", "const:4:8"]]
+ 00461b18 ["CALL", null, ["callee:00c57f80:8"]]
- 00461ad8 bytes f6d81f94
+ 00461b18 bytes 1ad91f94
- 00461b08 ["INT_ADD", "register:40f0:8", ["const:461b08:8", "const:4:8"]]
- 00461b08 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461b48 ["INT_ADD", "register:40f0:8", ["const:461b48:8", "const:4:8"]]
+ 00461b48 ["CALL", null, ["callee:00c57f80:8"]]
- 00461b08 bytes ead81f94
+ 00461b48 bytes 0ed91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a40bc8289f4e757738c0ca02cb2a11a"></a>

### [`00461b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md) → [`00461b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461b78.md) FUN_00461b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00461a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md#insn-00461bdc) · [`00461c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md#insn-00461c3c) · [`00461cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md#insn-00461cb8)
- 新版 `00461c1c`（命令位置の公開資料なし） · `00461c7c`（命令位置の公開資料なし） · `00461cf8`（命令位置の公開資料なし）

~~~diff
- 00461bdc ["INT_ADD", "register:40f0:8", ["const:461bdc:8", "const:4:8"]]
- 00461bdc ["CALL", null, ["callee:00c57f60:8"]]
+ 00461c1c ["INT_ADD", "register:40f0:8", ["const:461c1c:8", "const:4:8"]]
+ 00461c1c ["CALL", null, ["callee:00c57f60:8"]]
- 00461bdc bytes add81f94
+ 00461c1c bytes d1d81f94
- 00461c3c ["INT_ADD", "register:40f0:8", ["const:461c3c:8", "const:4:8"]]
- 00461c3c ["CALL", null, ["callee:0043bb60:8"]]
+ 00461c7c ["INT_ADD", "register:40f0:8", ["const:461c7c:8", "const:4:8"]]
+ 00461c7c ["CALL", null, ["callee:0043bb60:8"]]
- 00461c3c bytes b967ff97
+ 00461c7c bytes b967ff97
- 00461cb8 ["INT_ADD", "register:40f0:8", ["const:461cb8:8", "const:4:8"]]
- 00461cb8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461cf8 ["INT_ADD", "register:40f0:8", ["const:461cf8:8", "const:4:8"]]
+ 00461cf8 ["CALL", null, ["callee:00c57f80:8"]]
- 00461cb8 bytes 7ed81f94
+ 00461cf8 bytes a2d81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28a4f5bd256f684f2cd3ca6d927dafdd"></a>

### [`00461d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461d60.md) → [`00461da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461da0.md) FUN_00461da0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461d60.md#insn-00461db0)
- 新版 `00461df0`（命令位置の公開資料なし）

~~~diff
- 00461db0 ["INT_ADD", "register:40f0:8", ["const:461db0:8", "const:4:8"]]
- 00461db0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00461df0 ["INT_ADD", "register:40f0:8", ["const:461df0:8", "const:4:8"]]
+ 00461df0 ["CALL", null, ["callee:00c57f80:8"]]
- 00461db0 bytes 40d81f94
+ 00461df0 bytes 64d81f94
~~~


<a id="compare-79655678bd765cc0e21c886342b91562"></a>

### [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) → [`00461e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461e08.md) FUN_00461e08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004616a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md) [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md) [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00461e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md#insn-00461e4c) · [`00461e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md#insn-00461e70) · [`00461f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md#insn-00461f28)
- 新版 `00461e8c`（命令位置の公開資料なし） · `00461eb0`（命令位置の公開資料なし） · `00461f68`（命令位置の公開資料なし）

~~~diff
- 00461e4c ["INT_ADD", "register:40f0:8", ["const:461e4c:8", "const:4:8"]]
- 00461e4c ["CALL", null, ["callee:00c57f60:8"]]
+ 00461e8c ["INT_ADD", "register:40f0:8", ["const:461e8c:8", "const:4:8"]]
+ 00461e8c ["CALL", null, ["callee:00c57f60:8"]]
- 00461e4c bytes 11d81f94
+ 00461e8c bytes 35d81f94
- 00461e70 ["INT_ADD", "register:40f0:8", ["const:461e70:8", "const:4:8"]]
- 00461e70 ["CALL", null, ["callee:00461710:8"]]
+ 00461eb0 ["INT_ADD", "register:40f0:8", ["const:461eb0:8", "const:4:8"]]
+ 00461eb0 ["CALL", null, ["callee:00461710:8"]]
- 00461e70 bytes 18feff97
+ 00461eb0 bytes 18feff97
- 00461f28 ["INT_ADD", "register:40f0:8", ["const:461f28:8", "const:4:8"]]
- 00461f28 ["CALL", null, ["callee:00461ac0:8"]]
+ 00461f68 ["INT_ADD", "register:40f0:8", ["const:461f68:8", "const:4:8"]]
+ 00461f68 ["CALL", null, ["callee:00461ac0:8"]]
- 00461f28 bytes d6feff97
+ 00461f68 bytes d6feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5058e13c1388ffa66281d5c1fb4b8d5"></a>

### [`00461fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461fd8.md) → [`00462018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462018.md) FUN_00462018

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461fd8.md#insn-00462000)
- 新版 `00462040`（命令位置の公開資料なし）

~~~diff
- 00462000 ["INT_ADD", "register:40f0:8", ["const:462000:8", "const:4:8"]]
- 00462000 ["CALL", null, ["callee:00461ac0:8"]]
+ 00462040 ["INT_ADD", "register:40f0:8", ["const:462040:8", "const:4:8"]]
+ 00462040 ["CALL", null, ["callee:00461ac0:8"]]
- 00462000 bytes a0feff97
+ 00462040 bytes a0feff97
~~~


<a id="compare-bd0ee70164c451a482d2ec2240163455"></a>

### [`00462204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462204.md) → [`00462244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462244.md) FUN_00462244

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00454884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462204.md#insn-00462240)
- 新版 `00462280`（命令位置の公開資料なし）

~~~diff
- 00462240 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462240 ["INT_ADD", "register:40f0:8", ["const:462240:8", "const:4:8"]]
- 00462240 ["CALLIND", null, ["register:0:8"]]
+ 00462280 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462280 ["INT_ADD", "register:40f0:8", ["const:462280:8", "const:4:8"]]
+ 00462280 ["CALLIND", null, ["register:0:8"]]
- 00462240 bytes 00013fd6
+ 00462280 bytes 00013fd6
~~~


<a id="compare-4b8e8bf5985c9f1ab8f2435c5ec5a0af"></a>

### [`00462254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462254.md) → [`00462294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462294.md) FUN_00462294

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004622a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462254.md#insn-004622a4) · [`004622d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462254.md#insn-004622d8) · [`004622ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462254.md#insn-004622ec)
- 新版 `004622e4`（命令位置の公開資料なし） · `00462318`（命令位置の公開資料なし） · `0046232c`（命令位置の公開資料なし）

~~~diff
- 004622a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004622a4 ["INT_ADD", "register:40f0:8", ["const:4622a4:8", "const:4:8"]]
- 004622a4 ["CALLIND", null, ["register:0:8"]]
+ 004622e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004622e4 ["INT_ADD", "register:40f0:8", ["const:4622e4:8", "const:4:8"]]
+ 004622e4 ["CALLIND", null, ["register:0:8"]]
- 004622a4 bytes 00013fd6
+ 004622e4 bytes 00013fd6
- 004622d8 ["INT_ADD", "register:40f0:8", ["const:4622d8:8", "const:4:8"]]
- 004622d8 ["CALL", null, ["callee:00461ac0:8"]]
+ 00462318 ["INT_ADD", "register:40f0:8", ["const:462318:8", "const:4:8"]]
+ 00462318 ["CALL", null, ["callee:00461ac0:8"]]
- 004622d8 bytes eafdff97
+ 00462318 bytes eafdff97
- 004622ec ["INT_ADD", "register:40f0:8", ["const:4622ec:8", "const:4:8"]]
- 004622ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0046232c ["INT_ADD", "register:40f0:8", ["const:46232c:8", "const:4:8"]]
+ 0046232c ["CALL", null, ["callee:00c57f80:8"]]
- 004622ec bytes f1d61f94
+ 0046232c bytes 15d71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df88b041de0ba6b09125c20efc88a43"></a>

### [`00462594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462594.md) → [`004625d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004625d4.md) FUN_004625d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00454d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004625d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462594.md#insn-004625d0)
- 新版 `00462610`（命令位置の公開資料なし）

~~~diff
- 004625d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004625d0 ["INT_ADD", "register:40f0:8", ["const:4625d0:8", "const:4:8"]]
- 004625d0 ["CALLIND", null, ["register:0:8"]]
+ 00462610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462610 ["INT_ADD", "register:40f0:8", ["const:462610:8", "const:4:8"]]
+ 00462610 ["CALLIND", null, ["register:0:8"]]
- 004625d0 bytes 00013fd6
+ 00462610 bytes 00013fd6
~~~


<a id="compare-fdbeb44ae471f9e2c7c7f8d5df9ac84e"></a>

### [`004625e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004625e4.md) → [`00462624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462624.md) FUN_00462624

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046261c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004625e4.md#insn-0046261c) · [`00462650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004625e4.md#insn-00462650) · [`00462654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004625e4.md#insn-00462654)
- 新版 `0046265c`（命令位置の公開資料なし） · `00462690`（命令位置の公開資料なし） · `00462694`（命令位置の公開資料なし）

~~~diff
- 0046261c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046261c ["INT_ADD", "register:40f0:8", ["const:46261c:8", "const:4:8"]]
- 0046261c ["CALLIND", null, ["register:0:8"]]
+ 0046265c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046265c ["INT_ADD", "register:40f0:8", ["const:46265c:8", "const:4:8"]]
+ 0046265c ["CALLIND", null, ["register:0:8"]]
- 0046261c bytes 00013fd6
+ 0046265c bytes 00013fd6
- 00462650 ["INT_ADD", "register:40f0:8", ["const:462650:8", "const:4:8"]]
- 00462650 ["CALL", null, ["callee:00459db4:8"]]
+ 00462690 ["INT_ADD", "register:40f0:8", ["const:462690:8", "const:4:8"]]
+ 00462690 ["CALL", null, ["callee:00459db4:8"]]
- 00462650 bytes c9ddff97
+ 00462690 bytes c9ddff97
- 00462654 ["INT_ADD", "register:40f0:8", ["const:462654:8", "const:4:8"]]
- 00462654 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00462694 ["INT_ADD", "register:40f0:8", ["const:462694:8", "const:4:8"]]
+ 00462694 ["CALL", null, ["callee:00c57fb0:8"]]
- 00462654 bytes 23d61f94
+ 00462694 bytes 47d61f94
~~~


<a id="compare-670177edcc077925891cee461a6e16d9"></a>

### [`00462854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462854.md) → [`00462894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462894.md) FUN_00462894

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00454d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462854.md#insn-00462890)
- 新版 `004628d0`（命令位置の公開資料なし）

~~~diff
- 00462890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462890 ["INT_ADD", "register:40f0:8", ["const:462890:8", "const:4:8"]]
- 00462890 ["CALLIND", null, ["register:0:8"]]
+ 004628d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004628d0 ["INT_ADD", "register:40f0:8", ["const:4628d0:8", "const:4:8"]]
+ 004628d0 ["CALLIND", null, ["register:0:8"]]
- 00462890 bytes 00013fd6
+ 004628d0 bytes 00013fd6
~~~


<a id="compare-49defa45772d39c8284cde8f74312f8f"></a>

### [`004628a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004628a4.md) → [`004628e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004628e4.md) FUN_004628e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004628dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004628a4.md#insn-004628dc) · [`00462910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004628a4.md#insn-00462910) · [`00462914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004628a4.md#insn-00462914)
- 新版 `0046291c`（命令位置の公開資料なし） · `00462950`（命令位置の公開資料なし） · `00462954`（命令位置の公開資料なし）

~~~diff
- 004628dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004628dc ["INT_ADD", "register:40f0:8", ["const:4628dc:8", "const:4:8"]]
- 004628dc ["CALLIND", null, ["register:0:8"]]
+ 0046291c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046291c ["INT_ADD", "register:40f0:8", ["const:46291c:8", "const:4:8"]]
+ 0046291c ["CALLIND", null, ["register:0:8"]]
- 004628dc bytes 00013fd6
+ 0046291c bytes 00013fd6
- 00462910 ["INT_ADD", "register:40f0:8", ["const:462910:8", "const:4:8"]]
- 00462910 ["CALL", null, ["callee:00459db4:8"]]
+ 00462950 ["INT_ADD", "register:40f0:8", ["const:462950:8", "const:4:8"]]
+ 00462950 ["CALL", null, ["callee:00459db4:8"]]
- 00462910 bytes 19ddff97
+ 00462950 bytes 19ddff97
- 00462914 ["INT_ADD", "register:40f0:8", ["const:462914:8", "const:4:8"]]
- 00462914 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00462954 ["INT_ADD", "register:40f0:8", ["const:462954:8", "const:4:8"]]
+ 00462954 ["CALL", null, ["callee:00c57fb0:8"]]
- 00462914 bytes 73d51f94
+ 00462954 bytes 97d51f94
~~~


<a id="compare-68f1066c1e10c06789f918bede9a78c9"></a>

### [`00462b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b14.md) → [`00462b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462b54.md) FUN_00462b54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00455338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b14.md#insn-00462b50)
- 新版 `00462b90`（命令位置の公開資料なし）

~~~diff
- 00462b50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462b50 ["INT_ADD", "register:40f0:8", ["const:462b50:8", "const:4:8"]]
- 00462b50 ["CALLIND", null, ["register:0:8"]]
+ 00462b90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462b90 ["INT_ADD", "register:40f0:8", ["const:462b90:8", "const:4:8"]]
+ 00462b90 ["CALLIND", null, ["register:0:8"]]
- 00462b50 bytes 00013fd6
+ 00462b90 bytes 00013fd6
~~~


<a id="compare-8f0e01d5b340a67365a4780446432fb2"></a>

### [`00462b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b64.md) → [`00462ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462ba4.md) FUN_00462ba4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b64.md#insn-00462bc0) · [`00462bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b64.md#insn-00462bec) · [`00462c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b64.md#insn-00462c18)
- 新版 `00462c00`（命令位置の公開資料なし） · `00462c2c`（命令位置の公開資料なし） · `00462c58`（命令位置の公開資料なし）

~~~diff
- 00462bc0 ["INT_ADD", "register:40f0:8", ["const:462bc0:8", "const:4:8"]]
- 00462bc0 ["CALL", null, ["callee:004410cc:8"]]
+ 00462c00 ["INT_ADD", "register:40f0:8", ["const:462c00:8", "const:4:8"]]
+ 00462c00 ["CALL", null, ["callee:004410cc:8"]]
- 00462bc0 bytes 3379ff97
+ 00462c00 bytes 3379ff97
- 00462bec ["INT_ADD", "register:40f0:8", ["const:462bec:8", "const:4:8"]]
- 00462bec ["CALL", null, ["callee:00c57f80:8"]]
+ 00462c2c ["INT_ADD", "register:40f0:8", ["const:462c2c:8", "const:4:8"]]
+ 00462c2c ["CALL", null, ["callee:00c57f80:8"]]
- 00462bec bytes b1d41f94
+ 00462c2c bytes d5d41f94
- 00462c18 ["INT_ADD", "register:40f0:8", ["const:462c18:8", "const:4:8"]]
- 00462c18 ["CALL", null, ["callee:004410cc:8"]]
+ 00462c58 ["INT_ADD", "register:40f0:8", ["const:462c58:8", "const:4:8"]]
+ 00462c58 ["CALL", null, ["callee:004410cc:8"]]
- 00462c18 bytes 1d79ff97
+ 00462c58 bytes 1d79ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f3b5d6474cacf13b80dc3aae30b71f"></a>

### [`00462f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462f90.md) → [`00462fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462fd0.md) FUN_00462fd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00455338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00462fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462f90.md#insn-00462fcc)
- 新版 `0046300c`（命令位置の公開資料なし）

~~~diff
- 00462fcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00462fcc ["INT_ADD", "register:40f0:8", ["const:462fcc:8", "const:4:8"]]
- 00462fcc ["CALLIND", null, ["register:0:8"]]
+ 0046300c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046300c ["INT_ADD", "register:40f0:8", ["const:46300c:8", "const:4:8"]]
+ 0046300c ["CALLIND", null, ["register:0:8"]]
- 00462fcc bytes 00013fd6
+ 0046300c bytes 00013fd6
~~~


<a id="compare-0e00419d213fae833c520081c246918a"></a>

### [`00462fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462fe0.md) → [`00463020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463020.md) FUN_00463020

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462fe0.md#insn-00463020) · [`00463054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462fe0.md#insn-00463054) · [`00463058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462fe0.md#insn-00463058)
- 新版 `00463060`（命令位置の公開資料なし） · `00463094`（命令位置の公開資料なし） · `00463098`（命令位置の公開資料なし）

~~~diff
- 00463020 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463020 ["INT_ADD", "register:40f0:8", ["const:463020:8", "const:4:8"]]
- 00463020 ["CALLIND", null, ["register:0:8"]]
+ 00463060 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463060 ["INT_ADD", "register:40f0:8", ["const:463060:8", "const:4:8"]]
+ 00463060 ["CALLIND", null, ["register:0:8"]]
- 00463020 bytes 00013fd6
+ 00463060 bytes 00013fd6
- 00463054 ["INT_ADD", "register:40f0:8", ["const:463054:8", "const:4:8"]]
- 00463054 ["CALL", null, ["callee:00459db4:8"]]
+ 00463094 ["INT_ADD", "register:40f0:8", ["const:463094:8", "const:4:8"]]
+ 00463094 ["CALL", null, ["callee:00459db4:8"]]
- 00463054 bytes 48dbff97
+ 00463094 bytes 48dbff97
- 00463058 ["INT_ADD", "register:40f0:8", ["const:463058:8", "const:4:8"]]
- 00463058 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00463098 ["INT_ADD", "register:40f0:8", ["const:463098:8", "const:4:8"]]
+ 00463098 ["CALL", null, ["callee:00c57fb0:8"]]
- 00463058 bytes a2d31f94
+ 00463098 bytes c6d31f94
~~~


<a id="compare-b63d5a182f485f377a1a2719e0b8860a"></a>

### [`00463258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463258.md) → [`00463298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463298.md) FUN_00463298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463258.md#insn-00463294)
- 新版 `004632d4`（命令位置の公開資料なし）

~~~diff
- 00463294 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463294 ["INT_ADD", "register:40f0:8", ["const:463294:8", "const:4:8"]]
- 00463294 ["CALLIND", null, ["register:0:8"]]
+ 004632d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004632d4 ["INT_ADD", "register:40f0:8", ["const:4632d4:8", "const:4:8"]]
+ 004632d4 ["CALLIND", null, ["register:0:8"]]
- 00463294 bytes 00013fd6
+ 004632d4 bytes 00013fd6
~~~


<a id="compare-2e42ddc0c78f801c518da614ac320ded"></a>

### [`00463740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463740.md) → [`00463780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463780.md) FUN_00463780

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463740.md#insn-0046377c)
- 新版 `004637bc`（命令位置の公開資料なし）

~~~diff
- 0046377c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046377c ["INT_ADD", "register:40f0:8", ["const:46377c:8", "const:4:8"]]
- 0046377c ["CALLIND", null, ["register:0:8"]]
+ 004637bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004637bc ["INT_ADD", "register:40f0:8", ["const:4637bc:8", "const:4:8"]]
+ 004637bc ["CALLIND", null, ["register:0:8"]]
- 0046377c bytes 00013fd6
+ 004637bc bytes 00013fd6
~~~


<a id="compare-c2c441923033ea4f9705c9bb95438c77"></a>

### [`00463790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463790.md) → [`004637d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004637d0.md) FUN_004637d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004637d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463790.md#insn-004637d4) · [`004637ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463790.md#insn-004637ec) · [`00463820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463790.md#insn-00463820)
- 新版 `00463814`（命令位置の公開資料なし） · `0046382c`（命令位置の公開資料なし） · `00463860`（命令位置の公開資料なし）

~~~diff
- 004637d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004637d4 ["INT_ADD", "register:40f0:8", ["const:4637d4:8", "const:4:8"]]
- 004637d4 ["CALLIND", null, ["register:0:8"]]
+ 00463814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463814 ["INT_ADD", "register:40f0:8", ["const:463814:8", "const:4:8"]]
+ 00463814 ["CALLIND", null, ["register:0:8"]]
- 004637d4 bytes 00013fd6
+ 00463814 bytes 00013fd6
- 004637ec ["INT_ADD", "register:40f0:8", ["const:4637ec:8", "const:4:8"]]
- 004637ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0046382c ["INT_ADD", "register:40f0:8", ["const:46382c:8", "const:4:8"]]
+ 0046382c ["CALL", null, ["callee:00c57f80:8"]]
- 004637ec bytes b1d11f94
+ 0046382c bytes d5d11f94
- 00463820 ["INT_ADD", "register:40f0:8", ["const:463820:8", "const:4:8"]]
- 00463820 ["CALL", null, ["callee:00459db4:8"]]
+ 00463860 ["INT_ADD", "register:40f0:8", ["const:463860:8", "const:4:8"]]
+ 00463860 ["CALL", null, ["callee:00459db4:8"]]
- 00463820 bytes 55d9ff97
+ 00463860 bytes 55d9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09fae72823de190465a20bc1d528a4fa"></a>

### [`00463a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463a58.md) → [`00463a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463a98.md) FUN_00463a98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00455d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463a58.md#insn-00463a94)
- 新版 `00463ad4`（命令位置の公開資料なし）

~~~diff
- 00463a94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463a94 ["INT_ADD", "register:40f0:8", ["const:463a94:8", "const:4:8"]]
- 00463a94 ["CALLIND", null, ["register:0:8"]]
+ 00463ad4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463ad4 ["INT_ADD", "register:40f0:8", ["const:463ad4:8", "const:4:8"]]
+ 00463ad4 ["CALLIND", null, ["register:0:8"]]
- 00463a94 bytes 00013fd6
+ 00463ad4 bytes 00013fd6
~~~


<a id="compare-5a17a7b10f23488d46742d46cfcb96f6"></a>

### [`00463aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463aa8.md) → [`00463ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463ae8.md) FUN_00463ae8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463aa8.md#insn-00463ae0) · [`00463b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463aa8.md#insn-00463b14) · [`00463b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463aa8.md#insn-00463b18)
- 新版 `00463b20`（命令位置の公開資料なし） · `00463b54`（命令位置の公開資料なし） · `00463b58`（命令位置の公開資料なし）

~~~diff
- 00463ae0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463ae0 ["INT_ADD", "register:40f0:8", ["const:463ae0:8", "const:4:8"]]
- 00463ae0 ["CALLIND", null, ["register:0:8"]]
+ 00463b20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463b20 ["INT_ADD", "register:40f0:8", ["const:463b20:8", "const:4:8"]]
+ 00463b20 ["CALLIND", null, ["register:0:8"]]
- 00463ae0 bytes 00013fd6
+ 00463b20 bytes 00013fd6
- 00463b14 ["INT_ADD", "register:40f0:8", ["const:463b14:8", "const:4:8"]]
- 00463b14 ["CALL", null, ["callee:00459db4:8"]]
+ 00463b54 ["INT_ADD", "register:40f0:8", ["const:463b54:8", "const:4:8"]]
+ 00463b54 ["CALL", null, ["callee:00459db4:8"]]
- 00463b14 bytes 98d8ff97
+ 00463b54 bytes 98d8ff97
- 00463b18 ["INT_ADD", "register:40f0:8", ["const:463b18:8", "const:4:8"]]
- 00463b18 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00463b58 ["INT_ADD", "register:40f0:8", ["const:463b58:8", "const:4:8"]]
+ 00463b58 ["CALL", null, ["callee:00c57fb0:8"]]
- 00463b18 bytes f2d01f94
+ 00463b58 bytes 16d11f94
~~~


<a id="compare-447ffbc1b3af5280edee5656154f8ed8"></a>

### [`00463d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d18.md) → [`00463d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463d58.md) FUN_00463d58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00455d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d18.md#insn-00463d54)
- 新版 `00463d94`（命令位置の公開資料なし）

~~~diff
- 00463d54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463d54 ["INT_ADD", "register:40f0:8", ["const:463d54:8", "const:4:8"]]
- 00463d54 ["CALLIND", null, ["register:0:8"]]
+ 00463d94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463d94 ["INT_ADD", "register:40f0:8", ["const:463d94:8", "const:4:8"]]
+ 00463d94 ["CALLIND", null, ["register:0:8"]]
- 00463d54 bytes 00013fd6
+ 00463d94 bytes 00013fd6
~~~


<a id="compare-516bf88d0794a5a91dcd7c6459c9a5a8"></a>

### [`00463d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d68.md) → [`00463da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463da8.md) FUN_00463da8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00463da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d68.md#insn-00463da0) · [`00463dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d68.md#insn-00463dd4) · [`00463dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463d68.md#insn-00463dd8)
- 新版 `00463de0`（命令位置の公開資料なし） · `00463e14`（命令位置の公開資料なし） · `00463e18`（命令位置の公開資料なし）

~~~diff
- 00463da0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463da0 ["INT_ADD", "register:40f0:8", ["const:463da0:8", "const:4:8"]]
- 00463da0 ["CALLIND", null, ["register:0:8"]]
+ 00463de0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463de0 ["INT_ADD", "register:40f0:8", ["const:463de0:8", "const:4:8"]]
+ 00463de0 ["CALLIND", null, ["register:0:8"]]
- 00463da0 bytes 00013fd6
+ 00463de0 bytes 00013fd6
- 00463dd4 ["INT_ADD", "register:40f0:8", ["const:463dd4:8", "const:4:8"]]
- 00463dd4 ["CALL", null, ["callee:00459db4:8"]]
+ 00463e14 ["INT_ADD", "register:40f0:8", ["const:463e14:8", "const:4:8"]]
+ 00463e14 ["CALL", null, ["callee:00459db4:8"]]
- 00463dd4 bytes e8d7ff97
+ 00463e14 bytes e8d7ff97
- 00463dd8 ["INT_ADD", "register:40f0:8", ["const:463dd8:8", "const:4:8"]]
- 00463dd8 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00463e18 ["INT_ADD", "register:40f0:8", ["const:463e18:8", "const:4:8"]]
+ 00463e18 ["CALL", null, ["callee:00c57fb0:8"]]
- 00463dd8 bytes 42d01f94
+ 00463e18 bytes 66d01f94
~~~


<a id="compare-044938f943a4e8e621ddc4b6ee517789"></a>

### [`00463fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463fd8.md) → [`00464018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464018.md) FUN_00464018

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463fd8.md#insn-00464014)
- 新版 `00464054`（命令位置の公開資料なし）

~~~diff
- 00464014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464014 ["INT_ADD", "register:40f0:8", ["const:464014:8", "const:4:8"]]
- 00464014 ["CALLIND", null, ["register:0:8"]]
+ 00464054 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464054 ["INT_ADD", "register:40f0:8", ["const:464054:8", "const:4:8"]]
+ 00464054 ["CALLIND", null, ["register:0:8"]]
- 00464014 bytes 00013fd6
+ 00464054 bytes 00013fd6
~~~


<a id="compare-25e9b3950de1f870ee81718985916391"></a>

### [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) → [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) FUN_004647dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) [`00464d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md) [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086dc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc64.md) [`0086dc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dc84.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 8件 [`00464068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464068.md) [`00464d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464d6c.md) [`0086d774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d774.md) [`0086dcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dcbc.md) [`0086dcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dcdc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004647fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md#insn-004647fc) · [`0046480c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md#insn-0046480c) · [`0046481c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md#insn-0046481c)
- 新版 `0046483c`（命令位置の公開資料なし） · `0046484c`（命令位置の公開資料なし） · `0046485c`（命令位置の公開資料なし）

~~~diff
- 004647fc ["INT_ADD", "register:40f0:8", ["const:4647fc:8", "const:4:8"]]
- 004647fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0046483c ["INT_ADD", "register:40f0:8", ["const:46483c:8", "const:4:8"]]
+ 0046483c ["CALL", null, ["callee:00c57f80:8"]]
- 004647fc bytes adcd1f94
+ 0046483c bytes d1cd1f94
- 0046480c ["INT_ADD", "register:40f0:8", ["const:46480c:8", "const:4:8"]]
- 0046480c ["CALL", null, ["callee:00c57f80:8"]]
+ 0046484c ["INT_ADD", "register:40f0:8", ["const:46484c:8", "const:4:8"]]
+ 0046484c ["CALL", null, ["callee:00c57f80:8"]]
- 0046480c bytes a9cd1f94
+ 0046484c bytes cdcd1f94
- 0046481c ["INT_ADD", "register:40f0:8", ["const:46481c:8", "const:4:8"]]
- 0046481c ["CALL", null, ["callee:00c57f80:8"]]
+ 0046485c ["INT_ADD", "register:40f0:8", ["const:46485c:8", "const:4:8"]]
+ 0046485c ["CALL", null, ["callee:00c57f80:8"]]
- 0046481c bytes a5cd1f94
+ 0046485c bytes c9cd1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60d2de615e0cbc6101577f33d539b8a9"></a>

### [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md) → [`004648b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004648b8.md) FUN_004648b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086dcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dcc0.md) [`0086dd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086dd50.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 4件 [`00464068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464068.md) [`0086d774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d774.md) [`0086dd18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dd18.md) [`0086dda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dda8.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004648b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md#insn-004648b0) · [`004648dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md#insn-004648dc) · [`00464908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md#insn-00464908)
- 新版 `004648f0`（命令位置の公開資料なし） · `0046491c`（命令位置の公開資料なし） · `00464948`（命令位置の公開資料なし）

~~~diff
- 004648b0 ["INT_ADD", "register:40f0:8", ["const:4648b0:8", "const:4:8"]]
- 004648b0 ["CALL", null, ["callee:0043bb60:8"]]
+ 004648f0 ["INT_ADD", "register:40f0:8", ["const:4648f0:8", "const:4:8"]]
+ 004648f0 ["CALL", null, ["callee:0043bb60:8"]]
- 004648b0 bytes 9c5cff97
+ 004648f0 bytes 9c5cff97
- 004648dc ["INT_ADD", "register:40f0:8", ["const:4648dc:8", "const:4:8"]]
- 004648dc ["CALL", null, ["callee:0043bb60:8"]]
+ 0046491c ["INT_ADD", "register:40f0:8", ["const:46491c:8", "const:4:8"]]
+ 0046491c ["CALL", null, ["callee:0043bb60:8"]]
- 004648dc bytes 915cff97
+ 0046491c bytes 915cff97
- 00464908 ["INT_ADD", "register:40f0:8", ["const:464908:8", "const:4:8"]]
- 00464908 ["CALL", null, ["callee:0043bb60:8"]]
+ 00464948 ["INT_ADD", "register:40f0:8", ["const:464948:8", "const:4:8"]]
+ 00464948 ["CALL", null, ["callee:0043bb60:8"]]
- 00464908 bytes 865cff97
+ 00464948 bytes 865cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0887b15306d6244b948ac4043626e0f0"></a>

### [`00464cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464cdc.md) → [`00464d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464d1c.md) FUN_00464d1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464cdc.md#insn-00464d18)
- 新版 `00464d58`（命令位置の公開資料なし）

~~~diff
- 00464d18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464d18 ["INT_ADD", "register:40f0:8", ["const:464d18:8", "const:4:8"]]
- 00464d18 ["CALLIND", null, ["register:0:8"]]
+ 00464d58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464d58 ["INT_ADD", "register:40f0:8", ["const:464d58:8", "const:4:8"]]
+ 00464d58 ["CALLIND", null, ["register:0:8"]]
- 00464d18 bytes 00013fd6
+ 00464d58 bytes 00013fd6
~~~


<a id="compare-31f596876390877fd0266a7e50fbd37f"></a>

### [`00464d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md) → [`00464d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464d6c.md) FUN_00464d6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00464d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md#insn-00464d70) · [`00464d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md#insn-00464d80) · [`00464db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464d2c.md#insn-00464db4)
- 新版 `00464db0`（命令位置の公開資料なし） · `00464dc0`（命令位置の公開資料なし） · `00464df4`（命令位置の公開資料なし）

~~~diff
- 00464d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464d70 ["INT_ADD", "register:40f0:8", ["const:464d70:8", "const:4:8"]]
- 00464d70 ["CALLIND", null, ["register:0:8"]]
+ 00464db0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464db0 ["INT_ADD", "register:40f0:8", ["const:464db0:8", "const:4:8"]]
+ 00464db0 ["CALLIND", null, ["register:0:8"]]
- 00464d70 bytes 00013fd6
+ 00464db0 bytes 00013fd6
- 00464d80 ["INT_ADD", "register:40f0:8", ["const:464d80:8", "const:4:8"]]
- 00464d80 ["CALL", null, ["callee:004647dc:8"]]
+ 00464dc0 ["INT_ADD", "register:40f0:8", ["const:464dc0:8", "const:4:8"]]
+ 00464dc0 ["CALL", null, ["callee:004647dc:8"]]
- 00464d80 bytes 87feff97
+ 00464dc0 bytes 87feff97
- 00464db4 ["INT_ADD", "register:40f0:8", ["const:464db4:8", "const:4:8"]]
- 00464db4 ["CALL", null, ["callee:00459db4:8"]]
+ 00464df4 ["INT_ADD", "register:40f0:8", ["const:464df4:8", "const:4:8"]]
+ 00464df4 ["CALL", null, ["callee:00459db4:8"]]
- 00464db4 bytes f0d3ff97
+ 00464df4 bytes f0d3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-776c6cbefc3e045464f08f3bb87e45dc"></a>

### [`00464fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464fe4.md) → [`00465024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465024.md) FUN_00465024

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00465020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464fe4.md#insn-00465020)
- 新版 `00465060`（命令位置の公開資料なし）

~~~diff
- 00465020 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465020 ["INT_ADD", "register:40f0:8", ["const:465020:8", "const:4:8"]]
- 00465020 ["CALLIND", null, ["register:0:8"]]
+ 00465060 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465060 ["INT_ADD", "register:40f0:8", ["const:465060:8", "const:4:8"]]
+ 00465060 ["CALLIND", null, ["register:0:8"]]
- 00465020 bytes 00013fd6
+ 00465060 bytes 00013fd6
~~~


<a id="compare-edb34413ea7cc5fae1535c0739b3f15f"></a>

### [`00465034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465034.md) → [`00465074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465074.md) FUN_00465074

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00465068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465034.md#insn-00465068) · [`00465098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465034.md#insn-00465098) · [`004650bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465034.md#insn-004650bc)
- 新版 `004650a8`（命令位置の公開資料なし） · `004650d8`（命令位置の公開資料なし） · `004650fc`（命令位置の公開資料なし）

~~~diff
- 00465068 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465068 ["INT_ADD", "register:40f0:8", ["const:465068:8", "const:4:8"]]
- 00465068 ["CALLIND", null, ["register:0:8"]]
+ 004650a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004650a8 ["INT_ADD", "register:40f0:8", ["const:4650a8:8", "const:4:8"]]
+ 004650a8 ["CALLIND", null, ["register:0:8"]]
- 00465068 bytes 00013fd6
+ 004650a8 bytes 00013fd6
- 00465098 ["INT_ADD", "register:40f0:8", ["const:465098:8", "const:4:8"]]
- 00465098 ["CALL", null, ["callee:00459db4:8"]]
+ 004650d8 ["INT_ADD", "register:40f0:8", ["const:4650d8:8", "const:4:8"]]
+ 004650d8 ["CALL", null, ["callee:00459db4:8"]]
- 00465098 bytes 37d3ff97
+ 004650d8 bytes 37d3ff97
- 004650bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004650bc ["INT_ADD", "register:40f0:8", ["const:4650bc:8", "const:4:8"]]
- 004650bc ["CALLIND", null, ["register:0:8"]]
+ 004650fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004650fc ["INT_ADD", "register:40f0:8", ["const:4650fc:8", "const:4:8"]]
+ 004650fc ["CALLIND", null, ["register:0:8"]]
- 004650bc bytes 00013fd6
+ 004650fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4279467d5fa61820c7e266ddbea4fae4"></a>

### [`00465874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465874.md) → [`004658b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004658b4.md) FUN_004658b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004658ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465874.md#insn-004658ac) · [`004658bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465874.md#insn-004658bc)
- 新版 `004658ec`（命令位置の公開資料なし） · `004658fc`（命令位置の公開資料なし）

~~~diff
- 004658ac ["INT_ADD", "register:40f0:8", ["const:4658ac:8", "const:4:8"]]
- 004658ac ["CALL", null, ["callee:00c57f80:8"]]
+ 004658ec ["INT_ADD", "register:40f0:8", ["const:4658ec:8", "const:4:8"]]
+ 004658ec ["CALL", null, ["callee:00c57f80:8"]]
- 004658ac bytes 81c91f94
+ 004658ec bytes a5c91f94
- 004658bc ["INT_ADD", "register:40f0:8", ["const:4658bc:8", "const:4:8"]]
- 004658bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004658fc ["INT_ADD", "register:40f0:8", ["const:4658fc:8", "const:4:8"]]
+ 004658fc ["CALL", null, ["callee:00c57f80:8"]]
- 004658bc bytes 7dc91f94
+ 004658fc bytes a1c91f94
~~~


<a id="compare-ace79b0a4d75d667db9b55df1246e3f0"></a>

### [`004658d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004658d8.md) → [`00465918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465918.md) FUN_00465918

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00465904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004658d8.md#insn-00465904) · [`0046591c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004658d8.md#insn-0046591c) · [`0046592c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004658d8.md#insn-0046592c)
- 新版 `00465944`（命令位置の公開資料なし） · `0046595c`（命令位置の公開資料なし） · `0046596c`（命令位置の公開資料なし）

~~~diff
- 00465904 ["INT_ADD", "register:40f0:8", ["const:465904:8", "const:4:8"]]
- 00465904 ["CALL", null, ["callee:00c57f80:8"]]
+ 00465944 ["INT_ADD", "register:40f0:8", ["const:465944:8", "const:4:8"]]
+ 00465944 ["CALL", null, ["callee:00c57f80:8"]]
- 00465904 bytes 6bc91f94
+ 00465944 bytes 8fc91f94
- 0046591c ["INT_ADD", "register:40f0:8", ["const:46591c:8", "const:4:8"]]
- 0046591c ["CALL", null, ["callee:00c57f80:8"]]
+ 0046595c ["INT_ADD", "register:40f0:8", ["const:46595c:8", "const:4:8"]]
+ 0046595c ["CALL", null, ["callee:00c57f80:8"]]
- 0046591c bytes 65c91f94
+ 0046595c bytes 89c91f94
- 0046592c ["INT_ADD", "register:40f0:8", ["const:46592c:8", "const:4:8"]]
- 0046592c ["CALL", null, ["callee:00c57f80:8"]]
+ 0046596c ["INT_ADD", "register:40f0:8", ["const:46596c:8", "const:4:8"]]
+ 0046596c ["CALL", null, ["callee:00c57f80:8"]]
- 0046592c bytes 61c91f94
+ 0046596c bytes 85c91f94
~~~


<a id="compare-836492e75891503f69ec044cdc60cdab"></a>

### [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md) → [`0046690c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/0046690c.md) FUN_0046690c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00465804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md) [`00465858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465858.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 2件 [`00465844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465844.md) [`00465898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465898.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00466904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md#insn-00466904) · [`00466930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md#insn-00466930) · [`0046695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md#insn-0046695c)
- 新版 `00466944`（命令位置の公開資料なし） · `00466970`（命令位置の公開資料なし） · `0046699c`（命令位置の公開資料なし）

~~~diff
- 00466904 ["INT_ADD", "register:40f0:8", ["const:466904:8", "const:4:8"]]
- 00466904 ["CALL", null, ["callee:0043bb60:8"]]
+ 00466944 ["INT_ADD", "register:40f0:8", ["const:466944:8", "const:4:8"]]
+ 00466944 ["CALL", null, ["callee:0043bb60:8"]]
- 00466904 bytes 8754ff97
+ 00466944 bytes 8754ff97
- 00466930 ["INT_ADD", "register:40f0:8", ["const:466930:8", "const:4:8"]]
- 00466930 ["CALL", null, ["callee:0043bb60:8"]]
+ 00466970 ["INT_ADD", "register:40f0:8", ["const:466970:8", "const:4:8"]]
+ 00466970 ["CALL", null, ["callee:0043bb60:8"]]
- 00466930 bytes 7c54ff97
+ 00466970 bytes 7c54ff97
- 0046695c ["INT_ADD", "register:40f0:8", ["const:46695c:8", "const:4:8"]]
- 0046695c ["CALL", null, ["callee:0043bb60:8"]]
+ 0046699c ["INT_ADD", "register:40f0:8", ["const:46699c:8", "const:4:8"]]
+ 0046699c ["CALL", null, ["callee:0043bb60:8"]]
- 0046695c bytes 7154ff97
+ 0046699c bytes 7154ff97
~~~


<a id="compare-f8580f437bfa58a2be1ca7bbd027ab65"></a>

### [`00466d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d0c.md) → [`00466d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466d4c.md) FUN_00466d4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0045870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00466d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d0c.md#insn-00466d48)
- 新版 `00466d88`（命令位置の公開資料なし）

~~~diff
- 00466d48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466d48 ["INT_ADD", "register:40f0:8", ["const:466d48:8", "const:4:8"]]
- 00466d48 ["CALLIND", null, ["register:0:8"]]
+ 00466d88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466d88 ["INT_ADD", "register:40f0:8", ["const:466d88:8", "const:4:8"]]
+ 00466d88 ["CALLIND", null, ["register:0:8"]]
- 00466d48 bytes 00013fd6
+ 00466d88 bytes 00013fd6
~~~


<a id="compare-34d6e725b44f92cdd06a37d49f2e12bb"></a>

### [`00466d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d5c.md) → [`00466d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466d9c.md) FUN_00466d9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00466d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d5c.md#insn-00466d9c) · [`00466dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d5c.md#insn-00466dbc) · [`00466de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d5c.md#insn-00466de4)
- 新版 `00466ddc`（命令位置の公開資料なし） · `00466dfc`（命令位置の公開資料なし） · `00466e24`（命令位置の公開資料なし）

~~~diff
- 00466d9c ["COPY", "register:0:8", ["register:4048:8"]]
- 00466d9c ["INT_ADD", "register:40f0:8", ["const:466d9c:8", "const:4:8"]]
- 00466d9c ["CALLIND", null, ["register:0:8"]]
+ 00466ddc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00466ddc ["INT_ADD", "register:40f0:8", ["const:466ddc:8", "const:4:8"]]
+ 00466ddc ["CALLIND", null, ["register:0:8"]]
- 00466d9c bytes 20013fd6
+ 00466ddc bytes 20013fd6
- 00466dbc ["INT_ADD", "register:40f0:8", ["const:466dbc:8", "const:4:8"]]
- 00466dbc ["CALL", null, ["callee:00c53d70:8"]]
+ 00466dfc ["INT_ADD", "register:40f0:8", ["const:466dfc:8", "const:4:8"]]
+ 00466dfc ["CALL", null, ["callee:00c53d70:8"]]
- 00466dbc bytes c5b31f94
+ 00466dfc bytes ddb31f94
- 00466de4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466de4 ["INT_ADD", "register:40f0:8", ["const:466de4:8", "const:4:8"]]
- 00466de4 ["CALLIND", null, ["register:0:8"]]
+ 00466e24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466e24 ["INT_ADD", "register:40f0:8", ["const:466e24:8", "const:4:8"]]
+ 00466e24 ["CALLIND", null, ["register:0:8"]]
- 00466de4 bytes 00013fd6
+ 00466e24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec14caa8f4004d94b95c336668f726d"></a>

### [`00467604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467604.md) → [`00467644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467644.md) FUN_00467644

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 2件 [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md)
- 新版 呼出元 1件 [`005fc3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fc/005fc3e0.md) · 呼出先 2件 [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`0046d9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046761c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467604.md#insn-0046761c) · [`00467628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467604.md#insn-00467628)
- 新版 `0046765c`（命令位置の公開資料なし） · `00467668`（命令位置の公開資料なし）

~~~diff
- 0046761c ["INT_ADD", "register:40f0:8", ["const:46761c:8", "const:4:8"]]
- 0046761c ["CALL", null, ["callee:0046d9ec:8"]]
+ 0046765c ["INT_ADD", "register:40f0:8", ["const:46765c:8", "const:4:8"]]
+ 0046765c ["CALL", null, ["callee:0046d9ec:8"]]
- 0046761c bytes e4180094
+ 0046765c bytes e4180094
- 00467628 ["INT_ADD", "register:40f0:8", ["const:467628:8", "const:4:8"]]
- 00467628 ["CALL", null, ["callee:0046d9b4:8"]]
+ 00467668 ["INT_ADD", "register:40f0:8", ["const:467668:8", "const:4:8"]]
+ 00467668 ["CALL", null, ["callee:0046d9b4:8"]]
- 00467628 bytes d3180094
+ 00467668 bytes d3180094
~~~


<a id="compare-84a557ef2187685e0fa5155131d3eb34"></a>

### [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) → [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) FUN_00467758

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) [`00a47634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md) · 呼出先 2件 [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md)
- 新版 呼出元 3件 [`0046de64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046de64.md) [`00a47158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md) [`00a47688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md) · 呼出先 2件 [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`0046d9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md#insn-00467730) · [`0046773c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md#insn-0046773c)
- 新版 `00467770`（命令位置の公開資料なし） · `0046777c`（命令位置の公開資料なし）

~~~diff
- 00467730 ["INT_ADD", "register:40f0:8", ["const:467730:8", "const:4:8"]]
- 00467730 ["CALL", null, ["callee:0046d9ec:8"]]
+ 00467770 ["INT_ADD", "register:40f0:8", ["const:467770:8", "const:4:8"]]
+ 00467770 ["CALL", null, ["callee:0046d9ec:8"]]
- 00467730 bytes 9f180094
+ 00467770 bytes 9f180094
- 0046773c ["INT_ADD", "register:40f0:8", ["const:46773c:8", "const:4:8"]]
- 0046773c ["CALL", null, ["callee:0046d9b4:8"]]
+ 0046777c ["INT_ADD", "register:40f0:8", ["const:46777c:8", "const:4:8"]]
+ 0046777c ["CALL", null, ["callee:0046d9b4:8"]]
- 0046773c bytes 8e180094
+ 0046777c bytes 8e180094
~~~


<a id="compare-c54873c2aa5a878172941144373eeaf5"></a>

### [`0046791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md) → [`0046795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/0046795c.md) FUN_0046795c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md#insn-00467938) · [`00467958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md#insn-00467958)
- 新版 `00467978`（命令位置の公開資料なし） · `00467998`（命令位置の公開資料なし）

~~~diff
- 00467938 ["INT_ADD", "register:40f0:8", ["const:467938:8", "const:4:8"]]
- 00467938 ["CALL", null, ["callee:00c53da0:8"]]
+ 00467978 ["INT_ADD", "register:40f0:8", ["const:467978:8", "const:4:8"]]
+ 00467978 ["CALL", null, ["callee:00c53da0:8"]]
- 00467938 bytes f2b01f94
+ 00467978 bytes 0ab11f94
- 00467958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00467958 ["INT_ADD", "register:40f0:8", ["const:467958:8", "const:4:8"]]
- 00467958 ["CALLIND", null, ["register:0:8"]]
+ 00467998 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00467998 ["INT_ADD", "register:40f0:8", ["const:467998:8", "const:4:8"]]
+ 00467998 ["CALLIND", null, ["register:0:8"]]
- 00467958 bytes 00013fd6
+ 00467998 bytes 00013fd6
~~~


<a id="compare-8c6354cf7c47a3d7b9de82f8c227fd94"></a>

### [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) → [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) FUN_00467ba0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 69件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005f17ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f17ac.md) [`005f5230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5230.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) · 呼出先 2件 [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 69件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005f17ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f1/005f17ec.md) [`005f5270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f5270.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`0062a27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062a/0062a27c.md) · 呼出先 2件 [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md#insn-00467bc0) · [`00467be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md#insn-00467be4)
- 新版 `00467c00`（命令位置の公開資料なし） · `00467c24`（命令位置の公開資料なし）

~~~diff
- 00467bc0 ["INT_ADD", "register:40f0:8", ["const:467bc0:8", "const:4:8"]]
- 00467bc0 ["CALL", null, ["callee:0055cf8c:8"]]
+ 00467c00 ["INT_ADD", "register:40f0:8", ["const:467c00:8", "const:4:8"]]
+ 00467c00 ["CALL", null, ["callee:0055cf8c:8"]]
- 00467bc0 bytes e3d40394
+ 00467c00 bytes e3d40394
- 00467be4 ["INT_ADD", "register:40f0:8", ["const:467be4:8", "const:4:8"]]
- 00467be4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00467c24 ["INT_ADD", "register:40f0:8", ["const:467c24:8", "const:4:8"]]
+ 00467c24 ["CALL", null, ["callee:00c57fb0:8"]]
- 00467be4 bytes bfc01f94
+ 00467c24 bytes e3c01f94
~~~


<a id="compare-d9cac01638233919e4fae095e6c36aa3"></a>

### [`00467d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d44.md) → [`00467d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467d84.md) FUN_00467d84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md)
- 新版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 1件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d44.md#insn-00467d74)
- 新版 `00467db4`（命令位置の公開資料なし）

~~~diff
- 00467d74 ["INT_ADD", "register:40f0:8", ["const:467d74:8", "const:4:8"]]
- 00467d74 ["CALL", null, ["callee:0058fa88:8"]]
+ 00467db4 ["INT_ADD", "register:40f0:8", ["const:467db4:8", "const:4:8"]]
+ 00467db4 ["CALL", null, ["callee:0058fa88:8"]]
- 00467d74 bytes 359f0494
+ 00467db4 bytes 359f0494
~~~


<a id="compare-b96382ff8443e631a02be4850fa5422f"></a>

### [`00467d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md) → [`00467dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dcc.md) FUN_00467dcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00672904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672904.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ce4c.md)
- 新版 呼出元 2件 [`00672944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672944.md) [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 2件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0055ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055ce8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md#insn-00467da0)
- 新版 `00467de0`（命令位置の公開資料なし）

~~~diff
- 00467da0 ["INT_ADD", "register:40f0:8", ["const:467da0:8", "const:4:8"]]
- 00467da0 ["CALL", null, ["callee:00467dfc:8"]]
+ 00467de0 ["INT_ADD", "register:40f0:8", ["const:467de0:8", "const:4:8"]]
+ 00467de0 ["CALL", null, ["callee:00467dfc:8"]]
- 00467da0 bytes 07000094
+ 00467de0 bytes 07000094
~~~


<a id="compare-329782690c30d4116f82ed8a41b649aa"></a>

### [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) → [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) FUN_00467dfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d8c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md) · 呼出先 7件 [`00555458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555458.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf38.md) [`0055cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf8c.md) [`0055cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cfb8.md)
- 新版 呼出元 13件 [`004679ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004679ac.md) [`00467b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b3c.md) [`00467dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dcc.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00467eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467eec.md) · 呼出先 7件 [`00555498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555498.md) [`0055a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a63c.md) [`0055cf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf78.md) [`0055cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cfcc.md) [`0055cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cff8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md#insn-00467de0) · [`00467e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md#insn-00467e08) · [`00467e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md#insn-00467e14)
- 新版 `00467e20`（命令位置の公開資料なし） · `00467e48`（命令位置の公開資料なし） · `00467e54`（命令位置の公開資料なし）

~~~diff
- 00467de0 ["INT_ADD", "register:40f0:8", ["const:467de0:8", "const:4:8"]]
- 00467de0 ["CALL", null, ["callee:0055cf78:8"]]
+ 00467e20 ["INT_ADD", "register:40f0:8", ["const:467e20:8", "const:4:8"]]
+ 00467e20 ["CALL", null, ["callee:0055cf78:8"]]
- 00467de0 bytes 56d40394
+ 00467e20 bytes 56d40394
- 00467e08 ["INT_ADD", "register:40f0:8", ["const:467e08:8", "const:4:8"]]
- 00467e08 ["CALL", null, ["callee:0055cfcc:8"]]
+ 00467e48 ["INT_ADD", "register:40f0:8", ["const:467e48:8", "const:4:8"]]
+ 00467e48 ["CALL", null, ["callee:0055cfcc:8"]]
- 00467e08 bytes 61d40394
+ 00467e48 bytes 61d40394
- 00467e14 ["INT_ADD", "register:40f0:8", ["const:467e14:8", "const:4:8"]]
- 00467e14 ["CALL", null, ["callee:0055cff8:8"]]
+ 00467e54 ["INT_ADD", "register:40f0:8", ["const:467e54:8", "const:4:8"]]
+ 00467e54 ["CALL", null, ["callee:0055cff8:8"]]
- 00467e14 bytes 69d40394
+ 00467e54 bytes 69d40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c4e60107e840ce229cc045e8380e54"></a>

### [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) → [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) FUN_00467f94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 77件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md)
- 新版 呼出元 77件 [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) [`005ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005ed2b4.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ef5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ef/005ef5ec.md) · 呼出先 2件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0055a57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a57c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md#insn-00467f84)
- 新版 `00467fc4`（命令位置の公開資料なし）

~~~diff
- 00467f84 ["INT_ADD", "register:40f0:8", ["const:467f84:8", "const:4:8"]]
- 00467f84 ["CALL", null, ["callee:00467dfc:8"]]
+ 00467fc4 ["INT_ADD", "register:40f0:8", ["const:467fc4:8", "const:4:8"]]
+ 00467fc4 ["CALL", null, ["callee:00467dfc:8"]]
- 00467f84 bytes 8effff97
+ 00467fc4 bytes 8effff97
~~~


<a id="compare-9e234fdba503fa90764a2b8929437573"></a>

### [`00467fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467fac.md) → [`00467fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467fec.md) FUN_00467fec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md)
- 新版 呼出元 2件 [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0055a57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a57c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00467fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467fac.md#insn-00467fd4)
- 新版 `00468014`（命令位置の公開資料なし）

~~~diff
- 00467fd4 ["INT_ADD", "register:40f0:8", ["const:467fd4:8", "const:4:8"]]
- 00467fd4 ["CALL", null, ["callee:00467dfc:8"]]
+ 00468014 ["INT_ADD", "register:40f0:8", ["const:468014:8", "const:4:8"]]
+ 00468014 ["CALL", null, ["callee:00467dfc:8"]]
- 00467fd4 bytes 7affff97
+ 00468014 bytes 7affff97
~~~


<a id="compare-19d5b6d4b870c8fcdce59a00eb661b83"></a>

### [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) → [`0046803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/0046803c.md) FUN_0046803c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`00679800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00679/00679800.md) [`006ad414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006ad414.md) [`006b66e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b66e8.md) · 呼出先 8件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 7件 [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`00679840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00679/00679840.md) [`006ad46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006ad46c.md) [`006b6740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b6/006b6740.md) · 呼出先 8件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) [`0055a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a478.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md#insn-00468054) · [`00468070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md#insn-00468070) · [`00468120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md#insn-00468120)
- 新版 `00468094`（命令位置の公開資料なし） · `004680b0`（命令位置の公開資料なし） · `00468160`（命令位置の公開資料なし）

~~~diff
- 00468054 ["INT_ADD", "register:40f0:8", ["const:468054:8", "const:4:8"]]
- 00468054 ["CALL", null, ["callee:00c57f60:8"]]
+ 00468094 ["INT_ADD", "register:40f0:8", ["const:468094:8", "const:4:8"]]
+ 00468094 ["CALL", null, ["callee:00c57f60:8"]]
- 00468054 bytes 8fbf1f94
+ 00468094 bytes b3bf1f94
- 00468070 ["INT_ADD", "register:40f0:8", ["const:468070:8", "const:4:8"]]
- 00468070 ["CALL", null, ["callee:00c58160:8"]]
+ 004680b0 ["INT_ADD", "register:40f0:8", ["const:4680b0:8", "const:4:8"]]
+ 004680b0 ["CALL", null, ["callee:00c58160:8"]]
- 00468070 bytes 08c01f94
+ 004680b0 bytes 2cc01f94
- 00468120 ["INT_ADD", "register:40f0:8", ["const:468120:8", "const:4:8"]]
- 00468120 ["CALL", null, ["callee:00467dfc:8"]]
+ 00468160 ["INT_ADD", "register:40f0:8", ["const:468160:8", "const:4:8"]]
+ 00468160 ["CALL", null, ["callee:00467dfc:8"]]
- 00468120 bytes 27ffff97
+ 00468160 bytes 27ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9b637740fceeca3eda0b9258ddcb78"></a>

### [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) → [`00468540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468540.md) FUN_00468540

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00468200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468200.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004685e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md#insn-004685e8) · [`00468618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md#insn-00468618) · [`0046862c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md#insn-0046862c)
- 新版 `00468628`（命令位置の公開資料なし） · `00468658`（命令位置の公開資料なし） · `0046866c`（命令位置の公開資料なし）

~~~diff
- 004685e8 ["INT_ADD", "register:40f0:8", ["const:4685e8:8", "const:4:8"]]
- 004685e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00468628 ["INT_ADD", "register:40f0:8", ["const:468628:8", "const:4:8"]]
+ 00468628 ["CALL", null, ["callee:00c57f60:8"]]
- 004685e8 bytes 2abe1f94
+ 00468628 bytes 4ebe1f94
- 00468618 ["INT_ADD", "register:40f0:8", ["const:468618:8", "const:4:8"]]
- 00468618 ["CALL", null, ["callee:00c580d0:8"]]
+ 00468658 ["INT_ADD", "register:40f0:8", ["const:468658:8", "const:4:8"]]
+ 00468658 ["CALL", null, ["callee:00c580d0:8"]]
- 00468618 bytes 7abe1f94
+ 00468658 bytes 9ebe1f94
- 0046862c ["INT_ADD", "register:40f0:8", ["const:46862c:8", "const:4:8"]]
- 0046862c ["CALL", null, ["callee:00c57f80:8"]]
+ 0046866c ["INT_ADD", "register:40f0:8", ["const:46866c:8", "const:4:8"]]
+ 0046866c ["CALL", null, ["callee:00c57f80:8"]]
- 0046862c bytes 21be1f94
+ 0046866c bytes 45be1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f668e820078b05dbb5c3956cc9446e8"></a>

### [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) → [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) FUN_00468844

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 48件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`005fb0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb0f8.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`00635104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635104.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab50.md)
- 新版 呼出元 48件 [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`005fb138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fb/005fb138.md) [`00612324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00612/00612324.md) [`00635144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635144.md) · 呼出先 4件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md) [`0048ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md#insn-0046883c) · [`00468854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md#insn-00468854) · [`00468864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md#insn-00468864)
- 新版 `0046887c`（命令位置の公開資料なし） · `00468894`（命令位置の公開資料なし） · `004688a4`（命令位置の公開資料なし）

~~~diff
- 0046883c ["INT_ADD", "register:40f0:8", ["const:46883c:8", "const:4:8"]]
- 0046883c ["CALL", null, ["callee:0048ab70:8"]]
+ 0046887c ["INT_ADD", "register:40f0:8", ["const:46887c:8", "const:4:8"]]
+ 0046887c ["CALL", null, ["callee:0048ab70:8"]]
- 0046883c bytes bd880094
+ 0046887c bytes bd880094
- 00468854 ["INT_ADD", "register:40f0:8", ["const:468854:8", "const:4:8"]]
- 00468854 ["CALL", null, ["callee:0048ab78:8"]]
+ 00468894 ["INT_ADD", "register:40f0:8", ["const:468894:8", "const:4:8"]]
+ 00468894 ["CALL", null, ["callee:0048ab78:8"]]
- 00468854 bytes b9880094
+ 00468894 bytes b9880094
- 00468864 ["INT_ADD", "register:40f0:8", ["const:468864:8", "const:4:8"]]
- 00468864 ["CALL", null, ["callee:0048ab70:8"]]
+ 004688a4 ["INT_ADD", "register:40f0:8", ["const:4688a4:8", "const:4:8"]]
+ 004688a4 ["CALL", null, ["callee:0048ab70:8"]]
- 00468864 bytes b3880094
+ 004688a4 bytes b3880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51458c6126f913cd8af73c8189574a55"></a>

### [`004688b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004688b8.md) → [`004688f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/004688f8.md) FUN_004688f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`006acaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006acaec.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 5件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)
- 新版 呼出元 2件 [`006acb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ac/006acb44.md) [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 5件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md) [`0048abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048abc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004688f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004688b8.md#insn-004688f0) · [`004688fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004688b8.md#insn-004688fc) · [`00468918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004688b8.md#insn-00468918)
- 新版 `00468930`（命令位置の公開資料なし） · `0046893c`（命令位置の公開資料なし） · `00468958`（命令位置の公開資料なし）

~~~diff
- 004688f0 ["INT_ADD", "register:40f0:8", ["const:4688f0:8", "const:4:8"]]
- 004688f0 ["CALL", null, ["callee:0048ab80:8"]]
+ 00468930 ["INT_ADD", "register:40f0:8", ["const:468930:8", "const:4:8"]]
+ 00468930 ["CALL", null, ["callee:0048ab80:8"]]
- 004688f0 bytes 94880094
+ 00468930 bytes 94880094
- 004688fc ["INT_ADD", "register:40f0:8", ["const:4688fc:8", "const:4:8"]]
- 004688fc ["CALL", null, ["callee:0048ab88:8"]]
+ 0046893c ["INT_ADD", "register:40f0:8", ["const:46893c:8", "const:4:8"]]
+ 0046893c ["CALL", null, ["callee:0048ab88:8"]]
- 004688fc bytes 93880094
+ 0046893c bytes 93880094
- 00468918 ["INT_ADD", "register:40f0:8", ["const:468918:8", "const:4:8"]]
- 00468918 ["CALL", null, ["callee:0048ab70:8"]]
+ 00468958 ["INT_ADD", "register:40f0:8", ["const:468958:8", "const:4:8"]]
+ 00468958 ["CALL", null, ["callee:0048ab70:8"]]
- 00468918 bytes 86880094
+ 00468958 bytes 86880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-396ef19a63ab6bb74887bb9fbf27bcc2"></a>

### [`004689c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md) → [`00468a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468a00.md) FUN_00468a00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)
- 新版 呼出元 1件 [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) · 呼出先 4件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md) [`0048abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048abc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md#insn-00468a0c) · [`00468a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md#insn-00468a24) · [`00468a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md#insn-00468a34)
- 新版 `00468a4c`（命令位置の公開資料なし） · `00468a64`（命令位置の公開資料なし） · `00468a74`（命令位置の公開資料なし）

~~~diff
- 00468a0c ["INT_ADD", "register:40f0:8", ["const:468a0c:8", "const:4:8"]]
- 00468a0c ["CALL", null, ["callee:0048ab70:8"]]
+ 00468a4c ["INT_ADD", "register:40f0:8", ["const:468a4c:8", "const:4:8"]]
+ 00468a4c ["CALL", null, ["callee:0048ab70:8"]]
- 00468a0c bytes 49880094
+ 00468a4c bytes 49880094
- 00468a24 ["INT_ADD", "register:40f0:8", ["const:468a24:8", "const:4:8"]]
- 00468a24 ["CALL", null, ["callee:0048ab78:8"]]
+ 00468a64 ["INT_ADD", "register:40f0:8", ["const:468a64:8", "const:4:8"]]
+ 00468a64 ["CALL", null, ["callee:0048ab78:8"]]
- 00468a24 bytes 45880094
+ 00468a64 bytes 45880094
- 00468a34 ["INT_ADD", "register:40f0:8", ["const:468a34:8", "const:4:8"]]
- 00468a34 ["CALL", null, ["callee:0048ab70:8"]]
+ 00468a74 ["INT_ADD", "register:40f0:8", ["const:468a74:8", "const:4:8"]]
+ 00468a74 ["CALL", null, ["callee:0048ab70:8"]]
- 00468a34 bytes 3f880094
+ 00468a74 bytes 3f880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5442ad545fb71f367902f450df696ec"></a>

### [`00468ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468ad4.md) → [`00468b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468b14.md) FUN_00468b14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 4件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048ab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab80.md)
- 新版 呼出元 1件 [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) · 呼出先 4件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md) [`0048abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048abc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468ad4.md#insn-00468b1c) · [`00468b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468ad4.md#insn-00468b2c) · [`00468b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468ad4.md#insn-00468b54)
- 新版 `00468b5c`（命令位置の公開資料なし） · `00468b6c`（命令位置の公開資料なし） · `00468b94`（命令位置の公開資料なし）

~~~diff
- 00468b1c ["INT_ADD", "register:40f0:8", ["const:468b1c:8", "const:4:8"]]
- 00468b1c ["CALL", null, ["callee:0048ab70:8"]]
+ 00468b5c ["INT_ADD", "register:40f0:8", ["const:468b5c:8", "const:4:8"]]
+ 00468b5c ["CALL", null, ["callee:0048ab70:8"]]
- 00468b1c bytes 05880094
+ 00468b5c bytes 05880094
- 00468b2c ["INT_ADD", "register:40f0:8", ["const:468b2c:8", "const:4:8"]]
- 00468b2c ["CALL", null, ["callee:0048ab70:8"]]
+ 00468b6c ["INT_ADD", "register:40f0:8", ["const:468b6c:8", "const:4:8"]]
+ 00468b6c ["CALL", null, ["callee:0048ab70:8"]]
- 00468b2c bytes 01880094
+ 00468b6c bytes 01880094
- 00468b54 ["INT_ADD", "register:40f0:8", ["const:468b54:8", "const:4:8"]]
- 00468b54 ["CALL", null, ["callee:0048ab78:8"]]
+ 00468b94 ["INT_ADD", "register:40f0:8", ["const:468b94:8", "const:4:8"]]
+ 00468b94 ["CALL", null, ["callee:0048ab78:8"]]
- 00468b54 bytes f9870094
+ 00468b94 bytes f9870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3366cb9b6e00d77e45e59286d26fc82f"></a>

### [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) → [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) FUN_00468c1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 2件 [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 37件 [`0046e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e5c8.md) [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) · 呼出先 2件 [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md#insn-00468c38) · [`00468c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md#insn-00468c5c)
- 新版 `00468c78`（命令位置の公開資料なし） · `00468c9c`（命令位置の公開資料なし）

~~~diff
- 00468c38 ["INT_ADD", "register:40f0:8", ["const:468c38:8", "const:4:8"]]
- 00468c38 ["CALL", null, ["callee:0055cf8c:8"]]
+ 00468c78 ["INT_ADD", "register:40f0:8", ["const:468c78:8", "const:4:8"]]
+ 00468c78 ["CALL", null, ["callee:0055cf8c:8"]]
- 00468c38 bytes c5d00394
+ 00468c78 bytes c5d00394
- 00468c5c ["INT_ADD", "register:40f0:8", ["const:468c5c:8", "const:4:8"]]
- 00468c5c ["CALL", null, ["callee:00c57fb0:8"]]
+ 00468c9c ["INT_ADD", "register:40f0:8", ["const:468c9c:8", "const:4:8"]]
+ 00468c9c ["CALL", null, ["callee:00c57fb0:8"]]
- 00468c5c bytes a1bc1f94
+ 00468c9c bytes c5bc1f94
~~~


<a id="compare-1def548ce389632c4373a857a320d733"></a>

### [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) → [`00468ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca8.md) FUN_00468ca8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`008c9da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c9da8.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 3件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)
- 新版 呼出元 7件 [`0060eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060eb90.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007fb288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb288.md) [`008c9dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c9/008c9dfc.md) [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 3件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md#insn-00468c98) · [`00468ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md#insn-00468ca4) · [`00468cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md#insn-00468cb0)
- 新版 `00468cd8`（命令位置の公開資料なし） · `00468ce4`（命令位置の公開資料なし） · `00468cf0`（命令位置の公開資料なし）

~~~diff
- 00468c98 ["INT_ADD", "register:40f0:8", ["const:468c98:8", "const:4:8"]]
- 00468c98 ["CALL", null, ["callee:0048ab70:8"]]
+ 00468cd8 ["INT_ADD", "register:40f0:8", ["const:468cd8:8", "const:4:8"]]
+ 00468cd8 ["CALL", null, ["callee:0048ab70:8"]]
- 00468c98 bytes a6870094
+ 00468cd8 bytes a6870094
- 00468ca4 ["INT_ADD", "register:40f0:8", ["const:468ca4:8", "const:4:8"]]
- 00468ca4 ["CALL", null, ["callee:0048ab78:8"]]
+ 00468ce4 ["INT_ADD", "register:40f0:8", ["const:468ce4:8", "const:4:8"]]
+ 00468ce4 ["CALL", null, ["callee:0048ab78:8"]]
- 00468ca4 bytes a5870094
+ 00468ce4 bytes a5870094
- 00468cb0 ["INT_ADD", "register:40f0:8", ["const:468cb0:8", "const:4:8"]]
- 00468cb0 ["CALL", null, ["callee:0048ab70:8"]]
+ 00468cf0 ["INT_ADD", "register:40f0:8", ["const:468cf0:8", "const:4:8"]]
+ 00468cf0 ["CALL", null, ["callee:0048ab70:8"]]
- 00468cb0 bytes a0870094
+ 00468cf0 bytes a0870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243cbdc8631dc829dec8f8d4c3b5b275"></a>

### [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) → [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) FUN_00468d48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 13件 [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) · 呼出先 5件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 13件 [`00468ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca8.md) [`00468f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468f8c.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469184.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) · 呼出先 5件 [`0048acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048acd0.md) [`0055a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a5e8.md) [`0055a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a63c.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md#insn-00468d5c) · [`00468da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md#insn-00468da4) · [`00468dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md#insn-00468dd4)
- 新版 `00468d9c`（命令位置の公開資料なし） · `00468de4`（命令位置の公開資料なし） · `00468e14`（命令位置の公開資料なし）

~~~diff
- 00468d5c ["INT_ADD", "register:40f0:8", ["const:468d5c:8", "const:4:8"]]
- 00468d5c ["CALL", null, ["callee:0055a5e8:8"]]
+ 00468d9c ["INT_ADD", "register:40f0:8", ["const:468d9c:8", "const:4:8"]]
+ 00468d9c ["CALL", null, ["callee:0055a5e8:8"]]
- 00468d5c bytes 13c60394
+ 00468d9c bytes 13c60394
- 00468da4 ["INT_ADD", "register:40f0:8", ["const:468da4:8", "const:4:8"]]
- 00468da4 ["CALL", null, ["callee:0055cf8c:8"]]
+ 00468de4 ["INT_ADD", "register:40f0:8", ["const:468de4:8", "const:4:8"]]
+ 00468de4 ["CALL", null, ["callee:0055cf8c:8"]]
- 00468da4 bytes 6ad00394
+ 00468de4 bytes 6ad00394
- 00468dd4 ["INT_ADD", "register:40f0:8", ["const:468dd4:8", "const:4:8"]]
- 00468dd4 ["CALL", null, ["callee:0048acd0:8"]]
+ 00468e14 ["INT_ADD", "register:40f0:8", ["const:468e14:8", "const:4:8"]]
+ 00468e14 ["CALL", null, ["callee:0048acd0:8"]]
- 00468dd4 bytes af870094
+ 00468e14 bytes af870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5c07af0fe63de1cbd55d1a3e03b8f5"></a>

### [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) → [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) FUN_00468e60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) [`00469ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046a978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md) [`0046af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md) · 呼出先 5件 [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 7件 [`004690a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/004690a8.md) [`00469d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469d0c.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0046a9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a9b8.md) [`0046af60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af60.md) · 呼出先 5件 [`0048af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048af18.md) [`0055a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a5e8.md) [`0055a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a63c.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md#insn-00468e84) · [`00468ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md#insn-00468ecc) · [`00468efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md#insn-00468efc)
- 新版 `00468ec4`（命令位置の公開資料なし） · `00468f0c`（命令位置の公開資料なし） · `00468f3c`（命令位置の公開資料なし）

~~~diff
- 00468e84 ["INT_ADD", "register:40f0:8", ["const:468e84:8", "const:4:8"]]
- 00468e84 ["CALL", null, ["callee:0055a5e8:8"]]
+ 00468ec4 ["INT_ADD", "register:40f0:8", ["const:468ec4:8", "const:4:8"]]
+ 00468ec4 ["CALL", null, ["callee:0055a5e8:8"]]
- 00468e84 bytes c9c50394
+ 00468ec4 bytes c9c50394
- 00468ecc ["INT_ADD", "register:40f0:8", ["const:468ecc:8", "const:4:8"]]
- 00468ecc ["CALL", null, ["callee:0055cf8c:8"]]
+ 00468f0c ["INT_ADD", "register:40f0:8", ["const:468f0c:8", "const:4:8"]]
+ 00468f0c ["CALL", null, ["callee:0055cf8c:8"]]
- 00468ecc bytes 20d00394
+ 00468f0c bytes 20d00394
- 00468efc ["INT_ADD", "register:40f0:8", ["const:468efc:8", "const:4:8"]]
- 00468efc ["CALL", null, ["callee:0048af18:8"]]
+ 00468f3c ["INT_ADD", "register:40f0:8", ["const:468f3c:8", "const:4:8"]]
+ 00468f3c ["CALL", null, ["callee:0048af18:8"]]
- 00468efc bytes f7870094
+ 00468f3c bytes f7870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24543c94ddcb82013b0b1773cd8ad9ce"></a>

### [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) → [`00468f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468f8c.md) FUN_00468f8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006dde88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dd/006dde88.md) [`006f8a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md) [`007475f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007475f0.md) [`0077ad2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077ad2c.md) [`008e73d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e7/008e73d0.md) · 呼出先 1件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md)
- 新版 呼出元 6件 [`006ddee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006ddee0.md) [`006f8a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md) [`00747648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747648.md) [`0077ad84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077a/0077ad84.md) [`008e7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7424.md) · 呼出先 1件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md#insn-00468f78)
- 新版 `00468fb8`（命令位置の公開資料なし）

~~~diff
- 00468f78 ["INT_ADD", "register:40f0:8", ["const:468f78:8", "const:4:8"]]
- 00468f78 ["CALL", null, ["callee:00468d48:8"]]
+ 00468fb8 ["INT_ADD", "register:40f0:8", ["const:468fb8:8", "const:4:8"]]
+ 00468fb8 ["CALL", null, ["callee:00468d48:8"]]
- 00468f78 bytes 64ffff97
+ 00468fb8 bytes 64ffff97
~~~


<a id="compare-7b41bd0f044ffdefb81e37a44a1dcb72"></a>

### [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) → [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) FUN_00468fc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 111件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`005f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f6c54.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 111件 [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`005f6c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f6/005f6c94.md) · 呼出先 2件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00468fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md#insn-00468fc4) · [`00468fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md#insn-00468fd4) · [`00468fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md#insn-00468fe4)
- 新版 `00469004`（命令位置の公開資料なし） · `00469014`（命令位置の公開資料なし） · `00469024`（命令位置の公開資料なし）

~~~diff
- 00468fc4 ["INT_ADD", "register:40f0:8", ["const:468fc4:8", "const:4:8"]]
- 00468fc4 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469004 ["INT_ADD", "register:40f0:8", ["const:469004:8", "const:4:8"]]
+ 00469004 ["CALL", null, ["callee:00489f8c:8"]]
- 00468fc4 bytes e2830094
+ 00469004 bytes e2830094
- 00468fd4 ["INT_ADD", "register:40f0:8", ["const:468fd4:8", "const:4:8"]]
- 00468fd4 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469014 ["INT_ADD", "register:40f0:8", ["const:469014:8", "const:4:8"]]
+ 00469014 ["CALL", null, ["callee:00489f8c:8"]]
- 00468fd4 bytes de830094
+ 00469014 bytes de830094
- 00468fe4 ["INT_ADD", "register:40f0:8", ["const:468fe4:8", "const:4:8"]]
- 00468fe4 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469024 ["INT_ADD", "register:40f0:8", ["const:469024:8", "const:4:8"]]
+ 00469024 ["CALL", null, ["callee:00489f8c:8"]]
- 00468fe4 bytes da830094
+ 00469024 bytes da830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58fbe50c6c0ac83273c8dafbe8c124a"></a>

### [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) → [`004690a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/004690a8.md) FUN_004690a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) [`009f6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 4件 [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`0082d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d800.md) [`009f6c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6c68.md) · 呼出先 2件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004690a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md#insn-004690a0) · [`004690b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md#insn-004690b4) · [`004690c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md#insn-004690c8)
- 新版 `004690e0`（命令位置の公開資料なし） · `004690f4`（命令位置の公開資料なし） · `00469108`（命令位置の公開資料なし）

~~~diff
- 004690a0 ["INT_ADD", "register:40f0:8", ["const:4690a0:8", "const:4:8"]]
- 004690a0 ["CALL", null, ["callee:00489f8c:8"]]
+ 004690e0 ["INT_ADD", "register:40f0:8", ["const:4690e0:8", "const:4:8"]]
+ 004690e0 ["CALL", null, ["callee:00489f8c:8"]]
- 004690a0 bytes ab830094
+ 004690e0 bytes ab830094
- 004690b4 ["INT_ADD", "register:40f0:8", ["const:4690b4:8", "const:4:8"]]
- 004690b4 ["CALL", null, ["callee:00489f8c:8"]]
+ 004690f4 ["INT_ADD", "register:40f0:8", ["const:4690f4:8", "const:4:8"]]
+ 004690f4 ["CALL", null, ["callee:00489f8c:8"]]
- 004690b4 bytes a6830094
+ 004690f4 bytes a6830094
- 004690c8 ["INT_ADD", "register:40f0:8", ["const:4690c8:8", "const:4:8"]]
- 004690c8 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469108 ["INT_ADD", "register:40f0:8", ["const:469108:8", "const:4:8"]]
+ 00469108 ["CALL", null, ["callee:00489f8c:8"]]
- 004690c8 bytes a1830094
+ 00469108 bytes a1830094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-144324dee938b897c806170cfff7a24c"></a>

### [`00469144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md) → [`00469184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469184.md) FUN_00469184

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`0062b4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b4d8.md) [`006c43e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c43e4.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 9件 [`0062b518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062b/0062b518.md) [`006c443c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c443c.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004691c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md#insn-004691c0) · [`004691d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md#insn-004691d0) · [`00469200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md#insn-00469200)
- 新版 `00469200`（命令位置の公開資料なし） · `00469210`（命令位置の公開資料なし） · `00469240`（命令位置の公開資料なし）

~~~diff
- 004691c0 ["INT_ADD", "register:40f0:8", ["const:4691c0:8", "const:4:8"]]
- 004691c0 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469200 ["INT_ADD", "register:40f0:8", ["const:469200:8", "const:4:8"]]
+ 00469200 ["CALL", null, ["callee:00489f8c:8"]]
- 004691c0 bytes 63830094
+ 00469200 bytes 63830094
- 004691d0 ["INT_ADD", "register:40f0:8", ["const:4691d0:8", "const:4:8"]]
- 004691d0 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469210 ["INT_ADD", "register:40f0:8", ["const:469210:8", "const:4:8"]]
+ 00469210 ["CALL", null, ["callee:00489f8c:8"]]
- 004691d0 bytes 5f830094
+ 00469210 bytes 5f830094
- 00469200 ["INT_ADD", "register:40f0:8", ["const:469200:8", "const:4:8"]]
- 00469200 ["CALL", null, ["callee:00468d48:8"]]
+ 00469240 ["INT_ADD", "register:40f0:8", ["const:469240:8", "const:4:8"]]
+ 00469240 ["CALL", null, ["callee:00468d48:8"]]
- 00469200 bytes c2feff97
+ 00469240 bytes c2feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e0c5c58479b123e806ccddd21ec39c"></a>

### [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) → [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) FUN_0046969c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 37件 [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 37件 [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`0060eb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060eb90.md) [`00613ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md) [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) · 呼出先 2件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004696bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md#insn-004696bc) · [`004696cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md#insn-004696cc) · [`004696e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md#insn-004696e0)
- 新版 `004696fc`（命令位置の公開資料なし） · `0046970c`（命令位置の公開資料なし） · `00469720`（命令位置の公開資料なし）

~~~diff
- 004696bc ["INT_ADD", "register:40f0:8", ["const:4696bc:8", "const:4:8"]]
- 004696bc ["CALL", null, ["callee:00489f8c:8"]]
+ 004696fc ["INT_ADD", "register:40f0:8", ["const:4696fc:8", "const:4:8"]]
+ 004696fc ["CALL", null, ["callee:00489f8c:8"]]
- 004696bc bytes 24820094
+ 004696fc bytes 24820094
- 004696cc ["INT_ADD", "register:40f0:8", ["const:4696cc:8", "const:4:8"]]
- 004696cc ["CALL", null, ["callee:00489f8c:8"]]
+ 0046970c ["INT_ADD", "register:40f0:8", ["const:46970c:8", "const:4:8"]]
+ 0046970c ["CALL", null, ["callee:00489f8c:8"]]
- 004696cc bytes 20820094
+ 0046970c bytes 20820094
- 004696e0 ["INT_ADD", "register:40f0:8", ["const:4696e0:8", "const:4:8"]]
- 004696e0 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469720 ["INT_ADD", "register:40f0:8", ["const:469720:8", "const:4:8"]]
+ 00469720 ["CALL", null, ["callee:00489f8c:8"]]
- 004696e0 bytes 1b820094
+ 00469720 bytes 1b820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f71d5bb83026593fa4add6f2859bdd8"></a>

### [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) → [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) FUN_00469c44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 120件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f17ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f1/005f17ac.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 120件 [`005ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005ed2b4.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005f17ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f1/005f17ec.md) [`005f3d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f3/005f3d1c.md) · 呼出先 2件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md#insn-00469c48) · [`00469c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md#insn-00469c58) · [`00469c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md#insn-00469c68)
- 新版 `00469c88`（命令位置の公開資料なし） · `00469c98`（命令位置の公開資料なし） · `00469ca8`（命令位置の公開資料なし）

~~~diff
- 00469c48 ["INT_ADD", "register:40f0:8", ["const:469c48:8", "const:4:8"]]
- 00469c48 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469c88 ["INT_ADD", "register:40f0:8", ["const:469c88:8", "const:4:8"]]
+ 00469c88 ["CALL", null, ["callee:00489f8c:8"]]
- 00469c48 bytes c1800094
+ 00469c88 bytes c1800094
- 00469c58 ["INT_ADD", "register:40f0:8", ["const:469c58:8", "const:4:8"]]
- 00469c58 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469c98 ["INT_ADD", "register:40f0:8", ["const:469c98:8", "const:4:8"]]
+ 00469c98 ["CALL", null, ["callee:00489f8c:8"]]
- 00469c58 bytes bd800094
+ 00469c98 bytes bd800094
- 00469c68 ["INT_ADD", "register:40f0:8", ["const:469c68:8", "const:4:8"]]
- 00469c68 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469ca8 ["INT_ADD", "register:40f0:8", ["const:469ca8:8", "const:4:8"]]
+ 00469ca8 ["CALL", null, ["callee:00489f8c:8"]]
- 00469c68 bytes b9800094
+ 00469ca8 bytes b9800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa36283bdc72799dcb6b136c63ce736a"></a>

### [`00469ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md) → [`00469d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469d0c.md) FUN_00469d0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 5件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) [`00a79c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79c74.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 2件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00469d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md#insn-00469d30) · [`00469d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md#insn-00469d40) · [`00469d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469ccc.md#insn-00469d58)
- 新版 `00469d70`（命令位置の公開資料なし） · `00469d80`（命令位置の公開資料なし） · `00469d98`（命令位置の公開資料なし）

~~~diff
- 00469d30 ["INT_ADD", "register:40f0:8", ["const:469d30:8", "const:4:8"]]
- 00469d30 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469d70 ["INT_ADD", "register:40f0:8", ["const:469d70:8", "const:4:8"]]
+ 00469d70 ["CALL", null, ["callee:00489f8c:8"]]
- 00469d30 bytes 87800094
+ 00469d70 bytes 87800094
- 00469d40 ["INT_ADD", "register:40f0:8", ["const:469d40:8", "const:4:8"]]
- 00469d40 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469d80 ["INT_ADD", "register:40f0:8", ["const:469d80:8", "const:4:8"]]
+ 00469d80 ["CALL", null, ["callee:00489f8c:8"]]
- 00469d40 bytes 83800094
+ 00469d80 bytes 83800094
- 00469d58 ["INT_ADD", "register:40f0:8", ["const:469d58:8", "const:4:8"]]
- 00469d58 ["CALL", null, ["callee:00489f8c:8"]]
+ 00469d98 ["INT_ADD", "register:40f0:8", ["const:469d98:8", "const:4:8"]]
+ 00469d98 ["CALL", null, ["callee:00489f8c:8"]]
- 00469d58 bytes 7d800094
+ 00469d98 bytes 7d800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c35f804070ae1cd856eb21221cbea17"></a>

### [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) → [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) FUN_0046a290

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 24件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) [`006122e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00612/006122e4.md) [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`006d4d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d4/006d4d94.md) · 呼出先 2件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 24件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005f3d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f3/005f3d1c.md) [`00612324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00612/00612324.md) [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) [`006d4dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md) · 呼出先 2件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md#insn-0046a290) · [`0046a2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md#insn-0046a2a0) · [`0046a2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md#insn-0046a2b0)
- 新版 `0046a2d0`（命令位置の公開資料なし） · `0046a2e0`（命令位置の公開資料なし） · `0046a2f0`（命令位置の公開資料なし）

~~~diff
- 0046a290 ["INT_ADD", "register:40f0:8", ["const:46a290:8", "const:4:8"]]
- 0046a290 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a2d0 ["INT_ADD", "register:40f0:8", ["const:46a2d0:8", "const:4:8"]]
+ 0046a2d0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046a290 bytes 2f7f0094
+ 0046a2d0 bytes 2f7f0094
- 0046a2a0 ["INT_ADD", "register:40f0:8", ["const:46a2a0:8", "const:4:8"]]
- 0046a2a0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a2e0 ["INT_ADD", "register:40f0:8", ["const:46a2e0:8", "const:4:8"]]
+ 0046a2e0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046a2a0 bytes 2b7f0094
+ 0046a2e0 bytes 2b7f0094
- 0046a2b0 ["INT_ADD", "register:40f0:8", ["const:46a2b0:8", "const:4:8"]]
- 0046a2b0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a2f0 ["INT_ADD", "register:40f0:8", ["const:46a2f0:8", "const:4:8"]]
+ 0046a2f0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046a2b0 bytes 277f0094
+ 0046a2f0 bytes 277f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1eb30f238e22e800fcc5e9029acadce"></a>

### [`0046a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md) → [`0046a34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a34c.md) FUN_0046a34c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`0072c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md) · 呼出先 2件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 3件 [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) [`0065d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md) [`0072c334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c334.md) · 呼出先 2件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md#insn-0046a358) · [`0046a368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md#insn-0046a368) · [`0046a37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a30c.md#insn-0046a37c)
- 新版 `0046a398`（命令位置の公開資料なし） · `0046a3a8`（命令位置の公開資料なし） · `0046a3bc`（命令位置の公開資料なし）

~~~diff
- 0046a358 ["INT_ADD", "register:40f0:8", ["const:46a358:8", "const:4:8"]]
- 0046a358 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a398 ["INT_ADD", "register:40f0:8", ["const:46a398:8", "const:4:8"]]
+ 0046a398 ["CALL", null, ["callee:00489f8c:8"]]
- 0046a358 bytes fd7e0094
+ 0046a398 bytes fd7e0094
- 0046a368 ["INT_ADD", "register:40f0:8", ["const:46a368:8", "const:4:8"]]
- 0046a368 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a3a8 ["INT_ADD", "register:40f0:8", ["const:46a3a8:8", "const:4:8"]]
+ 0046a3a8 ["CALL", null, ["callee:00489f8c:8"]]
- 0046a368 bytes f97e0094
+ 0046a3a8 bytes f97e0094
- 0046a37c ["INT_ADD", "register:40f0:8", ["const:46a37c:8", "const:4:8"]]
- 0046a37c ["CALL", null, ["callee:00489f8c:8"]]
+ 0046a3bc ["INT_ADD", "register:40f0:8", ["const:46a3bc:8", "const:4:8"]]
+ 0046a3bc ["CALL", null, ["callee:00489f8c:8"]]
- 0046a37c bytes f47e0094
+ 0046a3bc bytes f47e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb2233daf4018f62fb24bef6b93f86b"></a>

### [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) → [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) FUN_0046a928

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 24件 [`005e4074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4074.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`0069550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/0069550c.md) · 呼出先 3件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)
- 新版 呼出元 24件 [`005e40b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e40b4.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) [`0065d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md) [`00695564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695564.md) · 呼出先 3件 [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md#insn-0046a920) · [`0046a92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md#insn-0046a92c) · [`0046a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md#insn-0046a958)
- 新版 `0046a960`（命令位置の公開資料なし） · `0046a96c`（命令位置の公開資料なし） · `0046a998`（命令位置の公開資料なし）

~~~diff
- 0046a920 ["INT_ADD", "register:40f0:8", ["const:46a920:8", "const:4:8"]]
- 0046a920 ["CALL", null, ["callee:0048ab70:8"]]
+ 0046a960 ["INT_ADD", "register:40f0:8", ["const:46a960:8", "const:4:8"]]
+ 0046a960 ["CALL", null, ["callee:0048ab70:8"]]
- 0046a920 bytes 84800094
+ 0046a960 bytes 84800094
- 0046a92c ["INT_ADD", "register:40f0:8", ["const:46a92c:8", "const:4:8"]]
- 0046a92c ["CALL", null, ["callee:0048ab78:8"]]
+ 0046a96c ["INT_ADD", "register:40f0:8", ["const:46a96c:8", "const:4:8"]]
+ 0046a96c ["CALL", null, ["callee:0048ab78:8"]]
- 0046a92c bytes 83800094
+ 0046a96c bytes 83800094
- 0046a958 ["INT_ADD", "register:40f0:8", ["const:46a958:8", "const:4:8"]]
- 0046a958 ["CALL", null, ["callee:00468d48:8"]]
+ 0046a998 ["INT_ADD", "register:40f0:8", ["const:46a998:8", "const:4:8"]]
+ 0046a998 ["CALL", null, ["callee:00468d48:8"]]
- 0046a958 bytes ecf8ff97
+ 0046a998 bytes ecf8ff97
~~~


<a id="compare-b36c0a3a7224338d0845d61d5e2439e1"></a>

### [`0046a978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md) → [`0046a9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a9b8.md) FUN_0046a9b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 3件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)
- 新版 呼出元 6件 [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) [`0073ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073ee8c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) [`0099bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0099b/0099bac4.md) · 呼出先 3件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md#insn-0046a9ac) · [`0046a9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a978.md#insn-0046a9b8)
- 新版 `0046a9ec`（命令位置の公開資料なし） · `0046a9f8`（命令位置の公開資料なし）

~~~diff
- 0046a9ac ["INT_ADD", "register:40f0:8", ["const:46a9ac:8", "const:4:8"]]
- 0046a9ac ["CALL", null, ["callee:0048ab70:8"]]
+ 0046a9ec ["INT_ADD", "register:40f0:8", ["const:46a9ec:8", "const:4:8"]]
+ 0046a9ec ["CALL", null, ["callee:0048ab70:8"]]
- 0046a9ac bytes 61800094
+ 0046a9ec bytes 61800094
- 0046a9b8 ["INT_ADD", "register:40f0:8", ["const:46a9b8:8", "const:4:8"]]
- 0046a9b8 ["CALL", null, ["callee:0048ab78:8"]]
+ 0046a9f8 ["INT_ADD", "register:40f0:8", ["const:46a9f8:8", "const:4:8"]]
+ 0046a9f8 ["CALL", null, ["callee:0048ab78:8"]]
- 0046a9b8 bytes 60800094
+ 0046a9f8 bytes 60800094
~~~


<a id="compare-0d7357ebe0f360ad1005cdf7fe63991d"></a>

### [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) → [`0046aa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046aa3c.md) FUN_0046aa3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0046ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md) [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) [`00a473f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a473f4.md) · 呼出先 5件 [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0046ae74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ae74.md) [`0046b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b548.md) [`005fc3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fc/005fc3e0.md) [`00a47448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47448.md) · 呼出先 5件 [`0048b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b11c.md) [`0055a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a5e8.md) [`0055a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a63c.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046aa64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md#insn-0046aa64) · [`0046aaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md#insn-0046aaac) · [`0046aafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md#insn-0046aafc)
- 新版 `0046aaa4`（命令位置の公開資料なし） · `0046aaec`（命令位置の公開資料なし） · `0046ab3c`（命令位置の公開資料なし）

~~~diff
- 0046aa64 ["INT_ADD", "register:40f0:8", ["const:46aa64:8", "const:4:8"]]
- 0046aa64 ["CALL", null, ["callee:0055a5e8:8"]]
+ 0046aaa4 ["INT_ADD", "register:40f0:8", ["const:46aaa4:8", "const:4:8"]]
+ 0046aaa4 ["CALL", null, ["callee:0055a5e8:8"]]
- 0046aa64 bytes d1be0394
+ 0046aaa4 bytes d1be0394
- 0046aaac ["INT_ADD", "register:40f0:8", ["const:46aaac:8", "const:4:8"]]
- 0046aaac ["CALL", null, ["callee:0055cf8c:8"]]
+ 0046aaec ["INT_ADD", "register:40f0:8", ["const:46aaec:8", "const:4:8"]]
+ 0046aaec ["CALL", null, ["callee:0055cf8c:8"]]
- 0046aaac bytes 28c90394
+ 0046aaec bytes 28c90394
- 0046aafc ["INT_ADD", "register:40f0:8", ["const:46aafc:8", "const:4:8"]]
- 0046aafc ["CALL", null, ["callee:0048b11c:8"]]
+ 0046ab3c ["INT_ADD", "register:40f0:8", ["const:46ab3c:8", "const:4:8"]]
+ 0046ab3c ["CALL", null, ["callee:0048b11c:8"]]
- 0046aafc bytes 78810094
+ 0046ab3c bytes 78810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c698c70492899740137dc93b34f793e"></a>

### [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) → [`0046ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ab88.md) FUN_0046ab88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) · 呼出先 5件 [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0046b734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b734.md) · 呼出先 5件 [`0048b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b290.md) [`0055a5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a5e8.md) [`0055a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a63c.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046abc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md#insn-0046abc4) · [`0046ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md#insn-0046ac0c) · [`0046ac48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md#insn-0046ac48)
- 新版 `0046ac04`（命令位置の公開資料なし） · `0046ac4c`（命令位置の公開資料なし） · `0046ac88`（命令位置の公開資料なし）

~~~diff
- 0046abc4 ["INT_ADD", "register:40f0:8", ["const:46abc4:8", "const:4:8"]]
- 0046abc4 ["CALL", null, ["callee:0055a5e8:8"]]
+ 0046ac04 ["INT_ADD", "register:40f0:8", ["const:46ac04:8", "const:4:8"]]
+ 0046ac04 ["CALL", null, ["callee:0055a5e8:8"]]
- 0046abc4 bytes 79be0394
+ 0046ac04 bytes 79be0394
- 0046ac0c ["INT_ADD", "register:40f0:8", ["const:46ac0c:8", "const:4:8"]]
- 0046ac0c ["CALL", null, ["callee:0055cf8c:8"]]
+ 0046ac4c ["INT_ADD", "register:40f0:8", ["const:46ac4c:8", "const:4:8"]]
+ 0046ac4c ["CALL", null, ["callee:0055cf8c:8"]]
- 0046ac0c bytes d0c80394
+ 0046ac4c bytes d0c80394
- 0046ac48 ["INT_ADD", "register:40f0:8", ["const:46ac48:8", "const:4:8"]]
- 0046ac48 ["CALL", null, ["callee:0048b290:8"]]
+ 0046ac88 ["INT_ADD", "register:40f0:8", ["const:46ac88:8", "const:4:8"]]
+ 0046ac88 ["CALL", null, ["callee:0048b290:8"]]
- 0046ac48 bytes 82810094
+ 0046ac88 bytes 82810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f08dac422935b34101e1dd75576b961"></a>

### [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) → [`0046ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ace0.md) FUN_0046ace0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0046be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md) [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) · 呼出先 5件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00489f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f58.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md)
- 新版 呼出元 2件 [`0046beb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046beb8.md) [`0046e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e5c8.md) · 呼出先 5件 [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00489f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f98.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md) [`0048b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b11c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046acf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md#insn-0046acf8) · [`0046ad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md#insn-0046ad04) · [`0046ad48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md#insn-0046ad48)
- 新版 `0046ad38`（命令位置の公開資料なし） · `0046ad44`（命令位置の公開資料なし） · `0046ad88`（命令位置の公開資料なし）

~~~diff
- 0046acf8 ["INT_ADD", "register:40f0:8", ["const:46acf8:8", "const:4:8"]]
- 0046acf8 ["CALL", null, ["callee:0048ab70:8"]]
+ 0046ad38 ["INT_ADD", "register:40f0:8", ["const:46ad38:8", "const:4:8"]]
+ 0046ad38 ["CALL", null, ["callee:0048ab70:8"]]
- 0046acf8 bytes 8e7f0094
+ 0046ad38 bytes 8e7f0094
- 0046ad04 ["INT_ADD", "register:40f0:8", ["const:46ad04:8", "const:4:8"]]
- 0046ad04 ["CALL", null, ["callee:0048ab78:8"]]
+ 0046ad44 ["INT_ADD", "register:40f0:8", ["const:46ad44:8", "const:4:8"]]
+ 0046ad44 ["CALL", null, ["callee:0048ab78:8"]]
- 0046ad04 bytes 8d7f0094
+ 0046ad44 bytes 8d7f0094
- 0046ad48 ["INT_ADD", "register:40f0:8", ["const:46ad48:8", "const:4:8"]]
- 0046ad48 ["CALL", null, ["callee:0048b11c:8"]]
+ 0046ad88 ["INT_ADD", "register:40f0:8", ["const:46ad88:8", "const:4:8"]]
+ 0046ad88 ["CALL", null, ["callee:0048b11c:8"]]
- 0046ad48 bytes e5800094
+ 0046ad88 bytes e5800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9211ae6f6d31ec88c76bdb9fcdd378b"></a>

### [`0046ae34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md) → [`0046ae74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ae74.md) FUN_0046ae74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 2件 [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`005fc3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fc/005fc3e0.md) · 呼出先 2件 [`0046aa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046aa3c.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md#insn-0046ae80) · [`0046ae90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md#insn-0046ae90) · [`0046aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ae34.md#insn-0046aea0)
- 新版 `0046aec0`（命令位置の公開資料なし） · `0046aed0`（命令位置の公開資料なし） · `0046aee0`（命令位置の公開資料なし）

~~~diff
- 0046ae80 ["INT_ADD", "register:40f0:8", ["const:46ae80:8", "const:4:8"]]
- 0046ae80 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046aec0 ["INT_ADD", "register:40f0:8", ["const:46aec0:8", "const:4:8"]]
+ 0046aec0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046ae80 bytes 337c0094
+ 0046aec0 bytes 337c0094
- 0046ae90 ["INT_ADD", "register:40f0:8", ["const:46ae90:8", "const:4:8"]]
- 0046ae90 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046aed0 ["INT_ADD", "register:40f0:8", ["const:46aed0:8", "const:4:8"]]
+ 0046aed0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046ae90 bytes 2f7c0094
+ 0046aed0 bytes 2f7c0094
- 0046aea0 ["INT_ADD", "register:40f0:8", ["const:46aea0:8", "const:4:8"]]
- 0046aea0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046aee0 ["INT_ADD", "register:40f0:8", ["const:46aee0:8", "const:4:8"]]
+ 0046aee0 ["CALL", null, ["callee:00489f8c:8"]]
- 0046aea0 bytes 2b7c0094
+ 0046aee0 bytes 2b7c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9b218830940ebc22639eb15df14dd83"></a>

### [`0046af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md) → [`0046af60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af60.md) FUN_0046af60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 4件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046da44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da44.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 5件 [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md) [`008d38f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d38f0.md) [`0099bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0099b/0099bac4.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 4件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`0046da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da84.md) [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046af8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md#insn-0046af8c) · [`0046afcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md#insn-0046afcc) · [`0046aff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af20.md#insn-0046aff4)
- 新版 `0046afcc`（命令位置の公開資料なし） · `0046b00c`（命令位置の公開資料なし） · `0046b034`（命令位置の公開資料なし）

~~~diff
- 0046af8c ["INT_ADD", "register:40f0:8", ["const:46af8c:8", "const:4:8"]]
- 0046af8c ["CALL", null, ["callee:0046da9c:8"]]
+ 0046afcc ["INT_ADD", "register:40f0:8", ["const:46afcc:8", "const:4:8"]]
+ 0046afcc ["CALL", null, ["callee:0046da9c:8"]]
- 0046af8c bytes b40a0094
+ 0046afcc bytes b40a0094
- 0046afcc ["INT_ADD", "register:40f0:8", ["const:46afcc:8", "const:4:8"]]
- 0046afcc ["CALL", null, ["callee:0046da84:8"]]
+ 0046b00c ["INT_ADD", "register:40f0:8", ["const:46b00c:8", "const:4:8"]]
+ 0046b00c ["CALL", null, ["callee:0046da84:8"]]
- 0046afcc bytes 9e0a0094
+ 0046b00c bytes 9e0a0094
- 0046aff4 ["INT_ADD", "register:40f0:8", ["const:46aff4:8", "const:4:8"]]
- 0046aff4 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b034 ["INT_ADD", "register:40f0:8", ["const:46b034:8", "const:4:8"]]
+ 0046b034 ["CALL", null, ["callee:00489f8c:8"]]
- 0046aff4 bytes d67b0094
+ 0046b034 bytes d67b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aaa504ea5a5c0fb9f88e29aca29fa8b"></a>

### [`0046b1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b1dc.md) → [`0046b21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b21c.md) FUN_0046b21c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`008e3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e3/008e3d50.md) · 呼出先 3件 [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da90.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`008e3da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md) · 呼出先 3件 [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`0046dad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dad0.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b1dc.md#insn-0046b24c) · [`0046b31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b1dc.md#insn-0046b31c) · [`0046b37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b1dc.md#insn-0046b37c)
- 新版 `0046b28c`（命令位置の公開資料なし） · `0046b35c`（命令位置の公開資料なし） · `0046b3bc`（命令位置の公開資料なし）

~~~diff
- 0046b24c ["INT_ADD", "register:40f0:8", ["const:46b24c:8", "const:4:8"]]
- 0046b24c ["CALL", null, ["callee:0046dad0:8"]]
+ 0046b28c ["INT_ADD", "register:40f0:8", ["const:46b28c:8", "const:4:8"]]
+ 0046b28c ["CALL", null, ["callee:0046dad0:8"]]
- 0046b24c bytes 110a0094
+ 0046b28c bytes 110a0094
- 0046b31c ["INT_ADD", "register:40f0:8", ["const:46b31c:8", "const:4:8"]]
- 0046b31c ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b35c ["INT_ADD", "register:40f0:8", ["const:46b35c:8", "const:4:8"]]
+ 0046b35c ["CALL", null, ["callee:00489f8c:8"]]
- 0046b31c bytes 0c7b0094
+ 0046b35c bytes 0c7b0094
- 0046b37c ["INT_ADD", "register:40f0:8", ["const:46b37c:8", "const:4:8"]]
- 0046b37c ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b3bc ["INT_ADD", "register:40f0:8", ["const:46b3bc:8", "const:4:8"]]
+ 0046b3bc ["CALL", null, ["callee:00489f8c:8"]]
- 0046b37c bytes f47a0094
+ 0046b3bc bytes f47a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5923f6d70057b6497e1c1bceb5d00d76"></a>

### [`0046b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md) → [`0046b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b8c0.md) FUN_0046b8c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`007f71a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f7/007f71a4.md) [`007f8050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f8050.md) [`007f84cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f84cc.md) [`007f86b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f8/007f86b4.md) · 呼出先 2件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 7件 [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`007f71fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f7/007f71fc.md) [`007f80a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f80a8.md) [`007f8524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f8524.md) [`007f870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f8/007f870c.md) · 呼出先 2件 [`0046b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b548.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md#insn-0046b8cc) · [`0046b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md#insn-0046b8dc) · [`0046b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b880.md#insn-0046b8ec)
- 新版 `0046b90c`（命令位置の公開資料なし） · `0046b91c`（命令位置の公開資料なし） · `0046b92c`（命令位置の公開資料なし）

~~~diff
- 0046b8cc ["INT_ADD", "register:40f0:8", ["const:46b8cc:8", "const:4:8"]]
- 0046b8cc ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b90c ["INT_ADD", "register:40f0:8", ["const:46b90c:8", "const:4:8"]]
+ 0046b90c ["CALL", null, ["callee:00489f8c:8"]]
- 0046b8cc bytes a0790094
+ 0046b90c bytes a0790094
- 0046b8dc ["INT_ADD", "register:40f0:8", ["const:46b8dc:8", "const:4:8"]]
- 0046b8dc ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b91c ["INT_ADD", "register:40f0:8", ["const:46b91c:8", "const:4:8"]]
+ 0046b91c ["CALL", null, ["callee:00489f8c:8"]]
- 0046b8dc bytes 9c790094
+ 0046b91c bytes 9c790094
- 0046b8ec ["INT_ADD", "register:40f0:8", ["const:46b8ec:8", "const:4:8"]]
- 0046b8ec ["CALL", null, ["callee:00489f8c:8"]]
+ 0046b92c ["INT_ADD", "register:40f0:8", ["const:46b92c:8", "const:4:8"]]
+ 0046b92c ["CALL", null, ["callee:00489f8c:8"]]
- 0046b8ec bytes 98790094
+ 0046b92c bytes 98790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244dfdab8bd478c42d107eb05c9ec156"></a>

### [`0046b984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b984.md) → [`0046b9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b9c4.md) FUN_0046b9c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) · 呼出先 2件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`007fb288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb288.md) · 呼出先 2件 [`0046b734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b734.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046b9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b984.md#insn-0046b9dc) · [`0046b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b984.md#insn-0046b9f0) · [`0046ba04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b984.md#insn-0046ba04)
- 新版 `0046ba1c`（命令位置の公開資料なし） · `0046ba30`（命令位置の公開資料なし） · `0046ba44`（命令位置の公開資料なし）

~~~diff
- 0046b9dc ["INT_ADD", "register:40f0:8", ["const:46b9dc:8", "const:4:8"]]
- 0046b9dc ["CALL", null, ["callee:00489f8c:8"]]
+ 0046ba1c ["INT_ADD", "register:40f0:8", ["const:46ba1c:8", "const:4:8"]]
+ 0046ba1c ["CALL", null, ["callee:00489f8c:8"]]
- 0046b9dc bytes 5c790094
+ 0046ba1c bytes 5c790094
- 0046b9f0 ["INT_ADD", "register:40f0:8", ["const:46b9f0:8", "const:4:8"]]
- 0046b9f0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046ba30 ["INT_ADD", "register:40f0:8", ["const:46ba30:8", "const:4:8"]]
+ 0046ba30 ["CALL", null, ["callee:00489f8c:8"]]
- 0046b9f0 bytes 57790094
+ 0046ba30 bytes 57790094
- 0046ba04 ["INT_ADD", "register:40f0:8", ["const:46ba04:8", "const:4:8"]]
- 0046ba04 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046ba44 ["INT_ADD", "register:40f0:8", ["const:46ba44:8", "const:4:8"]]
+ 0046ba44 ["CALL", null, ["callee:00489f8c:8"]]
- 0046ba04 bytes 52790094
+ 0046ba44 bytes 52790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c5d33605b478de296c36840b1475e01"></a>

### [`0046baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046baa0.md) → [`0046bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bae0.md) FUN_0046bae0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) · 呼出先 3件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`0048ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab38.md)
- 新版 呼出元 2件 [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`00a79c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79c74.md) · 呼出先 3件 [`0046b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b548.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046baf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046baa0.md#insn-0046baf4) · [`0046bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046baa0.md#insn-0046bb00) · [`0046bb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046baa0.md#insn-0046bb40)
- 新版 `0046bb34`（命令位置の公開資料なし） · `0046bb40`（命令位置の公開資料なし） · `0046bb80`（命令位置の公開資料なし）

~~~diff
- 0046baf4 ["INT_ADD", "register:40f0:8", ["const:46baf4:8", "const:4:8"]]
- 0046baf4 ["CALL", null, ["callee:0048ab70:8"]]
+ 0046bb34 ["INT_ADD", "register:40f0:8", ["const:46bb34:8", "const:4:8"]]
+ 0046bb34 ["CALL", null, ["callee:0048ab70:8"]]
- 0046baf4 bytes 0f7c0094
+ 0046bb34 bytes 0f7c0094
- 0046bb00 ["INT_ADD", "register:40f0:8", ["const:46bb00:8", "const:4:8"]]
- 0046bb00 ["CALL", null, ["callee:0048ab78:8"]]
+ 0046bb40 ["INT_ADD", "register:40f0:8", ["const:46bb40:8", "const:4:8"]]
+ 0046bb40 ["CALL", null, ["callee:0048ab78:8"]]
- 0046bb00 bytes 0e7c0094
+ 0046bb40 bytes 0e7c0094
- 0046bb40 ["INT_ADD", "register:40f0:8", ["const:46bb40:8", "const:4:8"]]
- 0046bb40 ["CALL", null, ["callee:0046b548:8"]]
+ 0046bb80 ["INT_ADD", "register:40f0:8", ["const:46bb80:8", "const:4:8"]]
+ 0046bb80 ["CALL", null, ["callee:0046b548:8"]]
- 0046bb40 bytes 72feff97
+ 0046bb80 bytes 72feff97
~~~


<a id="compare-d3a811177d34d6c6b525c80cfeb65f68"></a>

### [`0046bb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md) → [`0046bba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bba8.md) FUN_0046bba8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`0046b508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b508.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 8件 [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005f3d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f3/005f3d1c.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`0046b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b548.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md#insn-0046bbc0) · [`0046bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md#insn-0046bbd0) · [`0046bbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md#insn-0046bbe0)
- 新版 `0046bc00`（命令位置の公開資料なし） · `0046bc10`（命令位置の公開資料なし） · `0046bc20`（命令位置の公開資料なし）

~~~diff
- 0046bbc0 ["INT_ADD", "register:40f0:8", ["const:46bbc0:8", "const:4:8"]]
- 0046bbc0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bc00 ["INT_ADD", "register:40f0:8", ["const:46bc00:8", "const:4:8"]]
+ 0046bc00 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bbc0 bytes e3780094
+ 0046bc00 bytes e3780094
- 0046bbd0 ["INT_ADD", "register:40f0:8", ["const:46bbd0:8", "const:4:8"]]
- 0046bbd0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bc10 ["INT_ADD", "register:40f0:8", ["const:46bc10:8", "const:4:8"]]
+ 0046bc10 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bbd0 bytes df780094
+ 0046bc10 bytes df780094
- 0046bbe0 ["INT_ADD", "register:40f0:8", ["const:46bbe0:8", "const:4:8"]]
- 0046bbe0 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bc20 ["INT_ADD", "register:40f0:8", ["const:46bc20:8", "const:4:8"]]
+ 0046bc20 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bbe0 bytes db780094
+ 0046bc20 bytes db780094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca5b5651a9c24023413665befc140241"></a>

### [`0046bc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bc58.md) → [`0046bc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bc98.md) FUN_0046bc98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005f3cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3cdc.md) · 呼出先 2件 [`0046b6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046b6f4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`005f3d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f3/005f3d1c.md) · 呼出先 2件 [`0046b734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046b734.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bc58.md#insn-0046bcb8) · [`0046bcc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bc58.md#insn-0046bcc8) · [`0046bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bc58.md#insn-0046bcd8)
- 新版 `0046bcf8`（命令位置の公開資料なし） · `0046bd08`（命令位置の公開資料なし） · `0046bd18`（命令位置の公開資料なし）

~~~diff
- 0046bcb8 ["INT_ADD", "register:40f0:8", ["const:46bcb8:8", "const:4:8"]]
- 0046bcb8 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bcf8 ["INT_ADD", "register:40f0:8", ["const:46bcf8:8", "const:4:8"]]
+ 0046bcf8 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bcb8 bytes a5780094
+ 0046bcf8 bytes a5780094
- 0046bcc8 ["INT_ADD", "register:40f0:8", ["const:46bcc8:8", "const:4:8"]]
- 0046bcc8 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bd08 ["INT_ADD", "register:40f0:8", ["const:46bd08:8", "const:4:8"]]
+ 0046bd08 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bcc8 bytes a1780094
+ 0046bd08 bytes a1780094
- 0046bcd8 ["INT_ADD", "register:40f0:8", ["const:46bcd8:8", "const:4:8"]]
- 0046bcd8 ["CALL", null, ["callee:00489f8c:8"]]
+ 0046bd18 ["INT_ADD", "register:40f0:8", ["const:46bd18:8", "const:4:8"]]
+ 0046bd18 ["CALL", null, ["callee:00489f8c:8"]]
- 0046bcd8 bytes 9d780094
+ 0046bd18 bytes 9d780094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a20e0a6953896212257c661163b28522"></a>

### [`0046bd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md) → [`0046bdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bdb4.md) FUN_0046bdb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) · 呼出先 3件 [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) · 呼出先 3件 [`0046e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e5c8.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md#insn-0046bdfc) · [`0046be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md#insn-0046be40) · [`0046be74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md#insn-0046be74)
- 新版 `0046be3c`（命令位置の公開資料なし） · `0046be80`（命令位置の公開資料なし） · `0046beb4`（命令位置の公開資料なし）

~~~diff
- 0046bdfc ["INT_ADD", "register:40f0:8", ["const:46bdfc:8", "const:4:8"]]
- 0046bdfc ["CALL", null, ["callee:0046e5c8:8"]]
+ 0046be3c ["INT_ADD", "register:40f0:8", ["const:46be3c:8", "const:4:8"]]
+ 0046be3c ["CALL", null, ["callee:0046e5c8:8"]]
- 0046bdfc bytes e3090094
+ 0046be3c bytes e3090094
- 0046be40 ["INT_ADD", "register:40f0:8", ["const:46be40:8", "const:4:8"]]
- 0046be40 ["CALL", null, ["callee:0055cf8c:8"]]
+ 0046be80 ["INT_ADD", "register:40f0:8", ["const:46be80:8", "const:4:8"]]
+ 0046be80 ["CALL", null, ["callee:0055cf8c:8"]]
- 0046be40 bytes 43c40394
+ 0046be80 bytes 43c40394
- 0046be74 ["INT_ADD", "register:40f0:8", ["const:46be74:8", "const:4:8"]]
- 0046be74 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0046beb4 ["INT_ADD", "register:40f0:8", ["const:46beb4:8", "const:4:8"]]
+ 0046beb4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0046be74 bytes 1bb01f94
+ 0046beb4 bytes 3fb01f94
~~~


<a id="compare-35c9c57945c9bdf01ddae2fb2e42a824"></a>

### [`0046be78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md) → [`0046beb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046beb8.md) FUN_0046beb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 3件 [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) [`0055cf4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) · 呼出先 3件 [`0046ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ace0.md) [`0055cf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md#insn-0046c018) · [`0046c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md#insn-0046c0e0) · [`0046c124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046be78.md#insn-0046c124)
- 新版 `0046c058`（命令位置の公開資料なし） · `0046c120`（命令位置の公開資料なし） · `0046c164`（命令位置の公開資料なし）

~~~diff
- 0046c018 ["INT_ADD", "register:40f0:8", ["const:46c018:8", "const:4:8"]]
- 0046c018 ["CALL", null, ["callee:0046ace0:8"]]
+ 0046c058 ["INT_ADD", "register:40f0:8", ["const:46c058:8", "const:4:8"]]
+ 0046c058 ["CALL", null, ["callee:0046ace0:8"]]
- 0046c018 bytes 22fbff97
+ 0046c058 bytes 22fbff97
- 0046c0e0 ["INT_ADD", "register:40f0:8", ["const:46c0e0:8", "const:4:8"]]
- 0046c0e0 ["CALL", null, ["callee:0055cf8c:8"]]
+ 0046c120 ["INT_ADD", "register:40f0:8", ["const:46c120:8", "const:4:8"]]
+ 0046c120 ["CALL", null, ["callee:0055cf8c:8"]]
- 0046c0e0 bytes 9bc30394
+ 0046c120 bytes 9bc30394
- 0046c124 ["INT_ADD", "register:40f0:8", ["const:46c124:8", "const:4:8"]]
- 0046c124 ["CALL", null, ["callee:0055cf8c:8"]]
+ 0046c164 ["INT_ADD", "register:40f0:8", ["const:46c164:8", "const:4:8"]]
+ 0046c164 ["CALL", null, ["callee:0055cf8c:8"]]
- 0046c124 bytes 8ac30394
+ 0046c164 bytes 8ac30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69588a7c80f04f7d13bdff44965613ed"></a>

### [`0046c168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c168.md) → [`0046c1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1a8.md) FUN_0046c1a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c168.md#insn-0046c184) · [`0046c1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c168.md#insn-0046c1a4)
- 新版 `0046c1c4`（命令位置の公開資料なし） · `0046c1e4`（命令位置の公開資料なし）

~~~diff
- 0046c184 ["INT_ADD", "register:40f0:8", ["const:46c184:8", "const:4:8"]]
- 0046c184 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046c1c4 ["INT_ADD", "register:40f0:8", ["const:46c1c4:8", "const:4:8"]]
+ 0046c1c4 ["CALL", null, ["callee:00c53da0:8"]]
- 0046c184 bytes df9e1f94
+ 0046c1c4 bytes f79e1f94
- 0046c1a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c1a4 ["INT_ADD", "register:40f0:8", ["const:46c1a4:8", "const:4:8"]]
- 0046c1a4 ["CALLIND", null, ["register:0:8"]]
+ 0046c1e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046c1e4 ["INT_ADD", "register:40f0:8", ["const:46c1e4:8", "const:4:8"]]
+ 0046c1e4 ["CALLIND", null, ["register:0:8"]]
- 0046c1a4 bytes 00013fd6
+ 0046c1e4 bytes 00013fd6
~~~


<a id="compare-46b192b53d4714f19e62682db3a69084"></a>

### [`0046c1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md) → [`0046c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c1f8.md) FUN_0046c1f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 4件 [`0048acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048acd0.md) [`0048af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048af18.md) [`0048b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b11c.md) [`0048b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b290.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md#insn-0046c1dc) · [`0046c1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md#insn-0046c1f4) · [`0046c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c1b8.md#insn-0046c218)
- 新版 `0046c21c`（命令位置の公開資料なし） · `0046c234`（命令位置の公開資料なし） · `0046c258`（命令位置の公開資料なし）

~~~diff
- 0046c1dc ["INT_ADD", "register:40f0:8", ["const:46c1dc:8", "const:4:8"]]
- 0046c1dc ["CALL", null, ["callee:00c53d70:8"]]
+ 0046c21c ["INT_ADD", "register:40f0:8", ["const:46c21c:8", "const:4:8"]]
+ 0046c21c ["CALL", null, ["callee:00c53d70:8"]]
- 0046c1dc bytes bd9e1f94
+ 0046c21c bytes d59e1f94
- 0046c1f4 ["INT_ADD", "register:40f0:8", ["const:46c1f4:8", "const:4:8"]]
- 0046c1f4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046c234 ["INT_ADD", "register:40f0:8", ["const:46c234:8", "const:4:8"]]
+ 0046c234 ["CALL", null, ["callee:00c53da0:8"]]
- 0046c1f4 bytes c39e1f94
+ 0046c234 bytes db9e1f94
- 0046c218 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c218 ["INT_ADD", "register:40f0:8", ["const:46c218:8", "const:4:8"]]
- 0046c218 ["CALLIND", null, ["register:0:8"]]
+ 0046c258 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046c258 ["INT_ADD", "register:40f0:8", ["const:46c258:8", "const:4:8"]]
+ 0046c258 ["CALLIND", null, ["register:0:8"]]
- 0046c218 bytes 00013fd6
+ 0046c258 bytes 00013fd6
~~~


<a id="compare-72ecf7ae5264031f91bb897ba22d20c1"></a>

### [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) → [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) FUN_0046c270

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`0048ac90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac90.md) [`0048aed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aed8.md) [`0048b0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b0dc.md) [`0048b250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b250.md) · 呼出先 5件 [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) [`0055cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cd80.md) [`0055cf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cf38.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0048acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048acd0.md) [`0048af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048af18.md) [`0048b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b11c.md) [`0048b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b290.md) · 呼出先 5件 [`0046c4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4b4.md) [`0055cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cdc0.md) [`0055cf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055cf78.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md#insn-0046c31c) · [`0046c334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md#insn-0046c334) · [`0046c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md#insn-0046c378)
- 新版 `0046c35c`（命令位置の公開資料なし） · `0046c374`（命令位置の公開資料なし） · `0046c3b8`（命令位置の公開資料なし）

~~~diff
- 0046c31c ["INT_ADD", "register:40f0:8", ["const:46c31c:8", "const:4:8"]]
- 0046c31c ["CALL", null, ["callee:0055cf78:8"]]
+ 0046c35c ["INT_ADD", "register:40f0:8", ["const:46c35c:8", "const:4:8"]]
+ 0046c35c ["CALL", null, ["callee:0055cf78:8"]]
- 0046c31c bytes 07c30394
+ 0046c35c bytes 07c30394
- 0046c334 ["INT_ADD", "register:40f0:8", ["const:46c334:8", "const:4:8"]]
- 0046c334 ["CALL", null, ["callee:0055cf78:8"]]
+ 0046c374 ["INT_ADD", "register:40f0:8", ["const:46c374:8", "const:4:8"]]
+ 0046c374 ["CALL", null, ["callee:0055cf78:8"]]
- 0046c334 bytes 01c30394
+ 0046c374 bytes 01c30394
- 0046c378 ["INT_ADD", "register:40f0:8", ["const:46c378:8", "const:4:8"]]
- 0046c378 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046c3b8 ["INT_ADD", "register:40f0:8", ["const:46c3b8:8", "const:4:8"]]
+ 0046c3b8 ["CALL", null, ["callee:00c53d70:8"]]
- 0046c378 bytes 569e1f94
+ 0046c3b8 bytes 6e9e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9caa74017cbf6921dc4463804666a0c4"></a>

### [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) → [`0046c4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4b4.md) FUN_0046c4b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c230.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0046c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c270.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046c654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c654.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md#insn-0046c4f0) · [`0046c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md#insn-0046c530) · [`0046c5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md#insn-0046c5ac)
- 新版 `0046c530`（命令位置の公開資料なし） · `0046c570`（命令位置の公開資料なし） · `0046c5ec`（命令位置の公開資料なし）

~~~diff
- 0046c4f0 ["INT_ADD", "register:40f0:8", ["const:46c4f0:8", "const:4:8"]]
- 0046c4f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0046c530 ["INT_ADD", "register:40f0:8", ["const:46c530:8", "const:4:8"]]
+ 0046c530 ["CALL", null, ["callee:00c57f60:8"]]
- 0046c4f0 bytes 68ae1f94
+ 0046c530 bytes 8cae1f94
- 0046c530 ["INT_ADD", "register:40f0:8", ["const:46c530:8", "const:4:8"]]
- 0046c530 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046c570 ["INT_ADD", "register:40f0:8", ["const:46c570:8", "const:4:8"]]
+ 0046c570 ["CALL", null, ["callee:00c53d70:8"]]
- 0046c530 bytes e89d1f94
+ 0046c570 bytes 009e1f94
- 0046c5ac ["INT_ADD", "register:40f0:8", ["const:46c5ac:8", "const:4:8"]]
- 0046c5ac ["CALL", null, ["callee:00c53da0:8"]]
+ 0046c5ec ["INT_ADD", "register:40f0:8", ["const:46c5ec:8", "const:4:8"]]
+ 0046c5ec ["CALL", null, ["callee:00c53da0:8"]]
- 0046c5ac bytes d59d1f94
+ 0046c5ec bytes ed9d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f104e8f62b51a88bf28e7267100848eb"></a>

### [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md) → [`0046d43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d43c.md) FUN_0046d43c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md)
- 新版 呼出元 1件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0046d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d6ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md#insn-0046d418)
- 新版 `0046d458`（命令位置の公開資料なし）

~~~diff
- 0046d418 ["INT_ADD", "register:40f0:8", ["const:46d418:8", "const:4:8"]]
- 0046d418 ["CALL", null, ["callee:0046d6ec:8"]]
+ 0046d458 ["INT_ADD", "register:40f0:8", ["const:46d458:8", "const:4:8"]]
+ 0046d458 ["CALL", null, ["callee:0046d6ec:8"]]
- 0046d418 bytes a5000094
+ 0046d458 bytes a5000094
~~~


<a id="compare-7c96083baabddea0c28ca1e826e3ba48"></a>

### [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) → [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) FUN_0046d4d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 129件 [`0046d118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d118.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`00493c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493c78.md) · 呼出先 2件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 129件 [`0046d158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d158.md) [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`00493cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cb8.md) · 呼出先 2件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md#insn-0046d4ac) · [`0046d4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md#insn-0046d4b8) · [`0046d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md#insn-0046d4c8)
- 新版 `0046d4ec`（命令位置の公開資料なし） · `0046d4f8`（命令位置の公開資料なし） · `0046d508`（命令位置の公開資料なし）

~~~diff
- 0046d4ac ["INT_ADD", "register:40f0:8", ["const:46d4ac:8", "const:4:8"]]
- 0046d4ac ["CALL", null, ["local:b0:8"]]
+ 0046d4ec ["INT_ADD", "register:40f0:8", ["const:46d4ec:8", "const:4:8"]]
+ 0046d4ec ["CALL", null, ["local:b0:8"]]
- 0046d4ac bytes f9ffff97
+ 0046d4ec bytes f9ffff97
- 0046d4b8 ["INT_ADD", "register:40f0:8", ["const:46d4b8:8", "const:4:8"]]
- 0046d4b8 ["CALL", null, ["local:b0:8"]]
+ 0046d4f8 ["INT_ADD", "register:40f0:8", ["const:46d4f8:8", "const:4:8"]]
+ 0046d4f8 ["CALL", null, ["local:b0:8"]]
- 0046d4b8 bytes f6ffff97
+ 0046d4f8 bytes f6ffff97
- 0046d4c8 ["INT_ADD", "register:40f0:8", ["const:46d4c8:8", "const:4:8"]]
- 0046d4c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0046d508 ["INT_ADD", "register:40f0:8", ["const:46d508:8", "const:4:8"]]
+ 0046d508 ["CALL", null, ["callee:00c57f80:8"]]
- 0046d4c8 bytes 7aaa1f94
+ 0046d508 bytes 9eaa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a285832edcfb4e3692a4afa4dfdfd483"></a>

### [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) → [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) FUN_0046d5e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 21件 [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`0054a7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a7e4.md) [`0054f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f194.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 21件 [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`00494cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) [`0054a824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a824.md) [`0054f1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054f/0054f1d4.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md#insn-0046d62c) · [`0046d658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md#insn-0046d658)
- 新版 `0046d66c`（命令位置の公開資料なし） · `0046d698`（命令位置の公開資料なし）

~~~diff
- 0046d62c ["INT_ADD", "register:40f0:8", ["const:46d62c:8", "const:4:8"]]
- 0046d62c ["CALL", null, ["callee:00c58120:8"]]
+ 0046d66c ["INT_ADD", "register:40f0:8", ["const:46d66c:8", "const:4:8"]]
+ 0046d66c ["CALL", null, ["callee:00c58120:8"]]
- 0046d62c bytes 89aa1f94
+ 0046d66c bytes adaa1f94
- 0046d658 ["INT_ADD", "register:40f0:8", ["const:46d658:8", "const:4:8"]]
- 0046d658 ["CALL", null, ["callee:00c58120:8"]]
+ 0046d698 ["INT_ADD", "register:40f0:8", ["const:46d698:8", "const:4:8"]]
+ 0046d698 ["CALL", null, ["callee:00c58120:8"]]
- 0046d658 bytes 7eaa1f94
+ 0046d698 bytes a2aa1f94
~~~


<a id="compare-d05abc4cdc77f8e448a0b8cb66573d01"></a>

### [`0046d6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md) → [`0046d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d6ec.md) FUN_0046d6ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0046d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d3fc.md) [`00864910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) [`0088f2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f2f4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 3件 [`0046d43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d43c.md) [`00864968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) [`0088f34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046d718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md#insn-0046d718) · [`0046d774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md#insn-0046d774)
- 新版 `0046d758`（命令位置の公開資料なし） · `0046d7b4`（命令位置の公開資料なし）

~~~diff
- 0046d718 ["INT_ADD", "register:40f0:8", ["const:46d718:8", "const:4:8"]]
- 0046d718 ["CALL", null, ["callee:00c58120:8"]]
+ 0046d758 ["INT_ADD", "register:40f0:8", ["const:46d758:8", "const:4:8"]]
+ 0046d758 ["CALL", null, ["callee:00c58120:8"]]
- 0046d718 bytes 4eaa1f94
+ 0046d758 bytes 72aa1f94
- 0046d774 ["INT_ADD", "register:40f0:8", ["const:46d774:8", "const:4:8"]]
- 0046d774 ["CALL", null, ["callee:00c58120:8"]]
+ 0046d7b4 ["INT_ADD", "register:40f0:8", ["const:46d7b4:8", "const:4:8"]]
+ 0046d7b4 ["CALL", null, ["callee:00c58120:8"]]
- 0046d774 bytes 37aa1f94
+ 0046d7b4 bytes 5baa1f94
~~~


<a id="compare-f26dd2ab633a0ebf40ad64bfe458569c"></a>

### [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) → [`0046de64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046de64.md) FUN_0046de64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) · 呼出先 12件 [`00467650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md) [`004676a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004676a0.md) [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) [`004677e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004677e0.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)
- 新版 呼出元 1件 [`0046f79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f79c.md) · 呼出先 12件 [`00467690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467690.md) [`004676e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676e0.md) [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) [`00467820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467820.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046dfb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md#insn-0046dfb4) · [`0046dfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md#insn-0046dfc0) · [`0046dfe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md#insn-0046dfe4)
- 新版 `0046dff4`（命令位置の公開資料なし） · `0046e000`（命令位置の公開資料なし） · `0046e024`（命令位置の公開資料なし）

~~~diff
- 0046dfb4 ["INT_ADD", "register:40f0:8", ["const:46dfb4:8", "const:4:8"]]
- 0046dfb4 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046dff4 ["INT_ADD", "register:40f0:8", ["const:46dff4:8", "const:4:8"]]
+ 0046dff4 ["CALL", null, ["callee:00c53d70:8"]]
- 0046dfb4 bytes 47971f94
+ 0046dff4 bytes 5f971f94
- 0046dfc0 ["INT_ADD", "register:40f0:8", ["const:46dfc0:8", "const:4:8"]]
- 0046dfc0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046e000 ["INT_ADD", "register:40f0:8", ["const:46e000:8", "const:4:8"]]
+ 0046e000 ["CALL", null, ["callee:00c53da0:8"]]
- 0046dfc0 bytes 50971f94
+ 0046e000 bytes 68971f94
- 0046dfe4 ["INT_ADD", "register:40f0:8", ["const:46dfe4:8", "const:4:8"]]
- 0046dfe4 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046e024 ["INT_ADD", "register:40f0:8", ["const:46e024:8", "const:4:8"]]
+ 0046e024 ["CALL", null, ["callee:00c53d70:8"]]
- 0046dfe4 bytes 3b971f94
+ 0046e024 bytes 53971f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed726a59e8da82a285366a05d27c117"></a>

### [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) → [`0046e578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e578.md) FUN_0046e578

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 30件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 30件 [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005ef5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ef/005ef5ec.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md#insn-0046e554) · [`0046e574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md#insn-0046e574)
- 新版 `0046e594`（命令位置の公開資料なし） · `0046e5b4`（命令位置の公開資料なし）

~~~diff
- 0046e554 ["INT_ADD", "register:40f0:8", ["const:46e554:8", "const:4:8"]]
- 0046e554 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046e594 ["INT_ADD", "register:40f0:8", ["const:46e594:8", "const:4:8"]]
+ 0046e594 ["CALL", null, ["callee:00c53da0:8"]]
- 0046e554 bytes eb951f94
+ 0046e594 bytes 03961f94
- 0046e574 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046e574 ["INT_ADD", "register:40f0:8", ["const:46e574:8", "const:4:8"]]
- 0046e574 ["CALLIND", null, ["register:0:8"]]
+ 0046e5b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046e5b4 ["INT_ADD", "register:40f0:8", ["const:46e5b4:8", "const:4:8"]]
+ 0046e5b4 ["CALLIND", null, ["register:0:8"]]
- 0046e574 bytes 00013fd6
+ 0046e5b4 bytes 00013fd6
~~~


<a id="compare-89ca1cae9974b96baa8965fda96fa354"></a>

### [`0046e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md) → [`0046e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e5c8.md) FUN_0046e5c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046bd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd74.md) · 呼出先 7件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`0046aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046aca0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`0046bdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bdb4.md) · 呼出先 7件 [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`0046ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046ace0.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md#insn-0046e5e4) · [`0046e604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md#insn-0046e604) · [`0046e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e588.md#insn-0046e624)
- 新版 `0046e624`（命令位置の公開資料なし） · `0046e644`（命令位置の公開資料なし） · `0046e664`（命令位置の公開資料なし）

~~~diff
- 0046e5e4 ["INT_ADD", "register:40f0:8", ["const:46e5e4:8", "const:4:8"]]
- 0046e5e4 ["CALL", null, ["callee:00467b30:8"]]
+ 0046e624 ["INT_ADD", "register:40f0:8", ["const:46e624:8", "const:4:8"]]
+ 0046e624 ["CALL", null, ["callee:00467b30:8"]]
- 0046e5e4 bytes 43e5ff97
+ 0046e624 bytes 43e5ff97
- 0046e604 ["INT_ADD", "register:40f0:8", ["const:46e604:8", "const:4:8"]]
- 0046e604 ["CALL", null, ["callee:00468c1c:8"]]
+ 0046e644 ["INT_ADD", "register:40f0:8", ["const:46e644:8", "const:4:8"]]
+ 0046e644 ["CALL", null, ["callee:00468c1c:8"]]
- 0046e604 bytes 76e9ff97
+ 0046e644 bytes 76e9ff97
- 0046e624 ["INT_ADD", "register:40f0:8", ["const:46e624:8", "const:4:8"]]
- 0046e624 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046e664 ["INT_ADD", "register:40f0:8", ["const:46e664:8", "const:4:8"]]
+ 0046e664 ["CALL", null, ["callee:00c53d70:8"]]
- 0046e624 bytes ab951f94
+ 0046e664 bytes c3951f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f404947107fcfba35d9474d73f9c8267"></a>

### [`0046e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e82c.md) → [`0046e86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e86c.md) FUN_0046e86c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e82c.md#insn-0046e874)
- 新版 `0046e8b4`（命令位置の公開資料なし）

~~~diff
- 0046e874 ["INT_ADD", "register:40f0:8", ["const:46e874:8", "const:4:8"]]
- 0046e874 ["CALL", null, ["callee:00c57f80:8"]]
+ 0046e8b4 ["INT_ADD", "register:40f0:8", ["const:46e8b4:8", "const:4:8"]]
+ 0046e8b4 ["CALL", null, ["callee:00c57f80:8"]]
- 0046e874 bytes 8fa51f94
+ 0046e8b4 bytes b3a51f94
~~~


<a id="compare-45820ebc0fa8b431aab009b20b0979f7"></a>

### [`0046f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md) → [`0046f6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f6ac.md) FUN_0046f6ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`006dc940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc940.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 13件 [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005ef5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ef/005ef5ec.md) [`006dc998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc998.md) [`0078c274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078c/0078c274.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046f690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md#insn-0046f690) · [`0046f6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md#insn-0046f6a8) · [`0046f6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md#insn-0046f6cc)
- 新版 `0046f6d0`（命令位置の公開資料なし） · `0046f6e8`（命令位置の公開資料なし） · `0046f70c`（命令位置の公開資料なし）

~~~diff
- 0046f690 ["INT_ADD", "register:40f0:8", ["const:46f690:8", "const:4:8"]]
- 0046f690 ["CALL", null, ["callee:00c53d70:8"]]
+ 0046f6d0 ["INT_ADD", "register:40f0:8", ["const:46f6d0:8", "const:4:8"]]
+ 0046f6d0 ["CALL", null, ["callee:00c53d70:8"]]
- 0046f690 bytes 90911f94
+ 0046f6d0 bytes a8911f94
- 0046f6a8 ["INT_ADD", "register:40f0:8", ["const:46f6a8:8", "const:4:8"]]
- 0046f6a8 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046f6e8 ["INT_ADD", "register:40f0:8", ["const:46f6e8:8", "const:4:8"]]
+ 0046f6e8 ["CALL", null, ["callee:00c53da0:8"]]
- 0046f6a8 bytes 96911f94
+ 0046f6e8 bytes ae911f94
- 0046f6cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f6cc ["INT_ADD", "register:40f0:8", ["const:46f6cc:8", "const:4:8"]]
- 0046f6cc ["CALLIND", null, ["register:0:8"]]
+ 0046f70c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046f70c ["INT_ADD", "register:40f0:8", ["const:46f70c:8", "const:4:8"]]
+ 0046f70c ["CALLIND", null, ["register:0:8"]]
- 0046f6cc bytes 00013fd6
+ 0046f70c bytes 00013fd6
~~~


<a id="compare-871b296a14bb1d09ce9b33d7205d15c8"></a>

### [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md) → [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md) FUN_0046f724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 31件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005eda7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005eda7c.md) [`005ee5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ee/005ee5d0.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 31件 [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`005edabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005edabc.md) [`005ee610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ee/005ee610.md) [`005ef5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ef/005ef5ec.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0046f710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md#insn-0046f710) · [`0046f724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md#insn-0046f724) · [`0046f72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md#insn-0046f72c)
- 新版 `0046f750`（命令位置の公開資料なし） · `0046f764`（命令位置の公開資料なし） · `0046f76c`（命令位置の公開資料なし）

~~~diff
- 0046f710 ["INT_ADD", "register:40f0:8", ["const:46f710:8", "const:4:8"]]
- 0046f710 ["CALL", null, ["callee:00c53da0:8"]]
+ 0046f750 ["INT_ADD", "register:40f0:8", ["const:46f750:8", "const:4:8"]]
+ 0046f750 ["CALL", null, ["callee:00c53da0:8"]]
- 0046f710 bytes 7c911f94
+ 0046f750 bytes 94911f94
- 0046f724 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f724 ["INT_ADD", "register:40f0:8", ["const:46f724:8", "const:4:8"]]
- 0046f724 ["CALLIND", null, ["register:0:8"]]
+ 0046f764 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046f764 ["INT_ADD", "register:40f0:8", ["const:46f764:8", "const:4:8"]]
+ 0046f764 ["CALLIND", null, ["register:0:8"]]
- 0046f724 bytes 00013fd6
+ 0046f764 bytes 00013fd6
- 0046f72c ["INT_ADD", "register:40f0:8", ["const:46f72c:8", "const:4:8"]]
- 0046f72c ["CALL", null, ["callee:00c57f50:8"]]
+ 0046f76c ["INT_ADD", "register:40f0:8", ["const:46f76c:8", "const:4:8"]]
+ 0046f76c ["CALL", null, ["callee:00c57f50:8"]]
- 0046f72c bytes d5a11f94
+ 0046f76c bytes f9a11f94
~~~


